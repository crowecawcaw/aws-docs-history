

# Using NDI® sources in a MediaConnect flow
<a name="sources-using-ndi"></a>

AWS Elemental MediaConnect can ingest [Network Device Interface (NDI®)](https://ndi.video/tech/), a protocol for high-quality, low-latency video and audio over IP networks, and convert it into MPEG transport streams. This capability enables direct content ingestion within your network, connecting IP-based video production systems with traditional contribution workflows. 

Using NDI sources, you can create streamlined production workflows that take content from your NDI-enabled production systems—such as cameras, vision mixers, and graphics engines—and ingest it directly into a MediaConnect flow from your Virtual Private Cloud (VPC). MediaConnect then converts this NDI input into transport streams, which can be distributed to traditional broadcast infrastructure using protocols like SRT or Zixi. This integration works with your existing NDI infrastructure, requiring no modifications to your current VPC setup. 

## Key points
<a name="using-ndi-sources-key-points"></a>

### Understanding NDI terminology
<a name="using-ndi-sources-terminology"></a>

In video and audio workflows, the terms **source** and **output** have specific meanings that vary between contexts. Understanding these differences helps you work with NDI sources across your production workflow.
+ In MediaConnect flows:
  + A **source** is the entry point of a flow. **NDI sources** ingest NDI content into your flow from an upstream NDI sender.
  + An **output** is the exit point of a flow. **NDI outputs** send NDI content from your flow to a downstream NDI receiver.
+ In NDI implementation:
  + An **NDI sender** is a network endpoint that sends video and audio streams over IP networks using the NDI protocol.
  + From the perspective of your MediaConnect flow, the NDI sender is the upstream device that provides content to your flow’s NDI source.
  + When you add an NDI source to your MediaConnect flow, MediaConnect acts as an NDI receiver by connecting to an NDI sender in your network. Your flow can then convert this content for distribution through traditional broadcast protocols. 

### How NDI sources work
<a name="using-ndi-sources-how-it-works"></a>

At a high level, here’s how your content moves through MediaConnect when you use NDI sources in your flows:

1. Set up your VPC infrastructure with at least one NDI discovery server and active NDI senders within the VPC.

1. Create a large-sized flow with an NDI source, configuring your discovery servers and the NDI source settings.

1. Start your flow to discover the NDI senders that are broadcasting content within your VPC.

1. Connect to your selected NDI sender to start receiving content into your flow.

1. Convert and distribute the content through your flow outputs using transport stream protocols such as SRT or Zixi.

This workflow maintains compatibility with NDI-based production systems while adding the flexibility and networking advantages of traditional broadcast distribution.

### Considerations and limitations
<a name="using-ndi-sources-considerations"></a>

When planning your NDI source implementation in MediaConnect, keep in mind the following.


<table>
<thead>
  <tr><th colspan="2">Consideration</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td rowspan="7">Basic requirements and configuration</td><td>Required flow size </td><td>NDI flow sources work only with large flows.</td></tr>
  <tr><td rowspan="3">VPC requirements</td><td>At least one NDI discovery server is required for each flow (up to a maximum of three).</td></tr>
  <tr><td>NDI discovery servers must already be provisioned and accessible in your VPC network. MediaConnect connects to these servers, but it doesn't create them for you.</td></tr>
  <tr><td>NDI sources must be accessible through your VPC infrastructure. All NDI traffic remains within your VPCs.</td></tr>
  <tr><td>Encoding requirements</td><td>You must configure encoding profiles to convert NDI to transport streams. Each flow uses one encoding profile for all its transport stream outputs. <br />You can customize bitrates within the profile limits. </td></tr>
  <tr><td>Flow source limitations</td><td>You can use one NDI source for each large-sized flow. Failover and merge modes aren't supported for NDI sources.</td></tr>
  <tr><td>Flow output compatibility</td><td>When using an NDI source in your flow, you can use any supported transport stream protocol for the flow output (RTP, RTP+FEC, SRT, Zixi, and RIST). <br />You can't use an NDI source and an NDI output in the same flow. </td></tr>
  <tr><td rowspan="3">Management and operations</td><td>Flow source management</td><td>You can switch between an NDI source and a transport stream source while the flow is active or on standby.<ul><li> Before switching to an NDI source, you must first upgrade your flow size to large. </li><li> When switching to a transport stream source, the flow size remains large unless you choose to downgrade the size afterwards. </li></ul></td></tr>
  <tr><td>Monitoring</td><td>You can monitor the NDI source connection status through CloudWatch metrics. </td></tr>
  <tr><td>Cross-Region support</td><td>NDI sources are VPC-bound and can't span across different AWS Regions. Each flow can only receive NDI traffic from a source VPC subnet that's in the same AWS Region as your flow. </td></tr>
  <tr><td rowspan="6">Technical specifications</td><td>Transport protocols</td><td>When using NDI as your flow source, the content is transported using TCP.</td></tr>
  <tr><td>NDI protocols</td><td>Only NDI high quality (HQ) is supported. NDI HX isn't supported.</td></tr>
  <tr><td>Timecode processing</td><td>Timecodes that are embedded in the NDI source will be inserted to the encoded AVC (H.264) video in an SEI message of type pic_timing, in accordance with section D.1.2 of ISO/IEC 14496-10-2005.</td></tr>
  <tr><td>Discovery and connection methods</td><td>MediaConnect supports connections to NDI sources through NDI discovery servers only. Direct mDNS discovery or manual connection to NDI sources isn't supported.</td></tr>
  <tr><td rowspan="2">NDI feature support</td><td>NDI groups aren't supported.</td></tr>
  <tr><td>NDI genlock isn't supported.</td></tr>
</tbody>
</table>


## Next steps
<a name="using-ndi-sources-next-steps"></a>

To get started, [create a flow](flows-create-ndi.md) with an NDI source.

## Additional resources
<a name="using-ndi-outputs-additional-resources"></a>
+ [Flow sizes and capabilities](flow-sizes-capabilities.md)
+ [Best practices](best-practices.md)