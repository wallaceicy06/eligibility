Eligibility
===========

A program to randomly allocate students for on-campus housing.

Description
-----------

This program randomly allocates a specific number of students for housing
and places the remaining number onto an ordered wait list. It is designed
specifically to serve [McMurtry College](http://mcmurtry.rice.edu) at Rice
University.

Usage
-----

Provide a plain text file of names, each separated by a line feed. Determine
the number of spots for on-campus housing that you have, and execute

    eligibility namefile outfile -s numspots

where `namefile` is your plain text file of names, `outfile` is the file you
want the results written to, and `numspots` is the number of spots for on-campus
housing.

To adjust the seconds between random choices, use the `-d` flag and pass a
decimal number. By default, the delay is set at 0.5 seconds.

A list of command line options is also provided by passing the `-h` flag.

Sample
------

A sample names file `sample_names.txt` is provided as part of this package. To
try the program out of the box, execute

    eligibility sample_names.txt sample_out.txt -s 3

Credits
-------

This program is based on a similar program written by Kevin Lin (Rice '13).
The respository for that project is located
[here](https://github.com/kevinslin/eligibility_jack).
