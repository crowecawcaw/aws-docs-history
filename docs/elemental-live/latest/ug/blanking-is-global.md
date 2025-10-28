# Blanking is global

Both Ad avail blanking and Blackout apply to all outputs. You cannot choose to blank
out for some outputs and not blank out for others: it is an all-or-nothing decision.

###### Compare Blanking to Manifest Decoration and Passthrough

Manifest decoration and passthrough have a smaller scope than
blanking : they apply only to outputs that support these
features.

Take important note of this fact, because if you do _not_ do passthrough and do _not_ do manifest decoration in a given
output (because these are not supported or because you choose not
to) but you do implement blanking, there are no “markers” for where
the blanked content occurs.

To identify where this blanking is occurring. look for the IDR I-frames that
identify where the SCTE-35 message used to be.
