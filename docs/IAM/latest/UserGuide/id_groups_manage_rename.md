# Rename an IAM user group

When you change a user group's name or path, the following happens:

- Any policies attached to the user group stay with the group under the new name.
- The user group retains all its users under the new name.
- The unique ID for the user group remains the same. For more information about unique
  IDs, see [Unique identifiers](reference_identifiers.md#identifiers-unique-ids "reference_identifiers.md#identifiers-unique-ids").
  IAM does not automatically update policies that refer to the user group as a resource to
  use the new name. Therefore, you must be careful when you rename a user group. Before you rename
  your user group, you must manually check all of your policies to find any policies where that
  user group is mentioned by name. For example, let's say Bob is the manager of the testing part
  of the organization. Bob has a policy attached to his IAM user entity that lets him add and
  remove users from the Test user group. If an administrator changes the name of the user group
  (or changes the group path), the administrator must also update the policy attached to Bob to
  use the new name or path. Otherwise Bob won't be able to add and remove users from the user
  group.

###### To find policies that refer to an IAM group as a resource:

1. From the navigation pane of the IAM console, choose
   **Policies**.
2. Sort by the **Type** column to find your **Customer
   managed** custom policies.
3. Choose the policy name of the policy to edit.
4. Choose the **Permissions** tab, and then choose
   **Summary**.
5. Choose **IAM** from the list of services, if it exists.
6. Look for the name of your user group in the **Resource** column.
7. Choose **Edit** to change the name of your user group in the
   policy.

## To change the name of an IAM user group

Console

1. In the navigation pane, select
   **User groups** and then select the group name.
2. Choose
   **Edit**. Type the new user group name and then choose **Save
   changes**.

AWS CLI
Run the following command:

- [aws iam
  update-group](../../../cli/latest/reference/iam/update-group.md "../../../cli/latest/reference/iam/update-group.md")

API
Call the following operation:

- [UpdateGroup](../APIReference/API_UpdateGroup.md "../APIReference/API_UpdateGroup.md")
