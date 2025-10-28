# Billing and account management

## What do Lightsail plans cost?

Lightsail plans are billed on an on-demand hourly rate, so you pay only for what you
use. For every Lightsail plan you use, we charge you the fixed hourly price, up to the
maximum monthly plan cost. The least expensive Lightsail plan starts at $0.0067 USD/hour
($5 USD/month). Lightsail plans that include a Windows Server license start at $0.0127
USD/hour ($9.50 USD/month).

## When am I getting charged for a

plan?

Lightsail instances and managed databases incur charges until they are deleted. These
resources accrue charges even when they are in the stopped state. If you delete your
Lightsail instance or managed database before the end of the month, we only charge you a
prorated cost, based on the total number of hours that you used your Lightsail instance or
managed database for that month. For example, if you use the least expensive Lightsail
instance plan for 100 hours in a month, you will be charged 46 cents (100\*0.0046).

## Can I try Lightsail instances for

free?

Yes. Whether you're an existing or new AWS customer, you get 750 hours of free usage
of the $5 USD Lightsail plan for free. You also can try Lightsail plans that include a
Windows Server license for free using the $9.50 USD Windows plan. You can use your 750 hours
of usage across as many instances as you like. For example, you can run a single Lightsail
instance for a whole month, or 10 Lightsail instances for 75 hours. The free trial offer
is only applicable to usage within the first calendar month from when you sign up to use
Lightsail. If your account is linked to an organization (under AWS Organizations), only
one account within the organization can benefit from the AWS Free Tier offers.

Instance plans include a data transfer allowance. Data transferred both in and out of
your instance counts towards your data transfer allowance. When you exceed your data
transfer allowance, instances—including those within the free-trial
period—will incur charges only for the excess data that is transferred out. For more
information about data transfer costs, see [What does data transfer cost?](#what-does-data-transfer-cost "#what-does-data-transfer-cost").

###### Note

As part of the AWS Free Tier, you can get started with Amazon Lightsail for free on
select instance bundles. For more information, see **AWS Free Tier**
on the [Amazon Lightsail Pricing page](https://aws.amazon.com/lightsail/pricing "https://aws.amazon.com/lightsail/pricing").

## When does the Lightsail free trial

start?

The Lightsail free trial benefits start when the first free trial eligible resource is
launched.

The extended 90 day free trial for instances and databases is applicable only on select
plans (bundles). The offer applies to new or existing AWS accounts that started using
Lightsail on or after July 8, 2021. For more information, see the [Lightsail pricing page](https://aws.amazon.com/lightsail/pricing/ "https://aws.amazon.com/lightsail/pricing/").

## What do Lightsail managed databases

cost?

Lightsail managed databases come in 4 plan sizes and start at $15 USD per month for a
1GB RAM database instance with 40 GB of SSD storage and 100 GB data transfer allowance. High
Availability plans costs two times the Standard plan prices, because they run an additional
database instance and storage disk in another Availability zone for redundancy.

## Can I try Lightsail managed

databases for free?

Yes! New Lightsail customers get 1 month of the $15 USD Lightsail plan free.

## What does Lightsail block storage

cost?

Lightsail block storage costs $0.10 USD per GB per month.

## What do Lightsail load balancers

cost?

Lightsail load balancers cost $18 USD per month.

## What does certificate management

cost?

Lightsail certificates and certificate management are free with use of a Lightsail
load balancer.

## What do Lightsail static IPv4

addresses cost?

There are no costs associated with Static IP addresses when they are attached to a
Lightsail instance. Static IPs cannot be attached to IPv6-only instances. IPv4 addresses
are a scarce resource and Lightsail is committed to helping to use them efficiently, so we
charge a small $0.005 USD/hour fee for static IPs not attached to an instance for more than
1 hour.

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

transfer allowance work with my load balancers?

Your load balancer does not consume your data transfer allowance. Traffic between the
load balancer and the target instances or distributions is metered and counts toward your
data transfer allowance for your instances or distributions, in the same way that traffic in
from and out to the internet is counted toward your data transfer allowance for Lightsail
instances that are not behind a load balancer. Traffic into and out of your load balancer to
the internet is not calculated toward the data transfer allowance for your instances.

## What if I exceed my data

transfer plan allowance?

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

charged for?

When you exceed the monthly free data transfer allowance of your instance plan, you will
get charged for data transfer OUT from a Lightsail instance to the internet or to another
AWS Region or to AWS resources in the same Region when using public IP addresses. The
charge for these types of data transfer above the free allowance is as follows.

- US East (Ohio) (us-east-2): $0.090 USD/GB
- US East (N. Virginia) (us-east-1): $0.090 USD/GB
- US West (Oregon) (us-west-2): $0.090 USD/GB
- Asia Pacific (Jakarta) (ap-southeast-3): $0.132 USD/GB
- Asia Pacific (Mumbai) (ap-south-1): $0.130 USD/GB
- Asia Pacific (Seoul) (ap-northeast-2): $0.130 USD/GB
- Asia Pacific (Singapore) (ap-southeast-1): $0.120 USD/GB
- Asia Pacific (Sydney) (ap-southeast-2): $0.170 USD/GB
- Asia Pacific (Tokyo) (ap-northeast-1): $0.140 USD/GB
- Canada (Central) (ca-central-1): $0.090 USD/GB
- EU (Frankfurt) (eu-central-1): $0.090 USD/GB
- EU (Ireland) (eu-west-1): $0.090 USD/GB
- EU (London) (eu-west-2): $0.090 USD/GB
- EU (Paris) (eu-west-3): $0.090 USD/GB
- EU (Stockholm) (eu-north-1): $0.090 USD/GB

Instances created in different Availability Zones can communicate between zones
privately and for free, and are much less likely to be impaired concurrently. Availability
Zones enable you to build highly available applications and websites without increasing the
cost of data transfer or compromising your application's security.

When you exceed the data transfer allowance of your Lightsail CDN distribution plan,
you are charged for all data transfer OUT. The charge for data transfer above your
distribution’s allowance is different from Lightsail instances and is as follows.

- Asia Pacific: $0.130 USD/GB
- Canada: $0.090 USD/GB
- Europe: $0.090 USD/GB
- India: $0.130 USD/GB
- Japan: $0.140 USD/GB
- Middle East: $0.110 USD/GB
- South Africa: $0.110 USD/GB
- South America: $0.110 USD/GB
- United States: $0.090 USD/GB

## How does my instance data

transfer allowance vary by AWS Region?

The regional data transfer allowance for Lightsail instances is found on [Amazon Lightsail pricing](https://aws.amazon.com/lightsail/pricing/ "https://aws.amazon.com/lightsail/pricing/"). The
allowance is the same for all AWS Regions, with the exception of the
Asia Pacific (Jakarta), Asia Pacific (Mumbai), and Asia Pacific (Sydney) Regions. Plans in
the Jakarta, Mumbai, and Sydney Regions include half the data transfer allowances of other
Regions.

The data transfer allowance for Lightsail managed databases are the same in all
AWS Regions.

## What do Lightsail domains cost?

The prices listed in the linked .pdf file apply for new domain name registrations,
renewals of existing domain name registrations as of December 22 2021. All prices include a
DNS zone and privacy protection. For information about the cost of registering domains, see
[Amazon Route 53 Pricing for Domain Registration](https://d32ze2gidvkk54.cloudfront.net/Amazon_Route_53_Domain_Registration_Pricing_20140731.pdf "https://d32ze2gidvkk54.cloudfront.net/Amazon_Route_53_Domain_Registration_Pricing_20140731.pdf"), and [Domain registration](amazon-lightsail-domain-registration.md "amazon-lightsail-domain-registration.md").

## What does Lightsail DNS

management cost?

DNS management is free within Lightsail. You can create up to 6 DNS zones and as many
records as you want for each DNS zone. You also get a monthly allowance of 3 million DNS
queries per month to your zones. Beyond your first 3 million queries in a month, you are
charged $0.40 USD per 1 million DNS queries.

## What do Lightsail snapshots

cost?

Lightsail snapshots (manual and automatic) cost $0.05 USD/GB-month to store. This
means that if you create a snapshot of an instance that is using 28 GB of space, and keep it
for a month, you pay $1.40 USD for the month.

When you take multiple, successive snapshots of the same instance, Lightsail
automatically cost-optimizes your snapshots. For each new snapshot you take, you're charged
only for the part of the data that changed. In the example above, if your instance data only
changes by 2 GB, your second instance snapshot costs only $0.10 USD per month.

## How can I manage my AWS account?

Lightsail is an AWS service and runs on AWS cloud infrastructure. You use the same
AWS account and credentials to log in to Lightsail and the AWS Management Console.

You can manage your AWS account, including changing your AWS account password, user
name, contact methods, opt-in Regions (Regions that are disabled by default), or billing
information from the [AWS Billing
and Cost Management console](https://console.aws.amazon.com/billing/home "https://console.aws.amazon.com/billing/home").

## How can I manage which opt-in Regions are

enabled and disabled?

An opt-in Region (Region that is disabled by default) can be enabled or disabled. Before
you can use an opt-in Region, it must be enabled. For more information on the available
Regions and how you can manage opt-in Regions, see [Regions and
Availability Zones for Lightsail](understanding-regions-and-availability-zones-in-amazon-lightsail.md "understanding-regions-and-availability-zones-in-amazon-lightsail.md").

## What happens to resources

in a disabled opt-in Region?

Any resources in a disabled opt-in Region will continue to run and incur charges at
their normal rate. Resources in a disabled opt-in Region can't be managed with the
Lightsail console while the Region is disabled, Lightsail API, AWS CLI, or SDKs. To delete
such resources, you must first temporarily enable the Region again so that you can manage
them. For more information, see [How can I delete resources
in a disabled opt-in Region?](#how-can-i-delete-resources-in-a-disabled-region "#how-can-i-delete-resources-in-a-disabled-region").

## How can I delete resources

in a disabled opt-in Region?

If you disable an opt-in Region before deleting resources there, you must temporarily
enable the Region again to delete such resources. For more information, see [Disable opt-in Regions for
Lightsail](opt-in-regions-for-lightsail-disable.md "opt-in-regions-for-lightsail-disable.md")

## What are the Lightsail legal

terms of use?

Lightsail is an Amazon web service, so to use Lightsail, you first agree to the
[AWS Customer Agreement and Service
Terms](https://aws.amazon.com/legal/ "https://aws.amazon.com/legal/"). When creating Lightsail instances, you also agree that your use of
software is also subject to the end user license agreement of the seller, available for your
review on the create instance page.

## How can I pay my Lightsail bill?

You can pay and manage your bill through the AWS Billing and Cost Management console.
AWS accepts most major credit cards. Learn more about managing your payment methods [here](../../../awsaccountbilling/latest/aboutv2/manage-payments.md "../../../awsaccountbilling/latest/aboutv2/manage-payments.md").
