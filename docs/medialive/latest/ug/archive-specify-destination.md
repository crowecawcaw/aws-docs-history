

# Complete the fields on the console
<a name="archive-specify-destination"></a>

1. Enter the different portions of the destination in the appropriate fields. 


<table>
<thead>
  <tr><th>Portion of the destination URL</th><th>Field</th><th>Example</th></tr>
</thead>
<tbody>
  <tr><td>protocol, bucket, folders, baseFilename</td><td>The two <b>URL</b> fields in the <b>Archive group destinations</b> section.The data before the first slash is the bucket name. The data after the last slash is the baseFilename. The data in between is the folders.<br />Specify two destinations when the channel is set up as a <a href="channel-class.md">standard channel</a>, or one destination when it is set up as a single-pipeline channel. </td><td><code>s3ssl://amzn-s3-demo-bucket/channel59/delivery/curling</code></td></tr>
  <tr><td>nameModifier</td><td>The <b>Name modifier</b> field in the <b>Archive outputs</b> section.If you choose to include a modifier, you can enter a string such as <b>-high</b>, to indicate a high-resolution output.<br />Or you can enter a variable ID (such as <code>$dt$</code>) to ensure that the modifier is different for each file segment. For a list of variable data identifiers, see <a href="variable-data-identifiers.md">Identifiers for variable data in MediaLive</a>.</td><td><code>$dft$</code></td></tr>
  <tr><td>extension</td><td>The <b>Extension</b> field in the <b>Archive outputs</b>.Always leave the default, <b>m2ts</b>.</td><td><code>mt2s</code></td></tr>
</tbody>
</table>


1. Leave the **Credentials** section blank in both the **Archive group destinations** sections. MediaLive has permission to write to the S3 bucket via the trusted entity. Someone in your organization should have already set up these permissions. For more information, see [Access requirements for the trusted entity](trusted-entity-requirements.md).

1. Complete the **CDN settings** field only if MediaLive must set a canned ACL whenever it sends this output to the Amazon S3 bucket.

   Use of a canned ACL typically only applies if your organization is not the owner of the Amazon S3 bucket. You should have discussed the use of a canned ACL with the bucket owner when you discussed the [destination for the output](archive-op-origin-server-s3.md#setting-dss-archive-canned-acl).

1. Complete the **Rollover interval** field in the **Archive settings** section.

   For example, **300** divides the output into separate files, each with a 300 second (5 minutes) long duration. 

   Each time the rollover expires, MediaLive closes the current file on Amazon S3 and starts a new file using the `baseFilename`, the `nameModifier`, and a sequential counter. 

   The current file is visible on Amazon S3 only after it has closed.

For more information, see the [examples](archive-examples.md). 