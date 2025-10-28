# Release: Elastic Beanstalk adds support to opt out environment from default EC2 security group on

April 30, 2025

AWS Elastic Beanstalk added support to opt out environment from default EC2 security group.

**Release date:** April 30, 2025

## Changes

When you create an environment, Elastic Beanstalk assigns a default security group to the EC2
instances that are launched with it. The security group acts as a virtual firewall,
determining which traffic is allowed to reach and exit all of the EC2 instances. With this
release, the default security group that Elastic Beanstalk assigns to your EC2 instances is optional. You
can choose to disable it and assign new custom security groups for both new and existing
environments.

You can select to opt out your environment from the default EC2 security group by setting
the `DisableDefaultEC2SecurityGroup` option in the
`aws:autoscaling:launchconfiguration` namespace to `true`. You can use
the AWS CLI or configuration files to update this option and to attach custom security groups to
your environment's EC2 instances.

For more information, see [Managing EC2
security groups](../dg/using-features.managing.ec2.instances.md "../dg/using-features.managing.ec2.instances.md") in the _AWS Elastic Beanstalk Developer Guide_.
