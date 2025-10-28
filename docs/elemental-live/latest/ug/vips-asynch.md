# Virtual input switching using asynchronous

ESAM messages

## Input types

Asynchronous input switching works only with the following
sources:

- MPTS programs, from an MPTS input. MPTS programs are typically live
  sources.
- File inputs—any type of input that Elemental Live considers to be a
  file input. See [Supported upstream systems
  for file inputs](supported-inputs-file-types.md "supported-inputs-file-types.md")

If your event doesn't include these types of inputs, you can't set up
for asynchronous input switching.

## Setup

You set up the inputs in the Elemental Live event. You also set up the
POIS with information about the same set of inputs. In other words, the
inputs must be set up in both Elemental Live and the POIS.

You start the event. At any time, the POIS can send an asynchronous
ESAM request to Elemental Live.

## Principle of operation

The POIS sends a request to Elemental Live to request a switch away
from the currently active input and to another input. The request can be
seen as a switch away to another input. In addition, the originator of any
potential action is the POIS.

Compare this principle of operation to SCTE-35-based triggers, where
Elemental Live probes each non-active input for requests to switch to that
non-active input. The request can be seen as a switch to this input. In
addition, the originator of any potential action is Elemental Live.

## Types of requests

The POIS can send one or more of the following requests:

- Prepare input. This request makes Elemental Live start processing the
  input before you switch to it. This preparation reduces the delay
  that always occurs between the switch request and the switch
  happening.
- Switch input. The POIS sends this request to instruct Elemental Live
  to switch, either immediately, or at a specific time.
- Handles SCTE-35 messages for ad avails. The POIS can request that Elemental Live insert
  an ad avail message. For information about the handling of these types of SCTE-35 messages,
  see [POIS conditioning](pois-conditioning.md "pois-conditioning.md").
- SCTE-35 messages that instruct Elemental Live whether to include the SCTE-35 in the
  output or not. The POIS can choose to instruct Elemental Live to include or to remove any of
  the three types of SCTE-35 messages.

## Timing of input switching requests

The prepare input request should be sent at least 15 seconds before
the switch request.

If the POIS sends both a prepare request and a switch request, the
switch will occur in less than 4 seconds. After the switch occurs,
Elemental Live stops preparing the input.

If the POIS sends a switch request but no prepare request, the input
switch might take as long as 12 seconds.

## Result in outputs

If the POIS instructs Elemental Live to include an SCTE-35 message in the output, that
message becomes part of the stream. This rule applies to all types of messages – prepare input,
switch input, and message relating to ad avails.

For a prepare input or switch input, Elemental Live still performs the
action (prepare or switch), even if the POIS instructs Elemental Live not to
include the message itself in the output.

Elemental Live includes these messages in output types that support SCTE-35 messages. For
example, Elemental Live includes the messages in an HLS output.

For detailed information about how Elemental Live handles ad avail
SCTE-35 messages, see [POIS conditioning](pois-conditioning.md "pois-conditioning.md").

## No queuing of requests

There is no way to create a queue of requests. Elemental Live can
handle only one request. The POIS might send a request to switch to
input A at 2:00:00.00. Then, before Elemental Live has performed that
request, the POIS might send a request to switch to input B.

Even if the second request has a start time that is later than the
first request, the second request will replace the first request in the
request list.

## Example

Here's an example of an input switching scenario that illustrates the
different input switching capabilities.

The time is 2:00:00. You start the event and Elemental Live starts
ingesting the first input, which is a file input.

**Asynchronous request to a file
input**

At 2:01:00, the POIS sends an asynchronous request to switch to input
B. Input B is the first in a series of 20-second ads.

**Asynchronous request to switch to a live
input**

At 2:02:07, while these files are being processed, the POIS sends an
asynchronous request to switch to input Y at 2:04:00.00. Elemental Live
switches to input Y at the specified start time. Assume that input Y is a
live TS input.

**Canceled asynchronous request**

This example shows cancellation of an asynchronous request.

At 2:51:44, the POIS sends a request to switch to input F at
2:52:00.

At 2:51:47, the POIS sends a request to switch to input Y (the input
that is currently active) at 2:49:60.00. This request effectively cancels
the switch to input F. Elemental Live can only have one request in its
buffer, and the most recently received request always replaces any request
already waiting.

**Multiple requests in an unexpected
order**

At 2:53:48, the POIS sends a request to switch to input D at 2:57:00.

At 2:54:00, the POIS sends a request to switch to input E at 2:55:30.

Elemental Live ignores the request to switch to input D. Elemental Live
can only have one request in its buffer, and the most recently received
request always replaces any request already waiting.

Therefore at 2:55:30, Elemental Live switches to input E.
