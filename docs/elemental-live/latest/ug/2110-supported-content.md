

# Supported content
<a name="2110-supported-content"></a>

The following table describes the content that Elemental Live supports in SMPTE 2110 sources (inputs) and SMPTE 2110 outputs.
+ For inputs, Elemental Live supports ingest of one instance of each type of stream—one video stream, zero or one audio stream, and zero or one ancillary data stream.
+ For outputs, Elemental Live supports one video stream, zero or more audio streams, and zero or one ancillary data stream.

For detailed instructions for setting up a SMPTE 2110 input or output, see [Ingesting SMPTE 2110 content](input-2110.md) and [Configuring SMPTE 2110 outputs](output-2110.md).

**Note**  
Elemental Live can't ingest more than one audio stream in one SMPTE 2110 input.



- **Video**
  - **Direction:** Input and output / **Details:** UncompressedResolutions – SD, HD, and 4K<br />Scan types – Progressive and interlaced<br />Sampling – 4:2:2<br />Bit format – 10-bit / **Applicable standard:** SMPTE 2110-20
  - **Direction:** Input and output / **Details:** Lightly compressed with JPEG XS<br />Resolutions – SD and HD resolution<br />Scan types – Progressive and interlaced<br />Sampling – 4:2:2<br />Bit format – 8-bit, 10-bit, 12-bit / **Applicable standard:** SMPTE 2110-22

- **Audio**
  - **Direction:** Input and output / **Details:** PCM audioUncompressed <br />Sample rates: 44.1kHz and 48.0 kHz  / **Applicable standard:** SMPTE 2110-30
  - **Direction:** Input and output / **Details:** Dolby Digital (AC3)Coding modes – 1.0, 1\+1, 2.0, 3.2 (with LFE) / **Applicable standard:** SMPTE 2110-31
  - **Details:** Dolby Digital Plus (EAC3)Coding modes – 1.0, 2.0, 3.2
  - **Direction:** Output / **Details:** Dolby Digital passthroughYou can pass through Dolby Digital (AC3) from any input (SMPTE 2110 or another type) to a SMPTE 2110 output

- **Ancillary data – Captions (optional)**
  - **Direction:** Input and output
  - **Details:** EIA-608 embedded captionsCEA-708 embedded captions
  - **Applicable standard:** SMPTE 2110-40

- **Ancillary data – Ad avail messages (optional)**
  - **Direction:** Input / **Details:** SCTE 104 messages. Elemental Live will automatically convert these messages to SCTE 35 messages during ingest.
  - **Direction:** Output / **Details:** SCTE 104 messages. If the source content has SCTE 35 messages, you can configure Elemental Live to convert them to SCTE 104 and include the SCTE 104 messages in the output.
  - **Applicable standard:** SMPTE 2110-40

- **Timecode**
  - **Direction:** Input / **Details:** The SMPTE 2110 source must be Precision Time Protocol (PTP) locked. <br />If it isn't locked, the video, audio, and ancillary data might not get synchronized properly during processing, resulting in unsynchronized media in all the outputs in the event.
  - **Direction:** Output / **Details:** You must [enable PTP](enable-ptp.md) in Elemental Live so that the SMPTE 2110 outputs include RTP packet timestamps. This timestamp synchronizes the video, audio, and ancillary data. It ensures that the output is PTP-locked.
  - **Applicable standard:** SMPTE 2110-21

