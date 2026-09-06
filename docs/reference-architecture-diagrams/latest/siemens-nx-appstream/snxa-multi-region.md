

# Siemens NX multi-Region deployment
<a name="snxa-multi-region"></a>

With this architecture, you can minimize latency by cross-replicating storage across Regions. This deployment uses [Amazon WorkSpaces Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/), [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) (Amazon EC2), and [Amazon FSx](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/).

![Reference architecture for Siemens NX multi-Region deployment on Amazon WorkSpaces Applications.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/siemens-nx-appstream/images/siemens-nx-architecture-diagram-ra-3.png)


The following steps describe the architecture:

1. Two pairs of Microsoft Active Directory instances on Amazon EC2 run in each Region. Each instance runs in a different Availability Zone. Active Directory instances fully replicate across Availability Zones and Regions through Active Directory sites.

1. Two Amazon FSx single-Availability-Zone file systems are created in each Region. Full bidirectional Amazon FSx data replication uses Microsoft Distributed File System Replication.

1. Amazon WorkSpaces Applications image builders are shared across multiple Regions. An administrator tunes each image to access its closest Microsoft Active Directory and Amazon FSx instances.