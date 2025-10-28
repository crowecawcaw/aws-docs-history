# Support for conversion using OCR optical character recognition)

You can convert source captions that are in DVB-Sub or SCTE-27
format into output captions that are in WebVTT format. AWS Elemental
Live uses OCR (optical character recognition) to perform this
conversion.

**Enabling the OCR feature**

If you want to use OCR conversion, you must enable the feature when
you install or upgrade
Elemental Live.
For more information, see these guides:

- [AWS Elemental Live Installation Guide](../installguide.md "../installguide.md")
- [AWS Elemental Live Upgrade Guide](../upgradeguide.md "../upgradeguide.md")
  You can determine if the feature has already been enabled. In the
  event, go to the output section and start to set up a captions encode.
  Choose WebVTT as the output format. If the feature is enabled, a list of
  languages (language libraries) appears.

###### Note

When you enable OCR, you must make sure that you don't use the
`--skip-all` option with the command to install, upgrade
or configure. If you use that skip option, you won't see the prompts
to enable OCR conversion.

**Using OCR conversion**

For more information about setting up to convert captions using OCR,
see [Sidecar captions or
SMPTE-TT captions in MS Smooth](output-sidecar-and-smptett-mss.md "output-sidecar-and-smptett-mss.md").

For a list of languages supported with OCR conversion, see [Reference: Languages supported
with OCR captions](captions-ocr-languages.md "captions-ocr-languages.md").
