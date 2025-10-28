# `AWSSupport-TroubleshootEKSALBControllerIssues`

**Description**

The `AWSSupport-TroubleshootEKSALBControllerIssues` automation runbook helps diagnose common issues that prevent the AWS Load Balancer Controller from properly provisioning and managing Application Load Balancer (ALB) and Network Load Balancer (NLB) for Kubernetes ingresses and services.

This runbook performs end-to-end validation of essential components including OIDC identity provider setup, IRSA configuration, networking prerequisites, ingress/service configuration, and resource quotas. It also captures controller logs and relevant Kubernetes resource configurations to help identify misconfigurations or operational issues.

###### Important

This automation runbook is designed for Amazon EKS clusters using Amazon Elastic Compute Cloud (Amazon EC2) node groups and does not currently support clusters running on AWS Fargate.

**How does it work?**

The runbook `AWSSupport-TroubleshootEKSALBControllerIssues` performs the following high-level steps:

- Validates Amazon EKS cluster status, access entry configuration and OIDC provider setup.
- Creates temporary Lambda proxy for Kubernetes API communication.
- Checks AWS Load Balancer Controller deployment and service account configuration.
- Verifies pod identity webhook and IAM role injection.
- Validates subnet configuration and tagging for Application Load Balancer and Network Load Balancer provisioning.
- Checks Application Load Balancer and Network Load Balancer account quotas against current usage.
- Validates ingress and service resource annotations.
- Checks worker node security group tagging for load balancer integration.
- Collects controller pod logs for diagnostics.
- Cleans up temporary authentication resources.
- Generates diagnostic report with findings and remediation steps.

###### Note

- The Amazon EKS cluster must have an access entry configured for the IAM entity running this automation. The cluster's authentication mode must be set to either `API` or `API_AND_CONFIG_MAP`. Without proper access entry configuration, the automation will terminate during initial validation.
- The `LambdaRoleArn` parameter is required and must have the AWS managed policies `AWSLambdaBasicExecutionRole` and `AWSLambdaVPCAccessExecutionRole` attached to allow the proxy function to communicate with the Kubernetes API.
- The AWS Load Balancer Controller must be version `v2.1.1` or later.
- The automation includes a cleanup step that removes temporary authentication infrastructure resources. This cleanup step runs even when previous steps fail, ensuring no orphaned resources remain in your AWS account.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootEKSALBControllerIssues "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootEKSALBControllerIssues")

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
- `cloudformation:UpdateStack`
- `ec2:CreateNetworkInterface`
- `ec2:DeleteNetworkInterface`
- `ec2:DescribeInstances`
- `ec2:DescribeNetworkInterfaces`
- `ec2:DescribeRouteTables`
- `ec2:DescribeSecurityGroups`
- `ec2:DescribeSubnets`
- `ec2:DescribeVpcs`
- `eks:DescribeCluster`
- `eks:ListAssociatedAccessPolicies`
- `elasticloadbalancing:DescribeAccountLimits`
- `elasticloadbalancing:DescribeLoadBalancers`
- `iam:GetRole`
- `iam:ListOpenIDConnectProviders`
- `iam:PassRole`
- `lambda:CreateFunction`
- `lambda:DeleteFunction`
- `lambda:GetFunction`
- `lambda:InvokeFunction`
- `lambda:ListTags`
- `lambda:TagResource`
- `lambda:UntagResource`
- `lambda:UpdateFunctionCode`
- `logs:CreateLogGroup`
- `logs:CreateLogStream`
- `logs:DescribeLogGroups`
- `logs:DescribeLogStreams`
- `logs:ListTagsForResource`
- `logs:PutLogEvents`
- `logs:PutRetentionPolicy`
- `logs:TagResource`
- `logs:UntagResource`
- `ssm:DescribeAutomationExecutions`
- `ssm:GetAutomationExecution`
- `ssm:StartAutomationExecution`
- `tag:GetResources`
- `tag:TagResources`

**Instructions**

Follow these steps to configure and run the automation:

###### Note

Before running the automation, follow these steps to configure the required IAM roles: one for Systems Manager Automation to execute the runbook, and another for Lambda to communicate with the Kubernetes API:

1. Create a SSM automation role `TroubleshootEKSALBController-SSM-Role` in your account. Verify that the trust relationship contains the following policy.

```
{
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "",
                    "Effect": "Allow",
                    "Principal": {
                        "Service": "ssm.amazonaws.com"
                    },
                    "Action": "sts:AssumeRole"
                }
            ]
        }
```

2. Attach the following IAM policy to grant the required permissions:

```
{
            "Version": "2012-10-17",
            "Statement": [{
                "Sid": "TroubleshootEKSALBControllerIssuesActions",
                "Effect": "Allow",
                "Action": [
                    "eks:DescribeCluster",
                    "eks:ListAssociatedAccessPolicies",
                    "iam:GetRole",
                    "iam:ListOpenIDConnectProviders",
                    "ssm:StartAutomationExecution",
                    "ssm:GetAutomationExecution",
                    "ssm:DescribeAutomationExecutions",
                    "ec2:DescribeSubnets",
                    "ec2:DescribeRouteTables",
                    "elasticloadbalancing:DescribeLoadBalancers",
                    "elasticloadbalancing:DescribeAccountLimits",
                    "ec2:DescribeInstances",
                    "ec2:DescribeNetworkInterfaces",
                    "ec2:DescribeSecurityGroups"
                ],
                "Resource": "*"
            },
            {
                "Sid": "SetupK8sApiProxyForEKSActions",
                "Effect": "Allow",
                "Action": [
                    "cloudformation:CreateStack",
                    "cloudformation:DeleteStack",
                    "cloudformation:DescribeStacks",
                    "cloudformation:UpdateStack",
                    "ec2:CreateNetworkInterface",
                    "ec2:DeleteNetworkInterface",
                    "ec2:DescribeNetworkInterfaces",
                    "ec2:DescribeRouteTables",
                    "ec2:DescribeSecurityGroups",
                    "ec2:DescribeSubnets",
                    "ec2:DescribeVpcs",
                    "eks:DescribeCluster",
                    "iam:GetRole",
                    "lambda:CreateFunction",
                    "lambda:DeleteFunction",
                    "lambda:GetFunction",
                    "lambda:InvokeFunction",
                    "lambda:ListTags",
                    "lambda:TagResource",
                    "lambda:UntagResource",
                    "lambda:UpdateFunctionCode",
                    "logs:CreateLogGroup",
                    "logs:CreateLogStream",
                    "logs:DescribeLogGroups",
                    "logs:DescribeLogStreams",
                    "logs:ListTagsForResource",
                    "logs:PutLogEvents",
                    "logs:PutRetentionPolicy",
                    "logs:TagResource",
                    "logs:UntagResource",
                    "ssm:DescribeAutomationExecutions",
                    "tag:GetResources",
                    "tag:TagResources"
                ],
                "Resource": "*"
            },
            {
                "Sid": "PassRoleToAutomation",
                "Effect": "Allow",
                "Action": "iam:PassRole",
                "Resource": "*",
                "Condition": {
                    "StringLikeIfExists": {
                        "iam:PassedToService": [
                            "lambda.amazonaws.com",
                            "ssm.amazonaws.com"
                        ]
                    }
                }
            }]
        }
```

3. Configure access entry for your Amazon EKS cluster. This is a mandatory requirement for the automation. For steps to configure authentication mode for access entries, see [Setting up access entries](../../../eks/latest/userguide/setting-up-access-entries.md "../../../eks/latest/userguide/setting-up-access-entries.md").

In the Amazon EKS console, navigate to your cluster and follow these steps:

    * Under **Access** section, verify your authentication configuration is set to either `API` or `API_AND_CONFIG_MAP`.
    * Choose **Create access entry** and configure:




    	+ For *IAM principal ARN*, select the IAM role you created (`TroubleshootEKSALBController-SSM-Role`).
    	+ For *Type*, select `Standard`.
    * Add an access policy:




    	+ For *Policy name*, select `AmazonEKSAdminViewPolicy`.
    	+ For *Access scope*, select `Cluster`.
    * Choose **Add policy**.
    * Verify the details and choose **Create**.

4.  Create an IAM role for the Lambda function (referenced as `LambdaRoleArn` in the input parameters):
    - Create a new IAM role with the following trust policy:

    ```
    {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Effect": "Allow",
                        "Principal": {
                            "Service": "lambda.amazonaws.com"
                        },
                        "Action": "sts:AssumeRole"
                    }
                ]
            }
    ```

    - Attach the following AWS managed policies to this role:
      - `AWSLambdaBasicExecutionRole`
      - `AWSLambdaVPCAccessExecutionRole`

    - Note the ARN of this role as you will need it for the `LambdaRoleArn` input parameter.

1.  Navigate to [AWSSupport-TroubleshootEKSALBControllerIssues](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootEKSALBControllerIssues/description "https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootEKSALBControllerIssues/description") in the AWS Systems Manager console.
1.  Choose **Execute automation**.
1.  For the input parameters enter the following:
    - **AutomationAssumeRole (Optional):**

    Type: AWS::IAM::Role::Arn

    Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.

    Allowed Pattern: ^arn:(?:aws|aws-cn|aws-us-gov):iam::\d{12}:role/?[a-zA-Z\_0-9+=,.@\-\_/]+$
    - **EksClusterName (Required):**

    Type: String

    Description: (Required) Name of the Amazon Elastic Kubernetes Service (Amazon EKS) cluster.

    Allowed Pattern: ^[0-9A-Za-z][A-Za-z0-9-\_]{0,99}$
    - **ALBControllerDeploymentName (Optional):**

    Type: String

    Description: (Optional) The name of the AWS Load Balancer Controller deployment in your Amazon EKS cluster. This is typically 'aws-load-balancer-controller' unless you've customized it during installation.

    Allowed Pattern: ^[a-z0-9]([-.a-z0-9]{0,251}[a-z0-9])?$

    Default: aws-load-balancer-controller
    - **ALBControllerNamespace (Optional):**

    Type: String

    Description: (Optional) The Kubernetes namespace where the AWS Load Balancer Controller is deployed. By default, this is 'kube-system', but it may be different if you've installed the controller in a custom namespace.

    Allowed Pattern: ^[a-z0-9]([-a-z0-9]{0,61}[a-z0-9])?$

    Default: kube-system
    - **ServiceAccountName (Optional):**

    Type: String

    Description: (Optional) The name of the Kubernetes Service Account associated with the AWS Load Balancer Controller. This is typically 'aws-load-balancer-controller' unless customized during installation.

    Allowed Pattern: ^[a-z0-9]([-.a-z0-9]{0,251}[a-z0-9])?$

    Default: aws-load-balancer-controller
    - **ServiceAccountNamespace (Optional):**

    Type: String

    Description: (Optional) The Kubernetes namespace where the Service Account for the AWS Load Balancer Controller is located. This is typically 'kube-system', but may differ if you've used a custom namespace.

    Allowed Pattern: ^[a-z0-9]([-a-z0-9]{0,61}[a-z0-9])?$

    Default: kube-system
    - **IngressName (Optional):**

    Type: String

    Description: (Optional) Name of the Ingress resource to validate (Application Load Balancer). If not specified, Ingress validation will be skipped.

    Allowed Pattern: ^$|^[a-z0-9][a-z0-9.-]{0,251}[a-z0-9]$

    Default: "" (empty string)
    - **IngressNamespace (Optional):**

    Type: String

    Description: (Optional) Namespace of the Ingress resource. Required if `IngressName` is specified.

    Allowed Pattern: ^$|^[a-z0-9][a-z0-9-]{0,61}[a-z0-9]$

    Default: "" (empty string)
    - **ServiceName (Optional):**

    Type: String

    Description: (Optional) Name of a specific Service resource to validate Network Load Balancer (Network Load Balancer) annotations. If not specified, Service resources validation will be skipped.

    Allowed Pattern: ^$|^[a-z0-9][a-z0-9.-]{0,251}[a-z0-9]$

    Default: "" (empty string)
    - **ServiceNamespace (Optional):**

    Type: String

    Description: (Optional) Namespace of the Service resource. Required if `ServiceName` is specified.

    Allowed Pattern: ^$|^[a-z0-9][a-z0-9-]{0,61}[a-z0-9]$

    Default: "" (empty string)
    - **LambdaRoleArn (Required):**

    Type: AWS::IAM::Role::Arn

    Description: (Required) The ARN of the IAM role that allows the AWS Lambda (Lambda) function to access the required AWS services and resources. Associate the AWS managed policies: `AWSLambdaBasicExecutionRole` and `AWSLambdaVPCAccessExecutionRole` to your lambda function execution IAM role.

    Allowed Pattern: ^arn:(?:aws|aws-cn|aws-us-gov):iam::\d{12}:role/?[a-zA-Z\_0-9+=,.@\-\_/]+$

1.  Choose **Execute**.
1.  The automation initiates.
1.  The document performs the following steps:
    1. **ValidateAccessEntryAndOIDCProvider:**

    Validates Amazon EKS cluster IAM setup by checking access entry permissions and OIDC provider configuration. 2. **SetupK8sAuthenticationClient:**

    Execute the SAW Document AWSSupport-SetupK8sApiProxyForEKS to set up a lambda function to run Amazon EKS API calls on the cluster. 3. **VerifyALBControllerAndIRSASetup:**

    Checks whether the given Service Account & Application Load Balancer controller exists in their respective namespaces. Also checks Application Load Balancer controller's Service Account Role Annotation & Trust policy. 4. **VerifyPodIdentityWebhookAndEnv:**

    Checks whether pod-identity-webhook is running. Also checks whether IRSA is injected into pod's ENV variables. 5. **ValidateSubnetRequirements:**

    Check at least two subnets in two AZ's with 8 available IP's, Proper subnet tagging exist for public/private load balancers. 6. **CheckLoadBalancerLimitsAndUsage:**

    Compare the account limit against the number of Application Load Balancer and Network Load Balancer. 7. **CheckIngressOrServiceAnnotations:**

    Checks for correct annotations and specifications in Ingress and Service resources to ensure they are properly configured for Application Load Balancer and Network Load Balancer usage. 8. **CheckWorkerNodeSecurityGroupTags:**

    Verify that exactly one security group attached to the worker nodes has the required cluster tag. 9. **CaptureALBControllerLogs:**

    Retrieves latest diagnostic logs from the AWS Load Balancer Controller pods running in the Amazon EKS cluster. 10. **CleanupK8sAuthenticationClient:**

    Executes the SAW Document 'AWSSupport-SetupK8sApiProxyForEKS' using the 'Cleanup' operation to clean up resources created as part of the automation. 11. **GenerateReport:**

    Generates the automation report.

1.  After the execution completes, review the Outputs section for the detailed results of the execution:

        1. **Report:**


        Provides a comprehensive summary of all checks performed, including the status of the Amazon EKS cluster, Application Load Balancer Controller setup, IRSA configuration, subnet requirements, load balancer limits, ingress/service annotations, worker node security group tags, and Application Load Balancer Controller logs. It also includes any identified issues and recommended remediation steps.

    **References**

Systems Manager Automation

- [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootEKSALBControllerIssues/description "https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootEKSALBControllerIssues/description")
- [Run an automation](../../../systems-manager/latest/userguide/automation-working-executing.md "../../../systems-manager/latest/userguide/automation-working-executing.md")
- [Setting up Automation](../../../systems-manager/latest/userguide/automation-setup.md "../../../systems-manager/latest/userguide/automation-setup.md")
- [Support Automation Workflows](https://aws.amazon.com/premiumsupport/technology/saw/ "https://aws.amazon.com/premiumsupport/technology/saw/")
  Documentation related to AWS Load Balancer Controller

- [AWS Load Balancer Controller](../../../eks/latest/userguide/aws-load-balancer-controller.md "../../../eks/latest/userguide/aws-load-balancer-controller.md")
- [Setting up access entries](../../../eks/latest/userguide/setting-up-access-entries.md "../../../eks/latest/userguide/setting-up-access-entries.md")
