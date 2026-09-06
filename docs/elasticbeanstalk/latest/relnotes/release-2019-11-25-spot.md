

# Release: Elastic Beanstalk adds support for Spot Instance requests on November 25, 2019
<a name="release-2019-11-25-spot"></a>

AWS Elastic Beanstalk added support for Amazon Elastic Compute Cloud (Amazon EC2) Spot Instance requests.

**Release date:** November 25, 2019

## Changes
<a name="release-2019-11-25-spot.changes"></a>

So far you were able to use Amazon EC2 On-Demand and Reserved Instances in your Elastic Beanstalk environments.

Starting with this release, Elastic Beanstalk also supports Amazon EC2 *Spot Instances*. These are unused Amazon EC2 instances that are available for you at steep discounts. When you enable Spot for your environment, Elastic Beanstalk combines On-Demand and Spot Instances, using criteria that you provide.

For more information about Spot Instances, see [Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html) in the *Amazon EC2 User Guide*. For more information about Spot support in Elastic Beanstalk, see [Auto Scaling Group for Your Elastic Beanstalk Environment](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.managing.as.html) in the *AWS Elastic Beanstalk Developer Guide*.