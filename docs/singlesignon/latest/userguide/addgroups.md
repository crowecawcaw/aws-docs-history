# Add groups to your Identity Center directory

Use the following procedure to add groups to your Identity Center directory. Alternatively,
you can call the AWS API operation [CreateGroup](../IdentityStoreAPIReference/API_CreateGroup.md "../IdentityStoreAPIReference/API_CreateGroup.md") to add groups.

Console

###### To add a group

1. Open the [IAM Identity Center
   console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon").
2. Choose **Groups**.
3. Choose **Create group**.
4. Enter a **Group name** and \*\*Description

- \*optional**\*. The description should
  provide details on what permissions have been or will be assigned to
  the group. Under **Add users to group - \*optional\*\*\*,
  locate the users you want to add as members. Then select the check
  box next to each of them.

5. Choose **Create group**.

AWS CLI

###### To add a group

The following `create-group` command creates a new group in
your Identity Center directory.

```
aws identitystore create-group \
    --identity-store-id d-1234567890 \
    --display-name "Developers" \
    --description "Group that contains all developers"

```

Output:

```
{
    "GroupId": "1a2b3c4d-5e6f-7g8h-9i0j-1k2l3m4n5o6p",
    "IdentityStoreId": "d-1234567890"
}
```

After you add this group to your Identity Center directory, you can assign single sign-on
access to the group. For more information, see [Assign user or group access to AWS accounts](assignusers.md "assignusers.md").
