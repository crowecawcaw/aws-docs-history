# Output file names and

paths

The EventBridge job `COMPLETE` notification includes details about your
output in JSON. This information includes the file names and paths for the
outputs of the job—including manifests and media assets.

The files that AWS Elemental MediaConvert creates depends on the output groups that you
set up in the job. For example, DASH ISO packages contain an .mpd manifest and
.mp4 media fragment files.

You can find output file name and path information in the following
properties:

`playlistFilePaths`

A list of the Amazon S3 file paths to the multivariant playlists.

`outputFilePaths`

The file path to either the media or the manifest, depending on
the output group type.

`type`

The type of output group, which determines what files are listed
in the `playlistFilePaths` and
`outputFilePaths`.

The following table summarizes the values for these properties, depending on
the output group type.

| Type                                                | playlistFilePaths                                                                                                                                          | outputFilePaths                                                                                                                                                                             |
| --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `FILE_GROUP` (standard output)                      | _not returned_                                                                                                                                             | File name and path of the media file. Example: `s3://amzn-s3-demo-bucket/file/file.mp4`                                                                                                     |
| `FILE_GROUP` (with additional frame capture output) | _not returned_                                                                                                                                             | File name and path of the final captured image. Example: `s3://amzn-s3-demo-bucket/frameoutput/file.0000036.jpg`                                                                            |
| `HLS_GROUP`                                         | File name and path of the multivariant playlist. Example: `s3://amzn-s3-demo-bucket/hls/main.m3u8`                                                         | File name and path of the manifests for the individual outputs. Examples: <br>• `s3://amzn-s3-demo-bucket/hls/mainv1.m3u8` <br>• `s3://amzn-s3-demo-bucket/hls/mainv2.m3u8`                 |
| `DASH_ISO_GROUP`                                    | File name and path of the manifest. Example: `s3://amzn-s3-demo-bucket/dash/1.mpd`                                                                         | _not returned_                                                                                                                                                                              |
| `CMAF_GROUP`                                        | File name and path for each of the top-level manifests. Examples: <br>• `s3://amzn-s3-demo-bucket/cmaf/1.mpd` <br>• `s3://amzn-s3-demo-bucket/cmaf/1.m3u8` | _not returned_                                                                                                                                                                              |
| `MS_SMOOTH_GROUP`                                   | File name and path of the server-side manifest. Example: `s3://amzn-s3-demo-bucket/smooth/1.ism`                                                           | File name and path of the video manifests for each of the individual outputs. Examples: <br>• `s3://amzn-s3-demo-bucket/smooth/1_va.ismv` <br>• `s3://amzn-s3-demo-bucket/smooth/2_va.ismv` | For sample responses in JSON for each output group type, see the following topics: ###### Topics <br>• [File group](file-group.md "file-group.md") <br>• [File group with a frame capture output](file-group-with-frame-capture-output.md "file-group-with-frame-capture-output.md") <br>• [Apple HLS group](apple-hls-group.md "apple-hls-group.md") <br>• [DASH ISO group](dash-iso-group.md "dash-iso-group.md") <br>• [CMAF group](cmaf-group.md "cmaf-group.md") <br>• [Microsoft Smooth Streaming group](microsoft-smooth-streaming-group.md "microsoft-smooth-streaming-group.md") |
