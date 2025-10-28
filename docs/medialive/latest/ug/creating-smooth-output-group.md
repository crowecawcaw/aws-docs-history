# Create a Microsoft Smooth output

group

When you [planned
the workflow for your channel](identify-downstream-system.md "identify-downstream-system.md"), you might have
determined that you want to include a Microsoft Smooth output
group.

## The procedure

1. On the **Create channel** page, in the **Output
   groups** section, choose **Add**.
2. In the **Add output group** section, choose
   **Microsoft Smooth**, and then choose
   **Confirm**. More sections appear:
   - **Microsoft Smooth group destination** –
     This section contains fields for the [destination of the
     outputs](smooth-destinations.md "smooth-destinations.md").
   - **Microsoft Smooth settings** – This
     section contains fields for the [container](smooth-container.md "smooth-container.md"), the [connection to the downstream system](smooth-destinations.md "smooth-destinations.md"), and [resiliency](mss-other-fields.md#smooth-resiliency "mss-other-fields.md#smooth-resiliency").
   - **Microsoft Smooth outputs** – This section
     shows the single output that is added by default.
   - **Event configuration** – This section
     contains fields for the [destination of the outputs](smooth-destinations.md "smooth-destinations.md") and the[container](smooth-container.md "smooth-container.md").
   - **Timecode configuration** – This section
     contains fields for the [timecode](mss-other-fields.md#smooth-timecode "mss-other-fields.md#smooth-timecode") in the outputs.
   - **Sparse track** – This section contains
     fields for the [container](smooth-container.md "smooth-container.md").

3. If your plan includes more than one output in this output group, then in
   **Microsoft Smooth outputs**, choose **Add
   output** to add the appropriate number of outputs.
4. In **Microsoft Smooth outputs**, choose the first
   **Settings** link to view the sections for the first
   output:
   - **Output settings** – This section contains
     fields for the [output
     destination](smooth-destinations.md "smooth-destinations.md"), and the [container](smooth-container.md "smooth-container.md").
   - **Stream settings** – This section contains
     fields for the [output
     streams](smooth-streams-section.md "smooth-streams-section.md") (the video, audio, and captions).

5. (Optional) Enter names for the output group and the outputs:
   - In **Microsoft Smooth settings**, for
     **Name**, enter a name for the output group.
     This name is internal to MediaLive; it doesn't appear in the output. For
     example, `Sports Curling`.
   - In the **Output settings** section for each
     output, for **Output name**, enter a name for the
     output. This name is internal to MediaLive; it doesn't appear in the
     output. For example, `high resolution`.

6. To complete the other fields, see the topics listed after this
   procedure.
7. After you have finished setting up this output group and its outputs, you
   can create another output group (of any type), if your plan requires it.
   Otherwise, go to [Save the channel](creating-a-channel-step9.md "creating-a-channel-step9.md").

###### Topics
