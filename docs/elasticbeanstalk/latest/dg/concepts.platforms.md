# Elastic Beanstalk supported platforms

AWS Elastic Beanstalk provides a variety of platforms on which you can build your applications. You design your web application to one of these platforms,
and Elastic Beanstalk deploys your code to the platform version you selected to create an active application environment.

Elastic Beanstalk provisions the resources needed to run your application, including one or more Amazon EC2 instances. The software stack running on the Amazon EC2 instances
depends on the specific platform version you've selected for your environment.

###### The solution stack name for a platform branch

You can use the _solution stack name_ for a given platform branch version to launch an environment with the [EB CLI](eb-cli3.md "eb-cli3.md"), [Elastic Beanstalk API](../api.md "../api.md"), or the [AWS CLI](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/"). The
_AWS Elastic Beanstalk Platforms_ guide lists the _solution stack name_ under the platform branch version in
both the [Elastic Beanstalk Supported Platforms](../platforms/platforms-supported.md "../platforms/platforms-supported.md") and [Platform history](../platforms/platform-history.md "../platforms/platform-history.md") sections.

To retrieve all of the solution stack names that you can use to create an environment, use the [ListAvailableSolutionStacks](../api/API_ListAvailableSolutionStacks.md "../api/API_ListAvailableSolutionStacks.md") API or the [`aws elasticbeanstalk list-available-solution-stacks`](../../../cli/latest/reference/elasticbeanstalk/list-available-solution-stacks.md "../../../cli/latest/reference/elasticbeanstalk/list-available-solution-stacks.md") in the
AWS CLI.

You can customize and configure the software that your application depends on in your platform. Learn more at [Customizing software on Linux servers](customize-containers-ec2.md "customize-containers-ec2.md") and [Customizing software on Windows servers](customize-containers-windows-ec2.md "customize-containers-windows-ec2.md").
Detailed release notes are available for recent releases at [AWS Elastic Beanstalk Release Notes](../relnotes.md "../relnotes.md").

## Supported platforms and component history

The _AWS Elastic Beanstalk Platforms_ guide lists all of the current platform branch versions in the [Elastic Beanstalk Supported Platforms](../platforms/platforms-supported.md "../platforms/platforms-supported.md") section. The _Platforms_ guide also
lists a _platform history_ for each platform, which includes a list of previous branch platform versions. To view the
_platform history_ for each platform, select one of the following links.

- [Docker](../platforms/platform-history-docker.md "../platforms/platform-history-docker.md")
- [Go](../platforms/platform-history-go.md "../platforms/platform-history-go.md")
- [Java SE](../platforms/platform-history-javase.md "../platforms/platform-history-javase.md")
- [Tomcat (running Java SE)](../platforms/platform-history-java.md "../platforms/platform-history-java.md")
- [.NET Core on Linux](../platforms/platform-history-dotnetlinux.md "../platforms/platform-history-dotnetlinux.md")
- [.NET on Windows Server](../platforms/platform-history-dotnet.md "../platforms/platform-history-dotnet.md")
- [Node.js](../platforms/platform-history-nodejs.md "../platforms/platform-history-nodejs.md")
- [PHP](../platforms/platform-history-php.md "../platforms/platform-history-php.md")
- [Python](../platforms/platform-history-python.md "../platforms/platform-history-python.md")
- [Ruby](../platforms/platform-history-ruby.md "../platforms/platform-history-ruby.md")
