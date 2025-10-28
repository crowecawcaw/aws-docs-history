# Elastic Beanstalk Linux platforms

The Elastic Beanstalk Linux platforms provide an extensive amount of functionality out of the box. You can extend the platforms in several ways to support your application. For
details, see [Extending Elastic Beanstalk Linux platforms](platforms-linux-extend.md "platforms-linux-extend.md").

Most of the platforms that Elastic Beanstalk supports are based on the Linux operating system. Specifically, these platforms are based on Amazon Linux, a Linux distribution
provided by AWS. Elastic Beanstalk Linux platforms use Amazon Elastic Compute Cloud (Amazon EC2) instances, and these instances run Amazon Linux.

###### Topics

- [Supported Amazon Linux versions](#platforms-linux.versions "#platforms-linux.versions")
- [List of Elastic Beanstalk Linux platforms](#platforms-linux.list "#platforms-linux.list")
- [Instance deployment workflow](platforms-linux-extend.md "platforms-linux-extend.md")
- [Instance deployment workflow for ECS running on Amazon Linux 2 and later](platforms-linux-extend.workflow.md "platforms-linux-extend.workflow.md")
- [Platform script tools for your Elastic Beanstalk environments](custom-platforms-scripts.md "custom-platforms-scripts.md")

## Supported Amazon Linux versions

AWS Elastic Beanstalk supports platforms based on Amazon Linux 2 and Amazon Linux 2023.

For more information about Amazon Linux 2 and Amazon Linux 2023, see the following:

- Amazon Linux 2 – [Amazon Linux](../../../AWSEC2/latest/UserGuide/amazon-linux-ami-basics.md "../../../AWSEC2/latest/UserGuide/amazon-linux-ami-basics.md") in the
  _Amazon EC2 User Guide_.
- Amazon Linux 2023 – [What is Amazon
  Linux 2023?](../../../linux/al2023/ug/what-is-amazon-linux.md "../../../linux/al2023/ug/what-is-amazon-linux.md") in the _Amazon Linux 2023 User Guide_

For details about supported platform versions, see [Elastic Beanstalk supported platforms](concepts.md "concepts.md").

###### Note

You can migrate your application from an Elastic Beanstalk AL1 or AL2 platform branch to the equivalent AL2023 platform branch.
For more information, see [Migrating your Elastic Beanstalk Linux application to Amazon Linux 2023 or Amazon Linux 2](using-features.md "using-features.md").

### Amazon Linux 2023

AWS announced the [general
availability](https://aws.amazon.com/blogs/aws/amazon-linux-2023-a-cloud-optimized-linux-distribution-with-long-term-support/ "https://aws.amazon.com/blogs/aws/amazon-linux-2023-a-cloud-optimized-linux-distribution-with-long-term-support/") of Amazon Linux 2023 in March of 2023. The _Amazon Linux 2023 User Guide_ summarizes key differences between
Amazon Linux 2 and Amazon Linux 2023. For more information, see [Comparing
Amazon Linux 2 and Amazon Linux 2023](../../../linux/al2023/ug/compare-with-al2.md "../../../linux/al2023/ug/compare-with-al2.md") in the user guide.

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

## List of Elastic Beanstalk Linux platforms

The following list provides the Linux platforms that Elastic Beanstalk supports for different programming languages as well as for Docker containers.
Elastic Beanstalk offers platforms based on Amazon Linux 2 and Amazon Linux 2023 for all of them. To learn more about a platform, select the corresponding link.

- [Docker (and ECS Docker)](create_deploy_docker.md "create_deploy_docker.md")
- [Go](create_deploy_go.md "create_deploy_go.md")
- [Tomcat (running Java SE)](create_deploy_Java.md "create_deploy_Java.md")
- [Java SE](create_deploy_Java.md "create_deploy_Java.md")
- [.NET Core on Linux](create-deploy-dotnet-core-linux.md "create-deploy-dotnet-core-linux.md")
- [Node.js](create_deploy_nodejs.md "create_deploy_nodejs.md")
- [PHP](create_deploy_PHP_eb.md "create_deploy_PHP_eb.md")
- [Python](create-deploy-python-apps.md "create-deploy-python-apps.md")
- [Ruby](create_deploy_Ruby.md "create_deploy_Ruby.md")
