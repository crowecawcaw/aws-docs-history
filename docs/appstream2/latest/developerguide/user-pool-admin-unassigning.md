

# Unassigning Stacks from Users in Amazon WorkSpaces Applications
<a name="user-pool-admin-unassigning"></a>

You can unassign a stack from one or more users in the user pool. After a stack is unassigned from users, they can't launch applications from the stack. If users are connected when you unassign the stack, their sessions remain active until the session cookie expires (about one hour).

**To unassign a stack from users**

1. Open the WorkSpaces Applications console at [https://console.aws.amazon.com/appstream2](https://console.aws.amazon.com/appstream2).

1. In the left navigation pane, choose **User Pool** and select the users you want.

1. Choose **Actions**, **Unassign stack**.

1. Review the list to confirm that the correct users are specified. For **Stack**, choose the stack you want to unassign. The list includes all stacks, assigned or unassigned.

1. Choose **Unassign stack**.