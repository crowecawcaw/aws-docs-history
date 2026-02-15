# Using MediaConnect flows

A MediaConnect flow is a connection between one or more video sources and one or more outputs. For each flow, you specify
the protocol to use, encryption information, and details about the source. MediaConnect returns an ingest endpoint
where you can send your live video as a single unicast stream. The service replicates and distributes
the video to every output that you specify, whether inside or outside the AWS Cloud.

## Key points

### Flows concepts and terminology

Before working with flows, familiarize yourself with these key concepts and
terms.

**Flow components**

- **Source**

External video content that includes configuration information (encryption and source type)
and a network address. Each flow has at least one source. A standard source comes from a source other
than another MediaConnect flow, such as an on-premises encoder. An entitled source comes from a MediaConnect flow
that is owned by another AWS account and has granted an entitlement to your account.

- **Output**

The destination where you want MediaConnect to send ingested video. An output can have the same protocol
or a different protocol from the source.

- **Protocol**

A set of rules used for video and audio transmission. MediaConnect provides protocol options
(such as Zixi, RTP, and RTP-FEC) that implement a quality of service (QoS) layer to enable the service
to work with mezzanine-quality live video.

**Cross account content sharing**

- **Entitlement**

A permission that is granted to allow an AWS account to access the content in a specific
MediaConnect flow. The content originator grants an entitlement to a specific AWS account (the subscriber).
Once an entitlement is granted, the subscriber can create a flow using the originator's flow as the source.
You can only grant entitlements to transport stream flows.

- **Originator account**

An AWS account that was used to create a flow with at least one entitlement.

- **Subscriber account**

An AWS account that been granted access to content from an AWS Elemental MediaConnect flow that is owned
by another AWS account (the originator account). This permission is granted when the originator sets
up an entitlement for the subscriber. The entitlement permits the subscriber to create a flow that
uses the originator's content as the source.

**VPC interfaces**

- **VPC interface**

A connection between a flow and a virtual private cloud (VPC) that was created using the
Amazon Virtual Private Cloud (Amazon VPC) service.

**AWS CDI and SMPTE 2110 support**

- **AWS CDI flow**

A MediaConnect flow that transports high-quality content that has been
lightly compressed using JPEG XS. The content is demuxed into separate media
streams for audio, video, or ancillary data. Each AWS CDI flow can use multiple
media streams for the source and multiple media streams for each output.
MediaConnect uses AWS Cloud Digital Interface (AWS CDI) network technology to ingest content
that adheres to the SMPTE 2110, part 22 transport standard.

- **Media stream**

A single track or stream of media that contains video, audio, or ancillary
data. After you add a media stream to a flow, you can associate it with
sources and outputs on that flow, as long as they use the AWS CDI protocol or
the ST 2110 JPEG XS protocol. Each source or output can consist of one or
many media streams.

- **Mezzanine stream**

A lightly compressed video stream that takes up less space than a full
resolution uncompressed stream. The quality of a mezzanine stream is high
enough to use as a source for creating final encodes that are delivered to
consumer devices.

## How flows work

### Flows setup

Building on these concepts, the following steps show how you set up and use flows at
a high level:

1. **Create a flow** - Set up a flow to receive content from an upstream sender
   and send the content to one or more downstream receivers.
2. **Start the flow** - Change the flow status from Standby to Active when you're
   ready to begin streaming.

You can do these steps manually in the console, or programmatically using the MediaConnect API.

## Flows capabilities and management

Flows provide several key capabilities for managing your media workflows. You can:

- Ingest live video into the AWS Cloud.
- Distribute live video to multiple destinations inside or outside the AWS Cloud.
- Subscribe to a live video stream that is supplied by another AWS account.
  This requires permission from the content originator through an entitlement.
- Send content from one AWS Region to another.

You manage these functions through the MediaConnect console, where you can:

- See all your active flows.
- Start and stop multiple flows at the same time.
- Create, delete and update flows.

MediaConnect manages flows maintenance through automated scheduling, with restarts occurring
approximately every 60 days from the time when you start the flows. You can customize these maintenance
windows by selecting your preferred day and start hour when you create or update your
flows. You can monitor when your next maintenance window begins by checking the console.

## Flows considerations and limitations

As you plan your flow implementation, keep these points in mind.

| Flow features and considerations | Feature                                                                                                                                                                                                                                                                                                                                                                                                                       | Description |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| Supported protocols              | MediaConnect flows support multiple protocols to enable compatibility across<br>hybrid workflows.<br>The following protocols are currently supported: RTP, RTP-FEC, RIST, SRT-listener, SRT-caller,<br>Zixi-Pull, Zixi-Push and NDI®.                                                                                                                                                                                         |
| Cross account content sharing    | Content originators can grant entitlements to share their content with other AWS accounts (subscriber accounts).<br>Subscribers can then set up their own MediaConnect flows using the originator's flow as their source.                                                                                                                                                                                                     |
| Flows capacity                   | You can create up to 20 flows in each AWS Region.<br>Each flow supports up to 50 outputs.                                                                                                                                                                                                                                                                                                                                     |
| Source failover and merge        | MediaConnect flows support both automatic failover between redundant sources and<br>merged content from two source endpoints.<br>Supported protocols:<br>• Failover: RTP, RTP-FEC, RIST, SRT-listener, SRT-caller, Zixi-Push<br>• Merge: RTP, RTP-FEC, RIST, Zixi-Push<br>Both sources must:<br>• Use the same protocol configuration<br>• Use the same network configuration (VPC or public)<br>• Use different port numbers |
| MediaConnect router integration  | The MediaConnect router supports routing to or from MediaConnect flows.<br>For more details on flow integration considerations,<br>see [Integrating router<br>I/Os with MediaConnect<br>flows](integrate-flow-with-router.md "integrate-flow-with-router.md").                                                                                                                                                                |

## Next steps

You can learn how to set up and use flows in the following pages of this guide:

- [Managing flows in MediaConnect](flows.md "flows.md")
- [Managing sources in MediaConnect](sources.md "sources.md")
- [Managing outputs in MediaConnect](outputs.md "outputs.md")
- [Managing entitlements in MediaConnect](entitlements.md "entitlements.md")
- [VPC interfaces](vpc-interfaces.md "vpc-interfaces.md")
- [Protocols in MediaConnect](protocols.md "protocols.md")
- [Media streams in MediaConnect](media-streams.md "media-streams.md")
- [Best practices for MediaConnect flows](best-practices.md "best-practices.md")
