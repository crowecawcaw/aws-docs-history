# Source of Elemental Live

metadata

The metadata that Elemental Live emits can come from one of two sources:

- Metadata that is already in the source. Only audio sources that use a Dolby codec can
  include this metadata. Different Dolby codecs include different categories of metadata as shown
  in this table.

| Codec                               | Categories present            |
| ----------------------------------- | ----------------------------- |
| Dolby Digital or Dolby Digital Plus | Delivered only                |
| Dolby E                             | Delivered and Encoder Control |

- Metadata that is specified by completing metadata fields in the profile or event.
  You can specify this metadata in any audio whose output codec is a Dolby codec. In other words,
  you can add it when the audio source is not a Dolby codec as long as the output audio uses a
  Dolby codec.

Both categories of metadata can be specified when specifying this source.
You specify the source when setting up the profile or event.
