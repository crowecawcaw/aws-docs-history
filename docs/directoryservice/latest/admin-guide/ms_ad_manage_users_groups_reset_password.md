# Resetting an AWS Managed Microsoft AD user password

Users must adhere to password policies as defined in the Active Directory. Sometimes this
can get the best of users, including the Active Directory administrator, and they forget their
password. When this happens, you can quickly reset the user's password using AWS Directory Service if the
user resides AWS Managed Microsoft AD.

You must be signed in as a user with the necessary permissions to reset passwords. For more
information about permissions, see [Overview of managing access permissions to
your AWS Directory Service resources](IAM_Auth_Access_Overview.md "IAM_Auth_Access_Overview.md").

You can reset the password for any user in your Active Directory with the following exceptions:

- You can reset the password for any user within the Organizational Unit (OU) that is
  based off of the NetBIOS name you used when you created your Active Directory. For example, if you
  followed the procedure in [Creating your AWS Managed Microsoft AD](ms_ad_getting_started.md#ms_ad_getting_started_create_directory "ms_ad_getting_started.md#ms_ad_getting_started_create_directory") your NetBIOS name would be CORP
  and the users passwords you could reset would be members of Corp/Users OU.
- You cannot reset the password of any user outside of the OU that is based off the
  NetBIOS name you used when you created your Active Directory. For example, you cannot
  reset the password for a user in **AWS Reserved OU**. For more
  information about the OU structure for AWS Managed Microsoft AD, see [What gets created with your
  AWS Managed Microsoft AD](ms_ad_getting_started_what_gets_created.md "ms_ad_getting_started_what_gets_created.md").
  For more information on how the password policies are applied when a password is reset in
  AWS Managed Microsoft AD, see [How password policies are applied](ms_ad_password_policies.md#how_password_policies_applied "ms_ad_password_policies.md#how_password_policies_applied").

**You can use any of the following tools to reset an AWS Managed Microsoft AD user password:**

- AWS Management Console
- AWS CLI
- PowerShell

AWS Management Console
Use the following procedure to reset an AWS Managed Microsoft AD user password with the AWS Management Console.

1. In the [AWS Directory Service
   console](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/") navigation pane, under **Active Directory**, choose
   **Directories**, and then select the Active Directory in the list where
   you want to reset a user password.
2. On the **Directory details** page, choose
   **Actions**, and then choose **Reset user
   password**.
3. In the **Reset user password** dialog, in
   **Username** type the username of the user whose password needs to
   change.
4. Type a password in **New password** and **Confirm
   password**, and then choose **Reset password**.

AWS CLI
Use the following procedure to reset an AWS Managed Microsoft AD user password with the AWS CLI.

1. To install the AWS CLI, see [Install or update the latest
   version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").
2. Open the AWS CLI.
3. Type the following command and replace the Directory ID, username `jane.doe`, and
   password `P@ssw0rd` with your Active Directory Directory ID and desired credentials. See
   [reset-user-password](../../../cli/latest/reference/ds/reset-user-password.md "../../../cli/latest/reference/ds/reset-user-password.md") in the _AWS CLI Command Reference_
   for more information.

```
aws ds reset-user-password --directory-id `d-1234567890` --user-name "`jane.doe`" --new-password "`P@ssw0rd`"
```

PowerShell
Use the following procedure to reset an AWS Managed Microsoft AD user password with the PowerShell.

1. Connect to the instance joined to your Active Directory domain as the Active Directory administrator.
2. Open PowerShell.
3. Type the following command replacing the username `jane.doe`, the Directory ID, and
   password `P@ssw0rd` with your Active Directory Directory ID and desired credentials. See
   [Reset-DSUserPassword Cmdlet](../../../powershell/latest/reference/items/Reset-DSUserPassword.md "../../../powershell/latest/reference/items/Reset-DSUserPassword.md") for more information.

```
Reset-DSUserPassword -UserName "`jane.doe`" -DirectoryId `d-1234567890` -NewPassword "`P@ssw0rd`"
```
