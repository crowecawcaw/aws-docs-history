AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md "service-rename.md")

# Managing user roles as an administrator in Amazon Q Developer in chat applications

Administrators can unmap user roles from channel members' chat client IDs from the **User
permissions** page in the Amazon Q Developer in chat applications console. Administrators can also
require user roles by enabling a user role requirement in the **User
permissions** page. This requirement can be applied to all
workspaces and channels or to individual channel configurations. For more
information on user role requirements, see [User role
requirement](understanding-permissions.md#role-reqs "understanding-permissions.md#role-reqs").

###### Note

Administrators can't map user roles. Only channel members have this ability.

###### Topics

- [Unmapping a user role in Amazon Q Developer in chat applications](#admin-unmap-role "#admin-unmap-role")
- [Enabling a user role requirement in Amazon Q Developer in chat applications](#admin-ur-req "#admin-ur-req")

## Unmapping a user role in Amazon Q Developer in chat applications

You can unmap a user role from a chat client ID. When you unmap a user role, it will no longer appear your **Mapped roles** table.

###### Note

Unmapping user roles doesn't impact the ability to use Amazon Q Developer in the Amazon Q Developer console or in other places where
Amazon Q Developer is available.

###### To unmap a user role

1. Open the [Amazon Q Developer in chat applications
   console](https://console.aws.amazon.com/chatbot/ "https://console.aws.amazon.com/chatbot/").
2. Under **Account settings**, choose **User permissions**.
3. In **Mapped roles**, select the roles you want to unmap.
4. Choose **Unmap**.

## Enabling a user role requirement in Amazon Q Developer in chat applications

You can enable a user role requirement to force users to apply a user role before running commands in Microsoft Teams and Slack.

###### To enable a user role requirement

1. Open the [Amazon Q Developer in chat applications
   console](https://console.aws.amazon.com/chatbot/ "https://console.aws.amazon.com/chatbot/").
2. Under **Account settings**, choose **User permissions**.
3. In **User role requirement**, enable a user role requirement.
