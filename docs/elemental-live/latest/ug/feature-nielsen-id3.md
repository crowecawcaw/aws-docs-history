# Converting Nielsen watermarks to

ID3

If one or more inputs in an event includes Nielsen watermarks in the
audio, you have the option to set up the event to convert those watermarks
to ID3 metadata. These watermarks are part of the measurement and analytics
capabilities supported by Nielsen.

This option applies only in the following scenario:

- One or more inputs in your event includes Nielsen watermarks in the
  audio.
- Your event has at least one output group that can include the
  Nielsen ID3 tag. For example, an HLS output group.
- You know that at least some of your playback devices implement the Nielsen SDK. This SDK
  provides functionality to handle the ID3 tags.
  Converting the watermarks to ID3 tags doesn't remove the original watermarks. Outputs where you include the ID3 tags will contain both the watermark and the ID3 tags. Outputs that don't include the ID3 tags will contain only the watermark.

You can't remove the watermarks from the audio, but if your playback
devices don't implement the Nielsen SDK, the devices ignore the
watermarks.

###### To set up watermarks as ID3 tags

###### Note

The information in this section assumes that you are familiar with
the general steps for creating an event. It also assumes that you have
already set up the output groups that will contain the ID3 tags.

1.  On the **Event** page of the web
    interface, go to the **Nielsen Configuration** section.
    This section is before the **Global Processors**
    section.
2.  Set the fields to enable and configure the feature:

        * **Enable Nielsen PCM to ID3 tagging**: Choose
         the check box to enable the feature.
        * **Distributor ID**: This field appears when you
         enable the feature. Optionally, enter the distributor ID that you
         obtained from Nielsen. If you enter an ID here, it is added to the
         ID3 metadata along with the source ID (SID) that is always in the
         source watermark.

    Information following these fields describes the supported Nielsen
    SDK and the vendor ID that ID3 tags will use.

3.  Go to the output group where you want to include the ID3 tags. The
    output group must be an Archive, Apple HLS, or UDP/TS group. You can set
    up one or more output groups to include ID3 tags.
4.  If the output group doesn't have an output, choose the **Add
    Output** button. An **Outputs** section
    appears.
5.  In the **Outputs** section, take the appropriate
    action:
    - For an Archive output group, in **Container**,
      choose **MPEG-2 Transport Stream**. This is the
      only type of container that supports ID3 tags.
    - For an Apple HLS output group, in **Segment
      Type**, choose **TS**. This is the only
      segment type that supports ID3 tags.
    - For a UDP/TS output group, you don't need to set
      anything.

6.  Open the **PID Control** section to see more
    fields, including **Nielsen ID3**.
7.  In **Nielsen ID3**, choose the check box to enable
    passthrough in this output.
