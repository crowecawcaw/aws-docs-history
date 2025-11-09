# Using NDI® outputs in a MediaConnect

flow

AWS Elemental MediaConnect can convert MPEG transport streams into [Network Device Interface (NDI®)](https://ndi.video/tech/ "https://ndi.video/tech/"), a
protocol for high-quality, low-latency video and audio over IP networks. This
capability enables direct content delivery within your network, connecting
traditional contribution workflows with IP-based video production systems.

Using NDI outputs, you can create streamlined production workflows that take
content from your AVC or HEVC-based encoder, process it through a MediaConnect flow as a
transport stream, and output it directly into your Virtual Private Cloud (VPC) as
NDI. Your production systems—including vision mixers, audio mixers, replay systems,
and graphics engines—can immediately access these NDI streams through standard NDI
discovery. This integration works with your existing NDI infrastructure, requiring
no modifications to your current VPC setup.

## Key points

### Understanding NDI

terminology

In video and audio workflows, the terms _source_ and _output_ have
specific meanings that vary between contexts. Understanding these
differences helps you work with NDI outputs across your production
workflow.

- In MediaConnect flows:
  - A _source_ is the
    incoming video and audio feed to the flow. NDI isn’t
    currently supported as a source type.
  - An _output_ determines
    where and how your content is delivered. NDI is supported as
    an output type.

- In NDI implementation:
  - An NDI source is a network endpoint that sends video and
    audio streams over IP networks using the NDI protocol.
  - When you add an NDI output to your MediaConnect flow, MediaConnect acts
    as an NDI sender by creating an NDI source. Your production
    systems can then connect to this source as NDI receivers to
    get the video and audio stream.

In summary: Your MediaConnect flow takes video and audio from a flow source and,
with an NDI flow output enabled, it creates an NDI source that your
production systems can receive from.

### How NDI outputs

work

At a high level, here’s how your content moves through MediaConnect when you use
NDI outputs:

1. You create a large sized flow with NDI enabled, configuring your
   discovery servers and NDI output settings.
2. You send content to the flow source, using supported transport
   stream protocols such as SRT or Zixi.
3. MediaConnect processes the content to the flow output, creating a
   discoverable NDI source in your VPC.
4. The production systems in your network can now discover and
   connect to these endpoints and receive your content.

This workflow maintains compatibility with existing broadcast
infrastructure while adding the flexibility and networking advantages of NDI
distribution.

### White screen

generation for NDI outputs

When you configure a transport stream flow with NDI outputs, MediaConnect
automatically generates white video frames to provide a valid source signal
for downstream NDI devices. This helps you confirm that your NDI output is
properly configured and functioning, even when your source isn't actively
sending content.

The white frame generation operates as follows:

- **On initial flow startup** - If no
  source content is received within 10 seconds, MediaConnect generates white
  frames with silent audio on your NDI output.
- **After a source has connected and started
  sending content** - If a source disconnects for more
  than 60 seconds, MediaConnect generates white frames with silent
  audio.

This feature is particularly useful when you're setting up flows in
advance of live events, or in situations where your source content isn't
immediately available. The white frames serve as a visual indicator that
your NDI output is working correctly and is ready to receive source content.
This is more informative than seeing a black screen, which could either
indicate a loss of signal or intentional black video content from your
source.

This feature is available exclusively for NDI outputs. You don't need to
configure or enable white screen generation - it works automatically
whenever your flow is in a running state but isn't receiving source content.
When your source starts sending content to your flow, the source content
automatically replaces the white frames. MediaConnect stops generating silent audio
frames, and the audio passes through from the source.

### Considerations and

limitations

When planning your NDI output implementation in MediaConnect, keep in mind the
following.

| Consideration                                                                                                                                                                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Flow type                                                                                                                                                                                                                                                                                                                                                                                         | NDI outputs are only supported for standard transport<br>stream flows.<br>You can use them with all types of transport stream<br>sources (standard source, entitled source, or VPC<br>source).                                                                                                                                                                                                                                                                                                                                             |
| Flow size                                                                                                                                                                                                                                                                                                                                                                                         | The NDI output feature can only be used on large-sized<br>flows.<br>You can specify the flow size as large when you create<br>a new flow. However, you can't upgrade or downgrade the<br>size of an existing flow.                                                                                                                                                                                                                                                                                                                         |
| Supported source protocols                                                                                                                                                                                                                                                                                                                                                                        | NDI outputs are compatible with all supported source<br>protocols (RTP, RTP+FEC, SRT, Zixi, and RIST).                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Transport protocols                                                                                                                                                                                                                                                                                                                                                                               | MediaConnect uses TCP as the transport protocol for<br>NDI.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Multi-program source handling                                                                                                                                                                                                                                                                                                                                                                     | NDI outputs can only be created using single program<br>transport stream sources.<br>For multi-program transport stream sources, the NDI<br>output only transmits the first program available to<br>downstream receivers.                                                                                                                                                                                                                                                                                                                  |
| Output configuration                                                                                                                                                                                                                                                                                                                                                                              | NDI is supported for flow outputs only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| You can add one NDI output to each large-sized<br>flow.                                                                                                                                                                                                                                                                                                                                           |
| At least one NDI discovery server is required for each<br>flow (up to a maximum of three).                                                                                                                                                                                                                                                                                                        |
| You can combine an NDI output with transport stream<br>outputs in the same flow.<br>NoteKeep in mind that NDI outputs are resource<br>intensive, and adding an NDI output will reduce the<br>number of transport stream outputs you can run<br>simultaneously.For more information about best practices for<br>using NDI outputs, see [Best<br>practices](best-practices.md "best-practices.md"). |
| Network architecture                                                                                                                                                                                                                                                                                                                                                                              | NDI discovery servers must already be provisioned and<br>accessible in your VPC network. MediaConnect connects to these<br>servers, but it doesn't create them for you.                                                                                                                                                                                                                                                                                                                                                                    |
| NDI outputs must be delivered through your VPC<br>infrastructure. All NDI traffic remains within your<br>VPCs.                                                                                                                                                                                                                                                                                    |
| You can use one NDI output per VPC interface.                                                                                                                                                                                                                                                                                                                                                     |
| You can use up to three VPC interfaces per flow to<br>send video to different subnets. This means you can<br>distribute your video stream to up to three different<br>network segments from a single flow.                                                                                                                                                                                        |
| You can use two discovery servers in the same subnet.<br>However, you can't use two discovery servers with the<br>same IP address in different subnets.                                                                                                                                                                                                                                           |
| Receiver capacity                                                                                                                                                                                                                                                                                                                                                                                 | One NDI output can support multiple NDI receivers in<br>the same VPC subnet.                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| We recommend that you monitor flow performance when<br>multiple receivers connect to a single output, as this<br>can impact CPU and memory usage.                                                                                                                                                                                                                                                 |
| You can monitor the number of NDI receiver connections<br>through the `ConnectedReceivers` metric in<br>CloudWatch.                                                                                                                                                                                                                                                                               |
| NDI feature support                                                                                                                                                                                                                                                                                                                                                                               | NDI groups aren't supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| NDI failsafe sources/senders aren't supported.                                                                                                                                                                                                                                                                                                                                                    |
| NDI genlock isn't supported.                                                                                                                                                                                                                                                                                                                                                                      |
| Discovery and connection methods                                                                                                                                                                                                                                                                                                                                                                  | MediaConnect supports connections to NDI outputs through the<br>NDI discovery service only. Direct mDNS discovery or<br>manual connection to NDI outputs isn't supported.                                                                                                                                                                                                                                                                                                                                                                  |
| Cross-Region support                                                                                                                                                                                                                                                                                                                                                                              | NDI outputs are VPC-bound and can't span across<br>different AWS Regions. Each flow can only transmit NDI<br>traffic to the target VPC subnet that's in the same<br>AWS Region as your flow.<br>For NDI outputs across multiple AWS Regions, we<br>recommend using separate flows with dedicated NDI<br>ecosystems in each Region/VPC.<br>Alternatively, if you need to send NDI traffic to<br>different AWS Regions, you can set up a downstream<br>solution that uses networking services to route the NDI<br>traffic where you need it. |

### Supported

decoding parameters

The following table outlines the supported decoding parameters for NDI
outputs in MediaConnect.

For video decoder parameters: the supported bit depth/codecs for AVC
should be the same as HEVC.

| Decoding parameter                       | Description                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Video codec and chroma sampling profiles | • AVC (H.264): 8-bit 4:2:0, 8-bit 4:2:2, 10-bit<br>4:2:0, 10-bit 4:2:2<br>• HEVC (H.265): 8-bit 4:2:0, 8-bit 4:2:2, 10-bit<br>4:2:0, 10-bit 4:2:2<br>• MPEG-2: 8-bit 4:2:0, 8-bit 4:2:2                                                                                                                                                                                        |
| Audio codec support                      | • MPEG-1 Layer 2<br>• MPEG-2 Part 3<br>• MP3<br>• AAC (HE, LC)<br>• AC3<br>• SMPTE 302M<br>• Multiple audio channels supported (up to the<br>NDI limit of 16 audio channels).<br>NoteIf the source contains multiple audio PIDs, MediaConnect<br>combines all the audio streams. However, this is<br>only possible if the sample rates are the same<br>across all of the PIDs. |
| Supported resolutions                    | Supports resolutions from 480p up to 1080p                                                                                                                                                                                                                                                                                                                                     |
| Scan type                                | Supports both interlaced and progressive<br>formats                                                                                                                                                                                                                                                                                                                            |
| Frame rates                              | Supports the following frame rates : 23.98, 24, 25,<br>29.97, 30, 50, 59.94, 60 fps                                                                                                                                                                                                                                                                                            |

## Next steps

To get started with NDI outputs, first [create a
flow](flows-create.md "flows-create.md") with NDI enabled, then [add an
NDI output](outputs-add-ndi.md "outputs-add-ndi.md") to your flow.

## Additional

resources

- [Flow sizes and
  capabilities](flow-sizes-capabilities.md "flow-sizes-capabilities.md")
- [Best practices](best-practices.md "best-practices.md")
