**End of support notice**: On February
20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will
no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more
information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/ "https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/"). **Note:** This does not impact the
availability of the [Amazon Chime SDK
service](https://aws.amazon.com/chime/chime-sdk/ "https://aws.amazon.com/chime/chime-sdk/").

# Network configuration and bandwidth requirements

Amazon Chime requires the destinations and ports described in this topic to support
various services. If inbound or outbound traffic is blocked, this blockage might affect the
ability to use various services, including audio, video, screen sharing, or chat.

Amazon Chime uses Amazon Elastic Compute Cloud (Amazon EC2) and other AWS services on port TCP/443. If your firewall
blocks port TCP/443, you must put `*.amazonaws.com` on an allow list, or put
[AWS IP address
ranges](../../../general/latest/gr/aws-ip-ranges.md "../../../general/latest/gr/aws-ip-ranges.md") in the _AWS General Reference_ for the following
services:

- Amazon EC2
- Amazon CloudFront
- Amazon Route 53
  Expand the following sections for more information about destinations, ports, and bandwidth.

The following destinations and ports are required to run Amazon Chime.

| Destination      | Ports   |
| ---------------- | ------- |
| chime.aws        | TCP/443 |
| \*.chime.aws     | TCP/443 |
| \*.amazonaws.com | TCP/443 |
| 99.77.128.0/18   | TCP/443 |

Amazon Chime uses the following destination and port for meetings and Amazon Chime Business Calling.

| Destination    | Port     |
| -------------- | -------- |
| 99.77.128.0/18 | UDP/3478 |

Amazon Chime uses the following destinations and ports for H.323 in-room video systems.

| Destination                                                                              | Ports                          |
| ---------------------------------------------------------------------------------------- | ------------------------------ |
| 13.248.147.139                                                                           | TCP/1720                       |
| 76.223.18.152                                                                            | TCP/1720                       |
| 99.77.128.0/18<br>34.212.95.128/25<br>34.223.21.0/25<br>52.55.62.128/25<br>52.55.63.0/25 | TCP/5100:6200<br>UDP/5100:6200 |

The following destinations and ports are recommended when running Amazon Chime for SIP in-room video systems in your environment.

| AWS Region                | Destination                                                                              | Ports           |
| ------------------------- | ---------------------------------------------------------------------------------------- | --------------- |
| Global (nearest Region)   | 99.77.128.0/18<br>34.212.95.128/25<br>34.223.21.0/25<br>52.55.62.128/25<br>52.55.63.0/25 | UDP/10000:60000 |
| Global                    | meet.chime.in<br>13.248.147.139<br>76.223.18.152                                         | TCP/5061        |
| US East (N. Virginia)     | meet.ue1.chime.in                                                                        | TCP/5061        |
| US West (Oregon)          | meet.uw2.chime.in                                                                        | TCP/5061        |
| Asia Pacific (Singapore)  | meet.as1.chime.in                                                                        | TCP/5061        |
| Asia Pacific (Sydney)     | meet.as2.chime.in                                                                        | TCP/5061        |
| Asia Pacific (Tokyo)      | meet.an1.chime.in                                                                        | TCP/5061        |
| Europe (Ireland)          | meet.ew1.chime.in                                                                        | TCP/5061        |
| South America (São Paulo) | meet.se1.chime.in                                                                        | TCP/5061        |

Amazon Chime has the following bandwidth requirements for audio, video, and screen sharing:

- Audio
  - 1:1 call: 54 kbps up and down
  - Large call: no more than 32 kbps extra down for 50 callers

- Video
  - 1:1 call: 650 kbps up and down
  - HD mode: 1400 kbps up and down
  - 3–4 people: 450 kbps up and (N-1)\*400 kbps down
  - 5–16 people: 184 kbps up and (N-1)\*134 kbps down
  - Up and down bandwidth adapts lower based on network conditions

- Screen sharing
  - 1.2 mbps up (when presenting) and down (when viewing) for high quality.
    This adapts as low as 320 kbps based on network conditions.
  - Remote control: 800 kbps fixed
