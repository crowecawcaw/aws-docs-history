# Use `ChangePassword` with a CLI

The following code examples show how to use `ChangePassword`.

CLI

**AWS CLI**

**To change the password for your IAM user**

To change the password for your IAM user, we recommend using the `--cli-input-json` parameter to pass a JSON file that contains your old and new passwords. Using this method, you can use strong passwords with non-alphanumeric characters. It can be difficult to use passwords with non-alphanumeric characters when you pass them as command line parameters. To use the `--cli-input-json` parameter, start by using the `change-password` command with the `--generate-cli-skeleton` parameter, as in the following example.

```
`aws iam change-password \
 --generate-cli-skeleton `>` `change-password.json``

```

The previous command creates a JSON file called change-password.json that you can use to fill in your old and new passwords. For example, the file might look like the following.

```
{
    "OldPassword": "3s0K_;xh4~8XXI",
    "NewPassword": "]35d/{pB9Fo9wJ"
}
```

Next, to change your password, use the `change-password` command again, this time passing the `--cli-input-json` parameter to specify your JSON file. The following `change-password` command uses the `--cli-input-json` parameter with a JSON file called change-password.json.

```
`aws iam change-password \
 --cli-input-json `file://change-password.json``

```

This command produces no output.

This command can be called by IAM users only. If this command is called using AWS account (root) credentials, the command returns an `InvalidUserType` error.

For more information, see [How an IAM user changes their own password](id_credentials_passwords_user-change-own.md "id_credentials_passwords_user-change-own.md") in the _AWS IAM User Guide_.

- For API details, see
  [ChangePassword](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/change-password.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/change-password.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This command changes the password for the user that is running the command.
This command can be called by IAM users only. If this command is called when you are signed-in with AWS account (root) credentials, the command returns an `InvalidUserType` error.**

```
Edit-IAMPassword -OldPassword "MyOldP@ssw0rd" -NewPassword "MyNewP@ssw0rd"

```

- For API details, see
  [ChangePassword](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This command changes the password for the user that is running the command.
This command can be called by IAM users only. If this command is called when you are signed-in with AWS account (root) credentials, the command returns an `InvalidUserType` error.**

```
Edit-IAMPassword -OldPassword "MyOldP@ssw0rd" -NewPassword "MyNewP@ssw0rd"

```

- For API details, see
  [ChangePassword](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
