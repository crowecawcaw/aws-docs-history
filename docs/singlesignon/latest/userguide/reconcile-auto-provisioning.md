# Audit and reconcile auto-provisioned resources

SCIM enables you to automatically provision users, groups, and group memberships from your identity source to 
 IAM Identity Center. This guide helps you verify and reconcile these resources to maintain accurate synchronization.


## Why audit your resources?


Regular auditing helps ensure your access controls remain accurate and your identity
 provider (IdP) stays properly synchronized with IAM Identity Center. This is particularly important
 for security compliance and access management.


Resources you can audit:



* Users
* Groups
* Group memberships

 You can use AWS Identity Store [APIs](../IdentityStoreAPIReference/welcome.md "../IdentityStoreAPIReference/welcome.md") or
 [CLI commands](https://docs.aws.amazon.com/cli/latest/reference/identitystore/ "https://docs.aws.amazon.com/cli/latest/reference/identitystore/")
 to conduct the audit and reconciliation. The following examples use AWS CLI
 commands. For API alternatives, refer to the [corresponding operations](../IdentityStoreAPIReference/API_Operations.md "../IdentityStoreAPIReference/API_Operations.md") in the *Identity Store API reference*. 


## How to audit resources


Here are examples for how to audit these resources using AWS CLI commands.


Before you begin, ensure you have:



* Administrator access to IAM Identity Center.
* AWS CLI installed and configured. For information, see the [*AWS Command Line
 Interface User Guide*](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html "https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html").
* Required IAM permissions for Identity Store commands.

### Step 1: List current resources


You can view your current resources using the AWS CLI.


###### Note


 When using the AWS CLI, pagination is handled automatically unless you specify `--no-paginate`.
 If you’re calling the API directly (for example, with an SDK or a custom script), 
 handle the `NextToken` in the response. This ensures you retrieve all results across multiple pages.
 


###### Example for users


```
aws identitystore list-users \
  --region `REGION` \
  --identity-store-id `IDENTITY_STORE_ID` 
```

###### Example for groups


```
aws identitystore list-groups \
  --region `REGION` \
  --identity-store-id `IDENTITY_STORE_ID` 
```

###### Example for group memberships


```
aws identitystore list-group-memberships \
  --region `REGION` \
  --identity-store-id `IDENTITY_STORE_ID`
  --group-id `GROUP_ID` 
```

### Step 2: Compare with your identity source


Compare the listed resources with your identity source to identify any
 discrepancies, such as:



* Missing resources that should be provisioned in IAM Identity Center.
* Extra resources that should be removed from IAM Identity Center.

###### Example for users


```
# Create missing users
aws identitystore create-user \
  --identity-store-id `IDENTITY_STORE_ID` \
  --user-name `USERNAME` \
  --display-name `DISPLAY_NAME` \
  --name GivenName=`FIRST_NAME`,FamilyName=`LAST_NAME` \
  --emails Value=`EMAIL`,Primary=true

# Delete extra users
aws identitystore delete-user \
  --identity-store-id `IDENTITY_STORE_ID` \
  --user-id `USER_ID`  
```

###### Example for groups


```
# Create missing groups
aws identitystore create-group \
  --identity-store-id `IDENTITY_STORE_ID` \
  `[group attributes]`
  
# Delete extra groups
aws identitystore delete-group \
  --identity-store-id `IDENTITY_STORE_ID` \
  --group-id `GROUP_ID` 
```

###### Example for group memberships


```
# Add missing members
aws identitystore create-group-membership \
  --identity-store-id `IDENTITY_STORE_ID` \
  --group-id `GROUP_ID` \
  --member-id '{"UserId": "`USER_ID`"}'
  
# Remove extra members
aws identitystore delete-group-membership \
  --identity-store-id `IDENTITY_STORE_ID` \
  --membership-id `MEMBERSHIP_ID`  
```

## Considerations



* Commands are subject to [service quotas and API throttling](limits.md#ssothrottlelimits "limits.md#ssothrottlelimits").
* When you find many differences during reconciliation, make small, gradual changes to AWS Identity Store. This
 helps you avoid mistakes that affect multiple users.
* SCIM synchronization can override your manual changes. Check your IdP settings 
 to understand this behavior.
