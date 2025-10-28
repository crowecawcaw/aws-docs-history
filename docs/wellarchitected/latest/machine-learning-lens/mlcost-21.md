# MLCOST-21: Enable data and compute proximity

Ensure that the Region used for training and developing models
is the same as the one used for data. This approach helps
minimize the time and cost of transferring data to the
computation environment.

## Implementation plan

- **Keep data and compute resources in
  close proximity** -
  [Amazon EC2](../../../AWSEC2/latest/UserGuide/concepts.md "../../../AWSEC2/latest/UserGuide/concepts.md") is hosted in multiple locations world-wide.
  These locations are composed of
  [Regions,
  Availability Zones,](../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md "../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md")
  [Local
  Zones, AWS Outposts, and Wavelength Zones](../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md "../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md"). Each
  _Region_ is a separate geographic area.
  If you are launching a compute cluster, you should launch
  the cluster in close proximity to your data to get the
  best performance. Say, your
  [Amazon S3](../../../AmazonS3/latest/userguide/GetStartedWithS3.md "../../../AmazonS3/latest/userguide/GetStartedWithS3.md") bucket is in the US West (Oregon) Region, you
  should launch your cluster in the US West (Oregon) Region
  to avoid Cross-Region data transfer fees.

## Documents

- [Regions
  and Zones](../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md "../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md")

## Blogs

- [Overview
  of Data Transfer Costs for Common Architectures](https://aws.amazon.com/blogs/architecture/overview-of-data-transfer-costs-for-common-architectures/ "https://aws.amazon.com/blogs/architecture/overview-of-data-transfer-costs-for-common-architectures/")

## Videos

- [AWS re:Invent 2018: Architecture Patterns for Multi-Region
  Active-Active Applications](https://www.youtube.com/watch?v=2e29I3dA8o4 "https://www.youtube.com/watch?v=2e29I3dA8o4")
