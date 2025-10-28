# Design the path for the

output destination

Perform this step if you haven't yet designed the full destination path or
paths. If you've already designed the paths, go to [Complete the fields on the
console](hls-specify-destination.md "hls-specify-destination.md").

###### To design the path

1. Collect the information that you [previously obtained](origin-server-http.md "origin-server-http.md") from the
   operator of the downstream system:
   - The connection type for the downstream system –
     Akamai, basic PUT, or WebDAV.
   - The settings for connection fields, if the downstream
     system has special requirements.
   - The protocol for delivery—HTTP or HTTPS.
   - The user name and password to access the downstream
     system, if the downstream system requires authenticated
     requests. Note that these user credentials relate to user
     authentication, not to the protocol. User authentication is
     about whether the downstream system will accept your
     request. The protocol is about whether the request is sent
     over a secure connection.
   - All or part of the destination paths, possibly including
     the file names.
   - Whether you need to set up separate subdirectories.

2. As part of the planning with the operator of the downstream
   system, you should have determined if you want to implement
   redundant manifests. You should also have determined if the
   downstream system requires custom manifests. Given these two
   decisions, read the appropriate section:
   - If you are implementing redundant manifests, see [Creating redundant HLS manifests](hls-redundant-manifests.md "hls-redundant-manifests.md"), then return to this
     section.
   - If you are implementing custom paths for manifests, see
     [Customizing the paths inside HLS manifests](hls-manifest-paths.md "hls-manifest-paths.md"), then return to
     this section.
   - If you are not implementing either of those features,
     continue keep reading this section.

3. Design the portions of the destination paths that follow the
   bucket or buckets. For details, see the sections that follow.

###### Topics

- [The syntax for the paths for the
  outputs](#hls-syntax-http "#hls-syntax-http")
- [Designing the folders and
  baseFilename](#hls-baseFilename-design "#hls-baseFilename-design")
- [Designing the
  nameModifier](#hls-nameModifier-design "#hls-nameModifier-design")
- [Designing the
  segmentModifier](#hls-segmentModifier-design "#hls-segmentModifier-design")

## The syntax for the paths for the

outputs

The following table describes the parts that make up the destination
paths for these three categories of files.

The destination paths for these three categories of files are
identical up to and including the _baseFilename_, which means thatMediaLive sends all these
categories of files to the same folder. The modifiers and file
extensions are different for each category of file.

| File                   | Syntax of the path                                                                         | Example                                                                                                                                      |
| ---------------------- | ------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Main manifest files    | protocol domain path baseFilename extension                                                | The URL for a main manifest with the file name _/index_:`http://203.0.113.55/sports/delivery/curling/index.m3u8`                             |
| Child manifest files   | protocol domain path baseFilename nameModifier extension                                   | The URL for the child manifest for the high-resolution renditions of the output`http://203.0.113.55/sports/delivery/curling/index-high.m3u8` |
| Media files (segments) | `protocol domain path baseFilename nameModifier optionalSegmentModifier counter extension` | The URL for the file for the 230th segment might be:`http:// 203.0.113.55/sports/delivery/curling/index-high-00230.ts`                       | These destination paths are constructed as follows: <br>• The operator at the downstream system [should have provided you](origin-server-http.md "origin-server-http.md") with the protocol, domain and part of the path. For example: `http://203.0.113.55/sports/` The protocol is always HTTP or HTTPS. <br>• The operator might have provided the following. Otherwise, you decide them: + The folders + The baseFilename + The modifier + The segmentModifier See the sections that follow. <br>• MediaLive inserts the underscore before the counter. <br>• MediaLive generates the counter, which is always five digits starting at 00001. <br>• MediaLive inserts the dot before the extension. <br>• MediaLive selects the extension: + For manifest files – always`.m3u8` + For media files – `.ts` for files in a transport stream, and `.mp4` for files in an fMP4 container ## Designing the folders and baseFilename For the `folder` and `baseFilename` portion of the destination path, follow these guidelines: <br>• For a single-pipeline channel, you need only one `baseFilename`. <br>• For a standard channel when you are _not_ implementing [redundant manifests](hls-opg-redundant-manifest.md "hls-opg-redundant-manifest.md"), you need two `baseFilenames`. The two `baseFilenames` can be identical or different. Before you create different `baseFilenames`, make sure that the downstream system can work with that setup. <br>• For a standard channel when you _are_ implementing redundant manifests, see [Fields for redundant manifests](hls-opg-redundant-manifest.md "hls-opg-redundant-manifest.md"). ## Designing the nameModifier Design the `nameModifier` portions of the file name. The child manifests and media files include this modifier in their file names. This `nameModifier` distinguishes each output from the other, so it must be unique in each output. Follow these guidelines: <br>• For an output that contains video (and possibly other streams), you typically describe the video. For example, `-high` or `-1920x1080-5500kpbs` (to describe the resolution and the bitrate). <br>• For an output that contains only audio or only captions, you typically describe the audio or captions. For example, `-aac` or `-webVTT`. <br>• It’s a good idea to include a delimiter, to clearly separate the `baseFilename` from the `nameModifier`. <br>• The `nameModifier` can include [data variables](variable-data-identifiers.md "variable-data-identifiers.md"). ## Designing the segmentModifier Design the segmentModifiers portion of the destination path. The segmentModifier is optional, and if you include it, only the media file names include it. A typical use case for this modifier is to use a data variable to create a timestamp, to prevent segments overriding each other if the channel restarts. For example, assume that you include the timestamp `$t$-`. Segment 00001 might have the name `/index-120028-00001`. If the output restarts a few minutes later (which causes the segment counter to restart), the new segment 00001 will have the name `/index-120039-00001`. The new file won't overwrite the file for the original segment 00001. Some downstream systems might prefer this behavior. |
