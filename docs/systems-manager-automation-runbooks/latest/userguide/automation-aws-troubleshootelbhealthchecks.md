# `AWSSupport-TroubleshootELBHealthChecks`

**Description**

The **AWSSupport-TroubleshootELBHealthChecks** runbook helps troubleshoot AWS Elastic Load Balancing (Elastic Load Balancing) health check issues by analyzing its related Amazon CloudWatch (CloudWatch) metrics, verifying network connectivity, and executing diagnostic commands on its target instances.

This runbook addresses the following use cases:

- There are unhealthy instances within the target instances of a load balancer or a target group.
- While there are no unhealthy instances, CloudWatch metrics indicate data points for `UnHealthyHostCounts`

###### Important

Important considerations:

- The automation focuses on troubleshooting instance type targets.
- The maximum number of instances allowed for troubleshooting is 50.
- The target instances must be managed by Systems Manager to enable the execution of diagnostic commands at the instance level.
- The `S3BucketName` parameter is optional, but certain diagnostic results are uploaded directly to the specified Amazon S3 bucket and are not displayed in the automation output.
- IPv6 network connectivity troubleshooting is not supported.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootELBHealthChecks "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootELBHealthChecks")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

/

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `elasticloadbalancing:DescribeLoadBalancers`
- `elasticloadbalancing:DescribeTargetGroups`
- `elasticloadbalancing:DescribeTargetHealth`
- `elasticloadbalancing:DescribeInstanceHealth`
- `ec2:DescribeInstances`
- `ec2:DescribeNetworkInterfaces`
- `ec2:DescribeSecurityGroups`
- `ec2:DescribeSubnets`
- `cloudwatch:GetMetricStatistics`
- `ssm:SendCommand`
- `ssm:GetCommandInvocation`
- `ssm:DescribeInstanceInformation`
- `s3:GetBucketLocation`
- `s3:GetBucketAcl`
- `s3:PutObject`
  Example Policy:

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "elasticloadbalancing:DescribeLoadBalancers",
                "elasticloadbalancing:DescribeTargetGroups",
                "elasticloadbalancing:DescribeTargetHealth",
                "elasticloadbalancing:DescribeInstanceHealth",
                "ec2:DescribeInstances",
                "ec2:DescribeNetworkInterfaces",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeSubnets",
                "cloudwatch:GetMetricStatistics",
                "ssm:SendCommand",
                "ssm:GetCommandInvocation",
                "ssm:DescribeInstanceInformation",
                "s3:GetBucketLocation",
                "s3:GetBucketAcl",
                "s3:PutObject"
            ],
            "Resource": "*"
        }
    ]
}

```

**Instructions**

Follow these steps to configure the automation:

1. Navigate to [`AWSSupport-TroubleshootELBHealthChecks`](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootELBHealthChecks/description "https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootELBHealthChecks/description") in Systems Manager under Documents.
2. Select **Execute automation**.
3. For the input parameters, enter the following:
   - **AutomationAssumeRole (Optional):**
     - Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
       (IAM) role that allows SSM Automation to perform the actions on
       your behalf. If no role is specified, SSM Automation uses
       the permissions of the user who starts this runbook.
     - Type: `AWS::IAM::Role::Arn`

   - **LoadBalancerOrTargetGroupName (Required):**
     - Description: (Required) The name of a Classic Load Balancer, or the name of the target group associated with an Application Load Balancer or Network Load Balancer.
     - Type: `String`
     - Allowed Pattern:
       `^[a-zA-Z0-9-]+$`

   - **ExecutionMode (Required):**
     - Description: (Required) Controls the automation execution mode. `Complete` runs all steps including runCommands on Amazon EC2 instances. `SkipRunCommands` executes all steps except running commands on instances.
     - Type: `String`
     - Allowed Values:
       `[Complete, SkipRunCommands]`

   - **S3BucketName (Optional):**
     - Description: (Optional) The name of the Amazon S3 bucket in your account where you want to upload the troubleshooting logs.
     - Type: `String`
     - Default: `""`

4. Select **Execute**.
5. The automation initiates.
6. The document performs the following steps:
   - **getBucketPublicStatus**:

   Checks if the target Amazon S3 bucket potentially grants read or write public access to its objects.
   - **getLoadBalancerDetails**:

   Identifies the load balancer type and returns a unified load balancer details object.
   - **checkLoadBalancerType**:

   Checks if the load balancer exists.
   - **getTargets**:

   Based on the different types of load balancers, queries describe APIs to return a map of healthy and unhealthy targets details.
   - **checkCloudWatchMetrics**:

   Checks the CloudWatch metrics `HealthyHostCounts` and `UnHealthyHostCounts` and generates the CloudWatch links.
   - **checkUnhealthyReasons**:

   Checks for unhealthy reasons and filters targets.
   - **checkConnectivity**:

   Checks the connectivity between the load balancer and its instances.
   - **runCommands**:

   Runs troubleshooting commands on instances and uploads the output if the bucket name is provided.
   - **generateReport**:

   Generates the final report based on the output of the previous steps and uploads the report to the Amazon S3 bucket if specified.

7. After completed, review the **Outputs** section for the detailed results of the execution.

**Diagnostic Commands**

The runbook executes the following diagnostic commands on instances:

- **Linux Shell:** top, free, ss, curl, iptables, tcpdump
- **Windows PowerShell:** Get-CimInstance, Get-NetFirewallProfile, Get-NetFirewallRule, Invoke-WebRequest, netstat, netsh, pktmon
  **References**

Systems Manager Automation

- [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootELBHealthChecks/description "https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootELBHealthChecks/description")
- [Run an automation](../../../systems-manager/latest/userguide/automation-working-executing.md "../../../systems-manager/latest/userguide/automation-working-executing.md")
- [Setting up an Automation](../../../systems-manager/latest/userguide/automation-setup.md "../../../systems-manager/latest/userguide/automation-setup.md")
- [Support Automation Workflows](https://aws.amazon.com/premiumsupport/technology/saw/ "https://aws.amazon.com/premiumsupport/technology/saw/")
