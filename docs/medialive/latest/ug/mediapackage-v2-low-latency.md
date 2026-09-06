

# Implementing low latency outputs
<a name="mediapackage-v2-low-latency"></a>

You can create a glass-to-glass low latency workflow that uses AWS Elemental MediaLive and AWS Elemental MediaPackage. The channel in AWS Elemental MediaPackage must use MediaPackage v2.

**Note**  
This section assumes that you are familiar with creating or editing a channel, as described in [Creating a channel from scratch](creating-channel-scratch.md). 

Follow these steps:
+ Coordinate with the operator of the MediaPackage operator to obtain the destination URL. See [HLS output group to MediaPackage v2](origin-server-hls-empv2.md).
+ In the channel, create an HLS output group with MediaPackage v2 as the destination. Follow the guideance in [Fields for the output destination – sending to MediaPackage](hls-destinations-emp.md). 
+ When you set up the outputs and the video stream in the output group, follow the guidance for these fields, to achieve optimum latency:



- **HLS Settings, then CDN Settings**
  - **Field:** Connection Retry Interval / **Description:** We recommend the same value as the segment length (in the Manifest Segments section). This value can affect latency.
  - **Field:** Num Retries / **Description:** This value can affect latency.
  - **Field:** Filecache Duration / **Description:** This value can affect latency. We recommend a lower number.
  - **Field:** Restart Delay / **Description:** This value can affect latency.

- **Manifest Segments**
  - **Field:** Segment Length / **Description:** We recommend 1 second for better latency.
  - **Field:** Min Segment Length / **Description:** A value is required for delivery to MediaPackage. This value can affect latency.

- **HLS Output, then Settings then Gop Structure**
  - **Field:** GOP Size / **Description:** This value can affect latency because the segment length is a function of the GOP size. 
  - **Field:** Additional Settings > Closed GOP Cadence / **Description:** This value can affect latency.

