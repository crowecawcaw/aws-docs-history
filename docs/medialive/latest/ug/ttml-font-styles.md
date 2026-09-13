

# Font styles for TTML
<a name="ttml-font-styles"></a>

This section applies if you are [setting up TTML captions](output-sidecar-and-smptett-mss.md) from embedded or Teletext source captions. You can optionally specify some of the font style information. 

1. In the output that has the TTML captions, display the section for the captions. 

1. Set **Style control** to one of the following:
   + **Passthrough**: Copy the style and position information from the source captions to the output.
   + **Use configured**: Use default styling for the output captions instead of passing through style from the source. (There are no additional fields to configure with this option.)
   + **Manual**: Manually configure the output captions. Any settings that you don't specify use default values. Currently, only the vertical position (**Y position**) is supported.

1. If you set **Style control** to **Manual**, configure the settings that you want. Currently, only **Y position** is supported. For details about a field on the MediaLive console, choose the **Info** link next to the field. Enter the vertical position of the top edge of the caption as a percentage of the output height, where 0 is the top of the frame and 100 is the bottom.

The XML file for the captions will include the following style information:


| Style information | Value in XML file for Passthrough option | Value in XML file for User-configured option | 
| --- | --- | --- | 
| Font style information (position, alignment, italics, and so on) | Set to match the source captions. | Left blank. | 
| Font color and background color | Set to match the source captions. | Set to white font and black background. | 
| Font size  | Match size of source captions, if specified. Otherwise, set to 80% of the available height available for captions. | Left blank. | 
| Font family | Match family of source captions, if specified. Otherwise, set to monospaceSansSerif. | Left blank. | 
| Line gap  | Set to leave the line gap unfilled. | Set to leave the gap unfilled. | 

When you set **Style control** to **Manual**, AWS Elemental MediaLive uses default values for any setting that you don't specify. Currently, the only setting that you can specify is the vertical position (**Y position**).