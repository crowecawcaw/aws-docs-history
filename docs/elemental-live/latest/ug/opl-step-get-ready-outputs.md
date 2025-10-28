# Design the outputs

When you design a workflow that implements Elemental Live output
locking, you must decide which output group types you will produce,
design the outputs in the output groups, and decide on the video
encoding characteristics of the output type or types.

This section covers considerations that affect your design.

###### Topics

- [Number of outputs in an output group](#opl-design-outputs-opg "#opl-design-outputs-opg")
- [Number of encodes: video encode
  sharing](#opl-design-outputs-number-encodes "#opl-design-outputs-number-encodes")
- [Encodes across the locked
  events](#opl-design-outputs-number-encodes-event "#opl-design-outputs-number-encodes-event")
- [Features in an output](#opl-design-output-features "#opl-design-output-features")
- [Motion graphic overlay](#opl-design-output-features-motion-gx "#opl-design-output-features-motion-gx")

## Number of outputs in an output group

For distributed encoding, there will be many cases where one appliance can produce
only one output encode. To set up these encodes, create an output group (for example,
create an HLS output group), and create one output in that output group.

There might also be cases where you have determined that one appliance can produce
several one lower-resolution output encodes. To set up these encodes, create an output
group (for example, create an HLS output group), and create two outputs. Each output
contains one of the encodes.

## Number of encodes: video encode

sharing

If you have multiple output group types in one event, several different output groups
might be able to use the same video encode.

For example, if you're producing an HLS package and a UDP/TS
package, and both packages are encoded with H.264, you might be able
to create one video encode that the two output groups share. This
sharing reduces the compute demands on the appliance. To share the
encodes, create an output in one output group and an output in the
other output group. Create one video stream. Set up both outputs to
use the same encode.

![Diagram showing two output groups sharing a high resolution video stream.](images/opl-shared-encode.png)

## Encodes across the locked

events

You must set up the video encodes in the locked events as follows:

- For an output redundancy implementation, the pair of encodes in the same type of
  output group must be identical. For example, the encode in the output must be
  identical to the encode in the redundant output.
- For a distributed encoding implementation, each pair of encodes must be identical,
  so that the main ABR stack and the redundant ABR stack are identical. For example, you
  might have one ABR stack consisting of encodes A1, B1, C1, D1, and another ABR stack
  consisting of encodes A2, B2, C2, D2. Encode A1 must be identical to encode A2, B1
  identical to B2, and so on.

For an explanation of _pairs of encodes_, see [Output locking pairs](opl-redundant-pairs.md "opl-redundant-pairs.md").

## Features in an output

Some features, such as static graphic overlay, can apply within an individual portion
of an event.

Make sure that you apply the features in the same way in every locked event. For
example, if you implement the static overlay in all outputs in one event, then make sure
that you set it up on all outputs in the other event. For more information, including
diagrams, see [Insertion options and the effect on outputs](insertion-options-and-the-effect-on-outputs.md "insertion-options-and-the-effect-on-outputs.md").

## Motion graphic overlay

We strongly recommend against combining motion graphic overlays and output locking.
Frame accuracy can't apply to motion graphic overlays that are applied to the video
content.
