# General procedure for handling color

space

The procedure for handling color space in the channel is the same for both passing through
and converting the color space in the outputs.

1.  You must assess the color space in all the inputs, and determine if you can handle the
    color space according to your preference. See [Assess the color spaces in the sources](color-space-assess-inputs.md "color-space-assess-inputs.md").
2.  You must assess the source to make sure the color space metadata is correct.

        * For passthrough: If you plan to include the color space metadata, you must assess
         it. If the metadata isn't correct, downstream players won't handle the color space
         correctly.
        * For conversion: MediaLive reads this metadata to determine the color space of the
         source, so that it can apply the correct conversion formula. Therefore, even if you
         plan to remove the metadata in the outputs, you must assess the metadata.

    See [Assess the color space metadata in the
    sources](color-space-input-procedure.md "color-space-input-procedure.md").

3.  If you need to correct the color space metadata, you do so in the input. You configure
    each input separately.

See [Options for correcting metadata](color-space-cleanup-scenarios.md "color-space-cleanup-scenarios.md"). 4. Set up the output to pass through or convert the color space, and to include or omit
the color space metadata. See [Configuring color space handling in each
output](color-space-output-handling.md "color-space-output-handling.md").
