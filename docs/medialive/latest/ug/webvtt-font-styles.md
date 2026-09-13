

# Font styles for WebVTT
<a name="webvtt-font-styles"></a>

This section applies if you are [setting up a MediaLive channel with WebVTT captions](output-sidecar-and-smptett-mss.md) from source captions that are embedded or Teletext captions. You can optionally configure some of the style information.

1. In the output that has the WebVTT captions, display the section for the captions. 

1. Set **Style control**:
   + **NO\_STYLE\_DATA**: Includes only text and timestamp information for the caption encode. 
   + **Passthrough**: Passes through position and color style data from the source, and includes the text and timestamp information. 
   + **Manual**: Manually configure the output captions, and include the text and timestamp information. Any settings that you don't specify use default values. Currently, only the vertical position (**Y position**) is supported. 

1. If you set **Style control** to **Manual**, configure the settings that you want. Currently, only **Y position** is supported. For details about a field on the MediaLive console, choose the **Info** link next to the field. Enter the vertical position of the top edge of the caption as a percentage of the output height, where 0 is the top of the frame and 100 is the bottom.