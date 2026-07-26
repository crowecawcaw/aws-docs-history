# `AWSSupport-TroubleshootLambdaVpcConnectivity`

###### Description

The `AWSSupport-TroubleshootLambdaVpcConnectivity` runbook helps diagnose and
troubleshoot network connectivity issues between AWS Lambda (Lambda) functions connected to
an Amazon Virtual Private Cloud (Amazon VPC) and their target destinations. The runbook uses Amazon VPC Reachability Analyzer
to perform network path analysis, identifying potential issues such as missing NAT gateways,
incorrect routing configurations, security group misconfigurations, and network ACL
restrictions. The runbook provides actionable recommendations to resolve connectivity
problems and ensure proper network communication for VPC-enabled Lambda functions.

###### Important

You are charged per analysis processed between a source and destination. For more
information, see the **Network Analysis** section in
[Amazon VPC Pricing](https://aws.amazon.com/vpc/pricing/ "https://aws.amazon.com/vpc/pricing/").

This runbook creates a network insights path and network insights analysis in your
account using Reachability Analyzer. If the automation completes successfully, the
runbook deletes these resources. If the cleanup step fails, the network insights path is
not deleted and you must delete it manually. Undeleted network insights paths count
towards the quota for your AWS account. For more information, see [Quotas for Reachability Analyzer](../../../vpc/latest/reachability/reachability-analyzer-limits.md "../../../vpc/latest/reachability/reachability-analyzer-limits.md").

This runbook analyzes one Lambda function and one destination per execution.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootLambdaVpcConnectivity "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootLambdaVpcConnectivity")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

/

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ec2:CreateNetworkInsightsPath`
- `ec2:CreateTags`
- `ec2:DeleteNetworkInsightsAnalysis`
- `ec2:DeleteNetworkInsightsPath`
- `ec2:DescribeNetworkInsightsAnalyses`
- `ec2:DescribeNetworkInsightsPaths`
- `ec2:DescribeNetworkInterfaces`
- `ec2:StartNetworkInsightsAnalysis`
- `lambda:GetFunction`
- `ssm:DeleteParameter`
- `ssm:GetParameter`
- `ssm:PutParameter`
  Example IAM policy:

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ec2:CreateNetworkInsightsPath",
                "ec2:CreateTags",
                "ec2:DeleteNetworkInsightsAnalysis",
                "ec2:DeleteNetworkInsightsPath",
                "ec2:DescribeNetworkInsightsAnalyses",
                "ec2:DescribeNetworkInsightsPaths",
                "ec2:DescribeNetworkInterfaces",
                "ec2:StartNetworkInsightsAnalysis",
                "lambda:GetFunction",
                "ssm:DeleteParameter",
                "ssm:GetParameter",
                "ssm:PutParameter"
            ],
            "Resource": "*"
        }
    ]
}

```

###### Outputs

`SynthOutput.Findings` - Prioritized, actionable recommendations for resolving
the identified Lambda VPC network connectivity issues.

###### Instructions

Follow these steps to configure the automation:

1. Open [AWSSupport-TroubleshootLambdaVpcConnectivity](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootLambdaVpcConnectivity/description "https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootLambdaVpcConnectivity/description") in Systems Manager
   under Documents.
2. Choose Execute automation.
3. For the input parameters, enter the following:

   - **LambdaArn (Required):**

   The ARN of the Lambda function to analyze. This runbook analyzes one Lambda
   function per execution.
   - **DestinationId (Required):**

   The destination resource for network path analysis. Supports Amazon EC2
   instances, Elastic Network Interfaces, VPC Endpoints, Internet Gateways, NAT
   Gateways, Transit Gateways, Transit Gateway Attachments, Virtual Private
   Gateways, VPC Peering Connections, resource ARNs, or IPv4 addresses.
   - **DestinationPort (Optional):**

   The target port number for the path analysis. Defaults to `0`,
   which considers all combinations of IP addresses and ports.
   - **Protocol (Optional):**

   The network protocol to analyze. Valid values: `TCP` |
   `UDP`. Defaults to `TCP`.
   - **AutomationAssumeRole (Optional):**

   The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the
   actions on your behalf. If no role is specified, Systems Manager Automation uses the
   permissions of the user that starts this runbook.

4. Choose Execute.
5. The automation initiates.
6. The document performs the following steps:

   - **`InputValidation`**:

   Validates the input parameters, verifies the Lambda function exists and is
   VPC-enabled, and checks that the required AWS permissions are
   available.
   - **`ConnectionCheck`**:

   Discovers the ENIs associated with the Lambda function, creates Amazon VPC
   Reachability Analyzer network insights paths and analyses, and returns the
   results.
   - **`CleanupReachabilityResourcesOnCancel`**:

   Cleans up Amazon VPC Reachability Analyzer resources created by the
   `ConnectionCheck` step if the automation is cancelled or
   fails.
   - **`SynthOutput`**:

   Analyzes the Reachability Analyzer results and generates prioritized,
   actionable recommendations for resolving Lambda VPC network connectivity
   issues.

7. After completion, review the Outputs section for the detailed results of the
   execution.

###### References

Systems Manager Automation

- [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootLambdaVpcConnectivity/description "https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootLambdaVpcConnectivity/description")
- [Run an
  automation](../../../systems-manager/latest/userguide/automation-working-executing.md "../../../systems-manager/latest/userguide/automation-working-executing.md")
- [Setting up an
  Automation](../../../systems-manager/latest/userguide/automation-setup.md "../../../systems-manager/latest/userguide/automation-setup.md")
- [Support Automation
  Workflows](https://aws.amazon.com/premiumsupport/technology/saw/ "https://aws.amazon.com/premiumsupport/technology/saw/")
