# AWS SAM CLI troubleshooting

This section provides details on how to troubleshoot error messages when using, installing, and managing the AWS Serverless Application Model Command Line
Interface (AWS SAM CLI).

###### Topics

- [Troubleshooting](#install-sam-cli-troubleshooting "#install-sam-cli-troubleshooting")
- [Error messages](#sam-cli-troubleshoot-messages "#sam-cli-troubleshoot-messages")
- [Warning messages](#sam-cli-troubleshoot-warning "#sam-cli-troubleshoot-warning")

## Troubleshooting

For troubleshooting guidance related to AWS SAM CLI, see [Troubleshooting installation errors](install-sam-cli.md#sam-cli-troubleshoot-install "install-sam-cli.md#sam-cli-troubleshoot-install").

## Error messages

### Curl error: "curl: (6) Could not

resolve: ..."

When trying to invoke the API Gateway endpoint, you see the following error:

```
curl: (6) Could not resolve: endpointdomain (Domain name not found)
```

This means that you've attempted to send a request to a domain that's not valid. This
can happen if your serverless application failed to deploy successfully, or if you have a
typo in your **curl** command. Verify that the application deployed
successfully by using the AWS CloudFormation console or the AWS CLI, and verify that your
**curl** command is correct.

### Error: Can’t find exact

resource information with given stack name

When running the `sam remote invoke` command on an application that contains
a single Lambda function resource, you see the following error:

```
Error: Can't find exact resource information with given <stack-name>. Please provide full resource ARN or --stack-name to resolve the ambiguity.
```

**Possible cause: You didn’t provide the `--stack-name` option.**

If a function ARN is not provided as an argument, the `sam remote
 invoke` command requires that the `--stack-name` option is
provided.

**Solution: Provide the `--stack-name` option.**

The following is an example:

```
`$` `sam remote invoke --stack-name `sam-app``

Invoking Lambda Function HelloWorldFunction
START RequestId: 40593abb-e1ad-4d99-87bd-ac032e364e82 Version: $LATEST
END RequestId: 40593abb-e1ad-4d99-87bd-ac032e364e82
REPORT RequestId: 40593abb-e1ad-4d99-87bd-ac032e364e82  Duration: 11.31 ms      Billed Duration: 12 ms  Memory Size: 128 MB     Max Memory Used: 67 MB  Init Duration: 171.71 ms
{"statusCode":200,"body":"{\"message\":\"hello world\"}"}%
```

### Error: Can’t find resource

information from stack name

When running the `sam remote invoke` command and passing a Lambda function ARN
as an argument, you see the following error:

```
Error: Can't find resource information from stack name (<stack-name>) and resource id (<function-id>)
```

**Possible cause: You have the stack name value defined in your
`samconfig.toml` file.**

The AWS SAM CLI first checks your `samconfig.toml` file for a
stack name. If specified, the argument is passed as a logical ID value.

**Solution: Pass the function’s logical ID instead.**

You can pass the function’s logical ID as an argument instead of the function’s
ARN.

**Solution: Remove the stack name value from your configuration file.**

You can remove the stack name value from your configuration file. This prevents
the AWS SAM CLI from passing your function ARN as a logical ID value.

Run `sam build` after modifying your configuration file.

### Error: Failed to create managed

resources: Unable to locate credentials

When running the **sam deploy** command, you see the following
error:

```
Error: Failed to create managed resources: Unable to locate credentials
```

This means that you have not set up AWS credentials to enable the AWS SAM CLI to make
AWS service calls. To fix this, you must set up AWS credentials. For more information,
see [Setting up AWS
credentials](serverless-getting-started-set-up-credentials.md "serverless-getting-started-set-up-credentials.md").

### Error: FileNotFoundError in Windows

When running commands in AWS SAM CLI on Windows, you may see the following error:

```
Error: FileNotFoundError
```

Possible cause: The AWS SAM CLI might interact with filepaths that exceed the Windows max path limitation.

Solution: To resolve this issue, the new long paths behavior must enabled. To do this, see [Enable Long Paths in Windows 10, Version 1607, and Later](https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=powershell#enable-long-paths-in-windows-10-version-1607-and-later "https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=powershell#enable-long-paths-in-windows-10-version-1607-and-later") in the
_Microsoft Windows App Development Documentation_.

### Error: pip's dependency resolver

...

_Example error text_:

```
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
aws-sam-cli 1.58.0 requires aws-sam-translator==1.51.0, but you have aws-sam-translator 1.58.0 which is incompatible.
aws-sam-cli 1.58.0 requires typing-extensions==3.10.0.0, but you have typing-extensions 4.4.0 which is incompatible.
```

**Possible cause: If you use pip to install packages, dependencies
between packages may conflict.**

Each version of the `aws-sam-cli` package depends on a version of the
`aws-sam-translator` package. For example, `aws-sam-cli`
v1.58.0 may depend on `aws-sam-translator` v1.51.0.

If you install the AWS SAM CLI using pip, then install another
package which depends on a newer version of `aws-sam-translator`, the
following will occur:

- The newer version of `aws-sam-translator` will install.
- The current version of `aws-sam-cli` and the newer version of
  `aws-sam-translator` may not be compatible.
- When you use the AWS SAM CLI, the dependency resolver error will occur.

###### Solutions:

1. Use the AWS SAM CLI native package installer.
   1. Uninstall the AWS SAM CLI using pip. For instructions, see [Uninstalling the AWS SAM CLI](manage-sam-cli-versions.md#manage-sam-cli-versions-uninstall "manage-sam-cli-versions.md#manage-sam-cli-versions-uninstall").
   2. Install the AWS SAM CLI using the native package installer. For
      instructions, see [Install the AWS SAM CLI](install-sam-cli.md "install-sam-cli.md").
   3. When necessary, upgrade the AWS SAM CLI using the native package installer.
      For instructions, see [Upgrading the AWS SAM CLI](manage-sam-cli-versions.md#manage-sam-cli-versions-upgrade "manage-sam-cli-versions.md#manage-sam-cli-versions-upgrade").

2. If you must use pip, we recommend that you install the AWS SAM
   CLI into a virtual environment. This ensures a clean installation environment and
   an isolated environment if errors occur. For instructions, see [Installing the AWS SAM CLI into a virtual environment using
   pip](manage-sam-cli-versions.md#manage-sam-cli-versions-install-virtual "manage-sam-cli-versions.md#manage-sam-cli-versions-install-virtual").

### Error: No such command

‘remote’

When running the `sam remote invoke` command, you see the following
error:

```
`$` `sam remote invoke `...``
2023-06-20 08:15:07 Command remote not available
Usage: sam [OPTIONS] COMMAND [ARGS]...
Try 'sam -h' for help.

Error: No such command 'remote'.
```

**Possible cause: Your version of the AWS SAM CLI is out of date.**

The AWS SAM CLI `sam remote invoke` command was released with AWS SAM CLI
version 1.88.0. You can check your version by running the `sam --version`
command.

**Solution: Upgrade your AWS SAM CLI to the latest version.**

For instructions, see [Upgrading the AWS SAM CLI](manage-sam-cli-versions.md#manage-sam-cli-versions-upgrade "manage-sam-cli-versions.md#manage-sam-cli-versions-upgrade").

### Error: Running AWS SAM projects

locally requires Docker. Have you got it installed?

When running the **sam local start-api** command, you see the following
error:

```
Error: Running AWS SAM projects locally requires Docker. Have you got it installed?
```

This means that you do not have Docker properly installed.
Docker is required to test your application locally. To fix this, follow
the instructions for installing Docker for your development host. For more information, see
[Installing Docker](install-docker.md "install-docker.md").

### Error: Security

Constraints Not Satisfied

When running **sam deploy --guided**, you're prompted with the question
``Function` may not have authorization defined, Is this
okay? [y/N]`. If you respond to this prompt with `N` (the
default response), you see the following error:

```
Error: Security Constraints Not Satisfied
```

The prompt is informing you that the application you're about to deploy might have a
publicly accessible Amazon API Gateway API configured without authorization. By responding
`N` to this prompt, you're saying that this is not OK.

To fix this, you have the following options:

- Configure your application with authorization. For information about configuring
  authorization, see [Control API access with your AWS SAM template](serverless-controlling-access-to-apis.md "serverless-controlling-access-to-apis.md").
- If your intention is to have a publicly accessible API endpoint without
  authorization, restart your deployment and respond to this question with
  `Y` to indicate that you're OK with deploying.

### message: Missing Authentication

Token

When trying to invoke the API Gateway endpoint, you see the following error:

```
{"message":"Missing Authentication Token"}
```

This means that you've attempted to send a request to the correct domain, but the URI
isn't recognizable. To fix this, verify the full URL, and update the **curl**
command with the correct URL.

## Warning messages

### Warning: ... AWS will no longer maintain the

Homebrew installer for AWS SAM ...

When installing the AWS SAM CLI using Homebrew, you see the following warning message:

```
Warning: ... AWS will no longer maintain the Homebrew installer for AWS SAM (aws/tap/aws-sam-cli).
				For AWS supported installations, use the first party installers ...
```

**Potential cause: AWS no longer maintaining Homebrew support.**

Starting September 2023, AWS will no longer maintain the Homebrew installer for the
AWS SAM CLI.

###### Solution: Use an AWS supported installation method.

- You can find AWS supported installation methods at [Install the AWS SAM CLI](install-sam-cli.md "install-sam-cli.md").

###### Solution: To continue using Homebrew, use the community managed installer.

- You can use the community managed Homebrew installer at your discretion. For
  instructions, see [Managing the AWS SAM CLI with Homebrew](manage-sam-cli-versions.md#manage-sam-cli-versions-homebrew "manage-sam-cli-versions.md#manage-sam-cli-versions-homebrew").
