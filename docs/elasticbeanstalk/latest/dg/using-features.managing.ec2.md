# Amazon EC2 instance types

This topic explains the term _instance type_. When you create a new environment, Elastic Beanstalk provisions Amazon EC2 instances that are based on
the Amazon EC2 _instance types_ that you choose. The instance types that you choose determine the host hardware that runs your instances.
EC2 instance types can be categorized by which processor architecture each is based on. Elastic Beanstalk supports instance types based on the following processor
architectures: AWS Graviton 64-bit Arm architecture (arm64), 64-bit architecture (x86), and 32-bit architecture (i386). Elastic Beanstalk selects the x86 processor
architecture by default when you create a new environment.

###### Note

The i386 32-bit architecture is no longer supported by the majority of Elastic Beanstalk platforms. We recommended that you choose the x86 or arm64 architecture
types instead. Elastic Beanstalk provides [configuration options](command-options.md "command-options.md") for i386 processor instance types in the [aws:ec2:instances](command-options-general.md#command-options-general-ec2instances "command-options-general.md#command-options-general-ec2instances") namespace.

All of the instance types in the configuration for a given Elastic Beanstalk environment must have the same type of processor architecture. Assume that you add a
new instance type to an existing environment that already has a t2.medium instance type, which is based on x86 architecture. You can only add another
instance type of the same architecture, such as t2.small. If you want to replace the existing instance types with those from a different architecture, you
can do so. But make sure that all of the instance types in the command are based on the same type of architecture.

Elastic Beanstalk regularly adds support for new compatible instance types after Amazon EC2 introduces them. For information about instance types that are available,
see
[Instance types](../../../AWSEC2/latest/UserGuide/instance-types.md "../../../AWSEC2/latest/UserGuide/instance-types.md")
in the _Amazon EC2 User Guide_.

###### Note

Elastic Beanstalk now offers support for Graviton on all of the latest Amazon Linux 2 platforms across all AWS Graviton supported Regions. For more information about
creating an Elastic Beanstalk environment with arm64 based instances types, see [Configuring Amazon EC2 instances using the Elastic Beanstalk console](using-features.managing.ec2.md "using-features.managing.ec2.md").

Create new environments that run Amazon EC2 instances on arm64 architecture and migrate your existing applications to them with the [deployment options](using-features.md "using-features.md") in Elastic Beanstalk.

To learn more about Graviton arm64 based processors, see these AWS resources:

- Benefits — [The AWS Graviton Processor](https://aws.amazon.com/ec2/graviton/ "https://aws.amazon.com/ec2/graviton/")
- _Getting started_ and other topics, such as _Language-specific considerations_ — [Getting started with AWS Graviton](https://github.com/aws/aws-graviton-getting-started#getting-started-with-aws-graviton "https://github.com/aws/aws-graviton-getting-started#getting-started-with-aws-graviton") GitHub
  article
