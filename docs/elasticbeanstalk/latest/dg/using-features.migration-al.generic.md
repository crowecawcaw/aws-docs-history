# Migration from Amazon Linux 2 to Amazon Linux 2023

This topic provides guidance to migrate your application from an Amazon Linux 2 platform branch to an Amazon Linux 2023 platform branch.

## Differences and compatibility

###### Between the Elastic Beanstalk AL2 and AL2023 platforms

There is a high degree of compatibility between Elastic Beanstalk Amazon Linux 2 and Amazon Linux 2023 platforms.
Although there are some differences to note:

- Instance Metadata Service Version 1 (IMDSv1) – The
  [DisableIMDSv1](command-options-general.md#command-options-general-autoscalinglaunchconfiguration "command-options-general.md#command-options-general-autoscalinglaunchconfiguration") option setting defaults to `true` on AL2023
  platforms. The default is `false` on AL2 platforms.
- pkg-repo instance tool – The [pkg-repo](custom-platforms-scripts.md#custom-platforms-scripts.pkg-repo "custom-platforms-scripts.md#custom-platforms-scripts.pkg-repo") tool is not available for environments
  running on AL2023 platforms. However,you can manually apply package and operating system
  updates to an AL2023 instance. For more information, see [Managing packages and operating
  system updates](../../../linux/al2023/ug/managing-repos-os-updates.md "../../../linux/al2023/ug/managing-repos-os-updates.md") in the _Amazon Linux 2023 User Guide_.
- Apache HTTPd configuration – The Apache
  `httpd.conf` file for AL2023 platforms has some configuration settings
  that are different from those for AL2:
  - Deny access to the server’s entire file system by default. These settings are
    described in _Protect Server Files by Default_ on the Apache website
    [Security
    Tips](https://httpd.apache.org/docs/2.4/misc/security_tips.html "https://httpd.apache.org/docs/2.4/misc/security_tips.html") page.
  - Stop users from overriding security features you've configured. The configuration
    denies access to set up of `.htaccess` in all directories, except for
    those specifically enabled. This setting is described in _Protecting System
    Settings_ on the Apache website [Security Tips](https://httpd.apache.org/docs/2.4/misc/security_tips.html "https://httpd.apache.org/docs/2.4/misc/security_tips.html")
    page. The [Apache HTTP
    Server Tutorial: .htaccess files](https://httpd.apache.org/docs/2.4/howto/htaccess.html "https://httpd.apache.org/docs/2.4/howto/htaccess.html") page states this setting may help improve
    performance.
  - Deny access to files with name pattern `.ht*`. This setting
    prevents web clients from viewing `.htaccess` and
    `.htpasswd` files.

You can change any of the above configuration settings for your environment. For more
information, see [Configuring Apache HTTPD](platforms-linux-extend.md#platforms-linux-extend.proxy.httpd "platforms-linux-extend.md#platforms-linux-extend.proxy.httpd").

###### Between the Amazon Linux operating systems

For more information about the differences between the Amazon Linux 2 and Amazon Linux 2023 operating systems, see [Comparing Amazon Linux 2 and Amazon Linux 2023](../../../linux/al2023/ug/compare-with-al2.md "../../../linux/al2023/ug/compare-with-al2.md") in the _Amazon Linux 2023 User Guide_.

For more information about Amazon Linux 2023, see [What is Amazon Linux
2023?](../../../linux/al2023/ug/what-is-amazon-linux.md "../../../linux/al2023/ug/what-is-amazon-linux.md") in the _Amazon Linux 2023 User Guide_.

## General migration process

When you're ready to go to production, Elastic Beanstalk requires a blue/green deployment to perform the upgrade. The following are the general best practice
steps that we recommend for migration with a blue/green deployment procedure.

###### Preparing to test for your migration

Before you deploy your application and start testing, review the information in the prior section [Differences and compatibility](#using-features.migration-al.generic.from-al2.differences "#using-features.migration-al.generic.from-al2.differences"). Also
review the reference cited in that section, [Comparing
Amazon Linux 2 and Amazon Linux 2023](../../../linux/al2023/ug/compare-with-al2.md "../../../linux/al2023/ug/compare-with-al2.md") in the _Amazon Linux 2023 User Guide_. Make a note of the specific information from this content that
applies or may apply to your application and configuration set up.

###### High level migration steps

1. Create a new environment that's based on an AL2023 platform branch.
2. Deploy your application to the target AL2023 environment.

Your existing production environment will remain active and unaffected, while you iterate through testing and making adjustments to the new
environment. 3. Test your application thoroughly in the new environment. 4. When your destination AL2023 environment is ready to go to production, swap the CNAMEs of the two environments to redirect traffic to the new
AL2023 environment.

###### More detailed migration steps and best practices

For a more detailed blue/green deployment procedure, see [Blue/Green deployments with Elastic Beanstalk](using-features.md "using-features.md").

For more specific guidance and detailed best practice steps, see [Blue/Green
method](using-features.platform.md#using-features.platform.upgrade.bluegreen "using-features.platform.md#using-features.platform.upgrade.bluegreen").

## More references to help plan your migration

The following references can offer additional information to plan your migration.

- [Elastic Beanstalk supported platforms](../platforms/platforms-supported.md "../platforms/platforms-supported.md") in
  _AWS Elastic Beanstalk Platforms_
- [Retired platform branch history](platforms-schedule.md#platforms-support-policy.retired "platforms-schedule.md#platforms-support-policy.retired")
- [Elastic Beanstalk Linux platforms](platforms-linux.md "platforms-linux.md")
- [Platform retirement FAQ](using-features.migration-al.md "using-features.migration-al.md")
