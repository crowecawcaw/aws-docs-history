# Create a CMAF Ingest output group

You create the output group and its outputs when you [create or edit a MediaLive channel](creating-a-channel-step4.md "creating-a-channel-step4.md").

1. On the **Create channel** or **Edit
   channel** page, in **Output groups**, choose
   **Add**.
2. In the **Add output group** section, choose
   **CMAF Ingest**, and then choose
   **Confirm**. More sections appear:
   - **CMAF Ingest destination** – This section
     contains fields for the destination of the outputs. You should have
     obtained the URLs to enter when you [planned the destinations for
     the CMAF Ingest output group](downstream-system-cmafi-empv2.md "downstream-system-cmafi-empv2.md"). The URL looks like this:

   `https://mz82o4-1.ingest.hnycui.mediapackagev2.us-west-2.amazonaws.com/in/v1/curling-channel-group/1/curling-channel/`

   Leave the **Credentials** section empty. You don't
   need to enter credentials to authenticate with MediaPackage.
   - **CMAF Ingest settings** – This section
     contains fields for configuring how segments are delivered and for
     configuring how various features behave. See later in this
     section.
   - **CMAF Ingest outputs** – This section
     shows the single output that is added by default. You can add more
     outputs, and you can add video, audio, and captions encodes in each
     output. See later in this section.

###### Topics

- [Fields in CMAF Ingest settings section](#cmafi-opg-settings "#cmafi-opg-settings")
- [Fields for the video, audio, and
  captions streams (encodes)](#cmafi-opg-streams-section "#cmafi-opg-streams-section")

## Fields in CMAF Ingest settings section

| Field                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name                                 | A name for the output group. This name is internal to MediaLive. It<br>doesn't appear in the output. For example, `Sports<br>Curling`.                                                                                                                                                                                                                                                                                                                                    |
| SCTE35 Type                          | To pass through SCTE 35 messages in the output group, choose<br>**SCTE_35_WITHOUT_SEGMENTATION**.The<br>WITHOUT_SEGMENTATION wording indicates that each inserted SCTE<br>35 message will result in a new IDR in the video, but it won't<br>result in a new segment. This handling is standard for CMAF<br>Ingest For more information about setting up for<br>SCTE 35, see [Processing SCTE 35 messages](scte-35-message-processing.md "scte-35-message-processing.md"). |
| Segment Length, Segment Length Units | Enter the preferred duration of segments (in milliseconds or<br>seconds). The segments will end on the next keyframe after the<br>specified duration, so the actual segment duration might be<br>longer. If the units are seconds, the duration might be a<br>fraction of the seconds.                                                                                                                                                                                    |
| Send Delay Msec                      | Number of milliseconds to delay the output from pipeline 1,<br>when the channel starts or unpauses. (This field applies only to<br>standard channels. The value is ignored in a single-pipeline<br>channel.)<br>Some packagers always ingest the first pipeline that they<br>receive. You can therefore set a value here to ensure that<br>pipeline 0 always arrives at the packager first.                                                                               |
| Nielsen ID3 Behavior                 | For information about this feature, see [Converting Nielsen watermarks to ID3](feature-nielsen-id3.md "feature-nielsen-id3.md").                                                                                                                                                                                                                                                                                                                                          |

## Fields for the video, audio, and

captions streams (encodes)

1. In **CMAF Ingest outputs**, choose **Add
   output** to add the appropriate number of outputs to the list
   of outputs.
2. Choose the first **Settings** link to view the first
   output. Each output has two sections: **Output settings**
   and **Stream settings**.
3. Complete **Output settings**:
   - **Output name**: Change the randomly generated
     name to a meaningful name. This name is internal to MediaLive; it
     doesn't appear in the output.
   - **Name modifier**: MediaLive assigns a sequential
     modifier to each output in the output group:
     **\_1**, **\_2**, and so on. Change
     the name if you want.

4. Complete **Stream settings**. This section contains
   fields for the output encodes (the video, audio, and captions) to create in
   the output. For information about creating encodes, see the following
   sections:
   - [Set up the video encode](creating-a-channel-step6.md "creating-a-channel-step6.md")
   - [Set up the audio encodes](creating-a-channel-step7.md "creating-a-channel-step7.md")
   - [Set up the captions encodes](creating-a-channel-step8.md "creating-a-channel-step8.md")
