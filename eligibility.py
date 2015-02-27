import argparse
import random
import time
import sys

parser = argparse.ArgumentParser('eligibility')
parser.add_argument('infile', \
         help='the file containing the list of names to randomly sort')
parser.add_argument('-s', '--spots', metavar='num', required=True, type=int, \
         help='the number of spots available on campus')
parser.add_argument('outfile', \
         help='the file to output the results to')
parser.add_argument('-d', '--delay', metavar='seconds', required=False, \
         type=float, default=0.5, help='the delay between selections in '
         'decimal seconds (0.5 by default)')

MCM_CREST = """
   `/:.                                            .:+.
    `///.           McMURTRY COLLEGE             .///. ``
      .///.                                    .///- ``
        -///.        .-:////+ooo+/:-.        .///-```
          -///.  .:oyhhdyyddshydhydhhyo:.  .///-````
           `-/++sydyysddshhdsshddoyddddhys++/-````
            `/hhhsyhsyhddyyyhhysshdddhsdhdhh/```
           .shdssyohhhyo//+////+//+yhhhyyosyys-
          :yyyyy   . +    /+sssyo     .   yyyhy:
         :hhsyh    .sdho:+sdddddm+ os .    hhhhh:
        .hdsyyh    `oddyoyymdmmdds ydd/``-:hyhhdy.
        ohhdhhd    `.:ddmdddddddd- + o-.   hdssyy/
       `hdhyyhh     -`-ymmmddddms..s--     hdhhhdh.
       -hdyhydh     /o:/mdmdmmdy:  :h+     hyyyhhh:
       -hdshydd    /ymddhhhoydhohy/:+h     dhyyyhh:
       `hdsyyddo    /s+o-+hhhdmddddooy    +ddysydh.
        sdhhhddh/      ` +ddd+sdddy/+/    yddhyyh+`
        .hdhyyyyys:  .oyoydddo-+ddhs/.   +ydddhyy-
         +hsyhhddho` :yhodoo+yssddds.   sddyyyhh/
         +yyddhhdddy.`.-:/::+ymdhs:`` +hddhyhyy/
      :-``/shddddddddyo+/+oso+s++ooosdddhyhddy:```-:
      -oo::/+shdddddddddddddddddhdddddhyhdhyo///:+o:
       `sdhs-``/ydddhdddddddhhddddddhyhdhs:``-ohds.-.
     `+hdy:+o-  `:ohhddddddddddddddyhhho.   -o+:yho+.`
   `:hdy:   -o.     -/oyhdddddddhyso:.     `o-   :ydh:`
 `oyds-                 :hydddhoy:                 -omyo.
 -yh+                   -yyhs:+yy:                   +hh-
                         sys///ss`
                         `+osso+`
"""

def welcome(spots):
    """
    Prints the McMurtry crest to stdout. Returns when the user confirms the
    start of the program by typing any key.

    Arguments:
        spots - the number of spots that the program will allocate for housing

    Returns:
        none
    """

    print MCM_CREST
    print 'Welcome to McMurtry College Eligibility Jack.'
    print 'This program will randomly allocate ' + str(spots) \
            + ' spots for housing.'
    print 'Hit any key to begin...'
    raw_input('')

def run_eligibility(names_file, spots, delay=0.5):
    """
    Randomly sorts the provided names into two lists, one that is receiving
    housing and another that is a housing wait list. The number of spots for
    the former is determined by the variable passed to the function.

    Arguments:
        names_file - the path of the file containing a line separated list of
            names
        spots - the number of spots to allocate for housing
        delay (optional) - the delay between successive picks, default is 0.5

    Returns:
        the list of students who were picked for on campus housing;
        the list of students (in order) who were picked to be on the wait list
    """

    on_campus = []
    waitlist = []

    try:
        with open(names_file, 'r') as names_f:
            lines = names_f.readlines();
            names = map(lambda l: l.rstrip('\n'), lines);

            if spots > len(names):
                print >> sys.stderr, 'Number of spots greater than names ' + \
                        'list. No need for eligibility jack.'
                sys.exit(-1)

            print 'Receiving on campus housing:\n'

            num = 1
            while names:
                name = random.choice(names)
                names.remove(name)

                time.sleep(delay)

                if num > spots:
                    print str(num - spots) + ': ' + name
                    waitlist.append(name)
                else:
                    print str(num) + ': ' + name
                    on_campus.append(name)

                if num == spots:
                    print '\nHousing Waitlist:\n'

                num += 1
    except IOError:
        print >> sys.stderr, 'There was an error opening the specified' + \
                ' file \'' + names_file +'\' for read.'

    return on_campus, waitlist

def write_results(out_file, on_campus, waitlist):
    """
    Writes the specified lists of students to a file in the same format that
    run_eligibility prints to stdout.

    Arguments:
        out_file - the path of the file to write the results to
        on_campus - the list of students selected for on-campus housing
        waitlist - the list of students (in order) who were selected for the
            wait list

    Returns:
        none
    """

    try:
        with open(out_file, 'w') as out_f:
            out_f.write('Receiving on campus housing:\n')

            for name_i in xrange(len(on_campus)):
                out_f.write(str(name_i + 1) + ': ' + on_campus[name_i] + '\n')

            out_f.write('\nHousing Waitlist:\n')

            for name_i in xrange(len(waitlist)):
                out_f.write(str(name_i + 1) + ': ' + waitlist[name_i] + '\n')
    except IOError:
        print >> sys.stderr, 'There was an error opening the specified' + \
                ' file \'' + out_file +'\' for write.'

# Main runner for the program.
if __name__ == '__main__':
    args = parser.parse_args();

    welcome(args.spots)
    oc, wl = run_eligibility(args.infile, args.spots, args.delay)

    write_results(args.outfile, oc, wl)
