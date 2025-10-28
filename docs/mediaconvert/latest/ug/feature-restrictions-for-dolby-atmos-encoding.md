# Requirements for Dolby Atmos encoding

Note the following restrictions in the MediaConvert implementation of Dolby
Atmos encoding:

- **Input Channel-Based Immersive (CBI):** MediaConvert
  supports channel-based immersive (CBI) content.
- **Input Dolby Atmos Master File (DAMF):** MediaConvert
  supports Dolby Atmos master file (DAMF). This is a collection of 3 files
  with the extensions, .atmos, .atmos.metadata, and .atmos.audio
- **Input Immersive Audio Bitstream (IAB):** MediaConvert
  supports immersive audio bistream (IAB).
- **Input Audio Definition Model Broadcast WAV Format (ADM
  BWF):** MediaConvert supports ADM BWF. It is a single
  broadcast WAV file contains header data with the .atmos and .atmos.metadata
  information.
- **Output codec:** You can create Dolby Atmos
  audio outputs encoded with only the Dolby Digital Plus (EAC3) codec.
- **Output containers:** For file outputs, you
  can create Dolby Atmos audio in only in one of the video containers that
  supports Dolby Digital Plus: MPEG-4, MPEG-2 Transport Stream, or
  QuickTime.
- **Output packages:** For adaptive bitrate
  (ABR) outputs, you can create Dolby Atmos audio in any of the
  MediaConvert output group types: CMAF, Apple HLS, DASH ISO, or
  Microsoft Smooth Streaming.
