# Flow sizes and capabilities

A flow size determines how much video throughput your flow can handle and which source
and output
types it supports. Choosing the right size ensures your flow can accommodate your
required number of outputs, handle your desired video quality, and support specific
features like NDI® or AWS Cloud Digital Interface (CDI).

## Flow size options

MediaConnect currently offers three flow sizes: Medium, Large and Large 4x. Medium is the
default option and suitable for most standard streaming requirements. Large flows
provide enhanced capabilities for higher throughput and specialized features such as
NDI sources and outputs. Large 4x flows support high-quality uncompressed content with AWS Cloud Digital Interface (CDI)
or lightly compressed content with JPEG XS via the SMPTE 2110, part 22 transport standard.

## Managing flow sizes

- When creating a new flow, you'll select either Medium, Large or
  Large 4x as the size, with Medium being the default choice.
- After the flow is created, you can update Medium flows to Large or Large
  flows to Medium.
- You can't update the size of a Large 4x flow after the flow is created.
- Some older flows may display no size designation (`-`) in the
  flow details. These flows function at a medium capacity.

## Compare flow sizes

Use this table to compare flow sizes and select the one that meets your
needs.

|           |                                                                  | Transport Streams                                                                              | NDI                                                                      | CDI                                                                                                |
| --------- | ---------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------ |
| Flow Size | Use Case                                                         | Output limits                                                                                  | Throughput                                                               | Output limits                                                                                      | Throughput                          | Output limits                                                                                    | Throughput                           |
| Medium    | Standard transport stream distribution                           | • Up to 50 transport stream outputs, or up to four TR-07 outputs                               | • 400 Mbps combined for transport streams<br>• 1 Gbps combined for TR-07 | N/A                                                                                                | N/A                                 | N/A                                                                                              | N/A                                  |
| Large     | Transport stream distribution and NDI                            | • Up to 50 transport stream outputs (may include 1 NDI output),<br>or up to four TR-07 outputs | • 400 Mbps combined for transport streams<br>• 1 Gbps combined for TR-07 | • Up to 1 NDI output<br>• The NDI output can support multiple NDI receivers in the same VPC subnet | • 2 Gbps total aggregate throughput | N/A                                                                                              | N/A                                  |
| Large 4x  | Production environments requiring CDI or SMPTE 2110 with JPEG XS | N/A                                                                                            | N/A                                                                      | N/A                                                                                                | N/A                                 | • Up to 10 outputs<br>• For 4Kp60 content, up to 10 SMPTE 2110 JPEG XS outputs, or 4 CDI outputs | • 50 Gbps total aggregate throughput |

For information about flow pricing, see [AWS Elemental MediaConnect Pricing](https://aws.amazon.com/mediaconnect/pricing/ "https://aws.amazon.com/mediaconnect/pricing/").

## Flow bandwidth alerts

When the network bandwidth usage for a flow is approaching the maximum supported
capacity, MediaConnect publishes an alert on the flow details page. The video output
bitrate is typically the primary contributor to the total bandwidth usage, but the
bandwidth required for general flow operations also counts towards the threshold.

When you see this alert, you should consider taking action to reduce the load and
stay within supported limits. For example, you can do the following:

- Decrease the number of outputs in the flow
- Lower the source bitrate or the quality of the video input

For instructions on how to review the alerts for a flow, see [Viewing the details of a flow](flows-view-details.md "flows-view-details.md").
