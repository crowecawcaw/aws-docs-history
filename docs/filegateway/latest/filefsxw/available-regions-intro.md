Amazon FSx File Gateway is no longer available to new customers. Existing
customers of FSx File Gateway can continue to use the service normally. For capabilities
similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/ "https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/").

# AWS Regions that support Storage Gateway

An AWS Region is a physical location in the world where AWS has multiple Availability
Zones. Availability Zones consist of one or more discrete AWS data centers, each with
redundant power, networking, and connectivity, housed in separate facilities. This means
that each AWS Region is physically isolated and independent of the other Regions. Regions
provide fault tolerance, stability, and resilience, and can also reduce latency. The
resources that you create in one Region do not exist in any other Region unless you
explicitly use a replication feature offered by an AWS service. For example, Amazon S3 and
Amazon EC2 support cross-Region replication. Some services, such as AWS Identity and Access Management, do not have
Regional resources. You can launch AWS resources in locations that meet your business
requirements. For example, you might want to launch Amazon EC2 instances to host your AWS Storage Gateway
appliances in an AWS Region in Europe to be closer to your European users, or to meet
legal requirements. Your AWS account determines which of the Regions supported by a
specific service are available for you to use.

Amazon FSx File Gateway stores file data in the AWS Region where your Amazon FSx
file system is located. Before you start deploying your gateway, choose a Region in the
upper-right corner of the Storage Gateway console.

- Amazon FSx File Gateway — For supported AWS Regions and a list of AWS service
  endpoints that you can use with Amazon FSx File Gateway, see [Amazon FSx File Gateway endpoints and quotas](../../../general/latest/gr/fsxn.md "../../../general/latest/gr/fsxn.md")
  in the _AWS General Reference_.
- Storage Gateway — For supported AWS Regions and a list of AWS service
  endpoints that you can use with Storage Gateway, see [AWS Storage Gateway endpoints and quotas](../../../general/latest/gr/sg.md "../../../general/latest/gr/sg.md") in the
  _AWS General Reference_.
- Storage Gateway Hardware Appliance — For supported Regions that you can use with the
  hardware appliance, see [AWS Storage Gateway Hardware
  Appliance Regions](../../../general/latest/gr/sg.md#sg-hardware-appliance "../../../general/latest/gr/sg.md#sg-hardware-appliance") in the _AWS General Reference_.
