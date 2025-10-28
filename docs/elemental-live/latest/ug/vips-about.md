# About virtual input switching

## Supported version of the specification

Elemental Live supports communications with a POIS according to this
specification: OpenCable Specifications Alternate Content Real-time
Event Signaling and Management API, OC-SP-ESAM-API-I03-131025.

## The two virtual input switching features

There are two virtual input switching features. These features work in
different ways and support different use cases. But they both require a
POIS.

- Virtual input switching using asynchronous ESAM messages

This type of input switching is based only on decisions from the
POIS. We also refer to this switching as asynchronous input
switching. This feature is available in Elemental Live version 2.23.0 and later.

- Virtual input switching using SCTE-35 messages

This type of input switching relies on switch-related SCTE-35
messages that are in the input. We also refer to this switching as
SCTE-35-triggered input switching. This feature is available in Elemental Live
version 2.20.2 and later.

Virtual input switching requires the virtual input switcher license
(the Virtual Input Switcher License add-on pack). Contact your AWS sales
manager.

## Choosing the switching feature to use

Typical use cases for the virtual input switching features are the
following:

- SCTE-35-triggered input switching alone

When your event consists of live MPTS programs, you can implement
SCTE-35-triggered input switching. Upstream of Elemental Live, a
system inserts SCTE-35 messages into the programs, and Elemental Live
reacts to them during ingest.

This scenario works well when you have well-orchestrated, predictable
event.

- Asynchronous input switching alone

When it's not feasible to implement SCTE-35-triggered input switching, you can implement
asynchronous input switching. For example, if your event doesn't use sources that support
SCTE-35-triggered input switching.

With asynchronous input switching, the POIS sends SCTE-35 messages to
Elemental Live. These messages contain instructions that Elemental Live
reacts to.

Asynchronous input switching doesn't mean that the switching is
unplanned. You can design a schedule and automate your POIS to send the
switch requests.

- Both types of switching

You might implement the SCTE-35-triggered switch scenario described
previously, and also implement asynchronous input switching. To
handle planned cutaways to file content, you can implement
asynchronous input switching to handle unplanned cutaways to a file
content. You can also implement synchronous input switching when you
need to quickly drop the live stream and show a "please standby"
file clip.
