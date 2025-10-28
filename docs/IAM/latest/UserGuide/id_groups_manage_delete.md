# Delete an IAM group

When you delete an IAM group in the console, the console automatically removes all group
members, detaches all attached managed policies, and deletes all inline policies. However,
because IAM doesn't automatically delete policies that refer to the IAM group as a
resource, you must be careful when you delete an IAM group. Before you delete your
IAM group, manually review your policies to find any policies that mention the group by
name. For example, John, the Test Team manager, has a policy attached to his IAM user entity
that lets him add and remove users from the Test user group. If an administrator deletes the
group, the administrator must also delete the policy attached to John. Otherwise, if the
administrator recreates the deleted group and give it the same name, John's permissions remain
in place, even if he left the Test Team.

In contrast, when you use the CLI, SDK, or API to delete a user group, you remove the users
in the group first. Then you delete any inline policies embedded in the IAM group. Next, you
detach any managed policies that are attached to the group. Then you delete the IAM group
itself.

Console

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **User groups**.
3. In the list of IAM groups, select the check box next to the names of the
   IAM groups to delete. You can use the search box to filter the list of
   IAM groups by type, permissions, and group name.
4. Choose **Delete**.
5. In the confirmation box, if you want to delete a single group, type the group name
   and choose **Delete**. If you want to delete multiple groups, type
   the number of IAM group to delete followed by `user groups`
   and choose **Delete**. For example, if you want to delete three
   groups, type `3 `user groups``.

AWS CLI

1. Remove all users from the IAM group.
   - [aws iam get-group](../../../cli/latest/reference/iam/get-group.md "../../../cli/latest/reference/iam/get-group.md") (to get the list of users in the IAM group), and [aws iam remove-user-from-group](../../../cli/latest/reference/iam/remove-user-from-group.md "../../../cli/latest/reference/iam/remove-user-from-group.md") (to remove a user from the IAM group)

2. Delete all inline policies embedded in the IAM group.
   - [aws iam list-group-policies](../../../cli/latest/reference/iam/list-group-policies.md "../../../cli/latest/reference/iam/list-group-policies.md") (to get a list of the IAM group's inline policies), and [aws iam delete-group-policy](../../../cli/latest/reference/iam/delete-group-policy.md "../../../cli/latest/reference/iam/delete-group-policy.md") (to delete the IAM group's inline policies)

3. Detach all managed policies attached to the IAM group.
   - [aws iam list-attached-group-policies](../../../cli/latest/reference/iam/list-attached-group-policies.md "../../../cli/latest/reference/iam/list-attached-group-policies.md") (to get a list of the managed policies attached to the IAM group), and [aws iam detach-group-policy](../../../cli/latest/reference/iam/detach-group-policy.md "../../../cli/latest/reference/iam/detach-group-policy.md") (to detach a managed policy from the IAM group)

4. Delete the IAM group.
   - [aws iam delete-group](../../../cli/latest/reference/iam/delete-group.md "../../../cli/latest/reference/iam/delete-group.md")

API

1. Remove all users from the IAM group.
   - [GetGroup](../APIReference/API_GetGroup.md "../APIReference/API_GetGroup.md") (to get the list of users in the IAM group) and [RemoveUserFromGroup](../APIReference/API_RemoveUserFromGroup.md "../APIReference/API_RemoveUserFromGroup.md") (to remove a user from the IAM group)

2. Delete all inline policies embedded in the IAM group.
   - [ListGroupPolicies](../APIReference/API_ListGroupPolicies.md "../APIReference/API_ListGroupPolicies.md") (to get a list of the IAM group's inline policies) and [DeleteGroupPolicy](../APIReference/API_DeleteGroupPolicy.md "../APIReference/API_DeleteGroupPolicy.md") (to delete the IAM group's inline policies)

3. Detach all managed policies attached to the IAM group.
   - [ListAttachedGroupPolicies](../APIReference/API_ListAttachedGroupPolicies.md "../APIReference/API_ListAttachedGroupPolicies.md") (to get a list of the managed policies attached to the IAM group) and [DetachGroupPolicy](../APIReference/API_DetachGroupPolicy.md "../APIReference/API_DetachGroupPolicy.md") (to detach a managed policy from the IAM group)

4. Delete the IAM group.
   - [DeleteGroup](../APIReference/API_DeleteGroup.md "../APIReference/API_DeleteGroup.md")
