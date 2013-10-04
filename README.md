# routelog

routelog is a flexible execution-based log processing program and Domain
Specific Language. routelog takes a rules file in the following format:

    /pattern/    command $1 $2

And operates on one or more log files, executing `command $1 $2` for all lines
matching the regular expression `/pattern/` substituting the first and second
items in the log line for `$1` and `$2` respectively. A rules file with the
following directive:

    /ERROR/      echo "$*" | mail -s "Error executing ${3%:} on $2 at $1" error@example.com

Would process a log entry like:

    2012-12-07T12:06:11-05:00 server1 program_name: ERROR foo

and send an email to error@example.com with the subject:

    Error executing program_name on server1 at 2012-12-07T12:06:11-05:00'

and the body

    2012-12-07T12:06:11-05:00 server1 program_name: ERROR foo

For more on rules files, see `man 5 routelog`, for more on routelog see
`man 1 routelog`.

### Install

    sudo python setup.py install

### Usage

    routelog [-h|--help] [-c|--comments] [-n|--no-output] rules_file [ log_file [...]]
    optional arguments:
        -h, --help
            Print an extended usage to stdout
        -c, --comments
            Treat comments in log lines (anything following a ' #') as arguments,
            rather than ignoring them.
        -n, --no-output
            Suppress the (default) behavior of printing each log line to stdout.

### License

routelog is made available for use under a 3-clause BSD license (see: [LICENSE.txt](./LICENSE.txt)).

### Authors

Matthew Story (matt.story@axial.net)
