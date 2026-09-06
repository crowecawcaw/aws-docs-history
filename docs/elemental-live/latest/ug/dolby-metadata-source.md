

# Source of Elemental Live metadata
<a name="dolby-metadata-source"></a>

The metadata that Elemental Live emits can come from one of two sources:
+ Metadata that is already in the source. Only audio sources that use a Dolby codec can include this metadata. Different Dolby codecs include different categories of metadata as shown in this table.    
<a name="dolby-metadata-source-table"></a>[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-live/latest/ug/dolby-metadata-source.html)
+ Metadata that is specified by completing metadata fields in the profile or event. You can specify this metadata in any audio whose output codec is a Dolby codec. In other words, you can add it when the audio source is not a Dolby codec as long as the output audio uses a Dolby codec.

  Both categories of metadata can be specified when specifying this source.

You specify the source when setting up the profile or event.