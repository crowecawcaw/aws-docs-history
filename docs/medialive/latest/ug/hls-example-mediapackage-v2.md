# MediaPackage v2 example

This example shows how to set up the destination fields if the downstream
system for the HLS output group is standard MediaPackage.

Assume that you want to stream the curling game and to create three
outputs: high, medium, and low bitrate.

| Field                                                                                                  | Value                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **CDN settings\*<br>• in **HLS<br>settings\*<br>• section                                              | `basic PUT`                                                                                                                                                                                            |
| **URL\*<br>• in **HLS group<br>destination A\*<br>• section                                            | `mz82o4-1.ingest.hnycui.mediapackagev2.us-west-2.amazonaws.com/in/v1/live-sports/1/curling/index`                                                                                                      |
| **Credentials\*<br>• in **HLS group<br>destination A\*<br>• section                                    | Leave blank. MediaPackage v2 doesn't use credentials to<br>authenticate.                                                                                                                               |
| **URL\*<br>• in **HLS group<br>destination B\*<br>• section                                            | `mz82o4-2.ingest.hnycui.mediapackagev2.us-west-2.amazonaws.com/in/v1/live-sports/2/curling/index`.                                                                                                     |
| **Credentials\*<br>• in **HLS group<br>destination B\*<br>• section                                    | Leave blank. MediaPackage v2 doesn't use credentials to<br>authenticate.                                                                                                                               |
| **Name modifier\*<br>• in **HLS<br>outputs\*<br>• section                                              | Choose **Add output\*<br>• twice: two more<br>**Output\*<br>• lines are added to this<br>section, for a total of three lines. In each line, enter<br>a modifier: `-high`,<br>`-medium`, and<br>`-low`. |
| **Directory Structure\*<br>• and<br>**Segments Per Subdirectory*<br>• in<br>\*\*Location*<br>• section | MediaPackage doesn't use these fields, therefore leave them<br>blank.                                                                                                                                  |

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

  The files will be published to both URL inputs on MediaPackage.
