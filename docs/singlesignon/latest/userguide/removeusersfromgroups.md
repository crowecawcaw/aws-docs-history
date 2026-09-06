

# Remove users from groups
<a name="removeusersfromgroups"></a>

Use the following procedure to remove members from a group. Alternatively, you can call the AWS API operation [DeleteGroupMembership](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_DeleteGroupMembership.html) to remove a user from a group.

------
#### [ Console ]

**To remove a user from a group**

1. Open the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon).

1. Choose **Groups**.

1. Choose the group you want to update.

1. On the group details page, under the **Users in this group**, choose the users to remove.

1. Choose **Remove users from group**.

1. On the **Remove users** dialog box, choose **Remove users from group** to verify you want to remove the users access to the account and applications that are assigned to the group.

------
#### [ AWS CLI ]

**To remove a user from a group**  
The following `delete-group-membership` command removes a membership from a group.

```
aws identitystore delete-group-membership
    --identity-store-id d-1234567890 \
    --membership-id a1b2c3d4-5678-90ab-cdef-EXAMPLE33333
```

------