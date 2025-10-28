# View IAM groups

You can list all the IAM groups in your account, list the users in a user group, and list the IAM groups a user belongs to. If you use the CLI or API, you can list all the IAM groups with a particular path prefix.

Console
To list all IAM groups in your account:

- In the navigation pane , choose **User groups**.

To list the IAM users in a specific IAM group:

- In the navigation pane, choose **User groups**. Then
  choose the name of the group to open the group details page. Review the
  **Users** tab to see the group membership.

To list all the IAM groups that a user is in:

- In the navigation pane, choose **Users**. Then choose the user
  name to open the user details page. Choose the **Groups** tab to
  see a list of the groups to which the user belongs.

AWS CLI
To list all IAM groups in your account:

- [aws iam
  list-groups](../../../cli/latest/reference/iam/list-groups.md "../../../cli/latest/reference/iam/list-groups.md")

To list the users in a specific IAM group:

- [aws iam get-group](../../../cli/latest/reference/iam/get-group.md "../../../cli/latest/reference/iam/get-group.md")

To list all the IAM groups that a user is in:

- [aws iam list-groups-for-user](../../../cli/latest/reference/iam/list-groups-for-user.md "../../../cli/latest/reference/iam/list-groups-for-user.md")

API
To list all IAM groups in your account:

- [ListGroups](../APIReference/API_ListGroups.md "../APIReference/API_ListGroups.md")

To list the users in a specific IAM group:

- [GetGroup](../APIReference/API_GetGroup.md "../APIReference/API_GetGroup.md")

To list all the IAM groups that a user is in:

- [ListGroupsForUser](../APIReference/API_ListGroupsForUser.md "../APIReference/API_ListGroupsForUser.md")
