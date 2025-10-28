# Well-formed SMPTE 2038

source

For Elemental Live to handle the ancillary data, the SMPTE 2038 must
meet certain criteria:

- The SMPTE 2038 packet must be present in every PMT.
- The PID in which the SMPTE 2038 packet is located must not
  change in the stream. There is no support for changing the PID
  and sending a new PMT identifying that PID.
- The stream should contain the SMPTE 2038 packet in only one
  PID. If it is present in more than one PID, there is no guarantee
  that Elemental Live will identify the PID that appears first. It
  could choose another PID, with results you do not intend.
