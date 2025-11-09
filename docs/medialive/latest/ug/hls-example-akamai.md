# Akamai example

This example shows how to set up the destination fields if the downstream
system is an Akamai server.

Assume that you want to stream the curling game and to create three
outputs: high, medium, and low bitrate.

| Field                                                                                                  | Value                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CDN settings\*<br>• in **HLS<br>settings\*<br>• section                                              | `HLS akamai`<br>Select this setting if you are using Akamai Token<br>Authentication. Change the other CDN fields according to<br>the instructions from Akamai.`HLS basic<br>put`<br>Select this setting if you are using digest<br>authentication. Change the other CDN fields according to<br>the instructions from Akamai.                                                                   |
| **URL\*<br>• in **HLS group<br>destination A\*<br>• section                                            | For<br>example:`https://p-ep50002.i.akamaientrypoint.net/50002/curling/index`Mapping<br>this URL to the Akamai terminology:<br>• _p-ep_ stands<br>for primary entry point<br>*https://p-ep50002.i.akamaientrypoint.net*<br>is the hostname<br>• _50002_ is<br>the stream ID for the primary entry point<br>• _curling_ is<br>the event name<br>• _index_ is<br>the manifest name               |
| **Credentials\*<br>• in **HLS group<br>destination A\*<br>• section                                    | If Akamai requires authenticated requests, enter a user<br>name and a password that is known to Akamai. For the<br>password, enter the name of the password stored on the<br>AWS Systems Manager Parameter Store. Don't enter the password itself.<br>For more information, see [Requirements for AWS Systems Manager password parameters](requirements-for-EC2.md "requirements-for-EC2.md"). |
| **URL\*<br>• in **HLS group<br>destination B\*<br>• section                                            | For<br>example:`https://b-ep50002.i.akamaientrypoint.net/50002-b/curling/index`Mapping<br>this URL to the Akamai terminology:<br>• _b-ep_ stands<br>for backup entry point<br>*https://b-ep50002.i.akamaientrypoint.net*<br>is the hostname<br>• _50002-b_ is<br>the stream ID for the backup entry point<br>• _curling_ is<br>the event name<br>• _index_ is<br>the manifest name             |
| **Credentials\*<br>• in **HLS group<br>destination B\*<br>• section                                    | Enter a user name and password for the URL for the other<br>destination, if applicable. The credentials are probably the<br>same for both URLs, but they might not be.                                                                                                                                                                                                                         |
| **Name modifier\*<br>• in **HLS<br>outputs\*<br>• section                                              | Choose **Add output\*<br>• twice: two more<br>**Output\*<br>• lines are added to this<br>section, for a total of three lines. In each line, enter<br>a modifier: `-high`,<br>`-medium`, and<br>`-low`.                                                                                                                                                                                         |
| **Directory Structure\*<br>• and<br>**Segments Per Subdirectory*<br>• in<br>\*\*Location*<br>• section | Complete the fields according to the instructions from<br>Akamai.                                                                                                                                                                                                                                                                                                                              |

As a result, files are created with the following names:

- One main manifest: `index.m3u8`
- One child manifest for each output:
  `index-high.m3u8`,
  `index-medium.m3u8`,
  `index-low.m3u8`
- TS files for each output:

      + `index-high-00001.ts`,
       `index-high-00002.ts`,
       `index-high-00003.ts`, and so
       on
      + `index-medium-00001.ts`,
       `index-medium-00002.ts`,
       `index-medium-00003.ts`, and so on
      + `index-low-00001.ts`,
       `index-low-00002.ts`,`index-low-00003.ts`, and so on

  The files will be published to two places:

- On the Akamai host
  `p-ep50002.i.akamaientrypoint.net` in a
  folder called `50002`
- On the host
  `b-ep50002.i.akamaientrypoint.net` in a
  folder called `50002-b`
