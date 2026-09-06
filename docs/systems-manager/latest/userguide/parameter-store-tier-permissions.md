

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Configuring permissions to specify a Parameter Store default tier
<a name="parameter-store-tier-permissions"></a>

Verify that you have permission in AWS Identity and Access Management (IAM) to change the default parameter tier in Parameter Store by doing one of the following:
+ Make sure that you attach the `AdministratorAccess` policy to your IAM entity (such as user, group, or role).
+ Make sure that you have permission to change the default tier setting by using the following API operations:
  + [GetServiceSetting](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetServiceSetting.html)
  + [UpdateServiceSetting](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_UpdateServiceSetting.html)
  + [ResetServiceSetting](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ResetServiceSetting.html)

Grant the following permissions to the IAM entity to allow a user to view and change the default tier setting for parameters in a specific AWS Region in an AWS account.

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
                "ssm:GetServiceSetting"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ssm:UpdateServiceSetting"
            ],
            "Resource": "arn:aws:ssm:{{us-east-1}}:{{111122223333}}:servicesetting/ssm/parameter-store/default-parameter-tier"
        }
    ]
}
```

------

Administrators can specify read-only permission by assigning the following permissions.

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
                "ssm:GetServiceSetting"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Deny",
            "Action": [
                "ssm:ResetServiceSetting",
                "ssm:UpdateServiceSetting"
            ],
            "Resource": "*"
        }
    ]
}
```

------

To provide access, add permissions to your users, groups, or roles:
+ Users and groups in AWS IAM Identity Center:

  Create a permission set. Follow the instructions in [Create a permission set](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) in the *AWS IAM Identity Center User Guide*.
+ Users managed in IAM through an identity provider:

  Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp.html) in the *IAM User Guide*.
+ IAM users:
  + Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html) in the *IAM User Guide*.
  + (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console) in the *IAM User Guide*.