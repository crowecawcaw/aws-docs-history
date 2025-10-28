# Typical use cases

## Use case 1

An event is designed to process live feed from a specific
source. The input does not include ad markers.

You create a dynamic playlist in the event to process the live
input. Then, at a given time, process one or more file inputs
(the ad content). After that, switch back to the live input,
either at a given time or when the last ad content has been
processed. The dynamic playlist consists of the single live
input “interrupted” periodically by ad content.

## Use case 2

An event is designed to process live feed from a specific
source. Periodically, the live feed should be replaced by file
content (perhaps a movie). Then the same live feed should be
resumed.

## Use case 3

An event is designed to process live feed from a specific
source. However, you may need to cut away from the live feed to
process a file input. This cutaway file may be planned: For
example, you may have a “broadcasting will resume shortly”
message already prepared). Alternatively, the cutaway file may
be something that is created on the spot to convey an
unanticipated public announcement.

You create an event to process the live input. You then either
create a dynamic playlist ahead of time to switch to a special
file input, if necessary. Or at the last minute you create the
entire dynamic playlist and its input, and then switch to it
immediately.

## Use case 4

An event is designed to process live feed from a specific
source. Another event is designed to process live feed from a
different source.

Before the dynamic playlist feature was introduced, you could
only switch to the other live feed by stopping one event and
starting the other. Now, you can merge these two events into one
event, with each live feed in the dynamic playlist. You can set
up the dynamic playlist to switch from one feed to another
either at a scheduled time, or when the operator interrupts.

## Use case 5

An event is designed to process file inputs, one after the
other, without the event ending.

Before the dynamic playlist feature was introduced, you could
add inputs to the event, but only one at a time. Now, you can
add as many inputs as you want in one command.

In a variation of this use case, the event may contain only
two files. The event can be set up so that as soon as one input
ends, the next one starts over again, but with different content
specified inside that input.

## Use case 6

An event is designed to process file content (perhaps a
movie). Periodically, the file content should be replaced by
different file content that contains ad content. Then the
original file content should be resumed.

You create a dynamic playlist in the event that interleaves
sections of the movie with ad content, so: movie, ad content,
movie, ad content, movie, and so on. All the inputs are file
inputs.

Each time you add the movie file as an input, you include the
input clipping tags to create a clip out of a different segment
of the movie: 0 to 20 minutes, 20 to 25 minutes, 25 to 40
minutes, and so on. Each time that the movie resumes, it will
resume at the desired point.
