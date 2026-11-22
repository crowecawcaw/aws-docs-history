

# Architecture for Unified Communications

Publication date: **November 1, 2021 ([Diagram history](diagram-history.md))**

This reference architecture diagram shows how to deploy the Avaya Aura Unified Communications platform on AWS.

## Architecture for Unified Communications diagram
<a name="architecture-unified-communications-diagram1"></a>

![Reference architecture diagram showing the Avaya Aura Unified Communications platform deployed on AWS with Amazon Elastic Compute Cloud, Direct Connect, and Amazon WorkSpaces.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/contact-center/images/architecture-unified-communications.png)


1. Users on a corporate network register UC applications and devices by using [Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/) or [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/).

1. Remote workers connect UC applications and devices through the public internet.

1. UC devices and soft clients pull configuration from Avaya Aura Device Services (AADS) that runs on [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) (Amazon EC2).

1. Sessions are established with one of the Session Border Controllers (SBCs) as entry points managed by the Element Management System (EMS).

1. User authentication and session management occur at the Session Managers, controlled by the System Manager.

1. Communication Manager provides telephony features with Media Servers for digital signal processing (DSP) resources.

1. [Amazon WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/) provides a simplified bastion host for management activities.

1. [Directory Service](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/) provides a unified directory for user creation.

1. Avaya Aura roles are distributed in two Availability Zones for high availability (HA) purposes.

## Further reading
<a name="architecture-unified-communications-further-reading"></a>

For additional information, refer to
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [Amazon Connect Customer product page](https://aws.amazon.com/connect/)
+ [Direct Connect product page](https://aws.amazon.com/directconnect/)