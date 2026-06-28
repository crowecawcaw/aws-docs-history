# Standard MediaPackage example

This example shows how to set up the destination fields if the downstream
system for the HLS output group is standard MediaPackage.

Assume that you want to stream the curling game and to create three
outputs: high, medium, and low bitrate.

| Field                                                                                               | Value                                                                                                                                                                                                                                                                                                                                                                                                                   |
| --------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *_CDN settings_<br>• in *_HLS<br>settings_<br>• section                                             | `hls webdav`                                                                                                                                                                                                                                                                                                                                                                                                            |
| *_URL_<br>• in *_HLS group<br>destination A_<br>• section                                           | `6d2c.mediapackage.us-west-2.amazonaws.com/in/v2/9dj8/9dj8/channel`                                                                                                                                                                                                                                                                                                                                                     |
| *_Credentials_<br>• in *_HLS group<br>destination A_<br>• section                                   | MediaPackage accepts only authenticated requests, so you must<br>enter a user name and a password that is known to MediaPackage. For<br>the password, enter the name of the password stored on the<br>AWS Systems Manager Parameter Store. Don't enter the password itself.<br>For more information, see [Requirements for AWS Systems Manager password parameters](requirements-for-EC2.md "requirements-for-EC2.md"). |
| *_URL_<br>• in *_HLS group<br>destination B_<br>• section                                           | `6d2c.mediapackage.us-west-2.amazonaws.com/in/v2/9dj8/e333/channel`                                                                                                                                                                                                                                                                                                                                                     |
| *_Credentials_<br>• in *_HLS group<br>destination B_<br>• section                                   | Enter a user name and password for the URL for<br>destination B. The credentials are probably the same for<br>both URLs, but they might not be.                                                                                                                                                                                                                                                                         |
| *_Name modifier_<br>• in *_HLS<br>outputs_<br>• section                                             | Choose *_Add output_<br>• twice: two more<br>*_Output_<br>• lines are added to this<br>section, for a total of three lines. In each line, enter<br>a modifier: `-high`,<br>`-medium`, and<br>`-low`.                                                                                                                                                                                                                    |
| *_Directory Structure_<br>• and<br>*_Segments Per Subdirectory_<br>• in<br>*_Location_<br>• section | MediaPackage doesn't use these fields, therefore leave them<br>blank.                                                                                                                                                                                                                                                                                                                                                   |

As a result, files are created with the following names:

- One main manifest: `channel.m3u8`
- One child manifest for each output:
  `channel-high.m3u8`,
  `channel-medium.m3u8`,
  `channel-low.m3u8`
- TS files for each output:

  - `channel-high-00001.ts`,
    `channel-high-00002.ts`,
    `channel-high-00003.ts`, and so
    on
  - `channel-medium-00001.ts`,
    `channel-medium-00002.ts`,
    `channel-medium-00003.ts`, and so
    on
  - `channel-low-00001.ts`,
    `channel-low-00002.ts`,`channel-low-00003.ts`, and so on
    The files will be published to both URL inputs on MediaPackage.
