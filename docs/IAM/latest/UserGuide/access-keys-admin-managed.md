# How an IAM administrator can manage

IAM user access keys

IAM administrators can create, activate, deactivate, and delete the access keys
associated with individual IAM users. They can also list the IAM users in the account
which have access keys and locate which IAM user has a specific access key.

###### Topics

- [To create an access key for an
  IAM user](#admin-create-access-key "#admin-create-access-key")
- [To deactivate an access key for an
  IAM user](#admin-deactivate-access-key "#admin-deactivate-access-key")
- [To activate an access key for an
  IAM user](#admin-activate-access-key "#admin-activate-access-key")
- [To delete an access key for an
  IAM user](#admin-delete-access-key "#admin-delete-access-key")
- [To list the access keys for an
  IAM user](#admin-list-access-key "#admin-list-access-key")
- [To list the access keys for an
  IAM user](#admin-list-access-key "#admin-list-access-key")
- [To display all the access key IDs for users
  in your account](#admin-list-all-access-keys "#admin-list-all-access-keys")
- [To use an access key ID to find a
  user](#admin-find-user-access-keys "#admin-find-user-access-keys")
- [To find the most recent use of
  an access key ID](#admin-find-most-recent-use-access-keys "#admin-find-most-recent-use-access-keys")

## To create an access key for an

IAM user

Console

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Users**.
3. Choose the user name to go to the user details page.
4. On **Security credentials** tab, in
   the **Access keys** section, choose **Create
   access key**.

If the button is deactivated, then you must delete one of the
existing keys before you can create a new one. 5. On the **Access key best practices &
alternatives** page, review the best practices and
alternatives. Choose your use case to learn about additional options
which can help you avoid creating a long-term access key. 6. If you determine that your use case still requires an access key,
choose **Other** and then choose
**Next**. 7. **(Optional)** On the **Set description
tag** page, you can add a description tag to the access
key to help track your access key. Select **Create access
key**. 8. On the **Retrieve access key page**, choose
**Show** to reveal the value of your user's secret
access key. 9. To save the access key ID and secret access key to a
`.csv` file to a secure location on your
computer, choose the **Download .csv file**
button.

###### Important

This is your only time to view or download the newly created
access key and you cannot recover it. Make sure you securely
maintain your access key.

When you create an access key for your user, that key pair is active by
default, and your user can use the pair right away.

AWS CLI
Run the following command:

- [`aws iam
create-access-key`](../../../cli/latest/reference/iam/create-access-key.md "../../../cli/latest/reference/iam/create-access-key.md")

API
Call the following operation:

- [`CreateAccessKey`](../APIReference/API_CreateAccessKey.md "../APIReference/API_CreateAccessKey.md")

## To deactivate an access key for an

IAM user

Console

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Users**.
3. Choose the user name to go to the user details page.
4. On **Security credentials** tab, in
   the **Access keys** section, choose the
   **Actions** drop-down menu, then choose
   **Deactivate**.
5. In the **Deactivate** dialog box, confirm that you
   want to deactivate the access key by selecting
   **Deactivate**

After an access key is deactivated, it can no longer be used by API
calls. You can activate it again if needed.

AWS CLI
Run the following command:

- [`aws iam
update-access-key`](../../../cli/latest/reference/iam/update-access-key.md "../../../cli/latest/reference/iam/update-access-key.md")

API
Call the following operation:

- [`UpdateAccessKey`](../APIReference/API_UpdateAccessKey.md "../APIReference/API_UpdateAccessKey.md")

## To activate an access key for an

IAM user

Console

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Users**.
3. Choose the user name to go to the user details page.
4. On **Security credentials** tab, in
   the **Access keys** section, choose the
   **Actions** drop-down menu, then choose
   **Activate**.

After an access key is activated, it can be used by API calls. You can
deactivate it again if needed.

AWS CLI
Run the following command:

- [`aws iam
update-access-key`](../../../cli/latest/reference/iam/update-access-key.md "../../../cli/latest/reference/iam/update-access-key.md")

API
Call the following operation:

- [`UpdateAccessKey`](../APIReference/API_UpdateAccessKey.md "../APIReference/API_UpdateAccessKey.md")

## To delete an access key for an

IAM user

After an access key has been deactivated, if it is no longer required, delete
it.

Console

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Users**.
3. Choose the user name to go to the user details page.
4. On **Security credentials** tab, in
   the **Access keys** section, choose the
   **Actions** drop-down menu for the inactive access
   key, then choose **Delete**.
5. In the **Delete** dialog box, confirm that you
   want to delete the access key by entering the access key ID in the
   text input field and then selecting
   **Delete**.

After an access key is deleted, it can't be recovered.

AWS CLI
Run the following command:

- [`aws iam
delete-access-key`](../../../cli/latest/reference/iam/delete-access-key.md "../../../cli/latest/reference/iam/delete-access-key.md")

API
Call the following operation:

- [`DeleteAccessKey`](../APIReference/API_DeleteAccessKey.md "../APIReference/API_DeleteAccessKey.md")

## To list the access keys for an

IAM user

You can view a list of the access key IDs associated with an IAM user.

Console

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Users**.
3. Choose the user name to go to the user details page.
4. On **Security credentials** tab, the
   the **Access keys** section lists the access keys for
   the user.

Each IAM user can have two access keys.

AWS CLI
Run the following command:

- [`aws iam
list-access-keys`](../../../cli/latest/reference/iam/list-access-keys.md "../../../cli/latest/reference/iam/list-access-keys.md")

API
Call the following operation:

- [`ListAccessKeys`](../APIReference/API_ListAccessKeys.md "../APIReference/API_ListAccessKeys.md")

## To list the access keys for an

IAM user

You can view a list of the access key IDs associated with an IAM user.

Console

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Users**.
3. Choose the user name to go to the user details page.
4. On **Security credentials** tab, the
   **Access keys** section lists the access key IDs
   for the user including the status of each key displayed.

###### Note

Only the user's access key ID is visible. The secret access key
can only be retrieved when the key is created.

Each IAM user can have two access keys.

AWS CLI
Run the following command:

- [`aws iam
list-access-keys`](../../../cli/latest/reference/iam/list-access-keys.md "../../../cli/latest/reference/iam/list-access-keys.md")

API
Call the following operation:

- [`ListAccessKeys`](../APIReference/API_ListAccessKeys.md "../APIReference/API_ListAccessKeys.md")

## To display all the access key IDs for users

in your account

You can view a list of the access key IDs for users in your AWS account.

Console

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Users**.
3. Choose the user name to go to the user details page.
4. If necessary, add the **Access key ID** column to
   the users table by completing the following steps:
   1. Above the table on the far right, choose the
      **Preferences** icon (
      ![Preferences icon](images/console-settings-icon.console.png)
      ).
   2. In the **Preferences** dialog box, under
      **Select visible columns** turn on
      **Access key ID**.
   3. Choose **Confirm** to return to the list of
      users. The list is updated to include the access key ID.

5. The **Access key ID** column shows the state of
   each access key, followed by its ID; for example,
   **`Active - AKIAIOSFODNN7EXAMPLE`**
   or **`Inactive - AKIAI44QH8DHBEXAMPLE`**.

You can use this information to view and copy the access keys IDs
for users with one or two access keys. The column displays
**`-`** for users with no access
key.

###### Note

The secret access key can only be retrieved when the key is
created.

Each IAM user can have two access keys.

## To use an access key ID to find a

user

You can use an access key ID to find a user in your AWS account.

Console

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, in the search box, enter the
   **Access key ID**, for example
   AKIAI44QH8DHBEXAMPLE.
3. The IAM user that the access key ID is associated with appears in
   the navigation pane. Choose the user name to go to the user details
   page.

## To find the most recent use of

an access key ID

The most recent use of an access key is displayed in the user's list on the
IAM users page, on the user detail page, and is part of the credential report.

Console

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In users list, see the **Access key last used**
   column.

If the column is not displayed, choose the
**Preferences** icon (
![Preferences icon](images/console-settings-icon.console.png)
) and under **Select visible
columns** turn on **Access key last
used** to display the column. 3. (optional) In the navigation pane, under **Access
reports**, select **Credential report**
to download a report that includes the access key last used
information for all of the IAM users in your account. 4. (optional) Select the IAM user to view the user details. The
**Summary** section includes the access key IDs,
their status, and when they were last used.

AWS CLI
Run the following command:

- [`aws iam get-access-key-last-used`](../../../cli/latest/reference/iam/get-access-key-last-used.md "../../../cli/latest/reference/iam/get-access-key-last-used.md")

API
Call the following operation:

- [`GetAccessKeyLastUsed`](../APIReference/API_GetAccessKeyLastUsed.md "../APIReference/API_GetAccessKeyLastUsed.md")
