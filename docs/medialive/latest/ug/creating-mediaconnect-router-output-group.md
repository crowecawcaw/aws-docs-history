

# Create a MediaConnect Router output group
<a name="creating-mediaconnect-router-output-group"></a>

You create the output group and its outputs when you [create or edit a MediaLive channel](creating-a-channel-step4.md). 

1. On the **Create channel** or **Edit channel** page, in **Output groups**, choose **Add**. 

1. In the **Add output group** section, choose **MediaConnect Router Output Group**, and then choose **Confirm**. More sections appear:
   + **MediaConnect Router Output Group** destination – This section contains fields for the destination of the outputs. In the Output Destinations section, a **MediaConnect Router Output Group** tab appears. The encryption type defaults to **AUTOMATIC**. To use a secret from AWS Secrets Manager, change the encryption type to **SECRETS\_MANAGER** and enter the secret ARN.
   + **MediaConnect Router settings** – This section contains fields for configuring the output group. See later in this section.
   + **MediaConnect Router outputs** – This section shows the single output that is added by default. You can add more outputs (up to five per output group), and you can add video, audio, and captions encodes in each output. See later in this section.

**Topics**
+ [Fields in MediaConnect Router settings section](#mediaconnect-router-opg-settings)
+ [Fields for the video, audio, and captions streams (encodes)](#mediaconnect-router-opg-streams-section)

## Fields in MediaConnect Router settings section
<a name="mediaconnect-router-opg-settings"></a>


| Field | Description | 
| --- | --- | 
| Name | A name for the output group. This name is internal to MediaLive. It doesn't appear in the output. | 
| Availability Zones | The Availability Zones for the output group. For a single-pipeline channel, specify one Availability Zone. For a standard channel, specify two different Availability Zones. The two Availability Zones must be different to provide zonal resiliency. | 
| Connected Router Inputs | A read-only field that shows the MediaConnect Router inputs that are connected to this output. This information is purely informational. To connect or disconnect MediaConnect Router inputs, use the MediaConnect Router API. | 

## Fields for the video, audio, and captions streams (encodes)
<a name="mediaconnect-router-opg-streams-section"></a>

1. In **MediaConnect Router outputs**, choose **Add output** to add outputs.

1. Choose the first **Settings** link to view the first output. Each output has two sections: **Output settings** and **Stream settings**.

1. Complete **Output settings**:
   + **Output name**: Change the randomly generated name to a meaningful name. This name is internal to MediaLive; it doesn't appear in the output. 
   + **Name modifier**: MediaLive assigns a sequential modifier to each output in the output group: **\_1**, **\_2**, and so on. Change the name if you want. 

1. In **Output settings**, for **Container settings**, the container is set to M2TS. For information about M2TS settings, see the M2TS fields in [Fields for the UDP transport](udp-container.md).

1. Complete **Stream settings**. This section contains fields for the output encodes (the video, audio, and captions) to create in the output. For information about creating encodes, see the following sections:
   + [Set up the video encode](creating-a-channel-step6.md)
   + [Set up the audio encodes](creating-a-channel-step7.md)
   +  [Set up the captions encodes](creating-a-channel-step8.md)