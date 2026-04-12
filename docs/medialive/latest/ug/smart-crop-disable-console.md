# Disabling smart crop using the MediaLive console

You can use the MediaLive console to modify the disable smart crop in a channel.

###### Note

The information in this section assumes that you are familiar with the general
steps for creating a channel, as described in [Creating a channel from scratch](creating-channel-scratch.md "creating-channel-scratch.md").

**To disable smart crop in all outputs**

1.  On the **Create channel** or **Edit channel
    page**, choose **AWS Elemental Inference
    settings**. The **Smart crop** section is
    automatically expanded to show a list of output groups and their video outputs.
2.  Choose the appropriate action:

        * If smart crop is the only Elemental Inference feature that is enabled on this page:
         in **State**, choose
         **DISABLED**.
        * Otherwise, in the **Smart crop** section, move the
         slider for every output group to disabled (gray).

    **To disable smart crop in individual outputs**

3.  On the **Create channel** or **Edit channel
    page**, in the **Output groups** section, select
    the output that contains the video.
4.  Display the **Stream settings** section, and choose the
    **Video** section.

        * Adjust the values in the **Width** and
         **Height** fields.
        * Open **Scaling settings**, then set **Scaling
         behavior** to a value other than
         **SMART\_CROP**.

    When you disable Elemental Inference features in a channel, MediaLive handles the resources as
    follows:

- If you disable one feature among several features, MediaLive deletes the output
  for that feature.
- If you disable all the features, MediaLive deletes the feed, including its
  outputs. When the feed is deleted, its status changes to Archived. The feed
  can't become Active again.
