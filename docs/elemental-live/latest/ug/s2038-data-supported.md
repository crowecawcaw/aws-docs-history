# Supported ancillary data

Elemental Live can ingest several types of ancillary data. After the
data has been ingested, Elemental Live can handle it in one of two
ways—use it, following the instructions you set up in the channel, or
passing it through in the output, so that a downstream system can use
it.

Elemental Live can use the following ancillary data:

- Time code – If a time code is included in the SMPTE 2038, it
  is always an embedded time code.

You can choose to configure the event to use the extracted
time code as the timecode source for video processing.

- Captions – The SMPTE 2038 might include embedded, Teletext, or
  ARIB captions.

You can choose to set up the extracted captions as the source
for output captions, in [the usual
way](captions.md "captions.md").

- AFD signals – The SMPTE 2038 might include AFD signals.

You can choose to set up one or more outputs so that
Elemental Live uses the signals to modify the video.

- SCTE 104 messages – The SMPTE 2038 might include SCTE 104
  messages. Elemental Live automatically converts the messages to
  SCTE 35 messages.

You can choose to handle these messages in [the usual way](scte-message-processing.md "scte-message-processing.md").
Elemental Live can pass through the following ancillary data:

- Custom data – Elemental Live considers ancillary data to be
  _custom data_ if it is not
  any of the four types listed above.

You can choose to identify this custom data so that
Elemental Live can extract it.

You can then set up SMPTE 2110 outputs to include that data.
Elemental Live doesn't read or use the ancillary data in any
way.
