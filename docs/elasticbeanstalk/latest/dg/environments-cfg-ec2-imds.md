# Configuring the IMDS on your Elastic Beanstalk environment's instances

This topic describes the Instance Metadata Service (IMDS).

_Instance metadata_ is data that's related to an Amazon Elastic Compute Cloud (Amazon EC2) instance that applications can use to configure or manage the
running instance. The instance metadata service (IMDS) is an on-instance component that code on the instance uses to securely access instance metadata. This
code can be Elastic Beanstalk platform code on your environment instances, the AWS SDK that your application might be using, or even your application's own code. For
more information, see [Instance metadata and user data](../../../AWSEC2/latest/UserGuide/ec2-instance-metadata.md "../../../AWSEC2/latest/UserGuide/ec2-instance-metadata.md") in the
_Amazon EC2 User Guide_.

Code can access instance metadata from a running instance using one of two methods: Instance Metadata Service Version 1 (IMDSv1) or Instance Metadata
Service Version 2 (IMDSv2). IMDSv2 uses session-oriented requests and mitigates several types of vulnerabilities that could be used to try to access the
IMDS. For information about these two methods, see [Configuring the instance metadata
service](../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-service.md "../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-service.md") in the _Amazon EC2 User Guide_.

###### Topics

- [Platform support for IMDS](#environments-cfg-ec2-imds.plat "#environments-cfg-ec2-imds.plat")
- [Choosing IMDS methods](#environments-cfg-ec2-imds.choose "#environments-cfg-ec2-imds.choose")
- [Configuring IMDS using the Elastic Beanstalk console](#environments-cfg-ec2-imds.console "#environments-cfg-ec2-imds.console")
- [The aws:autoscaling:launchconfiguration namespace](#environments-cfg-ec2-imds.namespace "#environments-cfg-ec2-imds.namespace")

## Platform support for IMDS

Elastic Beanstalk platforms running on Amazon Linux 2 and Amazon Linux 2023 and Windows server all support both IMDSv1 and IMDSv2. For more information, see [Configuring IMDS using the Elastic Beanstalk console](#environments-cfg-ec2-imds.console "#environments-cfg-ec2-imds.console")

## Choosing IMDS methods

When making a decision about the IMDS methods that you want your environment to support, consider the following use cases:

- _AWS SDK_ – If your application uses an AWS SDK, make sure you use an the latest version of the SDK. The AWS SDKs
  make IMDS calls, and newer SDK versions use IMDSv2 whenever possible. If you ever disable IMDSv1, or if your application uses an old SDK version, IMDS
  calls might fail.
- _Your application code_ – If your application makes IMDS calls, consider using the AWS SDK so that you can make the
  calls instead of making direct HTTP requests. This way, you don't need to make code changes to switch between IMDS methods. The AWS SDK uses IMDSv2
  whenever possible.
- _Elastic Beanstalk platform code_ – Our code makes IMDS calls through the AWS SDK, and therefore uses IMDSv2 on all supporting
  platform versions. If your code uses an up-to-date AWS SDK and makes all IMDS calls through the SDK, you can safely disable IMDSv1.

## Configuring IMDS using the Elastic Beanstalk console

You can modify your Elastic Beanstalk environment's Amazon EC2 instance configuration in the Elastic Beanstalk console.

###### Important

The `DisableIMDSv1`
option setting can cause Elastic Beanstalk to migrate an existing environment with launch configurations to launch
templates. Doing so requires the necessary permissions to manage launch templates. These permissions are included in our managed policy. If you use custom
policies instead of our managed policies, environment creation or updates might fail when you update your environment
configuration. For more information
and other considerations, see [Migrating your Elastic Beanstalk
environment to launch templates](environments-cfg-autoscaling-launch-templates.md "environments-cfg-autoscaling-launch-templates.md") .

###### To configure IMDS on your Amazon EC2 instances in the Elastic Beanstalk console

1. Open the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk "https://console.aws.amazon.com/elasticbeanstalk"),
   and in the **Regions** list, select your AWS Region.
2. In the navigation pane, choose **Environments**, and then choose the name of your environment from the list.
3. In the navigation pane, choose **Configuration**.
4. In the **Instance traffic and scaling** configuration category, choose **Edit**.
5. Set **Disable IMDSv1** to enforce IMDSv2. Clear **Disable IMDSv1** to enable both IMDSv1 and IMDSv2.
6. To save the changes choose **Apply** at the bottom of the page.

## The aws:autoscaling:launchconfiguration namespace

You can use a [configuration option](command-options.md "command-options.md") in the `aws:autoscaling:launchconfiguration` namespace to configure IMDS on your
environment's instances.

###### Important

The `DisableIMDSv1`
option setting can cause Elastic Beanstalk to migrate an existing environment with launch configurations to launch
templates. Doing so requires the necessary permissions to manage launch templates. These permissions are included in our managed policy. If you use custom
policies instead of our managed policies, environment creation or updates might fail when you update your environment
configuration. For more information
and other considerations, see [Migrating your Elastic Beanstalk
environment to launch templates](environments-cfg-autoscaling-launch-templates.md "environments-cfg-autoscaling-launch-templates.md") .

The following [configuration file](ebextensions.md "ebextensions.md") example disables IMDSv1 using the `DisableIMDSv1` option.

```
option_settings:
  aws:autoscaling:launchconfiguration:
    DisableIMDSv1: true
```

Set **DisableIMDSv1** to `true` to disable IMDSv1 and enforce IMDSv2.

Set **DisableIMDSv1** to `false` to enable both IMDSv1 and IMDSv2.
