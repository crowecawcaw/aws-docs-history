# Assigning Stacks to Users in Amazon WorkSpaces Applications

You can assign one or more stacks to one or more users in the user pool. After
they are assigned to at least one stack, users can log in to WorkSpaces Applications and launch applications.
If users are assigned to more than one stack, they are presented with a list of
stacks as catalogs to choose from before launching applications.

###### Note

Stacks can't be assigned to users if the stacks are associated with a fleet that is joined to
an Active Directory domain.

###### To assign a stack to users

1. Open the WorkSpaces Applications console at
   [https://console.aws.amazon.com/appstream2](https://console.aws.amazon.com/appstream2 "https://console.aws.amazon.com/appstream2").
2. In the left navigation pane, choose **User Pool** and
   select the users you want.
3. Choose **Actions**, **Assign stack**.
   For more information, see [Using Active Directory with WorkSpaces Applications](active-directory.md "active-directory.md").
4. Review the list to confirm that the correct users are specified. For
   **Stack**, choose the stack you want to assign.
5. By default, **Send email notification to user** is
   enabled. Clear this option if you do not want to send the notification email
   to users now.
6. Choose **Assign stack**.
