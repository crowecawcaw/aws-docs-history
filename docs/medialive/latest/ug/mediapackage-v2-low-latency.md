# Implementing low latency

outputs

You can create a glass-to-glass low latency workflow that uses AWS Elemental MediaLive
and AWS Elemental MediaPackage. The channel in AWS Elemental MediaPackage must use MediaPackage v2.

###### Note

This section assumes that you are familiar with creating or editing a channel, as
described in [Creating a channel from scratch](creating-channel-scratch.md "creating-channel-scratch.md").

Follow these steps:

- Coordinate with the operator of the MediaPackage operator to obtain the
  destination URL. See [HLS output group to MediaPackage v2](origin-server-hls-empv2.md "origin-server-hls-empv2.md").
- In the channel, create an HLS output group with MediaPackage v2 as the
  destination. Follow the guideance in [Fields for the output destination –
  sending to MediaPackage](hls-destinations-emp.md "hls-destinations-emp.md").
- When you set up the outputs and the video stream in the output
  group, follow the guidance for these fields, to achieve optimum
  latency:

| Section                                  | Field                                                                            | Description                                                                                                              |
| ---------------------------------------- | -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------- | ----------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| HLS Settings, then CDN Settings          | Connection Retry Interval                                                        | We recommend the same value as the segment length (in the **Manifest Segments** section). This value can affect latency. |
| Num Retries                              | This value can affect latency.                                                   |                                                                                                                          | Filecache Duration                           | This value can affect latency. We recommend a lower number. |
| Restart Delay                            | This value can affect latency.                                                   |
| Manifest Segments                        | Segment Length                                                                   | We recommend 1 second for better latency.                                                                                |
| Min Segment Length                       | A value is required for delivery to MediaPackage. This value can affect latency. |                                                                                                                          | HLS Output, then Settings then Gop Structure | GOP Size                                                    | This value can affect latency because the segment length is a function of the GOP size. |
| Additional Settings > Closed GOP Cadence | This value can affect latency.                                                   |
