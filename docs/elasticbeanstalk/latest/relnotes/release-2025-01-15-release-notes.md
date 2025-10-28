# Release: Elastic Beanstalk adds support for Spot Allocation Strategy configuration during environment creation on January 15, 2025

AWS Elastic Beanstalk adds support for Spot Allocation Strategy configuration during environment creation.

**Release date:** January 15, 2025

## Changes

When your environment uses multiple instance types, Amazon EC2 Auto Scaling fulfills your On-Demand and Spot capacities from the possible instance types, following
an allocation strategy.

Elastic Beanstalk now offers the ability to choose a _Spot Allocation Strategy_ during environment creation. Use the Elastic Beanstalk console, namespace
configuration options, or the AWS CLI, to configure the Spot Instance allocation strategy for your environment.

For more information, see [Spot
Instance allocation strategy](../dg/environments-cfg-autoscaling-spot-allocation-strategy.md "../dg/environments-cfg-autoscaling-spot-allocation-strategy.md") in the _AWS Elastic Beanstalk Developer Guide_.
