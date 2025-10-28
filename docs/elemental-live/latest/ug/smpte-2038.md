# Handling ancillary data in SMPTE 2038

Whenever you plan to set up a transport stream (TS) source, you should
find out if the content provider has set up the TS so that some data is
included in SMPTE 2038 packets, rather than in the standard locations. The
content provider typically sets up the TS in this way because they have
converted an SDI stream to a TS.

If the content provider has provided data in SMPTE 2038, set up the
input to extract that data from the SMPTE 2038 packets. Doing so ensures
that Elemental Live will handle the source correctly. Don't ignore the
data.

###### Topics

- [Supported ancillary data](s2038-data-supported.md "s2038-data-supported.md")
- [Well-formed SMPTE 2038
  source](s2038-data-well-formed.md "s2038-data-well-formed.md")
- [Enable SMPTE 2038](s2038-data-enable.md "s2038-data-enable.md")
- [Setting up the event to use the
  ancillary data](s2038-data-use-data.md "s2038-data-use-data.md")
- [Setting up the
  event to pass through custom data](s2038-data-passthrough-custom-data.md "s2038-data-passthrough-custom-data.md")
