# Release: Elastic Beanstalk adds support for Spot Instance requests on November 25, 2019

AWS Elastic Beanstalk added support for Amazon Elastic Compute Cloud (Amazon EC2) Spot Instance requests.

**Release date:** November 25, 2019

## Changes

So far you were able to use Amazon EC2 On-Demand and Reserved Instances in your Elastic Beanstalk environments.

Starting with this release, Elastic Beanstalk also supports Amazon EC2 _Spot Instances_. These are unused Amazon EC2 instances that are available for you
at steep discounts. When you enable Spot for your environment, Elastic Beanstalk combines On-Demand and Spot
Instances, using criteria that you provide.

For more information about Spot Instances, see [Spot Instances](../../../AWSEC2/latest/UserGuide/using-spot-instances.md "../../../AWSEC2/latest/UserGuide/using-spot-instances.md") in the
_Amazon EC2 User Guide_. For more information about Spot support in Elastic Beanstalk, see [Auto Scaling Group for Your Elastic Beanstalk Environment](../dg/using-features.managing.md "../dg/using-features.managing.md") in the _AWS Elastic Beanstalk Developer Guide_.
