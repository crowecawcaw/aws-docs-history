# Create a MediaPackage output

group

When you [planned
the workflow for your channel](identify-downstream-system.md "identify-downstream-system.md"), you might have determined
that you want to include a MediaPackage output group. (Or you might
have decided to use an [HLS
output group to deliver to MediaPackage](hls-destinations-emp.md "hls-destinations-emp.md").)

## Create MediaPackage output groups

You can create MediaPackage output groups for two different MediaPackage versions:

- **MediaPackage v1 (HLS)** - Uses HLS ingest protocol and requires a MediaPackage channel ID
- **MediaPackage v2 (CMAF)** - Uses CMAF ingest protocol and requires MediaPackage channel group name and channel name

### MediaPackage v1 (HLS) procedure

1. On the **Create channel** page, in the **Output
   groups** section, choose **Add**. The content
   pane changes to show the **Add output** group section.
2. Choose **MediaPackage**, and then choose
   **Confirm**. More sections appear:
   - **MediaPackage destination**
   - **MediaPackage settings**
   - **MediaPackage outputs**–This section shows
     the single output that is added by default.

3. In the **MediaPackage destination** section, for
   **MediaPackage channel ID**, enter the channel ID for
   that channel. For example, `curling-live`.
4. (Optional) In the **MediaPackage settings** section, for
   **Name**, enter a name for the output group.
5. If you need to specify MediaPackage V2 group settings select it from the
   dropdown and specify settings as needed
6. If your plan includes more than one output in this output group, then in
   **MediaPackage outputs**, choose **Add output** to add the appropriate number of
   outputs.

You might want to add an output in order to implement trick-play. For more
information about this feature and for instructions on setting it up in the
channel, see [Trick-play track via the Image
Media Playlist specification](trick-play-roku.md "trick-play-roku.md"). 7. Choose the first **Settings** link to view the sections
for the first output. The section contains fields for the [output streams](hls-streams-section.md "hls-streams-section.md") (the video, audio,
and captions). 8. [Save the channel](creating-a-channel-step9.md "creating-a-channel-step9.md").

### MediaPackage v2 (CMAF) procedure

1. On the **Create channel** page, in the **Output
   groups** section, choose **Add**. The content
   pane changes to show the **Add output** group section.
2. Choose **MediaPackage**, and then choose
   **Confirm**. More sections appear:
   - **MediaPackage destination**
   - **MediaPackage settings**
   - **MediaPackage outputs**–This section shows
     the single output that is added by default.

3. In the **MediaPackage destination** section, configure the primary destination:
   1. For **Region**, select the region that contains your MediaPackage v2 channel. This defaults to your current region.
   2. For **MediaPackage channel group name**, select the MediaPackage channel group name that contains your MediaPackage v2 channel.
   3. For **MediaPackage channel name**, select your MediaPackage v2 channel.
   4. For **Endpoint ID**, select which MediaPackage ingest endpoint should receive content:
      - **ENDPOINT_1** - Content is sent to the first ingest endpoint
      - **ENDPOINT_2** - Content is sent to the second ingest endpoint

4. (Optional) To configure additional destinations for redundancy or cross-region delivery, expand the **Additional destinations** section and click **Add destination**. For each additional destination, repeat the configuration steps above, specifying the region, channel group name, channel name, and endpoint ID for each additional MediaPackage channel. Standard channels support up to two additional destinations, while single pipeline channels support one additional destination.
5. (Optional) In the **MediaPackage settings** section, for
   **Name**, enter a name for the output group.
6. If your plan includes more than one output in this output group, then in
   **MediaPackage outputs**, choose **Add output** to add the appropriate number of
   outputs.
7. Choose the first **Settings** link to view the sections
   for the first output. The section contains fields for the [output streams](hls-streams-section.md "hls-streams-section.md") (the video, audio,
   and captions). CMAF ingest outputs only allow a single stream type per output.
8. [Save the channel](creating-a-channel-step9.md "creating-a-channel-step9.md").
