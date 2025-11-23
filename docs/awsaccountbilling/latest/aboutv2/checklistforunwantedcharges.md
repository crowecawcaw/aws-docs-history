# Understanding unexpected charges

|                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **_For questions about your AWS bills or to appeal your charges, contact Support to address your inquiries immediately. To get help, see [Getting help with your bills and payments](billing-get-answers.md "billing-get-answers.md"). To understand your bills page contents, see [Using the Bills page to understand your monthly charges and<br>invoice](getting-viewing-bill.md#invoice "getting-viewing-bill.md#invoice")._** |

###### Note

If your AWS organization uses billing transfer, contact the bill transfer account owner first because they control your cost data and receive your AWS invoices. To find the bill transfer account information, go to the **billing transfer** page, **Outbound billing** tab.

Here are examples to help you avoid unexpected charges on your bill. This page lists
specific features or behaviors within individual services from AWS that can sometimes
result in unexpected charges, particularly if you unsubscribe from the service or close your
account.

###### Note

This is not an exhaustive list. For any questions for your specific use case, contact
Support by following the process on [Getting help with your bills and payments](billing-get-answers.md "billing-get-answers.md").

If you close your account or unsubscribe from a service, make sure that you take the
appropriate steps for every AWS Region you've allocated AWS resources.

###### Topics

- [Usage exceeds AWS Free Tier](#checkexceedfree "#checkexceedfree")
- [Charges received after account closure](#checkbillafterclosure "#checkbillafterclosure")
- [Charges incurred from resources in
  AWS Regions that are turned off](#check-disabled-region "#check-disabled-region")
- [Charges incurred by services launched by other
  services](#servicesnotfree "#servicesnotfree")
- [Charges incurred by Amazon EC2 instances](#checkec2instances "#checkec2instances")
- [Charges incurred by Amazon Elastic Block Store volumes and
  snapshots](#checkebsvolumes "#checkebsvolumes")
- [Charges incurred by Elastic IP
  addresses](#checkelasticipaddresses "#checkelasticipaddresses")
- [Charges incurred by storage services](#servicestorage "#servicestorage")
- [Charges incurred for AWS Organizations that use billing transfer](#billingtransfer-charges "#billingtransfer-charges")
- [Contacting Support](#all-other-charges "#all-other-charges")

## Usage exceeds AWS Free Tier

Check if your services have expired your free tier usage. If you chose **Paid plan** for your AWS Free Tier, you are charged using pay-as-you go pricing after six months ends or when your credits are fully used. Your account is not closed, allowing for seamless, continuous usage of your AWS resources. For more information, see [Trying services using AWS Free Tier (before July 15, 2025)](billing-free-tier.md "billing-free-tier.md").

After you've identified the resources that are generating charges, you can continue to
use the resources and manage your billing, terminate unused resources, or close your
AWS account.

- For information about managing your billing, see [What is AWS Billing and Cost Management?](billing-what-is.md "billing-what-is.md") and [Getting set up with Billing](billing-getting-started.md "billing-getting-started.md").
- For information about terminating resources, go to the resource documentation
  for that service. For example, if you have unused Amazon Elastic Compute Cloud instances, see [Terminate your instance](#checkec2instances "#checkec2instances").
- For information about closing your AWS account, see [Close your account](../../../accounts/latest/reference/manage-acct-closing.md "../../../accounts/latest/reference/manage-acct-closing.md") in the _AWS Account Management Reference Guide_.

###### Note

When you use billing transfer, you can't view your Free Tier benefits in Cost Explorer, the **Bills** page, or AWS Cost and Usage Report unless your bill transfer account enables this access. Contact your bill transfer account owner with questions about Free Tier benefits.

## Charges received after account closure

You might receive a bill after you close your account due to one of the following
reasons:

**You incurred charges in the month before you closed your account**

You receive a final bill for the usage incurred between the beginning of
the month and the date that you closed your account. For example, if you
closed your account on January 15, you will receive a bill at the beginning
of February for usage incurred from January 1-15.

**You have active Reserved Instances on your account**

You might have provisioned Amazon EC2 Reserved Instances, Amazon Relational Database Service (Amazon RDS) Reserved Instances, Amazon Redshift
Reserved Instances, or Amazon ElastiCache Reserved Cache Nodes. You will continue to receive a
bill for these resources until the reservation period expires. For more
information, see [Reserved Instances](../../../AWSEC2/latest/UserGuide/ec2-reserved-instances.md "../../../AWSEC2/latest/UserGuide/ec2-reserved-instances.md") in the
_Amazon EC2 User Guide_.

**You signed up for Savings Plans**

You will continue to receive a bill for your compute usage covered under
Savings Plans until the plan term is completed. For more information about Savings Plans,
see the [Savings Plans User Guide](../../../savingsplans/latest/userguide/what-is-savings-plans.md "../../../savingsplans/latest/userguide/what-is-savings-plans.md").

**You have active AWS Marketplace subscriptions**

AWS Marketplace subscriptions aren't automatically canceled on account closure.
First, [terminate all instances of your software](../../../marketplace/latest/buyerguide/buyer-getting-started.md#step-6-terminate-your-instance "../../../marketplace/latest/buyerguide/buyer-getting-started.md#step-6-terminate-your-instance") in
the subscriptions. Then, cancel subscriptions on the [Manage subscriptions](https://aws.amazon.com/marketplace/library "https://aws.amazon.com/marketplace/library")
page of the AWS Marketplace console.

###### Important

Within 90 days of closing your account, you can sign in to your account, view
resources that are still active, view past billing, and pay for AWS bills. For
more information, see [Close your account](../../../accounts/latest/reference/manage-acct-closing.md "../../../accounts/latest/reference/manage-acct-closing.md") in the _AWS Account Management Reference Guide_.

To pay your unpaid AWS bills, see [Making payments](manage-making-a-payment.md "manage-making-a-payment.md").

## Charges incurred from resources in

AWS Regions that are turned off

If you turn off (disable) an AWS Region that you still have resources in, you will
continue to incur charges for those resources. However, can't access the resources in a
disabled Region.

To avoid incurring charges from these resources, enable the Region, terminate all
resources in that Region, and then disable the Region.

For more information about managing Regions for your account, see [Specify which AWS Regions your account can use](../../../accounts/latest/reference/manage-acct-regions.md "../../../accounts/latest/reference/manage-acct-regions.md") in the
_AWS Account Management Reference Guide_.

## Charges incurred by services launched by other

services

A number of AWS services can launch resources, so be sure to check for anything that
might have launched through any service that you've used.

### Charges incurred from resources created by

AWS Elastic Beanstalk

Elastic Beanstalk is designed to ensure that all the resources that you need are running,
which means that it automatically relaunches any services that you stop. To avoid
this, you must terminate your Elastic Beanstalk environment before you terminate resources that
Elastic Beanstalk has created. For more information, see [Terminating an
Environment](../../../elasticbeanstalk/latest/dg/using-features.md "../../../elasticbeanstalk/latest/dg/using-features.md") in the _AWS Elastic Beanstalk Developer Guide_.

### Charges incurred from ELB (ELB) load

balancers

Like Elastic Beanstalk environments, ELB load balancers are designed to keep a minimum number
of Amazon Elastic Compute Cloud (Amazon EC2) instances running. You must terminate your load balancer before
you delete the Amazon EC2 instances that are registered with it. For more information,
see [Delete Your Load
Balancer](../../../elasticloadbalancing/latest/userguide/US_EndLoadBalancing02.md "../../../elasticloadbalancing/latest/userguide/US_EndLoadBalancing02.md") in the _Elastic Load Balancing User Guide_.

### Charges incurred by services started in OpsWorks

If you use the OpsWorks environment to create AWS resources, you must use OpsWorks to
terminate those resources or OpsWorks restarts them. For example, if you use OpsWorks to
create an Amazon EC2 instance, but then terminate it by using the Amazon EC2 console, the
OpsWorks auto healing feature categorizes the instance as failed and restarts it. For
more information, see the [AWS OpsWorks User Guide](../../../opsworks/latest/userguide/welcome.md "../../../opsworks/latest/userguide/welcome.md").

## Charges incurred by Amazon EC2 instances

After you remove load balancers and ELB environments, you can stop or terminate
Amazon EC2 instances. Stopping an instance allows you to start it again later, but you might
be charged for storage. Terminating an instance permanently deletes it. For more
information, see [Instance
lifecycle](../../../AWSEC2/latest/UserGuide/ec2-instance-lifecycle.md "../../../AWSEC2/latest/UserGuide/ec2-instance-lifecycle.md"), particularly [Stop and
start your instance](../../../AWSEC2/latest/UserGuide/Stop_Start.md "../../../AWSEC2/latest/UserGuide/Stop_Start.md") and [Terminate your Instance](../../../AWSEC2/latest/UserGuide/terminating-instances.md "../../../AWSEC2/latest/UserGuide/terminating-instances.md") in
the _Amazon EC2 User Guide_.

###### Notes

- Amazon EC2 instances serve as the foundation for multiple AWS services. They
  can appear in the Amazon EC2 console instances list even if they were started by
  other services. For example, Amazon RDS instances run on Amazon EC2 instances.
- If you terminate an underlying Amazon EC2 instance, the service that started it
  might interpret the termination as a failure and restart the instance. For
  example, OpsWorks has a feature called _auto healing_ that
  restarts resources when it detects failures. In general, it's a best
  practice to delete resources through the services that started them.

Additionally, if you create Amazon EC2 instances from an Amazon Machine Image (AMI) that is
backed by an instance store, check Amazon S3 for the related bundle. Deregistering an AMI
doesn't delete the bundle. For more information, see [Deregistering your AMI](../../../AWSEC2/latest/UserGuide/deregister-ami.md "../../../AWSEC2/latest/UserGuide/deregister-ami.md") in the
_Amazon EC2 User Guide_.

## Charges incurred by Amazon Elastic Block Store volumes and

snapshots

Most Amazon EC2 instances are configured so that their associated Amazon EBS volumes are deleted
when they are terminated, but it's possible to set up an instance that preserves its
volume and the data. Check the **Volumes** pane in the Amazon EC2 console
for volumes that you don’t need anymore. For more information, see [Deleting an Amazon EBS volume](../../../AWSEC2/latest/UserGuide/ebs-deleting-volume.md "../../../AWSEC2/latest/UserGuide/ebs-deleting-volume.md") in the
_Amazon EC2 User Guide_.

If you have stored snapshots of your Amazon EBS volumes and no longer need them, you should
delete them as well. Deleting a volume doesn't automatically delete the associated
snapshots.

For more information about deleting snapshots, see [Deleting an Amazon EBS snapshot](../../../AWSEC2/latest/UserGuide/ebs-deleting-snapshot.md "../../../AWSEC2/latest/UserGuide/ebs-deleting-snapshot.md") in
the _Amazon EC2 User Guide_.

Deleting a snapshot might not reduce your organization's data storage costs. Other
snapshots might reference that snapshot's data, and referenced data is always preserved.

###### Example: Deleting a snapshot

Say that when you take the first snapshot (`snap-A`) of a
volume with 10 GiB of data, the size of the snapshot is also 10 GiB. Because
snapshots are incremental, the second snapshot that you take of the same volume
contains only blocks of data that changed since the first snapshot was taken.

The second snapshot (`snap-B`) also references the data
in the first snapshot. That is, if you modify 4 GiB of data and take a second
snapshot, the size of the second snapshot is 4 GiB. In addition, the second snapshot
references the unchanged 6 GiB in the first snapshot. For more information, see
[How snapshots
work](../../../AWSEC2/latest/UserGuide/EBSSnapshots.md#how_snapshots_work "../../../AWSEC2/latest/UserGuide/EBSSnapshots.md#how_snapshots_work") in the _Amazon EC2 User Guide_.

In this example, you will see two entries in your daily AWS Cost and Usage Reports (AWS CUR). AWS CUR
captures the snapshot usage amount for a single day. In this example, the usage is
0.33 GiB (10 GiB/ 30 days) for `snap-A`, and 0.1333 GiB (4
GiB/ 30 days) for `snap-B`. Using the rate of $0.05 per GB
month, `snap-A` costs you 0.33 GiB x $0.05 = $0.0165.
`Snap-B` costs you 0.133 GiB x $0.05 = $0.0066, for a
total of $0.0231 per day for both snapshots. For more information, see the [AWS Data Exports User
Guide](../../../cur/latest/userguide/what-is-cur.md "../../../cur/latest/userguide/what-is-cur.md").

| lineItem/ Operation | lineItem/ ResourceId                      | lineItem/ UsageAmount | lineItem/ UnblendedCost | resourceTags/ user:usage |
| ------------------- | ----------------------------------------- | --------------------- | ----------------------- | ------------------------ |
| CreateSnapshot      | arn:aws:ec2:us-east-1:123:snapshot/snap-A | 0.33                  | 0.0165                  | dev                      |
| CreateSnapshot      | arn:aws:ec2:us-east-1:123:snapshot/snap-B | 0.133                 | 0.0066                  | dev                      |

If you delete the first snapshot (`snap-A` in the first
row of the previous table), any data that is referenced by the second snapshot
(`snap-B` in the second row of the previous table) is
preserved. Remember that the second snapshot contains the 4 GiB of incremental data,
and references 6 GiB from the first snapshot. After you delete
`snap-A`, the size of `snap-B`
becomes 10 GiB (4 changed GiB from the `snap-B` and 6
unchanged GiB from `snap-A`).

In the following table, your daily AWS CUR will have the usage amount for
`snap-B` as 0.33 GiB (10 GiB/ 30 days), charged at
$0.0165 per day. When you delete a snapshot, the charges for the remaining snapshots
are recalculated daily, resulting in the possibility that the cost for each snapshot
can change daily as well.

| lineItem/ Operation | lineItem/ ResourceId                      | lineItem/ UsageAmount | lineItem/ UnblendedCost | resourceTags/ user:usage |
| ------------------- | ----------------------------------------- | --------------------- | ----------------------- | ------------------------ |
| CreateSnapshot      | arn:aws:ec2:us-east-1:123:snapshot/snap-B | 0.33                  | 0.0165                  | dev                      |

For more information about snapshots, see the [Cost Allocation for EBS
Snapshots](https://aws.amazon.com/blogs/aws/new-cost-allocation-for-ebs-snapshots/ "https://aws.amazon.com/blogs/aws/new-cost-allocation-for-ebs-snapshots/") blog post.

## Charges incurred by Elastic IP

addresses

Any Elastic IP addresses that are attached to an instance that you terminate are
unattached, but they are still allocated to you. If you don’t need that IP address
anymore, release it to avoid additional charges. For more information, see [Release an Elastic IP address](../../../AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.md#using-instance-addressing-eips-releasing "../../../AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.md#using-instance-addressing-eips-releasing") in the _Amazon EC2 User Guide_.

## Charges incurred by storage services

When you're minimizing costs for AWS resources, keep in mind that many services
might incur storage costs, such as Amazon RDS and Amazon S3. For more information about storage
pricing, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/") and [Amazon RDS pricing](https://aws.amazon.com/rds/pricing/ "https://aws.amazon.com/rds/pricing/").

## Charges incurred for AWS Organizations that use billing transfer

When you sign in as a bill transfer account, you are responsible for paying charges for AWS Organizations that transfer their bills to you.

## Contacting Support

The above is not an exhaustive list of all the reasons why you might see unexpected
charges in your AWS account. If you receive charges that aren't due to any of the
reasons listed on this page, see [Contacting Support](billing-get-answers.md#billing-support "billing-get-answers.md#billing-support").
