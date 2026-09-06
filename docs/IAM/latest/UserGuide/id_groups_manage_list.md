

# View IAM groups
<a name="id_groups_manage_list"></a>

You can list all the IAM groups in your account, list the users in a user group, and list the IAM groups a user belongs to. If you use the CLI or API, you can list all the IAM groups with a particular path prefix.

------
#### [ Console ]

To list all IAM groups in your account:
+ In the navigation pane , choose **User groups**.

To list the IAM users in a specific IAM group:
+ In the navigation pane, choose **User groups**. Then choose the name of the group to open the group details page. Review the **Users** tab to see the group membership.

To list all the IAM groups that a user is in:
+ In the navigation pane, choose **Users**. Then choose the user name to open the user details page. Choose the **Groups** tab to see a list of the groups to which the user belongs.

------
#### [ AWS CLI ]

To list all IAM groups in your account:
+ [aws iam list-groups](https://docs.aws.amazon.com/cli/latest/reference/iam/list-groups.html)

To list the users in a specific IAM group:
+ [aws iam get-group](https://docs.aws.amazon.com/cli/latest/reference/iam/get-group.html)

To list all the IAM groups that a user is in:
+ [aws iam list-groups-for-user](https://docs.aws.amazon.com/cli/latest/reference/iam/list-groups-for-user.html)

------
#### [ API ]

To list all IAM groups in your account:
+ [ListGroups](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListGroups.html)

To list the users in a specific IAM group:
+ [GetGroup](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetGroup.html)

To list all the IAM groups that a user is in:
+ [ListGroupsForUser](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListGroupsForUser.html)

------