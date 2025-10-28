# View IAM users

You can list the IAM users in your AWS account or in a specific IAM group, and list
all the IAM groups that a user is in. For information about the permissions that you
need in order to list users, see [Permissions required to access IAM
resources](access_permissions-required.md "access_permissions-required.md").

## To list all the IAM users in your

account

Console

1. Follow the sign-in procedure appropriate to your user type as described in the topic [How to sign in to AWS](../../../signin/latest/userguide/how-to-sign-in.md "../../../signin/latest/userguide/how-to-sign-in.md") in the _AWS Sign-In User
   Guide_.
2. On the **IAM Console Home** page, in the left navigation pane, enter your query in the **Search IAM** text box.
3. In the navigation pane, choose **Users**.

The console displays the IAM users in your AWS account.

AWS CLI
Run the following command:

- `aws iam
list-users`

API
Call the following operation:

- `ListUsers`

## To list the IAM users in an

IAM group

Console

1. Follow the sign-in procedure appropriate to your user type as described in the topic [How to sign in to AWS](../../../signin/latest/userguide/how-to-sign-in.md "../../../signin/latest/userguide/how-to-sign-in.md") in the _AWS Sign-In User
   Guide_.
2. On the **IAM Console Home** page, in the left navigation pane, enter your query in the **Search IAM** text box.
3. In the navigation pane, choose **User
   groups**.
4. Choose the name of the user group.

The IAM users that are members of the group are listed on the
**Users** tab.

AWS CLI
Run the following command:

- `aws iam
get-group`

API
Call the following operation:

- `GetGroup`

## To list all the IAM groups that

a user is in

Console

1. Follow the sign-in procedure appropriate to your user type as described in the topic [How to sign in to AWS](../../../signin/latest/userguide/how-to-sign-in.md "../../../signin/latest/userguide/how-to-sign-in.md") in the _AWS Sign-In User
   Guide_.
2. On the **IAM Console Home** page, in the left navigation pane, enter your query in the **Search IAM** text box.
3. In the navigation pane, choose **Users**.
4. In the **Users** list, choose the name of the
   IAM user.
5. Select the **Groups** tab to display the list of
   groups that include the current user.

AWS CLI
Run the following command:

- `aws
iam list-groups-for-user`

API
Call the following operation:

- `ListGroupsForUser`

## Next steps

Once you have a list of your IAM users, you can rename, delete, or deactivate an
IAM user using the following procedures.

- [Rename an IAM user](id_users_rename.md "id_users_rename.md")
- [Remove or deactivate an IAM user](id_users_remove.md "id_users_remove.md")
