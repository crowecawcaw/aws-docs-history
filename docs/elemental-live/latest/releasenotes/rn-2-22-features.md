

# New features in version 2.22 and 3.22
<a name="rn-2-22-features"></a>

This topic describes the new features in version 2.22 (3.22 for Conductor Live).

## New features in Elemental Live and Statmux 2.22
<a name="rn-2-22-features-live"></a>

Elemental Live and Statmux 2.22 include the following new features.

### Dolby Digital Plus with Atmos
<a name="rn-2-22-dolby-atmos-encode"></a>

Elemental Live now supports encoding audio outputs as Dolby Digital Plus with Atmos. Elemental Live can ingest an audio source that contains up to eight channels, and convert it to Dolby Digital Plus with Atmos.

### RTSP inputs
<a name="rn-2-22-rtsp-inputs"></a>

Elemental Live now supports RTSP inputs, to support delivery over the RTSP protocol. The source video can be HEVC or AVC with resolutions up to 4K, and framerates up to 60 fps. The source audio must be AAC.

The RTSP protocol is popular with devices such as security cameras.

### Additional support for mixed video codecs
<a name="rn-2-22-mixed-codecs"></a>

The mix of video codecs possible in an MPTS has been enhanced. Previously, an MPTS could be set up so that some events have HEVC video, and others have AVC video. Now, MPEG-2 is included. An MPTS can include an event with any combination of HEVC, AVC, and MPEG-2.

### SRT outputs
<a name="rn-2-22-srt-outputs"></a>

Elemental Live now supports delivering TS outputs over the SRT protocol. Elemental Live can have the role of caller or listener in the transmission.

The feature is available in the existing Reliable TS output group. The [AWS Elemental Live User Guide](https://docs.aws.amazon.com/elemental-live/latest/ug/) will be updated shortly to include steps for setting up this type of output.

### Support for RTMPS inputs
<a name="rn-2-22-rtmps-inputs"></a>

Elemental Live now supports ingest of sources that use a secure connection – RTMPS. To ingest RTMPS, choose **Network** input, and set the protocol to `rtmps://`.

### SMPTE 2110 inputs and NMOS – Static receiver
<a name="rn-2-22-2110-static-receiver"></a>

Elemental Live now lets you choose whether to use static or dynamic information for the `Device` and `Label` tags that Elemental Live sends to the NMOS receiver. This feature is controlled by the new field in the **NMOS Control** section in a SMPTE 2110 input. The new field is called **Use Static Receives**:
+ When the field is cleared (the legacy behavior), dynamic tags are used. The `Device` is set to a random ID that Elemental Live assigns. The `Label` is set to the event ID plus the input ID (for example, `Live_Event1_Input1`).
+ When the field is selected, static tags are used. Enter a custom name in the input name field. When you do this, the `Device` is set to the event GUID. The `Label` is set to the custom input name. Furthermore, if you select the field for two inputs in the same event, and assign the same input name, then the tags have identical values. This behavior is useful for workflows that rely on static device IDs.

### SMPTE 2110 – NMOS support with JPEG XS inputs and outputs
<a name="rn-2-22-2110-jpegxs-nmos"></a>
+ SMPTE 2110 inputs and outputs with JPEG XS now support NMOS. Previously, only uncompressed inputs supported NMOS. (SOCK-36952)
+ SMPTE 2110 outputs with JPEG XS now support NMOS. The [AWS Elemental Live User Guide](https://docs.aws.amazon.com/elemental-live/latest/ug/) has been updated. (SOCK-36953)

### SMPTE 2110 – passthrough of Dolby Digital audio (SOCK-37345)
<a name="rn-2-22-2110-dd-passthrough"></a>

Elemental Live now supports passthrough of the Dolby Digital audio codec from any input to a SMPTE 2110 output. This passthrough applies to Dolby Digital but not to Dolby Digital Plus.

### SMPTE 2110 – improved alerts (SOCK-34046)
<a name="rn-2-22-2110-alerts"></a>

Elemental Live now includes more alerts and validation messages for problems with configuring or processing SMPTE 2110 inputs.

### Statmux – PID passthrough (SOCK-37020)
<a name="rn-2-22-statmux-pid-passthrough"></a>

Statmux now supports passthrough of PIDs. With passthrough, you identify one or more passthrough PIDs in any transport stream in the Statmux. Statmux extracts those PIDs, remaps each PID to an outgoing PID, and includes the remapped PIDs in the outgoing MPTS.

### Trick-play track (SOCK-37312)
<a name="rn-2-22-trick-play"></a>

Elemental Live now supports an implementation of trick-play track that conforms with the Image Media Playlist specification, version 0.4. Previously, you could implement trick-play track only using I-frames. Both these trick-play implementations apply only to HLS output groups.

The new feature encodes a series of JPEG thumbnails, one per video segment, along with the standard video segments. This thumbnail implementation provides a better user experience when the user is fast forwarding or rewinding in a downstream player. The player can show a preview of the video rather than showing a frozen screen until the fast forward or rewind is complete.

The [AWS Elemental Live User Guide](https://docs.aws.amazon.com/elemental-live/latest/ug/) has been updated to document this feature.

### Alerts, messages, and logs
<a name="rn-2-22-alerts-logs"></a>
+ Elemental Live now logs messages when inserting HLS timed metadata in response to a schedule action. Elemental Live also submits with a DTS of 0 for late-processed injection requests, for slightly improved latency. (SOCK-37480)
+ A log message has been added to notify you when the port for a UDP source changes more than twice within five seconds. Frequent switching of a port can indicate that two different upstream systems are sending to the same input, when only one system should be sending. (SOCK-37465)
+ The "HTTP Transfer Failed" alert now clears immediately if the next transfer attempt succeeds, or clears after 30 seconds in other situations. (SOCK-37472)
+ Conductor Live – There is now a CL3 alert when a failover causes a node replacement. The alert is active for 1–2 minutes, then automatically clears itself. (SC-78)

### Captions – 608 captions and extended character set (SOCK-37474)
<a name="rn-2-22-captions-608"></a>

If source 608 captions include characters from an extended character set, those characters are now passed through as is to a captions output.

### HLS manifests for SCTE-35 (SOCK-37466)
<a name="rn-2-22-hls-scte35"></a>

There has been a change to the base64 in SCTE-35 data in HLS manifests that are type SCTE-35 enhanced. (This is the only manifest type that includes the base64 data.) The values for PTS adjustment, PTS, and duration now match the output clock. Previously, they incorrectly matched the source base64 data.

### Support for field pictures (SOCK-37468)
<a name="rn-2-22-field-pictures"></a>

Elemental Live now supports input sources encoded as field pictures.

### QVBR enhancement (SOCK-37479)
<a name="rn-2-22-qvbr"></a>

There is now a default value for the **Buffer Size** in the video stream (encode) for H.264 and H.265, when you set the **Rate Control Mode** field to QVBR. The buffer size is set to be 2 times the max bitrate.

### Firmware upgrade (SOCK-37222)
<a name="rn-2-22-firmware"></a>

The NIC driver firmware has been upgraded to resolve issues on appliances that include a 1 GbE copper (Cu) SFP interface. These issues occur on specific appliances in the L800 series. The issues include the following:
+ After the interface disconnects, the link status of the interface doesn't update to show the new state. (SOCK-36051)
+ The link status of the interface doesn't correctly identify that it is in a bond. (SOCK-36779)
+ The interface can unexpectedly perform a link renegotiation, resulting in a link speed dropping from 1000 Mbps to 100 Mbps.

All these problems are resolved by the firmware upgrade. The firmware upgrade is automatically performed when you install Elemental Live version 2.20.0 or later.

### Producing output captions using OCR conversion (SOCK-37031)
<a name="rn-2-22-ocr"></a>

Elemental Live now supports optical character recognition (OCR) conversion of captions. OCR lets you convert image-based source captions to text-based output captions. Specifically, you can configure your Elemental Live event to convert DVB Sub and SCTE-27 source captions to WebVTT output captions.

For the list of languages that this conversion feature supports, see [Languages supported with OCR](#rn-2-22-ocr-languages).

Currently, to use this feature, you must set the environment variable `ENABLE_OCR_DVBSUB_OR_SCTE27` as follows:

```
ENABLE_OCR_DVBSUB_OR_SCTE27=TRUE
```

To set the variable, search the knowledge articles in the [AWS Elemental Support Center](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/supportcenter) for *How to add environment variables in CentOS 7/RHEL 7 from the CLI*. You must have an AWS account to access the AWS Elemental Support Center.

### Languages supported with OCR
<a name="rn-2-22-ocr-languages"></a>

The following list shows the languages that OCR captions conversion supports.
+ Afrikaans
+ Albanian
+ Amharic
+ Arabic
+ Assamese
+ Azerbaijani
+ Azerbaijani - Cyrillic
+ Basque
+ Belarusian
+ Bengali
+ Bosnian
+ Bulgarian
+ Burmese
+ Catalan; Valencian
+ Cebuano
+ Central Khmer
+ Cherokee
+ Chinese - Simplified
+ Chinese - Simplified Vertical
+ Chinese - Traditional
+ Chinese - Traditional Vertical
+ Croatian
+ Czech
+ Danish
+ Dutch; Flemish
+ Dzongkha
+ English
+ English, Middle (1100-1500)
+ Esperanto
+ Estonian
+ Finnish
+ French
+ French, Middle (ca. 1400-1600)
+ Galician
+ Georgian
+ Georgian - Old
+ German
+ German - Fraktur
+ Greek, Ancient (-1453)
+ Greek, Modern (1453-)
+ Gujarati
+ Haitian; Haitian Creole
+ Hebrew
+ Hindi
+ Hungarian
+ Icelandic
+ Indonesian
+ Inuktitut
+ Irish
+ Italian
+ Italian - Old
+ Japanese
+ Japanese Vertical
+ Javanese
+ Kannada
+ Kazakh
+ Kirghiz; Kyrgyz
+ Korean
+ Korean Vertical
+ Lao
+ Latin
+ Latvian
+ Lithuanian
+ Macedonian
+ Malay
+ Malayalam
+ Maltese
+ Marathi
+ Nepali
+ Norwegian
+ Oriya
+ Panjabi; Punjabi
+ Persian
+ Polish
+ Portuguese
+ Pushto; Pashto
+ Romanian; Moldavian; Moldovan
+ Russian
+ Sanskrit
+ Serbian
+ Serbian - Latin
+ Sinhala; Sinhalese
+ Slovak
+ Slovenian
+ Spanish; Castilian
+ Spanish; Castilian - Old
+ Swahili
+ Swedish
+ Syriac
+ Tajik
+ Tamil
+ Telugu
+ Thai
+ Tibetan
+ Tigrinya
+ Turkish
+ Uighur; Uyghur
+ Ukrainian
+ Urdu
+ Uzbek
+ Uzbek - Cyrillic
+ Vietnamese
+ Welsh

### Nielsen watermark encoding (SOCK-36314)
<a name="rn-2-22-nielsen"></a>

Elemental Live now supports insertion of Nielsen watermarks in audio outputs using the NAES II, NAES VI, and CBET watermarking algorithms. Nielsen audio watermarking is the process of inserting watermark codes into the audio signal to measure content viewership. These codes are inaudible to the human ear, but are detected by Nielsen meters in the downstream devices.

The Nielsen watermark contains a timestamp and an identifier (SID) that is unique for each broadcast channel. The Nielsen audio watermarking feature supports audio streams with the following characteristics:
+ Frequency of 48 kHz (48000 samples per second)
+ Up to 8 audio channels, with interleaved samples

This feature requires a new paid add-on pack license from AWS Elemental Live. The Elemental Live implementation has completed the official certification process with Nielsen.

### L800 series appliances – performance improvements (SOCK-37348)
<a name="rn-2-22-l800"></a>

Elemental Live on L800 series appliances now produces higher channel density in workflows with 1080 ABR outputs.

### SMPTE 2110 Dolby Digital audio (SOCK-37288)
<a name="rn-2-22-2110-dd-audio"></a>

SMPTE 2110 inputs and outputs now support 5.1 coding mode in Dolby Digital and Dolby Digital Plus audio. This functionality is part of SMPTE 2110-31.

### Statmux latency improvements
<a name="rn-2-22-statmux-latency"></a>

A Statmux MPTS can now achieve an additional 500 ms latency reduction. To configure for this reduction, enter a lower value in the maximum video buffer delay setting on the MPTS.

## New features in Conductor Live 3.22
<a name="rn-2-22-features-cl3"></a>

Conductor Live 3.22 includes the following new feature.

### Alerts, messages, and logs (SC-78)
<a name="rn-2-22-cl3-failover-alert"></a>

There is now a CL3 alert when a failover causes a node replacement. The alert is active for 1–2 minutes, then automatically clears itself.