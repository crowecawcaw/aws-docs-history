Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Setting up to use the AWS CLI with CodeCatalyst

The Amazon CodeCatalyst console is where you'll work on most of your daily tasks. However, you
might want to set up and configure the AWS CLI when you're working with Dev Environments, personal
access tokens, or logs of events in CodeCatalyst. You must install the AWS CLI and configure a
profile before you can use it with CodeCatalyst.

# To set up the AWS CLI for CodeCatalyst

1. Install the latest version of the AWS CLI. If you already have a version of the AWS CLI installed,
   make sure that it is recent and includes commands for CodeCatalyst, and update it if
   needed. To verify that you have a version installed that includes CodeCatalyst commands,
   open a command prompt and run the following command:

```
aws codecatalyst help
```

If you see a list of CodeCatalyst commands, you have a version that supports CodeCatalyst. If
the command is not recognized, update your version of the AWS CLI to the latest
version. For more information, see [Installing or updating
the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the AWS Command Line Interface User Guide. 2. Run the **aws configure** command to create a profile if you don't have one or if you want
to use a named profile specifically for CodeCatalyst. We recommend creating a named profile
to use specifically with CodeCatalyst, but you can also use the default profile. For more information, see
[Configuration basics](../../../cli/latest/userguide/cli-configure-quickstart.md "../../../cli/latest/userguide/cli-configure-quickstart.md"). 3. Edit the `config` file for the profile to add a section for connecting to CodeCatalyst as follows.
The `config` file is located at `~/.aws/config` on Linux or macOS, or at
`C:\Users\`USERNAME`\.aws\config` on Windows.

```
[profile codecatalyst]
region = `us-west-2`
sso_session = `codecatalyst`

[sso-session codecatalyst]
sso_region = `us-east-1`
sso_start_url = `https://view.awsapps.com/start`
sso_registration_scopes = `codecatalyst:read_write`
```

4. Save the file.
5. Before attempting to run any CodeCatalyst commands, open a new terminal or command prompt and run the following command to request and retrieve credentials to run `aws codecatalyst` commands.
   Replace `codecatalyst` with the name of your profile if needed.

```
aws sso login --profile codecatalyst
```

To view examples of **codecatalyst** commands, see the following topics:

- [Grant users repository access with personal access tokens](ipa-tokens-keys.md "ipa-tokens-keys.md")
- [Accessing logged events using event logging](ipa-logs.md "ipa-logs.md")
