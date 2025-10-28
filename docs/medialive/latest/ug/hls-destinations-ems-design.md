# Design the path for the output

destination

Perform this step if you haven't yet designed the full destination path or
paths. If you've already designed the paths, go to [Complete the fields on the
console](hls-specify-destination-ems.md "hls-specify-destination-ems.md").

###### To design the path

1. Collect the data endpoint for the container or containers. You
   [previously obtained](origin-server-ems.md "origin-server-ems.md")
   this information from the MediaStore user. For example:

`a23f.data.mediastore.us-west-2.amazonaws.com` 2. Design the portions of the destination paths that follow the data
endpoint (for MediaStore).

###### Topics

- [The syntax for the paths for the
  outputs](#hls-syntax-ems "#hls-syntax-ems")
- [How MediaLive constructs the
  paths](#hls-how-construct-urls-ems "#hls-how-construct-urls-ems")
- [Designing the folders and
  baseFilename](#hls-path-ems "#hls-path-ems")
- [Designing the
  nameModifier](#hls-nameModifier-design-ems "#hls-nameModifier-design-ems")
- [Designing the
  segmentModifier](#hls-segmentModifier-design-ems "#hls-segmentModifier-design-ems")

## The syntax for the paths for the

outputs

An HLS output always includes three categories of files:

- The main manifest
- The child manifests
- The media files

The following table describes the parts that make up the destination
paths for these three categories of files.

The destination paths for these three categories of files are
identical up to and including the _baseFilename_, which means that MediaLive sends all these
categories of files to the same folder. The modifiers and file
extensions are different for each category of file. When sending to
MediaStore, you must send all the files to the same folder. The downstream
systems expect all the files to be together.

| File                   | Syntax of the path                                                                               | Example                                                                                                                                                                                 |
| ---------------------- | ------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Main manifest files    | `protocol dataEndpoint path baseFilename extension`                                              | The path for a main manifest in the path _delivery_ in the container, and with the file name _index_:`mediastoressl://a23f.data.mediastore.us-west-2.amazonaws.com/delivery/index.m3u8` |
| Child manifest files   | `protocol dataEndpoint path baseFilename nameModifier extension`                                 | The path for the child manifest for the high-resolution renditions of the output`mediastoressl://a23f.data.mediastore.us-west-2.amazonaws.com/delivery/index-high.m3u8`                 |
| Media files (segments) | `protocol dataEndpoint path baseFilename nameModifier optionalSegmentModifier counter extension` | The path for the file for the 230th segment might be:`mediastoressl://a23f.data.mediastore.us-west-2.amazonaws.com/delivery/index-high-00230.ts`                                        | ## How MediaLive constructs the paths These paths are constructed as follows: <br>• The user of the AWS service should have provided you with the container names. <br>• For MediaStore, you must determine the following: + The folders + The baseFilename + The modifier + The segmentModifier See the sections that follow. <br>• MediaLive inserts the underscore before the counter. <br>• MediaLive generates the counter, which is always five digits starting at 00001. <br>• MediaLive inserts the dot before the extension. <br>• MediaLive selects the extension: + For manifest files – always`.m3u8` + For media files – .ts for files in a transport stream, or .mp4 for files in an fMP4 container ## Designing the folders and baseFilename Design a folder path and baseFilename that suits your purposes. If you have two destinations for each output, the destination paths must be different from each other in some way. Follow these guidelines: <br>• At least one of the portions of one path must be different from the other. It is acceptable for all the portions to be different. Therefore, if the buckets or containers are different, the folder path and file names for the two destinations can be different from each other, or they can be the same. For example: `mediastoressl://a23f.data.mediastore.us-west-2.amazonaws.com/delivery/index.m3u8` `mediastoressl://fe30.data.mediastore.us-west-2.amazonaws.com/delivery/index.m3u8` or `mediastoressl://a23f.data.mediastore.us-west-2.amazonaws.com/delivery/index.m3u8` `mediastoressl://fe30.data.mediastore.us-west-2.amazonaws.com/redundant/index.m3u8` <br>• If the buckets or containers are the same, the folder path and file names for the two destinations must be different from each other. For example: `mediastoressl://a23f.data.mediastore.us-west-2.amazonaws.com/delivery/index.m3u8` `mediastoressl://a23f.data.mediastore.us-west-2.amazonaws.com/redundant/index.m3u8` ## Designing the nameModifier Design the `nameModifier` portions of the file name. The child manifests and media files include this modifier in their file names. This `nameModifier` distinguishes each output from the other, so it must be unique in each output. Follow these guidelines: <br>• For an output that contains video (and possibly other streams), you typically describe the video. For example, `-high` or `-1920x1080-5500kpbs` (to describe the resolution and the bitrate). <br>• For an output that contains only audio or only captions, you typically describe the audio or captions. For example, `-aac` or `-webVTT`. <br>• It’s a good idea to start the `nameModifier` with a delimiter, such as a hyphen, in order to separate the`baseFilename` from the `nameModifier`. <br>• The `nameModifier` can include [data variables](variable-data-identifiers.md "variable-data-identifiers.md"). ## Designing the segmentModifier Design the segmentModifiers portion of the destination path. The segmentModifier is optional, and if you include it, only the media file names include it. A typical use case for this modifier is to use a data variable to create a timestamp, to prevent segments overriding each other if the channel restarts. For example, assume that you include the timestamp `$t$-`. Segment 00001 might have the name `index-120028-00001`. If the output restarts a few minutes later (which causes the segment counter to restart), the new segment 00001 will have the name `index-120039-00001`. The new file won't overwrite the file for the original segment 00001. Some downstream systems might prefer this behavior. |
