# Font styles for WebVTT

This section applies if you are [setting up a MediaLive channel with WebVTT captions](output-sidecar-and-smptett-mss.md "output-sidecar-and-smptett-mss.md") from source captions that are
embedded or Teletext captions. You can optionally pass through some of the style
information.

1. In the output that has the WebVTT captions, display the section for the
   captions.
2. Set **Style control**:
   - **No_Style_Data**: Includes only text and timestamp
     information for the caption encode.
   - **Passthrough**: Passes through position and color style data
     from the source, and includes the text and timestamp information.
