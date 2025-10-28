# Use AMS SSP to provision Amazon FSx for OpenZFS in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access Amazon FSx for OpenZFS capabilities directly in your AMS managed account. FSx for OpenZFS is a fully managed file storage service that makes it easy to move data residing in on-premises ZFS or other
Linux-based file servers to AWS without changing your application code or how you manage data. It offers highly reliable, scalable,
performant, and feature-rich file storage built on the open-source OpenZFS file system, providing the familiar features and capabilities
of OpenZFS file systems with the agility, scalability, and simplicity of a fully managed AWS service. For developers building cloud-native
applications, it offers simple, high-performance storage with rich capabilities for working with data.

FSx for OpenZFS file systems are broadly accessible from Linux, Windows, and macOS compute instances and containers using the industry-standard
NFS protocol (v3, v4.0, v4.1, v4.2). Powered by AWS Graviton processors and the latest AWS disk and networking technologies (including
AWS Scalable Reliable Datagram networking and the AWS Nitro system), FSx for OpenZFS delivers up to 1 million IOPS with latencies of hundreds of
microseconds. With complete support for OpenZFS features like instant point-in-time snapshots and data cloning, FSx for OpenZFS makes it easy for you to
replace your on-premises file servers with AWS storage that provides familiar file system capabilities and eliminates the need to perform lengthy
qualifications and change or re-architect existing applications or tools. And, by combining the power of OpenZFS data management capabilities with
the high performance and cost efficiency of the latest AWS technologies, FSx for OpenZFS enables you to build and run high-performance, data-intensive applications.

As a fully managed service, FSx for OpenZFS makes it easy to launch, run, and scale fully managed file systems on AWS that replace the file servers
you run on premises while helping to provide better agility and lower costs. With FSx for OpenZFS, you no longer have to worry about setting up and
provisioning file servers and storage volumes, replicating data, installing and patching file server software, detecting and addressing hardware failures,
and manually performing backups. It also provides rich integration with other AWS services, such as AWS Identity and Access Management (IAM),
AWS Key Management Service (AWS KMS), Amazon CloudWatch, and AWS CloudTrail.

Amazon FSx provides you with two file systems to choose from: Amazon FSx for Windows File Server for Windows-based
applications and Amazon FSx for Lustre for compute-intensive workloads.
To learn more, see [Amazon FSx](https://aws.amazon.com/fsx/ "https://aws.amazon.com/fsx/").

## Amazon FSx for OpenZFS in AWS Managed Services FAQ

**Q: How do I request access to use FSx for OpenZFS in my AMS account?**

Request access to Amazon FSx OpenZFS by submitting an RFC with the Management | AWS service | Self-provisioned service | Add (ct-1w8z66n899dct) change type.
This RFC provisions the following IAM role to your account: `customer_fsx_ontap_admin_role`. After it's provisioned in your
account, you must onboard the role in your federation solution.

**Q: What are the restrictions to using FSx for OpenZFS in my AMS account?**

Replacing the security group on the Amazon FSx elastic network interfaces (ENIs) requires you to submit Management | Other | Other | Update RFCs
since security groups are a critical perimeter for the AMS environment. That is the only restriction.

**Q: What are the prerequisites or dependencies to using FSx for OpenZFS in my AMS account?**

There are no prerequisites. However, you must have [Use AMS SSP to provision Amazon FSx in your AMS account](amz-fsx.md "amz-fsx.md") installed.
