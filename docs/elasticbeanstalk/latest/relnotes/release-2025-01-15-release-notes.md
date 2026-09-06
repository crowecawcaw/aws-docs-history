

# Release: Elastic Beanstalk adds support for Spot Allocation Strategy configuration during environment creation on January 15, 2025
<a name="release-2025-01-15-release-notes"></a>

AWS Elastic Beanstalk adds support for Spot Allocation Strategy configuration during environment creation.

**Release date:** January 15, 2025

## Changes
<a name="release-2025-01-15-release-notes.changes"></a>

When your environment uses multiple instance types, Amazon EC2 Auto Scaling fulfills your On-Demand and Spot capacities from the possible instance types, following an allocation strategy.

Elastic Beanstalk now offers the ability to choose a *Spot Allocation Strategy* during environment creation. Use the Elastic Beanstalk console, namespace configuration options, or the AWS CLI, to configure the Spot Instance allocation strategy for your environment.

For more information, see [Spot Instance allocation strategy](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-cfg-autoscaling-spot-allocation-strategy.html) in the *AWS Elastic Beanstalk Developer Guide*.