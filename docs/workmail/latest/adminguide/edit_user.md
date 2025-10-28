# Editing user details

When you edit the user details, you can change the following:

- **Personal data** – Names, email
  address, phone numbers, and other personal details.
- **Mailbox quotas (sizes)** – Quotas
  can range from 1 MB to 51,200 MB (50 GB). Amazon WorkMail notifies users when they
  reach 90 percent of their quota. Also, changing a user's mailbox quota won't
  affect pricing. For more information about pricing, refer to [Amazon WorkMail Pricing](https://aws.amazon.com/workmail/pricing/ "https://aws.amazon.com/workmail/pricing/").
- **Mobile device access** – Remove and
  wipe devices, and view device details.
- **Mailbox access permissions** – Grant
  users permission to use a mailbox, and grant users different levels of
  access to the mailbox.
- **Personal access tokens (when IAM Identity Center is enabled)** – View and delete personal access tokens.

###### Note

If you integrate Amazon WorkMail with an AD Connector directory, you can't edit these
details from the AWS Management Console. Instead, you must edit them using your Active
Directory management tools. Limitations apply when your organization is in
interoperability mode. For more information, see [Limitations in interoperability mode](interoperability.md#interop_limitations "interoperability.md#interop_limitations").

###### To edit the user details

1. Open the Amazon WorkMail console at
   [https://console.aws.amazon.com/workmail/](https://console.aws.amazon.com/workmail/ "https://console.aws.amazon.com/workmail/").

If necessary, change the AWS Region. In the bar at the top of the console window, open
the **Select a Region** list and choose a Region. For more information, see [Regions and
endpoints](../../../general/latest/gr/index.md "../../../general/latest/gr/index.md") in the _Amazon Web Services General Reference_. 2. In the navigation pane, choose **Organizations**, then choose the organization that you want to use. 3. In the navigation pane, choose **Users**, and then choose
the name of the user to edit.

###### To edit personal data

1. In the **User details** section, choose
   **Edit**.
2. Under **User details**, enter or change the
   user's personal information as needed.
3. When finished, choose **Save changes**.

###### To associate with an IAM Identity Center user

1. Under **User details**, choose **Edit**.
2. Enter the user ID of the IAM Identity Center user you want to associate. You can view this information under the **Assigned Users** table in the IAM Identity Center page or in the IAM Identity Center console.
3. Choose **Save changes**.

###### To edit mailbox quotas

1. Under **User details**, choose the
   **Quota** tab, and then choose
   **Edit**.
2. In the **Update mailbox quota** box, enter a size
   for the mailbox. You can enter values from `1`
   to `51200`.
3. Choose **Save changes**.

###### To manage mobile device data

###### Note

To manage mobile devices, your users first need to connect their
devices to your instance of Amazon WorkMail. For information about connecting
mobile devices, refer to [Setting up mobile
device clients for Amazon WorkMail](../userguide/mobile-client.md "../userguide/mobile-client.md").

1. Under **User details**, choose the
   **Mobile devices** tab.
2. To see a current list of devices, choose
   **Refresh**.
3. To view a device's details, choose the device name from the
   **Device ID** column.
4. To remove or wipe the device, choose the radio button next to the
   device name, and then choose **Remove** or
   **Wipe** as needed.
5. In the dialog box that appears, confirm the removal or wipe
   operation. Remember that users will reappear when they sync their
   devices with Amazon WorkMail again.

###### To edit mailbox permissions

1.  Choose the **Permissions** tab.
2.  Do one of the following:

        1. To add permissions, choose **Add
         permissions**. Open the **Add new
         permissions** list and choose a user or group,
         choose the permission settings for the user or group, and
         then choose **Save**.
        2. To edit user permissions, choose the button next to
         the user's name. Choose **Edit**, select
         the desired options, and then choose
         **Save**.

    For more information about the permission options, refer to [Working with mailbox permissions](mail_perms_overview.md "mail_perms_overview.md").

3.  To remove all permissions, choose **Remove**,
    then confirm the removal.

###### To delete personal access tokens

###### Note

Make sure the token you are deleting is not actively used by any email client. Deleting a token when in use will break the authentication for the clients using the token.

1. Choose the **Personal Access Tokens** tab.
2. From the list of personal access tokens, select the personal access token to delete.
3. Choose **Delete token**.
4. Enter **Type** in the confirmation text box.
