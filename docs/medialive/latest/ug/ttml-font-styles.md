

# Font styles for TTML
<a name="ttml-font-styles"></a>

This section applies if you are [setting up TTML captions](output-sidecar-and-smptett-mss.md) from embedded or Teletext source captions. You can optionally specify some of the font style information. 

1. In the output that has the TTML captions, display the section for the captions. 

1. Set **Style control** to **Passthrough** or **USE\_CONFIGURED**.

   Note that when **USE\_CONFIGURED** is selected, there are actually no fields that you can configure.

The XML file for the captions will include the following style information:


| Style information | Value in XML file for Passthrough option | Value in XML file for User-configured option | 
| --- | --- | --- | 
| Font style information (position, alignment, italics, and so on) | Set to match the source captions. | Left blank. | 
| Font color and background color | Set to match the source captions. | Set to white font and black background. | 
| Font size  | Match size of source captions, if specified. Otherwise, set to 80% of the available height available for captions. | Left blank. | 
| Font family | Match family of source captions, if specified. Otherwise, set to monospaceSansSerif. | Left blank. | 
| Line gap  | Set to leave the line gap unfilled. | Set to leave the gap unfilled. | 