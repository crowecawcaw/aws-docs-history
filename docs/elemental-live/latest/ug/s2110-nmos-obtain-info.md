# Obtain information from the NMOS

operator

Speak to the NMOS operator in your organization to make sure that you are aligned on
the content of the streams.

- Obtain the number and types of the streams — video, audio, and so on.
- For each audio stream, obtain the languages and order of the languages. For
  example, in an audio stream that contains three languages, you must know the names
  and the order of the languages. The languages are assigned an index, starting at

0.

- For each embedded captions stream, obtain the number and order of the
  languages.
  You must be aligned so that you can set up Elemental Live to select the audio and ancillary
  streams correctly, and so that the NMOS controller can successfully perform NMOS
  patching.

**Example 1**

You and the NMOS operator might agree that the SDP files and their streams are
ordered as follows:

- SDP 1: Video stream
- SDP 2: Audio stream containing English Dolby Digital
- SDP 3: Audio stream containing French Dolby Digital
- SDP 4: Audio stream containing Spanish Dolby Digital
- SDP 5: Ancillary stream containing EIA-608 embedded captions, with English in
  CC1, French in CC2, Spanish in CC3, and CC4 not used.
- SDP 6: Ancillary stream for SCTE-104 messages.
  **Example 2**

You and the NMOS operator might agree to this setup:

- SDP 1: Video stream
- SDP 2: Audio stream containing three audio descriptions, in this order:
  - English Dolby Digital
  - French Dolby Digital
  - Spanish Dolby Digital

- SDP 3: Ancillary stream containing EIA-608 embedded captions, with English in
  CC1, French in CC2, and Spanish in CC3. CC4 is not used.
