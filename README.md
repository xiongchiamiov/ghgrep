List all your Github repositories containing a filename matching a search
pattern.

`ghgrep` is partially `grep -l` and partially `find -name` - you can pretend it
is a special version of `grep(1)` in which files are actually repositories and
each line of a file is actually a filename inside the repository.

# Examples

`ghgrep` is still in development; don't expect it to actually do these things
yet.

Show all repositories with a readme:

    ghgrep 'README(.*)'

List all repositories that have a file named 'COPYING':

    ghgrep -F COPYING

List all repositories that don't have a license file:

    ghgrep -v (COPYING|LICENSE)

# Installation

    [$]> pip install ghgrep

or

    [$]> easy_install ghgrep

# Hacking

I highly recommend using virtualenv:

    [$]> virtualenv --no-site-packages --distribute env
    [$]> source env/bin/activate
    [$]> pip install -r requirements.txt
    [$]> pip install -e . # So we can import the version from inside bin/ .

