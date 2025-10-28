# Working with Dolby metadata

Audio encoded with a Dolby codec always includes Dolby metadata, as per the ATSC A/52 2012
standard. This Dolby metadata is used by AWS Elemental Live in two ways
when the stream is encoded with Dolby codec:

- It is used to manipulate the audio just before encoding the output.
- It is included in the metadata for the output stream.
  This document describes how to set up an Elemental Live profile or event to use Dolby metadata in these ways.

Dolby metadata is supported in the output only when the audio codec for the output is Dolby
Digital (also known as AC3) or Dolby Digital Plus (also known as Enhanced AC3).

###### Topics

- [Categories of metadata: Delivered
  and encoder control](dolby-metadata-categories.md "dolby-metadata-categories.md")
- [Source of Elemental Live
  metadata](dolby-metadata-source.md "dolby-metadata-source.md")
- [Impact of the metadata on the output
  audio](dolby-metadata-impact.md "dolby-metadata-impact.md")
- [Combinations of input and output codec](dolby-metadata-impact-combination-input-output-codec.md "dolby-metadata-impact-combination-input-output-codec.md")
- [Setting up the profile or event using
  the web interface](dolby-metadata-setup.md "dolby-metadata-setup.md")
- [Output with the
  Dolby Digital codec](dolby-metadata-output-dolby-digital-codec.md "dolby-metadata-output-dolby-digital-codec.md")
- [Output with
  Dolby Digital Plus (EC2, EAC3) codec](dolby-metadata-output-dolby-digital-plus-codec.md "dolby-metadata-output-dolby-digital-plus-codec.md")
