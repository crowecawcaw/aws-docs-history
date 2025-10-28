# Support for SMPTE 2022-7 – seamless protection

switching

Elemental Live supports seamless protection switching (conforming with SMPTE 2022-7) for both
SMPTE 2110 inputs and SMPTE 2110 outputs. The Elemental Live implementation of SMPTE 2022-7 provides
protection against packet loss, interface failure, and network loss (because the two
interfaces use different network paths).

- For inputs, if the source implements SMPTE 2022-7, you can configure some or all
  of the SMPTE 2110 streams in your event to accept inputs over two interfaces. Elemental Live
  will then perform seamless protection switching at the packet level, to ensure
  uninterrupted ingest of the content.

For those streams, AWS Elemental Live receives two identical packet streams. When there is
a problem with the first stream, AWS Elemental Live immediately uses the second stream to
reconstruct the data, with no effect on the content.

- For outputs, you set up for SMPTE 2022-7 in the streams (Elemental Live outputs) in the
  SMPTE 2110 output group. Elemental Live will include two identical packet streams in each
  applicable stream.
  Note that in both the inputs and the outputs, seamless protection switching might be
  implemented in some streams but not others. For example, it might be implemented in the
  video streams but not the audio or ancillary data streams. Compare this to [NMOS](2110-and-nmos.md "2110-and-nmos.md"), where all the streams in an input or output either
  use NMOS or don't use NMOS.
