# Designing the

segmentModifier

Design the segmentModifiers portion of the destination path. The
segmentModifier is optional, and if you include it, only the media file
names include it.

A typical use case for this modifier is to use a data variable to
create a timestamp, to prevent segments overriding each other if the
channel restarts. For example, assume that you include the timestamp
`$t$-`. Segment 00001 might have the name
`index-120028-00001`. If the output restarts a
few minutes later (which causes the segment counter to restart), the new
segment 00001 will have the name
`index-120039-00001`. The new file won't overwrite
the file for the original segment 00001. Some downstream systems might
prefer this behavior.
