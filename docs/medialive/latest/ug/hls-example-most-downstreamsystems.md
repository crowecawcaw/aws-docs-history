# Example for an HTTP or HTTPS server

This example shows how to set up the destination fields if the downstream
system is an HTTPS server that uses basic PUT.

Assume that you want to stream the curling game and to create three
outputs: high, medium, and low bitrate.

| Field                                                                                               | Value                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *_CDN settings_<br>• in *_HLS<br>settings_<br>• section                                             | `Hls basic put`Change the<br>other CDN fields according to the instructions from the<br>downstream system.                                                                                                                                                                                                                                                                                                 |
| *_URL_<br>• in *_HLS group<br>destination A_<br>• section                                           | For<br>example:`https://203.0.113.55/sports/curling/index`                                                                                                                                                                                                                                                                                                                                                 |
| *_Credentials_<br>• in *_HLS group<br>destination A_<br>• section                                   | If the downstream system requires authenticated requests,<br>enter the user name provided by the downstream system. For<br>the password, enter the name of the password stored on the<br>AWS Systems Manager Parameter Store. Don't enter the password itself.<br>For more information, see [Requirements for AWS Systems Manager password parameters](requirements-for-EC2.md "requirements-for-EC2.md"). |
| *_URL_<br>• in *_HLS group<br>destination B_<br>• section                                           | For<br>example:`https://203.0.113.82/sports/curling/index`                                                                                                                                                                                                                                                                                                                                                 |
| *_Credentials_<br>• in *_HLS group<br>destination B_<br>• section                                   | Enter a user name and password for the URL for<br>destination B, if applicable. The credentials are probably<br>the same for both URLs, but they might not be.                                                                                                                                                                                                                                             |
| *_Name modifier_<br>• in *_HLS<br>outputs_<br>• section                                             | Choose *_Add output_<br>• twice: two more<br>*_Output_<br>• lines are added to this<br>section, for a total of three lines. In each line, enter<br>a modifier: `-high`,<br>`-medium`, and<br>`-low`.                                                                                                                                                                                                       |
| *_Directory Structure_<br>• and<br>*_Segments Per Subdirectory_<br>• in<br>*_Location_<br>• section | Assume that the downstream system doesn't use these<br>fields.                                                                                                                                                                                                                                                                                                                                             |

As a result, files are created with the following names:

- One main manifest: `index.m3u8`
- One child manifest for each output:
  `index-high.m3u8`,
  `index-medium.m3u8`,
  `index-low.m3u8`
- TS files for each output:

  - `index-high-00001.ts`,
    `index-high-00002.ts`,
    `index-high-00003.ts`, and so
    on
  - `index-medium-00001.ts`,
    `index-medium-00002.ts`,
    `index-medium-00003.ts`, and so on
  - `index-low-00001.ts`,
    `index-low-00002.ts`, `index-low-00003.ts`, and so on
    The files will be published to two hosts at the downstream system, and in
    a folder called `sports` on each host.
