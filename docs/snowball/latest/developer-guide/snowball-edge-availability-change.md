Effective November 7, 2025, AWS Snowball Edge will only be available to existing customers. If you would like to use AWS Snowball Edge,
sign up prior to that date. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# AWS Snowball Edge availability change

Effective November 7, 2025, AWS Snowball Edge devices will only be available to existing customers. New customers should explore [DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for secure physical transfers, or AWS Partner solutions. For edge computing workloads, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

With this change, after November 7, 2025, AWS will no longer be offering any AWS Snow Family devices for new customers to order. This change will not impact customers currently using AWS Snowball Edge to meet their edge compute and data migration needs. AWS continues to invest in security and availability improvements for AWS Snowball Edge devices. However, we recommend evaluating the alternatives below to better meet your needs.

## AWS Snowball Edge storage optimized alternatives

AWS has provided details on your service transition options for both online and offline data transfer scenarios below. AWS recommends that your migration goals, network bandwidth throughput and reliability, and size of data to be imported, should guide you on which service to use.

### Online data transfers

[AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") is an online data movement service that simplifies and accelerates data migrations to AWS and helps you move data quickly and securely between on-premises storage, edge locations, other cloud providers, and AWS storage. DataSync can copy data to and from Network File System (NFS) shares, Server Message Block (SMB) shares, Hadoop Distributed File Systems (HDFS), self-managed object storage, and AWS storage services. With DataSync, you pay only for your usage of the service. No software licenses, contracts, or maintenance fees are required. This provides a lower total cost of ownership (TCO) compared to manually building, operating, and optimizing your own high-performance scripted transfers, as well as lower total cost than buying and running commercial transfer tools.

DataSync employs an transfer protocol designed by AWS that's decooupled from the storage protocol to accelerate data movement. The protocol performs optimizations on how, when, and what data is sent over the network. Network optimizations performed by DataSync include incremental transfers, in-line compression, and sparse file detection, as well as in-line data validation and encryption. Connections between the local DataSync agent and the in-cloud service components are multi-threaded, maximizing performance over your Wide Area Network (WAN). A single DataSync task is capable fully utilizing 10 Gbps over a network link between your on-premises environment and AWS.

The DataSync agent connects to your existing storage systems using the industry-standard NFS and SMB protocols, to your Hadoop cluster as an HDFS client, to your self-managed object storage using the Amazon S3 application programming interface (API). The agent transfers data rapidly and writes it into your designated Amazon S3 bucket, Amazon EFS file system, or Amazon FSx file system. File permissions and metadata are preserved when copying objects and or data between Amazon S3, Amazon EFS, Amazon FSx for Windows File Server, FSx for Lustre, FSx for OpenZFS, or FSx for ONTAP.

Consider your available network bandwidth, its reliability, and your data size to determine if DataSync meets your migration goals. To estimate your data migration timelines, more details are available [here](../../../datasync/latest/userguide/datasync-large-migration-timelines.md "../../../datasync/latest/userguide/datasync-large-migration-timelines.md"). To overcome network bandwidth limitations, consider using DataSync with an AWS Direct Connect hosted connection. You can procure this connection from an AWS Direct Connect Delivery Partner for the duration of the data transfer project. More information is available [here](../../../directconnect/latest/UserGuide/hosted_connection.md "../../../directconnect/latest/UserGuide/hosted_connection.md"). AWS Direct Connect can significantly improve the reliability and speed of large data migrations when used with DataSync.

For more details on transferring your data using DataSync, see the [DataSync User Guide](../../../datasync/latest/userguide/transferring-data-datasync.md "../../../datasync/latest/userguide/transferring-data-datasync.md").

### Offline data transfers

[AWS Data Transfer Terminals](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") is a secure, physical location for you to bring your data storage devices for fast data transfer to the AWS cloud. Simply schedule a reservation at your nearest Data Transfer Terminal from the AWS console, arrive at the facility at your scheduled time, and upload your data to your AWS cloud services with your own devices, in a private setting. AWS Data Transfer Terminal is intended for those who create or collect large amounts of data on physical, portable storage devices and need to transfer that data into the AWS cloud to enable cloud-based workloads. AWS Data Transfer Terminal offers a high-speed solution for uploading large volumes of data to the AWS cloud. With rapid upload speeds, you can transfer massive amounts of data in a fraction of the time compared to traditional methods. This accelerated data ingestion process significantly reduces upload times from hours or days to mere minutes, enabling faster time-to-market for your data-driven projects and applications.

[Read the blog post](https://aws.amazon.com/blogs/aws/new-physical-aws-data-transfer-terminals-let-you-upload-to-the-cloud-faster/ "https://aws.amazon.com/blogs/aws/new-physical-aws-data-transfer-terminals-let-you-upload-to-the-cloud-faster/") for guidance for typical data transfer scenarios and outcomes from AWS Data Transfer Terminal. For more details on getting started with AWS Data Transfer Terminal, please read the [User Guide](../../../datatransferterminal/latest/userguide/what-is-dtt.md "../../../datatransferterminal/latest/userguide/what-is-dtt.md").

#### Partner solutions for offline data transfers

AWS Partners offer offline data transfer services through the AWS Marketplace, such as Seagate and Tsecond. Learn more about these offline data transfer services by searching the [AWS Marketplace](https://aws.amazon.com/marketplace "https://aws.amazon.com/marketplace").

## AWS Snowball Edge Compute Optimized Alternatives

For customers using or considering AWS Snowball Edge Compute Optimized for hybrid or edge computing workloads, consider [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/") as an alternative. Outposts is a family of fully managed solutions delivering AWS infrastructure and services to virtually any on-premises or edge location for a truly consistent hybrid experience. Outposts solutions allow you to extend and run native AWS services on premises, and is available in a variety of form factors, from 2U Outposts servers to 42U Outposts racks, and multiple rack deployments. With AWS Outposts, you can run some AWS services locally and connect to a broad range of services available in the local AWS Region. Run applications and workloads on premises using familiar AWS services, tools, and APIs. Outposts supports workloads and devices requiring low latency access to on-premises systems, local data processing, data residency, and application migration with local system interdependencies.

- [AWS Outposts racks](https://aws.amazon.com/outposts/rack/ "https://aws.amazon.com/outposts/rack/"): The AWS
  Outposts racks are industry standard 42U form factor. They provide the same AWS infrastructure,
  services, APIs, and tools to virtually any data center or co-location space. Outposts racks
  provide AWS compute, storage, database, and other services locally, while still allowing you to
  access the full range of AWS services available in the Region for a truly consistent hybrid
  experience. Scale from a single 42U rack to multiple rack deployments of up to 96 racks to
  create pools of compute and storage capacity.
- [AWS Outposts servers](https://aws.amazon.com/outposts/servers/ "https://aws.amazon.com/outposts/servers/"): The AWS Outposts servers come in a 2U form factor. They provide the same AWS infrastructure, services, APIs, and tools to on-premises and edge locations that have limited space or smaller capacity requirements, such as retail stores, branch offices, healthcare provider locations, or factory floors. Outposts servers provide local compute and networking services.

Both form factors are fully managed by AWS and can operate without AWS connectivity for up to
7 days in Denied, Disrupted, Intermittent, and Limited (DDIL) environments. For organizations with
edge computing workloads, Outposts offers a cloud-native hybrid architecture, providing the full,
native Amazon EC2 API experience that extends your Amazon Virtual Private Cloud (VPC) into your
on-premises environment. This enables operational consistency, allowing you to manage your cloud
and on-premises workloads with the same tools, APIs, and familiar AWS services. To learn more
about Outposts, visit our technical documentation for [Outposts
servers](../../../outposts/latest/server-userguide/what-is-outposts.md "../../../outposts/latest/server-userguide/what-is-outposts.md"), [first-generation Outposts racks](../../../outposts/latest/userguide/what-is-outposts.md "../../../outposts/latest/userguide/what-is-outposts.md"), and [second-generation Outposts racks](../../../outposts/latest/network-userguide/what-is-outposts.md "../../../outposts/latest/network-userguide/what-is-outposts.md") .
