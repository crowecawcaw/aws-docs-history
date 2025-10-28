# Set up outputs to process color space

Follow this procedure to configure color space handling in each MediaLive output. You can set up
each output with different color space handling. For example, you can create one output that
passes through the original color space, and another that converts it.

###### Note

This section assumes that you are familiar with creating or editing a channel, as
described in [Creating a channel from scratch](creating-channel-scratch.md "creating-channel-scratch.md").

###### Topics

- [Setting up for passthrough](#colorspace-output-setup-passthrough "#colorspace-output-setup-passthrough")
- [Setting up to convert](#colorspace-output-setup-convert "#colorspace-output-setup-convert")

## Setting up for passthrough

You can set up to pass through the source color space in one or more outputs. The key
fields to set are **Color space** and **Color
metadata**.

1. On the **Create channel** page, in the **Output groups** section, choose the output that contains the video.
2. Display the **Stream settings** section, and choose the
   **Video** section.
3. For **Codec settings**, choose a codec. For information about the
   color spaces that each codec supports, see [Supported output codecs](color-space-input-output-requirements.md#color-space-supported-output-codecs "color-space-input-output-requirements.md#color-space-supported-output-codecs").
4. Choose **Codec details**. More fields appear. Choose
   **Additional settings**. More fields appear.

In **Color metadata**, choose **Insert** or
**Ignore** to specify how you want to handle the color space
metadata. 5. Choose **Color space**. The **Color space
settings** field appears. Choose **Color space
passthrough**. (Or choose **Don't include**, which is
equivalent to **Color space passthrough**.)

## Setting up to convert

You can set up to convert the color space in one or more outputs. There are several
fields that must each be set in a specific way.

You can set up to convert the source color space in one or more outputs.

1. On the **Create channel** page, in the **Output groups** section, select the output that contains the video.
2. Display the **Stream settings** section, and choose the
   **Video** section.
3. Complete the **Width** and **Height** fields to
   specify a valid resolution. Make a note of whether you are specifying an SD, an HD, or
   a UHD resolution.
4. In **Codec settings**, choose a codec. For information about the
   color spaces that each codec supports, see [Supported output codecs](color-space-input-output-requirements.md#color-space-supported-output-codecs "color-space-input-output-requirements.md#color-space-supported-output-codecs").
5. Choose **Codec details**. More fields appear. Set the
   **Profile**, **Tier**, and
   **Level** fields, if they appear for the codec that you
   chose:
   - If the resolution is SD, enter values that suit your requirements.
   - If the resolution is an HD or UHD resolution, set the tier and level to suit
     your requirements, and set the profile as follows:
     - If the output color space will be an HDR color space, you must choose one
       of the profiles that has **10BIT** in the name.
     - If the output color space will be an SDR color space, you can choose any
       profile.

6. Choose **Color space**. The **Color space
   settings** field appears.

Set the field to the color space to convert to.

If you choose **HDR10**, the **Max CLL** and
**Max FALL** fields appear. Complete these fields to set the
display metadata. 7. Go back to **Codec details** and choose **Additional
settings**. More fields appear, including **Color
metadata**. In **Color metadata**, choose
**Insert** or **Ignore** to specify how you want
to handle the color space metadata.
