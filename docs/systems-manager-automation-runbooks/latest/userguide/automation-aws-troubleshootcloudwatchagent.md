# `AWSSupport-TroubleshootCloudWatchAgent`

**Description**

The **AWSSupport-TroubleshootCloudWatchAgent** runbook automates troubleshooting the Amazon CloudWatch Agent on your Amazon Elastic Compute Cloud (Amazon EC2) instances. The runbook performs this troubleshooting through a series of basic, and (optional) extended checks.

The basic checks include the following:

- Check for an AWS Identity and Access Management (IAM) instance profile
- Verify if the necessary Amazon CloudWatch Agent IAM permissions are attached to the Amazon EC2 instance
  The extended checks are only performed if the Amazon EC2 instance ID provided is an Systems Manager managed instance. These extended checks include the following:

- Check the status of the Amazon CloudWatch Agent on the instance
- Analyze the logs of the Amazon CloudWatch Agent for common issues and relevant troubleshooting steps
- Zip the relevant logs and configuration files on the Amazon EC2 instance and optionally upload them to an Amazon Simple Storage Service (Amazon S3) bucket of your choosing
- Perform a connectivity check between the instance and the required endpoints

###### Important

When the `RunVpcReachabilityAnalyzer` parameter is set to `true`, this runbook will determine if there is a need to call the child runbook, `AWSSupport-AnalyzeAWSEndpointReachabilityFromEC2`. The child runbook uses VPC Reachability Analyzer which has an associated cost. For more information on pricing, refer to the [Amazon VPC pricing](https://aws.amazon.com/vpc/pricing/ "https://aws.amazon.com/vpc/pricing/") documentation.

###### Important

This runbook only checks your IAM instance profile role for the necessary permissions. If you instead rely on credentials defined in a `.aws/credentials` file, the results of the `verifyIamPermissions` step may be inaccurate.

**How does it work?**

The runbook performs the following steps:

- **getInstanceProfile**: Verifies if the provided Amazon EC2 instance has an IAM instance profile attached.
- **verifyIamPermissions**: Checks the instance profile associated with the instance to determine if the necessary IAM permissions are applied.
- **getInstanceInformation**: Checks if the instance has an active Systems Manager agent, and fetches the OS type of the instance.
- **getAgentStatus**: Checks the status of the Amazon CloudWatch Agent on the instance (extended check).
- **analyzeLogs/analyzeLogsWindows**: Analyzes and outputs findings of Amazon CloudWatch Agent logs based on the OS type.
- **collectLogs/collectLogsWindows**: Bundles and outputs the relevant Amazon CloudWatch Agent troubleshooting files based on the OS type.
- **checkEndpointReachability/checkEndpointReachabilityWindows**: Checks if the instance can reach the required endpoints based on the OS type.
- **analyzeAwsEndpointReachabilityFromEC2**: Calls the child automation runbook to check the reachability of the selected instance to the required endpoints (if enabled).

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootCloudWatchAgent "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootCloudWatchAgent")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

/

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- ec2:DescribeInstances
- iam:GetInstanceProfile
- iam:GetRole
- iam:ListAttachedRolePolicies
- iam:ListRolePolicies
- iam:GetRolePolicy
- iam:GetPolicy
- iam:GetPolicyVersion
- iam:SimulatePrincipalPolicy
- ssm:DescribeInstanceInformation
- ssm:SendCommand
- ssm:GetCommandInvocation
- ssm:DescribeInstanceAssociationsStatus
- ssm:StartAutomationExecution
  Example Policy:

```
{
        "Version": "2012-10-17",
        "Statement": [
            {
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeInstances",
                "iam:GetInstanceProfile",
                "iam:GetRole",
                "iam:ListAttachedRolePolicies",
                "iam:ListRolePolicies",
                "iam:GetRolePolicy",
                "iam:GetPolicy",
                "iam:GetPolicyVersion",
                "iam:SimulatePrincipalPolicy",
                "ssm:DescribeInstanceInformation",
                "ssm:SendCommand",
                "ssm:GetCommandInvocation",
                "ssm:DescribeInstanceAssociationsStatus",
                "ssm:StartAutomationExecution"
            ],
            "Resource": "*"
            }
        ]
        }
```

**Instructions**

Follow these steps to configure the automation:

1. Navigate to [`AWSSupport-TroubleshootCloudWatchAgent`](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootCloudWatchAgent/description "https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootCloudWatchAgent/description") in Systems Manager under Documents.
2. Select **Execute automation.**
3. For the input parameters, enter the following:
   - **AutomationAssumeRole (Optional):**
     - Description: (Optional) The ARN of the IAM role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
     - Type: `AWS::IAM::Role::Arn`

   - **InstanceId (Required):**
     - Description: (Required) The ID of the Amazon EC2 instance you want to troubleshoot the Amazon CloudWatch Agent on.
     - Type: `AWS::EC2::Instance::Id`
     - Allow Pattern: `^i-[0-9a-f]{8,17}$`

   - **S3UploadBucket (Optional):**
     - Description: (Optional) The name of an Amazon S3 bucket to upload the collected Amazon CloudWatch Agent logs. The Amazon EC2 instance profile must have correct permissions to upload files to this bucket. This also requires the target Amazon EC2 instance to be an Systems Manager managed instance.
     - Type: `AWS::S3::Bucket::Name`
     - Allow Pattern: `^$|^[a-z0-9][a-z0-9.-]{1,61}[a-z0-9]$`
     - Default: `""`

   - **S3BucketOwnerAccountId (Optional):**
     - Description: (Optional) The AWS Account Number that owns the Amazon S3 bucket where you want to upload the Amazon CloudWatch Agent logs. If you do not modify this parameter, the runbooks uses the AWS account ID of the user or role in which the Automation runs.
     - Type: `String`
     - Allow Pattern: `^\\{\\{ global:ACCOUNT_ID \\}\\}$|^[0-9]{12}$`
     - Default: `{{ global:ACCOUNT_ID }}`

   - **CheckEC2Endpoint (Optional):**
     - Description: (Optional) Specify `true` if your agent configuration uses the option `append_dimensions` to append Amazon EC2 metric dimensions to the metrics collected by the agent. When `append_dimensions` is used, the Amazon CloudWatch Agent requires connectivity to the Amazon EC2 API endpoint, so an additional connectivity tests will be performed via the extended checks.
     - Type: `String`
     - Allowed Values: `[true, false]`
     - Default: `false`

   - **RunVpcReachabilityAnalyzer (Optional):**
     - Description: (Optional) Specify `true` to run the `AWSSupport-AnalyzeAWSEndpointReachabilityFromEC2` child automation if a network issue is determined by the extended checks, or if the instance ID specified is not a managed instance.
     - Type: `Boolean`
     - Default: `false`

   - **RetainVpcReachabilityAnalysis (Optional):**
     - Description: (Optional) Only relevant if `RunVpcReachabilityAnalyzer` is `true`. Specify `true` to retain the network insight path and related analyses created by VPC Reachability Analyzer. By default, those resources are deleted after successful analysis.
     - Type: `Boolean`
     - Default: `false`

4. Select **Execute**.
5. The automation initiates.
6. The document performs the following steps:
   - **getInstanceProfile**:

   Verifies if the provided Amazon EC2 instance has an IAM instance profile attached.
   - **branchOnInstanceProfileStatus**:

   Branches the automation to check for necessary instance profile permissions if the instance profile is attached to the instance.
   - **verifyIamPermissions**:

   Checks the instance profile associated with the instance to determine if the necessary IAM permissions are applied.
   - **getInstanceInformation**:

   Checks if the instance has an active Systems Manager agent, and fetches the OS type of the instance.
   - **branchOnManagedInstance**:

   Branches the automation to perform extended checks if the instance is managed.
   - **getAgentStatus**:

   Checks the status of the Amazon CloudWatch Agent on the instance.
   - **branchOnInstanceOsType**:

   Branches the automation to run a specific log collection/analysis command based on the OS.
   - **analyzeLogs/analyzeLogsWindows**:

   Analyzes and outputs findings of Amazon CloudWatch Agent logs based on the OS type.
   - **collectLogs/collectLogsWindows**:

   Bundles and outputs the relevant Amazon CloudWatch Agent troubleshooting files based on the OS type.
   - **checkEndpointReachability/checkEndpointReachabilityWindows**:

   Checks if the instance can reach the required endpoints based on the OS type.
   - **branchOnRunVpcReachabilityAnalyzer**:

   Branches the automation to run VPC reachability analysis if enabled and network issues are detected.
   - **generateEndpoints**:

   Generates an endpoint to check from the extended check failures and the value of `CheckEC2Endpoint`.
   - **analyzeAwsEndpointReachabilityFromEC2**:

   Calls the automation runbook, `AWSSupport-AnalyzeAWSEndpointReachabilityFromEC2` to check the reachability of the selected instance to the required endpoints.
   - **outputFindings**:

   Outputs results of the automation execution steps.

7. After completion, review the **Outputs** section for the detailed results of the execution.
   **References**

Systems Manager Automation

- [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootCloudWatchAgent/description "https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootCloudWatchAgent/description")
- [Run an automation](../../../systems-manager/latest/userguide/automation-working-executing.md "../../../systems-manager/latest/userguide/automation-working-executing.md")
- [Setting up an Automation](../../../systems-manager/latest/userguide/automation-setup.md "../../../systems-manager/latest/userguide/automation-setup.md")
- [Support Automation Workflows](https://aws.amazon.com/premiumsupport/technology/saw/ "https://aws.amazon.com/premiumsupport/technology/saw/")
