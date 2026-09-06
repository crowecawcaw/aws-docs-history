

# Delete an IAM group
<a name="id_groups_manage_delete"></a>

When you delete an IAM group in the console, the console automatically removes all group members, detaches all attached managed policies, and deletes all inline policies. However, because IAM doesn't automatically delete policies that refer to the IAM group as a resource, you must be careful when you delete an IAM group. Before you delete your IAM group, manually review your policies to find any policies that mention the group by name. For example, John, the Test Team manager, has a policy attached to his IAM user entity that lets him add and remove users from the Test user group. If an administrator deletes the group, the administrator must also delete the policy attached to John. Otherwise, if the administrator recreates the deleted group and gives it the same name, John's permissions remain in place, even if he left the Test Team.

In contrast, when you use the CLI, SDK, or API to delete a user group, you remove the users in the group first. Then you delete any inline policies embedded in the IAM group. Next, you detach any managed policies that are attached to the group. Then you delete the IAM group itself.

------
#### [ Console ]

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **User groups**.

1. In the list of IAM groups, select the check box next to the names of the IAM groups to delete. You can use the search box to filter the list of IAM groups by type, permissions, and group name.

1. Choose **Delete**.

1. In the confirmation box, if you want to delete a single group, type the group name and choose **Delete**. If you want to delete multiple groups, type the number of IAM group to delete followed by **user groups** and choose **Delete**. For example, if you want to delete three groups, type **3 **user groups****.

------
#### [ AWS CLI ]

1. Remove all users from the IAM group.
   + [aws iam get-group](https://docs.aws.amazon.com/cli/latest/reference/iam/get-group.html) (to get the list of users in the IAM group), and [aws iam remove-user-from-group](https://docs.aws.amazon.com/cli/latest/reference/iam/remove-user-from-group.html) (to remove a user from the IAM group)

1. Delete all inline policies embedded in the IAM group.
   + [aws iam list-group-policies](https://docs.aws.amazon.com/cli/latest/reference/iam/list-group-policies.html) (to get a list of the IAM group's inline policies), and [aws iam delete-group-policy](https://docs.aws.amazon.com/cli/latest/reference/iam/delete-group-policy.html) (to delete the IAM group's inline policies)

1. Detach all managed policies attached to the IAM group.
   + [aws iam list-attached-group-policies](https://docs.aws.amazon.com/cli/latest/reference/iam/list-attached-group-policies.html) (to get a list of the managed policies attached to the IAM group), and [aws iam detach-group-policy](https://docs.aws.amazon.com/cli/latest/reference/iam/detach-group-policy.html) (to detach a managed policy from the IAM group)

1. Delete the IAM group.
   + [aws iam delete-group](https://docs.aws.amazon.com/cli/latest/reference/iam/delete-group.html)

------
#### [ API ]

1. Remove all users from the IAM group.
   + [GetGroup](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetGroup.html) (to get the list of users in the IAM group) and [RemoveUserFromGroup](https://docs.aws.amazon.com/IAM/latest/APIReference/API_RemoveUserFromGroup.html) (to remove a user from the IAM group)

1. Delete all inline policies embedded in the IAM group.
   + [ListGroupPolicies](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListGroupPolicies.html) (to get a list of the IAM group's inline policies) and [DeleteGroupPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteGroupPolicy.html) (to delete the IAM group's inline policies)

1. Detach all managed policies attached to the IAM group.
   + [ListAttachedGroupPolicies](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListAttachedGroupPolicies.html) (to get a list of the managed policies attached to the IAM group) and [DetachGroupPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DetachGroupPolicy.html) (to detach a managed policy from the IAM group)

1. Delete the IAM group.
   + [DeleteGroup](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteGroup.html)

------