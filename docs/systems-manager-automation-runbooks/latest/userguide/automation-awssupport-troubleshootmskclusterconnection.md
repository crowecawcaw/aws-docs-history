

# `AWSSupport-TroubleshootMSKClusterConnection`
<a name="automation-awssupport-troubleshootmskclusterconnection"></a>

## Description
<a name="automation-awssupport-troubleshootmskclusterconnection-description"></a>

The `AWSSupport-TroubleshootMSKClusterConnection` runbook diagnoses and helps resolve Amazon Managed Streaming for Apache Kafka cluster connectivity issues. It performs broker health analysis, network configuration validation, live connectivity testing, and AWS Identity and Access Management authentication verification.

## How it works
<a name="automation-awssupport-troubleshootmskclusterconnection-how-it-works"></a>

The runbook performs the following operations:

1. **Permission verification:** Validates that the execution role has all required permissions before proceeding, preventing partial resource creation due to insufficient permissions.

1. **Cluster analysis:** Retrieves Amazon MSK cluster configuration and metadata to understand the cluster's current state.

1. **Broker health check:** Analyzes broker health metrics from Amazon CloudWatch to identify performance issues such as high CPU, memory, disk usage, or exhausted credit balance.

1. **Live connectivity testing:** Deploys a AWS CloudFormation stack with a Amazon VPC-attached AWS Lambda function to test DNS resolution and TCP connectivity to the Amazon MSK cluster from within the client's network environment.

1. **Network path analysis:** Uses Amazon VPC Reachability Analyzer to diagnose network connectivity issues between the client and Amazon MSK brokers when connectivity tests fail.

1. **Static network analysis:** Performs fallback analysis of route tables, Network ACLs, and security group rules when Lambda testing is unavailable.

1. **IAM authentication verification:** For IAM-authenticated connections (ports `9098` or `9198`), analyzes IAM policies to verify required permissions, particularly the `kafka-cluster:Connect` permission.

1. **Resource cleanup:** Automatically removes the CloudFormation stack and associated resources created for testing.

1. **Comprehensive reporting:** Compiles findings with actionable recommendations for resolving identified issues.

**Amazon VPC Reachability Analyzer charges apply**  
This runbook uses [Amazon VPC Reachability Analyzer](https://docs.aws.amazon.com/vpc/latest/reachability/what-is-reachability-analyzer.html) to diagnose network connectivity issues. Each analysis incurs a charge. For current pricing information, see [Amazon VPC Pricing](https://aws.amazon.com/vpc/pricing/). To use static analysis only, make sure the Lambda connectivity test succeeds. If the connectivity test fails, the automation runs the Reachability Analyzer step automatically.

## Document parameters
<a name="automation-awssupport-troubleshootmskclusterconnection-parameters"></a>
+ AutomationAssumeRole

  Type: String

  Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
+ `ClusterARN`

  Type: String

  Description: (Required) The Amazon Resource Name of the Amazon MSK cluster to troubleshoot.

  Allowed Pattern: `^arn:(aws|aws-cn|aws-us-gov):kafka:[a-z0-9\-]+:\d{12,13}:cluster\/[a-zA-Z0-9\-]{1,64}\/[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}(-[0-9a-z]{1,2})?$`
+ `BootstrapEndpoints`

  Type: String

  Description: (Required) The Amazon MSK cluster bootstrap endpoint(s). Accepts a single endpoint in `hostname:port` format or multiple comma-separated endpoints (for example, `broker1.example.com:9092,broker2.example.com:9092,broker3.example.com:9092`).

  Allowed Pattern: `^[a-zA-Z0-9.-]+:[0-9]{1,5}(,[a-zA-Z0-9.-]+:[0-9]{1,5})*$`
+ `ClientVPC`

  Type: String

  Description: (Required) The Amazon VPC ID where the client attempting to connect resides.

  Allowed Pattern: `^vpc-[a-z0-9]{8,17}$`
+ `ClientSubnet`

  Type: String

  Description: (Required) The subnet ID where the client attempting to connect resides.

  Allowed Pattern: `^subnet-[a-z0-9]{8,17}$`
+ `ClientSecurityGroups`

  Type: String

  Description: (Required) The security group ID(s) of the client attempting to connect. Accepts a single security group or multiple comma-separated security groups (for example, `sg-abcd1234,sg-0abcdef1234567890`).

  Allowed Pattern: `^sg-[a-z0-9]{8,17}(,sg-[a-z0-9]{8,17})*$`
+ `LambdaAssumeRole`

  Type: `AWS::IAM::Role::Arn`

  Description: (Optional) IAM role ARN for Lambda function execution with Amazon VPC access permissions. If not provided, the automation creates a new role with required permissions.

  Default: Empty string

  Allowed Pattern: `^$|^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b|aws-iso-e|aws-iso-f|aws-eusc):iam::\d{12}:role/[\w+=,.@/-]+$`
+ `ClientIAMRole`

  Type: `AWS::IAM::Role::Arn`

  Description: (Optional) IAM role ARN used by the client for Amazon MSK authentication. Required only when troubleshooting IAM-authenticated connections (ports 9098 or 9198).

  Default: Empty string

  Allowed Pattern: `^$|^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b|aws-iso-e|aws-iso-f|aws-eusc):iam::\d{12}:role/[\w+=,.@/-]+$`
+ `RetainResources`

  Type: Boolean

  Description: (Optional) Whether to retain Network Insights Analysis resources after completion. Set to `true` to keep analysis resources for further review, or `false` to automatically delete them.

  Default: `false`

  Valid values: `true`, `false`

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.

The automation requires the following permissions:
+ **Amazon MSK permissions:**
  + `kafka:DescribeClusterV2`
  + `kafka:GetBootstrapBrokers`
+ **CloudWatch permissions:**
  + `cloudwatch:GetMetricData`
+ **CloudFormation permissions:**
  + `cloudformation:CreateStack`
  + `cloudformation:DescribeStacks`
  + `cloudformation:DescribeStackResources`
  + `cloudformation:DeleteStack`
+ **Lambda permissions:**
  + `lambda:CreateFunction`
  + `lambda:InvokeFunction`
  + `lambda:GetFunction`
  + `lambda:DeleteFunction`
  + `lambda:UpdateFunctionConfiguration`
  + `lambda:TagResource`
+ **Amazon EC2 and Amazon VPC permissions:**
  + `ec2:DescribeNetworkInterfaces`
  + `ec2:DescribeSecurityGroups`
  + `ec2:DescribeSubnets`
  + `ec2:DescribeVpcs`
  + `ec2:DescribeRouteTables`
  + `ec2:DescribeNetworkAcls`
  + `ec2:CreateNetworkInsightsPath`
  + `ec2:StartNetworkInsightsAnalysis`
  + `ec2:DescribeNetworkInsightsPaths`
  + `ec2:DescribeNetworkInsightsAnalyses`
  + `ec2:DeleteNetworkInsightsPath`
  + `ec2:DeleteNetworkInsightsAnalysis`
  + `ec2:DeleteNetworkInterface`
+ **IAM permissions (required only when `LambdaAssumeRole` is not provided):**
  + `iam:CreateRole`
  + `iam:PutRolePolicy`
  + `iam:AttachRolePolicy`
  + `iam:GetRole`
  + `iam:TagRole`
  + `iam:PassRole`
  + `iam:DeleteRole`
  + `iam:DeleteRolePolicy`
  + `iam:DetachRolePolicy`
+ **IAM permissions (for IAM authentication analysis when `ClientIAMRole` is provided):**
  + `iam:GetRole`
  + `iam:GetRolePolicy`
  + `iam:ListRolePolicies`
  + `iam:ListAttachedRolePolicies`
  + `iam:GetPolicy`
  + `iam:GetPolicyVersion`
+ **CloudWatch Logs permissions:**
  + `logs:CreateLogGroup`
  + `logs:CreateLogStream`
  + `logs:PutLogEvents`
  + `logs:DeleteLogGroup`

To run this runbook, the `AutomationAssumeRole` or your IAM user requires the following actions. The following example shows a least-privilege IAM policy that scopes permissions to specific resource patterns used by the automation:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "kafka:DescribeClusterV2",
                "kafka:GetBootstrapBrokers"
            ],
            "Resource": "arn:aws:kafka:{{REGION}}:{{ACCOUNTID}}:cluster/*/*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "cloudwatch:GetMetricData"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeNetworkInterfaces",
                "ec2:DescribeRouteTables",
                "ec2:DescribeNetworkAcls",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeSubnets",
                "ec2:DescribeVpcs",
                "ec2:CreateNetworkInsightsPath",
                "ec2:StartNetworkInsightsAnalysis",
                "ec2:DescribeNetworkInsightsPaths",
                "ec2:DescribeNetworkInsightsAnalyses",
                "ec2:DeleteNetworkInsightsPath",
                "ec2:DeleteNetworkInsightsAnalysis",
                "ec2:DeleteNetworkInterface"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "cloudformation:CreateStack",
                "cloudformation:DeleteStack",
                "cloudformation:DescribeStacks",
                "cloudformation:DescribeStackResources"
            ],
            "Resource": "arn:aws:cloudformation:{{REGION}}:{{ACCOUNTID}}:stack/msk-connectivity-test-stack-*/*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "lambda:InvokeFunction",
                "lambda:CreateFunction",
                "lambda:DeleteFunction",
                "lambda:GetFunction",
                "lambda:UpdateFunctionConfiguration",
                "lambda:TagResource"
            ],
            "Resource": "arn:aws:lambda:{{REGION}}:{{ACCOUNTID}}:function:msk-connectivity-test-*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "iam:GetRole",
                "iam:GetRolePolicy",
                "iam:ListRolePolicies",
                "iam:ListAttachedRolePolicies",
                "iam:GetPolicy",
                "iam:GetPolicyVersion"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "iam:CreateRole",
                "iam:DeleteRole",
                "iam:PutRolePolicy",
                "iam:DeleteRolePolicy",
                "iam:AttachRolePolicy",
                "iam:DetachRolePolicy",
                "iam:TagRole"
            ],
            "Resource": "arn:aws:iam::{{ACCOUNTID}}:role/msk-connectivity-test-*"
        },
        {
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::{{ACCOUNTID}}:role/msk-connectivity-test-*",
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": "lambda.amazonaws.com"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents",
                "logs:DeleteLogGroup"
            ],
            "Resource": "arn:aws:logs:{{REGION}}:{{ACCOUNTID}}:log-group:/aws/lambda/msk-connectivity-test-*"
        }
    ]
}
```

## Instructions
<a name="automation-awssupport-troubleshootmskclusterconnection-instructions"></a>

1. Navigate to the [AWSSupport-TroubleshootMSKClusterConnection](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootMSKClusterConnection/description) page in the AWS Systems Manager console.

1. Choose **Execute automation**.

1. For the input parameters, enter the following:
   + **`AutomationAssumeRole` (Optional):**

     The ARN of the IAM role that allows AWS Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
   + **`ClusterARN` (Required):**

     Enter the ARN of the Amazon MSK cluster experiencing connectivity issues. You can find this in the Amazon MSK console or by using the `aws kafka list-clusters` command.
   + **`BootstrapEndpoints` (Required):**

     Enter the bootstrap broker endpoint(s) for your Amazon MSK cluster. You can find these in the Amazon MSK console under cluster details, or by using the `aws kafka get-bootstrap-brokers` command. For multiple brokers, separate them with commas (for example, `b-1.mycluster.abc123.kafka.us-east-1.amazonaws.com:9092,b-2.mycluster.abc123.kafka.us-east-1.amazonaws.com:9092`).
   + **`ClientVPC` (Required):**

     Enter the Amazon VPC ID where your client application or resource attempting to connect to the Amazon MSK cluster is located.
   + **`ClientSubnet` (Required):**

     Enter the subnet ID within the `ClientVPC` where your client resource resides. This is used for the connectivity test Lambda function deployment.
   + **`ClientSecurityGroups` (Required):**

     Enter the security group ID(s) attached to your client resource. For multiple security groups, separate them with commas (for example, `sg-abc123,sg-def456`).
   + **`LambdaAssumeRole` (Optional):**

     If you have a pre-configured IAM role with Lambda execution and Amazon VPC access permissions, provide its ARN here. If you leave this empty, the automation creates a temporary role for the connectivity test.
   + **`ClientIAMRole` (Optional):**

     For IAM-authenticated connections (using ports 9098 or 9198), provide the ARN of the IAM role your client uses to authenticate to Amazon MSK. This enables the automation to analyze IAM permissions for required Amazon MSK access.
   + **`RetainResources` (Optional):**

     Set to `true` if you want to keep the Amazon VPC Reachability Analyzer network insights paths and analyses for further investigation. Set to `false` (default) to automatically clean up these resources after the automation completes.

1. Choose **Execute**.

1. Monitor the automation execution. The runbook typically completes in 5-15 minutes, depending on the complexity of network analysis required.

1. Review the **Outputs** section for detailed findings:
   + **BrokerHealthIssues:** List of identified broker performance problems (high CPU, memory, disk usage, credit exhaustion).
   + **NetworkConnectivityIssues:** Network-related problems such as security group misconfigurations, NACL restrictions, routing issues, or Amazon VPC Reachability Analyzer findings.
   + **`IAMAuthenticationIssues`:** IAM permission problems for IAM-authenticated connections, including missing or insufficient permissions.
   + **AuthenticationDocumentation:** Links to relevant AWS documentation for resolving authentication issues.
   + **TroubleshootingSummary:** Comprehensive summary with actionable recommendations for resolving all identified issues.

## Common issues and resolutions
<a name="automation-awssupport-troubleshootmskclusterconnection-common-issues"></a>
+ **Security group misconfiguration:** Ensure the client's security group allows outbound traffic to the Amazon MSK cluster's security group on the appropriate port (`9092` for `PLAINTEXT`, `9094` for `TLS`, `9096` for `SASL_SCRAM`, `9098` for `SASL_IAM`, or `9198` for IAM over `TLS`). The Amazon MSK cluster's security group must allow inbound traffic from the client's security group.
+ **Network ACL restrictions:** Verify that the subnet's Network ACL allows both inbound and outbound traffic for the required ports. Remember that NACLs are stateless and require rules for both directions.
+ **Routing issues:** Ensure the client subnet has a route to reach the Amazon MSK cluster's private IP addresses, typically through a route table with local Amazon VPC CIDR.
+ **IAM authentication failures:** For IAM-authenticated connections, verify that the client IAM role has the `kafka-cluster:Connect` action in its policy with the correct cluster ARN as the resource.
+ **Broker performance issues:** If brokers show high resource utilization, consider scaling up broker instance types, adding more brokers, or optimizing producer/consumer configurations.
+ **DNS resolution failures:** Verify that the client Amazon VPC has DNS resolution enabled (enableDnsHostnames and enableDnsSupport set to true in Amazon VPC settings).

## Troubleshooting the automation
<a name="automation-awssupport-troubleshootmskclusterconnection-troubleshooting"></a>
+ If the automation fails during CloudFormation stack creation, check that the execution role has the required IAM permissions for creating Lambda functions, IAM roles, and network interfaces.
+ If the connectivity test Lambda function fails to invoke, verify that the ClientSubnet has available IP addresses and that the ClientSecurityGroups allow the necessary outbound connections.
+ If Amazon VPC Reachability Analyzer analysis fails, ensure you have not exceeded the service quotas for network insights paths or analyses in your Region.
+ If IAM policy analysis fails, verify that the `ClientIAMRole` ARN is correct and that the automation role has permission to retrieve the role's policies.

## Resources
<a name="automation-awssupport-troubleshootmskclusterconnection-resources"></a>

Systems Manager Automation
+ [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootMSKClusterConnection/description)
+ [Run an automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-working-executing.html)
+ [Setting up an Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-setup.html)
+ [AWS Support Automation Workflows (SAW) on the AWS website](https://aws.amazon.com/premiumsupport/technology/saw/)

## Additional resources
<a name="automation-awssupport-troubleshootmskclusterconnection-additional-resources"></a>
+ [Amazon MSK troubleshooting guide](https://docs.aws.amazon.com/msk/latest/developerguide/troubleshooting.html)
+ [Accessing an Amazon MSK cluster](https://docs.aws.amazon.com/msk/latest/developerguide/client-access.html)
+ [IAM access control for Amazon MSK clusters](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html)
+ [Monitoring Amazon MSK with CloudWatch](https://docs.aws.amazon.com/msk/latest/developerguide/metrics-details.html)
+ [Amazon VPC Reachability Analyzer](https://docs.aws.amazon.com/vpc/latest/reachability/what-is-reachability-analyzer.html)