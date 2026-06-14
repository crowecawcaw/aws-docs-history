# Create a MediaConnect Router output group

You create the output group and its outputs when you [create or edit a MediaLive channel](creating-a-channel-step4.md "creating-a-channel-step4.md").

1. On the **Create channel** or **Edit
   channel** page, in **Output groups**, choose
   **Add**.
2. In the **Add output group** section, choose
   **MediaConnect Router Output Group**, and then choose
   **Confirm**. More sections appear:

   - **MediaConnect Router Output Group** destination
     – This section contains fields for the destination of the outputs.
     In the Output Destinations section, a **MediaConnect Router
     Output Group** tab appears. The encryption type defaults to
     **AUTOMATIC**. To use a secret from AWS Secrets Manager, change
     the encryption type to **SECRETS_MANAGER** and enter
     the secret ARN.
   - **MediaConnect Router settings** – This section
     contains fields for configuring the output group. See later in this
     section.
   - **MediaConnect Router outputs** – This section
     shows the single output that is added by default. You can add more
     outputs (up to five per output group), and you can add video, audio, and
     captions encodes in each output. See later in this section.

###### Topics

- [Fields in MediaConnect Router settings section](#mediaconnect-router-opg-settings "#mediaconnect-router-opg-settings")
- [Fields for the video, audio, and captions streams (encodes)](#mediaconnect-router-opg-streams-section "#mediaconnect-router-opg-streams-section")

## Fields in MediaConnect Router settings section

| Field                   | Description                                                                                                                                                                                                                                                        |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Name                    | A name for the output group. This name is internal to MediaLive. It<br>doesn't appear in the output.                                                                                                                                                               |
| Availability Zones      | The Availability Zones for the output group. For a<br>single-pipeline channel, specify one Availability Zone. For a<br>standard channel, specify two different Availability Zones. The two<br>Availability Zones must be different to provide zonal<br>resiliency. |
| Connected Router Inputs | A read-only field that shows the MediaConnect Router inputs that<br>are connected to this output. This information is purely<br>informational. To connect or disconnect MediaConnect Router inputs,<br>use the MediaConnect Router API.                            |

## Fields for the video, audio, and captions streams (encodes)

1. In **MediaConnect Router outputs**, choose
   **Add output** to add outputs.
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

4. In **Output settings**, for **Container
   settings**, the container is set to M2TS. For information about
   M2TS settings, see the M2TS fields in [Fields for the UDP transport](udp-container.md "udp-container.md").
5. Complete **Stream settings**. This section contains
   fields for the output encodes (the video, audio, and captions) to create in
   the output. For information about creating encodes, see the following
   sections:

   - [Set up the video encode](creating-a-channel-step6.md "creating-a-channel-step6.md")
   - [Set up the audio encodes](creating-a-channel-step7.md "creating-a-channel-step7.md")
   - [Set up the captions encodes](creating-a-channel-step8.md "creating-a-channel-step8.md")
