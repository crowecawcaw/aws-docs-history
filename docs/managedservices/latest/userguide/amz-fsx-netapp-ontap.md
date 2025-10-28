# Use AMS SSP to provision Amazon FSx for NetApp ONTAP in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access Amazon FSx for NetApp ONTAP capabilities directly in your AMS managed account. Amazon FSx for NetApp ONTAP is a fully managed service that provides highly reliable, scalable, performant, and feature-rich file storage
built on NetApp's popular ONTAP file system. It provides the familiar features, performance, capabilities, and APIs of NetApp file systems
with the agility, scalability, and simplicity of a fully managed AWS service.

Amazon FSx for NetApp ONTAP provides feature-rich, fast, and flexible shared file storage that’s broadly accessible from Linux, Windows, and
macOS compute instances running in AWS or on premises. FSx for ONTAP offers high-performance SSD storage with sub-millisecond latencies, and
makes it quick and easy to manage your data by enabling you to snapshot, clone, and replicate your files with the click of a button. It also
automatically tiers your data to lower-cost, elastic storage, eliminating the need to provision or manage capacity and allowing you to achieve
SSD levels of performance for your workload while only paying for SSD storage for a small fraction of your data. It provides highly available
and durable storage with fully managed backups and support for cross-region disaster recovery, and supports popular data security and anti-virus
applications that make it even easier to protect and secure your data. For customers who use NetApp ONTAP on-premises, FSx for ONTAP is an ideal
solution to migrate, back up, or burst your file-based applications from on-premises to AWS without the need to change your application code or
how you manage your data.

As a fully managed service, Amazon FSx for NetApp ONTAP makes it simple to launch and scale reliable, performant, and secure shared file storage
in the cloud. With Amazon FSx for NetApp ONTAP, you no longer have to worry about setting up and provisioning file servers and storage volumes,
replicating data, installing and patching file server software, detecting and addressing hardware failures, managing failover and failback, and
manually performing backups. It also provides rich integration with other AWS services, such as AWS Identity and Access Management,
Amazon WorkSpaces, AWS Key Management Service, and AWS CloudTrail.

Amazon FSx provides you with two file systems to choose from: Amazon FSx for Windows File Server for Windows-based
applications and Amazon FSx for Lustre for compute-intensive workloads.
To learn more, see [Amazon FSx](https://aws.amazon.com/fsx/ "https://aws.amazon.com/fsx/").

## Amazon FSx for NetApp ONTAP in AWS Managed Services FAQ

**Q: How do I request access to Amazon FSx for NetApp ONTAP in my AMS account?**

Request access to Amazon FSx for NetApp ONTAP by submitting an RFC with the Management | AWS service | Self-provisioned service | Add (ct-1w8z66n899dct) change type.
This RFC provisions the following IAM role to your account: `customer_fsx_ontap_admin_role`. After it's provisioned in your
account, you must onboard the role in your federation solution.

**Q: What are the restrictions to using Amazon FSx for NetApp ONTAP in my AMS account?**

Replacing the security group on the Amazon FSx for NetApp ONTAP elastic network interfaces (ENIs) requires you to submit Management | Other | Other | Update RFCs
since security groups are a critical perimeter for the AMS environment. That is the only restriction.

**Q: What are the prerequisites or dependencies to using Amazon FSx for NetApp ONTAP in my AMS account?**

There are no prerequisites. However, you must have [Use AMS SSP to provision Amazon FSx in your AMS account](amz-fsx.md "amz-fsx.md") installed.
