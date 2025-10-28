# Release: Elastic Beanstalk adds support for IMDSv2 on June 10, 2020

AWS Elastic Beanstalk added support for Instance Metadata Service Version 2 (IMDSv2) on Amazon Linux 2 platforms.

**Release date:** June 10, 2020

## Changes

Amazon Elastic Compute Cloud (Amazon EC2) instances in your Elastic Beanstalk environments use the instance metadata service (IMDS), an on-instance component, to securely access
instance metadata. IMDS supports two methods for accessing data: IMDSv1 and IMDSv2. IMDSv2 uses session-oriented requests and mitigates several types of
vulnerabilities that could be used to try to access the IMDS. For details about IMDSv2's advantages, see [enhancements to
add defense in depth to the EC2 Instance Metadata Service](https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/ "https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/").

Today we're announcing the support of IMDSv2 on all Elastic Beanstalk platform versions based on Amazon Linux 2. These platform versions still support IMDSv1. However,
IMDSv2 is more secure, so it's a good idea to enforce the use of IMDSv2 on your environment instances. To enforce IMDSv2, ensure that all components of
your application support IMDSv2, and then disable IMDSv1. For more information, see [Configuring
the instance metadata service on your environment's instances](../dg/environments-cfg-ec2-imds.md "../dg/environments-cfg-ec2-imds.md"). For Amazon Linux 2 migration information, see [Migrating your Elastic Beanstalk Linux application to Amazon Linux 2](../dg/using-features.md "../dg/using-features.md").

###### Note

Disabling IMDSv1 requires using Amazon EC2 launch templates. When you enable a feature that depends on Amazon EC2 launch templates during environment creation
or updates, Elastic Beanstalk attempts to configure your environment to use Amazon EC2 launch templates (if the environment isn't using them already). In this case, if
your user policy lacks the necessary permissions, environment creation or updates might fail. Therefore, we recommend that you use our managed user
policy or add the required permissions to your custom policies. For details about the required permissions, see [Creating a Custom User Policy](../dg/AWSHowTo.iam.md#AWSHowTo.iam.policies "../dg/AWSHowTo.iam.md#AWSHowTo.iam.policies") in the
_AWS Elastic Beanstalk Developer Guide_.
