# Create a WorkSpace in WorkSpaces Personal

WorkSpaces enables you to provision virtual, cloud-based Windows and Linux desktops for your users,
known as _WorkSpaces_.

Before creating a personal WorkSpace, create a directory by doing one of the following:

- Create a Simple AD directory.
- Create an AWS Directory Service for Microsoft Active Directory, also known as AWS Managed Microsoft AD.
- Connect to an existing Microsoft
  Active Directory by using Active Directory Connector.
- Create a trust relationship between your
  AWS Managed Microsoft AD directory and your on-premises domain.
- Create a dedicated directory that uses Microsoft Entra ID as the identity source
  (through IAM Identity Center). WorkSpaces in the directory are native Entra ID-joined and enrolled
  into Microsoft Intune through Microsoft Windows Autopilot user-driven mode.

###### Note

Such directories currently only support Windows 10 and 11 Bring Your Own Licenses
personal WorkSpaces.

- Create a dedicated directory that uses an identity provider of your choice as the identity source
  (through IAM Identity Center). WorkSpaces in the directory are native Entra ID-joined and enrolled
  into Microsoft Intune through Microsoft Windows Autopilot user-driven mode.

###### Note

Such directories currently only support Windows 10 and 11 Bring Your Own Licenses
personal WorkSpaces.
Now that you have created a directory, you are ready to create a personal WorkSpace.

###### To create a personal WorkSpace

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. In the navigation pane, choose **WorkSpaces**.
3. Choose **Launch WorkSpaces**, **Personal**.
4. Choose **Create WorkSpaces**
5. Under **Onboarding** (optional), you can choose **Recommend options to me based
   on my use case** to get recommendations on the type of WorkSpace you want to use.
   You can skip this step if you know that you want to use personal WorkSpaces.
6. Choose **Next**. WorkSpaces registers your AD Connector.
7. Under **Configure WorkSpaces**, enter the following details:
   - For **Bundle**, choose from the following the bundle type that you want to use for your WorkSpaces.
     - **Use a base WorkSpaces bundle** - Choose one of the bundles from the
       drop down. For more information about the bundle type you selected, choose **Bundle details**.
       To compare bundles offered for pools, choose **Compare all bundles**.
     - **Use your own custom or BYOL bundle** - Choose a bundle that you previously created.
       To create a custom bundle, see [Create a custom WorkSpaces image and bundle for WorkSpaces Personal](create-custom-bundle.md "create-custom-bundle.md").

   ###### Note

   Review the recommended uses and specifications of each bundle to help ensure you select the bundle that works best for your users. For more information about each use case, see [Amazon WorkSpaces
   Bundles](https://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles "https://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles"). For more information about bundle specifications, recommended uses, and pricing, see [Amazon WorkSpaces pricing](https://aws.amazon.com/workspaces/pricing/ "https://aws.amazon.com/workspaces/pricing/").
   - For **Running mode**, choose from the following to configure your
     personal WorkSpace’s immediate availability and how you pay for it (monthly or hourly):
     - **AlwaysOn** — Bills monthly fee for unlimited usage of your WorkSpaces.
       This mode is best for users who use their WorkSpace full time as their primary desktop.
     - **AutoStop** — Bills by the hour. With this mode,
       your WorkSpaces stop after a specified period of disconnection, and the state of apps and
       data is saved.

   - For **Tags**, specify the key pair value that you want to use.
     A key can be a general category, such as "project," "owner," or "environment," with specific associated values.

8. Under **Select directory**, enter the following details:
   - Choose the directory that you created. To create a directory, choose
     **Create directory**. For more information about creating personal directories, see
     [Register an existing AWS Directory Service directory with WorkSpaces Personal](register-deregister-directory.md "register-deregister-directory.md").
   - Choose the users from that directory you want to provision personal WorkSpaces for by doing the following.
     1. Choose **Create users**.
     2. Enter the user’s **Username**, **First name**,
        **Last name**, and **Email**. To add additional users,
        choose **Create additional user** and enter their information.

9. Under **Customization** (optional), you can customize bundles,
   root and user volume encryption, and user volume for all users or specific users.
10. Choose Create WorkSpaces. The initial status of the WorkSpace is PENDING.
    When the creation is complete, the status is AVAILABLE and an invitation is sent to the
    email address that you specified for the users.
11. Send invitations to the email address for each user. For more information, see
    [Send an invitation email](manage-workspaces-users.md#send-invitation "manage-workspaces-users.md#send-invitation").

###### Note

    * These invitations aren't sent automatically if you're using AD Connector
     or a trust relationship.
    * Invitation emails aren't sent if the user already exists in Active Directory.
     Instead, make sure you manually send the user an invitation email. For more information, see
     [Send an invitation email](manage-workspaces-users.md#send-invitation "manage-workspaces-users.md#send-invitation").
    * In all Regions, the text of the invitation email is in English (US). In the
     following Regions, the English text is preceded by a second language:




    	+ Asia Pacific (Seoul): Korean
    	+ Asia Pacific (Tokyo): Japanese
    	+ Canada (Central): French (Canadian)
    	+ China (Ningxia): Simplified Chinese

## Connect to the WorkSpace

You can connect to your WorkSpace using the client of your choice. After you sign in, the client
displays the WorkSpace desktop.

###### To connect to the WorkSpace

1. Open the link in the invitation email.
2. Review [WorkSpaces Clients](../userguide/amazon-workspaces-clients.md "../userguide/amazon-workspaces-clients.md")
   in the _Amazon WorkSpaces User Guide_ for more information about the requirements
   for each client, and then do one of the following:
   - When prompted, download one of the client applications or launch Web Access.
   - If you aren't prompted and you haven't installed a client application already,
     open [https://clients.amazonworkspaces.com/](https://clients.amazonworkspaces.com/ "https://clients.amazonworkspaces.com/")

   and download one of the client applications or launch Web Access.

###### Note

You cannot use a web browser (Web Access) to connect to Amazon Linux WorkSpaces. 3. Start the client, enter the registration code from the invitation
email, and choose **Register**. 4. When prompted to sign in, enter the the user's sign-in credentials, and then
choose **Sign In**. 5. (Optional) When prompted to save your credentials, choose **Yes**.

###### Note

Because you're using AD Connector, your users won't be able to reset their own passwords. (The
**Forgot password?** option on the WorkSpaces client application login screen won't
be available.) For information about how to reset user passwords, see
[Set up Active Directory Administration Tools for WorkSpaces Personal](directory_administration.md "directory_administration.md").

## Next steps

You can continue to customize the WorkSpace that you just created. For example, you can install
software and then create a custom bundle from your WorkSpace. You can also perform various administrative
tasks for your WorkSpaces and your WorkSpaces directory. If you are finished with your WorkSpace,
you can delete it. For more information, see the following documentation.

- [Create a custom WorkSpaces image and bundle for WorkSpaces Personal](create-custom-bundle.md "create-custom-bundle.md")
- [Administer WorkSpaces Personal](administer-workspaces.md "administer-workspaces.md")
- [Manage directories for WorkSpaces Personal](manage-workspaces-directory.md "manage-workspaces-directory.md")
- [Delete a WorkSpace in WorkSpaces Personal](delete-workspaces.md "delete-workspaces.md")

For more information about using the WorkSpaces client applications, such as setting up multiple monitors or
using peripheral devices, see [WorkSpaces Clients](../userguide/amazon-workspaces-clients.md "../userguide/amazon-workspaces-clients.md")
and [Peripheral Device Support](../userguide/peripheral_devices.md "../userguide/peripheral_devices.md")
in the _Amazon WorkSpaces User Guide_.
