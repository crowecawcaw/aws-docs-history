# Add users to groups

Use the following procedure to add users as members of a group that you previously
 created in your Identity Center directory. Alternatively, you can call the AWS API
 operation [CreateGroupMembership](../IdentityStoreAPIReference/API_CreateGroupMembership.md "../IdentityStoreAPIReference/API_CreateGroupMembership.md") to add a user as a member
 of a group.


Console
###### To add a user as a member of a group

1. Open the [IAM Identity Center
 console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon").
2. Choose **Groups**.
3. Choose the **group name** that you want to
 update.
4. On the group details page, under **Users in this group**,
 choose **Add users to group**.
5. On the **Add users to group** page, under **Other
 users**, locate the users you want to add as members. Then,
 select the check box next to each of them.
6. Choose **Add users**.


AWS CLI
###### To add a user as a member of a group


The following `create-group-membership` command adds a user
 to a group in your Identity Center directory.



```
aws identitystore create-group-membership \ 
    --identity-store-id d-1234567890 \
    --group-id a1b2c3d4-5678-90ab-cdef-EXAMPLE22222 \
    --member-id UserId=a1b2c3d4-5678-90ab-cdef-EXAMPLE11111
```

Output:



```
{
    "MembershipId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
    "IdentityStoreId": "d-1234567890"
}
```
