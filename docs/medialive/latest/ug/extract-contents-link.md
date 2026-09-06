

# Identifying content in an AWS Elemental Link source
<a name="extract-contents-link"></a>

The content in an AWS Elemental Link source is always a transport stream (TS) that contains one video asset, one audio pair, and optional captions. 

Obtain identifying information from the content provider.




- **Video**
  - **Details:** You don't need identifying information. MediaLive always extracts the single video asset.
  - **Format of information to obtain:** None

- **Audio**
  - **Details:** The source might include multiple audio tracks, typically, one for each language. 
  - **Format of information to obtain:** Obtain the numbers and languages of the tracks. For example, "track 1 is French". 

- **Captions**
  - **Details:** ARIB / **Format of information to obtain:** You don't need any information. With ARIB captions, MediaLiveextracts all the languages.
  - **Details:** Embedded / **Format of information to obtain:** Obtain the languages of the channels. For example, "channel 1 is French". 
  - **Details:** Teletext / **Format of information to obtain:** [If your plan for teletext captions](assess-uss-captions.md) is to convert the captions to a different format, you must obtain the page numbers for the languages that you want to convert. If you plan to pass through the captions as Teletext in the output, you don't need any identifiers.



Also obtain the following information about the content:
+ The maximum bitrate. You will have the option to throttle this bitrate when you set up the device in MediaLive. For more information, see [Setting up AWS Elemental Link](setup-devices.md). 
+ Whether the content includes an embedded timecode. If it does, you can choose to use that timecode. For more information, see [Timecode configuration](https://docs.aws.amazon.com/medialive/latest/ug/timecode.html)[Working with timecodes and timestamps](timecode.md). 
+ Whether the content includes ad avail messages (SCTE-104 messages that MediaLive will automatically convert to SCTE-35 messages). For more information about ad avail messages, see [Processing SCTE 35 messages](scte-35-message-processing.md).