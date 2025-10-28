# Result of this procedure

As a result of this setup, an Elemental Link input (the blue box) exists that
identifies the AWS Elemental Link device or devices (the purple box) that are connected to MediaLive.
There is no other setup for you to perform, because the AWS Elemental Link device is designed to
work seamlessly with MediaLive.

Keep in mind that with a push input, the upstream system must be pushing the video
source to the input when you start the channel. The upstream system does not need to be
pushing before then.

At runtime of the channel, MediaLive reacts to and ingests the content that AWS Elemental Link is
pushing.
