

# View or search account assignments
<a name="aam-view-assignments"></a><a name="aam-view-account-access"></a>

You can view account assignments in several ways.

## Console
<a name="aam-view-account-access-from-console"></a>

For all procedures in this section, sign in to the management account (or delegated admin account), select the Region where account access manager is enabled, and navigate to Account access manager in the IAM console.

------
#### [ Accounts tab ]

**View user or group access from the Accounts tab**

1. Choose the **Accounts** tab.

1. By default, you see the Hierarchy view. You can switch to the List view if desired. You can search accounts by their name, ID, email, and OU ID. When you find the desired account, choose its name.

1. On the account page, you can see the account assignments in the **Account access assignments** section. You can filter them further by username, user ID, group name, group ID, and IAM role ARN.

------
#### [ Users tab ]

**View user access from the Users tab**

1. Choose the **Users** tab.

1. Search for the user by name or user ID. When you find the desired user, choose the username.

1. On the user page, you can see the user's account assignments. You can filter them further by account ID, account name, and IAM role ARN.

------
#### [ Groups tab ]

**View group access from the Groups tab**

1. Choose the **Groups** tab.

1. Search for the group by name or group ID. When you find the desired group, choose the group name.

1. On the group page, you can see the group's account assignments. You can filter them further by account ID, account name, and IAM role ARN.

------

## AWS CLI
<a name="aam-view-account-access-from-cli"></a>

The following commands illustrate how to retrieve account assignments using different filters. The CLI refers to assignments as entitlements.

**Retrieve first 100 assignments (entitlements) for a specific account**

```
aws account-access list-entitlements \
    --region <Region> \
    --application-arn "<Account_access_manager_ARN>" \
    --filter '{
      "principalRole": {
        "account": "<ACCOUNT_ID>"
      }
    }' \
    --max-results 100
```

**Retrieve all assignments (entitlements) for a specific user**

```
aws account-access list-entitlements \
    --region <Region> \
    --application-arn "<Account_access_manager_ARN>" \
    --filter '{
      "principal": {
        "type": "USER",
        "id": "<USER_ID>"
      }
    }'
```

**Retrieve all assignments (entitlements) for a specific group**

```
aws account-access list-entitlements \
    --region <Region> \
    --application-arn "<Account_access_manager_ARN>" \
    --filter '{
      "principal": {
        "type": "GROUP",
        "id": "<GROUP_ID>"
      }
    }'
```