

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Configuration for Assume Role for Systems Manager
<a name="quick-setup-assume-role"></a>

## To create an assume role for Systems Manager Quick Setup:
<a name="create-assume-role"></a>

Systems Manager Quick Setup requires a role that allows Systems Manager to securely perform actions in your account. This role grants Systems Manager the permissions needed to run commands on your instances and configure EC2 instances, IAM roles, and other Systems Manager resources on your behalf.

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Policies**, and then **Create Policy**

1. Add the `SsmOnboardingInlinePolicy` policy using the JSON below. This policy enables actions required to attach instance profile permissions to instances you specify. For example, it lets you create instance profiles and associate them with EC2 instances.

1. After completing this step, in the navigation pane, choose **Roles**, and then choose **Create role**.

1. For **Trusted entity type**, keep it as default (service).

1. Under **Use case**, choose **Systems Manager**, then choose **Next**.

1. On the **Add permissions** page:

1. Add the `SsmOnboardingInlinePolicy` policy

1. Choose **Next**

1. For **Role name**, enter a descriptive name (for example, `AmazonSSMRoleForAutomationAssumeQuickSetup`).

1. (Optional) Add tags to help identify and organize the role.

1. Choose **Create role**.

**Important**  
The role must include a trust relationship with `ssm.amazonaws.com`. This is automatically configured when you select Systems Manager as the service in step 4.

After creating the role, you can select it when configuring Quick Setup. The role enables Systems Manager to manage EC2 instances, IAM roles, and other Systems Manager resources and run commands on your behalf while maintaining security through specific, limited permissions.

## Permissions Policies
<a name="permissions-policies"></a>

**`SsmOnboardingInlinePolicy`**  
The following policy defines the permissions for Systems Manager Quick Setup:

```
{
    "Version": "2012-10-17" 		 	 	 ,
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "iam:CreateInstanceProfile",
                "iam:ListInstanceProfilesForRole",
                "ec2:DescribeIamInstanceProfileAssociations",
                "iam:GetInstanceProfile",
                "iam:AddRoleToInstanceProfile"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:AssociateIamInstanceProfile"
            ],
            "Resource": "arn:aws:ec2:*:*:instance/*",
            "Condition": {
                "Null": {
                    "ec2:InstanceProfile": "true"
                },
                "ArnLike": {
                    "ec2:NewInstanceProfile": "arn:aws:iam::*:instance-profile/[INSTANCE_PROFILE_ROLE_NAME]"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::*:role/[INSTANCE_PROFILE_ROLE_NAME]",
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": "ec2.amazonaws.com"
                }
            }
        }
    ]
        }
```

**Trust Relationship**  
*This is added automatically through the preceding steps*

```
{
    "Version": "2012-10-17" 		 	 	 ,
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "ssm.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
     ]
        }
```