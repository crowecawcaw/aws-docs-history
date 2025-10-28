# A well-formed SMPTE 2038

stream

For MediaLive to extract and process the data appropriately, the SMPTE
2038 stream in the input must meet certain criteria:

- The SMPTE 2038 stream must be present in every PMT.
- The PID in which the SMPTE 2038 stream is located must not
  change in the stream. There is no support for changing the PID
  and sending a new PMT identifying that PID.
- The transport stream should contain the SMPTE 2038 stream in
  only one PID. If it's present in more than one PID, there's no
  guarantee that MediaLive will identify the PID that appears first. It
  could choose another PID, with results you don't intend.
  Note that if the input is a Elemental Link input, embedded captions (if
  any), the timecode, and KLV metadata (if any) are always in a SMPTE
  2038 stream. The stream is always well-formed.
