# Virtual input switching using SCTE-35

messages

This type of input switching works with SCTE-35 messages that are in a transport stream
source. When Elemental Live encounters an SCTE 35 message in the source, it sends the message to
the POIS. The POIS might decide to send a request to switch input. Note that there is no sense
of a particular type of SCTE 35 message that can trigger an input switch request. The POIS can
request a switch in response to any type of SCTE 35 message that it receives.

## Input types

SCTE-35-triggered input switching works only with the following
sources:

- MPTS programs, from one MPTS input. MPTS programs are typically live
  sources.

## Principle of operation

Elemental Live probes each non-active MPTS program for requests to
switch to that non-active input. The request can be seen as a switch to this
input. In addition, the originator of any potential action is
Elemental Live.

Compare this principle of operation to asynchronous input switching,
where the POIS sends a request to Elemental Live to request a switch away
from the currently active input and to another input. The request can be
seen as a switch away to another input. In addition, the originator of any
potential action is the POIS.

## Setup

In the event, you set up the inputs:

- You identify all the MPTS programs that you want to use, and set up each program as an
  individual input.

You also set up the POIS with information about the same set of inputs.
In other words, the inputs must be set up in both Elemental Live and the
POIS.

You start the event. As Elemental Live ingests the first input, it encounters SCTE-35
messages. It sends these messages to the POIS. It sends all SCTE-35 messages, not only
switching-related messages. For example, it also sends ad avail messages.

For any switching-related message, the POIS might decide to send a request to Elemental Live
to switch to another input at a specific time. The POIS can send this instruction at any time.
There is no timeout between receiving the information and sending an instruction. The POIS
might also decide not to send an instruction.

## Types of requests

The following are the types of requests:

- Prepare input. This request makes Elemental Live start processing the
  input, even before the input is active. This preparation reduces
  the delay that always occurs between the switch request and the
  switch happening.
- Switch input. The POIS sends this request to instruct Elemental Live
  to switch, either immediately, or at a specific time.

The prepare input request should be sent at least 15 seconds before
the switch request.

If the POIS sends a prepare input and a switch input, the switch
will occur in less than 4 seconds.

If the POIS doesn't send a prepare input, the input switch can take as long as 12
seconds.

- SCTE-35 messages for ad avail handling. The POIS can request that
  Elemental Live insert an ad avail message, or delete or modify an ad avail
  message that is in the source stream (and that Elemental Live therefore
  sent to the POIS). For information about the handling of these types of
  SCTE-35 messages, see [POIS conditioning](pois-conditioning.md "pois-conditioning.md").
- SCTE-35 messages that instruct Elemental Live whether to include the SCTE-35 in the
  output or not. The POIS can choose to instruct Elemental Live to include or to remove any of
  the three types of SCTE-35 messages.

## Timing of input switching requests

The prepare input request should be sent at least 15 seconds before the
switch request.

If the POIS sends a prepare input and a switch input, the switch will
occur in less than 4 seconds. After the switch occurs, Elemental Live stops
preparing the input.

If the POIS doesn't send a prepare input, the input switch might take
as long as 12 seconds.

## Result in outputs

If the POIS instructs Elemental Live to include an SCTE-35 message in the output, that
message becomes part of the stream. This rule applies to all types of messages – prepare input,
switch input, and messages relating to ad avails.

For a prepare input or switch input, Elemental Live still performs the
action (prepare or switch), even if the POIS instructs Elemental Live not to
include the message itself in the output.

Elemental Live includes these messages in output types that support SCTE-35 messages. For
example, Elemental Live includes the messages in an HLS output.

For detailed information about how Elemental Live handles ad avail
SCTE-35 messages, see [POIS conditioning](pois-conditioning.md "pois-conditioning.md").

## Example

Here's an example of an input switching scenario that illustrates the
different input switching capabilities.

The time is 2:00:00. You start the event and Elemental Live starts
ingesting the first input. At the same time, Elemental Live reads all the
other inputs,

**SCTE-35-triggered request**

At 2:17:33, while ingesting input Y, Elemental Live encounters an SCTE-35 message. It sends
the message to the POIS. Shortly after, the POIS sends a request to switch to input Z at
2:30:00.

At 2:30:00, Elemental Live switches to input Z (another live
input).

**SCTE-35 message that the POIS
ignores**

At 2:37:00, Elemental Live encounters an SCTE-35 message. It sends the message to the POIS,
but the POIS doesn't send an input switch request. There is no rule that dictates that the POIS
must switch on receiving a message.

**Multiple SCTE-35-triggered
requests**

At 2:40:02, Elemental Live encounters another SCTE-35 message, and this
time the POIS does respond by sending two requests. One request is to switch
at 2:45:13 to input B (one of the ads that played previously). The second
request is to switch at 2:45:43 back to input Z.

At 2:45:13, Elemental Live switches to input B.

At 2:45:43, Elemental Live switches back to input Z.

**Canceled asynchronous request**

At 2:51:44, the POIS sends a request to switch to input F at
2:52:00.

At 2:51:47, the POIS sends a request to cancel the switch to input
F.

This example shows cancellation of an asynchronous request. The POIS
can cancel either an asynchronous request of a SCTE-35-triggered
request.

**Multiple requests in an unexpected
order**

At 2:53:48, the POIS sends a request to switch to input D at 2:57:00.

At 2:54:00, the POIS sends a request to switch to input E at 2:55:30.

At 2:55:30, Elemental Live switches to input E. Then at 2:57:00,
Elemental Live switches to input D.

Note that Elemental Live doesn't ignore the request to switch to input
D, even though it received the request for input E in the meantime.
