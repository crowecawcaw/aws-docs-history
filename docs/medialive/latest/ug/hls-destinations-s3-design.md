# Design the path for the output

destination

Perform this step if you haven't yet designed the full destination path or
paths. If you've already designed the paths, go to [Complete the fields on the
Console](hls-destinations-s3-specify.md "hls-destinations-s3-specify.md").

###### To design the path

1. Collect the bucket names that you [previously obtained](origin-server-hls-s3.md "origin-server-hls-s3.md") from
   the Amazon S3 user. For example:

`amzn-s3-demo-bucket` 2. Design the portions of the destination paths that follow the
bucket or buckets. For details, see the sections that follow.

###### Topics

- [The syntax for the paths for the
  outputs](#hls-syntax-s3 "#hls-syntax-s3")
- [Designing the folders and
  baseFilename](#hls-path-s3 "#hls-path-s3")
- [Designing the
  nameModifier](#hls-nameModifier-design-s3 "#hls-nameModifier-design-s3")
- [Designing the
  segmentModifier](#hls-segmentModifier-design-s3 "#hls-segmentModifier-design-s3")

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
Amazon S3, you must send all the files to the same folder. The downstream
systems expect all the files to be together.

| File                   | Syntax of the path                                                                               | Example                                                                                                                                                             |
| ---------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Main manifest files    | `protocol bucket path baseFilename<br>extension`                                                 | The path for a main manifest in the bucket<br>_sports_, with<br>the file name _index_:`s3ssl://amzn-s3-demo-bucket/sports/delivery/curling/index.m3u8`              |
| Child manifest files   | `protocol bucket path baseFilename nameModifier<br>extension`                                    | The path for the child manifest for the<br>high-resolution renditions of the curling<br>output`s3ssl://amzn-s3-demo-bucket/sports/delivery/curling/index-high.m3u8` |
| Media files (segments) | `protocol bucket path baseFilename nameModifier<br>optionalSegmentModifier counter<br>extension` | The path for the file for the 230th segment<br>might<br>be:`s3ssl://amzn-s3-demo-bucket/sports/delivery/curling/index-high-00230.ts`                                |

These destination paths are constructed as follows:

- The Amazon S3 user should have provided you with the bucket
  names.
- You must determine the following:

      + The folders
      + The baseFilename
      + The modifier
      + The segmentModifier

  See the sections that follow.

- MediaLive inserts the underscore before the counter.
- MediaLiveautomatically generates this counter. Initially, this is
  a five-digit number starting at 00001, and increasing by 1. So
  00001, 00002, 00003 and so on. After 99999, the next number is
  100000 (six digits), then 100001, 100002, and so on. Then from
  999999 to 1000000 (seven digits), and so on.
- MediaLive inserts the dot before the extension.
- MediaLive selects the extension:
  - For manifest files – always
    `.m3u8`
  - For media files – .ts for files in a transport stream,
    or .mp4 for files in an fMP4 container

## Designing the folders and

baseFilename

Design a folder path and baseFilename that suits your purposes.

If you have two destinations for each output, the destination paths
must be different from each other in some way. Follow these
guidelines:

- At least one of the portions of one path must be different
  from the other. It is acceptable for all the portions to be
  different.

Therefore, if the buckets are _different_, the folder path and file names for
the two destinations can be different from each other, or they
can be the same. For example:

`s3ssl://amzn-s3-demo-bucket/sports/delivery/curling/index-high.m3u8`

`s3ssl://amzn-s3-demo-bucket1/sports/delivery/curling/index-high.m3u8`

or

`s3ssl://amzn-s3-demo-bucket/sports/delivery/curling/index-high.m3u8`

`s3ssl://amzn-s3-demo-bucket1/sports/redundant/curling/index-high.m3u8`

- If the buckets are _the
  same_, the folder path and file names for the two
  destinations must be different from each other. For
  example:

`s3ssl://amzn-s3-demo-bucket/sports/delivery/curling/index-high.m3u8`

`s3ssl://amzn-s3-demo-bucket/sports/redundant/curling/index-high.m3u8`

## Designing the

nameModifier

Design the `nameModifier` portions of the file name. The
child manifests and media files include this modifier in their file
names. This `nameModifier` distinguishes each output from the
other, so it must be unique in each output. Follow these
guidelines:

- For an output that contains video (and possibly other
  streams), you typically describe the video. For example,
  `-high` or
  `-1920x1080-5500kpbs` (to describe the
  resolution and the bitrate).
- For an output that contains only audio or only captions, you
  typically describe the audio or captions. For example,
  `-aac` or
  `-webVTT`.
- It’s a good idea to start the `nameModifier` with a
  delimiter, such as a hyphen, in order to separate the`baseFilename` from the
  `nameModifier`.
- The `nameModifier` can include [data
  variables](variable-data-identifiers.md "variable-data-identifiers.md").

## Designing the

segmentModifier

Design the segmentModifiers portion of the destination path. The
segmentModifier is optional, and if you include it, only the media file
names include it.

A typical use case for this modifier is to use a data variable to
create a timestamp, to prevent segments overriding each other if the
channel restarts. For example, assume that you include the timestamp
`$t$-`. Segment 00001 might have the name
`index-120028-00001`. If the output restarts a
few minutes later (which causes the segment counter to restart), the new
segment 00001 will have the name
`index-120039-00001`. The new file won't overwrite
the file for the original segment 00001. Some downstream systems might
prefer this behavior.
