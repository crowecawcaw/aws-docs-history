# Burn-in output captions

This section covers how to configure burn-in output captions in AWS Elemental MediaConvert. The main topics include:

- Where to specify the captions.
- How to specify multiple captions tracks.
- How to use style passthrough.
- Non-english fonts and unsupported characters.
  _Burn-in_ is a way to deliver captions, rather
  than a captions format. Burn-in writes the captions directly on your video frames,
  replacing pixels of video content with the captions. If you want burn-in captions in
  an output, set up the captions according to the following information.

## Where to specify the

captions

Put your captions in the same output group and the same output as your video.

## How to specify multiple

captions tracks

You can burn in only one track of captions in each output.

## How to use style

passthrough

You can choose how to stylize the burn-in caption text that appears in your
output video. There are a few options, including style passthrough, default
settings, or manual overrides.

When you set Style passthrough to Enabled, MediaConvert uses the available
style and position information from your input captions. Note that MediaConvert
uses default settings for any missing style information.

MediaConvert supports style passthrough for the following input caption
formats:

- Ancillary
- Embedded
- SCTE-20
- SCC
- TTML
- STL (EBU STL)
- SMPTE-TT (text based)
- Teletext
- IMSC
- WebVTT

When you set Style passthrough to Disabled, MediaConvert ignores style
information from your input and uses default settings: white text with black
outlining, bottom-center positioning, and automatic sizing.

Whether you set style passthrough to enabled or not, you can also choose to
manually override any of the individual style options.

###### Note

TTML and TTML-like (IMSC, SMPTE-TT) inputs have special style formatting
requirements. For more information, see [TTML style formatting](ttml-style-formatting.md "ttml-style-formatting.md").

## How to specify the

font script

AWS Elemental MediaConvert automatically selects the appropriate script for your captions, based on
the language that you specify in the output captions settings. If the language that you choose has more
than one possible script, specify the script that you want.

###### To ensure that the service uses the correct font script

1. In the **Captions** section under **Encoding
   settings**, for
   **Language**, choose the language of the captions text.
2. If the language that you specify has more than one possible script, use **Font
   script** to specify the script.

For example, if you choose **Chinese** (ZH) for
**Language**, use **Font script** to choose either
**Simplified Chinese** or **Traditional Chinese**. In this
case, if you don’t specify a value for **Font script**, the service defaults to simplified Chinese.

###### Tip

In most cases, for **Font script** you can keep the default value of **Automatic**. When you do, the service chooses the script based on the language of the captions text.

## Non-english fonts and unsupported

characters

When your input font uses a non-English font script, your output burn-in
captions may contain unsupported Unicode characters `□`. To resolve,
set **Style passthrough** to
**Enabled**.
