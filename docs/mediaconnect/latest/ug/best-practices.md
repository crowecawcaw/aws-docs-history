# Best practices for MediaConnect

For the best performance and availability, follow best practices when you configure your AWS Elemental MediaConnect flows.

## Performance

###### Transport stream flows

The following best practices describe how to optimize the performance of transport
stream flows:

- Ensure you have set up your transport stream flows with an aggregate output
  bandwidth of up to 400 Mb/s. MediaConnect is designed to work with an aggregate
  output bandwidth of 400 Mb/s.

_aggregate output bandwidth_ = (bitrate of
the source) x (number of outputs)

For example, if your flow has a source with a bitrate of 80 Mb/s and 5
outputs, the aggregate output bandwidth is 400 Mb/s. Likewise, a flow that has a
source with a bitrate of 20 Mb/s and sends content to 20 outputs also has an
aggregate output bandwidth of 400 Mb/s.

###### Note

Because you can specify two destinations for a single ST 2110 JPEG XS
output, those outputs should be counted twice in this calculation.

- You can set up transport stream flows with bitrates up to 120 megabits per
  second (Mb/s) with mezzanine-quality live video.

###### Transport stream flows with NDI® outputs

MediaConnect doesn’t impose a hard limit on the number of NDI outputs you can
configure for each transport stream flow. However, as you scale your NDI outputs,
keep in mind that each additional NDI output receiver connected to your flow
increases the CPU and memory usage on the MediaConnect service. This is because
MediaConnect is acting as the NDI sender, and needs to encode and transmit the
video and audio streams to all connected receivers.

The following best practices describe how to optimize the performance of NDI
flows:

- Monitor the performance of your MediaConnect flow as you scale NDI outputs.
  In particular, watch for signs of over-subscription, such as:

      + Dropped frames or stuttering video on your NDI receivers
      + Dropped NDI connections

  If you notice these issues, consider reducing the number of outputs or
  investigating ways to optimize your workflow.

- Calculate the aggregate bandwidth of your NDI outputs and ensure it fits
  within the total throughput capacity of your MediaConnect flow size. The large
  flow size supports up to 2.5 Gbps of aggregate throughput.
- Use descriptive naming conventions for your NDI outputs to make it easier for
  production systems to quickly discover and connect to the correct
  sources.
- Consider segmenting your NDI outputs across multiple MediaConnect flows,
  rather than concentrating all outputs in a single flow. This can help distribute
  the resource load. However, keep in mind that using multiple NDI flow outputs
  will generate multiple NDI sources, each with their own unique machine name and
  program name. This will need to be accounted for in your overall
  workflow.
- Test your full NDI workflow, including connecting multiple receivers, to
  understand the performance characteristics and limits for your specific use
  case.
- Limit your NDI configuration setup to a single interface adapter per VPC. Each
  VPC interface has its own private IP address. When you use multiple VPC
  interfaces, this can confuse the NDI discovery server and lead to unexpected
  routing behavior.

###### CDI flows

The following best practices describe how to optimize the performance of CDI
flows:

- You can use up to 10 outputs for CDI flows. In addition, 4Kp60 CDI flows
  support 10 ST 2110 JPEG XS outputs, but only 4 CDI outputs.

###### Gateways

The following best practices describe how to optimize the performance of
Gateways:

- The API can be used to start multiple bridges at one time. If you are starting
  multiple bridges using the API, we recommend starting no more than 10 at one
  time. If you need to start more than 10 bridges, use multiple requests.

###### Flows with managed outputs

The following best practices describe how to optimize the performance of flows
with managed output types:

- You can use managed outputs to send content exclusively between MediaConnect
  flows and MediaLive channels. For instructions on creating these output types, see
  [Setting up for a MediaConnect input](../../../medialive/latest/ug/input-create-push-mediaconnect.md "../../../medialive/latest/ug/input-create-push-mediaconnect.md") in the
  MediaLive User Guide.
- For flows with managed output types, we recommend an aggregate bitrate
  limitation of 160 Mbps. For example, if a flow has a source bitrate of 4.5 Mbps,
  the total number of managed outputs shouldn't exceed 35.
- For flows with both managed outputs and transport stream outputs, apply the
  same 160 Mbps aggregate limitation.

## Availability

- To minimize packet loss, use Forward Error Correction (FEC) or automatic repeat request (ARQ) based protocols such as the Zixi or RTP-FEC
  protocol. These [protocols](protocols.md "protocols.md") are designed to minimize packet loss between the source and destination
  devices.
- Because packet loss is present on any network, even in fully managed networks such as the AWS Cloud, you should create and manage
  redundant connections throughout your workflows. In MediaConnect, there are multiple ways to add redundancy to your workflow:
  - Create flows in at least two different Availability Zones.
  - [Add a second source](source-adding.md "source-adding.md") to each flow. If there are errors in the stream, MediaConnect can use
    packets from a redundant source or switch to the redundant source completely.

- We recommend that your organization create a VPC specifically for all AWS Media Services. A single VPC will help to ensure the availability of IP addresses, help in setting up appropriate rules in the security groups, and help to ensure that a network administrator doesn't accidentally delete elastic network interfaces.

## Reliability

- Set up Amazon CloudWatch metrics and alarms to track the health of your source. For information about which metrics to monitor, see [Monitoring and tagging](monitor.md "monitor.md").

## Security

- The CIDR block on the flow source should be as precise as possible. Include only the IP addresses that you want to contribute content to
  your flow. If the CIDR block is too wide, it allows for the possibility of outside parties sending content to your flow.
- When you create a new SRT password to encrypt an SRT output, you must create
  that password in AWS Secrets Manager. AWS Secrets Manager does not enforce a specific password
  policy. However, we recommend the following password policy:
  - Minimum password length of 10 characters and a maximum length of 80
    characters
  - Minimum of three of the following mix of character types: uppercase,
    lowercase, numbers, and `! @ # $ % ^ & * ( ) _ + - = [ ] {
} | '` symbols
  - Not be identical to your AWS account name or email address
