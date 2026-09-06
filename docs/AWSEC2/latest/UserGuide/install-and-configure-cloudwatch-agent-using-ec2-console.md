

# Install and configure the CloudWatch agent using the Amazon EC2 console to add additional metrics
<a name="install-and-configure-cloudwatch-agent-using-ec2-console"></a>


| Description | 
| --- | 
| Installing and configuring the CloudWatch agent using the Amazon EC2 console is in beta for Amazon EC2 and is subject to change. | 

By default, Amazon CloudWatch provides basic metrics, such as `CPUUtilization` and `NetworkIn`, for monitoring your Amazon EC2 instances. To collect additional metrics, you can install the CloudWatch agent on your EC2 instances, and then configure the agent to emit selected metrics. Instead of manually installing and configuring the CloudWatch agent on every EC2 instance, you can use the Amazon EC2 console to do this for you.

You can use the Amazon EC2 console to install the CloudWatch agent on your instances and configure the agent to emit selected metrics.

Alternatively, to complete this process manually, see [Installing the CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-EC2-Instance.html) in the *Amazon CloudWatch User Guide*. For more information about the CloudWatch agent, see [Collect metrics, logs, and traces using the CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html).

**Topics**
+ [Prerequisites](#install-and-configure-cw-agent-prerequisites)
+ [How it works](#install-and-configure-cw-agent-how-it-works)
+ [Costs](#install-and-configure-cw-agent-costs)
+ [Install and configure the CloudWatch agent](#install-and-configure-cw-agent-procedure)

## Prerequisites
<a name="install-and-configure-cw-agent-prerequisites"></a>

To use Amazon EC2 to install and configure the CloudWatch agent, you must meet the user and instance prerequisites described in this section.

**Tip**  
This feature is not available in all AWS Regions. If the menu item described in the installation procedure on this page does not exist in the Amazon EC2 console and you are flexible about where your instances run, try another Region. Otherwise, you can use the manual directions in the *Amazon CloudWatch User Guide* to install and configure the agent.

**User prerequisites**  
To use this feature, your IAM console user or role must have the permissions required for using Amazon EC2 and the following IAM permissions:

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ssm:GetParameter",
                "ssm:PutParameter"
            ],
            "Resource": "arn:aws:ssm:*:*:parameter/EC2-Custom-Metrics-*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ssm:SendCommand",
                "ssm:ListCommandInvocations",
                "ssm:DescribeInstanceInformation"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "iam:GetInstanceProfile",
                "iam:SimulatePrincipalPolicy"
            ],
            "Resource": "*"
        }
    ]
}
```

------

**Instance prerequisites**
+ Instance state: `running`
+ Supported operating system: Linux
+ AWS Systems Manager Agent (SSM Agent): Installed. Two notes about SSM Agent:
  + SSM Agent is preinstalled on some Amazon Machine Images (AMIs) provided by AWS and trusted third-parties. For information about the supported AMIs and the instructions for installing SSM Agent, see [Amazon Machine Images (AMIs) with SSM Agent preinstalled](https://docs.aws.amazon.com/systems-manager/latest/userguide/ami-preinstalled-agent.html) in the *AWS Systems Manager User Guide*.
  + If you experience issues with the SSM Agent, see [Troubleshooting SSM Agent](https://docs.aws.amazon.com/systems-manager/latest/userguide/troubleshooting-ssm-agent.html) in the *AWS Systems Manager User Guide*.
+ IAM permissions for the instance: The following AWS managed policies must be added to an IAM role that is attached to the instance:
  + [AmazonSSMManagedInstanceCore](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSSMManagedInstanceCore.html) – Enables an instance to use Systems Manager to install and configure the CloudWatch agent.
  + [CloudWatchAgentServerPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchAgentServerPolicy.html) – Enables an instance to use the CloudWatch agent to write data to CloudWatch.

  For information about how to add IAM permissions to your instance, see [Use instance profiles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html) in the *IAM User Guide*.

## How it works
<a name="install-and-configure-cw-agent-how-it-works"></a>

Before you can use the Amazon EC2 console to install and configure the CloudWatch agent, you must make sure that your IAM user or role, and the instances on which you want to add metrics, meet certain prerequisites. Then, you can use the Amazon EC2 console to install and configure the CloudWatch agent on your selected instances.

**First meet the [prerequisites](#install-and-configure-cw-agent-prerequisites)**
+ **You need the required IAM permissions** – Before you get started, make sure that your console user or role has the required IAM permissions to use this feature.
+ **Instances** – To use the feature, your EC2 instances must be Linux instances, have the SSM Agent installed, have the required IAM permissions, and be running. 

**Then you can [use the feature](#install-and-configure-cw-agent-procedure)**

1. **Select your instances** – In the Amazon EC2 console, you select the instances on which to install and configure the CloudWatch agent. You then start the process by choosing **Configure CloudWatch agent**.

1. **Validate SSM Agent** – Amazon EC2 checks that the SSM Agent is installed and started on each instance. Any instances that fail this check are excluded from the process. The SSM Agent is used for performing actions on the instance during this process.

1. **Validate IAM permissions** – Amazon EC2 checks that each instance has the required IAM permissions for this process. Any instances that fail this check are excluded from the process. The IAM permissions enable the CloudWatch agent to collect metrics from the instance and integrate with AWS Systems Manager to use the SSM Agent.

1. **Validate CloudWatch agent** – Amazon EC2 checks that the CloudWatch agent is installed and running on each instance. If any instances fail this check, Amazon EC2 offers to install and start the CloudWatch agent for you. The CloudWatch agent will collect the selected metrics on each instance after this process is completed.

1. **Select metric configuration** – You select the metrics for the CloudWatch agent to emit from your instances. Once selected, Amazon EC2 stores a configuration file in Parameter Store, where it remains until the process is completed. Amazon EC2 will delete the configuration file from Parameter Store unless the process is interrupted. Note that if you don't select a metric, but you previously added it to your instance, it will be removed from your instance when this process is completed.

1. **Update CloudWatch agent configuration** – Amazon EC2 sends the metric configuration to the CloudWatch agent. This is the last step in the process. If it succeeds, your instances can emit data for the selected metrics and Amazon EC2 deletes the configuration file from Parameter Store.

## Costs
<a name="install-and-configure-cw-agent-costs"></a>

Additional metrics that you add during this process are billed as custom metrics. For more information about CloudWatch metrics pricing, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).

## Install and configure the CloudWatch agent
<a name="install-and-configure-cw-agent-procedure"></a>

You can use the Amazon EC2 console to install and configure the CloudWatch agent to add additional metrics.

**Note**  
Every time you perform this procedure, you overwrite the existing CloudWatch agent configuration. If you don't select a metric that was selected previously, it will be removed from the instance.

**To install and configure the CloudWatch agent using the Amazon EC2 console**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Instances**.

1. Select the instances on which to install and configure the CloudWatch agent.

1. Choose **Actions**, **Monitor and troubleshoot**, **Configure CloudWatch agent**.

1. For each step in the process, read the console text, and then choose **Next**.

1. To complete the process, in the final step, choose **Complete**.

**To update the agent configuration created by the Amazon EC2 console**  
You can manually customize the configuration that the EC2 console created. For more information, see [Manually create or edit the CloudWatch agent configuration file](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-Configuration-File-Details.html) in the *Amazon CloudWatch User Guide*.