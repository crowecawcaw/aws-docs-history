# VOD Content Processing

In the processing flow for VOD content, AWS Elemental MediaPackage
ingests file-based video content from Amazon S3. MediaPackage then packages the content,
formatting it in response to playback requests from downstream devices.

Here is the general processing flow for VOD content in
MediaPackage:

1. From the MediaPackage asset, you initiate ingest of the source
   content from an Amazon S3 bucket. This process can take several minutes. You
   receive an Amazon CloudWatch event when ingest is complete and the playback URLs
   are live.
2. A downstream device requests content from MediaPackage through the
   packaging configuration URL on the asset. A downstream device is either a video player or a
   CDN. The URL is associated with a
   configuration for a specific streaming format (either Apple HLS, DASH-ISO, Microsoft Smooth Streaming,
   or CMAF).
3. When MediaPackage receives the playback request from the downstream
   device, it dynamically packages the stream according to the settings that
   you specified in the packaging configuration. Packaging can include adding encryption and
   configuring audio, video, and subtitles or captions track outputs.

Be sure to order your inputs so that your preferred audio rendition is
listed first in the audio section of the parent manifest. Do the same for
the subtitles or captions. When packaging audio and subtitles or captions
tracks, MediaPackage designates the first audio and captions or subtitles track as
`DEFAULT=YES` and `AUTO-SELECT=YES`. This
packaging overrides default and auto-select settings from the input. 4. MediaPackage delivers the output stream over HTTPS to the requesting
device. As with input, AWS scales resources up and down to handle changes
in traffic. 5. MediaPackage logs activity through Amazon CloudWatch. You can view information
like the number of content requests and amount of content that MediaPackage
has delivered. For information about viewing MediaPackage VOD
metrics in CloudWatch, see [Monitoring AWS Elemental MediaPackage with Amazon CloudWatch
metrics](monitoring-cloudwatch.md "monitoring-cloudwatch.md").
Throughout the content input and output processes, MediaPackage detects and
mitigates potential infrastructure failures before they become a problem for
viewers.
