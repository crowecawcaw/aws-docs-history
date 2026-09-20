

# Complete the fields on the console
<a name="hls-specify-destination-emp"></a>

After you have designed the output names and destination paths, you can set up the HLS output group.

The following fields configure the location and names of the HLS media and manifest files (the destination).
+ **Output group – HLS group destination** section
+ **Output group – HLS settings – CDN** section
+ **Output group – Location – Directory structure **
+ **Output group – Location – Segments per subdirectory**
+ **HLS outputs – Output settings – Name modifier**
+ **HLS outputs – Output settings – Segment modifier**

**To set the destination**

1. Complete the **URL** fields in the **HLS group destinations** section. Specify two destinations if the channel is set up as a standard channel, or one destination if it is set up as a single-pipeline channel. 


<table>
<thead>
  <tr><th> Portion of the destination path</th><th>Location of the Field</th><th colspan="3">Description</th></tr>
</thead>
<tbody>
  <tr><td> protocol </td><td><b>URL</b> in <b>HLS group destinations</b> section</td><td colspan="3">Enter <code>https://</code></td></tr>
  <tr><td> domain </td><td><b>URL</b> in <b>HLS group destinations</b> section</td><td colspan="3">Enter the MediaPackage channel URL</td></tr>
  <tr><td> path </td><td><b>URL</b> in <b>HLS group destinations</b> section</td><td colspan="3">Not applicable, the path is already specified in the channel URL</td></tr>
  <tr><td> baseFilename </td><td><b>URL</b> in <b>HLS group destinations</b> section</td><td colspan="3">Not applicable, the path is already specified in the channel URLWith MediaPackage, the <code>baseFilename</code> is always <b>channel</b>. With MediaPackage v2 it is always <b>index</b>.<br />Don't terminate the <b>baseFilename</b> with a slash.</td></tr>
  <tr><td>modifier</td><td><b>Name modifier</b> in each <b>HLS outputs</b> section</td><td colspan="3">Required. For guidance, see <a href="hls-nameModifier-design-emp.md">Designing the nameModifier</a>.Make sure the modifiers are unique across all outputs in the output group</td></tr>
  <tr><td>segmentModifier</td><td>Segment modifier in each <b>HLS outputs</b> section</td><td colspan="3">Optional. For guidance, see <a href="hls-segmentModifier-design-emp.md">Designing the segmentModifier</a>.Keep in mind that this field exists for each output.</td></tr>
</tbody>
</table>


1. Enter the input user name. For the password (if applicable), enter the name of the password stored on the AWS Systems Manager Parameter Store. Don't enter the password itself. For more information, see [Requirements for AWS Systems Manager password parameters](requirements-for-EC2.md).

1. In the **CDN** settings section, choose the appropriate connection type:
   + To send to standard MediaPackage, choose `Hls webdav`.
   + To send to MediaPackage v2, choose `Basic PUT`.

1. If the downstream system gave you values to [configure the connection](origin-server-http.md), enter those values in the fields in the **CDN** settings section.