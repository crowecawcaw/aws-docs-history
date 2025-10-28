# Release: Elastic Beanstalk supports AWS Graviton instance types based on 64-bit Arm architecture on November 24, 2021

AWS Elastic Beanstalk supports AWS Graviton instance types based on 64-bit Arm architecture.

**Release date:** November 24, 2021

## Changes

Elastic Beanstalk now offers support for Graviton on all of the latest Amazon Linux 2 platforms across all AWS Graviton supported Regions. AWS Graviton is an arm64
processor that offers up to 40% better price-performance over comparable x86 based processors.

With this release Elastic Beanstalk provides support for Graviton arm64 architecture from the console, EB CLI and AWS CLI. For more information, see [Configuring Amazon EC2 instances
for your environment](../dg/using-features.managing.md#using-features.managing.ec2.console "../dg/using-features.managing.md#using-features.managing.ec2.console") in the _AWS Elastic Beanstalk Developer Guide_.

To learn more about Graviton arm64 processor architecture, see [The AWS Graviton Processor](https://aws.amazon.com/ec2/graviton/ "https://aws.amazon.com/ec2/graviton/")
website and [Getting started with AWS Graviton](https://github.com/aws/aws-graviton-getting-started#getting-started-with-aws-graviton "https://github.com/aws/aws-graviton-getting-started#getting-started-with-aws-graviton")
in the AWS GitHub repository.

###### Note

If you created environments with the custom AMIs provided in the Graviton first wave releases, we recommend that you remove the custom AMIs and
upgrade your Graviton arm64 based environments to the latest platform version. For more information, see [Recommendations for Graviton arm64 first
wave environments](../dg/using-features.managing.md#using-features.managing.ec2.graviton-wave-1 "../dg/using-features.managing.md#using-features.managing.ec2.graviton-wave-1") in the _AWS Elastic Beanstalk Developer Guide_.
