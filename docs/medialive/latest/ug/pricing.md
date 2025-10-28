# Pricing in MediaLive

As with other AWS products, there are no contracts or minimum
commitments for using AWS Elemental MediaLive.

This section provides very general information about pricing. For
detailed information, see [https://aws.amazon.com/medialive/pricing/](https://aws.amazon.com/medialive/pricing/ "https://aws.amazon.com/medialive/pricing/").

There are charges for MediaLive based on the state of resources. There are
idle charges and running charges.

**States**

- A channel is either running or not running.

It is _not running_ if any of the
following situations applies:

    + It has not been started
    + It was running but has failed and has not yet automatically
     restarted.
    + It was running but has been stopped for maintenance and has
     not yet automatically restarted.

- An input is idle or running.

It is _idle_ if either of the
following situations applies:

    + It isn't attached to a channel
    + It is attached to a channel but the channel is not
     running.

**Idle Charges**

- There is an _idle channel
  charge_ for each channel that isn't running. There isn't
  a channel charge for a running channel. The charges are for the
  inputs and outputs in the channel.
- There is an _idle push input
  charge_ for each push input that isn't attached to a
  channel, and for each push input that is attached to a channel that
  isn't running.
- There is no charge for idle pull inputs.
  **Running Charges**

- There is no channel charge for a running channel. There are
  charges for the inputs and outputs in the channel.
- There is a _running output
  charge_ for each output that is configured in a channel
  that is running. The charge applies even if the output has been paused
  by the user or by Elemental Live.

The charge for each output is based on the type of output, and
on a combination of key video characteristics of the output, such as
video output codec, and video frame rate. You specify the
characteristics in the video settings of each output in the channel.
For more information, see [Set up the video encode](creating-a-channel-step6.md "creating-a-channel-step6.md").

- There is a _running input
  charge_ for each input that is attached to a channel that
  is running. The charge applies to both push and pull inputs. It
  applies even to the inputs in the channel that aren't currently active
  or that aren't receiving any content.

The input pricing is based on the type of input, and on a
combination of key characteristics of the input, such as input codec,
bitrate, and resolution. For detailed information about the basis for
input pricing, see [https://aws.amazon.com/medialive/pricing/](https://aws.amazon.com/medialive/pricing/ "https://aws.amazon.com/medialive/pricing/"). You specify some
of these characteristics in the input specification when you create
the channel. For more information, see [Input specifications settings](input-specification.md "input-specification.md").

- There is an _add-on charge_ for
  running channels that have specific features enabled. The charge
  applies to the channel, not to individual inputs, outputs, or other
  components within the channel. For example, the add-on charge for
  Advanced Audio is applied at the same rate for a running channel with
  one output that uses advanced audio as it is for a running channel
  with three outputs that use advanced audio. For a list of add-on
  charges, see [https://aws.amazon.com/medialive/pricing/](https://aws.amazon.com/medialive/pricing/ "https://aws.amazon.com/medialive/pricing/").
