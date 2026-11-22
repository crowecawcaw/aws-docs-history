

# Install the CloudWatch agent using AWS Systems Manager

 Using AWS Systems Manager makes it easier to install the CloudWatch agent on a fleet of Amazon EC2 instances. You can download the agent into one server and create your CloudWatch agent configuration file for all servers in the fleet. Then you can use Systems Manager to install the agent on the other servers, using the configuration file that you created. Use the following topics to install and run the CloudWatch agent using AWS Systems Manager. 

**Topics**
+ [Install or update the SSM Agent](#update-SSM-Agent-EC2instance-first)
+ [Verify Systems Manager prerequisites](#install-CloudWatch-Agent-minimum-requirements-first)
+ [Verify internet access](#install-CloudWatch-Agent-internet-access-first)
+ [Verifying VPC endpoint prerequisites for private subnets](#CloudWatch-Agent-vpc-endpoint-prerequisites)
+ [Download the CloudWatch agent package to your first instance](#install-CloudWatch-Agent-EC2-first)
+ [Create and modify the agent configuration file](#CW-Agent-Instance-Create-Configuration-File-first)
+ [Install the CloudWatch agent on additional EC2 instances using your agent configuration](#install-CloudWatch-Agent-on-EC2-Instance-fleet-ssm)
+ [(Optional) Modify the common configuration and named profile for CloudWatch agent](#CloudWatch-Agent-profile-instance-fleet)

## Install or update the SSM Agent
<a name="update-SSM-Agent-EC2instance-first"></a>

On an Amazon EC2 instance, the CloudWatch agent requires that the instance is running a current version of SSM Agent. Before you install the CloudWatch agent, update or install SSM Agent on the instance if you haven't already done so. 

For information about installing or updating SSM Agent on an instance running Linux, see [ Installing and Configuring SSM Agent on Linux Instances](https://docs.aws.amazon.com/systems-manager/latest/userguide/manually-install-ssm-agent-linux.html) in the *AWS Systems Manager User Guide*.

For information about installing or updating the SSM Agent, see [Working with SSM Agent](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent.html) in the *AWS Systems Manager User Guide*.

## Verify Systems Manager prerequisites
<a name="install-CloudWatch-Agent-minimum-requirements-first"></a>

Before you use Systems Manager Run Command to install and configure the CloudWatch agent, verify that your instances meet the minimum Systems Manager requirements. For more information, see [Systems Manager Prerequisites](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up.html#systems-manager-prereqs) in the *AWS Systems Manager User Guide*.

## Verify internet access
<a name="install-CloudWatch-Agent-internet-access-first"></a>

Your Amazon EC2 instances must be able to connect to CloudWatch endpoints. This can be by Internet Gateway, NAT gateway, or CloudWatch Interface VPC endpoints. For more information about how to configure internet access, see [Internet Gateways](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html) in the *Amazon VPC User Guide*.

The endpoints and ports to configure on your proxy are as follows:
+ If you're using the agent to collect metrics, you must allow list the CloudWatch endpoints for the appropriate Regions. These endpoints are listed in [Amazon CloudWatch](https://docs.aws.amazon.com/general/latest/gr/rande.html#cw_region) in the *Amazon Web Services General Reference*. 
+ If you're using the agent to collect logs, you must allow list the CloudWatch Logs endpoints for the appropriate Regions. These endpoints are listed in [Amazon CloudWatch Logs](https://docs.aws.amazon.com/general/latest/gr/rande.html#cwl_region) in the *Amazon Web Services General Reference*. 
+ If you're using Systems Manager to install the agent or Parameter Store to store your configuration file, you must allow list the Systems Manager endpoints for the appropriate Regions. These endpoints are listed in [AWS Systems Manager](https://docs.aws.amazon.com/general/latest/gr/rande.html#ssm_region) in the *Amazon Web Services General Reference*. 

## Verifying VPC endpoint prerequisites for private subnets
<a name="CloudWatch-Agent-vpc-endpoint-prerequisites"></a>

For instances without direct internet access (no internet gateway or NAT gateway), you must create VPC endpoints so that the CloudWatch agent and SSM Agent can communicate with AWS services. Create a VPC endpoint for each service that the agent must reach. For more information about these endpoints, see [Network requirements](prerequisites.md#CloudWatch-Agent-network-requirements).

Create the following interface endpoints:
+ `com.amazonaws.{{region}}.monitoring`: for publishing CloudWatch metrics
+ `com.amazonaws.{{region}}.ec2`: for EC2 instance tag lookups used by the agent
+ `com.amazonaws.{{region}}.logs`: for publishing CloudWatch Logs

If you use AWS Systems Manager (Systems Manager) to install the agent or Parameter Store to hold its configuration, also create the following interface endpoints:
+ `com.amazonaws.{{region}}.ssm`: for Systems Manager operations
+ `com.amazonaws.{{region}}.ssmmessages`: for Session Manager and Run Command
+ `com.amazonaws.{{region}}.ec2messages`: for Systems Manager message delivery

To download the agent package, also create a gateway endpoint for `com.amazonaws.{{region}}.s3`.

If you send traces or use Application Signals, also create an interface endpoint for `com.amazonaws.{{region}}.xray`. Without it, the agent can't reach the traces OTLP endpoint and drops the traces that it receives.

If you use `role_arn` for cross-account delivery, also create an interface endpoint for `com.amazonaws.{{region}}.sts`.

Configure the interface endpoints as follows. These steps do not apply to the Amazon S3 gateway endpoint, which has no private DNS option and no security group; it routes through a route table instead.
+ Enable private DNS on each interface endpoint so that standard AWS service hostnames resolve to the endpoint's private IP addresses.
+ Make sure the interface endpoint security groups allow inbound TCP 443 from the security groups attached to your agent instances.
+ Verify that the VPC's DNS settings have both `enableDnsSupport` and `enableDnsHostnames` set to true.

## Download the CloudWatch agent package to your first instance
<a name="install-CloudWatch-Agent-EC2-first"></a>

Use the following steps to download the CloudWatch agent package using Systems Manager.

**To download the CloudWatch agent using Systems Manager**

1. Open the Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Run Command**.

   -or-

   If the AWS Systems Manager home page opens, scroll down and choose **Explore Run Command**.

1. Choose **Run command**.

1. In the **Command document** list, choose **AWS-ConfigureAWSPackage**.

1. In the **Targets** area, choose the instance to install the CloudWatch agent on. If you don't see a specific instance, it might not be configured as a managed instance for use with Systems Manager. For more information, see [Managing nodes in hybrid and multicloud environments with Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-hybrid-multicloud.html) in the *AWS Systems Manager User Guide*.

1. In the **Action** list, choose **Install**.

1. In the **Name** field, enter {{AmazonCloudWatchAgent}}.

1. Leave **Version** blank to install the latest version of the agent.

1. Choose **Run**.

1. Optionally, in the **Targets and outputs** areas, select the button next to an instance name and choose **View output**. Systems Manager should show that the agent was successfully installed.

   

## Create and modify the agent configuration file
<a name="CW-Agent-Instance-Create-Configuration-File-first"></a>

After you have downloaded the CloudWatch agent, you must create the configuration file before you start the agent on any servers.

If you're going to save your agent configuration file in the Systems Manager Parameter Store, you must use an EC2 instance to save to the Parameter Store. Additionally, you must first attach to that instance the `CloudWatchAgentAdminRole` IAM role. For more information about attaching roles, see [Attach an IAM role to an instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/attach-iam-role.html) in the *Amazon EC2 User Guide*.

For more information about creating the CloudWatch agent configuration file, see [Create the Classic CloudWatch agent configuration file](create-cloudwatch-agent-configuration-file.md).

## Install the CloudWatch agent on additional EC2 instances using your agent configuration
<a name="install-CloudWatch-Agent-on-EC2-Instance-fleet-ssm"></a>

After you have a CloudWatch agent configuration saved in Parameter Store, you can use it when you install the agent on other servers.

For each of these servers, follow the steps listed previously in this section to verify the Systems Manager prerequisites, the version of the SSM Agent, and internet access. Then use the following instructions to install the CloudWatch agent on the additional instances, using the CloudWatch agent configuration file that you have created.

**Step 1: Download and install the CloudWatch agent**

You need to install the agent on each server where you will run the agent. The CloudWatch agent is available as a package in Amazon Linux 2023 and Amazon Linux 2. If you are using this operating system, you can use Systems Manager to install the package by using the following steps.

**Note**  
You must also make sure that the IAM role attached to the instance has the **CloudWatchAgentServerPolicy** attached. For more information, see [Prerequisites](prerequisites.md)﻿.

**To use Systems Manager to install the CloudWatch agent package**

1. Open the Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Run Command**.

   -or-

   If the AWS Systems Manager home page opens, scroll down and choose **Explore Run Command**.

1. Choose **Run command**.

1. In the **Command document** list, select **AWS-RunShellScript**. Then paste the following into **Command parameters**.

   ```
   sudo yum install amazon-cloudwatch-agent
   ```

1. Choose **Run**

On all supported operating systems, you can download the CloudWatch agent package using either Systems Manager Run Command or an Amazon S3 download link. For information about using an Amazon S3 download link, see [Download the CloudWatch agent package](download-CloudWatch-Agent-on-EC2-Instance-commandline-first.md).

**Note**  
When you install or update the CloudWatch agent, only the **Uninstall and reinstall** option is supported. You can't use the **In-place update** option.

Systems Manager Run Command enables you to manage the configuration of your instances. You specify a Systems Manager document, specify parameters, and execute the command on one or more instances. SSM Agent on the instance processes the command and configures the instance as specified.

**To download the CloudWatch agent using Run Command**

1. Open the Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Run Command**.

   -or-

   If the AWS Systems Manager home page opens, scroll down and choose **Explore Run Command**.

1. Choose **Run command**.

1. In the **Command document** list, choose **AWS-ConfigureAWSPackage**.

1. In the **Targets** area, choose the instance on which to install the CloudWatch agent. If you do not see a specific instance, it might not be configured for Run Command. For more information, see [Managing nodes in hybrid and multicloud environments with Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-hybrid-multicloud.html) in the *AWS Systems Manager User Guide*.

1. In the **Action** list, choose **Install**.

1. In the **Name** box, enter {{AmazonCloudWatchAgent}}.

1. Leave **Version** blank to install the latest version of the agent.

1. Choose **Run**.

1. Optionally, in the **Targets and outputs** areas, select the button next to an instance name and choose **View output**. Systems Manager should show that the agent was successfully installed. 

**Step 2: Start the CloudWatch agent using your agent configuration file**

Follow these steps to start the agent using Systems Manager Run Command.

For information about setting up the agent on a system that has security-enhanced Linux (SELinux) enabled, see [Set up the CloudWatch agent with security-enhanced Linux (SELinux)](CloudWatch-Agent-SELinux.md).

**To start the CloudWatch agent using Run Command**

1. Open the Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Run Command**.

   -or-

   If the AWS Systems Manager home page opens, scroll down and choose **Explore Run Command**.

1. Choose **Run command**.

1. In the **Command document** list, choose **AmazonCloudWatch-ManageAgent**.

1. In the **Targets** area, choose the instance where you installed the CloudWatch agent.

1. In the **Action** list, choose **configure**.

1. In the **Optional Configuration Source** list, choose **ssm**.

1. In the **Optional Configuration Location** box, enter the name of the Parameter Store parameter that contains your agent configuration file. The name must start with `AmazonCloudWatch-`, because the `CloudWatchAgentServerPolicy` managed policy can read only those parameters. To create the file, see [Create a CloudWatch agent configuration for OpenTelemetry](CloudWatch-Agent-OpenTelemetry-config.md) or [Create the Classic CloudWatch agent configuration file](create-cloudwatch-agent-configuration-file.md).

1. In the **Optional Restart** list, choose **yes** to start the agent after you have finished these steps.

1. Choose **Run**.

1. Optionally, in the **Targets and outputs** areas, select the button next to an instance name and choose **View output**. Systems Manager should show that the agent was successfully started. 

## (Optional) Modify the common configuration and named profile for CloudWatch agent
<a name="CloudWatch-Agent-profile-instance-fleet"></a>

To specify a named profile, proxy, or Region for the agent, edit `common-config.toml`. For the file contents and settings, see [(Optional) Modifying the common configuration and named profile for CloudWatch agent](install-CloudWatch-Agent-on-premise.md#CloudWatch-Agent-profile-onprem).