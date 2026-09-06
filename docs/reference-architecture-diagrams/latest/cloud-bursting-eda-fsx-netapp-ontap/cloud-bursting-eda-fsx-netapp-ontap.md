

# Cloud Bursting EDA with Amazon FSx for NetApp ONTAP
<a name="cloud-bursting-eda-fsx-netapp-ontap"></a>

Publication date: **November 19, 2021 ([Diagram history](#burst-eda-history))**

With this architecture, you can burst Electronic Design Automation (EDA) jobs from your on-premises data center to AWS and quickly access the results. The solution uses [Amazon FSx for NetApp ONTAP](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/) with FlexCache volumes for bidirectional caching between on-premises and cloud storage.

## Cloud bursting EDA with Amazon FSx for NetApp ONTAP diagram
<a name="burst-eda-diagram"></a>

![Reference architecture diagram showing how to enable EDA cloud bursting by using Amazon FSx for NetApp ONTAP, Amazon EC2, and AWS Direct Connect.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/cloud-bursting-eda-fsx-netapp-ontap/images/cloud-bursting-eda-fsx-netapp-ontap.png)


The following steps describe the data flow and caching configuration for this architecture:

1. Establish fast, secure networking between your on-premises data center and AWS. Use AWS Direct Connect for production, or AWS Site-to-Site VPN for initial testing or proof of concept.

1. Deploy Amazon FSx for NetApp ONTAP in AWS and configure cluster peering with your on-premises NetApp system.

1. Create a FlexCache volume in Amazon FSx for NetApp ONTAP and pair it with the on-premises origin volume. Your [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) instances can then access cached data from the on-premises file system through Network File System (NFS).

1. Run EDA jobs on Amazon EC2 instances by using the local FlexCache volume. Required file blocks load on demand and cache in AWS. Write output to a local output origin volume in the cloud.

1. Create a FlexCache volume within your on-premises NetApp system and pair it with the Amazon FSx for NetApp ONTAP origin volume. You can then access the output data from your on-premises data center.

1. Only data read by users is fetched from the origin volume in AWS. This minimizes bandwidth use.

1. Multiple engineers accessing the same files in the on-premises FlexCache volume, or users accessing files multiple times, receive the file from the local cache.

1. Use a multi-Availability Zone configuration for high availability (HA) in Amazon FSx for NetApp ONTAP.

## Further reading
<a name="burst-eda-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="burst-eda-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#burst-eda-history) | Reference architecture diagram first published. | November 19, 2021 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.