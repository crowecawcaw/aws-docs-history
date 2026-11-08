

# `AWSSupport-SetupK8sApiProxyForEKS`
<a name="automation-awssupport-setupk8sapiproxyforeks"></a>

 **Description** 

The **AWSSupport-SetupK8sApiProxyForEKS** automation runbook provides a way to create an AWS Lambda function that acts as a proxy for making control plane API calls to the Amazon Elastic Kubernetes Service cluster endpoint. It serves as a building block for runbooks which require making control plane API calls for automating tasks and troubleshooting issues with an Amazon EKS cluster.

**Important**  
All the resources created by this automation are tagged so that they can be easily found. The tags used are:  
 `AWSSupport-SetupK8sApiProxyForEKS`: true 

**Note**  
The automation is a helper runbook and cannot be executed as a standalone runbook. It is invoked as a child automation for runbooks which require control plane API calls to Amazon EKS cluster.
Please ensure to run `Cleanup` operation after usage to avoid incurring unwanted costs.

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux

**Parameters**
+ AutomationAssumeRole

  Type: String

  Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
+ ClusterName

  Type: String

  Description: (Required) The name of the Amazon Elastic Kubernetes Service cluster.
+ Operation

  Type: String

  Description: (Required) Operation to perform: `Setup` provisions the Lambda function in the account, `Cleanup` will de-provision resources created as part of setup phase.

  Allowed Values: `Setup` \| `Cleanup`

  Default: Setup
+ LambdaRoleArn

  Type: String

  Description: (Optional) The ARN of the IAM role that allows the AWS Lambda function to access the required AWS services and resources. If no role is specified, this Systems Manager Automation will create one IAM role for Lambda in your account with the name `Automation-K8sProxy-Role-<ExecutionId>` that includes the managed policies: `AWSLambdaBasicExecutionRole` and `AWSLambdaVPCAccessExecutionRole`.

 **How does it work?** 

 The runbook performs the following steps: 
+ Validates that the automation is running as a child execution. The runbook will not work when invoked as a standalone runbook since it does not perform any meaningful work on its own.
+ Checks for existing CloudFormation stack for the proxy Lambda function for the specified cluster.
  + If the stack exists, the existing infrastructure is re-used instead of re-creating it.
  + A reference counter is maintained using tags to ensure a runbook does not delete the infrastructure if it is being re-used by another runbook for the same cluster.
+ Perform the operation type (`Setup`/`Cleanup`) specified for the invocation:
  + **Setup:** Creates or describes existing resources.

    **Cleanup:** Removes provisioned resources, if the infrastructure is not being used by any other runbook.

 **Required IAM Permissions** 

This runbook runs under the `AutomationAssumeRole` of the runbook that calls it, so that role must have the following permissions in addition to its own. The policy assumes that you specify an existing role in `LambdaRoleArn`, so it grants no IAM write actions.

The role that you pass in `LambdaRoleArn` is the proxy function's execution role. It must trust `lambda.amazonaws.com` and have the `AWSLambdaBasicExecutionRole` managed policy. For a cluster with a private endpoint, it must also have the `AWSLambdaVPCAccessExecutionRole` managed policy.

Don't grant the execution role other permissions. Anyone with this policy can update and invoke the proxy function, and the function runs with the permissions of that role.

The `UnscopedActions` statement uses `"Resource": "*"` because those actions don't support resource-level permissions. In the following policy, replace these values:
+ {{REGION}} and {{ACCOUNTID}} – The AWS Region and account ID where the cluster runs.
+ {{CLUSTER\_NAME}} – The name of the cluster. If the calling runbook targets more than one cluster, add an entry for each one.
+ {{AUTOMATION\_ROLE\_NAME}} – The name of the role that you pass in `AutomationAssumeRole`.
+ {{LAMBDA\_ROLE\_NAME}} – The name of the role that you pass in `LambdaRoleArn`.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "UnscopedActions",
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeNetworkInterfaces",
                "ec2:DescribeRouteTables",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeSubnets",
                "ec2:DescribeVpcs",
                "logs:DescribeLogGroups",
                "ssm:DescribeAutomationExecutions",
                "tag:GetResources",
                "tag:TagResources"
            ],
            "Resource": "*"
        },
        {
            "Sid": "ReadCluster",
            "Effect": "Allow",
            "Action": "eks:DescribeCluster",
            "Resource": "arn:aws:eks:{{REGION}}:{{ACCOUNTID}}:cluster/{{CLUSTER_NAME}}"
        },
        {
            "Sid": "RunProxyRunbook",
            "Effect": "Allow",
            "Action": "ssm:StartAutomationExecution",
            "Resource": [
                "arn:aws:ssm:{{REGION}}:{{ACCOUNTID}}:automation-definition/AWSSupport-SetupK8sApiProxyForEKS:*",
                "arn:aws:ssm:{{REGION}}:{{ACCOUNTID}}:automation-execution/*"
            ]
        },
        {
            "Sid": "ReadProxyRunbookExecution",
            "Effect": "Allow",
            "Action": "ssm:GetAutomationExecution",
            "Resource": "arn:aws:ssm:{{REGION}}:{{ACCOUNTID}}:automation-execution/*"
        },
        {
            "Sid": "PassAutomationRoleToProxyRunbook",
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::{{ACCOUNTID}}:role/{{AUTOMATION_ROLE_NAME}}",
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": "ssm.amazonaws.com"
                }
            }
        },
        {
            "Sid": "ProxyStack",
            "Effect": "Allow",
            "Action": [
                "cloudformation:CreateStack",
                "cloudformation:DescribeStacks",
                "cloudformation:UpdateStack",
                "cloudformation:DeleteStack"
            ],
            "Resource": "arn:aws:cloudformation:{{REGION}}:{{ACCOUNTID}}:stack/AWSSupport-SetupK8sApiProxyForEKS-*/*"
        },
        {
            "Sid": "ProxyFunction",
            "Effect": "Allow",
            "Action": [
                "lambda:CreateFunction",
                "lambda:DeleteFunction",
                "lambda:GetFunction",
                "lambda:InvokeFunction",
                "lambda:ListTags",
                "lambda:TagResource",
                "lambda:UntagResource",
                "lambda:UpdateFunctionCode"
            ],
            "Resource": "arn:aws:lambda:{{REGION}}:{{ACCOUNTID}}:function:Automation-K8sProxy-*"
        },
        {
            "Sid": "ProxyLogGroup",
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:DescribeLogStreams",
                "logs:ListTagsForResource",
                "logs:PutRetentionPolicy",
                "logs:TagResource",
                "logs:UntagResource"
            ],
            "Resource": [
                "arn:aws:logs:{{REGION}}:{{ACCOUNTID}}:log-group:/aws/lambda/Automation-K8sProxy-*",
                "arn:aws:logs:{{REGION}}:{{ACCOUNTID}}:log-group:/aws/lambda/Automation-K8sProxy-*:*"
            ]
        },
        {
            "Sid": "ProxyNetworkInterfaces",
            "Effect": "Allow",
            "Action": [
                "ec2:CreateNetworkInterface",
                "ec2:DeleteNetworkInterface"
            ],
            "Resource": [
                "arn:aws:ec2:{{REGION}}:{{ACCOUNTID}}:network-interface/*",
                "arn:aws:ec2:{{REGION}}:{{ACCOUNTID}}:subnet/*",
                "arn:aws:ec2:{{REGION}}:{{ACCOUNTID}}:security-group/*"
            ]
        },
        {
            "Sid": "PassLambdaRole",
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::{{ACCOUNTID}}:role/{{LAMBDA_ROLE_NAME}}",
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": "lambda.amazonaws.com"
                }
            }
        }
    ]
}
```

The `ProxyNetworkInterfaces` statement is needed only for a cluster with a private endpoint, where the proxy function runs in the cluster's VPC.

If `LambdaRoleArn` is empty, or the calling runbook doesn't pass it, the automation creates the execution role itself. In that case, leave out the `PassLambdaRole` statement from the preceding policy and add the following statements.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CreateProxyLambdaRole",
            "Effect": "Allow",
            "Action": [
                "iam:CreateRole",
                "iam:TagRole"
            ],
            "Resource": "arn:aws:iam::{{ACCOUNTID}}:role/Automation-K8sProxy-Role-*",
            "Condition": {
                "StringEquals": {
                    "aws:RequestTag/AWSSupport-SetupK8sApiProxyForEKS": "true"
                }
            }
        },
        {
            "Sid": "ManageProxyLambdaRole",
            "Effect": "Allow",
            "Action": [
                "iam:GetRole",
                "iam:TagRole",
                "iam:UntagRole",
                "iam:DeleteRole"
            ],
            "Resource": "arn:aws:iam::{{ACCOUNTID}}:role/Automation-K8sProxy-Role-*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceTag/AWSSupport-SetupK8sApiProxyForEKS": "true"
                }
            }
        },
        {
            "Sid": "AttachLambdaManagedPoliciesOnly",
            "Effect": "Allow",
            "Action": [
                "iam:AttachRolePolicy",
                "iam:DetachRolePolicy"
            ],
            "Resource": "arn:aws:iam::{{ACCOUNTID}}:role/Automation-K8sProxy-Role-*",
            "Condition": {
                "ArnEquals": {
                    "iam:PolicyARN": [
                        "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole",
                        "arn:aws:iam::aws:policy/service-role/AWSLambdaVPCAccessExecutionRole"
                    ]
                }
            }
        },
        {
            "Sid": "PassProxyLambdaRole",
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::{{ACCOUNTID}}:role/Automation-K8sProxy-Role-*",
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": "lambda.amazonaws.com"
                }
            }
        }
    ]
}
```

The following list describes the value to replace in this policy and how each statement limits what the automation can do to the role that it creates:
+ {{ACCOUNTID}} – Your AWS account ID.
+ `CreateProxyLambdaRole` – Allows creating roles named `Automation-K8sProxy-Role-*` only when the request includes the `AWSSupport-SetupK8sApiProxyForEKS` tag set to `true`, which the `aws:RequestTag/AWSSupport-SetupK8sApiProxyForEKS` condition key checks. The automation adds this tag to every resource that it creates.
+ `ManageProxyLambdaRole` – Allows reading, tagging, and deleting only the roles that already carry that tag, which the `aws:ResourceTag/AWSSupport-SetupK8sApiProxyForEKS` condition key checks. The automation updates a reference-count tag on the CloudFormation stack, which is propagated to the role.
+ `AttachLambdaManagedPoliciesOnly` – The `iam:PolicyARN` condition allows attaching only `AWSLambdaBasicExecutionRole` and `AWSLambdaVPCAccessExecutionRole`. The policy grants no `iam:PutRolePolicy`, so the role can't be given any other permissions.
+ `PassProxyLambdaRole` – Allows passing those roles only to Lambda. This replaces the `PassLambdaRole` statement.

 **Resources Created** 

The following resources are created during `Setup` operation:

1. AWS Lambda function

1. IAM Role: Lambda execution role, if not provided.

1. CloudWatch Log Group (Lambda Logs)

 *Lambda function and execution role are retained until `Cleanup` operation is executed. Lambda log group will be retained for 30 days or until manually deleted.* 

 **Instructions** 

The runbook is a helper utility designed to be executed from within other runbooks as a child automation. It facilitates the creation of infrastructure enabling the parent runbook to make Amazon EKS K8s control plane API calls. In order to use the runbook, you can follow the below steps from the context of the parent automation.

1. **Setup Phase**: Invoke the automation using ` aws:executeAutomation` action operation from the runbook that would like to make Amazon EKS K8s control plane API calls with operation set to `Setup`.

   Example of input parameters:

   ```
      {
        "AutomationAssumeRole": "<role-arn>",
        "ClusterName": "<eks-cluster-name>",
        "Operation": "Setup"
      }
   ```

   The output of the `aws:executeAutomation` step will contain the ARN of the proxy Lambda function.

1. **Using the Lambda Proxy**: Invoke the Lambda function inside the `aws:executeScript` action using `boto3`'s ` Lambda.Client.invoke(...)` with a list of API call paths and bearer token. The Lambda function will perform HTTP `GET` calls to the specified path by passing the bearer token as part of authorization header.

   Example of Lambda invoke event:

   ```
      {
          "ApiCalls": ["/api/v1/pods/", ...],
          "BearerToken": "..."
      }
   ```
**Note**  
The bearer token has to be generated as part of the parent automation script. You need to ensure the principal executing the parent runbook has read-only permission to the specified Amazon EKS cluster.

1. **Cleanup Phase**: Invoke the automation using ` aws:executeAutomation` action operation from the runbook that would like to make Amazon EKS K8s control plane API calls with operation set to `Cleanup`.

   Example of input parameters:

   ```
      {
        "AutomationAssumeRole": "<role-arn>",
        "ClusterName": "<eks-cluster-name>",
        "Operation": "Cleanup"
      }
   ```

 **Automation Steps** 

1.  **ValidateExecution** 
   + Verifies that the automation is not running as a standalone execution.

1.  **CheckForExistingStack** 
   + Checks if a CloudFormation stack was already provisioned for the specified cluster name.
   + Returns stack existence status and whether it's safe to delete.

1.  **BranchOnIsStackExists** 
   + Decision step that branches based on stack existence.
   + Routes to either update existing stack name or proceed with operation branching.

1.  **UpdateStackName** 
   + Updates the `StackName` variable with the existing stack's name.
   + Only executed if stack already exists.

1.  **BranchOnOperation** 
   + Routes the automation based on the `Operation` parameter (`Setup` /`Cleanup`).
   + For `Setup`: Routes to either create new stack or describe existing resources.
   + For `Cleanup`: Proceeds to stack deletion if safe to delete.

1.  **GetClusterNetworkConfig** 
   + Describes the Amazon EKS cluster to obtain VPC configuration.
   + Retrieves endpoint, VPC ID, subnet IDs, security group ID, and CA data.

1.  **ProvisionResources** 
   + Creates a CloudFormation stack with required resources.
   + Provisions Lambda function with necessary networking configuration.
   + Tags all resources for tracking and management.

1.  **DescribeStackResources** 
   + Retrieves information about the created/existing stack.
   + Gets the ARN of the provisioned Lambda function.

1.  **BranchOnIsLambdaDeploymentRequired** 
   + Determines if Lambda code deployment is needed.
   + Only proceeds to deployment for newly created stacks.

1.  **DeployLambdaFunctionCode** 
   + Deploys the Lambda function code using the deployment package.
   + Updates the function with the proxy implementation.

1.  **AssertLambdaAvailable** 
   + Verifies that the Lambda function code update was successful.
   + Waits for the function to be in `Successful` state.

1.  **PerformStackCleanup** 
   + Deletes the CloudFormation stack and associated resources.
   + Executed during `Cleanup` operation or on failure of ` Setup` operation.

 **Outputs** 

*LambdaFunctionArn*: ARN of the proxy Lambda function

**References**

Systems Manager Automation
+ [Run an automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-working-executing.html)
+ [Setting up an Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-setup.html)
+ [Support Automation Workflows](https://aws.amazon.com/premiumsupport/technology/saw/)