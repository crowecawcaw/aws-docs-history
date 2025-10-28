# Complete the fields on the

console

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

###### To set the destination

1. Complete the **URL** fields in the **HLS
   group destinations** section. Specify two destinations
   if the channel is set up as a standard channel, or one destination
   if it is set up as a single-pipeline channel.

| Portion of the destination path | Location of the Field                             | Description                                                                                                                                                                                                             |
| ------------------------------- | ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| protocol                        | **URL** in **HLS group destinations** section     | Enter `https://`                                                                                                                                                                                                        |
| domain                          | **URL** in **HLS group destinations** section     | Enter the MediaPackage channel URL                                                                                                                                                                                      |
| path                            | **URL** in **HLS group destinations** section     | Not applicable, the path is already specified in the channel URL                                                                                                                                                        |
| baseFilename                    | **URL** in **HLS group destinations** section     | Not applicable, the path is already specified in the channel URLWith MediaPackage, the `baseFilename` is always `channel`. With MediaPackage v2 it is always `index`.Don't terminate the **baseFilename** with a slash. |
| modifier                        | **Name modifier** in each **HLS outputs** section | Required. For guidance, see [Designing the nameModifier](hls-nameModifier-design-emp.md "hls-nameModifier-design-emp.md").Make sure the modifiers are unique across all outputs in the output group                     |
| segmentModifier                 | Segment modifier in each **HLS outputs** section  | Optional. For guidance, see [Designing the segmentModifier](hls-segmentModifier-design-emp.md "hls-segmentModifier-design-emp.md").Keep in mind that this field exists for each output.                                 | 2. Enter the input user name. For the password (if applicable), enter the name of the password stored on the AWS Systems Manager Parameter Store. Don't enter the password itself. For more information, see [Requirements for AWS Systems Manager password parameters](requirements-for-EC2.md "requirements-for-EC2.md"). 3. In the **CDN** settings section, choose the appropriate connection type: <br>• To send to standard MediaPackage, choose `Hls webdav`. <br>• To send to MediaPackage v2, choose `Basic PUT`. 4. If the downstream system gave you values to [configure the connection](origin-server-http.md "origin-server-http.md"), enter those values in the fields in the **CDN** settings section. |
