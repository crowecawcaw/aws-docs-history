# Video on demand and live streaming video with CloudFront

You can use CloudFront to deliver video on demand (VOD) or live streaming video by using any
HTTP origin. One way you can set up video workflows in the cloud is by using CloudFront together
with [AWS Media Services](https://aws.amazon.com/media-services/ "https://aws.amazon.com/media-services/").

###### Topics

- [About streaming video](#StreamingVideo "#StreamingVideo")
- [Deliver video on demand with CloudFront](on-demand-video.md "on-demand-video.md")
- [Deliver video streaming with CloudFront and AWS Media Services](live-streaming.md "live-streaming.md")
- [Media quality-aware resiliency](media-quality-score.md "media-quality-score.md")

## About streaming video

You must use an encoder to package video content before CloudFront can distribute the
content. The packaging process creates _segments_ that
contain your audio, video, and captions content. It also generates manifest files, which
describe in a specific order what segments to play and when. Common package formats are
MPEG DASH, Apple HLS, Microsoft Smooth Streaming, and CMAF.

**VOD streaming**

For VOD streaming, your video content is stored on a server and viewers
can watch it at any time. To make an asset that viewers can stream, use an
encoder, such as [AWS Elemental MediaConvert](../../../mediaconvert/latest/ug/getting-started.md "../../../mediaconvert/latest/ug/getting-started.md"), to format and package your media files.

After your video is packaged into the right formats, you can store it on a
server or in an Amazon S3 bucket, and then deliver it with CloudFront as viewers
request it.

**Live video streaming**

For live video streaming, your video content is streamed real time as live
events happen, or is set up as a 24x7 live channel. To create live outputs
for broadcast and streaming delivery, use an encoder such as AWS Elemental MediaLive, to
compress the video and format it for viewing devices.

After your video is encoded, you can store it in AWS Elemental MediaStore or convert it
into different delivery formats by using AWS Elemental MediaPackage. Use either of these
origins to set up a CloudFront distribution to deliver the content. For specific
steps and guidance for creating distributions that work together with these
services, see [Serve video by using AWS Elemental MediaStore as the origin](live-streaming.md#video-streaming-mediastore "live-streaming.md#video-streaming-mediastore") and [Serve live video formatted with AWS Elemental MediaPackage](live-streaming.md#live-streaming-with-mediapackage "live-streaming.md#live-streaming-with-mediapackage").

Wowza and Unified Streaming also provide tools that you can use for streaming video
with CloudFront. For more information about using Wowza with CloudFront, see [Bring your Wowza Streaming Engine license to CloudFront live HTTP streaming](https://www.wowza.com/docs/how-to-bring-your-wowza-streaming-engine-license-to-cloudfront-live-http-streaming "https://www.wowza.com/docs/how-to-bring-your-wowza-streaming-engine-license-to-cloudfront-live-http-streaming")
on the Wowza documentation website. For information about using Unified Streaming with
CloudFront for VOD streaming, see [CloudFront](https://docs.unified-streaming.com/documentation/vod/cloud/amazon/amazon-cloudfront.html "https://docs.unified-streaming.com/documentation/vod/cloud/amazon/amazon-cloudfront.html") on the Unified Streaming documentation website.
