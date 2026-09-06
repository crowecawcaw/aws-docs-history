

# Permit IAM users to change their own passwords
<a name="id_credentials_passwords_enable-user-change"></a>

**Note**  
Users with federated identities will use the process defined by their identity provider to change their passwords. As a [best practice](best-practices.md), require human users to use federation with an identity provider to access AWS using temporary credentials.

You can grant IAM users the permission to change their own passwords for signing in to the AWS Management Console. You can do this in one of two ways:
+ [Allow all IAM users in the account to change their own passwords](#proc_letalluserschangepassword). 
+ [Allow only selected IAM users to change their own passwords](#proc_letselectuserschangepassword). In this scenario, you disable the option for all users to change their own passwords and you use an IAM policy to grant permissions to only some users. This approach allows those users to change their own passwords and optionally other credentials like their own access keys. 

**Important**  
We recommend that you [set a custom password policy](id_credentials_passwords_account-policy.md) that requires IAM users to create strong passwords.

## To allow all IAM users to change their own passwords
<a name="proc_letalluserschangepassword"></a>

------
#### [ Console ]

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Account settings**.

1. In the **Password policy** section, choose **Edit**.

1. Choose **Custom** to use a custom password policy.

1. Select **Allow users to change their own password**, and then choose **Save changes**. This allows all users in the account access to the `iam:ChangePassword` action for only their user and to the `iam:GetAccountPasswordPolicy` action.

1. Provide users with the following instructions for changing their passwords: [How an IAM user changes their own password](id_credentials_passwords_user-change-own.md). 

------
#### [ AWS CLI ]

Run the following command:
+ `[aws iam update-account-password-policy](https://docs.aws.amazon.com/cli/latest/reference/iam/update-account-password-policy.html)`

------
#### [ API ]

To update the account password policy, call the following operation:
+ `[UpdateAccountPasswordPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateAccountPasswordPolicy.html)` 

------

## To allow selected IAM users to change their own passwords
<a name="proc_letselectuserschangepassword"></a>

------
#### [ Console ]

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Account settings**. 

1. In the **Password policy** section, make sure that **Allow users to change their own password** is not selected. If this checkbox is selected, all users can change their own passwords. (See the previous procedure.) 

1. Create the users who should be allowed to change their own password, if they do not already exist. For details, see [Create an IAM user in your AWS account](id_users_create.md). 

1. (Optional) Create an IAM group for the users who should be allowed to change their passwords, and then add the users from the previous step to the group. For details, see [IAM user groups](id_groups.md). 

1. Assign the following policy to the group. For more information, see [Manage IAM policies](access_policies_manage.md).

------
#### [ JSON ]

****  

   ```
   {
     "Version":"2012-10-17",		 	 	 
     "Statement": [
       {
         "Effect": "Allow",
         "Action": "iam:GetAccountPasswordPolicy",
         "Resource": "*"
       },
       {
         "Effect": "Allow",
         "Action": "iam:ChangePassword",
         "Resource": "arn:aws:iam::*:user/${aws:username}"
       }
     ]
   }
   ```

------

   This policy grants access to the [ChangePassword](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ChangePassword.html) action, which lets users change only their own passwords from the console, the AWS CLI, Tools for Windows PowerShell, or the API. It also grants access to the [GetAccountPasswordPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetAccountPasswordPolicy.html) action, which lets the user view the current password policy; this permission is required so that the user can view the account password policy on the **Change password** page. The user must be allowed to read the current password policy to make sure that the changed password meets the requirements of the policy.

1. Provide users with the following instructions for changing their passwords: [How an IAM user changes their own password](id_credentials_passwords_user-change-own.md). 

------

### For more information
<a name="HowToPwdIAMUser-moreinfo"></a>

For more information on managing credentials, see the following topics:
+ [Permit IAM users to change their own passwords](#id_credentials_passwords_enable-user-change) 
+ [User passwords in AWS](id_credentials_passwords.md)
+ [Set an account password policy for IAM users](id_credentials_passwords_account-policy.md)
+ [Manage IAM policies](access_policies_manage.md)
+ [How an IAM user changes their own password](id_credentials_passwords_user-change-own.md)