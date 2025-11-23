# `AWSSupport-SetupK8sApiProxyForEKS`

**Description**

The **AWSSupport-SetupK8sApiProxyForEKS** automation runbook
provides a way to create an AWS Lambda function that acts as a proxy for making control plane
API calls to the Amazon Elastic Kubernetes Service cluster endpoint. It serves as a building block for runbooks
which require making control plane API calls for automating tasks and troubleshooting issues
with an Amazon EKS cluster.

###### Important

All the resources created by this automation are tagged so that they can be easily
found. The tags used are:

- `AWSSupport-SetupK8sApiProxyForEKS`: true

###### Note

- The automation is a helper runbook and cannot be executed as a standalone
  runbook. It is invoked as a child automation for runbooks which require control
  plane API calls to Amazon EKS cluster.
- Please ensure to run `Cleanup` operation after usage to avoid
  incurring unwanted costs.
  **Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux

**Parameters**

- AutomationAssumeRole

Type: String

Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
(IAM) role that allows Systems Manager Automation to perform the actions on your
behalf. If no role is specified, Systems Manager Automation uses the permissions of
the user that starts this runbook.

- ClusterName

Type: String

Description: (Required) The name of the Amazon Elastic Kubernetes Service cluster.

- Operation

Type: String

Description: (Required) Operation to perform: `Setup` provisions the
Lambda function in the account, `Cleanup` will de-provision resources
created as part of setup phase.

Allowed Values: `Setup` | `Cleanup`

Default: Setup

- LambdaRoleArn

Type: String

Description: (Optional) The ARN of the IAM role that allows the AWS Lambda
function to access the required AWS services and resources. If no role is
specified, this Systems Manager Automation will create one IAM role for Lambda in your
account with the name `Automation-K8sProxy-Role-<ExecutionId>` that
includes the managed policies: `AWSLambdaBasicExecutionRole` and
`AWSLambdaVPCAccessExecutionRole`.

**How does it work?**

The runbook performs the following steps:

- Validates that the automation is running as a child execution. The runbook will
  not work when invoked as a standalone runbook since it does not perform any
  meaningful work on its own.
- Checks for existing CloudFormation stack for the proxy Lambda function for the specified
  cluster.
  - If the stack exists, the existing infrastructure is re-used instead of
    re-creating it.
  - A reference counter is maintained using tags to ensure a runbook does not
    delete the infrastructure if it is being re-used by another runbook for the
    same cluster.

- Perform the operation type (`Setup`/`Cleanup`) specified for
  the invocation:
  - **Setup:** Creates or describes existing
    resources.

  **Cleanup:** Removes provisioned resources,
  if the infrastructure is not being used by any other runbook.

**Required IAM Permissions**

The `AutomationAssumeRole` parameter requires the following permissions given
`LambdaRoleArn` is not passed:

- `cloudformation:CreateStack`
- `cloudformation:DescribeStacks`
- `cloudformation:DeleteStack`
- `cloudformation:UpdateStack`
- `ec2:CreateNetworkInterface`
- `ec2:DescribeNetworkInterfaces`
- `ec2:DescribeRouteTables`
- `ec2:DescribeSecurityGroups`
- `ec2:DescribeSubnets`
- `ec2:DescribeVpcs`
- `ec2:DeleteNetworkInterface`
- `eks:DescribeCluster`
- `lambda:CreateFunction`
- `lambda:DeleteFunction`
- `lambda:ListTags`
- `lambda:GetFunction`
- `lambda:ListTags`
- `lambda:TagResource`
- `lambda:UntagResource`
- `lambda:UpdateFunctionCode`
- `logs:CreateLogGroup`
- `logs:PutRetentionPolicy`
- `logs:TagResource`
- `logs:UntagResource`
- `logs:DescribeLogGroups`
- `logs:DescribeLogStreams`
- `logs:ListTagsForResource`
- `iam:CreateRole`
- `iam:AttachRolePolicy`
- `iam:DetachRolePolicy`
- `iam:PassRole`
- `iam:GetRole`
- `iam:DeleteRole`
- `iam:TagRole`
- `iam:UntagRole`
- `tag:GetResources`
- `tag:TagResources`
  When `LambdaRoleArn` is provided, the automation does not need to create the
  role and the following permissions can be excluded:

- `iam:CreateRole`
- `iam:DeleteRole`
- `iam:TagRole`
- `iam:UntagRole`
- `iam:AttachRolePolicy`
- `iam:DetachRolePolicy`
  Below is an example policy demonstrating permissions required for `AutomationAssumeRole` when `LambdaRoleArn` is not passed:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "tag:GetResources",
 "tag:TagResources",
 "ec2:CreateNetworkInterface",
 "ec2:DescribeNetworkInterfaces",
 "ec2:DescribeRouteTables",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeSubnets",
 "ec2:DescribeVpcs",
 "ec2:DeleteNetworkInterface",
 "eks:DescribeCluster",
 "iam:GetRole",
 "cloudformation:DescribeStacks",
 "logs:DescribeLogGroups",
 "logs:DescribeLogStreams",
 "lambda:GetFunction",
 "lambda:ListTags",
 "logs:ListTagsForResource"
 ],
 "Resource": "*",
 "Effect": "Allow",
 "Sid": "AllowActionsWithoutConditions"
 },
 {
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/AWSSupport-SetupK8sApiProxyForEKS": "true"
 }
 },
 "Action": "iam:CreateRole",
 "Resource": [
 "arn:aws:iam::`111122223333`:role/Automation-K8sProxy*"
 ],
 "Effect": "Allow",
 "Sid": "AllowCreateRoleWithRequiredTag"
 },
 {
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/AWSSupport-SetupK8sApiProxyForEKS": "true"
 }
 },
 "Action": [
 "iam:DeleteRole",
 "iam:TagRole",
 "iam:UntagRole"
 ],
 "Resource": [
 "arn:aws:iam::`111122223333`:role/Automation-K8sProxy*"
 ],
 "Effect": "Allow",
 "Sid": "IAMActions"
 },
 {
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/AWSSupport-SetupK8sApiProxyForEKS": "true"
 },
 "StringLike": {
 "iam:PolicyARN": [
 "arn:aws:iam::`111122223333`:policy/service-role/AWSLambdaBasicExecutionRole",
 "arn:aws:iam::`111122223333`:policy/service-role/AWSLambdaVPCAccessExecutionRole"
 ]
 }
 },
 "Action": [
 "iam:AttachRolePolicy",
 "iam:DetachRolePolicy"
 ],
 "Resource": [
 "arn:aws:iam::`111122223333`:role/Automation-K8sProxy*"
 ],
 "Effect": "Allow",
 "Sid": "AttachRolePolicy"
 },
 {
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/AWSSupport-SetupK8sApiProxyForEKS": "true"
 }
 },
 "Action": [
 "lambda:CreateFunction",
 "lambda:DeleteFunction",
 "lambda:TagResource",
 "lambda:UntagResource",
 "lambda:UpdateFunctionCode"
 ],
 "Resource": "arn:aws:lambda:`us-east-1`:`111122223333`:function:Automation-K8sProxy*",
 "Effect": "Allow",
 "Sid": "LambdaActions"
 },
 {
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/AWSSupport-SetupK8sApiProxyForEKS": "true"
 }
 },
 "Action": [
 "cloudformation:CreateStack",
 "cloudformation:DeleteStack",
 "cloudformation:UpdateStack"
 ],
 "Resource": "arn:aws:cloudformation:`us-east-1`:`111122223333`:stack/AWSSupport-SetupK8sApiProxyForEKS*",
 "Effect": "Allow",
 "Sid": "CloudFormationActions"
 },
 {
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/AWSSupport-SetupK8sApiProxyForEKS": "true"
 }
 },
 "Action": [
 "logs:CreateLogGroup",
 "logs:CreateLogStream",
 "logs:PutLogEvents",
 "logs:PutRetentionPolicy",
 "logs:TagResource",
 "logs:UntagResource"
 ],
 "Resource": [
 "arn:aws:logs:`us-east-1`:`111122223333`:log-group:/aws/lambda/Automation-K8sProxy*",
 "arn:aws:logs:`us-east-1`:`111122223333`:log-group:/aws/lambda/Automation-K8sProxy*:*"
 ],
 "Effect": "Allow",
 "Sid": "LogsActions"
 },
 {
 "Condition": {
 "StringLikeIfExists": {
 "iam:PassedToService": "lambda.amazonaws.com"
 }
 },
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::`111122223333`:role/Automation-K8sProxy-Role*"
 ],
 "Effect": "Allow",
 "Sid": "PassRoleToLambda"
 }
 ]
}`

```

In case the `LambdaRoleArn` is passed, please ensure that it has [AWSLambdaBasicExecutionRole](https://console.aws.amazon.com/iam/home?region=us-east-1#/policies/details/arn%3Aaws%3Aiam%3A%3Aaws%3Apolicy%2Fservice-role%2FAWSLambdaBasicExecutionRole "https://console.aws.amazon.com/iam/home?region=us-east-1#/policies/details/arn%3Aaws%3Aiam%3A%3Aaws%3Apolicy%2Fservice-role%2FAWSLambdaBasicExecutionRole") policy attached to it for public cluster and
additionally, [AWSLambdaVPCAccessExecutionRole](https://console.aws.amazon.com/iam/home?region=us-east-1#/policies/details/arn%3Aaws%3Aiam%3A%3Aaws%3Apolicy%2Fservice-role%2FAWSLambdaVPCAccessExecutionRole "https://console.aws.amazon.com/iam/home?region=us-east-1#/policies/details/arn%3Aaws%3Aiam%3A%3Aaws%3Apolicy%2Fservice-role%2FAWSLambdaVPCAccessExecutionRole") for private clusters.

**Resources Created**

The following resources are created during `Setup` operation:

1. AWS Lambda function
2. IAM Role: Lambda execution role, if not provided.
3. CloudWatch Log Group (Lambda Logs)

_Lambda function and execution role are retained until `Cleanup`
operation is executed. Lambda log group will be retained for 30 days or until manually
deleted._

**Instructions**

The runbook is a helper utility designed to be executed from within other runbooks as a
child automation. It facilitates the creation of infrastructure enabling the parent runbook
to make Amazon EKS K8s control plane API calls. In order to use the runbook, you can follow the
below steps from the context of the parent automation.

1. **Setup Phase**: Invoke the automation using `aws:executeAutomation` action operation from the runbook that would like
   to make Amazon EKS K8s control plane API calls with operation set to
   `Setup`.

Example of input parameters:

```
   {
     "AutomationAssumeRole": "<role-arn>",
     "ClusterName": "<eks-cluster-name>",
     "Operation": "Setup"
   }
```

The output of the `aws:executeAutomation` step will contain the ARN of
the proxy Lambda function. 2. **Using the Lambda Proxy**: Invoke the Lambda function
inside the `aws:executeScript` action using `boto3`'s `Lambda.Client.invoke(...)` with a list of API call paths and bearer token.
The Lambda function will perform HTTP `GET` calls to the specified path by
passing the bearer token as part of authorization header.

Example of Lambda invoke event:

```
   {
       "ApiCalls": ["/api/v1/pods/", ...],
       "BearerToken": "..."
   }
```

###### Note

The bearer token has to be generated as part of the parent automation script.
You need to ensure the principal executing the parent runbook has read-only
permission to the specified Amazon EKS cluster. 3. **Cleanup Phase**: Invoke the automation using `aws:executeAutomation` action operation from the runbook that would like
to make Amazon EKS K8s control plane API calls with operation set to
`Cleanup`.

Example of input parameters:

```
   {
     "AutomationAssumeRole": "<role-arn>",
     "ClusterName": "<eks-cluster-name>",
     "Operation": "Cleanup"
   }
```

**Automation Steps**

1. **ValidateExecution**
   - Verifies that the automation is not running as a standalone
     execution.

2. **CheckForExistingStack**
   - Checks if a CloudFormation stack was already provisioned for the specified cluster
     name.
   - Returns stack existence status and whether it's safe to delete.

3. **BranchOnIsStackExists**
   - Decision step that branches based on stack existence.
   - Routes to either update existing stack name or proceed with operation
     branching.

4. **UpdateStackName**
   - Updates the `StackName` variable with the existing stack's
     name.
   - Only executed if stack already exists.

5. **BranchOnOperation**
   - Routes the automation based on the `Operation` parameter
     (`Setup` /`Cleanup`).
   - For `Setup`: Routes to either create new stack or describe
     existing resources.
   - For `Cleanup`: Proceeds to stack deletion if safe to
     delete.

6. **GetClusterNetworkConfig**
   - Describes the Amazon EKS cluster to obtain VPC configuration.
   - Retrieves endpoint, VPC ID, subnet IDs, security group ID, and CA
     data.

7. **ProvisionResources**
   - Creates a CloudFormation stack with required resources.
   - Provisions Lambda function with necessary networking configuration.
   - Tags all resources for tracking and management.

8. **DescribeStackResources**
   - Retrieves information about the created/existing stack.
   - Gets the ARN of the provisioned Lambda function.

9. **BranchOnIsLambdaDeploymentRequired**
   - Determines if Lambda code deployment is needed.
   - Only proceeds to deployment for newly created stacks.

10. **DeployLambdaFunctionCode**
    - Deploys the Lambda function code using the deployment package.
    - Updates the function with the proxy implementation.

11. **AssertLambdaAvailable**
    - Verifies that the Lambda function code update was successful.
    - Waits for the function to be in `Successful` state.

12. **PerformStackCleanup**
    - Deletes the CloudFormation stack and associated resources.
    - Executed during `Cleanup` operation or on failure of `Setup` operation.

**Outputs**

_LambdaFunctionArn_: ARN of the proxy Lambda function

**References**

Systems Manager Automation

- [Run an
  automation](../../../systems-manager/latest/userguide/automation-working-executing.md "../../../systems-manager/latest/userguide/automation-working-executing.md")
- [Setting up an
  Automation](../../../systems-manager/latest/userguide/automation-setup.md "../../../systems-manager/latest/userguide/automation-setup.md")
- [Support Automation
  Workflows](https://aws.amazon.com/premiumsupport/technology/saw/ "https://aws.amazon.com/premiumsupport/technology/saw/")
