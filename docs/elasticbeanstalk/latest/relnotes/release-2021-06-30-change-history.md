# Release: Elastic Beanstalk adds support for Amazon EBS gp3 volumes on June 30, 2021

AWS Elastic Beanstalk added support for Amazon Elastic Block Store (Amazon EBS) gp3 volumes.

**Release date:** June 30, 2021

## Changes

In December 2020, AWS announced the upcoming availability of gp3 storage volumes, which is the next-generation general purpose SSD storage volumes
for Amazon Elastic Block Store (Amazon EBS). Today we’re announcing that Elastic Beanstalk now also supports gp3 storage volumes. Starting now you can configure your Elastic Beanstalk instances to
provision gp3 storage volumes to take advantage of all that gp3 has to offer. This includes the following features:

- Independently provision IOPS and throughput, separate from storage capacity.
- Scale performance for transaction-intensive workloads that eliminates the need to provision more capacity.
- Offered at a price-point that’s 20 % lower per GB than existing gp2 volumes.

You can migrate your existing gp2 volumes to gp3 volumes using Elastic Volumes, which is an existing feature of Amazon EBS. For more information, see the
[gp3 announcement](https://aws.amazon.com/blogs/aws/new-amazon-ebs-gp3-volume-lets-you-provision-performance-separate-from-capacity-and-offers-20-lower-price/ "https://aws.amazon.com/blogs/aws/new-amazon-ebs-gp3-volume-lets-you-provision-performance-separate-from-capacity-and-offers-20-lower-price/")

on the AWS News blog and the [Amazon EBS product overview page](https://aws.amazon.com/ebs/general-purpose/ "https://aws.amazon.com/ebs/general-purpose/").

You can configure your Amazon EC2 instances that are running on Elastic Beanstalk platforms to use gp3 storage volumes directly in the Elastic Beanstalk Console. You can also
configure your Elastic Beanstalk environments to use gp3 storage volumes by using the EB CLI or the

`aws:autoscaling:launchconfiguration` namespace configuration option. For more information, see [Configuring your environment's Amazon EC2 instances](../dg/using-features.managing.md#using-features.managing.ec2.console "../dg/using-features.managing.md#using-features.managing.ec2.console") in the _AWS Elastic Beanstalk Developer Guide_.
