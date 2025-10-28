# Update access keys

As a security [best practice](best-practices.md#update-access-keys "best-practices.md#update-access-keys"), we recommend that
you update IAM user access keys when needed, such as when an employee leaves your
company. IAM users can update their own access keys if they have been granted the
necessary permissions.

For details about granting IAM users permissions to update their own access keys, see
[AWS: Allows IAM users to manage their own password, access keys, and SSH public
keys on the Security credentials page](reference_policies_examples_aws_my-sec-creds-self-manage-pass-accesskeys-ssh.md "reference_policies_examples_aws_my-sec-creds-self-manage-pass-accesskeys-ssh.md"). You can also apply a password policy to your account to require that all of your IAM
users periodically update their passwords and how often they must do so. For more
information, see [Set an account password policy for
IAM users](id_credentials_passwords_account-policy.md "id_credentials_passwords_account-policy.md").

###### Note

If you lose your secret access key, you must delete the access key and create a new
one. The secret access key can be retrieved only at the time you create it. Use this
procedure to deactivate and then replace any lost access keys with new
credentials.

###### Topics

- [Updating IAM user access keys
  (console)](#rotating_access_keys_console "#rotating_access_keys_console")
- [Updating access keys (AWS CLI)](#rotating_access_keys_cli "#rotating_access_keys_cli")
- [Updating access keys (AWS API)](#rotating_access_keys_api "#rotating_access_keys_api")

## Updating IAM user access keys

(console)

You can update access keys from the AWS Management Console.

###### To update access keys for an IAM user without interrupting your applications

(console)

1. While the first access key is still active, create a second access key.
   1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
   2. In the navigation pane, choose **Users**.
   3. Choose the name of the intended user, and then choose the
      **Security credentials** tab.
   4. In the **Access keys** section, choose **Create
      access key**. On the **Access key best practices &
      alternatives** page, choose **Other**, then
      choose **Next**.
   5. (Optional) Set a description tag value for the access key to add a tag
      key-value pair to this IAM user. This can help you identify and update
      access keys later. The tag key is set to the access key id. The tag value is
      set to the access key description that you specify. When you are finished,
      choose **Create access key**.
   6. On the **Retrieve access keys** page, choose either
      **Show** to reveal the value of your user's secret
      access key, or **Download .csv file**. This is your only
      opportunity to save your secret access key. After you've saved your secret
      access key in a secure location, choose **Done**.

   When you create an access key for your user, that key pair is active by
   default, and your user can use the pair right away. At this point, the user
   has two active access keys.

2. Update all applications and tools to use the new access key.
3. Determine whether the first access key is still in use by reviewing the
   **Last used** information for the oldest access key. One
   approach is to wait several days and then check the old access key for any use
   before proceeding.
4. Even if the **Last used** information indicates that the old
   key has never been used, we recommend that you do not immediately delete the first
   access key. Instead, choose **Actions** and then choose
   **Deactivate** to deactivate the first access key.
5. Use only the new access key to confirm that your applications are working. Any
   applications and tools that still use the original access key will stop working at
   this point because they no longer have access to AWS resources. If you find such
   an application or tool, you can reactivate the first access key. Then return to
   [Step 3](#id_credentials_access-keys-key-still-in-use "#id_credentials_access-keys-key-still-in-use") and update this application to use the new key.
6. After you wait some period of time to ensure that all applications and tools
   have been updated, you can delete the first access key:
   1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
   2. In the navigation pane, choose **Users**.
   3. Choose the name of the intended user, and then choose the
      **Security credentials** tab.
   4. In the **Access keys** section for the access key you
      want to delete, choose **Actions**, and then choose
      **Delete**. Follow the instructions in the dialog to
      first **Deactivate** and then confirm the deletion.

###### To determine which access keys need to be updated or deleted(console)

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Users**.
3. If necessary, add the **Access key age** column to the users
   table by completing the following steps:
   1. Above the table on the far right, choose the settings icon (
      ![Settings icon](images/console-settings-icon.console.png)
      ).
   2. In **Manage columns**, select **Access key
      age**.
   3. Choose **Close** to return to the list of users.

4. The **Access key age** column shows the number of days since
   the oldest active access key was created. You can use this information to find
   users with access keys that might need to be updated or deleted. The column
   displays **None** for users with no access key.

## Updating access keys (AWS CLI)

You can update access keys from the AWS Command Line Interface.

###### To update access keys without interrupting your applications (AWS CLI)

1.  While the first access key is still active, create a second access key, which
    is active by default. Run the following command:
    - [`aws iam
create-access-key`](../../../cli/latest/reference/iam/create-access-key.md "../../../cli/latest/reference/iam/create-access-key.md")

    At this point, the user has two active access keys.

2.  Update all applications and tools to use the new access key.
3.  Determine whether the first access key is still in use by using this
    command:

        * [`aws iam
         get-access-key-last-used`](../../../cli/latest/reference/iam/get-access-key-last-used.md "../../../cli/latest/reference/iam/get-access-key-last-used.md")

    One approach is to wait several days and then check the old access key for any
    use before proceeding.

4.  Even if step [Step 3](#step-determine-use "#step-determine-use")
    indicates no use of the old key, we recommend that you do not immediately delete
    the first access key. Instead, change the state of the first access key to
    `Inactive` using this command:
    - [`aws iam
update-access-key`](../../../cli/latest/reference/iam/update-access-key.md "../../../cli/latest/reference/iam/update-access-key.md")

5.  Use only the new access key to confirm that your applications are working. Any
    applications and tools that still use the original access key will stop working at
    this point because they no longer have access to AWS resources. If you find such
    an application or tool, you can switch its state back to `Active` to
    reactivate the first access key. Then return to step [Step 2](#step-update-apps "#step-update-apps") and update this
    application to use the new key.
6.  After you wait some period of time to ensure that all applications and tools
    have been updated, you can delete the first access key with this command:
    - [`aws iam
delete-access-key`](../../../cli/latest/reference/iam/delete-access-key.md "../../../cli/latest/reference/iam/delete-access-key.md")

## Updating access keys (AWS API)

You can update access keys using the AWS API.

###### To update access keys without interrupting your applications (AWS API)

1.  While the first access key is still active, create a second access key, which
    is active by default. Call the following operation:
    - [`CreateAccessKey`](../APIReference/API_CreateAccessKey.md "../APIReference/API_CreateAccessKey.md")

    At this point, the user has two active access keys.

2.  Update all applications and tools to use the new access key.
3.  Determine whether the first access key is still in use by calling this
    operation:

        * [`GetAccessKeyLastUsed`](../APIReference/API_GetAccessKeyLastUsed.md "../APIReference/API_GetAccessKeyLastUsed.md")

    One approach is to wait several days and then check the old access key for any
    use before proceeding.

4.  Even if step [Step 3](#step-determine-use-2 "#step-determine-use-2") indicates no use of the old key, we recommend that you do not immediately
    delete the first access key. Instead, change the state of the first access key to
    `Inactive` calling this operation:
    - [`UpdateAccessKey`](../APIReference/API_UpdateAccessKey.md "../APIReference/API_UpdateAccessKey.md")

5.  Use only the new access key to confirm that your applications are working. Any
    applications and tools that still use the original access key will stop working at
    this point because they no longer have access to AWS resources. If you find such
    an application or tool, you can switch its state back to `Active` to
    reactivate the first access key. Then return to step [Step 2](#step-update-apps-2 "#step-update-apps-2") and update this
    application to use the new key.
6.  After you wait some period of time to ensure that all applications and tools
    have been updated, you can delete the first access key calling this
    operation:
    - [`DeleteAccessKey`](../APIReference/API_DeleteAccessKey.md "../APIReference/API_DeleteAccessKey.md")
