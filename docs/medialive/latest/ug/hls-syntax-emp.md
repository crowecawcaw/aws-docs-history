# The syntax for the paths for the

outputs

An HLS output always includes three categories of files:

See the following sections.

- The main manifest
- The child manifests
- The media files
  The following table describes the parts that make up the destination
  paths for these three categories of files.

The destination paths for these three categories of files are
identical up to and including the _baseFilename_, which means thatMediaLive sends all these
categories of files to the same folder. The modifiers and file
extensions are different for each category of file. When sending to
MediaPackage, you must send all the files to the same folder. The downstream
systems expect all the files to be together.

| File                   | Syntax of the path                                                                 | Example                                                                                                                                                                                                                                                                                   |
| ---------------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Main manifest files    | `protocol channelURL extension`                                                    | The path for output. Here is an example that uses<br>MediaPackage v2<br>`https://mz82o4-2.ingest.hnycui.mediapackagev2.us-west-2.amazonaws.com/in/v1/live-sports/2/curling/index.m3u8`                                                                                                    |
| Child manifest files   | `protocol channelURL nameModifier<br>extension`                                    | Here is an example for the path for the child<br>manifest for the high-resolution renditions of the<br>curling output (in a destination that uses MediaPackage<br>v2):`https://mz82o4-1.ingest.hnycui.mediapackagev2.us-west-2.amazonaws.com/in/v1/live-sports/1/curling/index-high.m3u8` |
| Media files (segments) | `protocol channelURL nameModifier<br>optionalSegmentModifier counter<br>extension` | Here is an example for the path for the file<br>for the 230th segment (in a destination that uses<br>MediaPackage<br>v2):`https://mz82o4-1.ingest.hnycui.mediapackagev2.us-west-2.amazonaws.com/in/v1/live-sports/1/curling/index-high-00230.ts`                                          |

These paths are constructed as follows:

- The MediaPackage user should have provided you with the channel URLs.
  The URLs cover the portion of the path up to and including the
  baseFilename:
  - With standard MediaPackage, the baseFilename is always
    `channel`.
  - With MediaPackage v2, the baseFilename is always
    `index`.

- You must specify the following:

      + The modifier
      + The segmentModifier

  See the sections that follow.

- MediaLive inserts the underscore before the counter.
- MediaLive generates the counter, which is always five digits
  starting at 00001.
- MediaLive inserts the dot before the extension.
- MediaLive selects the extension:
  - For manifest files – always`.m3u8`
  - For media files – .ts for files in a transport stream,
    or .mp4 for files in an fMP4 container
