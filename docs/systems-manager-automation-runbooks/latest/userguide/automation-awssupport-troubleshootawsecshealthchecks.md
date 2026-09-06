

# `AWSSupport-TroubleshootAWSECSHealthChecks`
<a name="automation-awssupport-troubleshootawsecshealthchecks"></a>

The `AWSSupport-TroubleshootAWSECSHealthChecks` runbook helps diagnose and troubleshoot issues where Amazon Elastic Container Service (Amazon ECS) tasks running on Amazon Elastic Compute Cloud (Amazon EC2) instances or AWS Fargate (Fargate) fail Application Load Balancer (ALB) health checks.

The runbook performs a systematic analysis by:

1. Verifying network connectivity between ALBs and Amazon ECS tasks

1. Checking if tasks are exiting unexpectedly

1. Analyzing target group health status and response codes

1. Examining ALB configuration and health check settings

1. Validating service configuration including health check grace periods

1. Performing custom diagnostics for response code mismatches

**Important**  
For advanced diagnostics, the runbook deploys temporary AWS Lambda (Lambda) functions within your Amazon Virtual Private Cloud (Amazon VPC) to simulate health check requests from the same network perspective as your ALB. A Lambda execution role is required for these functions and can either be specified as a parameter or created temporarily by this runbook.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootAWSECSHealthChecks) 

**Document type**

Automation

**Owner**

Amazon

**Platforms**

/

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `cloudformation:CreateChangeSet`
+ `cloudformation:CreateStack`
+ `cloudformation:DeleteStack`
+ `cloudformation:DescribeStacks`
+ `ec2:DescribeInstances`
+ `ec2:DescribeNetworkAcls`
+ `ec2:DescribeNetworkInterfaces`
+ `ec2:DescribeRouteTables`
+ `ec2:DescribeSecurityGroups`
+ `ec2:DescribeSubnets`
+ `ec2:DescribeVpcEndpointServices`
+ `ec2:DescribeVpcEndpoints`
+ `ec2:DescribeVpcs`
+ `ecs:DescribeClusters`
+ `ecs:DescribeContainerInstances`
+ `ecs:DescribeServices`
+ `ecs:DescribeTaskDefinition`
+ `ecs:DescribeTaskSets`
+ `ecs:DescribeTasks`
+ `ecs:ListTasks`
+ `elasticloadbalancing:DescribeListeners`
+ `elasticloadbalancing:DescribeLoadBalancerAttributes`
+ `elasticloadbalancing:DescribeLoadBalancers`
+ `elasticloadbalancing:DescribeRules`
+ `elasticloadbalancing:DescribeTargetGroupAttributes`
+ `elasticloadbalancing:DescribeTargetGroups`
+ `elasticloadbalancing:DescribeTargetHealth`
+ `iam:AttachRolePolicy`
+ `iam:CreateRole`
+ `iam:DeleteRole`
+ `iam:DetachRolePolicy`
+ `iam:GetRole`
+ `iam:ListRoles`
+ `iam:PassRole`
+ `iam:SimulateCustomPolicy`
+ `iam:SimulatePrincipalPolicy`
+ `iam:TagRole`
+ `lambda:CreateFunction`
+ `lambda:DeleteFunction`
+ `lambda:GetFunction`
+ `lambda:GetFunctionConfiguration`
+ `lambda:InvokeFunction`
+ `lambda:TagResource`
+ `servicequotas:GetServiceQuota`
+ `ssm:GetAutomationExecution`

Example IAM policy:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "cloudformation:CreateChangeSet",
                "cloudformation:CreateStack",
                "cloudformation:DeleteStack",
                "cloudformation:DescribeStacks",
                "ec2:DescribeInstances",
                "ec2:DescribeNetworkAcls",
                "ec2:DescribeNetworkInterfaces",
                "ec2:DescribeRouteTables",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeSubnets",
                "ec2:DescribeVpcEndpointServices",
                "ec2:DescribeVpcEndpoints",
                "ec2:DescribeVpcs",
                "ecs:DescribeClusters",
                "ecs:DescribeContainerInstances",
                "ecs:DescribeServices",
                "ecs:DescribeTaskDefinition",
                "ecs:DescribeTaskSets",
                "ecs:DescribeTasks",
                "ecs:ListTasks",
                "elasticloadbalancing:DescribeListeners",
                "elasticloadbalancing:DescribeLoadBalancerAttributes",
                "elasticloadbalancing:DescribeLoadBalancers",
                "elasticloadbalancing:DescribeRules",
                "elasticloadbalancing:DescribeTargetGroupAttributes",
                "elasticloadbalancing:DescribeTargetGroups",
                "elasticloadbalancing:DescribeTargetHealth",
                "iam:CreateRole",
                "iam:DeleteRole",
                "iam:DetachRolePolicy",
                "iam:GetRole",
                "iam:ListRoles",
                "iam:SimulateCustomPolicy",
                "iam:SimulatePrincipalPolicy",
                "iam:TagRole",
                "lambda:CreateFunction",
                "lambda:DeleteFunction",
                "lambda:GetFunction",
                "lambda:GetFunctionConfiguration",
                "lambda:InvokeFunction",
                "lambda:TagResource",
                "servicequotas:GetServiceQuota",
                "ssm:GetAutomationExecution"
            ],
            "Resource": "*"
        },
        {
            "Action": [
                "iam:AttachRolePolicy"
            ],
            "Resource": "arn:aws:iam::111122223333:role/AWSECSHealthChecks-*",
            "Condition": {
                "ArnLike": {
                    "iam:PolicyArn": "arn:aws:iam::aws:policy/service-role/AWSLambdaVPCAccessExecutionRole"
                }
            },
            "Effect": "Allow"
        },
        {
            "Action": [
                "iam:PassRole"
            ],
            "Resource": "arn:aws:iam::111122223333:role/AWSECSHealthChecks-*",
            "Effect": "Allow",
            "Condition": {
                "StringLikeIfExists": {
                    "iam:PassedToService": "lambda.amazonaws.com"
                }
            }
        }
    ]
}
```

`ExecutionResult.message` - A summary of findings from all diagnostic steps, including network connectivity, task health, target group status, and recommendations.

Follow these steps to configure the automation:

1. Open [AWSSupport-TroubleshootAWSECSHealthChecks](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootAWSECSHealthChecks/description) in Systems Manager under Documents.

1. Choose Execute automation.

1. For the input parameters, enter the following:
   + **ECSClusterName (Required):**

     The name of the Amazon ECS cluster.
   + **ECSServiceName (Required):**

     The name of the Amazon ECS service.
   + **LambdaExecutionRole (Optional):**

     The ARN of the Lambda execution role used for the custom health check diagnostics step. If no role is specified, the runbook skips the advanced diagnostics step or creates a temporary role.
   + **AutomationAssumeRole (Optional):**

     The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.

1. Choose Execute.

1. The automation initiates.

1. The document performs the following steps:
   + **`CheckPermissions`**:

     Verifies that the IAM user or role that started the automation has the required permissions.
   + **`CheckTargetClusterExistence`**:

     Checks if the specified Amazon ECS cluster exists and is active.
   + **`CheckEcsServiceExistence`**:

     Checks if the specified Amazon ECS service exists and is active.
   + **`CheckNetworkConnectivity`**:

     Checks network connectivity between the ALB and Amazon ECS tasks.
   + **`CheckTasksAreExiting`**:

     Checks if Amazon ECS tasks are exiting unexpectedly.
   + **`CheckTargetHealth`**:

     Checks the health status of targets in the target group.
   + **`CreateLambdaExecutionRole`**:

     Creates a temporary Lambda execution role if the `LambdaExecutionRole` parameter is not specified.
   + **`ExecuteCustomCheck`**:

     Deploys temporary Lambda functions to simulate health check requests and identify response code mismatches.
   + **`ExecuteAdditionalCheck`**:

     Performs additional checks on ALB configuration and health check grace periods.
   + **`DeleteLambdaExecutionRole`**:

     Deletes the temporary Lambda execution role and Lambda functions created during the diagnostic process.
   + **`ExecutionResult`**:

     Compiles all findings into a summary report with recommendations.

1. After completion, review the Outputs section for the detailed results of the execution.

Systems Manager Automation
+  [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootAWSECSHealthChecks/description) 
+  [Run an automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-working-executing.html) 
+  [Setting up an Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-setup.html) 
+  [Support Automation Workflows](https://aws.amazon.com/premiumsupport/technology/saw/) 