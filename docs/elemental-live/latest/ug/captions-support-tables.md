# Rules

for converting source captions to output captions

This section helps you to ensure that when creating an event or profile,
you select a format that is valid for your output captions.

Various constraints exist for the caption formats that you can include
in your content:

- For a given input container, Elemental Live can parse certain caption
  formats.
- For a given input caption format, Elemental Live can create one or more
  output captions. However, a given output caption can appear only in
  specific output containers.
  In summary – starting with the output container you want to produce:

- A given output container supports a given set of output caption
  formats. This container constrains your choice of output captions.
- Furthermore, to produce each output caption format, you must use one
  of the compatible input caption formats .And you must select an input which
  can appear in the input container you have selected. So both which original
  input container and format you choose constrains your choice of output
  caption formats.
  You must determine if it's possible for you to include the captions
  format that you want in your output. For example, assume that you want to
  include WebVTT captions in an HLS output. Assume that your captions source is
  in an MP4 container.You can implement this use case only if the MP4 container
  holds 608 embedded captions. You can't implement if, for example, the MP4
  container holds ancillary captions.

###### Topics

- [Supported source captions
  and output captions in a GPP output container](captions-gpp-output-container.md "captions-gpp-output-container.md")
- [Supported source captions
  and output captions in a DASH output container](captions-dash-output-container.md "captions-dash-output-container.md")
- [Supported source captions
  and output captions in an HLS output container](captions-hls-output-container.md "captions-hls-output-container.md")
- [Supported source
  captions and output captions in an fMP4 output container](captions-hls-fmp4-output-container.md "captions-hls-fmp4-output-container.md")
- [Supported
  source captions and output captions in an MP4 output container](captions-hds-mp4-output-container.md "captions-hds-mp4-output-container.md")
- [Supported source captions and output captions in MPEG2-TS or
  MPEG2-UDP](captions-mpeg2-ts-file-mpeg2-udp-streaming-output-container.md "captions-mpeg2-ts-file-mpeg2-udp-streaming-output-container.md")
- [Supported source captions
  and output captions in an MSS output container](captions-mss-output-container.md "captions-mss-output-container.md")
- [Supported source captions
  and output captions in an MXF output container](captions-mxf-output-container.md "captions-mxf-output-container.md")
- [Supported source
  captions and output captions in a QuickTime output container](captions-quicktime-output-container.md "captions-quicktime-output-container.md")
- [Supported source captions
  and output captions in a raw output container](captions-raw-output-container.md "captions-raw-output-container.md")
- [Supported source captions
  and output captions in an RTMP output container](captions-rtmp-output-container.md "captions-rtmp-output-container.md")
- [Supported source
  captions and output captions in a captions-only output container](captions-captions-only-output-container.md "captions-captions-only-output-container.md")
