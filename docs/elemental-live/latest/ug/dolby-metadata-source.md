

# Source of Elemental Live metadata
<a name="dolby-metadata-source"></a>

The metadata that Elemental Live emits can come from one of two sources:
+ Metadata that is already in the source. Only audio sources that use a Dolby codec can include this metadata. Different Dolby codecs include different categories of metadata as shown in this table.

<a name="dolby-metadata-source-table"></a>
<table>
<thead>
  <tr><th>Codec</th><th>Categories present</th></tr>
</thead>
<tbody>
  <tr><td>Dolby Digital or Dolby Digital Plus</td><td>Delivered only</td></tr>
  <tr><td>Dolby E</td><td>Delivered and Encoder Control</td></tr>
</tbody>
</table>

+ Metadata that is specified by completing metadata fields in the profile or event. You can specify this metadata in any audio whose output codec is a Dolby codec. In other words, you can add it when the audio source is not a Dolby codec as long as the output audio uses a Dolby codec.

  Both categories of metadata can be specified when specifying this source.

You specify the source when setting up the profile or event.