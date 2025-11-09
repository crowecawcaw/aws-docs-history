# S3 Express One Zone Availability Zones and Regions

An Availability Zone is one or more discrete data centers with redundant power,
networking, and connectivity in an AWS Region. To optimize low-latency retrievals, objects
in the Amazon S3 Express One Zone storage class are redundantly stored in S3 directory buckets in a single
Availability Zone that's local to your compute workload. When you create a directory bucket,
you choose the Availability Zone and AWS Region where your bucket will be located.

AWS maps the physical Availability Zones randomly to the Availability Zone names for
each AWS account. This approach helps to distribute resources across the Availability
Zones in an AWS Region, instead of resources likely being concentrated in the first
Availability Zone for each Region. As a result, the Availability Zone
`us-east-1a` for your AWS account might not represent the same physical
location as `us-east-1a` for a different AWS account. For more information, see
[Regions and
Availability Zones](../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md "../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md") in the _Amazon EC2 User Guide_.

To coordinate Availability Zones across accounts, you must use the _AZ ID_, which is a unique and consistent identifier for an Availability Zone.
For example, `use1-az1` is an AZ ID for the `us-east-1` Region and it
has the same physical location in every AWS account. The following illustration shows how
the AZ IDs are the same for every account, even though the Availability Zone names might be
mapped differently for each account.

![Illustration showing Availability Zone mapping and Regions.](images/availability-zone-mapping.png)
With
S3 Express One Zone, your data is redundantly stored on multiple devices within a single
Availability Zone. S3 Express One Zone is designed for 99.95 percent availability within a single Availability Zone and is backed
by the [Amazon S3 Service Level Agreement](https://aws.amazon.com/s3/sla/ "https://aws.amazon.com/s3/sla/"). For more information, see [Availability Zones](directory-bucket-high-performance.md#s3-express-overview-az "directory-bucket-high-performance.md#s3-express-overview-az")

The following table shows the S3 Express One Zone supported Regions and Availability
Zones.

| Region name           | Region code      | Availability Zone ID |
| --------------------- | ---------------- | -------------------- |
| US East (N. Virginia) | `us-east-1`      | `use1-az4`           |
| `use1-az5`            |
| `use1-az6`            |
| US East (Ohio)        | `us-east-2`      | `use2-az1`           |
| `use2-az2`            |
| US West (Oregon)      | `us-west-2`      | `usw2-az1`           |
| `usw2-az3`            |
| `usw2-az4`            |
| Asia Pacific (Mumbai) | `ap-south-1`     | `aps1-az1`           |
| `aps1-az3`            |
| Asia Pacific (Tokyo)  | `ap-northeast-1` | `apne1-az1`          |
| `apne1-az4`           |
| Europe (Ireland)      | `eu-west-1`      | `euw1-az1`           |
| `euw1-az3`            |
| Europe (Stockholm)    | `eu-north-1`     | `eun1-az1`           |
| `eun1-az2`            |
| `eun1-az3`            |
