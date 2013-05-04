Search through your Github repositories.

# Examples

Show all repositories with a readme:

    ghgrep 'README(.*)'

List all repositories that have a file named 'COPYING':

    ghgrep -F COPYING

List all repositories that don't have a license file:

    ghgrep -v (COPYING|LICENSE)

