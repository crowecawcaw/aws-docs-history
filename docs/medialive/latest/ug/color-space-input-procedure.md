# Assess the color space metadata in the

sources

Before you can set up the outputs, you must determine if you need to modify the color
space metadata in the inputs. To make this decision, you must assess the quality of the
metadata in the inputs.

###### Important

The handling on the input side of the event is about changing the color space
metadata, not changing the color space itself. The handling is about changing the metadata
to correctly identify the color space in the input, in preparation for the planned
handling in the outputs.

The conversion of the video to a different color space occurs in [Configuring color space handling in each
output](color-space-output-handling.md "color-space-output-handling.md").

###### To assess the inputs

1. You should have already obtained information about the accuracy of the color space
   metadata in all the inputs.
2. Make a note of the presence and accuracy of the metadata for all the color spaces in
   all the inputs.

The color space metadata is accurate if the following applies:

    * It is present in the input and it accurately identifies the color space, which
     means that the color space is accurately marked.

The color space metadata might be present, but it might be inaccurate in one or more
ways:

    * Incorrect: The metadata doesn't match the color space.
    * Unknown: The metadata marks the color space as *unknown*.
    * Not supported: The metadata specifies a color space that MediaLive [doesn't support](color-space-standards.md "color-space-standards.md"). MediaLive doesn't read this
     metadata.
    * Missing: All or part of the video might not have color space metadata.

3.  This step applies only for the following situation:

        * The input is for a MediaLive device such as AWS Elemental Link.
        * The input color space is HDR10.
        * You plan to pass through the color space to the output.

    Obtain the values for the Max CLL and Max FALL for the content.

MediaLive can't read the metadata from an AWS Elemental Link device. But you will be able to enter
the color space and the display metadata (Max CLL and Max FALL) manually, in the channel
configuration.

You don't need these values if you plan to convert this input from HDR10 to another
color space.
