

# Deploying 5G Core on AWS
<a name="deploying-5g-core"></a>

Publication date: **December 28, 2020 ([Diagram history](#5gcore-history))**

With this architecture, you can distribute your 5G Core between on-premises data centers and AWS Regions. The solution uses [AWS Outposts](https://docs.aws.amazon.com/outposts/latest/userguide/) for the User Plane Function (UPF) and [Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/eks/latest/userguide/) for containerized network functions.

## Deploying 5G Core on AWS diagram
<a name="5gcore-diagram"></a>

![Reference architecture diagram showing how to distribute 5G Core between on-premises and AWS Regions by using AWS Outposts, Amazon EKS, and AWS Direct Connect.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/deploying-5g-core/images/deploying-5g-core.png)


The following steps describe the network topology and data flow for this architecture:

1. Ingest subscriber traffic from the Radio Access Network (RAN) into AWS Outposts running the 5G UPF through the Outposts Local Gateway (LGW).

1. Run UPF instances as containers on Amazon EKS with access to multiple network interfaces through AWS multi-homing support and Multus.

1. Configure two subnets on AWS Outposts (for ingress and egress) with routing tables that contain paths to service endpoints and [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/) for other VPCs.

1. Achieve internet access for mobile subscribers through the local gateway as a default route in the subnet route tables.

1. Separate Service Link traffic from local traffic through virtual LANs (VLANs). This provides connectivity both locally and to AWS Regions.

1. Use [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/) to provide a high-throughput connection to a Amazon VPC on an AWS Region through a public virtual interface.

1. Use the service endpoint to provide direct access to AWS Regional services such as [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) without traversing the internet.

1. Use AWS Transit Gateway to provide connectivity to other VPCs that perform 5G management and control services.

1. Run orchestration, operational, and business support systems on AWS Regions with direct connectivity to on-premises data centers.

## Further reading
<a name="5gcore-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="5gcore-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#5gcore-history) | Reference architecture diagram first published. | December 28, 2020 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.