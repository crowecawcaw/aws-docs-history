# Coordinate with the downstream system

You and the operator of the downstream system must agree about the destination for
each output of the UDP output group.

A UDP output group requires one set of destination addresses for each output.

1.  Decide if you need two destinations for the output:
    - If the MediaLive channel is a [standard
      channel](plan-redundancy.md "plan-redundancy.md"), you need two destinations.
    - If the MediaLive channel is a single-pipeline channel, you need one
      destination.

2.  Speak to the operator who manages the downstream system that will receive UDP
    content. Make sure that the operator sets up to expect one or two MediaLive outputs,
    as appropriate.
3.  Obtain the following information from the operator:

        * Whether the protocol is UDP or RTP
        * The URLs
        * The port numbers

    Each URL will look like this, for example:

`udp://203.0.113.28:5000`

`udp://203.0.113.33:5005`

Note that in this example, the port numbers are not sequential. These
non-sequential numbers are important if you plan to enable FEC in the outputs
(this field is in the **Output** pane of the UDP output group).
With FEC, you must leave space between the port numbers for the two
destinations. For example, if one destination is
`rtp://203.0.113.28:5000`, assume that FEC also uses
port 5002 and 5004. So the lowest possible port number for the other destination
is 5005.
