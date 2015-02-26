import argparse
import random
import time
import sys

parser = argparse.ArgumentParser('eligibility')
parser.add_argument('in_file', \
         help='the file containing the list of names to randomly sort')
parser.add_argument('-s', metavar='spots', required=True, type=int, \
         help='the number of spots available on campus')
parser.add_argument('out_file', \
         help='the file to output the results to')
parser.add_argument('-d', metavar='delay', required=False, type=float, \
         default=0.5, help='the delay between selections in decimal seconds')

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
    print MCM_CREST
    print 'Welcome to McMurtry College Eligibility Jack.'
    print 'This program will randomly allocate ' + str(spots) \
            + ' spots for housing.'
    print 'Hit any key to begin...'
    raw_input('')

def run_eligibility(names_file, spots, delay=0.5):
    on_campus = []
    waitlist = []

    with open(names_file, 'r') as names_f:
        lines = names_f.readlines();
        names = map(lambda l: l.rstrip('\n'), lines);

        if spots > len(names):
            print >> sys.stderr, 'Number of spots greater than names list. ' + \
                    'No need for eligibility jack.'
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

    return on_campus, waitlist

def write_results(out_file, on_campus, waitlist):
    with open(out_file, 'w') as out_f:
        out_f.write('Receiving on campus housing:\n')

        for name_i in xrange(len(on_campus)):
            out_f.write(str(name_i + 1) + ': ' + on_campus[name_i] + '\n')

        out_f.write('\nHousing Waitlist:\n')

        for name_i in xrange(len(waitlist)):
            out_f.write(str(name_i + 1) + ': ' + waitlist[name_i] + '\n')

if __name__ == '__main__':
    args = parser.parse_args();

    welcome(args.s)
    oc, wl = run_eligibility(args.in_file, args.s)

    write_results(args.out_file, oc, wl)
