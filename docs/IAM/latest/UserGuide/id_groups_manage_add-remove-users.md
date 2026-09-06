

# Edit users in IAM groups
<a name="id_groups_manage_add-remove-users"></a>

Use IAM groups to apply the same permissions policies across multiple users at once. You can then add users to or remove users from an IAM group. This is useful as people enter and leave your organization.

## Review policy access
<a name="groups-remove_prerequisites"></a>

Before you remove a group, use the group details page to review the members (IAM users) of the group, the policies attached to the group on the **Permissions** tab and review recent service-level activity using the **Last Accessed** tab. This helps prevent unintentionally removing access from a principal (person or application) who is using it. For more information about viewing last accessed information, see [Refine permissions in AWS using last accessed information](access_policies_last-accessed.md).

## Add an IAM user to an IAM group
<a name="groups-add-remove-console"></a>

------
#### [ Console ]

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **User groups** and then choose the name of the group.

1. Choose the **Users** tab and then choose **Add users**. Select the check box next to the users you want to add.

1. Choose **Add users**.

------
#### [ AWS CLI ]

Run the following command:
+ `[aws iam add-user-to-group](https://docs.aws.amazon.com/cli/latest/reference/iam/add-user-to-group.html)`

------
#### [ API ]

Call the following operation:
+ `[AddUserToGroup](https://docs.aws.amazon.com/IAM/latest/APIReference/API_AddUserToGroup.html)`

------

## Remove an IAM user from an IAM group
<a name="id_groups_manage_add-remove-users-section-1"></a>

------
#### [ Console ]

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **User groups** and then choose the name of the group.

1. Choose the **Users** tab. Select the check box next to the users you want to remove and then choose **Remove users**.

------
#### [ AWS CLI ]

Run the following command:
+ `[aws iam remove-user-from-group](https://docs.aws.amazon.com/cli/latest/reference/iam/remove-user-from-group.html)`

------
#### [ API ]

Call the following operation:
+ `[RemoveUserFromGroup](https://docs.aws.amazon.com/IAM/latest/APIReference/API_RemoveUserFromGroup.html)`

------