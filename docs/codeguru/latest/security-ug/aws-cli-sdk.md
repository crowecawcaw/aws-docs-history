On November 20, 2025, AWS will discontinue support for Amazon CodeGuru Security. After
November 20, 2025, you will no longer be able to access the /codeguru/security console, service
resources, or documentation. For more information, see [End of support for CodeGuru Security](end-of-support.md "end-of-support.md").

# Install and configure the AWS CLI and AWS SDKs

## AWS CLI

To call Amazon CodeGuru Security commands from the AWS Command Line Interface (AWS CLI) on a
local development machine, you must install the AWS CLI.

If you have an older version of the AWS CLI installed, we recommend you upgrade it so the
Amazon CodeGuru Security commands are available. To check the version, use the `aws --version`
command.

###### To install and configure the AWS CLI

1. To install or upgrade the AWS CLI, follow the instructions in [Getting started with the
   AWS CLI](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md").
2. To configure the AWS CLI, see [Configuring the AWS CLI](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md") in the
   _AWS Command Line Interface User Guide_ and [Managing access keys for
   IAM users](../../../IAM/latest/UserGuide/id_credentials_access-keys.md "../../../IAM/latest/UserGuide/id_credentials_access-keys.md") in the _IAM User Guide_.

###### Important

When you configure the AWS CLI, you are prompted to specify an AWS Region. Choose one of
the supported Regions listed in
[Amazon CodeGuru Security endpoints and quotas](../../../en_us/general/latest/gr/codeguru-security.md "../../../en_us/general/latest/gr/codeguru-security.md") in the
_AWS General Reference_. 3. To verify the installation or upgrade, run the following command from the
AWS CLI.

```
aws codeguru-security help
```

If successful, this command displays a list of available CodeGuru Security commands.

## AWS SDKs

Download and install the AWS SDKs that you want to use. For more information about the
SDKs and how to install the programming languages you want to use with AWS, see [Tools to Build on AWS](https://aws.amazon.com/developer/tools/ "https://aws.amazon.com/developer/tools/").
