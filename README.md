What is this?
============

If:

  * you've got a script that could be useful to Ubuntu developers
  * it's reasonable quality
  * you're too lazy to submit it to [`ubuntu-dev-tools`](https://git.launchpad.net/ubuntu-dev-tools)

then you've come to the right place.

What's in here?
==============

`make-sru-tasks`
----------------

Give it Launchpad bug numbers. It'll set all of the (development) tasks to the
status you give it, create stable release tasks for the releases you specify,
set them to the given status (e.g. In Progress for an SRU you're about to
upload), and assign them to you. (Or someone else.)
