Search through your Github repositories.

# Examples

    ghgrep 'README(.*)'

Show all repositories with a readme.

    ghgrep -F COPYING

List all repositories that have a file named 'COPYING'.

    ghgrep -v (COPYING|LICENSE)

List all repositories that don't have a license file.

