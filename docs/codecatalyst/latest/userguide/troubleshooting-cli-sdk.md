Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Troubleshooting problems between Amazon CodeCatalyst and the AWS SDKs or the AWS CLI

The following information can help you troubleshoot common issues when working with CodeCatalyst and the AWS CLI or the AWS SDKs.

###### Topics

- [I receive an error when I enter aws codecatalyst at a command line or terminal saying it's an invalid choice](#cli-sdk-troubleshoot-no-commands "#cli-sdk-troubleshoot-no-commands")
- [I receive a credentials error when I run aws codecatalyst commands](#cli-sdk-troubleshoot-profile "#cli-sdk-troubleshoot-profile")

## I receive an error when I enter **aws codecatalyst** at a command line or terminal saying it's an invalid choice

**Problem:** When I try to use the AWS CLI with CodeCatalyst, one or more of the **aws codecatalyst** commands are not recognized as valid.

**Solution:** The most common cause for this problem is
that you are using a version of the AWS CLI that does not contain the most recent updates
for the latest services and commands. Update your installation of the AWS CLI and then try
again. For more information see [Setting up to use the AWS CLI with CodeCatalyst](set-up-cli.md "set-up-cli.md").

## I receive a credentials error when I run **aws codecatalyst** commands

**Problem:** When I try to use the AWS CLI with CodeCatalyst, I receive a message stating `You can configure credentials by running "aws configure".`
or `Unable to locate authorization token`.

**Solution:** You must configure an AWS CLI profile to work
with CodeCatalyst commands. For more information see [Setting up to use the AWS CLI with CodeCatalyst](set-up-cli.md "set-up-cli.md").
