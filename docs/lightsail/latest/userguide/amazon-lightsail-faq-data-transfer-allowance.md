# Data transfer in Lightsail

## What if I exceed my data

transfer plan allowance for instances?

We have designed our data transfer plans so that the vast majority of our customers will
be fully covered by their allowance and not incur any additional charges. If your instance
exceeds its plan data transfer allowance, you will be charged an overage fee per GB of data
transfer used (data transfer OUT to the internet only).

Even if your instance exceeds its plan data transfer allowance, many types of data
transfer are free. Data transfer IN to Lightsail instances and databases is always free.
Data transfer OUT from a Lightsail instance to another Lightsail instance, in between
Lightsail instances and Lightsail managed databases, or to AWS resources in the same
Region is also free if private IP addresses are used.

## What types of data transfer do I get

charged for with instances?

When you exceed the monthly free data transfer allowance of your instance plan, you will
get charged for data transfer OUT from a Lightsail instance to the internet or to another
AWS Region or to AWS resources in the same Region when using public IP addresses. The
charge for these types of data transfer above the free allowance is as follows.

- US East (Ohio) (us-east-2): $0.09 USD/GB
- US East (N. Virginia) (us-east-1): $0.09 USD/GB
- US West (Oregon) (us-west-2): $0.09 USD/GB
- Asia Pacific (Mumbai) (ap-south-1): $0.13 USD/GB
- Asia Pacific (Seoul) (ap-northeast-2): $0.13 USD/GB
- Asia Pacific (Singapore) (ap-southeast-1): $0.12 USD/GB
- Asia Pacific (Sydney) (ap-southeast-2): $0.17 USD/GB
- Asia Pacific (Tokyo) (ap-northeast-1): $0.14 USD/GB
- Canada (Central) (ca-central-1): $0.09 USD/GB
- EU (Frankfurt) (eu-central-1): $0.09 USD/GB
- EU (Ireland) (eu-west-1): $0.09 USD/GB
- EU (London) (eu-west-2): $0.09 USD/GB
- EU (Paris) (eu-west-3): $0.09 USD/GB
- EU (Stockholm) (eu-north-1): $0.09 USD/GB

Instances created in different Availability Zones can communicate between zones
privately and for free, and are much less likely to be impaired concurrently. Availability
Zones enable you to build highly available applications and websites without increasing the
cost of data transfer or compromising your application's security.

## How does my data

transfer allowance work for instances?

Every Lightsail instance plan includes a data transfer allowance. Both data transfer
IN and data transfer OUT of your instance count toward your data transfer allowance. If you
exceed your data transfer allowance, you will only be charged for the excess data transfer
OUT from a Lightsail instance to the Internet or to AWS resources using the public IP
address of the instance. This additional charge for data transfer beyond allowance is also
payable for resources that are within their free trial period. Your data transfer allowance
resets every month, and your instance can consume it whenever it needs to within the
month.

You will not be charged for the excess data transfer IN to your Lightsail instance
(see **Example 1**). Data transfer allowance is aggregated for instances of
the same bundle (bundleId) in a Region (see **Example 2** and
**Example 3**). Data transfer allowance is also aggregated for IPv4 and
IPv6 instances of the same size (see **Example 4**). Deleting an instance
and creating a new instance does not reset the data transfer allowance (see
**Example 5**). Creating a new instance does not offset the existing data
transfer overage (see **Example 6**). For more information about
Lightsail bundles, see [Bundle](../../2016-11-28/api-reference/API_Bundle.md "../../2016-11-28/api-reference/API_Bundle.md") in the
Amazon Lightsail API Reference.

- Example 1 – You have one $5 USD per month
  instance bundle (bundleId `nano_3_0`) with 1 TB per month data transfer
  allowance. If you send 500 GB of data to the Internet (data transfer OUT) and 400 GB of
  data to the instance (data transfer IN), you will have consumed 900 GB of your 1 TB
  allowance. If you send another 200 GB of data to the Internet, you will exceed your
  allowance by 100 GB, and will be charged a data transfer OUT overage fee for 100 GB. If
  you next send 200 GB of data to the instance, you will not be charged for
  overage.
- Example 2 – If you have two $5 USD per month
  instance bundles (bundleId `nano_3_0`) for a full month in a region, each
  with 1 TB per month data transfer allowance, you get 2 TB data transfer allowance in
  aggregate. If you send 1.5 TB of data to the Internet with the first instance and 100 GB
  of data to the Internet with the second instance, you will still be 400 GB under your
  total allowance of 2 TB, and you will not be charged any data transfer OUT overage
  fees.
- Example 3 – You create two sets of instance
  bundles: set A with two $5 USD per month instance bundles (bundleId
  `nano_3_0`) and set B with three $7 USD per month instance bundles
  (bundleId `micro_3_0`), both in the US West (Oregon) Region. In aggregate,
  this gives you 2 TB of data transfer allowance for set A, and 6 TB of data transfer
  allowance for set B. If you transfer 3 TB of data to the Internet through set A
  instances and 4 TB of data to the Internet through Set B instances, you will exceed your
  data transfer allowance for Set A instances and will be charged a data transfer OUT
  overage fee for 1 TB. You will still be within your allowance for Set B instances by 2
  TB.
- Example 4 – You have consumed 600 GB of the
  total 1 TB data transfer allowance for your $3.50 USD per month IPv6 instance bundle
  (bundleId `nano_ipv6_3_0`) within the first 20 days of the billing month. You
  decide to switch the networking type of your instance to dual-stack (bundleId
  `nano_3_0` charged at $5 USD per month price) on the 21st day. Your data
  transfer utilization for the month will not reset, and will remain at 600 GB, with 400
  GB allowance left. During the remainder of the billing month, if you send 500 GB of data
  to the Internet, you will accrue data transfer OUT overage charges for 100 GB.
- Example 5 – You have three $5 USD per month
  instance bundles (bundleId `nano_3_0`), each with 1 TB per month data
  transfer allowance. Assume you have consumed 1 TB of the total 3 TB data transfer
  allowance within the billing month, which leaves you with 2 TB of remaining data
  transfer allowance. If you delete all your instances, and create three new instances of
  the same bundle (bundleId `nano_3_0`) in the same Region within the same
  billing month, your data transfer utilization will still be 1 TB and remaining data
  transfer allowance will still be 2 TB. You can transfer 2 TB more data through your
  instances within the same month before you start accruing any data transfer OUT overage
  charges.
- Example 6 – After using your monthly 1 TB data
  transfer allowance for your $5 USD per month instance bundle (bundleId
  `nano_3_0`) in the first 20 days of the billing month, you sent an
  additional 100 GB of data to the Internet. You will accrue a data transfer OUT overage
  fee for this 100 GB. If you now create another new instance of the same bundle (bundleId
  `nano_3_0`), you will still be charged the data transfer OUT overage fee
  previously accrued. Further data transfer OUT through these instances will continue to
  accrue data transfer OUT overage fees.

## How does my data

transfer allowance for instances vary by AWS Region?

The regional data transfer allowance for Lightsail instances is found on [Amazon Lightsail pricing](https://aws.amazon.com/lightsail/pricing/ "https://aws.amazon.com/lightsail/pricing/"). The
allowance is the same for all AWS Regions, with the exception of the
Asia Pacific (Jakarta), Asia Pacific (Mumbai), and Asia Pacific (Sydney) Regions. Plans in
the Jakarta, Mumbai, and Sydney Regions include half the data transfer allowances of other
Regions.

The data transfer allowance for Lightsail managed databases is the same in all
AWS Regions.

## What does data transfer cost?

Your instance, database, and content delivery network (CDN) distribution plans include a
data transfer allowance.

For Lightsail instances, both data transfer in and data transfer out of your instance
count toward your data transfer allowance. If you exceed your data transfer allowance, you
will only be charged for the excess data transfer OUT from a Lightsail instance to the
internet or to AWS resources using the public IP address of the instance. You will not be
charged for the excess data transfer IN to your Lightsail instance. When transferring data using the instance's
private IP address, data transfer IN and OUT of Lightsail instances count towards your data transfer quota.
However, data transferred using the private IP address is free even if you exceed your data transfer allowance.

For Lightsail managed databases, only data transfer OUT is counted against your
allowance. If you exceed your data transfer allowance, you will only get charged for data
transfer OUT from a Lightsail managed database to the internet.

For Lightsail CDN distributions, all data transfer out of your distribution counts
toward your allowance. All data transfer out of your distribution will incur a charge after
you exceed your distribution data transfer allowance.

## How does my data

transfer allowance work with my load balancers?

Your load balancer does not consume your data transfer allowance. Traffic between the
load balancer and the target instances or distributions is metered and counts toward your
data transfer allowance for your instances or distributions, in the same way that traffic in
from and out to the internet is counted toward your data transfer allowance for Lightsail
instances that are not behind a load balancer. Traffic into and out of your load balancer to
the internet is not calculated toward the data transfer allowance for your instances.

## How does my data transfer allowance work with object

storage?

You can consume your data transfer allowance by transferring data into and out of
Lightsail object storage, except for the following.

- Data transferred into Lightsail object storage from the internet
- Data transfer between Lightsail object storage resources
- Data transferred out from Lightsail object storage to another Lightsail resource
  in the same AWS Region (including to a resource in a different AWS account, but in
  the same AWS Region)
- Data transferred out from Lightsail object storage to a Lightsail CDN
  distribution

## What types of data transfer do I get

charged for with distributions?

When you exceed the data transfer allowance of your Lightsail CDN distribution plan,
you are charged for all data transfer OUT. The charge for data transfer above your
distribution's allowance is as follows.

- Asia Pacific: $0.13 USD/GB
- Canada: $0.09 USD/GB
- Europe: $0.09 USD/GB
- India: $0.13 USD/GB
- Japan: $0.14 USD/GB
- Middle East: $0.11 USD/GB
- South Africa: $0.11 USD/GB
- South America: $0.11 USD/GB
- United States: $0.09 USD/GB

## What are the differences between Lightsail's instance data transfer quotas and

distribution data transfer quotas?

The charge for data transfer above your distribution's allowance is different from Lightsail instances.
While data transfer IN and OUT count toward your instance's data transfer quota, only
data transfer OUT to your origin and to your viewers counts toward your distribution's quota.
In addition, all data transfer OUT in excess of your distribution's quota is charged an
overage fee, whereas some types of data transfer OUT are free for instances. Finally,
Lightsail distributions use a different regional overage model, though the majority of the
rates are the same as those charged for instance overage.

## Will I be charged for data

transfer in and out of the container service?

Every container service comes with a data transfer quota (500 GB per month). This counts
toward both the data transfer IN and OUT of your service. When you exceed the quota, you
will get charged for data transfer OUT from a Lightsail container service to the Internet
or to another AWS Region or to AWS resources in the same Region when using public IP
addresses. The charge for these types of data transfer above the free allowance is as
follows.

- US East (Ohio) (us-east-2): $0.09 USD/GB
- US East (N. Virginia) (us-east-1): $0.09 USD/GB
- US West (Oregon) (us-west-2): $0.09 USD/GB
- Asia Pacific (Mumbai) (ap-south-1): $0.13 USD/GB
- Asia Pacific (Seoul) (ap-northeast-2): $0.13 USD/GB
- Asia Pacific (Singapore) (ap-southeast-1): $0.12 USD/GB
- Asia Pacific (Sydney) (ap-southeast-2): $0.17 USD/GB
- Asia Pacific (Tokyo) (ap-northeast-1): $0.14 USD/GB
- Canada (Central) (ca-central-1): $0.09 USD/GB
- EU (Frankfurt) (eu-central-1): $0.09 USD/GB
- EU (Ireland) (eu-west-1): $0.09 USD/GB
- EU (London) (eu-west-2): $0.09 USD/GB
- EU (Paris) (eu-west-3): $0.09 USD/GB
- EU (Stockholm) (eu-north-1): $0.09 USD/GB
