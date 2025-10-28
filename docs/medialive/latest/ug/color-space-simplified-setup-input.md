# Configuring the inputs

###### Note

This section assumes that you are familiar with creating or editing a channel, as
described in [Creating a channel from scratch](creating-channel-scratch.md "creating-channel-scratch.md").

This section describes how to set up each of the sources (inputs) in a MediaLive channel. It applies both when
you pass through the color space to the output and when you convert the color space.

Follow these steps for each input in the channel.

1.  Make sure that your inputs comply with [the requirements](color-space-simplified-supported-inputs.md "color-space-simplified-supported-inputs.md").
2.  On the **Create channel** page, in the **Input
    attachment** section for the input, in the **General input
    settings** section, group, open the **Video selector** field.
3.  Set these fields:

        * **Color space**: Choose **Follow**.


        (The other options apply only to [complicated color
         space situations](color-space.md "color-space.md").)


        * **Color space usage**: Leave the default. This field is ignored
         when you set **Color space** to **Follow**.

    This combination of values indicates that the color space metadata in the content
    correctly identifies the color space, therefore MediaLive can use that metadata.

4.  Obtain the values for the Max CLL and Max FALL for the content, but only if the
    following situation applies:

        * The input is for a MediaLive device such as AWS Elemental Link.
        * The input color space is HDR10. (This means that the output from the Link
         device is HDR10.)
        * You plan to pass through the color space to the output.

    You need this information because MediaLive can't read the metadata from an AWS Elemental Link device.
    Instead, you will be able to enter the color space and the display metadata (Max CLL and
    Max FALL) manually, in the next step.

You don't need these values if you plan to convert this input from HDR10 to another
color space. 5. Complete **Color space settings** as follows:

    * If the situation in step 4 applies, choose **HDR10** (to identify
     the source color space). Then, if you obtained metadata values, enter them in the
     **Max CLL** and **Max Fall** fields that appear
     (to provide the metadata that is missing from the input).


    * If the situation doesn't apply, choose **Don't include**.
