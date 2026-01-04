AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Configuration for Assume Role for Systems Manager

## To create an assume role for Systems Manager Quick Setup:

Systems Manager Quick Setup requires a role that allows Systems Manager to securely perform actions in your account. This role grants Systems Manager the permissions needed to run commands on your instances and configure EC2 instances, IAM roles, and other Systems Manager resources on your behalf.

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Policies**, and then **Create Policy**
3. Add the `SsmOnboardingInlinePolicy` policy using the JSON below. (This policy enables actions required in order to attach instance profile permissions to instances you specify. For example allowing creation of instance profiles and associating them with EC2 instances).
4. Once complete, in the navigation pane, choose **Roles**, and then choose **Create role**.
5. For **Trusted entity type**, keep it as default (service).
6. Under **Use case**, choose **Systems Manager**, then choose **Next**.
7. On the **Add permissions** page:
8. Add the `SsmOnboardingInlinePolicy` policy
9. Choose **Next**
10. For **Role name**, enter a descriptive name (for example, `AmazonSSMRoleForAutomationAssumeQuickSetup`).
11. (Optional) Add tags to help identify and organize the role.
12. Choose **Create role**.

###### Important

The role must include a trust relationship with `ssm.amazonaws.com`. This is automatically configured when you select Systems Manager as the service in step 4.

After creating the role, you can select it when configuring Quick Setup. The role enables Systems Manager to manage EC2 instances, IAM roles, and other Systems Manager resources and run commands on your behalf while maintaining security through specific, limited permissions.

## Permissions Policies

###### `SsmOnboardingInlinePolicy`

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

###### Trust Relationship

_This is added automatically via the above steps_

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
