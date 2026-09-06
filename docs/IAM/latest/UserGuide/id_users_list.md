

# View IAM users
<a name="id_users_list"></a>

You can list the IAM users in your AWS account or in a specific IAM group, and list all the IAM groups that a user is in. For information about the permissions that you need in order to list users, see [Permissions required to access IAM resources](access_permissions-required.md). 

## To list all the IAM users in your account
<a name="id_users_manage_list-users"></a>

------
#### [ Console ]

1. Follow the sign-in procedure appropriate to your user type as described in the topic [How to sign in to AWS](https://docs.aws.amazon.com/signin/latest/userguide/how-to-sign-in.html) in the *AWS Sign-In User Guide*.

1. On the **IAM Console Home** page, in the left navigation pane, enter your query in the **Search IAM** text box.

1. In the navigation pane, choose **Users**. 

The console displays the IAM users in your AWS account.

------
#### [ AWS CLI ]

Run the following command:
+ `[aws iam list-users](https://docs.aws.amazon.com/cli/latest/reference/iam/list-users.html)`

------
#### [ API ]

Call the following operation:
+ `[ListUsers](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListUsers.html)` 

------

## To list the IAM users in an IAM group
<a name="id_users_manage_list-users-group"></a>

------
#### [ Console ]

1. Follow the sign-in procedure appropriate to your user type as described in the topic [How to sign in to AWS](https://docs.aws.amazon.com/signin/latest/userguide/how-to-sign-in.html) in the *AWS Sign-In User Guide*.

1. On the **IAM Console Home** page, in the left navigation pane, enter your query in the **Search IAM** text box.

1. In the navigation pane, choose **User groups**.

1. Choose the name of the user group. 

The IAM users that are members of the group are listed on the **Users** tab.

------
#### [ AWS CLI ]

Run the following command:
+ `[aws iam get-group](https://docs.aws.amazon.com/cli/latest/reference/iam/get-group.html)`

------
#### [ API ]

Call the following operation:
+ `[GetGroup](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetGroup.html)` 

------

## To list all the IAM groups that a user is in
<a name="id_users_manage_list-groups-users"></a>

------
#### [ Console ]

1. Follow the sign-in procedure appropriate to your user type as described in the topic [How to sign in to AWS](https://docs.aws.amazon.com/signin/latest/userguide/how-to-sign-in.html) in the *AWS Sign-In User Guide*.

1. On the **IAM Console Home** page, in the left navigation pane, enter your query in the **Search IAM** text box.

1. In the navigation pane, choose **Users**.

1. In the **Users** list, choose the name of the IAM user. 

1. Select the **Groups** tab to display the list of groups that include the current user.

------
#### [ AWS CLI ]

Run the following command:
+ `[aws iam list-groups-for-user](https://docs.aws.amazon.com/cli/latest/reference/iam/list-groups-for-user.html)`

------
#### [ API ]

Call the following operation:
+ `[ListGroupsForUser](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListGroupsForUser.html)` 

------

## Next steps
<a name="id_users_list-next-steps"></a>

Once you have a list of your IAM users, you can rename, delete, or deactivate an IAM user using the following procedures.
+ [Rename an IAM user](id_users_rename.md)
+ [Remove or deactivate an IAM user](id_users_remove.md)