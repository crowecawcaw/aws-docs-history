# Step 3: Plan captions

for the outputs

If you followed the instructions in [Step 1: Identify the
source captions that you want](identify-captions-in-the-input.md "identify-captions-in-the-input.md"),
you should have a list of the captions formats and languages that will be available for
inclusion in the outputs.

You must now plan the captions information for the outputs.

###### To plan captions for the outputs

1. Identify the types of output media that you plan to create in the event. For
   example, MS Smooth and HLS.
2. Identify the streams (the combinations of video and audio) that you plan to create
   for each output media.
3. Map each output to the stream it uses. For example:
   - HLS (Output 1) uses video/audio Stream 1.
   - DASH (Output 2) also uses video/audio Stream 1. (Or it might need its own stream
     if the video requirements are different.)

4. For each output media, identify which input captions will be converted to which
   output formats. For example, you might convert teletext captions to TTML for the MS
   Smooth output media, and those same teletext captions to WebVTT for the HLS output
   media.

The output formats that are possible depend on the input formats and the type of
output media. See [Reference: Supported captions](supported-captions.md "supported-captions.md") to determine which output captions are possible given the input format. 5. Identify the languages for each output format:

    * In general, count each language separately.
    * Exception: For embedded passthrough, count all languages as one.
    * Exception: For teletext passthrough, count all languages as one.

###### The Result

You end up with a list of outputs, and the captions formats and languages for each
output. For example:

- MS Smooth output with TTML captions in Czech
- MS Smooth output with TTML captions in Polish
- HLS output with WebVTT captions in Czech
- HLS output with WebVTT captions in Polish.

## Planning for Output in Multiple Formats

You can include captions from two or more different formats in an output. For example,
you can include both embedded captions and WebVTT captions in an HLS output, to give the
downstream system more choices about which captions to use. The only rules for multiple
formats are the following:

- The output container must support all the formats. See [Reference: Supported captions](supported-captions.md "supported-captions.md").
- The font styles in all the captions that are associated with an output must match.
  This means that the end result must be identical, not that you must use the same
  option to get that result. For example, all captions that are associated with the
  output must be white for the first language and blue for the second language.

Managing this style matching can be a little tricky. For information about the font
style options, see [Support for
font styles in output captions](support-for-font-styles-in-output-captions.md "support-for-font-styles-in-output-captions.md").
