# Change permissions for an IAM user

You can change the permissions for an IAM user in your AWS account by changing its group
memberships, by copying permissions from an existing user, by attaching policies directly to a
user, or by setting a [permissions boundary](access_policies_boundaries.md "access_policies_boundaries.md"). A
permissions boundary controls the maximum permissions that a user can have. Permissions
boundaries are an advanced AWS feature.

For information about the permissions that you need in order to modify the permissions for a
user, see [Permissions required to access IAM
resources](access_permissions-required.md "access_permissions-required.md").

###### Topics

- [View user access](#users-modify_prerequisites "#users-modify_prerequisites")
- [Generate a policy based on a user's
  access activity](#users_change_permissions-gen-policy "#users_change_permissions-gen-policy")
- [Adding permissions to a user
  (console)](#users_change_permissions-add-console "#users_change_permissions-add-console")
- [Changing permissions for a user
  (console)](#users_change_permissions-change-console "#users_change_permissions-change-console")
- [To remove a permissions
  policy from a user (console)](#users_change_permissions-remove-policy-console "#users_change_permissions-remove-policy-console")
- [To remove the permissions
  boundary from a user (console)](#users_change_permissions-remove-boundary-console "#users_change_permissions-remove-boundary-console")
- [Adding and removing a user's
  permissions (AWS CLI or AWS API)](#users_change_permissions-add-programmatic "#users_change_permissions-add-programmatic")

## View user access

Before you change the permissions for a user, you should review its recent service-level
activity. This is important because you don't want to remove access from a principal (person
or application) who is using it. For more information about viewing last accessed information,
see [Refine permissions in AWS using last
accessed information](access_policies_last-accessed.md "access_policies_last-accessed.md").

## Generate a policy based on a user's

access activity

You might sometimes grant permissions to an IAM entity (user or role) beyond what they
require. To help you refine the permissions that you grant, you can generate an IAM policy
that is based on the access activity for an entity. IAM Access Analyzer reviews your AWS CloudTrail logs
and generates a policy template that contains the permissions that have been used by the
entity in your specified date range. You can use the template to create a managed policy with
fine-grained permissions and then attach it to the IAM entity. That way, you grant only the
permissions that the user or role needs to interact with AWS resources for your specific use
case. To learn more, see [IAM Access Analyzer policy
generation](access-analyzer-policy-generation.md "access-analyzer-policy-generation.md").

## Adding permissions to a user

(console)

IAM offers three ways to add permissions policies to a user:

- **Add the IAM user to an IAM group** – Make
  the user a member of a group. The policies from the group are attached to the user.
- **Copy permissions from an existing IAM user** –
  Copy all group memberships, attached managed policies, inline policies, and any existing
  permissions boundaries from the source user.
- **Attach policies directly to the IAM user** –
  Attach a managed policy directly to the user. For easier permissions management, attach
  your policies to a group and then make IAM users members of the appropriate
  groups.

###### Important

If the user has a permissions boundary, then you cannot add more permissions to the user
than are allowed by the permissions boundary.

### To add permissions by adding

the IAM user to a group

Adding an IAM user to an IAM group updates the user's permissions with the
permissions defined for the group immediately.

Console

1. Follow the sign-in procedure appropriate to your user type as described in the topic [How to sign in to AWS](../../../signin/latest/userguide/how-to-sign-in.md "../../../signin/latest/userguide/how-to-sign-in.md") in the _AWS Sign-In User
   Guide_.
2. On the **IAM Console Home** page, in the left navigation pane, enter your query in the **Search IAM** text box.
3. In the navigation pane, choose **Users**.
4. In the **Users** list, choose the name of the IAM user.
5. Select the **Groups** tab to display the list of groups that
   include the current user.
6. Choose **Add user to groups**.
7. Select the checkbox for each group that you want the user to join. The list
   shows each group's name and the policies that the user receives if made a member
   of that group.
8. (Optional) You can choose **Create group** to define a new
   group. This is useful if you want to add the user to a group with different
   attached policies than the existing groups:
   1. In the new tab, for **User group name**, type a name for
      your new group.

   ###### Note

   The number and size of IAM resources in an AWS account are limited. For more information, see [IAM and AWS STS quotas](reference_iam-quotas.md "reference_iam-quotas.md"). Group names can be a combination of up to 128 letters,
   digits, and these characters: plus (+), equal (=), comma (,), period (.), at
   sign (@), and hyphen (-). Names must be unique within an account. They are
   not distinguished by case. For example, you cannot create two groups named
   _TESTGROUP_ and _testgroup_. 2. Select one or more checkboxes for the managed policies that you want to
   attach to the group. You can also create a new managed policy by choosing
   **Create policy**. If you do, return to this browser tab or
   window when the new policy is done; choose **Refresh**; and
   then choose the new policy to attach it to your group. For more information,
   see [Define custom IAM permissions with customer managed
   policies](access_policies_create.md "access_policies_create.md"). 3. Choose **Create user group**. 4. Return to the original tab, refresh your list of groups. Then select the
   checkbox for your new group.

9. Choose **Add user to group(s)**.

The console displays a status message informing you that the user has been added
to the groups you specified.

### To add permissions by copying

from another IAM user

If you choose to add permissions to an IAM user by copying permissions, IAM copies
all group memberships, attached managed policies, inline policies, and any existing
permissions boundaries from the specified user and applies them immediately to the currently
selected user.

Console

1. Follow the sign-in procedure appropriate to your user type as described in the topic [How to sign in to AWS](../../../signin/latest/userguide/how-to-sign-in.md "../../../signin/latest/userguide/how-to-sign-in.md") in the _AWS Sign-In User
   Guide_.
2. On the **IAM Console Home** page, in the left navigation pane, enter your query in the **Search IAM** text box.
3. In the navigation pane, choose **Users**.
4. In the **Users** list, choose the name of the IAM user.
5. On the **Permissions** tab choose and select **Add
   permissions**.
6. On the **Add permissions** page, choose **Copy
   permissions**. The list displays available IAM users along with their
   group memberships and attached policies.
7. Select the radio button next to the user whose permissions you want to copy.
8. Choose **Next** to see the list of changes that are to be
   made to the user. Then choose **Add permissions**.

The console displays a status message informing you that the permissions were
copied from the IAM user you specified.

### To add permissions by

attaching policies directly to the IAM user

You can attach a managed policy directly to an IAM user. The updated permissions are
applied immediately.

Console

1. Follow the sign-in procedure appropriate to your user type as described in the topic [How to sign in to AWS](../../../signin/latest/userguide/how-to-sign-in.md "../../../signin/latest/userguide/how-to-sign-in.md") in the _AWS Sign-In User
   Guide_.
2. On the **IAM Console Home** page, in the left navigation pane, enter your query in the **Search IAM** text box.
3. In the navigation pane, choose **Users**.
4. In the **Users** list, choose the name of the IAM user.
5. On the **Permissions** tab, choose and select **Add
   permissions**.
6. On the **Add permissions** page, choose **Attach
   policies directly**. The **Permissions policies** list
   displays available policies along with their policy types and attached entities.
7. Select the radio button next to the **Policy name** you want
   to attach.
8. Choose **Next** to see the list of changes that are to be
   made to the user. Then choose **Add permissions**.

The console displays a status message informing you that the policy was added to
the IAM user you specified.

### To set the permissions

boundary for an IAM user

A permissions boundary is an advanced feature for managing permissions in AWS that is
used to set the maximum permissions that an IAM user can have. Setting a permissions
boundary immediately restricts the IAM user permissions to the boundary, regardless of the
other permissions granted.

Console

1. Follow the sign-in procedure appropriate to your user type as described in the topic [How to sign in to AWS](../../../signin/latest/userguide/how-to-sign-in.md "../../../signin/latest/userguide/how-to-sign-in.md") in the _AWS Sign-In User
   Guide_.
2. On the **IAM Console Home** page, in the left navigation pane, enter your query in the **Search IAM** text box.
3. In the navigation pane, choose **Users**.
4. In the **Users** list, choose the name of the IAM user
   whose permissions boundary you want to change.
5. Choose the **Permissions** tab. If necessary, open the
   **Permissions boundary** section and then choose **Set
   permissions boundary**.
6. On the **Set permissions boundary** page, under
   **Permissions policies** select the policy that you want to use
   for the permissions boundary.
7. Choose **Set boundary**.

The console displays a status message informing you that the permissions boundary
has been added.

## Changing permissions for a user

(console)

IAM allows you to change the permissions that are associated with a user in the
following ways:

- **Edit a permissions policy** – Edit a user's
  inline policy, the inline policy of the user's group, or edit a managed policy that is
  attached to the user directly or from a group. If the user has a permissions boundary,
  then you cannot provide more permissions than are allowed by the policy that was used as
  the user's permissions boundary.
- **Changing the permissions boundary** – Change the
  policy that is used as the permissions boundary for the user. This can expand or restrict
  the maximum permissions that a user can have.

### Editing a permissions policy

attached to a user

Changing permissions updates the user's access immediately.

Console

1. Follow the sign-in procedure appropriate to your user type as described in the topic [How to sign in to AWS](../../../signin/latest/userguide/how-to-sign-in.md "../../../signin/latest/userguide/how-to-sign-in.md") in the _AWS Sign-In User
   Guide_.
2. On the **IAM Console Home** page, in the left navigation pane, enter your query in the **Search IAM** text box.
3. In the navigation pane, choose **Users**.
4. In the **Users** list, choose the name of the IAM user
   whose permissions boundary you want to change.
5. Choose the **Permissions** tab. If necessary, open the
   **Permissions boundary** section.
6. Choose the name of the policy that you want to edit to view details about the
   policy. Choose the **Entities attached** tab to view other
   entities (IAM users, groups, and roles) that might be affected if you edit the
   policy.
7. Choose the **Permissions** tab and review the permissions
   granted by the policy. To make changes to the permissions, choose
   **Edit**.
8. Edit the policy and resolve any [policy validation](access_policies_policy-validator.md "access_policies_policy-validator.md")
   recommendations. For more information, see [Edit IAM policies](access_policies_manage-edit.md "access_policies_manage-edit.md").
9. Choose **Next**, review the policy summary, and then choose
   **Save changes**.

The console displays a status message informing you that the policy has been
updated.

### To change the permissions

boundary for a user

Changing a permissions boundary updates the user's access immediately.

Console

1. Follow the sign-in procedure appropriate to your user type as described in the topic [How to sign in to AWS](../../../signin/latest/userguide/how-to-sign-in.md "../../../signin/latest/userguide/how-to-sign-in.md") in the _AWS Sign-In User
   Guide_.
2. On the **IAM Console Home** page, in the left navigation pane, enter your query in the **Search IAM** text box.
3. In the navigation pane, choose **Users**.
4. In the **Users** list, choose the name of the IAM user
   whose permissions boundary you want to change.
5. Choose the **Permissions** tab. If necessary, open the
   **Permissions boundary** section and then choose
   **Change boundary**.
6. Select the policy that you want to use for the permissions boundary.
7. Choose **Set boundary**.

The console displays a status message informing you that the permissions boundary
has been changed.

## To remove a permissions

policy from a user (console)

Removing a permissions policy updates the user's access immediately.

Console

1. Follow the sign-in procedure appropriate to your user type as described in the topic [How to sign in to AWS](../../../signin/latest/userguide/how-to-sign-in.md "../../../signin/latest/userguide/how-to-sign-in.md") in the _AWS Sign-In User
   Guide_.
2. On the **IAM Console Home** page, in the left navigation pane, enter your query in the **Search IAM** text box.
3. In the navigation pane, choose **Users**.
4. Choose the name of the user whose permissions policies you want to remove.
5. Choose the **Permissions** tab.
6. If you want to remove permissions by removing an existing policy, view the
   **Attached via** column to understand how the user is getting
   that policy before choosing **Remove** to remove the policy:
   - If the policy applies because of group membership, then choosing
     **Remove** removes the user from the group. Remember that you
     might have multiple policies attached to a single group. If you remove a user
     from a group, the user loses access to _all_
     policies that it received through that group membership.
   - If the policy is a managed policy attached directly to the user, then
     choosing **Remove** detaches the policy from the user. This
     does not affect the policy itself or any other entity that the policy might be
     attached to.
   - If the policy is an inline embedded policy, then choosing
     **Remove** removes the policy from IAM. Inline policies
     that are attached directly to a user exist only on that user.

If the policy was granted to the user through a group membership, the console
displays a status message informing you that the IAM user was removed from the
IAM group. If the policy directly attached or inline, the status message informs you
that the policy has been removed.

## To remove the permissions

boundary from a user (console)

Removing the permissions boundary updates the user's access immediately.

Console

1. Follow the sign-in procedure appropriate to your user type as described in the topic [How to sign in to AWS](../../../signin/latest/userguide/how-to-sign-in.md "../../../signin/latest/userguide/how-to-sign-in.md") in the _AWS Sign-In User
   Guide_.
2. On the **IAM Console Home** page, in the left navigation pane, enter your query in the **Search IAM** text box.
3. In the navigation pane, choose **Users**.
4. In the **Users** list, choose the name of the IAM user
   whose permissions boundary you want to remove.
5. Choose the **Permissions** tab. If necessary, open the
   **Permissions boundary** section.
6. Choose **Change boundary**. To confirm that you want to remove the permissions boundary, in the confirmation dialog, choose **Remove boundary**.

The console displays a status message informing you that the permissions boundary
has been removed.

## Adding and removing a user's

permissions (AWS CLI or AWS API)

To add or remove permissions programmatically, you must add or remove the group
memberships, attach or detach the managed policies, or add or delete the inline policies. For
more information, see the following topics:

- [Edit users in IAM groups](id_groups_manage_add-remove-users.md "id_groups_manage_add-remove-users.md")
- [Adding and removing IAM identity
  permissions](access_policies_manage-attach-detach.md "access_policies_manage-attach-detach.md")
