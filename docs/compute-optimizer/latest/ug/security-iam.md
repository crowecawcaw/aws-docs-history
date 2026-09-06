

# Identity and Access Management for AWS Compute Optimizer
<a name="security-iam"></a>

You can use AWS Identity and Access Management (IAM) to create identities (users, groups, or roles), and give those identities permissions to access the AWS Compute Optimizer console and APIs.

By default, IAM users don't have access to the Compute Optimizer console and APIs. You give users access by attaching IAM policies to a single user, a group of users, or a role. For more information, see [Identities (Users, Groups, and Roles)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html) and [Overview of IAM Policies in the IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/PoliciesOverview.html).

After you create IAM users, you can give those users individual passwords. Then, they can sign in to your account and view Compute Optimizer information by using an account-specific sign-in page. For more information, see [How Users Sign In to Your Account](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_how-users-sign-in.html).

**Important**  
To view recommendations for EC2 instances, an IAM user requires the `ec2:DescribeInstances` permission.
To view recommendations for EBS volumes, an IAM user requires the `ec2:DescribeVolumes` permission.
To view recommendations for EC2 Auto Scaling groups, an IAM user requires the `autoscaling:DescribeAutoScalingGroups` and `autoscaling:DescribeAutoScalingInstances` permissions.
To view recommendations for Lambda functions, an IAM user requires the `lambda:ListFunctions` and `lambda:ListProvisionedConcurrencyConfigs` permissions.
To view recommendations for Amazon ECS services on Fargate, an IAM user requires the `ecs:ListServices` and `ecs:ListClusters` permissions.
To view current CloudWatch metrics data in the Compute Optimizer console, an IAM user requires the `cloudwatch:GetMetricData` permission.
To view recommendations commercial software licenses, certain Amazon EC2 instance roles and IAM user permissions are required. For more information see, [Policies to enable commercial software license recommendations](#license-access).
To view recommendations for Amazon RDS, an IAM user requires the `rds:DescribeDBInstances` and `rds:DescribeDBClusters` permissions.

If the user or group that you want to give permissions to already has a policy, you can add one of the Compute Optimizer specific policy statements illustrated here to that policy.

**Topics**
+ [Trusted access for AWS Organizations](#trusted-service-access)
+ [Policy examples for Compute Optimizer](#CO-policy-examples)
+ [Policy examples for Automation](#COA-policy-example)
+ [Additional resources](#iam-resources)

## Trusted access for AWS Organizations
<a name="trusted-service-access"></a>

When you opt in using your organization's management account and include all member accounts within the organization, trusted access for Compute Optimizer is automatically enabled in your organization account. This allows Compute Optimizer to analyze compute resources in those member accounts, and generate recommendations for them.

Every time that you access recommendations for member accounts, Compute Optimizer verifies that trusted access is enabled in your organization account. If you disable Compute Optimizer trusted access after you opt in, Compute Optimizer denies access to recommendations for your organization's member accounts. Moreover, the member accounts within the organization aren't opted in to Compute Optimizer. To re-enable trusted access, opt in to Compute Optimizer again using your organization's management account and include all the member accounts within the organization. For more information, see [Opting in to AWS Compute Optimizer](account-opt-in.md). For more information about AWS Organizations trusted access, see [Using AWS Organizations with other AWS services](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html) in the *AWS Organizations User Guide*.

## Policy examples for Compute Optimizer
<a name="CO-policy-examples"></a>

**Topics**
+ [Policy to opt in to Compute Optimizer](#opting-in-access)
+ [Policies to grant access to Compute Optimizer for standalone AWS accounts](#standalone-account-access)
+ [Policies to grant access to Compute Optimizer for a management account of an organization](#organization-account-access)
+ [Policies to grant access to manage Compute Optimizer recommendation preferences](#enhanced-infrastructure-metrics-permissions)
+ [Policies to enable commercial software license recommendations](#license-access)
+ [Policy to deny access to Compute Optimizer](#deny-access)

### Policy to opt in to Compute Optimizer
<a name="opting-in-access"></a>

This policy statement grants the following:
+ Access to opt in to Compute Optimizer.
+ Access to create a service-linked role for Compute Optimizer. For more information, see [Using service-linked roles for AWS Compute Optimizer](using-service-linked-roles.md).
+ Access to update the enrollment status to the Compute Optimizer service.

**Important**  
This IAM role is required to opt in to AWS Compute Optimizer.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iam:CreateServiceLinkedRole",
            "Resource": "arn:aws:iam::*:role/aws-service-role/compute-optimizer.amazonaws.com/AWSServiceRoleForComputeOptimizer*",
            "Condition": {"StringLike": {"iam:AWSServiceName": "compute-optimizer.amazonaws.com"}}
        },
        {
            "Effect": "Allow",
            "Action": "iam:PutRolePolicy",
            "Resource": "arn:aws:iam::*:role/aws-service-role/compute-optimizer.amazonaws.com/AWSServiceRoleForComputeOptimizer"
        },
        {
            "Effect": "Allow",
            "Action": "compute-optimizer:UpdateEnrollmentStatus",
            "Resource": "*"
        }
    ]
}
```

------

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iam:CreateServiceLinkedRole",
            "Resource": "arn:aws-cn:iam::*:role/aws-service-role/compute-optimizer.amazonaws.com/AWSServiceRoleForComputeOptimizer*",
            "Condition": {"StringLike": {"iam:AWSServiceName": "compute-optimizer.amazonaws.com"}}
        },
        {
            "Effect": "Allow",
            "Action": "iam:PutRolePolicy",
            "Resource": "arn:aws-cn:iam::*:role/aws-service-role/compute-optimizer.amazonaws.com/AWSServiceRoleForComputeOptimizer"
        },
        {
            "Effect": "Allow",
            "Action": "compute-optimizer:UpdateEnrollmentStatus",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "organizations:DescribeOrganization",
            "Resource": "*"
        }
    ]
}
```

------

### Policies to grant access to Compute Optimizer for standalone AWS accounts
<a name="standalone-account-access"></a>

The following policy statement grants full access to Compute Optimizer for standalone AWS accounts. 

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
                "compute-optimizer:*",
                "ec2:DescribeInstances",
                "ec2:DescribeVolumes",
                "ecs:ListServices",
                "ecs:ListClusters",
                "autoscaling:DescribeAutoScalingGroups",
                "autoscaling:DescribeAutoScalingInstances",
                "lambda:ListFunctions",
                "lambda:ListProvisionedConcurrencyConfigs",
                "cloudwatch:GetMetricData"
            ],
            "Resource": "*"
        }
    ]
}
```

------

The following policy statement grants read-only access to Compute Optimizer for standalone AWS accounts.

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
                "compute-optimizer:GetEnrollmentStatus",
                "compute-optimizer:GetEffectiveRecommendationPreferences",
                "compute-optimizer:GetRecommendationPreferences",
                "compute-optimizer:GetRecommendationSummaries",
                "compute-optimizer:GetEC2InstanceRecommendations",
                "compute-optimizer:GetEC2RecommendationProjectedMetrics",
                "compute-optimizer:GetAutoScalingGroupRecommendations",
                "compute-optimizer:GetEBSVolumeRecommendations",
                "compute-optimizer:GetLambdaFunctionRecommendations",
                "compute-optimizer:DescribeRecommendationExportJobs",
                "compute-optimizer:GetEffectiveRecommendationPreferences",
                "compute-optimizer:GetRecommendationPreferences",
                "compute-optimizer:GetECSServiceRecommendations",
                "compute-optimizer:GetECSServiceRecommendationProjectedMetrics",
                "compute-optimizer:GetRDSDatabaseRecommendations",
                "compute-optimizer:GetRDSDatabaseRecommendationProjectedMetrics",
                "compute-optimizer:GetIdleRecommendations",
                "ec2:DescribeInstances",
                "ec2:DescribeVolumes",
                "ecs:ListServices",
                "ecs:ListClusters",
                "autoscaling:DescribeAutoScalingGroups",
                "autoscaling:DescribeAutoScalingInstances",
                "lambda:ListFunctions",
                "lambda:ListProvisionedConcurrencyConfigs",
                "cloudwatch:GetMetricData",
                "rds:DescribeDBInstances",
                "rds:DescribeDBClusters"
            ],
            "Resource": "*"
        }
    ]
}
```

------

### Policies to grant access to Compute Optimizer for a management account of an organization
<a name="organization-account-access"></a>

The following policy statement grants full access to Compute Optimizer for a management account of your organization. 

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
                "compute-optimizer:*",
                "ec2:DescribeInstances",
                "ec2:DescribeVolumes",
                "ecs:ListServices",
                "ecs:ListClusters",
                "autoscaling:DescribeAutoScalingGroups",
                "autoscaling:DescribeAutoScalingInstances",
                "lambda:ListFunctions",
                "lambda:ListProvisionedConcurrencyConfigs",
                "cloudwatch:GetMetricData",
                "organizations:ListAccounts",
                "organizations:DescribeOrganization",
                "organizations:DescribeAccount",
                "organizations:EnableAWSServiceAccess",
                "organizations:ListDelegatedAdministrators",
                "organizations:RegisterDelegatedAdministrator",
                "organizations:DeregisterDelegatedAdministrator"
            ],
            "Resource": "*"
        }
    ]
}
```

------

The following policy statement grants read-only access to Compute Optimizer for a management account of an organization.

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
                "compute-optimizer:GetEnrollmentStatus",
                "compute-optimizer:GetEnrollmentStatusesForOrganization",
                "compute-optimizer:GetRecommendationSummaries",
                "compute-optimizer:GetEC2InstanceRecommendations",
                "compute-optimizer:GetEC2RecommendationProjectedMetrics",
                "compute-optimizer:GetAutoScalingGroupRecommendations",
                "compute-optimizer:GetEBSVolumeRecommendations",
                "compute-optimizer:GetLambdaFunctionRecommendations",
                "compute-optimizer:GetEffectiveRecommendationPreferences",
                "compute-optimizer:GetRecommendationPreferences",
                "compute-optimizer:GetECSServiceRecommendations",
                "compute-optimizer:GetECSServiceRecommendationProjectedMetrics",
                "compute-optimizer:GetRDSDatabaseRecommendations",
                "compute-optimizer:GetRDSDatabaseRecommendationProjectedMetrics",
                "compute-optimizer:GetIdleRecommendations",
                "ec2:DescribeInstances",
                "ec2:DescribeVolumes",
                "ecs:ListServices",
                "ecs:ListClusters",
                "autoscaling:DescribeAutoScalingGroups",
                "autoscaling:DescribeAutoScalingInstances",
                "lambda:ListFunctions",
                "lambda:ListProvisionedConcurrencyConfigs",
                "cloudwatch:GetMetricData",
                "organizations:ListAccounts",
                "organizations:DescribeOrganization",
                "organizations:DescribeAccount",
                "organizations:ListDelegatedAdministrators",
                "rds:DescribeDBInstances",
                "rds:DescribeDBClusters"
            ],
            "Resource": "*"
        }
    ]
}
```

------

### Policies to grant access to manage Compute Optimizer recommendation preferences
<a name="enhanced-infrastructure-metrics-permissions"></a>

The following policy statements grant access to view and edit recommendation preferences. 

**Grant access to manage recommendation preferences for EC2 instances only**

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
                "compute-optimizer:DeleteRecommendationPreferences",
                "compute-optimizer:GetEffectiveRecommendationPreferences",
                "compute-optimizer:GetRecommendationPreferences",
                "compute-optimizer:PutRecommendationPreferences"
            ],
            "Resource": "*",
            "Condition" :  {
                "StringEquals" : {
                    "compute-optimizer:ResourceType" : "Ec2Instance"
                }
            }            
        }
    ]
}
```

------

**Grant access to manage recommendation preferences for EC2 Auto Scaling groups only**

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
                "compute-optimizer:DeleteRecommendationPreferences",
                "compute-optimizer:GetEffectiveRecommendationPreferences",
                "compute-optimizer:GetRecommendationPreferences",
                "compute-optimizer:PutRecommendationPreferences"
            ],
            "Resource": "*",
            "Condition" :  {
                "StringEquals" : {
                    "compute-optimizer:ResourceType" : "AutoScalingGroup"
                }
            }            
        }
    ]
}
```

------

**Grant access to manage recommendation preferences for RDS instances only**

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
                "compute-optimizer:DeleteRecommendationPreferences",
                "compute-optimizer:GetEffectiveRecommendationPreferences",
                "compute-optimizer:GetRecommendationPreferences",
                "compute-optimizer:PutRecommendationPreferences"
            ],
            "Resource": "*",
            "Condition" :  {
                "StringEquals" : {
                    "compute-optimizer:ResourceType" : "RdsDBInstance"
                }
            }            
        }
    ]
}
```

------

### Policies to enable commercial software license recommendations
<a name="license-access"></a>

For Compute Optimizer to generate license recommendations, attach the following Amazon EC2 instance roles and policies.
+ The `AmazonSSMManagedInstanceCore` role to enable Systems Manager. For more information, see [AWS Systems Manager identity-based policy examples](https://docs.aws.amazon.com/systems-manager/latest/userguide/security_iam_id-based-policy-examples) in the *AWS Systems Manager User Guide*.
+ The `CloudWatchAgentServerPolicy` policy to enable the release of instance metrics and logs to CloudWatch. For more information, see [ Create IAM roles and users for use with the CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create-iam-roles-for-cloudwatch-agent) in the *Amazon CloudWatch User Guide*.
+ The following IAM inline policy statement to read the secret Microsoft SQL Server connection string stored in AWS Systems Manager. For more information about inline policies, see [ Managed policies and inline policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline) in the *AWS Identity and Access Management User Guide*.

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
                "secretsmanager:GetSecretValue*"
            ],
            "Resource": "arn:aws:secretsmanager:*:*:secret:ApplicationInsights-*"
        }
    ]
}
```

------

Additionally, to enable and receive license recommendations, attach the following IAM policy to your user, group or role. For more information, [ IAM policy](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-iam) in the *Amazon CloudWatch User Guide*.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Action": [
                "applicationinsights:*",
                "iam:CreateServiceLinkedRole",
                "iam:ListRoles",
                "resource-groups:ListGroups"
            ],
            "Effect": "Allow",
            "Resource": "*"
        }
    ]
}
```

------

### Policy to deny access to Compute Optimizer
<a name="deny-access"></a>

The following policy statement denies access to Compute Optimizer.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Deny",
            "Action": "compute-optimizer:*",
            "Resource": "*"
        }
    ]
}
```

------

## Policy examples for Automation
<a name="COA-policy-example"></a>

**Topics**
+ [Policy to enable Automation for your account](#policy-automation-enable)
+ [Policy to enable Automation across your organization](#automation-enable-org)
+ [Policy to grant full access to Compute Optimizer Automation for standalone AWS accounts](#automation-account-full)
+ [Policy to grant read-only access to Compute Optimizer Automation for standalone AWS accounts](#automation-account-read)
+ [Policy to grant full access to Compute Optimizer Automation for a management account of an organization](#automation-account-mgmt)
+ [Policy to grant read-only access to Compute Optimizer Automation for a management account of an organization](#automation-account-mgmt-readonly)

### Policy to enable Automation for your account
<a name="policy-automation-enable"></a>

The following policy statement enables Automation for your account.

```
{
    "Version": "2012-10-17",                   
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iam:CreateServiceLinkedRole",
            "Resource": "arn:aws:iam::*:role/aws-service-role/aco-automation.amazonaws.com/AWSServiceRoleForComputeOptimizerAutomation",
            "Condition": {"StringLike": {"iam:AWSServiceName": "aco-automation.amazonaws.com"}}
        },
        {
            "Effect": "Allow",
            "Action": [
                "iam:PutRolePolicy", 
                "iam:AttachRolePolicy"
            ],
            "Resource": "arn:aws:iam::*:role/aws-service-role/aco-automation.amazonaws.com/AWSServiceRoleForComputeOptimizerAutomation"
        },
        {
            "Effect": "Allow",
            "Action": "aco-automation:UpdateEnrollmentConfiguration",
            "Resource": "*"
        }
    ]
}
```

### Policy to enable Automation across your organization
<a name="automation-enable-org"></a>

The following policy statement enables Automation across your organization.

```
                {
    "Version": "2012-10-17",                   
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iam:CreateServiceLinkedRole",
            "Resource": "arn:aws:iam::*:role/aws-service-role/aco-automation.amazonaws.com/AWSServiceRoleForComputeOptimizerAutomation",
            "Condition": {"StringLike": {"iam:AWSServiceName": "aco-automation.amazonaws.com"}}
        },
        {
            "Effect": "Allow",
            "Action": [
                "iam:PutRolePolicy", 
                "iam:AttachRolePolicy"
            ],
            "Resource": "arn:aws:iam::*:role/aws-service-role/aco-automation.amazonaws.com/AWSServiceRoleForComputeOptimizerAutomation"
        },
        {
            "Effect": "Allow",
            "Action": "aco-automation:UpdateEnrollmentConfiguration",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "aco-automation:AssociateAccounts",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "aco-automation:DisassociateAccounts",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "aco-automation:ListAccounts",
            "Resource": "*"
        }
    ]
}
```

### Policy to grant full access to Compute Optimizer Automation for standalone AWS accounts
<a name="automation-account-full"></a>

The following policy grants full access to Compute Optimizer Automation for standalone AWS accounts.

```
                {
    "Version": "2012-10-17",                   
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
               "aco-automation:*",
            "ec2:DescribeVolumes"
            ],
            "Resource": "*"
        }
    ]
}
```

### Policy to grant read-only access to Compute Optimizer Automation for standalone AWS accounts
<a name="automation-account-read"></a>

The following policy grants read-only access to Compute Optimizer Automation for standalone AWS accounts.

```
                {
    "Version": "2012-10-17",                   
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
               "aco-automation:GetEnrollmentConfiguration",
               "aco-automation:GetAutomationEvent",
               "aco-automation:GetAutomationRule",
               "aco-automation:ListAutomationEvents",
               "aco-automation:ListAutomationEventSteps",
               "aco-automation:ListAutomationEventSummaries",
               "aco-automation:ListAutomationRules",
               "aco-automation:ListAutomationRulePreview",
               "aco-automation:ListAutomationRulePreviewSummaries",
               "aco-automation:ListRecommendedActions",
               "aco-automation:ListRecommendedActionSummaries",
               "aco-automation:ListTagsForResource",
               "ec2:DescribeVolumes"
            ],
            "Resource": "*"
        }
    ]
}
```

### Policy to grant full access to Compute Optimizer Automation for a management account of an organization
<a name="automation-account-mgmt"></a>

The following policy grants full access to Compute Optimizer Automation for a management account of an organization.

```
                {
    "Version": "2012-10-17",                   
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
               "aco-automation:*",
               "ec2:DescribeVolumes",
               "organizations:ListAccounts",
               "organizations:DescribeOrganization",
               "organizations:DescribeAccount",
               "organizations:EnableAWSServiceAccess",
               "organizations:ListDelegatedAdministrators",
               "organizations:RegisterDelegatedAdministrator",
               "organizations:DeregisterDelegatedAdministrator"
            ],
            "Resource": "*"
        }
    ]
}
```

### Policy to grant read-only access to Compute Optimizer Automation for a management account of an organization
<a name="automation-account-mgmt-readonly"></a>

The following policy grants read-only access to Compute Optimizer Automation for a management account of an organization.

```
                {
    "Version": "2012-10-17",                   
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
               "aco-automation:GetEnrollmentConfiguration",
               "aco-automation:GetAutomationEvent",
               "aco-automation:GetAutomationRule",
               "aco-automation:ListAccounts",
               "aco-automation:ListAutomationEvents",
               "aco-automation:ListAutomationEventSteps",
               "aco-automation:ListAutomationEventSummaries",
               "aco-automation:ListAutomationRules",
               "aco-automation:ListAutomationRulePreview",
               "aco-automation:ListAutomationRulePreviewSummaries",
               "aco-automation:ListRecommendedActions",
               "aco-automation:ListRecommendedActionSummaries",
               "aco-automation:ListTagsForResource",
               "ec2:DescribeVolumes"
            ],
            "Resource": "*"
        }
    ]
}
```

## Additional resources
<a name="iam-resources"></a>
+ Troubleshooting — [Troubleshooting in Compute Optimizer](troubleshooting-account-opt-in.md)
+ [Opting in to AWS Compute Optimizer](account-opt-in.md)
+ [AWS managed policies for AWS Compute Optimizer](managed-policies.md)
+ [Using service-linked roles for AWS Compute Optimizer](using-service-linked-roles.md)
+ [Using service-linked roles for Automation](using-service-linked-roles-automation.md)