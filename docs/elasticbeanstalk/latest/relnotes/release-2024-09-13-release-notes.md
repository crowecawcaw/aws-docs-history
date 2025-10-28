# Release: Elastic Beanstalk increases the number of instance types you can choose for an environment on September 13, 2024

AWS Elastic Beanstalk increased the number of instance types you can choose for an environment from 10 to 40.

**Release date:** September 13, 2024

## Changes

When you create an environment, Elastic Beanstalk provisions Amazon EC2 instances that are based on the Amazon EC2 _instance types_ that
you specify in the configuration. The instance types are based on different processor architectures, and they determine the host hardware that runs your
instances.

Elastic Beanstalk has increased the number of different instance types that you can specify for your environment to use. Previously you could select up to ten
different instance types. Now you can specify up to forty different instance types.

You provide the list of EC2 instance types for your environment in the `InstanceTypes` option of the `aws:ec2:instances`
namespace. For more information, see the following sections in the _AWS Elastic Beanstalk Developer Guide_: [Configuring AWS EC2 instances](../dg/using-features.managing.md#using-features.managing.ec2.aws-cli "../dg/using-features.managing.md#using-features.managing.ec2.aws-cli") and [aws:ec2:instances
namespace](../dg/command-options-general.md#command-options-general-ec2instances "../dg/command-options-general.md#command-options-general-ec2instances").
