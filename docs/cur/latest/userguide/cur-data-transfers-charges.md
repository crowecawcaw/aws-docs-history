# Understanding data transfer charges

You can identify your AWS data transfer charges using the [lineItem/UsageType](Lineitem-columns.md#Lineitem-details-U-UsageType "Lineitem-columns.md#Lineitem-details-U-UsageType") column of your AWS CUR.

###### Note

Data transfer charges can vary depending on the services used and the source AWS
Region. For detailed pricing information, refer to the service’s pricing page. For
example, see [Amazon EC2 On-Demand
Pricing](https://aws.amazon.com/ec2/pricing/on-demand/ "https://aws.amazon.com/ec2/pricing/on-demand/") for detailed pricing information about Amazon EC2 data
transfer.

## Data transfer within an AWS

Region

Data transfer between Availability Zones in the same AWS Region have a
**UsageType** of
``Region`-DataTransfer-Regional-Bytes`. For
 example, the `USE2-DataTransfer-Regional-Bytes` usage type identifies
charges for data transfer between Availability Zones in the US East (Ohio) Region.

For a given resource, you’re charged for both inbound and outbound traffic in a
data transfer within an AWS Region. This means for each resource metered, you'll
see two `DataTransfer-Regional-Bytes` line items for each data transfer.
Confirm the service's pricing page for more information, because some services have
in-Region traffic at no cost.

## Data transfer between AWS

Regions

Data transfer between different AWS Regions can have the following usage
types:

- ``Source Region`-`Destination
Region`-AWS-In-Bytes`: Measures incoming data
  transfer TO the destination Region FROM another specific AWS
  Region.
- ``Source Region`-`Destination
Region`-AWS-Out-Bytes`: Measures outgoing data
  transfer FROM the source Region TO another specific AWS Region.
- ``Source Region`-AWS-In-Bytes`: This
  usage type appears when traffic flows via VPC Peering.
- ``Source Region`-AWS-Out-Bytes`: This
  usage type appears when traffic flows via VPC Peering.

For each resource, data transfer between AWS Regions corresponds to two line
items in your report:

- A line item for the data transferred into the destination Region
- A line item for the data transferred out from the source Region

There's no charge for the data transferred into the destination Region. The data
transfer charge is determined by the data transferred out from the source
Region.

For example, a data transfer from the `USE2` Region to the
`APS3` Region will have both a `APS3-USE2-AWS-In-Bytes`
line item and a `USE2-APS3-AWS-Out-Bytes` line item. The
`APS3-USE2-AWS-In-Bytes` line item has no corresponding charge. The
data transfer charge is associated with the `USE2-APS3-AWS-Out-Bytes`
line item.

## Data transfer out to the

internet

Data transfer from AWS to the internet have a **UsageType** of
``Region`-DataTransfer-Out-Bytes`. For
 example, the `USE2-DataTransfer-Out-Bytes`usage type identifies charges
 for data transfer from the`USE2` Region to the internet.

There’s no charge for data transfer from the internet to AWS.

###### Note

Data transfer usage types that don’t have the Region prefix, such as
`DataTransfer-Regional-Bytes` or
`DataTransfer-Out-Bytes`, represent data transfer from the
US East (N. Virginia) Region.

## AWS Direct Connect traffic

AWS Direct Connect data transfer over a public virtual interface have usage types that end
with `DataXfer-In` or `DataXfer-Out`.

AWS Direct Connect data transfer over a private or transit virtual interface have usage
types that end with `DataXfer-In:dc.3` or
`DataXfer-Out:dc.3`.

## S3 Transfer Acceleration

traffic

Amazon S3 data transfer using S3 Transfer Acceleration have usage types that contain
`ABytes`:

- Between Amazon S3 and Amazon EC2: Usage types that end with
  `C3DataTransfer-In-ABytes` or
  `C3DataTransfer-Out-ABytes`
- Between Amazon S3 and the internet: Usage types that end with
  `DataTransfer-In-ABytes` or
  `DataTransfer-Out-ABytes`
- Between Amazon S3 and CloudFront: Usage types that end with
  `CloudFront-In-ABytes` or
  `CloudFront-Out-ABytes`
- Between Amazon S3 buckets in different AWS Regions: Usage type of
  ``Source
Region`-`Destination
Region`-AWS-Out-ABytes`

## CloudFront traffic

CloudFront data transfer have a usage type of
``Region`-DataTransfer-Out-Bytes` or
 ``Region`-DataTransfer-Out-OBytes`
coupled with the product code `AmazonCloudFront`. The Region prefix in
the usage type refers to the CloudFront Edge location used in the data transfer. For
example, the `AP-DataTransfer-Out-Bytes` usage type identifies charges
for data transfer from the AP Region to the internet.

###### Tip

Use the [lineItem/ProductCode](Lineitem-columns.md#Lineitem-details-P-ProductCode "Lineitem-columns.md#Lineitem-details-P-ProductCode") column to distinguish CloudFront
data transfer from data transfer out to the internet. The usage types for these
data transfer types look similar.
