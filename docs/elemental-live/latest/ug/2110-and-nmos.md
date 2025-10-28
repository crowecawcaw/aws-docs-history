# Support for NMOS IS-04

stream
discovery

Elemental Live supports NMOS IS-04
with
both SMPTE 2110 inputs and outputs.

###### Note

Currently, Elemental Live supports management of SMPTE 2110 streams using NMOS. Elemental Live doesn't
support management of other types of streams.

**SMPTE 2110 with NMOS**

An NMOS solution
includes an NMOS
controller and an optional NMOS registry. If your solution includes a registry, you
configure Elemental Live to communicate with that registry. If your solution doesn't include a
registry, you must configure your NMOS controller to query
Elemental Live

- Information about the SMPTE 2110 streams, including a unique ID for each stream.
- Information about the
  available
  _senders_
  and _receivers_.
  For a stream that Elemental Live outputs, Elemental Live is the sender. For a stream that Elemental Live
  ingests, it is the receiver.
  **SMPTE 2110 without NMOS**

If you don't set up an NMOS solution, you still use SDP files:

- For a SMPTE 2110 input, you must identify the server where the SDP files are
  stored. This can be any HTTP server. When you configure the input, you specify which
  SDP files contain information about the SMPTE 2110 stream.
- For a SMPTE 2110 output, Elemental Live automatically creates the applicable SDP files. You
  must make these files accessible to the downstream system.
