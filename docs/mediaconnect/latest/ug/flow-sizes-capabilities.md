

# Flow sizes and capabilities
<a name="flow-sizes-capabilities"></a>

A flow size determines how much video throughput your flow can handle and which source and output types it supports. Choosing the right size ensures your flow can accommodate your required number of outputs, handle your desired video quality, and support specific features like NDI® or AWS Cloud Digital Interface (CDI).

## Flow size options
<a name="flow-size-options"></a>

MediaConnect currently offers three flow sizes: Medium, Large and Large 4x. Medium is the default option and suitable for most standard streaming requirements. Large flows provide enhanced capabilities for higher throughput and specialized features such as NDI sources and outputs. Large 4x flows support high-quality uncompressed content with AWS Cloud Digital Interface (CDI) or lightly compressed content with JPEG XS via the SMPTE 2110, part 22 transport standard. 

## Managing flow sizes
<a name="managing-flow-sizes"></a>
+ When creating a new flow, you'll select either Medium, Large or Large 4x as the size, with Medium being the default choice. 
+ After the flow is created, you can update Medium flows to Large or Large flows to Medium. 
+ You can't update the size of a Large 4x flow after the flow is created. 
+ Some older flows may display no size designation (`-`) in the flow details. These flows function at a medium capacity.

## Compare flow sizes
<a name="flow-sizes-reference-table"></a>

Use this table to compare flow sizes and select the one that meets your needs.



<table>
<thead>
  <tr><th></th><th></th><th colspan="2">Transport Streams</th><th colspan="2">NDI</th><th colspan="2">CDI</th></tr>
  <tr><th>Flow Size</th><th>Use Case</th><th>Output limits</th><th>Throughput</th><th>Output limits</th><th>Throughput</th><th>Output limits</th><th>Throughput</th></tr>
</thead>
<tbody>
  <tr><td>Medium</td><td>Standard transport stream distribution</td><td> <ul><li> Up to 50 transport stream outputs, or up to four TR-07 outputs </li></ul> </td><td> <ul><li> 400 Mbps combined for transport streams </li><li> 1 Gbps combined for TR-07 </li></ul> </td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td></tr>
  <tr><td>Large</td><td>Transport stream distribution and NDI</td><td> <ul><li> Up to 50 transport stream outputs (may include 1 NDI output), or up to four TR-07 outputs  </li></ul> </td><td> <ul><li> 400 Mbps combined for transport streams </li><li> 1 Gbps combined for TR-07 </li></ul> </td><td> <ul><li> Up to 1 NDI output </li><li> The NDI output can support multiple NDI receivers in the same VPC subnet </li></ul> </td><td> <ul><li> 2 Gbps total aggregate throughput </li></ul> </td><td>N/A</td><td>N/A</td></tr>
  <tr><td>Large 4x</td><td>Production environments requiring CDI or SMPTE 2110 with JPEG XS</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td> <ul><li> Up to 10 outputs  </li><li> For 4Kp60 content, up to 10 SMPTE 2110 JPEG XS outputs, or 4 CDI outputs  </li></ul> </td><td> <ul><li> 50 Gbps total aggregate throughput </li></ul> </td></tr>
</tbody>
</table>


For information about flow pricing, see [AWS Elemental MediaConnect Pricing](https://aws.amazon.com/mediaconnect/pricing/).

## Flow bandwidth alerts
<a name="flow-bandwidth-alerts"></a>

When the network bandwidth usage for a flow is approaching the maximum supported capacity, MediaConnect publishes an alert on the flow details page. The video output bitrate is typically the primary contributor to the total bandwidth usage, but the bandwidth required for general flow operations also counts towards the threshold. 

When you see this alert, you should consider taking action to reduce the load and stay within supported limits. For example, you can do the following:
+ Decrease the number of outputs in the flow 
+ Lower the source bitrate or the quality of the video input 

For instructions on how to review the alerts for a flow, see [Viewing the details of a flow](flows-view-details.md). 