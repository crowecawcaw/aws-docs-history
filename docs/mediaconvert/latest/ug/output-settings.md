# Creating outputs

A single MediaConvert job
can
create outputs as a standalone file (for example, an .mp4 file), a set of
files for adaptive bitrate (ABR) streaming (for example, an Apple HLS
package), or combinations of both. When you create output groups and the outputs within
them, you specify the number and types of files that your job generates.

When your MediaConvert job is complete, you can use Amazon CloudFront, or another content
distribution network (CDN), to deliver your streaming package. The CDN gets your video to
the people who want to view it. For more information, see [Delivering video on demand (VOD) with
CloudFront](../../../AmazonCloudFront/latest/DeveloperGuide/on-demand-video.md "../../../AmazonCloudFront/latest/DeveloperGuide/on-demand-video.md").

The topics in this section explain the relationship between MediaConvert output groups,
MediaConvert outputs, and the actual output files that MediaConvert delivers to you.

###### Topics

- [Setting up captions in outputs](set-up-captions-in-outputs.md "set-up-captions-in-outputs.md")
- [Using output groups to specify a streaming package
  type or standalone file](outputs-file-ABR.md "outputs-file-ABR.md")
- [Choosing your ABR streaming
  output groups](choosing-your-streaming-output-groups.md "choosing-your-streaming-output-groups.md")
- [Recommended encoding settings for video quality](video-quality.md "video-quality.md")
- [Using variables in your job settings](using-variables-in-your-job-settings.md "using-variables-in-your-job-settings.md")
