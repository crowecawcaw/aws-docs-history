# Install the CloudWatch agent using
 AWS Systems Manager

 Using AWS Systems Manager makes it easier to install the CloudWatch agent on a fleet of Amazon EC2
 instances. You can download the agent into one server and create your CloudWatch agent
 configuration file for all servers in the fleet. Then you can use Systems Manager to install the agent
 on the other servers, using the configuration file that you created. Use the following
 topics to install and run the CloudWatch agent using AWS Systems Manager. 

###### Topics

* [Install or update the SSM Agent](#update-SSM-Agent-EC2instance-first "#update-SSM-Agent-EC2instance-first")
* [Verify Systems Manager
 prerequisites](#install-CloudWatch-Agent-minimum-requirements-first "#install-CloudWatch-Agent-minimum-requirements-first")
* [Verify internet
 access](#install-CloudWatch-Agent-internet-access-first "#install-CloudWatch-Agent-internet-access-first")
* [Download the CloudWatch agent package to
 your first instance](#install-CloudWatch-Agent-EC2-first "#install-CloudWatch-Agent-EC2-first")
* [Create and modify the
 agent configuration file](#CW-Agent-Instance-Create-Configuration-File-first "#CW-Agent-Instance-Create-Configuration-File-first")
* [Install and start the
 CloudWatch agent on additional EC2 instances using your agent configuration](#install-CloudWatch-Agent-on-EC2-Instance-fleet "#install-CloudWatch-Agent-on-EC2-Instance-fleet")
* [Install the CloudWatch agent on
 additional EC2 instances using your agent configuration](#install-CloudWatch-Agent-on-EC2-Instance-fleet "#install-CloudWatch-Agent-on-EC2-Instance-fleet")
* [(Optional) Modify the common
 configuration and named profile for CloudWatch agent](#CloudWatch-Agent-profile-instance-fleet "#CloudWatch-Agent-profile-instance-fleet")

## Install or update the SSM Agent


On an Amazon EC2 instance, the CloudWatch agent requires that the instance is running version
 2.2.93.0 or later of the SSM Agent. Before you install the CloudWatch agent, update or install
 SSM Agent on the instance if you haven't already done so. 


For information about installing or updating SSM Agent on an instance running Linux,
 see  [Installing and
 Configuring SSM Agent on Linux Instances](https://docs.aws.amazon.com/systems-manager/latest/userguide/manually-install-ssm-agent-linux.html "https://docs.aws.amazon.com/systems-manager/latest/userguide/manually-install-ssm-agent-linux.html") in the
 *AWS Systems Manager User Guide*.


For information about installing or updating the SSM Agent, see [Working with SSM Agent](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent.html "https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent.html") in the
 *AWS Systems Manager User Guide*.


## Verify Systems Manager
 prerequisites


Before you use Systems Manager Run Command to install and configure the CloudWatch agent, verify that
 your instances meet the minimum Systems Manager requirements. For more information, see [Systems Manager
 Prerequisites](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up.html#systems-manager-prereqs "https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up.html#systems-manager-prereqs") in the *AWS Systems Manager User Guide*.


## Verify internet
 access


Your Amazon EC2 instances must be able to connect to CloudWatch endpoints. This can be by
 Internet Gateway, NAT gateway, or CloudWatch Interface VPC endpoints. For more information about
 how to configure internet access, see [Internet Gateways](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html "https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html") in the *Amazon VPC User Guide*.


The endpoints and ports to configure on your proxy are as follows:



* If you're using the agent to collect metrics, you must allow list the CloudWatch
 endpoints for the appropriate Regions. These endpoints are listed in [Amazon CloudWatch](https://docs.aws.amazon.com/general/latest/gr/rande.html#cw_region "https://docs.aws.amazon.com/general/latest/gr/rande.html#cw_region") in the
 *Amazon Web Services General Reference*.
* If you're using the agent to collect logs, you must allow list the CloudWatch Logs endpoints
 for the appropriate Regions. These endpoints are listed in [Amazon CloudWatch Logs](https://docs.aws.amazon.com/general/latest/gr/rande.html#cwl_region "https://docs.aws.amazon.com/general/latest/gr/rande.html#cwl_region") in the
 *Amazon Web Services General Reference*.
* If you're using Systems Manager to install the agent or Parameter Store to store your configuration
 file, you must allow list the Systems Manager endpoints for the appropriate Regions. These
 endpoints are listed in [AWS
 Systems Manager](https://docs.aws.amazon.com/general/latest/gr/rande.html#ssm_region "https://docs.aws.amazon.com/general/latest/gr/rande.html#ssm_region") in the *Amazon Web Services General Reference*.

## Download the CloudWatch agent package to
 your first instance


Use the following steps to download the CloudWatch agent package using Systems Manager.


###### To download the CloudWatch agent using Systems Manager

1. Open the Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose 
 **Run Command**.


-or-


If the AWS Systems Manager home page opens, scroll down and 
 choose **Explore Run Command**.
3. Choose **Run command**.
4. In the **Command document** list, choose
 **AWS-ConfigureAWSPackage**.
5. In the **Targets** area, choose the instance to install the CloudWatch
 agent on. If you don't see a specific instance, it might not be configured as a
 managed instance for use with Systems Manager. For more information, see [Setting Up AWS Systems Manager for
 Hybrid Environments](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-managedinstances.html "https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-managedinstances.html") in the *AWS Systems Manager User Guide*.
6. In the **Action** list, choose
 **Install**.
7. In the **Name** field, enter
 `AmazonCloudWatchAgent`.
8. Keep **Version** set to **latest** to install
 the latest version of the agent.
9. Choose **Run**.
10. Optionally, in the **Targets and outputs** areas, select the
 button next to an instance name and choose **View output**. Systems Manager
 should show that the agent was successfully installed.

## Create and modify the
 agent configuration file


After you have downloaded the CloudWatch agent, you must create the configuration file
 before you start the agent on any servers.


If you're going to save your agent configuration file in the
 Systems Manager Parameter Store, you must use an EC2 instance to save to the Parameter Store. Additionally, you
 must first attach to that instance the `CloudWatchAgentAdminRole` IAM role.
 For more information about attaching roles, see [Attaching an IAM
 Role to an Instance](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/iam-roles-for-amazon-ec2.html#attach-iam-role "https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/iam-roles-for-amazon-ec2.html#attach-iam-role") in the *Amazon EC2 User Guide*.


For more information about creating the CloudWatch agent configuration file, see [Create the CloudWatch agent
 configuration file](create-cloudwatch-agent-configuration-file.md "create-cloudwatch-agent-configuration-file.md").


## Install and start the
 CloudWatch agent on additional EC2 instances using your agent configuration


After you have a CloudWatch agent configuration saved in Parameter Store, you can use it when you
 install the agent on other servers.


For each of these servers, follow the steps listed previously in this section to
 verify the Systems Manager prerequisites, the version of the SSM Agent, and internet access. Then use
 the following instructions to install the CloudWatch agent on the additional instances, using
 the CloudWatch agent configuration file that you have created.


**Step 1: Download and install the CloudWatch agent**


To be able to send the CloudWatch data to a different Region, make sure that the IAM role
 that you attached to this instance has permissions to write the CloudWatch data in that
 Region.


Following is an example of using the `aws configure` command to create a
 named profile for the CloudWatch agent. This example assumes that you are using the default
 profile name of `AmazonCloudWatchAgent`.


###### To create the AmazonCloudWatchAgent profile for the CloudWatch agent

* On Linux servers, type the following command and follow the prompts:



```
sudo aws configure --profile AmazonCloudWatchAgent
```

On Windows Server, open PowerShell as an administrator, type the following command
 and follow the prompts.



```
aws configure --profile AmazonCloudWatchAgent
```

## Install the CloudWatch agent on
 additional EC2 instances using your agent configuration


After you have a CloudWatch agent configuration saved in Parameter Store, you can use it when you
 install the agent on other servers.


For each of these servers, follow the steps listed previously in this section to
 verify the Systems Manager prerequisites, the version of the SSM Agent, and internet access. Then use
 the following instructions to install the CloudWatch agent on the additional instances, using
 the CloudWatch agent configuration file that you have created.


**Step 1: Download and install the CloudWatch agent**


You need to install the agent on each server where you will run the
 agent. The CloudWatch agent is available as a package in Amazon Linux 2023 and Amazon Linux 2. If you are
 using this operating system, you can use Systems Manager to install the package by using the
 following steps.


###### Note

You must also make sure that the IAM role attached to the instance has the
 **CloudWatchAgentServerPolicy** attached. For more information, see
 [Prerequisites](prerequisites.md "prerequisites.md")﻿.


###### To use Systems Manager to install the CloudWatch agent package

1. Open the Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose 
 **Run Command**.


-or-


If the AWS Systems Manager home page opens, scroll down and 
 choose **Explore Run Command**.
3. Choose **Run command**.
4. In the **Command document** list, select
 **AWS-RunShellScript**. Then paste the following into
 **Command parameters**.



```
sudo yum install amazon-cloudwatch-agent
```
5. Choose **Run**

On all supported operating systems, you can download the CloudWatch agent
 package using either Systems Manager Run Command or an Amazon S3 download link.
 


###### Note

When you install or update the CloudWatch agent, only the **Uninstall and
 reinstall** option is supported. You can't use the **In-place
 update** option.


Systems Manager Run Command enables you to manage the configuration of your instances. You specify
 a Systems Manager document, specify parameters, and execute the command on one or more instances.
 SSM Agent on the instance processes the command and configures the instance as
 specified.


###### To download the CloudWatch agent using Run Command

1. Open the Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose 
 **Run Command**.


-or-


If the AWS Systems Manager home page opens, scroll down and 
 choose **Explore Run Command**.
3. Choose **Run command**.
4. In the **Command document** list, choose
 **AWS-ConfigureAWSPackage**.
5. In the **Targets** area, choose the instance on which to install
 the CloudWatch agent. If you do not see a specific instance, it might not be configured for
 Run Command. For more information, see [Setting Up AWS Systems Manager for
 Hybrid Environments](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-managedinstances.html "https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-managedinstances.html") in the *AWS Systems Manager User Guide*.
6. In the **Action** list, choose
 **Install**.
7. In the **Name** box, enter
 `AmazonCloudWatchAgent`.
8. Keep **Version** set to **latest** to install
 the latest version of the agent.
9. Choose **Run**.
10. Optionally, in the **Targets and outputs** areas, select the
 button next to an instance name and choose **View output**. Systems Manager
 should show that the agent was successfully installed.

**Step 2: Start the CloudWatch agent using your agent configuration
 file**


Follow these steps to start the agent using Systems Manager Run Command.


For information about setting up the agent on a system that has security-enhanced
 Linux (SELinux) enabled, see [Set up the CloudWatch agent with security-enhanced Linux
 (SELinux)](CloudWatch-Agent-SELinux.md "CloudWatch-Agent-SELinux.md").


###### To start the CloudWatch agent using Run Command

1. Open the Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose 
 **Run Command**.


-or-


If the AWS Systems Manager home page opens, scroll down and 
 choose **Explore Run Command**.
3. Choose **Run command**.
4. In the **Command document** list, choose
 **AmazonCloudWatch-ManageAgent**.
5. In the **Targets** area, choose the instance where you installed
 the CloudWatch agent.
6. In the **Action** list, choose
 **configure**.
7. In the **Optional Configuration Source** list, choose
 **ssm**.
8. In the **Optional Configuration Location** box, enter the name of
 the Systems Manager parameter name of the agent configuration file that you created and saved to
 Systems Manager Parameter Store, as explained in [Create the CloudWatch agent
 configuration file](create-cloudwatch-agent-configuration-file.md "create-cloudwatch-agent-configuration-file.md").
9. In the **Optional Restart** list, choose **yes**
 to start the agent after you have finished these steps.
10. Choose **Run**.
11. Optionally, in the **Targets and outputs** areas, select the
 button next to an instance name and choose **View output**. Systems Manager
 should show that the agent was successfully started.

## (Optional) Modify the common
 configuration and named profile for CloudWatch agent


The CloudWatch agent includes a configuration file called
 `common-config.toml`. You can use this file to optionally specify
 proxy and Region information.


On a server running Linux, this file is in the
 `/opt/aws/amazon-cloudwatch-agent/etc` directory. On a server running Windows
 Server, this file is in the `C:\ProgramData\Amazon\AmazonCloudWatchAgent`
 directory.


The default `common-config.toml` is as follows:



```
# This common-config is used to configure items used for both ssm and cloudwatch access
 
 
## Configuration for shared credential.
## Default credential strategy will be used if it is absent here:
##            Instance role is used for EC2 case by default.
##            AmazonCloudWatchAgent profile is used for onPremise case by default.
# [credentials]
#    shared_credential_profile = "{profile_name}"
#    shared_credential_file= "{file_name}"
 
## Configuration for proxy.
## System-wide environment-variable will be read if it is absent here.
## i.e. HTTP_PROXY/http_proxy; HTTPS_PROXY/https_proxy; NO_PROXY/no_proxy
## Note: system-wide environment-variable is not accessible when using ssm run-command.
## Absent in both here and environment-variable means no proxy will be used.
# [proxy]
#    http_proxy = "{http_url}"
#    https_proxy = "{https_url}"
#    no_proxy = "{domain}"
```

All lines are commented out initially. To set the credential profile or proxy
 settings, remove the `#` from that line and specify a value. You can edit this
 file manually, or by using the `RunShellScript` Run Command in Systems Manager:



* `shared_credential_profile` – For on-premises servers, this line
 specifies the IAM user credential profile to use to send data to CloudWatch. If you keep
 this line commented out, `AmazonCloudWatchAgent` is used. 


On an EC2 instance, you can use this line to have the CloudWatch agent send data from
 this instance to CloudWatch in a different AWS Region. To do so, specify a named profile
 that includes a `region` field specifying the name of the Region to send
 to.


If you specify a `shared_credential_profile`, you must also remove the
 `#` from the beginning of the `[credentials]` line.
* `shared_credential_file` – To have the agent look for
 credentials in a file located in a path other than the default path, specify that
 complete path and file name here. The default path is `/root/.aws` on Linux
 and is `C:\\Users\\Administrator\\.aws` on Windows Server.


The first example below shows the syntax of a valid
 `shared_credential_file` line for Linux servers, and the second example
 is valid for Windows Server. On Windows Server, you must escape the \
 characters.



```
shared_credential_file= "/usr/`username`/credentials"
```


```
shared_credential_file= "C:\\Documents and Settings\\`username`\\.aws\\credentials"
```

If you specify a `shared_credential_file`, you must also remove the
 `#` from the beginning of the `[credentials]` line.
* Proxy settings – If your servers use HTTP or HTTPS proxies to contact AWS
 services, specify those proxies in the `http_proxy` and
 `https_proxy` fields. If there are URLs that should be excluded from
 proxying, specify them in the `no_proxy` field, separated by commas.
