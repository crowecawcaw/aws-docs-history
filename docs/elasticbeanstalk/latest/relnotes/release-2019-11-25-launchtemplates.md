# Release: Elastic Beanstalk starts using Amazon EC2 launch templates on November 25, 2019

AWS Elastic Beanstalk started using Amazon Elastic Compute Cloud (Amazon EC2) launch templates to launch instances when necessary.

**Release date:** November 25, 2019

## Changes

Until now, the Amazon EC2 Auto Scaling group in your Elastic Beanstalk environment used a launch configuration attached to the group when it launched Amazon EC2 instances, for example,
during scaling actions or during deployments and updates.

Today we released support for [Spot Instances](release-2019-11-25-spot.md "release-2019-11-25-spot.md"), and enabling Spot Instances requires using Amazon EC2 launch
templates. In the future, additional features might depend on Amazon EC2 launch templates. When you enable such a feature during environment creation or
updates, Elastic Beanstalk attempts to configure your environment to use Amazon EC2 launch templates (if the environment isn't using them already). In this case, if your
user policy lacks the necessary permissions, environment creation or updates might fail. Therefore, we recommend that you use our managed user policy or
add the required permissions to your custom policies. For details about the required permissions, see [Creating a Custom User Policy](../dg/AWSHowTo.iam.md#AWSHowTo.iam.policies "../dg/AWSHowTo.iam.md#AWSHowTo.iam.policies") in the
_AWS Elastic Beanstalk Developer Guide_.
