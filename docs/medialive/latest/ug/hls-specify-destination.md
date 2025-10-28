# Complete the fields on the

console

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

| Portion of the destination URL | Location of the Field                             | Example                                                                            |
| ------------------------------ | ------------------------------------------------- | ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| protocol                       | **URL** in **HLS group destinations** section     | `http://`                                                                          |
| domain                         | **URL** in **HLS group destinations** section     | `203.0.113.55`                                                                     |
| path                           | **URL** in **HLS group destinations** section     | `/sports/delivery/curling/`Always terminate with a slash                           |
| baseFilename                   | **URL** in **HLS group destinations** section     | `index`Don't terminate the baseFilename with a slash.                              |
| modifier                       | **Name modifier** in each **HLS outputs** section | Required Make sure the modifiers are unique across all outputs in the output group |
| segmentModifier                | Segment modifier in each **HLS outputs** section  | OptionalKeep in mind that this field exists for each output.                       | 2. If the downstream system requires user authentication from MediaLive, in each **HLS group destination** section, complete the **Credentials** section. Enter a user name and a password provided by the downstream system. For the password, enter the name of the password stored on the AWS Systems Manager Parameter Store. Don't enter the password itself. For more information, see [Requirements for AWS Systems Manager password parameters](requirements-for-EC2.md "requirements-for-EC2.md"). 3. In the **CDN** settings section, choose the option that the downstream system told you to use—Akamai, PUT, or WebDAV. 4. If the downstream system gave you values to [configure the connection](origin-server-http.md "origin-server-http.md"), enter those values in the fields in the **CDN** settings section. |
