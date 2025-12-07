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
availability](https://aws.amazon.com//blogs/aws/amazon-linux-2023-a-cloud-optimized-linux-distribution-with-long-term-support/ "https://aws.amazon.com//blogs/aws/amazon-linux-2023-a-cloud-optimized-linux-distribution-with-long-term-support/") of Amazon Linux 2023 in March of 2023. The _Amazon Linux 2023 User Guide_ summarizes key differences between
Amazon Linux 2 and Amazon Linux 2023. For more information, see [Comparing
Amazon Linux 2 and Amazon Linux 2023](../../../linux/al2023/ug/compare-with-al2.md "../../../linux/al2023/ug/compare-with-al2.md") in the user guide.

There is a high degree of compatibility between Elastic Beanstalk Amazon Linux 2 and Amazon Linux 2023 platforms.
Although there are some differences to note:

- Instance Metadata Service Version 1 (IMDSv1) – The
  [DisableIMDSv1](command-options-general.md#command-options-general-autoscalinglaunchconfiguration "command-options-general.md#command-options-general-autoscalinglaunchconfiguration") option setting defaults to `true` on AL2023
  platforms. The default is `false` on AL2 platforms.
- pkg-repo instance tool – The [pkg-repo](custom-platforms-scripts.md#custom-platforms-scripts.pkg-repo "custom-platforms-scripts.md#custom-platforms-scripts.pkg-repo") tool is not available for environments
  running on AL2023 platforms. However, you can still manually apply package and operating system
  updates to an AL2023 instance. For more information, see [Managing packages and operating
  system updates](../../../linux/al2023/ug/managing-repos-os-updates.md "../../../linux/al2023/ug/managing-repos-os-updates.md") in the _Amazon Linux 2023 User Guide_.
- Apache HTTPd configuration – The Apache
  `httpd.conf` file for AL2023 platforms has some configuration settings
  that are different from those for AL2:

      + Deny access to the server’s entire file system by default. These settings are
       described in *Protect Server Files by Default* on the Apache website
       [Security
       Tips](https://httpd.apache.org/docs/2.4/misc/security_tips.html "https://httpd.apache.org/docs/2.4/misc/security_tips.html") page.
      + Deny access to set up of `.htaccess` in all directories, except for
       those specifically enabled. This setting is described in *Protecting System
       Settings* on the Apache website [Security Tips](https://httpd.apache.org/docs/2.4/misc/security_tips.html "https://httpd.apache.org/docs/2.4/misc/security_tips.html")
       page. The [Apache HTTP
       Server Tutorial: .htaccess files](https://httpd.apache.org/docs/2.4/howto/htaccess.html "https://httpd.apache.org/docs/2.4/howto/htaccess.html")  page states this setting may help improve
       performance.
      + Deny access to files with name pattern `.ht*`. This setting
       prevents web clients from viewing `.htaccess` and
       `.htpasswd` files.

  You can change any of the above configuration settings for your environment. For more
  information, see [Configuring Apache HTTPD](platforms-linux-extend.md#platforms-linux-extend.proxy.httpd "platforms-linux-extend.md#platforms-linux-extend.proxy.httpd").

- Multiline environment variable support – AL2023 platforms
  support multiline values for environment variables and secrets in systemd service
  configurations. Amazon Linux 2 platforms do not support multiline environment variable values. This
  enhancement allows you to use multiline secrets and configuration values on AL2023
  platforms. For more information about using environment variables and secrets, see [Multiline values in Amazon Linux 2 environment variables](AWSHowTo.secrets.md#AWSHowTo.secrets.multiline "AWSHowTo.secrets.md#AWSHowTo.secrets.multiline").
- CloudWatch custom log forwarding – The deprecated
  CloudWatch Logs agent (`awslogs` package) is not available on AL2023
  platforms. If you have custom log forwarding configurations that install and use the
  deprecated `awslogs` agent, you must update your configuration files to
  use the unified CloudWatch agent when migrating from Amazon Linux 2 to AL2023. For more
  information, see [Custom log file streaming](AWSHowTo.md#AWSHowTo.cloudwatchlogs.streaming.custom "AWSHowTo.md#AWSHowTo.cloudwatchlogs.streaming.custom").

Platform-specific differences

In addition to the base operating system differences, there are platform-specific differences
between Amazon Linux 2 and AL2023 runtime platforms:

- .NET platform branching – The .NET platform
  branching strategy differs between Amazon Linux 2 and AL2023. On Amazon Linux 2, the .NET Core platform
  maintains a rotating window of .NET major versions within a single platform branch. On
  AL2023, each platform branch is pinned to a specific .NET major version (for example, .NET
  9, .NET 10).

If you deploy framework-dependent applications (applications that rely on the platform's
installed .NET runtime), you must select a platform branch that matches your application's
target .NET version. If you deploy self-contained applications (applications that bundle
their own .NET runtime), you can use any AL2023 .NET platform branch regardless of your
application's .NET version, as your application is not dependent on the platform's installed
runtime. For more information, see [Bundling applications for the .NET Core on Linux Elastic Beanstalk platform](dotnet-linux-platform-bundle-app.md "dotnet-linux-platform-bundle-app.md").

- Node.js version selection – The Node.js platform
  on Amazon Linux 2 supports specifying a Node.js version in your application's
  `package.json` file. The Node.js platform on AL2023 does not support
  this feature. You must use the default Node.js version provided by the platform branch. For
  more information about Node.js version management, see [Configuring your application's dependencies on Elastic Beanstalk](nodejs-platform-dependencies.md "nodejs-platform-dependencies.md").
- Ruby Puma server version – The Ruby platform on
  Amazon Linux 2 ignores the Puma version specified in your application's
  `Gemfile.lock` file and uses the platform default Puma version. The Ruby
  platform on AL2023 honors the Puma version specified in `Gemfile.lock`
  if present. If no version is specified, the platform installs the platform default Puma
  version.
- PHP package availability – Some packages available
  on Amazon Linux 2 PHP platforms are not available on AL2023 PHP platforms:
  - _MySQL client packages_ – The `mysql`
    and `mysql-devel` command-line client packages are not installed on
    AL2023 PHP platforms. If your application requires MySQL database connectivity, use the
    PHP `mysqli` or `pdo_mysql` extensions, which are
    available on both platforms.
  - _Compass and Ruby tools_ – The `ruby-devel`
    and `rubygems` packages for Compass CSS framework support are not
    installed on AL2023 PHP platforms. Compass has been deprecated. Consider using modern
    CSS preprocessing tools as alternatives.

- Go version control tools – The Bazaar version
  control system (`bzr`) is not available on AL2023 Go platforms. Bazaar
  is deprecated and not included in the AL2023 package repository. Use Git, Mercurial, or
  Subversion for version control instead, all of which are available on AL2023 Go
  platforms.

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
