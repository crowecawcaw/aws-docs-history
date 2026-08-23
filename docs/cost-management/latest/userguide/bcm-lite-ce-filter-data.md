# Filter your data in the AWS Billing and Cost Management console

###### Warning

We're currently releasing our new experience to a limited number of customers. You might not be able to access this experience yet.

With Cost Explorer, you can filter how you view your AWS costs by one or more of the
following values:

- API operation
- Availability Zone
- Billing entity
- Charge type
- Include all
- Instance type
- Legal entity
- Linked account
- Platform
- Purchase option
- Region
- Resources
- Service
- Tag
- Tenancy
- Usage type
- Usage type group
  You can use Cost Explorer to see which service you use the most or apply multiple filters
  to look at intersecting datasets.

The following procedure shows you how to filter your cost and usage graph based on
DynamoDB usage only.

###### To filter your data

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. For **Filters**, choose a **Service**, and then
   select **DynamoDB**.

You can filter by entering DynamoDB in the search box. 3. Choose **Apply**.
To save this view, use your browser's bookmark feature to save your settings. If your
view has a forecast, it won't be saved, and instead Cost Explorer displays the most recent
forecast when you revisit your saved chart.

## Use multiple filters to show data in common

You can combine filters to show data in common. You can use up to 1024 filters in
Cost Explorer.

When you select multiple filters, Cost Explorer uses AND. This means if you filter
for service of Amazon EC2 and tag of Prod, only data about Amazon EC2 resources tagged with the
Prod tag is shown. When you select multiple values within a filter, Cost Explorer uses
OR.

## Filter and group options

In Cost Explorer, you can filter by the following groups. Note that these are not the
same filters as filtering the data that you want to view.

API operation

Requests made to and tasks performed by a service, such as write and get
requests to Amazon S3.

Availability Zone

Distinct locations within a Region that are insulated from failures in
other Availability Zones. They provide inexpensive, low-latency network
connectivity to other Availability Zones in the same Region.

Billing entity

Helps you identify whether your invoices or transactions are for AWS
Marketplace or for purchases of other AWS services.

Charge type

Different types of charges or fees.

- **Credit**: Any AWS credits
  that are applied to your account.
- **Other out-of-cycle
  charges**: Any subscription charges that aren't upfront
  reservation charges or support charges.
- **Refund**: Any refunds that
  you received. Refunds are listed as a separate line item in the data
  table. They don't appear as an item in the chart because they represent
  a negative value in the calculation of your costs. The chart displays
  only positive values.
- **Reservation applied
  usage**: Usage that AWS applied reservation discounts
  to.
- **Tax**: Any taxes that are
  associated with the charges or fees in your cost chart. Cost Explorer
  adds all taxes together as a single component of your costs. If you
  select five or fewer filters, Cost Explorer displays your tax expenses
  as a single bar. If you select six or more filters, Cost Explorer
  displays five bars, stacks, or lines, and then aggregates all remaining
  items, including taxes, into a sixth bar, stack slice, or plot line
  that's labeled Other.

Cost Explorer displays your tax costs in the chart only when you
choose Monthly drop down.

- **Usage**: Usage that AWS
  didn't apply reservation discounts to.

Instance type

The type of RI that you specified when you launched an Amazon EC2 host, Amazon RDS
instance class, Amazon Redshift node, or Amazon ElastiCache node. The instance type determines
the hardware of the computer used to host your instance.

Legal entity

The Seller of Record of a specific product or service. In most cases, the
invoicing entity and legal entity are the same. Possible values
include:

- **Amazon Web Services,
  Inc.** – The entity that sells AWS
  services.
- **Amazon Web Services India Private
  Limited** – The local Indian entity that acts as a reseller
  for AWS services in India.

Linked account

The member accounts in an organization.

Platform

The operating system that your RI runs on. Platform is either Linux or
Windows.

Purchase option

The method you choose to pay for your Amazon EC2 instances. This includes
Reserved Instances, Spot Instances, Scheduled Reserved Instances, and
On-Demand Instances.

Region

The geographic areas where AWS hosts your resources.

Resources

The unique identifier for your resources.

Service

AWS products. To learn what's available, see [AWS Products and
Services](https://aws.amazon.com/products/ "https://aws.amazon.com/products/").

Tag

A label that you can use to track the costs associated with specific areas
or entities within your business.

Tenancy

Specifies if the Amazon EC2 instance is hosted on shared or single-tenant
hardware. Some tenancy values include Shared (Default), Dedicated, and
Host.

Usage type

Usage types are the units that each service uses to measure the usage of a
specific type of resource. For example, the
`BoxUsage:t2.micro(Hrs)` usage type filters by the running hours
of Amazon EC2 t2.micro instances.

Usage type group

Usage type groups are filters that collect a specific category of usage
type filters into one filter. For example,
`BoxUsage:c1.medium(Hrs)`,
`BoxUsage:m3.xlarge(Hrs)`, and
`BoxUsage:t1.micro(Hrs)` are all filters for Amazon EC2 instance
running hours, so they are collected into the EC2: Running Hours
filter.

Usage type groups are available for DynamoDB, Amazon EC2, ElastiCache, Amazon RDS,
Amazon Redshift, and Amazon S3. The specific groups available to your account
depend on what services you've used. The list of groups that might be
available includes but isn't limited to the following:

DDB: Data Transfer - Internet (In)
Filters by the costs associated with how many GB are transferred to your DynamoDB databases.

DDB: Data Transfer - Internet (Out)
Filters by the costs associated with how many GB are transferred from your DynamoDB databases.

DDB: Indexed Data Storage
Filters by the costs associated with how many GB that you have stored in DynamoDB.

DDB: Provisioned Throughput Capacity - Read
Filters by the costs associated with how many units of read capacity that your DynamoDB databases used.

DDB: Provisioned Throughput Capacity - Write
Filters by the costs associated with how many units of write capacity that your DynamoDB databases used.

EC2: CloudWatch - Alarms
Filters by the costs associated with how many CloudWatch alarms that you have.

EC2: CloudWatch - Metrics
Filters by the costs associated with how many CloudWatch metrics that you have.

EC2: CloudWatch - Requests
Filters by the costs associated with how many CloudWatch requests that you make.

EC2: Data Transfer - CloudFront (Out)
Filters by the costs associated with how many GB are transferred from your Amazon EC2 instances to a CloudFront distribution.

EC2: Data Transfer - CloudFront (In)
Filters by the costs associated with how many GB are transferred to your Amazon EC2 instances from a CloudFront distribution.

EC2: Data Transfer - Inter AZ
Filters by the costs associated with how many GB are transferred into, out of, or between your Amazon EC2 instances in different AZs.

EC2: Data Transfer - Internet (In)
Filters by the costs associated with how many GB are transferred to your Amazon EC2 instances from outside the AWS network.

EC2: Data Transfer - Internet (Out)
Filters by the costs associated with how many GB are transferred from an Amazon EC2 instance to a host outside the AWS network.

EC2: Data Transfer - Region to Region (In)
Filters by the costs associated with how many GB are transferred to your Amazon EC2 instances from a different AWS Region.

EC2: Data Transfer - Region to Region (Out)
Filters by the costs associated with how many GB are transferred from your Amazon EC2 instances to a different AWS Region.

EC2: EBS - I/O Requests
Filters by the costs associated with how many I/O requests that you make to your Amazon EBS volumes.

EC2: EBS - Magnetic
Filters by the costs associated with how many GB that you have stored on Amazon EBS Magnetic volumes.

EC2: EBS - Provisioned IOPS
Filters by the costs associated with how many IOPS-months that you have provisioned for Amazon EBS.

EC2: EBS - SSD(gp2)
Filters by the costs associated with how many GB per month of General Purpose storage that your Amazon EBS volumes use.

EC2: EBS - SSD(io1)
Filters by the costs associated with how many GB per month of Provisioned IOPS SSD storage that your Amazon EBS volumes use.

EC2: EBS - Snapshots
Filters by the costs associated with how many GB per month that your Amazon EBS snapshots store.

EC2: EBS - Optimized
Filters by the costs associated with how many MB per instance hour that your Amazon EBS-optimized instances use.

EC2: ELB - Running Hours
Filters by the costs associated with how many hours that your Elastic Load Balancing load balancers ran.

EC2: Elastic IP - Additional Address
Filters by the costs associated with how many Elastic IP addresses that you attached to running Amazon EC2 instances.

EC2: Elastic IP - Idle Address
Filters by the costs associated with Elastic IP addresses that you have that aren't attached to running Amazon EC2 instances.

EC2: NAT Gateway - Data Processed
Filters by the costs associated with how many GB that your network address translation gateways (NAT gateways) processed.

EC2: NAT Gateway - Running Hours
Filters by the costs associated with how many hours that your NAT gateways ran.

EC2: Running Hours

Filters by the costs associated with how many hours that your Amazon EC2 instances ran.

This Usage Type Group contains only the following Usage Types:

- BoxUsage
- DedicatedUsage
- HostBoxUsage
- HostUsage
- ReservedHostUsage
- SchedUsage
- SpotUsage
- UnusedBox

ElastiCache: Running Hours
Filters by the costs associated with how many hours that your Amazon ElastiCache nodes ran.

ElastiCache: Storage
Filters by the costs associated with how many GB that you stored in Amazon ElastiCache.

RDS: Running Hours

Filters by the costs associated with how many hours that your Amazon RDS databases ran.

This Usage Type Group contains only the following Usage Types:

- AlwaysOnUsage
- BoxUsage
- DedicatedUsage
- HighUsage
- InstanceUsage
- MirrorUsage
- Multi-AZUsage
- SpotUsage

RDS: Data Transfer – CloudFront – In
Filters by the costs associated with how many GB are transferred into Amazon RDS from a CloudFront distribution.

RDS: Data Transfer – CloudFront – Out
Filters by the costs associated with how many GB are transferred from a CloudFront distribution to Amazon RDS data transfers.

RDS: Data Transfer – Direct Connect Locations – In
Filters by the costs associated with how many GB are transferred into Amazon RDS through a Direct Connect network connection.

RDS: Data Transfer – Direct Connect Locations – Out
Filters by the costs associated with how many GB are transferred from Amazon RDS through a Direct Connect network connection.

RDS: Data Transfer – InterAZ
Filters by the costs associated with how many GB are transferred into, out of, or between Amazon RDS buckets in different Availability Zones.

RDS: Data Transfer – Internet – In
Filters by the costs associated with how many GB are transferred to your Amazon RDS databases.

RDS: Data Transfer – Internet – Out
Filters by the costs associated with how many GB are transferred from your Amazon RDS databases.

RDS: Data Transfer – Region to Region – In
Filters by the costs associated with how many GB are transferred to your Amazon RDS instances from a different AWS Region.

RDS: Data Transfer – Region to Region – Out
Filters by the costs associated with how many GB are transferred from your Amazon RDS instances to a different AWS Region.

RDS: I/O Requests
Filters by the costs associated with how many I/O requests that you make to your Amazon RDS instance.

RDS: Provisioned IOPS
Filters by the costs associated with how many IOPS-months that you have provisioned for Amazon RDS.

RDS: Storage
Filters by the costs associated with how many GB that you have stored in Amazon RDS.

Redshift: DataScanned
Filters by the costs associated with how many GB that your Amazon Redshift nodes scanned.

Redshift: Running Hours
Filters by the costs associated with how many hours that your Amazon Redshift nodes ran.

S3: API Requests - Standard
Filters by the costs associated with GET and all other standard storage Amazon S3 requests.

S3: Data Transfer - CloudFront (In)
Filters by the costs associated with how many GB are transferred into Amazon S3 from a CloudFront distribution.

S3: Data Transfer - CloudFront (Out)
Filters by costs associated with how many GB are transferred from a CloudFront distribution to Amazon S3 data transfers, such as how much data was uploaded from your Amazon S3 bucket to your CloudFront distribution.

S3: Data Transfer - Inter AZ
Filters by the costs associated with how many GB are transferred into, out of, or between Amazon S3 buckets in different Availability Zones.

S3: Data Transfer - Internet (In)
Filters by the costs associated with how many GB are transferred to an Amazon S3 bucket from outside the AWS network.

S3: Data Transfer - Internet (Out)
Filters by the costs associated with how many GB are transferred from an Amazon S3 bucket to a host outside the AWS network.

S3: Data Transfer - Region to Region (In)
Filters by the costs associated with how many GB are transferred to Amazon S3 from a different AWS Region.

S3: Data Transfer - Region to Region (Out)
Filters by the costs associated with how many GB are transferred from Amazon S3 to a different AWS Region.

S3: Storage - Standard
Filters by the costs associated with how many GB that you have stored in Amazon S3.
