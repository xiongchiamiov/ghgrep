List all your Github repositories containing a filename matching a search
pattern.

`ghgrep` is partially `grep -l` and partially `find -name` - you can pretend it
is a special version of `grep(1)` in which files are actually repositories and
each line of a file is actually a filename inside the repository.

# Examples

Show all repositories with a readme:

    ghgrep 'README(.*)'

List all repositories that have a file named 'COPYING':

    ghgrep -F COPYING

List all repositories that don't have a license file:

    ghgrep -v (COPYING|LICENSE)

