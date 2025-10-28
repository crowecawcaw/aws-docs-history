# Creating a UDP

output group

When you [planned
the workflow for your channel](identify-downstream-system.md "identify-downstream-system.md"), you might have
determined that you want to include a UDP output group.

1. On the **Create channel** page,
   under **Output groups**, choose
   **Add**.
2. In the **Add output group**
   section, choose **UDP**, and then
   choose **Confirm**. More sections
   appear:
   - **UDP destination**
     – This section contains fields for the
     [output
     destination](udp-destinations.md "udp-destinations.md").
   - **UDP settings** –
     This section contains fields for [setting up
     ID3](udp-other.md "udp-other.md") and for [resiliency](udp-other.md "udp-other.md").
   - **UDP outputs** –
     This section shows the single output that is
     added by default. A UDP output can contain
     only one output, so don't click
     **Add output**.

3. In **UDP outputs**,
   choose the **Settings**
   link to view the sections for the output:
   - **Output settings**
     – This section contains fields for the
     [transport](udp-destinations.md "udp-destinations.md") and the [connection to
     the destination](udp-destinations.md "udp-destinations.md").
   - **Stream settings**
     – This section contains fields for the
     [output
     streams](udp-streams.md "udp-streams.md") (the video, audio, and
     captions).

4. (Optional) Enter names for the output group and
   the output:
   - In **UDP settings**, for
     **Name**, enter a name
     for the output group. This name is internal
     to MediaLive; it doesn't appear in the output.
     For example, `Sports
Game`.
   - In **UDP output**, in
     **Output settings**,
     for **Output name**, enter
     a name for the output. This name is internal
     to MediaLive; it doesn't appear in the
     output.

5. To complete the other fields, see the topics
   listed after this procedure.
6. After you have finished setting up this output
   group and its single output, you can create another
   output group (of any type), if your plan requires
   it. Otherwise, go to [Save the channel](creating-a-channel-step9.md "creating-a-channel-step9.md").

###### Topics

- [Fields for the output
  destination](udp-destinations.md "udp-destinations.md")
- [Fields for the UDP
  transport](udp-container.md "udp-container.md")
- [Fields for the video, audio,
  and captions stream (encode)](udp-streams.md "udp-streams.md")
- [Fields for other UDP
  features](udp-other.md "udp-other.md")
