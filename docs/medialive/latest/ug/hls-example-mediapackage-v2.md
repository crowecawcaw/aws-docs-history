# MediaPackage v2 example

This example shows how to set up the destination fields if the downstream
system for the HLS output group is standard MediaPackage.

Assume that you want to stream the curling game and to create three
outputs: high, medium, and low bitrate.

| Field                                                                                               | Value                                                                                                                                                                                                |
| --------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *_CDN settings_<br>• in *_HLS<br>settings_<br>• section                                             | `basic PUT`                                                                                                                                                                                          |
| *_URL_<br>• in *_HLS group<br>destination A_<br>• section                                           | `mz82o4-1.ingest.hnycui.mediapackagev2.us-west-2.amazonaws.com/in/v1/live-sports/1/curling/index`                                                                                                    |
| *_Credentials_<br>• in *_HLS group<br>destination A_<br>• section                                   | Leave blank. MediaPackage v2 doesn't use credentials to<br>authenticate.                                                                                                                             |
| *_URL_<br>• in *_HLS group<br>destination B_<br>• section                                           | `mz82o4-2.ingest.hnycui.mediapackagev2.us-west-2.amazonaws.com/in/v1/live-sports/2/curling/index`.                                                                                                   |
| *_Credentials_<br>• in *_HLS group<br>destination B_<br>• section                                   | Leave blank. MediaPackage v2 doesn't use credentials to<br>authenticate.                                                                                                                             |
| *_Name modifier_<br>• in *_HLS<br>outputs_<br>• section                                             | Choose *_Add output_<br>• twice: two more<br>*_Output_<br>• lines are added to this<br>section, for a total of three lines. In each line, enter<br>a modifier: `-high`,<br>`-medium`, and<br>`-low`. |
| *_Directory Structure_<br>• and<br>*_Segments Per Subdirectory_<br>• in<br>*_Location_<br>• section | MediaPackage doesn't use these fields, therefore leave them<br>blank.                                                                                                                                |

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
    `index-low-00002.ts`,`index-low-00003.ts`, and so on
    The files will be published to both URL inputs on MediaPackage.
