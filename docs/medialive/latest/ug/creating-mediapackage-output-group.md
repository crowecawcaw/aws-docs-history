# Create a MediaPackage output

group

When you [planned
the workflow for your channel](identify-downstream-system.md "identify-downstream-system.md"), you might have determined
that you want to include a MediaPackage output group. (Or you might
have decided to use an [HLS
output group to deliver to MediaPackage](hls-destinations-emp.md "hls-destinations-emp.md").)

## The procedure

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
   that channel. For example, `curlinglive`.
4. (Optional) In the **MediaPackage settings** section, for
   **Name**, enter a name for the output group.
5. If your plan includes more than one output in this output group, then in
   **MediaPackage outputs**, choose **Add output** to add the appropriate number of
   outputs.

You might want to add an output in order to implement trick-play. For more
information about this feature and for instructions on setting it up in the
channel, see [Trick-play track via the Image
Media Playlist specification](trick-play-roku.md "trick-play-roku.md"). 6. Choose the first **Settings** link to view the sections
for the first output. The section contains fields for the [output streams](hls-streams-section.md "hls-streams-section.md") (the video, audio,
and captions). 7. After you have finished setting up this output group and its outputs, you
can create another output group (of any type), if your plan requires it.
Otherwise, go to [Save the channel](creating-a-channel-step9.md "creating-a-channel-step9.md").

Topics
