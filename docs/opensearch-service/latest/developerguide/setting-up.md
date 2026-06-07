# Setting up Amazon OpenSearch Service

## Grant permissions

### Sign up for an AWS account

To get started with AWS, you need an AWS account. For information about creating an AWS account, see
[Getting started with an AWS account](../../../accounts/latest/reference/getting-started.md "../../../accounts/latest/reference/getting-started.md")
in the _AWS Account Management Reference Guide_.

## Install and configure the AWS CLI

If you want to use OpenSearch Service APIs, you must install the latest version of the
AWS Command Line Interface (AWS CLI). You don't need the AWS CLI to use OpenSearch Service from the console, and
you can get started without the CLI by following the steps in [Getting started with Amazon OpenSearch Service](gsg.md "gsg.md").

###### To set up the AWS CLI

1. To install the latest version of the AWS CLI for macOS, Linux, or Windows, see
   [Installing or
   updating the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").
2. To configure the AWS CLI and secure setup of your access to AWS services,
   including OpenSearch Service, see [Quick configuration with `aws configure`](../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-config "../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-config").
3. To verify the setup, enter the following DataBrew command at the command
   prompt.

```
aws opensearch help
```

AWS CLI commands use the default AWS Region from your configuration, unless
you set it with a parameter or a profile. To set your AWS Region with a
parameter, you can add the `--region` parameter to each
command.

To set your AWS Region with a profile, first add a named profile in the
`~/.aws/config` file or the
`%UserProfile%/.aws/config` file (for Microsoft Windows). Follow
the steps in [Named profiles for
the AWS CLI](../../../cli/latest/userguide/cli-configure-profiles.md "../../../cli/latest/userguide/cli-configure-profiles.md"). Next, set your AWS Region and other settings with a
command similar to the one in the following example.

```
[profile opensearch]
aws_access_key_id = ACCESS-KEY-ID-OF-IAM-USER
aws_secret_access_key = SECRET-ACCESS-KEY-ID-OF-IAM-USER
region = us-east-1
output = text
```

## Open the console

Most of the console-oriented topics in this section start from the [OpenSearch Service console](https://console.aws.amazon.com/aos/home "https://console.aws.amazon.com/aos/home"). If you aren't already signed in
to your AWS account, sign in, then open the [OpenSearch Service
console](https://console.aws.amazon.com/aos/home "https://console.aws.amazon.com/aos/home") and continue to the next section to continue getting started with
OpenSearch Service.
