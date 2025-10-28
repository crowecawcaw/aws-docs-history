# Step 1: Decide on the input handling

If you plan to pass through or convert the color space on the output
side of the event, you must decide whether you need to change the color
space metadata in the input.

###### Note

If you plan to remove the color space metadata from _all_ the outputs, there is no need to review the
inputs. Skip to [Converting color space: Procedure A](colorspace-output-procedure.md "colorspace-output-procedure.md").

###### To decide how to handle the color space metadata

Follow this procedure for each input.

1.  Contact the content provider of the input source to find out the
    following information:

        * Whether the input source contains a combination of different color
         spaces.
        * The name of the color space or color spaces in the input source.
        * Whether the color space metadata is accurate. It is accurate if it
         correctly identifies the color space and if it isn't missing. The
         content is most likely to be one of the following:




        	+ Correctly marked.


        	+ Unmarked (no color space metadata is present). In this case, try
        	 to find out what the probable color space is.
        The content might also be one of the following:




        	+ Incorrectly marked.
        	+ Marked as *unknown*.
        	+ Marked with a color space that Elemental Live [doesn't support](color-space-conversions.md "color-space-conversions.md") and
        	 therefore doesn't read.
        * If the color space metadata isn't accurate or is missing, and if
         the color space is HDR10, obtain the values that the content provider
         intends for the HDR10 master display metadata.
        * If you plan to convert the color space to HDR10 or Dolby Vision, find out whether the
         source video is Full Range or Video Range. You will need this information in order to
         correctly set the **Video Range** field in the output.

    If the content provider can't provide accurate information about the
    color space or its metadata, you might choose at this point to remove the
    color space metadata. Move on to the next input. Or if this is the only
    input, stop reading this section and go to [Configuring color space handling in each
    output](hdr-output.md "hdr-output.md").

2.  Make a note of the information:
    - The names of the color spaces.
    - If applicable, the values for the HDR10 display metadata.
    - If applicable, whether the source video is full range or video
      range.
