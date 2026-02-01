# Using NDI®

sources in a MediaConnect flow

AWS Elemental MediaConnect can ingest [Network Device
Interface (NDI®)](https://ndi.video/tech/ "https://ndi.video/tech/"), a protocol for high-quality, low-latency video and audio
over IP networks, and convert it into MPEG transport streams. This capability enables
direct content ingestion within your network, connecting IP-based video production
systems with traditional contribution workflows.

Using NDI sources, you can create streamlined production workflows that take content
from your NDI-enabled production systems—such as cameras, vision mixers, and graphics
engines—and ingest it directly into a MediaConnect flow from your Virtual Private Cloud
(VPC). MediaConnect then converts this NDI input into transport streams, which can be
distributed to traditional broadcast infrastructure using protocols like SRT or Zixi.
This integration works with your existing NDI infrastructure, requiring no modifications
to your current VPC setup.

## Key points

### Understanding NDI

terminology

In video and audio workflows, the terms **source** and **output** have specific
meanings that vary between contexts. Understanding these differences helps you
work with NDI sources across your production workflow.

- In MediaConnect flows:
  - A **source** is the entry point
    of a flow. **NDI sources** ingest
    NDI content into your flow from an upstream NDI sender.
  - An **output** is the exit point
    of a flow. **NDI outputs** send NDI
    content from your flow to a downstream NDI receiver.

- In NDI implementation:
  - An **NDI sender** is a network
    endpoint that sends video and audio streams over IP networks
    using the NDI protocol.
  - From the perspective of your MediaConnect flow, the NDI sender is the
    upstream device that provides content to your flow’s NDI
    source.
  - When you add an NDI source to your MediaConnect flow, MediaConnect acts as
    an NDI receiver by connecting to an NDI sender in your network.
    Your flow can then convert this content for distribution through
    traditional broadcast protocols.

### How NDI sources work

At a high level, here’s how your content moves through MediaConnect when you use NDI
sources in your flows:

1. Set up your VPC infrastructure with at least one NDI discovery server
   and active NDI senders within the VPC.
2. Create a large-sized flow with an NDI source, configuring your
   discovery servers and the NDI source settings.
3. Start your flow to discover the NDI senders that are broadcasting
   content within your VPC.
4. Connect to your selected NDI sender to start receiving content into
   your flow.
5. Convert and distribute the content through your flow outputs using
   transport stream protocols such as SRT or Zixi.

This workflow maintains compatibility with NDI-based production systems while
adding the flexibility and networking advantages of traditional broadcast
distribution.

### Considerations and

limitations

When planning your NDI source implementation in MediaConnect, keep in mind the
following.

| Consideration                                                                                                                                                           | Description                                                                                                                                                                                                                  |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Basic requirements and configuration                                                                                                                                    | Required flow size                                                                                                                                                                                                           | NDI flow sources work only with large flows.                                                                                                                                                                                                                                                                                                     |
| VPC requirements                                                                                                                                                        | At least one NDI discovery server is required for each<br>flow (up to a maximum of three).                                                                                                                                   |
| NDI discovery servers must already be provisioned and<br>accessible in your VPC network. MediaConnect connects to these<br>servers, but it doesn't create them for you. |
| NDI sources must be accessible through your VPC<br>infrastructure. All NDI traffic remains within your<br>VPCs.                                                         |
| Encoding requirements                                                                                                                                                   | You must configure encoding profiles to convert NDI to<br>transport streams.<br>Each flow uses one encoding profile for all its transport stream outputs.<br>You can customize bitrates within the profile limits.           |
| Flow source limitations                                                                                                                                                 | You can use one NDI source for each large-sized<br>flow.<br>Failover and merge modes aren't supported for NDI sources.                                                                                                       |
| Flow output compatibility                                                                                                                                               | When using an NDI source in your flow, you can use any<br>supported transport stream protocol for the flow output<br>(RTP, RTP+FEC, SRT, Zixi, and RIST).<br>You can't use an NDI source and an NDI output in the same flow. |
| Management and operations                                                                                                                                               | Flow source management                                                                                                                                                                                                       | You can switch between an NDI source and a transport<br>stream source while the flow is active or on standby.<br>• Before switching to an NDI source, you must first<br>upgrade your flow size to large.<br>• When switching to a transport stream source, the<br>flow size remains large unless you choose to<br>downgrade the size afterwards. |
| Monitoring                                                                                                                                                              | You can monitor the NDI source connection status through CloudWatch<br>metrics.                                                                                                                                              |
| Cross-Region support                                                                                                                                                    | NDI sources are VPC-bound and can't span across different<br>AWS Regions. Each flow can only receive NDI traffic from a<br>source VPC subnet that's in the same AWS Region as your<br>flow.                                  |
| Technical specifications                                                                                                                                                | Transport protocols                                                                                                                                                                                                          | When using NDI as your flow source, the content is<br>transported using TCP.                                                                                                                                                                                                                                                                     |
| NDI protocols                                                                                                                                                           | Only NDI high quality (HQ) is supported. NDI HX isn't<br>supported.                                                                                                                                                          |
| Discovery and connection methods                                                                                                                                        | MediaConnect supports connections to NDI sources through NDI<br>discovery servers only. Direct mDNS discovery or manual<br>connection to NDI sources isn't supported.                                                        |
| NDI feature support                                                                                                                                                     | NDI groups aren't supported.                                                                                                                                                                                                 |
| NDI genlock isn't supported.                                                                                                                                            |

## Next steps

To get started, [create a flow](flows-create-ndi.md "flows-create-ndi.md") with an NDI
source.

## Additional

resources

- [Flow sizes and
  capabilities](flow-sizes-capabilities.md "flow-sizes-capabilities.md")
- [Best practices](best-practices.md "best-practices.md")
