This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Working with Dolby Metadata

Audio encoded with a Dolby codec always includes Dolby metadata, as per the ATSC A/52 2012
standard. This Dolby metadata is used by AWS Elemental Server in two ways
when the stream is encoded with Dolby codec:

- It is used to manipulate the audio just before encoding the output.
- It is included in the metadata for the output stream.
  This document describes how to set up an AWS Elemental Server profile or job to use Dolby metadata in these ways.

Dolby metadata is supported in the output only when the audio codec for the output is Dolby
Digital (also known as AC3) or Dolby Digital Plus (also known as Enhanced AC3).

###### Topics

- [Categories of Metadata: Delivered and Encoder
  Control](#dolby-metadata-categories "#dolby-metadata-categories")
- [Source of AWS Elemental Server Metadata](#dolby-metadata-source "#dolby-metadata-source")
- [Impact of the Metadata on the Output Audio](#dolby-metadata-impact "#dolby-metadata-impact")
- [Combinations of Input and
  Output Codec](#dolby-metadata-impact-combination-input-output-codec "#dolby-metadata-impact-combination-input-output-codec")
- [Setting Up the Profile or Event Using the Web
  Interface](dolby-metadata-setup.md "dolby-metadata-setup.md")
- [Output with the Dolby Digital
  Codec](dolby-metadata-output-dolby-digital-codec.md "dolby-metadata-output-dolby-digital-codec.md")
- [Output with Dolby Digital Plus
  (EC2, EAC3) Codec](dolby-metadata-output-dolby-digital-plus-codec.md "dolby-metadata-output-dolby-digital-plus-codec.md")

## Categories of Metadata: Delivered and Encoder

Control

There are two categories of parameters in the Dolby metadata, characterized by how
AWS Elemental Server uses it:

- Delivered: AWS Elemental Server does not read these parameters, so they have no
  effect on the audio produced by AWS Elemental Server. Instead, they are included as
  metadata in the output in order to **deliver** them to the
  downstream decoder.

“Delivered” metadata is also called _Consumer_ metadata
because it is intended to be used by the end consumer’s home decoder.

- Encoder Control: AWS Elemental Server uses these parameters to manipulate the audio
  just before encoding the stream and producing the output. They provide a mechanism for AWS Elemental Server to control the transcoding performed by AWS Elemental Server. These parameters
  are never included in the output metadata.

“Encoder Control” metadata is also called _Professional_
metadata because it is intended to be used by a professional device – in our case
AWS Elemental Server. It is never intended for the end consumer's home
decoder.

## Source of AWS Elemental Server Metadata

The metadata that AWS Elemental Server emits can come from one of two sources:

- Metadata that is already in the source. Only audio sources that use a Dolby codec can
  include this metadata. Different Dolby codecs include different categories of metadata as shown
  in this table.

| Codec                               | Categories Present            |
| ----------------------------------- | ----------------------------- |
| Dolby Digital or Dolby Digital Plus | Delivered only                |
| Dolby E                             | Delivered and Encoder Control |

- Metadata that is specified by completing metadata fields in the profile or event.
  You can specify this metadata in any audio whose output codec is a Dolby codec. In other words,
  you can add it when the audio source is not a Dolby codec as long as the output audio uses a
  Dolby codec.

Both categories of metadata can be specified when specifying this source.

You specify the source when setting up the profile or event.

## Impact of the Metadata on the Output Audio

Regardless of the source of the metadata, it affects the audio (either by manipulating
encoder control or by being included in the output metadata) but only if the output codec is
Dolby Digital or Dolby Digital Plus.

## Combinations of Input and

Output Codec

The possible input and output codec combinations (in which at least one codec is a Dolby
codec) are as follows. All these combinations support including metadata in the output.

| Input Codec                                 | Output Codec                                                                                       |
| ------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Dolby Digital or Dolby Digital Plus         | Dolby Digital or Dolby Digital Plus                                                                |
| Dolby Digital                               | Dolby Digital Passthrough (so Dolby Digital audio is passed through; it is not<br>transcoded)      |
| Dolby Digital Plus                          | Dolby Digital Passthrough (so Dolby Digital Plus audio is passed through; it is not<br>transcoded) |
| Mix of Dolby Digital Plus and another codec | Dolby Digital Plus (with the Automatic Passthrough field checked)                                  |
| Dolby E                                     | Dolby Digital                                                                                      |
| Dolby E                                     | Dolby Digital Plus                                                                                 |
| Dolby E                                     | Dolby E (passthrough )                                                                             |
| A non-Dolby codec                           | Dolby Digital or Dolby Digital Plus                                                                |

The sample rate when encoding with a Dolby codec is always 48000.
