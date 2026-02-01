# Protocols in AWS Elemental MediaConnect

AWS Elemental MediaConnect supports different protocols for incoming (source) and outgoing (output)
live video streams depending on the type of flow you use.

## Transport stream flows

For transport stream flows, which transport compressed content that is muxed (audio,
video, and ancillary data are combined) into a single stream, you can use the following
protocols:

- **Network Device Interface
  (NDI\*\***®\***\*)**
  uses SpeedHQ compression to deliver high-quality, low-latency video transmission
  over IP networks. This protocol is optimized for professional video workflows
  and supports up to 1080p60 video quality.
- **Reliable Internet Stream Transport (RIST) (Simple
  profile only)** is a highly available, low-latency protocol that is
  suitable for long-distance applications. MediaConnect doesn't support
  encryption for sources or outputs that use the RIST protocol.
- **Real-Time Transport Protocol (RTP)** has wide
  applicability and takes less bandwidth than RTP-FEC. MediaConnect doesn't
  support encryption for sources or outputs that use the RTP protocol.
- **Real-Time Transport Protocol with Forward Error
  Correction (RTP-FEC)** has wide applicability and forward error
  correction (FEC) to self-heal any corruption and packet loss. Using this
  protocol takes more bandwidth than RTP without FEC. AWS Elemental MediaConnect doesn't
  support encryption for sources or outputs that use the RTP-FEC protocol.
- **Secure Reliable Transport (SRT)** is a highly
  available, low-latency protocol that is suitable for long-distance
  applications.
  - **SRT listener** is a pull-based
    implementation of the SRT protocol. You can use it as a source or an
    output. When configured as a source or an output, an SRT listener can
    accept connections from only one SRT caller at a time. Multiple
    connections to a flow configured with an SRT listener aren't
    supported.
  - **SRT caller** is a push-based
    implementation of the SRT protocol. You can use it as a source or an
    output. SRT caller must communicate with an SRT listener.

- **Zixi** is a highly available protocol suitable
  for most applications, especially use cases that involve longer distances. If
  your encoder is not capable of using Zixi, you can use the Zixi feeder/receiver
  software that was created specifically for use with MediaConnect. You can
  access this software on the [Zixi
  website](http://www.mediaconnect.zixi.com "http://www.mediaconnect.zixi.com"), where you will be asked to provide your information before
  you can download the software. If you set up multiple flows for distribution, we
  recommend that you use Zixi as the protocol to send content between flows.
  MediaConnect supports two Zixi protocol options:
  - **Zixi pull** uses the Zixi protocol to
    send content to a receiver or an integrated receiver decoder (IRD) that
    is behind a firewall. Additionally, you can use this option when you
    need network address translation (NAT) to route the traffic from
    MediaConnect to the receiver.
  - **Zixi push** uses the Zixi protocol to
    send content to a receiver that has a static, publicly addressable IP
    address. Use this option when the receiver is not behind a firewall or
    NAT-based router.
  - **Zixi push for AWS Elemental Link** uses the Zixi
    push protocol to connect an AWS Elemental Link UHD device with a MediaConnect flow.

## CDI flows

For CDI flows, which transport high-quality content that has been lightly compressed using
JPEG XS, you use the following protocols:

- **AWS Cloud Digital Interface (AWS CDI)** is a technology that allows you to transport high-quality uncompressed
  video inside the AWS Cloud, with high reliability and network latency as low as 8 milliseconds.
- **ST 2110 JPEG XS** is a low-latency protocol that
  can be used on streams with minimal compression.

## Protocol support for sources and outputs

The following table describes what protocols can be used for sources, outputs, or both.

| Transport stream protocols | Protocol | Can this be used as a Source? | Can this be used as an Output? |
| -------------------------- | -------- | ----------------------------- | ------------------------------ |
| NDI-SpeedHQ                | Yes      | Yes                           |
| RIST                       | Yes      | Yes                           |
| RTP                        | Yes      | Yes                           |
| RTP-FEC                    | Yes      | Yes                           |
| SRT listener               | Yes      | Yes                           |
| SRT caller                 | Yes      | Yes                           |
| Zixi pull                  | No       | Yes                           |
| Zixi push                  | Yes      | Yes                           |

| CDI protocols   | Protocol | Can this be used as a Source? | Can this be used as an Output? |
| --------------- | -------- | ----------------------------- | ------------------------------ |
| CDI             | Yes      | Yes                           |
| ST 2110 JPEG XS | Yes      | Yes                           |
