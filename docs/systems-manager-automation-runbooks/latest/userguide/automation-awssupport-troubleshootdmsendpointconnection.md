# `AWSSupport-TroubleshootDMSEndpointConnection`

**Description**

The **AWSSupport-TroubleshootDMSEndpointConnection** runbook helps diagnose and troubleshoot connectivity issues between AWS Database Migration Service replication instances and AWS DMS endpoints. The automation uses [Reachability Analyzer](../../../vpc/latest/reachability/what-is-reachability-analyzer.md "../../../vpc/latest/reachability/what-is-reachability-analyzer.md")
checks to test network connectivity and analyzes the network configuration to identify potential connectivity problems that could prevent successful AWS DMS migrations.

###### Important

You must have tested the connectivity between the AWS DMS replication instance and endpoint using the AWS DMS console or API before running this runbook. If you haven't tested the connection, please do so first, otherwise you may need to rerun this runbook. Both the AWS DMS replication instance and endpoint must be in an available state for accurate connectivity testing.

###### Important

This runbook creates and invokes AWS Lambda functions, which will incur Lambda charges. Each Reachability Analyzer analysis run also incurs charges. For pricing details, see the [Amazon VPC Pricing](https://aws.amazon.com/vpc/pricing/ "https://aws.amazon.com/vpc/pricing/") page under the Network Analysis tab and [AWS Lambda Pricing](https://aws.amazon.com/lambda/pricing/ "https://aws.amazon.com/lambda/pricing/").

**How does it work?**

The runbook performs a systematic analysis of AWS DMS connectivity through the following phases:

**Phase 1: Resource Validation and Prerequisites**

- **Endpoint Validation**: Verifies the AWS DMS endpoint exists, retrieves its configuration (server name, port, engine type), and confirms the database engine is supported for troubleshooting.
- **Connection Test Status**: Retrieves the current connection test status between the replication instance and endpoint using the AWS DMS `DescribeConnections` API, including any failure messages from previous test attempts.
- **Replication Instance Analysis**: Gathers network configuration details including Amazon VPC ID, subnet IDs, security group IDs, and identifies the associated Elastic Network Interface (ENI) for the replication instance.
  **Phase 2: DNS Resolution and Network Path Discovery**

- **Amazon VPC-based DNS Resolution**: Creates a temporary Lambda function within the same Amazon VPC as the replication instance to resolve the endpoint hostname to its IP address from within the Amazon VPC context, ensuring accurate private DNS resolution.
- **Target Identification**: Determines the appropriate target for Reachability Analyzer based on whether the endpoint is within the same Amazon VPC (uses ENI) or external (uses resolved IP address).
- **IPv6 Compatibility Check**: Validates that resolved addresses are IPv4, as Reachability Analyzer does not support IPv6 addresses.
  **Phase 3: Comprehensive Network Path Analysis**

- **Reachability Analyzer Execution**: Creates a Network Insights Path from the replication instance ENI to the target (endpoint ENI or IP address) and executes a comprehensive analysis to test TCP connectivity on the specified port.
- **Multi-layer Network Analysis**: Examines the complete network path including route tables, security groups, network ACLs, internet gateways, NAT gateways, Amazon VPC peering connections, and transit gateways to identify connectivity barriers.
- **Detailed Explanation Generation**: For failed connectivity, provides specific explanations for each network component that blocks traffic, including exact rule numbers, CIDR blocks, port ranges, and protocol restrictions.
  **Phase 4: Report Generation and Resource Cleanup**

- **Comprehensive Reporting**: Generates a detailed report containing connection test summary, network path analysis results, and specific failure explanations with remediation guidance.
- **Resource Management**: Automatically cleans up created resources (Lambda function, IAM roles, Network Insights Paths) unless the PersistReachabilityAnalyzerResults parameter is set to retain analysis results for further investigation.
- **Error Handling**: Provides specific error reports for various failure scenarios including unsupported database engines, missing resources, DNS resolution failures, and permission issues.
  The runbook supports troubleshooting connectivity for multiple database engines including Amazon Aurora, Amazon DocumentDB, Amazon DynamoDB, Amazon Neptune, Amazon Redshift, Amazon S3, Azure SQL Database, DB2, MySQL, Oracle, PostgreSQL, SQL Server, and many others.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootDMSEndpointConnection "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootDMSEndpointConnection")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

/

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `cloudformation:CreateStack`
- `cloudformation:DeleteStack`
- `cloudformation:DescribeStacks`
- `cloudformation:DescribeStackEvents`
- `dms:DescribeEndpoints`
- `dms:DescribeReplicationInstances`
- `dms:DescribeConnections`
- `iam:GetRole`
- `iam:PassRole`
- `iam:SimulatePrincipalPolicy`
- `lambda:CreateFunction`
- `lambda:DeleteFunction`
- `lambda:GetFunction`
- `lambda:InvokeFunction`
- `lambda:ListTags`
- `lambda:TagResource`
- `lambda:UntagResource`
- `lambda:UpdateFunctionCode`

**Optional IAM permissions**

The following permissions are only required within the `AutomationAssumeRole` if you do not provide a `LambdaRoleArn` parameter and want the automation to create the Lambda execution role for you:

- `iam:CreateRole`
- `iam:DeleteRole`
- `iam:AttachRolePolicy`
- `iam:DetachRolePolicy`
- `iam:TagRole`
- `iam:UntagRole`

###### Important

In addition to the above mentioned actions, the `AutomationAssumeRole`
should have the [AmazonVPCReachabilityAnalyzerFullAccessPolicy](../../../aws-managed-policy/latest/reference/AmazonVPCReachabilityAnalyzerFullAccessPolicy.md "../../../aws-managed-policy/latest/reference/AmazonVPCReachabilityAnalyzerFullAccessPolicy.md") as an [attached
managed policy](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") so that the [Reachability Analyzer](../../../vpc/latest/reachability/what-is-reachability-analyzer.md "../../../vpc/latest/reachability/what-is-reachability-analyzer.md") tests
are performed successfully.

Example Policy:

```

        {
            "Version": "2012-10-17"		 	 	 ,
            "Statement": [
                {
                    "Sid": "AllowDMSTroubleshootingActions",
                    "Effect": "Allow",
                    "Action": [
                        "dms:DescribeEndpoints",
                        "dms:DescribeReplicationInstances",
                        "dms:DescribeConnections",
                        "lambda:GetFunction",
                        "lambda:ListTags",
                        "lambda:CreateFunction",
                        "lambda:DeleteFunction",
                        "lambda:TagResource",
                        "lambda:UntagResource",
                        "lambda:UpdateFunctionCode",
                        "cloudformation:DescribeStacks",
                        "cloudformation:DescribeStackEvents",
                        "cloudformation:CreateStack",
                        "cloudformation:DeleteStack",
                        "iam:GetRole",
                        "iam:SimulatePrincipalPolicy",
                        "iam:CreateRole",
                        "iam:DeleteRole",
                        "iam:TagRole",
                        "iam:UntagRole"
                    ],
                    "Resource": "*"
                },
                {
                    "Sid": "AllowDMSLambdaInvocation",
                    "Effect": "Allow",
                    "Action": [
                        "lambda:InvokeFunction"
                    ],
                    "Resource": "arn:*:lambda:*:*:function:AWSSupport-TroubleshootDMSEndpointConnection-*"
                },
                {
                    "Sid": "AllowPassRoleToDMSLambda",
                    "Effect": "Allow",
                    "Action": [
                        "iam:PassRole"
                    ],
                    "Resource": "arn:*:iam::*:role/AWSSupport-TroubleshootDMSEndpointConnection-*",
                    "Condition": {
                        "StringLikeIfExists": {
                            "iam:PassedToService": "lambda.amazonaws.com"
                        }
                    }
                },
                {
                    "Sid": "AllowRolePolicyManagement",
                    "Effect": "Allow",
                    "Action": [
                        "iam:AttachRolePolicy",
                        "iam:DetachRolePolicy"
                    ],
                    "Resource": "*",
                    "Condition": {
                        "StringLikeIfExists": {
                            "iam:ResourceTag/AWSSupport-TroubleshootDMSEndpointConnection": "true"
                        }
                    }
                }
            ]
        }

```

**Instructions**

Follow these steps to configure the automation:

1. Navigate to [`AWSSupport-TroubleshootDMSEndpointConnection`](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootDMSEndpointConnection/description "https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootDMSEndpointConnection/description") in Systems Manager under Documents.
2. Select **Execute automation.**
3. For the input parameters, enter the following:
   - **AutomationAssumeRole (Optional):**
     - Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
       (IAM) role that allows SSM Automation to perform the actions on
       your behalf. If no role is specified, SSM Automation uses
       the permissions of the user who starts this runbook.
     - Type: `AWS::IAM::Role::Arn`

   - **DmsEndpointArn (Required)**
     - Description: (Required) The Amazon Resource Name (ARN) of the AWS Database Migration Service Endpoint.
     - Type: `String`
     - Allowed Pattern:
       `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):dms:[a-z0-9-]+:\\d{12}:endpoint:[A-Z0-9]{1,48}$`

   - **DmsReplicationInstanceArn (Required)**
     - Description: (Required) The Amazon Resource Name (ARN) of the AWS Database Migration Service Replication instance.
     - Type: `String`
     - Allowed Pattern:
       `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):dms:[a-z0-9-]+:\\d{12}:rep:[A-Z0-9]+$`

   - **PersistReachabilityAnalyzerResults (Optional)**
     - Description: (Optional) The flag informing if the results of the Network Insights Analysis execution should be kept or not.
     - Type: `Boolean`
     - Allowed Values:
       `[true, false]`
     - Default: `false`

   - **LambdaRoleArn (Optional)**
     - Description: (Optional) The Amazon Resource Name (ARN) of the AWS AWS Identity and Access Management (IAM) role that allows the AWS Lambda function to access the required AWS services and resources. If no role is specified, this Systems Manager Automation will create one IAM role for Lambda in your account.
     - Type: `AWS::IAM::Role::Arn`
     - Default: `""`

   - **Acknowledge (Required)**
     - Description: (Required) Enter `yes` to acknowledge that this runbook will create a Lambda function in your account and will create an IAM role if no `LambdaRoleArn` is provided.
     - Type: `String`
     - Allowed Pattern:
       `^[Yy][Ee][Ss]$`

4. Select **Execute.**
5. The automation initiates.
6. The document performs the following steps:
   - **DescribeEndpointAndCheckEngine:**

   Retrieves the AWS DMS endpoint configuration and validates if the database engine type is supported for troubleshooting. Extracts server name, port, and engine type from the endpoint configuration.
   - **BranchOnEndpointAndCheckEngineErrors:**

   Branches the automation based on any errors from the endpoint validation. If errors are found, the automation proceeds to generate an error report; otherwise, it continues with connectivity testing.
   - **GetTestConnectionStatus:**

   Retrieves the connection status and error message for the AWS DMS endpoint using the `DescribeConnections` API. This step checks if a connection test has been performed and captures any failure messages.
   - **BranchOnTestConnectionStatusErrors:**

   Branches the automation based on connection test status errors. If errors are detected, the automation generates an error report; otherwise, it proceeds with replication instance analysis.
   - **DescribeReplicationInstance:**

   Retrieves network configuration details for the AWS DMS replication instance including Amazon VPC ID, subnet IDs, security group IDs, and identifies the associated Elastic Network Interface (ENI).
   - **ValidateResourcePermissions:**

   Validates that the execution role has necessary permissions to clean up resources that will be created during the automation process.
   - **CreateDNSResolverLambda:**

   Creates a AWS CloudFormation stack containing a Lambda function deployed within the same Amazon VPC as the replication instance. This function is used to resolve DNS names to private IP addresses from within the Amazon VPC context.
   - **DescribeCloudFormationErrorFromStackEvents:**

   If the CloudFormation stack creation fails, this step describes errors from the stack events to provide detailed failure information for troubleshooting.
   - **GetDNSResolverLambdaName:**

   Retrieves the name of the DNS resolver Lambda function from the CloudFormation stack outputs for use in subsequent steps.
   - **ResolveDmsEndpoint:**

   Invokes the Lambda function to resolve the AWS DMS endpoint hostname to its IP address from within the Amazon VPC. This ensures accurate private DNS resolution and validates IPv4 compatibility.
   - **BranchOnResolveDmsEndpointErrors:**

   Branches the automation based on DNS resolution errors. If the endpoint cannot be resolved or resolves to an IPv6 address, the automation generates an error report.
   - **GetReachabilityAnalyzerTarget:**

   Identifies the appropriate target for Reachability Analyzer based on Amazon VPC configuration and endpoint location. Determines whether to use an ENI (for same-Amazon VPC endpoints) or IP address (for external endpoints) as the target.
   - **GenerateErrors:**

   Creates a comprehensive error report when failures occur in previous steps. This includes details about endpoint validation errors, connection test failures, or DNS resolution issues with specific remediation guidance.
   - **GenerateReport:**

   Creates a comprehensive troubleshooting report containing connection status, network path analysis results using Reachability Analyzer, detailed explanations of connectivity barriers, and recommended actions for resolution.
   - **CheckStackExists:**

   Checks if the CloudFormation stack was successfully created and needs to be deleted during cleanup. This step ensures proper resource management regardless of automation success or failure.
   - **DeleteDNSResolverLambda:**

   Deletes the CloudFormation stack containing the DNS resolver Lambda function and associated resources (unless `PersistReachabilityAnalyzerResults` is set to `true`), ensuring no residual resources remain after automation completion.

7. After completed, review the **Outputs** section for the detailed results of the execution:
   - **GetTestConnectionStatus.status**

   The current connection test status between the AWS DMS replication instance and endpoint (e.g., successful, failed, testing).
   - **DescribeCloudFormationErrorFromStackEvents.Events**

   If CloudFormation stack creation fails, this output contains detailed error events from the stack creation process to help diagnose infrastructure deployment issues.
   - **GenerateReport.report**

   A comprehensive troubleshooting report containing connection analysis results, Reachability Analyzer findings, network path analysis, specific connectivity barriers identified, and detailed remediation recommendations with links to relevant AWS documentation.
   - **GenerateErrors.report**

   If errors occur during the automation process, this output provides a detailed error report including specific failure reasons, affected resources, and guidance for resolving the issues before retrying the automation.

**References**

Systems Manager Automation

- [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootDMSEndpointConnection/description "https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootDMSEndpointConnection/description")
- [Run an automation](../../../systems-manager/latest/userguide/automation-working-executing.md "../../../systems-manager/latest/userguide/automation-working-executing.md")
- [Setting up an Automation](../../../systems-manager/latest/userguide/automation-setup.md "../../../systems-manager/latest/userguide/automation-setup.md")
- [Support Automation Workflows landing page](https://aws.amazon.com/premiumsupport/technology/saw/ "https://aws.amazon.com/premiumsupport/technology/saw/")
