

# Assign and remove access
<a name="aam-assign-remove-access"></a>

## Assign user or group access to an AWS account
<a name="aam-assign-account-access"></a>

You can assign a user or group access to an AWS account by creating an assignment between the user or group, the account, and the IAM role that the user or group can assume in the account. Thus, a single assignment is a triplet consisting of the user or group ID, the account ID, and the IAM role ARN.

If you want to perform bulk assignments such as assigning the same role to a number of users and groups, you must create each assignment individually. You can script this procedure using the account access API, and the AWS SDK/CLI.

### Console
<a name="aam-assign-account-access-from-console"></a>

The console provides a few different ways to assign new access depending on whether you want to first identify the account, the user, or the group.

**Note**  
The account access manager console provides a search capability for users, groups, and accounts. To identify the role you want to assign, you must find its name (or ARN) beforehand. The account access manager console cannot detect IAM roles in AWS accounts.

For all procedures in this section, sign in to the management account (or delegated admin account), select the Region where account access manager is enabled, and navigate to **Account access manager** in the IAM console.

------
#### [ Accounts tab ]

**To assign user or group access from the Accounts tab**

1. Choose the **Accounts** tab.

1. If you already know the account ID, choose **Assign new access**. On the **Assign account access** page, look up the desired user or group, enter the account ID, and IAM role name, and then choose **Assign access**.

1. If you need to first find the account, you can search for the desired AWS account by its name, ID, or email address. Alternatively, you can review the organizational structure or account list to find the relevant AWS account. Choose the radio button in front of the account and then **Assign new access**. On the **Assign account access** page, look up the desired user or group, enter the IAM role name, and then choose **Assign access**.

1. The organizational structure or account list lets you choose an account to view account details and account access assignments. You can choose **Assign new access** from there too.

------
#### [ Users tab ]

**To assign user access from the Users tab**

1. Choose the **Users** tab.

1. You can search users by username and display name or find them in the displayed user list.

1. Choose the user you want to assign new access to.

1. The next page shows the user attributes, account assignments, and group memberships.

1. Choose **Assign new access**.

1. On the **Assign account access** page, enter the account ID and IAM role name, and then choose **Assign access**.

------
#### [ Groups tab ]

**To assign group access from the Groups tab**

1. In the navigation pane, choose **Account access manager**.

1. Choose the **Groups** tab.

1. You can search groups by group name or find them in the displayed group list.

1. Choose the group you want to assign new access to.

1. The next page shows the group attributes, account assignments, and user members.

1. Choose **Assign new access**.

1. On the **Assign account access** page, enter the account ID and IAM role name, and then choose **Assign access**.

------

### AWS CLI
<a name="aam-assign-account-access-from-cli"></a>

The following AWS CLI command can be used to create an account assignment for a user:

```
aws account-access create-entitlement \
  --region <Region> \
  --application-arn "<Account_access_manager_ARN>" \
  --entitlement '{
    "principalRole": {
      "principal": {
        "identityCenter": {
          "userId": "<Identity_Center_User_ID>"
        }
      },
      "roleArn": "arn:aws:iam::<ACCOUNT_ID>:role/<ROLE_NAME>"
    }
  }'
```

The following AWS CLI command can be used to create an account assignment for a group:

```
aws account-access create-entitlement \
  --region <Region> \
  --application-arn "<Account_access_manager_ARN>" \
  --entitlement '{
    "principalRole": {
      "principal": {
        "identityCenter": {
          "groupId": "<IDC_GROUP_ID>"
        }
      },
      "roleArn": "arn:aws:iam::<ACCOUNT_ID>:role/<ROLE_NAME>"
    }
  }'
```

## Remove user or group access to an AWS account
<a name="aam-remove-account-access"></a>

You can find the assignment to remove in several ways.

### Console
<a name="aam-remove-account-access-from-console"></a>

For all procedures in this section, sign in to the management account (or delegated admin account), select the Region where account access manager is enabled, and navigate to **Account access manager** in the IAM console.

------
#### [ Accounts tab ]

**To remove user or group access from the Accounts tab**

1. Choose the **Accounts** tab.

1. Find the relevant account and choose its name.

1. In the **Account access assignments** section, choose the user or group you want to remove access for, and choose **Unassign**.

1. In the modal, choose **Unassign** to confirm.

------
#### [ Users tab ]

**To remove user access from the Users tab**

1. Choose the **Users** tab.

1. Choose the user you want to remove access for.

1. In the **Account access assignments** section, choose the account you want to remove access for, and choose **Unassign**.

1. In the modal, choose **Unassign** to confirm.

------

### AWS CLI
<a name="aam-remove-account-access-from-cli"></a>

To remove access with the CLI, you first need to find the account assignment (entitlement) and then use its ID in the following command. You can see later in this topic how to search for account assignments for a specific account, user, group, or role. The CLI refers to assignments as entitlements.

```
aws account-access delete-entitlement \
    --region <Region> \
    --application-arn "<Account_access_manager_ARN>" \
    --entitlement-id "<ENTITLEMENT_ID>"
```