# Obtain information

Obtain the following information from your contact person at the upstream
system:

- The public network IP addresses. You need two sets of IP addresses because
  an RTP input is always a [standard-class
  input](class-channel-input.md "class-channel-input.md"), even if your channel is a single-pipeline channel. For
  information about input classes, see [Choosing the channel class and input
  class](class-channel-input.md "class-channel-input.md").

These are the sets of IP addresses where the source or sources for the
content will appear on the public network. You need this information to
create the input security group.

For example:

    + For one source: `203.0.113.19, 203.0.113.58, 203.0.113.25`
    + For the other source: `198.51.100.19, 198.51.100.59,
     198.51.100.21`
