

# Release: Elastic Beanstalk supports AWS Graviton instance types based on 64-bit Arm architecture on November 24, 2021
<a name="release-2021-11-24-graviton-mvp"></a>

AWS Elastic Beanstalk supports AWS Graviton instance types based on 64-bit Arm architecture.

**Release date:** November 24, 2021

## Changes
<a name="release-2021-11-24-graviton-mvp.changes"></a>

Elastic Beanstalk now offers support for Graviton on all of the latest Amazon Linux 2 platforms across all AWS Graviton supported Regions. AWS Graviton is an arm64 processor that offers up to 40% better price-performance over comparable x86 based processors.

With this release Elastic Beanstalk provides support for Graviton arm64 architecture from the console, EB CLI and AWS CLI. For more information, see [Configuring Amazon EC2 instances for your environment](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.managing.ec2.html#using-features.managing.ec2.console) in the *AWS Elastic Beanstalk Developer Guide*. 

To learn more about Graviton arm64 processor architecture, see [The AWS Graviton Processor](https://aws.amazon.com/ec2/graviton/) website and [Getting started with AWS Graviton](https://github.com/aws/aws-graviton-getting-started#getting-started-with-aws-graviton) in the AWS GitHub repository.

**Note**  
If you created environments with the custom AMIs provided in the Graviton first wave releases, we recommend that you remove the custom AMIs and upgrade your Graviton arm64 based environments to the latest platform version. For more information, see [Recommendations for Graviton arm64 first wave environments](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.managing.ec2.html#using-features.managing.ec2.graviton-wave-1) in the *AWS Elastic Beanstalk Developer Guide*.