# Flow sizes and capabilities

A flow size determines how much video throughput your flow can handle and which output
types it supports. Choosing the right size ensures your flow can accommodate your
required number of outputs, handle your desired video quality, and support specific
features like NDI® outputs.

## Flow size options

MediaConnect currently offers two flow sizes: medium and large. Medium is the
default option and suitable for most standard streaming requirements. Large flows
provide enhanced capabilities for higher throughput and specialized features such as
NDI outputs.

## Managing flow sizes

- When creating a new transport stream flow, you'll select either Medium or
  Large as the size, with Medium being the default choice.
- Some older flows may display no size designation (`-`) in the
  flow details. These flows function at a medium capacity.

## Compare flow sizes

Use this table to compare flow sizes and select the one that meets your
needs.

| Flow size | Use case                                | Features                                                             | Output limits                                                        | Throughput                                                                       |
| --------- | --------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Medium    | Standard video distribution without NDI | <br>• Transport stream outputs <br>• TR-07 outputs                   | <br>• Up to 50 transport stream outputs, or up to four TR-07 outputs | <br>• 400 Mbps combined for transport streams <br>• 1.25 Gbps combined for TR-07 |
| Large     | Production environments requiring NDI   | <br>• Transport stream outputs <br>• TR-07 outputs <br>• NDI outputs | <br>• Up to 50 transport stream outputs, or up to four TR-07 outputs | <br>• 2.5 Gbps total aggregate throughput                                        | For information about flow pricing, see [AWS Elemental MediaConnect Pricing](https://aws.amazon.com/mediaconnect/pricing/ "https://aws.amazon.com/mediaconnect/pricing/"). ## Flow bandwidth alerts When the network bandwidth usage for a flow is approaching the maximum supported capacity, MediaConnect publishes an alert on the flow details page. The video output bitrate is typically the primary contributor to the total bandwidth usage, but the bandwidth required for general flow operations also counts towards the threshold. When you see this alert, you should consider taking action to reduce the load and stay within supported limits. For example, you can do the following: <br>• Decrease the number of outputs in the flow <br>• Lower the source bitrate or the quality of the video input For instructions on how to review the alerts for a flow, see [Viewing the details of a flow](flows-view-details.md "flows-view-details.md"). |
