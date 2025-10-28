# Metadata that MediaLive can extract

MediaLive can extract the following data from a SMPTE 2038 stream that is in the
source.

**Captions**

- ARIB captions – Captions that are compliant with ARIB STD-B37 version
  2.4.
- Embedded captions – Captions carried as ancillary captions that are
  compliant with SMPTE 334. The ancillary captions themselves must be compliant with
  EIA-608 standard (also known as CEA-608 or “line 21 captions”) or CEA-708 standard
  (also known as EIA-708).

- Teletext captions – OP47 teletext format, also known as SMPTE RDD-08
  (compliant with ITU-R BT.1120-7).
  **Timecode**

- Timecode – A SMPTE 12M timecode. MediaLive recognizes this timecode as an
  embedded timecode source.
  **Ad avail messages**

- SCTE 104 messages.
  **Metadata**

- KLV metadata – Data that is compliant with SMPTE 336M-2007.
