# How input and output reservations work

MediaLive offers input and output reservations.

###### Topics

- [Input reservation attributes and
  matching](#input-reservation-attributes-matching "#input-reservation-attributes-matching")
- [Output reservation attributes and
  matching](#output-reservation-attributes-matching "#output-reservation-attributes-matching")
- [How an input or output reservation
  is applied](#how-inputoutput-reservation-applied "#how-inputoutput-reservation-applied")

## Input reservation attributes and

matching

An _input reservation_ applies to the cost of processing input. An
input reservation has these attributes:

- Codec
- Resolution (a range)
- Bitrate (a range)
- Region (in which the input runs)
  **How matching works**

For a reservation to apply to an input, the attributes of the input reservation must
match the fields in the channel's **Input specification**. The channel must
also run in the Region that is specified in the reservation. For example, suppose that your
input specification for a channel is **AVC**, **HD**, and
**Max 20 Mbps**. A reservation that matches those attributes could apply
to the input in that channel.

## Output reservation attributes and

matching

An _output reservation_ applies to the cost of the processing
output. An output reservation has the following attributes:

- Codec
- Resolution (a range)
- Bitrate (a range)
- Frame rate (a range)
- Region (in which the input runs)

**How matching works**

For a reservation to apply to an output, the attributes of the output reservation must
match the corresponding fields in the channel configuration. The channel must also run in
the Region that is specified in the reservation. You can find the fields on the AWS Elemental MediaLive
console:

- For a regular video and audio output, the fields are in the **Video
  output** section of the channel configuration. To make most of the fields
  appear, you must choose a codec on the page.
- For an audio-only output, the fields are in the **Audio output**
  section of the channel configuration.

**Example of matching**

There is a match between an existing channel and a reservation if all of the fields in
the channel match the corresponding reservation attributes.

There is a match if the value of a field in the channel is equal to, or falls within
the range of, the corresponding attribute. For example, a frame rate of `29.97
 fps` in the channel configuration falls within the range of a frame rate
attribute of `<=30fps` in the reservation.

For the frame rate attribute, there is a match as follows:

- If
  the channel output frame rate is set to a specific frame rate: There is a match if the
  frame rate specified in the channel configuration falls within the reservation frame
  rate range. For example, the specified frame rate is
  `24fps` and the reservation is
  `<=30fps`.
- If the channel output frame rate is set to initialize from the source, there is a
  match only if the reservation range includes `60fps`. For
  example, there is a match on reservations with `30-60fps`.

Note:
If you purchase a reservation to target a specific output, and that
output has the frame rate set to initialize from source, make sure that you purchase a
reservation that specifies `30-60fps`. Don't purchase a
reservation that specifies `<=30fps`.

**Example of no match**

If only one of the fields does not match its corresponding reservation attribute,
there is no match between the output and reservation.

## How an input or output reservation

is applied

At the start of each monthly billing cycle, AWS replenishes each reservation with
the pool of minutes for the month.

At the end of the cycle, AWS applies the minutes from a given reservation to reduce
the cost for the processed
items
(inputs or outputs) whose attributes match
this reservation. For each minute in the month, AWS determines if one or more matching
items were running. It accumulates these
_running minutes_ within the hour, up to a
maximum of 60 minutes in the hour.

After the reservation minutes are used up for the hour, AWS charges the regular
rate-per-minute for the remainder of the items in that hour.

### Running minutes can be allocated

over items

The running minutes could come from more than one item. For example, you start
Channel A with an input that matches a given reservation. You have purchased only one
instance of this reservation. After 45 minutes, you start Channel B that also has an
input that matches a given reservation. After 15 more minutes, you stop Channel A. The
running minutes are accumulated as shown by the shading in the following
illustration.

![A graphic representation of 80 minutes with two inputs, one input running for 60 minutes and one input running for 35 minutes. The second input has a 15 minute overlap with the first input. A bar runs across the top of the image and is divided into eight segments representing 10 minute blocks, totalling 80 minutes. Below the top bar, a block labelled Input is aligned underneath the first six 10 minute blocks, representing 60 minutes beginning at the start of the total 80 minute period. This first Input block is fully shaded, showing it fully matches the reservation. Below the first Input block is another block labelled Input. This block begins after the first 45 minutes represented by the 10 minute blocks. On the second Input block, only the final 20 minutes, of 35, are shaded. The shading that represents running minutes does not overlap between the two Input blocks.](images/reservations-inout-shared2inputs.png)

Here is another example of how different items can consume the running minutes.
Suppose that in one hour, you run only outputs that match a given reservation. You have
purchased only one instance of this reservation. You run these four matching outputs
simultaneously for 15 minutes each. During that hour, you don't run any other matching
outputs. Those four outputs would all contribute to the 60 minutes.

![A graphic representation of 60 minutes with four outputs, each output running for 15 minutes. A bar runs across the top of the image and is divided into six segments representing 10 minute blocks, totalling 60 minutes. Below the top bar, four block are labelled as outputs. Each output block occupies 15 minutes of space. Each output block starts at the first 10 minute block. All four output blocks are fully shaded to represent the entire output is considered running minutes.](images/reservations-inout-shared4outputs.png)

### Processing bursts are not

supported

The 60-minute rule means that reservations can't be used for processing
bursts.

For example, in one hour you run four outputs that match a given reservation. You
have purchased only one instance of this reservation. You run these four matching
outputs simultaneously for 60 minutes each. Only one of these outputs is eligible for
the reservation because one output is enough to use up the 60 running minutes per
hour.

![A graphic representation of 60 minutes with four inputs, each input running for 60 total minutes. A bar runs across the top of the image and is divided into six segments representing 10 minute blocks, totalling 60 minutes. Below the top bar, four block are labelled as inputs. Each input block occupies 60 minutes of space, running the entire length of the 60 minute bar. Only the first input block is shaded, representing that only one of the four inputs is consuming the 60 minutes of running minutes.](images/reservations-inout-bursts.png)

### Unused minutes

If some or all of the minutes in the reservation are not used in the month, those
minutes are lost.

The minutes are not transferred to the next month.

### Running minutes can be

allocated over items

There are no restrictions regarding channels:

- For example, the reservation could be consumed based on the processing of one
  input from one channel and another input from a different channel.
- There is no requirement that all the inputs or outputs in a given channel must
  be covered by a reservation.
