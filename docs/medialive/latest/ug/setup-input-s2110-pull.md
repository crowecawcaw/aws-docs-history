

# Create a SMPTE 2110 input
<a name="setup-input-s2110-pull"></a>

After you have obtained information from the upstream system, you can create a SMPTE 2110 input.

**To create an SMPTE 2110 input**

1. Make sure that you have the information from [step 1](setup-s2110-pull-obtain-info.md).

1. Open the MediaLive console at [https://console.aws.amazon.com/medialive/](https://console.aws.amazon.com/medialive/).

1. In the navigation pane, choose **Inputs**. On the **Inputs** page, choose **Create input**.

1. Complete the **SMPTE 2110 Receiver Group** section as described in the table that follows this procedure. 

1. In the **Tags **section, create tags if you want to associate tags with this input. For more information, see [Tagging resources](tagging.md).

1. Choose **Create**.

   MediaLive creates the input and adds it to the list of inputs. The input identifies the locations of the SDP files that contain information about the SMPTE 2110 streams. 

   When you start the channel, MediaLive will retrieve the SDP files. It will obtain the location of the SMPTE 2110 streams from the files. It will connection to those locations and pull the content that you specified when you [attach the input to the channel](creating-a-channel-step2.md).

**Fields for a SMPTE 2110 input**


| Field | Description | 
| --- | --- | 
| Video SDP | Enter the URL for the video SDP file. If you obtained a number that identifies the video line to extract, enter it in the Media index field. <br />This index is zero-based. So if you need to extract the third line, enter 2. | 
| Audio SDPs | Enter information for each for each audio SDP file and audio line combination.See the example after this table. | 
| Ancillary SDPs | Enter information for each for each ancillary SDP file and audio line combination.See the example after this table. | 

You might have obtained the following information about the SDP files and their media lines:
+ One video file at `http://172.18.8.19/curling_video.sdp`. You need to extract the third video (index member 2).
+ The following audio SDP files and their audio lines:

  `http://172.18.8.19/curling_audio_1.sdp` with one audio line. 

  `http://172.18.8.19/curling_audio_2.sdp`, with two media lines.
+ One ancillary SDP file and their ancillary lines:

  `http://172.18.8.19/curling_ancill.sdp` with two media lines.

You will set up the Receiver Group fields as follows:


| SDP | SDP URL | Media index | 
| --- | --- | --- | 
| Video SDP | http://172.18.8.19/curling\_video.sdp | 2 | 
| Audio SDP | http://172.18.8.19/curling\_audio\_1.sdp | 0 | 
|  | http://172.18.8.19/curling\_audio\_2.sdp | 0 | 
|  | http://172.18.8.19/curling\_audio\_2.sdp | 1 | 
| Ancillary SDP  | http://172.18.8.19/curling\_ancill.sdp | 0 | 
|  | http://172.18.8.19/curling\_ancill.sdp | 0 | 