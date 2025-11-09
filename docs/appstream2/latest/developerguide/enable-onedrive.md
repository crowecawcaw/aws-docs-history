# Enable OneDrive for Your WorkSpaces Applications Users

Before enabling OneDrive, you must do the following:

- Have an active Microsoft Office 365 or OneDrive for Business account with
  a valid organizational domain and users in the domain to use with WorkSpaces Applications.
- Configure an WorkSpaces Applications stack with an associated fleet.

The fleet must use an image that uses a version of the WorkSpaces Applications agent
released on or after July 26, 2018. For more information, see [WorkSpaces Applications Agent Release Notes](agent-software-versions.md "agent-software-versions.md"). The fleet must also have access to
the internet.

- Have a Windows-based stack. (Linux-based stacks are not supported).
  Follow these steps to enable OneDrive for your WorkSpaces Applications users.

###### To enable OneDrive while creating a stack

- Follow the steps in [Create a Stack in Amazon WorkSpaces Applications](set-up-stacks-fleets-install.md "set-up-stacks-fleets-install.md"), make sure that
  **Enable OneDrive** is selected, and that you have
  specified at least one organizational domain that is associated with your
  OneDrive for Business account.

###### To enable OneDrive for an existing stack

1. Open the WorkSpaces Applications console at
   [https://console.aws.amazon.com/appstream2](https://console.aws.amazon.com/appstream2 "https://console.aws.amazon.com/appstream2").
2. In the left navigation pane, choose **Stacks**, and
   select the stack for which to enable OneDrive.
3. Below the stacks list, choose **Storage**, and select
   **Enable OneDrive for Business**.
4. In the **Enable OneDrive for Business** dialog box, in
   **OneDrive domain name**, type the name of at least one
   organizational domain that is associated with your OneDrive account. To
   specify another domain, choose **Add another domain**, and
   type the name of the domain.
5. For each domain, you can specify whether users need to get admin consent
   before linking their OneDrive for Business account to WorkSpaces Applications.
   **Require OneDrive for Business admin consent** is
   disabled by default. When you check the box, users are prompted to get the
   admin consent before linking their OneDrive for Business account.
6. After you add OneDrive domain names, choose
   **Enable**.
   Before your users can use OneDrive with WorkSpaces Applications, you must provide them with
   permissions to link their OneDrive account with third-party web applications. To do
   so, follow the steps in the next section.

###### Important

You must configure your Microsoft Azure Active Directory environment to allow
end-user consent to applications. For more information, see [Configure how end-users consent to applications](https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/configure-user-consent "https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/configure-user-consent") in the Azure Active
Directory [Application management](https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/ "https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/") documentation.

###### Provide Your Users with Permissions to Link OneDrive

with WorkSpaces Applications

You must enable Integrated Apps in your Office 365 or OneDrive for Business
admin console before users can link their OneDrive for Business account to
WorkSpaces Applications.

1. Sign in to Office 365 or the OneDrive for Business admin console.
2. In the left navigation pane of the console, choose
   **Settings**, **Services &
   add-ins**.
3. From the list of services and add-ins, choose **Integrated
   Apps**.
4. On the **Integrated apps** page, turn on the option to
   allow users in your organization to let third party web apps access their
   Office 365 information.

###### Note

For guidance that you can provide your users to help them get started with
using OneDrive during WorkSpaces Applications streaming sessions, see [Use OneDrive for Business](onedrive-end-user.md "onedrive-end-user.md").
