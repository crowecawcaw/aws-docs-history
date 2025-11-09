# Complete the fields on the

Console

After you have designed the output names and destination paths, you can
set up the HLS output group.

The following fields configure the location and names of the HLS media and
manifest files (the destination).

- **Output group – HLS group destination**
  section
- **Output group – HLS settings – CDN**
  section
- **Output group – Location – Directory structure**
- **Output group – Location – Segments per
  subdirectory**
- **HLS outputs – Output settings – Name
  modifier**
- **HLS outputs – Output settings – Segment
  modifier**

###### To set the destination for most downstream systems

1. Complete the **URL** fields in the **HLS
   group destinations** section. Specify two destinations
   if the channel is set up as a standard channel, or one destination
   if it is set up as a single-pipeline channel.

| Portion of the destination path | Location of the Field                                          | Description                                                                             |
| ------------------------------- | -------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| protocol                        | **URL\*<br>• in **HLS group<br>destinations\*<br>• section     | `s3ssl://`                                                                              |
| domain                          | **URL\*<br>• in **HLS group<br>destinations\*<br>• section     | The bucket<br>name                                                                      |
| path                            | **URL\*<br>• in **HLS group<br>destinations\*<br>• section     | The optional<br>path of foldersAlways terminate with a<br>slash                         |
| baseFilename                    | **URL\*<br>• in **HLS group<br>destinations\*<br>• section     | RequiredDon't terminate the baseFilename<br>with a slash.                               |
| modifier                        | **Name modifier\*<br>• in each<br>**HLS outputs\*<br>• section | RequiredMake sure the modifiers are unique<br>across all outputs in the output<br>group |
| segmentModifier                 | Segment modifier in each<br>\*_HLS outputs_<br>• section       | OptionalKeep in mind that this field exists<br>for each output.                         |

2. Leave the **Credentials** section blank in both
   the **HLS group destinations** sections. MediaLive has
   permission to write to the S3 bucket via the trusted entity. Someone
   in your organization should have already set up these permissions.
   For more information, see [Access requirements for the trusted entity](trusted-entity-requirements.md "trusted-entity-requirements.md").
3. In the **CDN** settings section, choose `Hls
S3`.
4. Complete the **CDN settings** field only if MediaLive
   must set a canned ACL whenever it sends this output to the Amazon S3
   bucket.

Use of a canned ACL typically only applies if your organization is
not the owner of the Amazon S3 bucket. You should have discussed the use
of a canned ACL with the bucket owner when you discussed the [destination for the
output](origin-server-hls-s3.md#setting-dss-hls-canned-acl "origin-server-hls-s3.md#setting-dss-hls-canned-acl").
