

# AVEVA Unified Engineering Deployment on AWS
<a name="aveva-unified-engineering"></a>

Publication date: **April 5, 2022 ([Diagram history](#aveva-diagram-history))**

With this architecture, you can deploy AVEVA Unified Engineering, a suite of Windows desktop authoring applications for process simulation and 1D, 2D, 3D engineering and design. You can provide engineers with secure virtual desktop access through [Amazon WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/). This architecture uses Amazon WorkSpaces, [AWS Directory Service](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/), [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) (Amazon EC2), [FSx for Windows File Server](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/), and [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/).

## AVEVA Unified Engineering architecture diagram
<a name="aveva-diagram"></a>

![Reference architecture diagram for deploying AVEVA Unified Engineering on AWS with Amazon WorkSpaces and multi-AZ architecture.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/aveva-unified-engineering/images/aveva-unified-engineering-deployment-ra.png)


The following steps describe the architecture:

1. AWS Directory Service provides managed domain access control for engineers to access AVEVA Unified Engineering through Amazon WorkSpaces.

1. Users access virtual desktops through Amazon WorkSpaces.

1. Operations administrators log on to the Admin server through a bastion host in the public subnet.

1. GPU-powered and CPU-based WorkSpaces provide access to each Unified Engineering application. Deploy WorkSpaces in two Availability Zones for high availability.

1. The integration server hosts AVEVA middleware. Load balance Amazon EC2 instances with [Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/) for resilient architecture.

1. AVEVA stores data in Microsoft SQL Server on Amazon EC2 instances. Deploy SQL servers in two Availability Zones as primary and secondary.

1. FSx for Windows File Server managed file system replicates between two Availability Zones for AVEVA Dabacon databases and project files through SMB.

1. A bastion host on Amazon EC2 allows administrators to access servers in the private subnet for Active Directory admin, SQL admin, and service configuration.

1. AWS Backup backs up AIS, admin, and SQL Server Amazon EC2 instances along with [Amazon Elastic Block Store](https://docs.aws.amazon.com/ebs/latest/userguide/) (Amazon EBS) and Amazon FSx.

## Further reading
<a name="aveva-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [Manufacturing on AWS](../manufacturing-on-aws/manufacturing-on-aws.html)

## Diagram history
<a name="aveva-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#aveva-diagram-history) | Reference architecture diagram first published. | April 5, 2022 | 

**RSS subscription**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser that you are using.