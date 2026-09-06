

# Collect information about the source content
<a name="planning-content-extract"></a>

After you have assessed the source content and have identified suitable video, audio, and captions assets in that content, you must obtain information about those assets. The information you need is different for each type of source. 

You don't need this information to [create the input](medialive-inputs.md) in MediaLive. But you will need this information when you [attach the input](creating-a-channel-step2.md) to the channel in MediaLive.

**Result of this step**  
After you have performed the procedures in this step, you should have source content information that looks like this example.


**Example**  


- ** Upstream System **
  - **Format:** RTP 
  - **Characteristics:** with FEC
  - **Identifiers:** 

- **Selected video **
  - **Format:** HEVC 
  - **Characteristics:** 1920x1080<br />5 Mbps maximum
  - **Identifiers:** PID 600

- **Selected audio**
  - **Format:** Dolby Digital 5.1  / **Characteristics:**  / **Identifiers:** Spanish in PID 720
  - **Format:** AAC 2.0 / **Characteristics:**  / **Identifiers:** Spanish in PID 746
  - **Format:** AAC 2.0  / **Characteristics:**  / **Identifiers:** French in PID 747
  - **Format:** AAC 2.0 / **Characteristics:**  / **Identifiers:** English in PID 759

- **Selected captions**
  - **Format:** Embedded / **Characteristics:**  / **Identifiers:** C1 = Spanish
  - **Identifiers:** C2 = French
  - **Identifiers:** C4 = English
  - **Format:** Teletext / **Characteristics:** 10 languages / **Identifiers:** PID 815



**Topics**
+ [Identifying content in a CDI source](extract-contents-cdi.md)
+ [Identifying content in an AWS Elemental Link source](extract-contents-link.md)
+ [Identifying content in an HLS source](extract-contents-hls.md)
+ [Identifying content in a MediaConnect source](extract-content-emx.md)
+ [Identifying content in an MP4 source](extract-contents-mp4.md)
+ [Identifying content in an RTMP source](extract-contents-rtmp.md)
+ [Identifying content in an RTP source](extract-contents-rtp.md)
+ [Identifying content in a SMPTE 2110 source](extract-contents-s2110.md)
+ [Identifying content in an SRT source](extract-contents-srt.md)