

# Complete the fields on the Console
<a name="hls-destinations-s3-specify"></a>

After you have designed the output names and destination paths, you can set up the HLS output group.

The following fields configure the location and names of the HLS media and manifest files (the destination).
+ **Output group – HLS group destination** section
+ **Output group – HLS settings – CDN** section
+ **Output group – Location – Directory structure **
+ **Output group – Location – Segments per subdirectory**
+ **HLS outputs – Output settings – Name modifier**
+ **HLS outputs – Output settings – Segment modifier**

**To set the destination for most downstream systems**

1. Complete the **URL** fields in the **HLS group destinations** section. Specify two destinations if the channel is set up as a standard channel, or one destination if it is set up as a single-pipeline channel. 


<table>
<thead>
  <tr><th> Portion of the destination path</th><th>Location of the Field</th><th colspan="3">Description</th></tr>
</thead>
<tbody>
  <tr><td> protocol </td><td><b>URL</b> in <b>HLS group destinations</b> section</td><td colspan="3"><code>s3ssl://</code></td></tr>
  <tr><td> domain </td><td><b>URL</b> in <b>HLS group destinations</b> section</td><td colspan="3">The bucket name</td></tr>
  <tr><td> path </td><td><b>URL</b> in <b>HLS group destinations</b> section</td><td colspan="3">The optional path of foldersAlways terminate with a slash</td></tr>
  <tr><td> baseFilename </td><td><b>URL</b> in <b>HLS group destinations</b> section</td><td colspan="3">RequiredDon't terminate the baseFilename with a slash.</td></tr>
  <tr><td>modifier</td><td><b>Name modifier</b> in each <b>HLS outputs</b> section</td><td colspan="3">RequiredMake sure the modifiers are unique across all outputs in the output group</td></tr>
  <tr><td>segmentModifier</td><td>Segment modifier in each <b>HLS outputs</b> section</td><td colspan="3">OptionalKeep in mind that this field exists for each output.</td></tr>
</tbody>
</table>


1. Leave the **Credentials** section blank in both the **HLS group destinations** sections. MediaLive has permission to write to the S3 bucket via the trusted entity. Someone in your organization should have already set up these permissions. For more information, see [Access requirements for the trusted entity](trusted-entity-requirements.md).

1. In the **CDN** settings section, choose `Hls S3`.

1. Complete the **CDN settings** field only if MediaLive must set a canned ACL whenever it sends this output to the Amazon S3 bucket.

   Use of a canned ACL typically only applies if your organization is not the owner of the Amazon S3 bucket. You should have discussed the use of a canned ACL with the bucket owner when you discussed the [destination for the output](origin-server-hls-s3.md#setting-dss-hls-canned-acl).