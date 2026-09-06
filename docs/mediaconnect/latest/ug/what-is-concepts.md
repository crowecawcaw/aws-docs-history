

# MediaConnect concepts and terminology
<a name="what-is-concepts"></a>

To help you get started with AWS Elemental MediaConnect, and to understand how it works, refer to the following key concepts and terminology.

Allowlist CIDR  
A range of Classless Inter-Domain Routing (CIDR) IP addresses permitted to contribute content to your MediaConnect flow or router input. In the MediaConnect API, this value is specified using the `WhitelistCidr` parameter.

Contribution encoder  
An encoder that receives a live video feed and encodes the stream into a single, high-quality mezzanine stream for transportation or further processing into an adaptive bitrate (ABR) stream.

Destination  
A physical or virtual connection point in your downstream environment that receives content from MediaConnect. A destination might be an affiliate, a cloud encoder, an on-premises decoder, another MediaConnect flow, a MediaConnect router input, or a MediaLive input. In flows, you define destinations by adding outputs. In the router, you create router outputs that connect to your destination endpoints.

Entitlement  
A permission that allows an AWS account (the subscriber) to access the content in a specific MediaConnect flow. The content originator grants an entitlement to the subscriber account, which can then create a flow using the originator's content as the source.

Flow  
A connection between one or more video sources and one or more outputs. For each flow, you specify the protocol to use, encryption information, and details about the source. The service replicates and distributes the video to every output that you specify, whether inside or outside the AWS Cloud.

Input  
A connection point in MediaConnect that receives content from a source. In flows, the flow's source configuration acts as the input. In the router, a router input is a dedicated resource that receives content and can be routed to multiple outputs simultaneously.

Media stream  
A single track of video, audio, or ancillary data. Media streams are used with CDI and ST 2110 JPEG XS flows, where content is demuxed into separate tracks. Each source or output can consist of one or many media streams.

Mezzanine stream  
A lightly compressed video stream that takes up less space than a full resolution uncompressed stream. The quality is high enough to use as a source for creating final encodes delivered to consumer devices.

NDI (Network Device Interface)  
A standard developed by NewTek (now Vizrt) that enables video-compatible products to communicate, deliver, and receive high-definition video over a standard Ethernet network. NDI allows multiple video systems to share video across a network in real time with low latency. MediaConnect supports NDI as both a source and output type for flows, enabling integration with NDI-based production environments.

Network interface  
The network configuration that determines how MediaConnect resources connect to other resources. In flows, a VPC interface provides private connectivity between a flow and your Amazon VPC. Flows use public networking by default. In the router, a network interface can be either public (for connecting over the internet) or VPC (for connecting to resources within your VPC), and is associated with one or more router I/Os.

Offering  
A discount that MediaConnect offers in exchange for a commitment to use a certain amount of outbound bandwidth each month. When you purchase an offering, it becomes a reservation.

Output  
A connection point in MediaConnect that sends content to a destination. In flows, an output defines where and how the service delivers video. In the router, a router output is a dedicated resource that sends content and can receive from only one input at a time.

Protocol  
A set of rules used for video and audio transmission. MediaConnect provides protocol options (such as SRT, RTP, RTP-FEC, RIST, Zixi, and NDI) that implement a quality of service (QoS) layer for mezzanine-quality live video. Supported protocols differ between flows and the router.

Reservation  
A commitment to use a specific amount of outbound bandwidth each month over a specified duration. In return, you pay a discounted hourly rate. Reservations are created by purchasing an offering.

Route  
The complete end-to-end path from an input to an output within the router. Routes are defined by input-to-output assignments.

Router  
A MediaConnect capability that provides dynamic, software-defined signal routing for live video in the cloud. A router can accept multiple inputs simultaneously and route any input to any output on demand. Routers are designed for use cases such as master control, live cloud production, playout, and contribution workflows.

Source  
A physical or virtual connection point in your upstream environment that transmits content into MediaConnect. A source might be an on-premises contribution encoder, an NDI device, another MediaConnect flow, or a MediaLive channel output. In flows, you configure sources when you create or update a flow. A standard source comes from outside of MediaConnect, while an entitled source comes from a flow owned by another AWS account that has granted an entitlement to your account. In the router, you connect sources to router inputs.