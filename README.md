List all your Github repositories containing a filename matching a search
pattern.

`ghgrep` is partially `grep -l` and partially `find -name` - you can pretend it
is a special version of `grep(1)` in which files are actually repositories and
each line of a file is actually a filename inside the repository.

# Examples

Show all repositories with a readme:

    ghgrep 'README.*'

List all repositories that have a file named 'COPYING':

    ghgrep -f COPYING

List all repositories that don't have a license file:

    ghgrep -v (COPYING|LICENSE)

# Installation

    [$]> pip install ghgrep

or

    [$]> easy_install ghgrep

# Caveats

`ghgrep` will fail if you have any repositories without a branch named
'master'.  This is due to [a bug] in an upstream dependency.

[a bug]: https://github.com/sigmavirus24/github3.py/pull/102

# Hacking

I highly recommend using virtualenv:

    [$]> virtualenv --no-site-packages --distribute env
    [$]> source env/bin/activate
    [$]> pip install -r requirements.txt
    [$]> pip install -e . # So we can import the version from inside bin/ .

