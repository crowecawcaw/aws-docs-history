# Troubleshooting your Elastic Beanstalk environment

This chapter provides guidance for troubleshooting issues with your Elastic Beanstalk environment. It includes the following:

- An introduction to AWS Systems Manager, including a procedure to run predefined Elastic Beanstalk
  runbooks that output troubleshooting steps and recommendations.
- General guidance for actions and resources to use when your environment status degrades.
- Specific troubleshooting tips organized by category.
  **If the health of your environment changes to red**, we
  recommend that you first use the AWS Systems Manager tool that includes predefined runbooks to
  troubleshoot Elastic Beanstalk. For more information see the [Using the Systems Manager
  tool](#troubleshooting-systems-manager "#troubleshooting-systems-manager").

###### Try Amazon Q Developer CLI for AI-assisted troubleshooting

Amazon Q Developer CLI can help you troubleshoot environment issues quickly. The Q CLI provides
solutions by checking environment status, reviewing events, analyzing logs, and asking clarifying questions. For
more information and detailed walkthroughs, see [Troubleshooting Elastic Beanstalk Environments with Amazon Q Developer CLI](https://aws.amazon.com/blogs/devops/troubleshooting-elastic-beanstalk-environments-with-amazon-q-developer-cli/ "https://aws.amazon.com/blogs/devops/troubleshooting-elastic-beanstalk-environments-with-amazon-q-developer-cli/") in the AWS blogs.

###### Topics

- [Using AWS Systems Manager Elastic Beanstalk runbooks](#troubleshooting-systems-manager "#troubleshooting-systems-manager")
- [General guidance for troubleshooting your Elastic Beanstalk environment](#troubleshooting-general "#troubleshooting-general")
- [Environments that access secrets and parameters with environment variables](#troubleshooting-secrets-env-variables "#troubleshooting-secrets-env-variables")
- [Environment creation and instance launches](#troubleshooting-envcreate "#troubleshooting-envcreate")
- [Deployments](#troubleshooting-deployments "#troubleshooting-deployments")
- [Health](#troubleshooting-health "#troubleshooting-health")
- [Environments with dual-stack configured load balancers](#troubleshooting-dual-stack-load-balancer "#troubleshooting-dual-stack-load-balancer")
- [Configuration](#troubleshooting-configuration "#troubleshooting-configuration")
- [Troubleshooting Docker containers](#troubleshooting-docker "#troubleshooting-docker")
- [FAQ](#troubleshooting-faq "#troubleshooting-faq")
- [Common Errors](#common-errors "#common-errors")
- [Deployment errors](#python-common-troubleshooting "#python-common-troubleshooting")

## Using AWS Systems Manager Elastic Beanstalk runbooks

You can use Systems Manager to troubleshoot your Elastic Beanstalk environments. To help you get started quickly,
Systems Manager provides predefined Automation runbooks for Elastic Beanstalk. An Automation runbook is a type of
Systems Manager document that defines actions to perform on your environment's instances and other AWS
resources.

The document `AWSSupport-TroubleshootElasticBeanstalk` is an Automation runbook
designed to help identify a number of common issues that can degrade your Elastic Beanstalk environment. To
do so, it checks components of your environment, including the following: EC2 instances, the VPC,
CloudFormation stack, load balancers, Amazon EC2 Auto Scaling groups, and network configuration associated with security
group rules, route tables, and ACLs.

It also provides an option to upload bundled log files from your environment to AWS
Support.

For more information, see [`AWSSupport-TroubleshootElasticBeanstalk`](../../../systems-manager-automation-runbooks/latest/userguide/automation-awssupport-troubleshoot-elastic-beanstalk.md "../../../systems-manager-automation-runbooks/latest/userguide/automation-awssupport-troubleshoot-elastic-beanstalk.md") in the _AWS Systems Manager
Automation runbook reference_.

###### Use Systems Manager to run `AWSSupport-TroubleshootElasticBeanstalk` runbook

###### Note

Run this procedure in the same AWS Region where your Elastic Beanstalk environment is
located.

1. Open the
   [AWS Systems Manager](https://console.aws.amazon.com/systems-manager/home "https://console.aws.amazon.com/systems-manager/home") console.
2. From the navigation pane, in the **Change Management** section, choose
   **Automation**.
3. Choose **Execute automation**.
4. On the **Owned by Amazon** tab, in the **Automation
   document** search box, enter
   `AWSSupport-TroubleshootElasticBeanstalk`.
5. Select the **AWSSupport-TroubleshootElasticBeanstalk** card, then
   choose **Next**.
6. Select **Execute**.
7. In the **Input parameters** section:
   1. From the **AutomationAssumeRole** dropdown, select the ARN of the
      role that allows Systems Manager to perform actions on your behalf.
   2. For **ApplicationName**, enter the name of the Elastic Beanstalk
      application.
   3. For **Environment Name**, enter the Elastic Beanstalk environment.
   4. (Optional) For **S3UploaderLink**, enter a link if an AWS Support
      Engineer has provided you an S3 link for log collection.

8. Choose **Execute**.

If any of the steps fail, select the link under the **Step ID** column
for the step that failed. This displays an **Execution detail** page for
the step. The **VerificationErrorMessage** section will display a summary
of the steps that require attention. For example, the `IAMPermissionCheck` could
display a Warning message. In this case, you could check that the role selected in the
**AutomationAssumeRole** dropdown has the necessary permissions.

After all of the steps successfully complete, the output gives troubleshooting steps and
recommendations to restore your environment to a healthy state.

## General guidance for troubleshooting your Elastic Beanstalk environment

Error messages can appear on the Events page in the console, in logs, or on the Health page. You can also take actions to recover from a degraded
environment that was caused by a recent change. If the health of your environment changes to Red, try the following:

- If an operation on your environment returns an error that contains the text
  `The stack ``stack_id`` associated with environment ``environment-ID`` is in ``stack-status`` state`, see [Recovering your Elastic Beanstalk environment from an invalid state](environment-management-invalid-stack.md "environment-management-invalid-stack.md") for troubleshooting
  help.
- If an operation on your environment returns an error that contains the text `Environment `environment-name`
associated CloudFormation stack`stack_arn` does not exist`, terminate your environment and create another one.
- Review recent environment [events](using-features.md "using-features.md"). Messages from Elastic Beanstalk about deployment, load, and configuration issues
  often appear here.
- Review recent environment [change history](using-features.md "using-features.md"). Change history lists all of the configuration changes
  made to your environments and includes other information, such as which IAM user made changes and which configuration parameters were set.
- [Pull logs](using-features.md "using-features.md") to view recent log file entries. Web server logs contain information about incoming requests
  and errors.
- [Connect to an instance](using-features.md "using-features.md") and check system resources.
- [Roll back](using-features.md "using-features.md") to a previous working version of the application.
- Undo recent configuration changes or restore a [saved configuration](environment-configuration-methods-before.md#configuration-options-before-savedconfig "environment-configuration-methods-before.md#configuration-options-before-savedconfig").
- Deploy a new environment. If the environment appears healthy, perform a [CNAME swap](using-features.md "using-features.md") to route traffic
  to the new environment and continue to debug the previous one.

## Environments that access secrets and parameters with environment variables

**Event:**
_Instance deployment failed to get one or more secrets_

This message indicates that Elastic Beanstalk was not able to fetch one or more of the secrets specified during your application deployment.

- Check that the resources specified by the ARN values in your environment variable configuration exist.
- Confirm that your Elastic Beanstalk EC2 instance profile role has the [required IAM
  permissions](AWSHowTo.secrets.md#AWSHowTo.secrets.IAM-permissions.secrets-manager "AWSHowTo.secrets.md#AWSHowTo.secrets.IAM-permissions.secrets-manager") to access the resources.
- If this event was triggered through the `RestartAppServer` operation, once the issue is fixed, retry the `RestartAppServer`
  call to resolve the issue.
- If the event was triggered through an `UpdateEnvironment` call, retry the `UpdateEnvironment` operation.

For examples of these commands, see [_AWS CLI
examples for Elastic Beanstalk_](../../../cli/latest/userguide/cli_elastic-beanstalk_code_examples.md "../../../cli/latest/userguide/cli_elastic-beanstalk_code_examples.md"). For more information about the API actions for these operations, see the
_[AWS Elastic Beanstalk API Reference](../api.md "../api.md")_.

**Event:**
_Instance deployment detected one or more multiline environment values, which are not supported for this platform_

Multiline variables are not supported for Amazon Linux 2 platforms, excluding Docker and ECS managed Docker platforms. For available options to proceed, see
[Multiline values](AWSHowTo.secrets.md#AWSHowTo.secrets.multiline "AWSHowTo.secrets.md#AWSHowTo.secrets.multiline").

**Event:**
_CreateEnvironment fails when a secret is specified_

When `CreateEnvironment` fails and you have secrets as environment variables, you need to address the underlying issue and then use
`UpdateEnvironment` to complete the environment setup. Do not use `RestartAppServer`, as it will not be sufficient to bring the
environment up in this situation. For examples of these commands, see [_AWS CLI examples for Elastic Beanstalk_](../../../cli/latest/userguide/cli_elastic-beanstalk_code_examples.md "../../../cli/latest/userguide/cli_elastic-beanstalk_code_examples.md"). For more information about
the API actions for these operations, see the _[AWS Elastic Beanstalk API Reference](../api.md "../api.md")_.

## Environment creation and instance launches

**Event:**
_Failed to Launch Environment_

This event occurs when Elastic Beanstalk attempts to launch an environment and encounters failures along the way. Previous events on the **Events**
page will alert you to the root cause of this issue.

**Event:**
_Create environment operation is complete, but with command timeouts. Try increasing
the timeout period._

Your application may take a long time to deploy if you use configuration files that run
commands on the instance, download large files, or install packages. Increase the [command timeout](using-features.md#environments-cfg-rollingdeployments-console "using-features.md#environments-cfg-rollingdeployments-console") to give your
application more time to start running during deployments.

**Event:**
_The following resource(s) failed to create:
[AWSEBInstanceLaunchWaitCondition]_

This message indicates that your environment's Amazon EC2 instances did not communicate to Elastic Beanstalk that they were launched successfully. This can occur if the
instances do not have Internet connectivity. If you configured your environment to launch instances in a private VPC subnet, [ensure that the subnet has a NAT](vpc.md "vpc.md") to allow the instances to connect to Elastic Beanstalk.

**Event:**
_A Service Role is required in this region. Please add a Service Role option to the
environment._

Elastic Beanstalk uses a service role to monitor the resources in your environment and support [managed platform updates](environment-platform-update-managed.md "environment-platform-update-managed.md"). See [Managing Elastic Beanstalk service roles](iam-servicerole.md "iam-servicerole.md") for more information.

## Deployments

**Issue:**
_Application becomes unavailable during deployments_

Because Elastic Beanstalk uses a drop-in upgrade process, there might be a few seconds of downtime. Use
[rolling deployments](using-features.md "using-features.md") to minimize
the effect of deployments on your production environments.

**Event:**
_Failed to create the AWS Elastic Beanstalk application version_

Your application source bundle may be too large, or you may have reached the [application version quota](applications-versions.md "applications-versions.md").

**Event:**
_Update environment operation is complete, but with command timeouts. Try increasing
the timeout period._

Your application may take a long time to deploy if you use configuration files that run
commands on the instance, download large files, or install packages. Increase the [command timeout](using-features.md#environments-cfg-rollingdeployments-console "using-features.md#environments-cfg-rollingdeployments-console") to give your
application more time to start running during deployments.

## Health

**Event:**
_CPU Utilization Exceeds 95.00%_

Try [running more instances](using-features.managing.md "using-features.managing.md"), or [choose a different instance type](using-features.managing.md "using-features.managing.md").

**Event:**
_Elastic Load Balancer awseb-`myapp` Has Zero Healthy
Instances_

If your application appears to be working, make sure that your application’s health check
URL is configured correctly. If not, check the Health screen and environment logs for more
information.

**Event:**
_Elastic Load Balancer awseb-`myapp` Cannot Be
Found_

Your environment's load balancer may have been removed out-of-band. Only make changes to
your environment's resources with the configuration options and [extensibility](ebextensions.md "ebextensions.md") provided by Elastic Beanstalk. Rebuild your environment or launch a new one.

**Event:**
_EC2 Instance Launch Failure. Waiting for a New EC2 Instance to
Launch..._

Availability for your environment's instance type may be low, or you may have reached the
instance quota for your account. Check the [service
health dashboard](http://status.aws.amazon.com/ "http://status.aws.amazon.com/") to ensure that the Elastic Compute Cloud (Amazon EC2) service is
green, or [request a quota increase](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-ec2-instances "https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-ec2-instances").

## Environments with dual-stack configured load balancers

**Event:**
_VPC `vpc_id` does not have IPv6 CIDR blocks configured. IPv6
CIDR blocks are required for dualstack load balancer. Please associate an IPv6 CIDR block with
your VPC before using dualstack mode._

Your VPC and all of the subnets must have IPv6 CIDR blocks associated with them. This is
one of the VPC prerequisites that you must complete before configuring your load balancer for
dualstack support. For more information to complete this task see [Amazon VPC prerequisites](environments-cfg-elbv2-ipv6-dualstack.md#environments-cfg-elbv2-ipv6-dualstack.prereqs "environments-cfg-elbv2-ipv6-dualstack.md#environments-cfg-elbv2-ipv6-dualstack.prereqs") earlier in this topic.

**Event:**
_One or more subnets for VPC `vpc_id` do not have IPv6 CIDR
blocks configured. IPv6 CIDR blocks are required for the subnets used with dualstack load
balancer. Please associate IPv6 CIDR blocks with all required subnets before using dualstack
mode._

All of the subnets for your VPC must have IPv6 CIDR blocks associated with them. This is
one of the VPC prerequisites that you must complete before configuring your load balancer for
dualstack support. For more information to complete this task see [Amazon VPC prerequisites](environments-cfg-elbv2-ipv6-dualstack.md#environments-cfg-elbv2-ipv6-dualstack.prereqs "environments-cfg-elbv2-ipv6-dualstack.md#environments-cfg-elbv2-ipv6-dualstack.prereqs") earlier in this topic.

**Error:**
_The `IpAddressType` option can only be applied on Elastic Beanstalk environments
configured with an Application Load Balancer or Network Load Balancer._

This message indicates that your Elastic Beanstalk environment may be a single instance environment or
that it may be using a Classic Load Balancer. Only environments configured with an Application Load Balancer or Network Load Balancer can configure
`IpAddressType`.

## Configuration

**Event:**
_The stack `stack_id` associated with environment `environment-ID` is in `stack-status` state_

The underlying CloudFormation stack of your environment may be in a _\*\_FAILED_ status. This status must be
remedied in order to continue Elastic Beanstalk operations on your environment. For more information,
see [Recovering your Elastic Beanstalk environment from an invalid state](environment-management-invalid-stack.md "environment-management-invalid-stack.md").

**Event:**
_You cannot configure an Elastic Beanstalk environment with values for both the Elastic Load Balancing Target option and Application Healthcheck URL
option_

The `Target` option in the `aws:elb:healthcheck` namespace is deprecated. Remove the `Target` option namespace) from
your environment and try updating again.

**Event:**
_ELB cannot be attached to multiple subnets in the same AZ_

This message can be seen if you try to move a load balancer between subnets in the same Availability Zone. Changing subnets on the load balancer
requires moving it out of the original availability zone(s) and then back into the original with the desired subnets. During the process, all of your
instances will be migrated between AZs, causing significant downtime. Instead, consider creating a new environment and [perform a CNAME swap](using-features.md "using-features.md").

## Troubleshooting Docker containers

**Event:**
_Failed to pull Docker image :latest: Invalid repository name (), only [a-z0-9-\_.] are
allowed. Tail the logs for more details._

Check the syntax of the `dockerrun.aws.json` file using a JSON validator.
Also verify the dockerfile contents against the requirements described in [Preparing your Docker image for deployment to Elastic Beanstalk](single-container-docker-configuration.md "single-container-docker-configuration.md")

**Event:**
_No EXPOSE directive found in Dockerfile, abort deployment_

The `Dockerfile` or the `dockerrun.aws.json` file does not
declare the container port. Use the `EXPOSE` instruction (`Dockerfile`) or
`Ports` block (`dockerrun.aws.json` file) to expose a port for
incoming traffic.

**Event:**
_Failed to download authentication credentials `repository`
from `bucket name`_

The `dockerrun.aws.json` provides an invalid EC2 key pair and/or S3
bucket for the `.dockercfg` file. Or, the instance profile does not have
GetObject authorization for the S3 bucket. Verify that the `.dockercfg` file
contains a valid S3 bucket and EC2 key pair. Grant permissions for the action
`s3:GetObject` to the IAM role in the instance profile. For details, go to [Managing Elastic Beanstalk instance profiles](iam-instanceprofile.md "iam-instanceprofile.md")

**Event:**
_Activity execution failed, because: WARNING: Invalid auth configuration
file_

Your authentication file (`config.json`) is not formatted correctly. See
[Authenticating with image repositories](docker-configuration.md "docker-configuration.md")

## FAQ

**Question:**
_How can I change my application URL from myapp.us-west-2.elasticbeanstalk.com to
www.myapp.com?_

In a DNS server, register a CNAME record such as `www.mydomain.com CNAME
 mydomain.elasticbeanstalk.com`.

**Question:**
_How do I specify a specific Availability Zone for my Elastic Beanstalk
application?_

You can pick a specific Availability Zone by using the APIs, CLI, Eclipse plugin, or Visual Studio plugin. For instructions about using the Elastic Beanstalk
console to specify an Availability Zone, see [Amazon EC2 Auto Scaling your Elastic Beanstalk environment instances](using-features.managing.md "using-features.managing.md").

**Question:**
_How do I change my environment's instance type?_

To change your environment's instance type go to the environment configuration page and choose **Edit** in the
**Instances** configuration category. Then, select a new instance type and choose **Apply** to update your environment.
After this, Elastic Beanstalk terminates all running instances and replaces them with new ones.

**Question:**
_How do I determine if anyone made configuration changes to an
environment?_

To see this information, in the navigation pane of the Elastic Beanstalk console choose **Change history** to display a list of configuration
changes for all environments. This list includes the date and time of the change, the configuration parameter and value it was changed to, and the IAM user
that made the change. For more information, see [Change history](using-features.md "using-features.md").

**Question:**
_Can I prevent Amazon EBS volumes from being deleted when instances are
terminated?_

Instances in your environment use Amazon EBS for storage; however, the root volume is deleted when an instance is terminated by Amazon EC2 Auto Scaling. We don'trecommend that
you store state or other data on your instances. If needed, you can prevent volumes from being deleted with the AWS CLI: `$ aws ec2
 modify-instance-attribute -b '/dev/sdc=<vol-id>:false` as described in the [AWS CLI
Reference](../../../cli/latest/reference/ec2/modify-instance-attribute.md "../../../cli/latest/reference/ec2/modify-instance-attribute.md").

**Question:**
_How do I delete personal information from my Elastic Beanstalk application?_

AWS resources that your Elastic Beanstalk application uses might store personal information. When you terminate an environment, Elastic Beanstalk terminates the resources that
it created. Resources you added using [configuration files](ebextensions.md "ebextensions.md") are also terminated. However, if you created AWS resources
outside of your Elastic Beanstalk environment and associated them with your application, you might need to manually check that personal information that your
application might have stored isn't retained. Throughout this developer guide, whenever we discuss creating additional resources, we also mention when you
should consider deleting them.

## Common Errors

This topic lists common error messages encountered when using the EB CLI and possible
solutions. If you encounter an error message not shown here, use the
_Feedback_ links to let us know about it.

**ERROR: An error occurred while handling git command. Error code: 128
Error: fatal: Not a valid object name HEAD**

**Cause:** This error message is shown when you have
initialized a Git repository but have not yet committed. The EB CLI looks for the HEAD
revision when your project folder contains a Git repository.

**Solution:** Add the files in your project folder to the
staging area and commit:

```
~/my-app$ `git add .`
~/my-app$ `git commit -m "First commit"`
```

**ERROR: This branch does not have a default environment. You must
either specify an environment by typing "eb status my-env-name" or set a default environment
by typing "eb use my-env-name".**

**Cause:** When you create a new branch in git, it is not
attached to an Elastic Beanstalk environment by default.

**Solution:** Run **eb list** to see a list of
available environments. Then run **eb use `env-name`**
to use one of the available environments.

**ERROR: 2.0+ Platforms require a service role. You can provide one
with --service-role option**

**Cause:** If you specify an environment name with
**eb create** (for example, **eb create my-env**), the EB CLI
will not attempt to create a service role for you. If you don't have the default service role,
the above error is shown.

**Solution:** Run **eb create** without an
environment name and follow the prompts to create the default service role.

## Deployment errors

Your Elastic Beanstalk deployment might response with a 404 (if your application failed to launch) or
500 (if your application fails during runtime) response. To troubleshoot many common issues,
you can use the EB CLI to check the status of your deployment, view its logs, gain access to
your EC2 instance with SSH, or to open the AWS Management Console page for your application
environment.

###### To use the EB CLI to help troubleshoot your deployment

1. Run **eb status** to see the status of your current deployment and
   health of your EC2 hosts. For example:

```
$ `eb status --verbose`

Environment details for: python_eb_app
  Application name: python_eb_app
  Region: us-west-2
  Deployed Version: app-150206_035343
  Environment ID: e-wa8u6rrmqy
  Platform: 64bit Amazon Linux 2014.09 v1.1.0 running Python 2.7
  Tier: WebServer-Standard-
  CNAME: python_eb_app.elasticbeanstalk.com
  Updated: 2015-02-06 12:00:08.557000+00:00
  Status: Ready
  Health: Green
  Running instances: 1
      i-8000528c: InService
```

###### Note

Using the `--verbose` switch provides information about the status of
your running instances. Without it, **eb status** will print only general
information about your environment. 2. Run **eb health** to view health information about your
environment:

```
$ `eb health --refresh`
 elasticBeanstalkExa-env                                  Degraded                  2016-03-28 23:13:20
WebServer                                                                              Ruby 2.1 (Puma)
  total      ok    warning  degraded  severe    info   pending  unknown
    5        2        0        2        1        0        0        0

  instance-id   status     cause
    Overall     Degraded  Incorrect application version found on 3 out of 5 instances. Expected version "Sample Application" (deployment 1).
  i-d581497d    Degraded  Incorrect application version "v2" (deployment 2). Expected version "Sample Application" (deployment 1).
  i-d481497c    Degraded  Incorrect application version "v2" (deployment 2). Expected version "Sample Application" (deployment 1).
  i-136e00c0    Severe    Instance ELB health has not been available for 5 minutes.
  i-126e00c1    Ok
  i-8b2cf575    Ok

  instance-id   r/sec    %2xx   %3xx   %4xx   %5xx      p99      p90      p75     p50     p10
    Overall     646.7   100.0    0.0    0.0    0.0    0.003    0.002    0.001   0.001   0.000
  i-dac3f859    167.5    1675      0      0      0    0.003    0.002    0.001   0.001   0.000
  i-05013a81    161.2    1612      0      0      0    0.003    0.002    0.001   0.001   0.000
  i-04013a80    0.0         -      -      -      -         -        -       -       -       -
  i-3ab524a1    155.9    1559      0      0      0    0.003    0.002    0.001   0.001   0.000
  i-bf300d3c    162.1    1621      0      0      0    0.003    0.002    0.001   0.001   0.000

  instance-id   type       az   running     load 1  load 5      user%  nice%  system%  idle%   iowait%
  i-d581497d    t2.micro   1a   25 mins       0.16     0.1        7.0    0.0      1.7   91.0       0.1
  i-d481497c    t2.micro   1a   25 mins       0.14     0.1        7.2    0.0      1.6   91.1       0.0
  i-136e00c0    t2.micro   1b   25 mins        0.0    0.01        0.0    0.0      0.0   99.9       0.1
  i-126e00c1    t2.micro   1b   25 mins       0.03    0.08        6.9    0.0      2.1   90.7       0.1
  i-8b2cf575    t2.micro   1c   1 hour        0.05    0.41        6.9    0.0      2.0   90.9       0.0

  instance-id   status     id   version              ago                                  deployments
  i-d581497d    Deployed   2    v2                   9 mins
  i-d481497c    Deployed   2    v2                   7 mins
  **i-136e00c0 Failed 2 v2 5 mins**
  i-126e00c1    Deployed   1    Sample Application   25 mins
  i-8b2cf575    Deployed   1    Sample Application   1 hour
```

The above example shows an environment with five instances where the deployment of
version "v2" failed on the third instance. After a failed deployment, the expected version
is reset to the last version that succeeded, which in this case is "Sample Application"
from the first deployment. See [Using the EB CLI to monitor environment health](health-enhanced-ebcli.md "health-enhanced-ebcli.md") for more information. 3. Run **eb logs** to download and view the logs associated with your
application deployment.

```
$ `eb logs`
```

4. Run **eb ssh** to connect with the EC2 instance that's running your
   application and examine it directly. On the instance, your deployed application can be
   found in the `/opt/python/current/app` directory, and your Python environment
   will be found in `/opt/python/run/venv/`.
5. Run **eb console** to view your application environment on the [AWS Management Console](https://aws.amazon.com/console/ "https://aws.amazon.com/console/"). You can use the web
   interface to easily examine various aspects of your deployment, including your
   application's configuration, status, events, logs. You can also download the current or
   past application versions that you've deployed to the server.
