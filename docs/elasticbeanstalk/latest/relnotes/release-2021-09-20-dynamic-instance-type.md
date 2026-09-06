

# Release: Elastic Beanstalk added support for dynamic instance type selection on September 20, 2021
<a name="release-2021-09-20-dynamic-instance-type"></a>

AWS Elastic Beanstalk added support for dynamic instance type selection.

**Release date:** September 20, 2021

## Changes
<a name="release-2021-09-20-dynamic-instance-type.changes"></a>

When you create or configure an Elastic Beanstalk environment, you choose an instance type to determine the hardware of the host computer that's used to run your instances.

Elastic Beanstalk now supports dynamic instance type selection. This means it will automatically fetch compatible instance types after Amazon EC2 introduces them. For example, if you’re running an application with a compute-intensive workload, you can optimize performance by selecting an accelerated computing instance types such as p3 or p4d.

You can learn more about instance types supported by Elastic Beanstalk and configuring your Elastic Beanstalk environments with Amazon EC2 instances. For more information, see [Your Elastic Beanstalk environment's Amazon EC2 instances](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.managing.ec2.html) in the *AWS Elastic Beanstalk Developer Guide*.