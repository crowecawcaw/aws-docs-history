# Install the CloudWatch agent on on-premises servers

If you downloaded the CloudWatch agent on a computer and created your agent configuration
file, you can use that configuration file to install the agent in other on-premises servers.

## Download the CloudWatch agent on an on-premises server

You can download the CloudWatch agent package using either Systems Manager Run Command or an Amazon S3
download link.

### Download using Systems Manager

To use Systems Manager Run Command, you must register your on-premises server with Amazon EC2 Systems Manager. For
more information, see [Setting Up Systems Manager in Hybrid Environments](../../../systems-manager/latest/userguide/systems-manager-managedinstances.md "../../../systems-manager/latest/userguide/systems-manager-managedinstances.md") in the
_AWS Systems Manager User Guide_.

If you have already registered your server, update SSM Agent to the latest
version.

For information about updating SSM Agent on a server running Linux, see [Install SSM Agent for a Hybrid Environment (Linux)](../../../systems-manager/latest/userguide/systems-manager-managedinstances.md#sysman-install-managed-linux "../../../systems-manager/latest/userguide/systems-manager-managedinstances.md#sysman-install-managed-linux") in the
_AWS Systems Manager User Guide_.

For information about updating the SSM Agent on a server running Windows Server, see
[Install SSM Agent for a Hybrid Environment (Windows)](../../../systems-manager/latest/userguide/systems-manager-managedinstances.md#sysman-install-managed-win "../../../systems-manager/latest/userguide/systems-manager-managedinstances.md#sysman-install-managed-win") in the
_AWS Systems Manager User Guide_.

###### To use the SSM Agent to download the CloudWatch agent package on an on-premises server

1. Open the Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose
   **Run Command**.

-or-

If the AWS Systems Manager home page opens, scroll down and
choose **Explore Run Command**. 3. Choose **Run command**. 4. In the **Command document** list, select the button next to
**AWS-ConfigureAWSPackage**. 5. In the **Targets** area, select the server to install the CloudWatch
agent on. If you don't see a specific server, it might not be configured for
Run Command. For more information, see [Setting Up AWS Systems Manager for
Hybrid Environments](../../../systems-manager/latest/userguide/systems-manager-managedinstances.md "../../../systems-manager/latest/userguide/systems-manager-managedinstances.md") in the _AWS Systems Manager User Guide_. 6. In the **Action** list, choose
**Install**. 7. In the **Name** box, enter
`AmazonCloudWatchAgent`. 8. Keep **Version** blank to install the latest version of the
agent. 9. Choose **Run**.

The agent package is downloaded, and the next steps are to configure and start
it.

## (Installing on an on-premises server) Specify IAM credentials and AWS Region

To enable the CloudWatch agent to send data from an on-premises server, you must specify the
access key and secret key of the IAM user that you created earlier.

You also must specify the AWS Region to send the metrics to, using the
`region` field.

Following is an example of this file.

```
[AmazonCloudWatchAgent]
aws_access_key_id=`my_access_key`
aws_secret_access_key=`my_secret_key`
region = `us-west-1`
```

For `my_access_key` and
`my_secret_key`, use the keys from the IAM user that doesn't
have the permissions to write to Systems Manager Parameter Store.

If you name this profile `AmazonCloudWatchAgent`, you don't need to do
anything more. Optionally, you can give it a different name and specify that name as the
value for `shared_credential_profile` in the`common-config.toml` file, which is explained in the following section.

Following is an example of using the **aws configure** command to
create a named profile for the CloudWatch agent. This example assumes that you're using the
default profile name of `AmazonCloudWatchAgent`.

###### To create the AmazonCloudWatchAgent profile for the CloudWatch agent

1. If you haven't already done so, install the AWS Command Line Interface on the server. For more
   information, see [Installing the
   AWS CLI](../../../cli/latest/userguide/cli-chap-install.md "../../../cli/latest/userguide/cli-chap-install.md").
2. On Linux servers, enter the following command and follow the prompts:

```
sudo aws configure --profile AmazonCloudWatchAgent
```

On Windows Server, open PowerShell as an administrator, enter the following
command, and follow the prompts.

```
aws configure --profile AmazonCloudWatchAgent
```

## (Optional) Modifying the common configuration and named profile for CloudWatch agent

The CloudWatch agent includes a configuration file called
`common-config.toml`. You can optionally use this file to specify
proxy and Region information.

On a server running Linux, this file is in the
`/opt/aws/amazon-cloudwatch-agent/etc` directory. On a server running Windows
Server, this file is in the `C:\ProgramData\Amazon\AmazonCloudWatchAgent`
directory.

The default `common-config.toml` is as follows:

```
# This common-config is used to configure items used for both ssm and cloudwatch access


## Configuration for shared credential.
## Default credential strategy will be used if it is absent here:
##            Instance role is used for EC2 case by default.
##            AmazonCloudWatchAgent profile is used for onPremise case by default.
# [credentials]
#    shared_credential_profile = "{profile_name}"
#    shared_credential_file= "{file_name}"

## Configuration for proxy.
## System-wide environment-variable will be read if it is absent here.
## i.e. HTTP_PROXY/http_proxy; HTTPS_PROXY/https_proxy; NO_PROXY/no_proxy
## Note: system-wide environment-variable is not accessible when using ssm run-command.
## Absent in both here and environment-variable means no proxy will be used.
# [proxy]
#    http_proxy = "{http_url}"
#    https_proxy = "{https_url}"
#    no_proxy = "{domain}"
```

All lines are commented out initially. To set the credential profile or proxy
settings, remove the `#` from that line and specify a value. You can edit this
file manually, or by using the `RunShellScript` Run Command in Systems Manager:

- `shared_credential_profile` – For on-premises servers, this line
  specifies the IAM user credential profile to use to send data to CloudWatch. If you keep
  this line commented out, `AmazonCloudWatchAgent` is used. For more
  information about creating this profile, see [(Installing on an on-premises server) Specify IAM credentials and AWS Region](#install-CloudWatch-Agent-iam_user-SSM-onprem "#install-CloudWatch-Agent-iam_user-SSM-onprem").

On an EC2 instance, you can use this line to have the CloudWatch agent send data from
this instance to CloudWatch in a different AWS Region. To do so, specify a named profile
that includes a `region` field specifying the name of the Region to send
to.

If you specify a `shared_credential_profile`, you must also remove the
`#` from the beginning of the `[credentials]` line.

- `shared_credential_file` – To have the agent look for
  credentials in a file located in a path other than the default path, specify that
  complete path and file name here. The default path is `/root/.aws` on Linux
  and is `C:\\Users\\Administrator\\.aws` on Windows Server.

The first example below shows the syntax of a valid
`shared_credential_file` line for Linux servers, and the second example
is valid for Windows Server. On Windows Server, you must escape the \
 characters.

```
shared_credential_file= "/usr/`username`/credentials"
```

```
shared_credential_file= "C:\\Documents and Settings\\`username`\\.aws\\credentials"
```

If you specify a `shared_credential_file`, you must also remove the
`#` from the beginning of the `[credentials]` line.

- Proxy settings – If your servers use HTTP or HTTPS proxies to contact AWS
  services, specify those proxies in the `http_proxy` and
  `https_proxy` fields. If there are URLs that should be excluded from
  proxying, specify them in the `no_proxy` field, separated by commas.
