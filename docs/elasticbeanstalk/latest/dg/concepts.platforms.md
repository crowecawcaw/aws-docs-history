

# Elastic Beanstalk supported platforms
<a name="concepts.platforms"></a>

AWS Elastic Beanstalk provides a variety of platforms on which you can build your applications. You design your web application to one of these platforms, and Elastic Beanstalk deploys your code to the platform version you selected to create an active application environment.

Elastic Beanstalk provisions the resources needed to run your application, including one or more Amazon EC2 instances. The software stack running on the Amazon EC2 instances depends on the specific platform version you've selected for your environment.

**The solution stack name for a platform branch**  
You can use the *solution stack name* for a given platform branch version to launch an environment with the [EB CLI](eb-cli3.md), [Elastic Beanstalk API](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/), or the [AWS CLI](https://aws.amazon.com/cli/). The *AWS Elastic Beanstalk Platforms* guide lists the *solution stack name* under the platform branch version in both the [Elastic Beanstalk Supported Platforms](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-supported.html) and [Platform history](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platform-history.html) sections.

To retrieve all of the solution stack names that you can use to create an environment, use the [ListAvailableSolutionStacks](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ListAvailableSolutionStacks.html) API or the [`aws elasticbeanstalk list-available-solution-stacks`](https://docs.aws.amazon.com/cli/latest/reference/elasticbeanstalk/list-available-solution-stacks.html) in the AWS CLI.

You can customize and configure the software that your application depends on in your platform. Learn more at [Customizing software on Linux servers](customize-containers-ec2.md) and [Customizing software on Windows servers](customize-containers-windows-ec2.md). Detailed release notes are available for recent releases at [AWS Elastic Beanstalk Release Notes](https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/). 

## Supported platforms and component history
<a name="concepts.platforms.list"></a>

The *AWS Elastic Beanstalk Platforms* guide lists all of the current platform branch versions in the [Elastic Beanstalk Supported Platforms](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-supported.html) section. The *Platforms* guide also lists a *platform history* for each platform, which includes a list of previous branch platform versions. To view the *platform history* for each platform, select one of the following links.
+ [Docker](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platform-history-docker.html)
+ [Go](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platform-history-go.html)
+ [Java SE](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platform-history-javase.html)
+ [Tomcat (running Java SE)](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platform-history-java.html)
+ [.NET Core on Linux](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platform-history-dotnetlinux.html)
+ [.NET on Windows Server](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platform-history-dotnet.html)
+ [Node.js](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platform-history-nodejs.html)
+ [PHP](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platform-history-php.html)
+ [Python](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platform-history-python.html)
+ [Ruby](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platform-history-ruby.html)