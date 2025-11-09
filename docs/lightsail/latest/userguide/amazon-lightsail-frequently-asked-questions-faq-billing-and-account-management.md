# Billing and account management

###### Note

Topics about data transfer in Lightsail have been relocated to [Data transfer in Lightsail](amazon-lightsail-faq-data-transfer-allowance.md "amazon-lightsail-faq-data-transfer-allowance.md").

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
information about data transfer costs, see [What does data transfer cost?](amazon-lightsail-faq-data-transfer-allowance.md#data-transfer-allowance-what-does-data-transfer-cost "amazon-lightsail-faq-data-transfer-allowance.md#data-transfer-allowance-what-does-data-transfer-cost").

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
