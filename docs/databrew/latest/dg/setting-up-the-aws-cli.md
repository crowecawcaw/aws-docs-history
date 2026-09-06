

# Setting up the AWS CLI
<a name="setting-up-the-aws-cli"></a>

If you plan to use JupyterLab or the DataBrew API, make sure to install the AWS Command Line Interface (AWS CLI). You don't need it to use the DataBrew console or perform the steps in the Getting Started exercises. 

**To set up the AWS CLI**

1. Download and configure the AWS CLI by using the steps found following:
   + [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)
   + [Configuration Basics](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)

1. Verify the setup by entering the following DataBrew command at the command prompt.

   ```
   aws databrew help
   ```

   If this statement returns the error "`aws: error: argument command: Invalid choice`" followed by a long list of services, uninstall the AWS CLI, and then reinstall. This action doesn't overwrite your existing configuration.

AWS CLI commands use the default AWS Region from your configuration, unless you set it with a parameter or a profile. You can add the `--region` parameter to each command. 

If you prefer, you can add a [named profile](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html) in `~/.aws/config` or `%UserProfile%/.aws/config` (on Microsoft Windows). Named profiles can also preserve other settings, as shown in the following example. 

```
[profile {{databrew}}]
aws_access_key_id = {{ACCESS-KEY-ID-OF-IAM-USER}}
aws_secret_access_key = {{SECRET-ACCESS-KEY-ID-OF-IAM-USER}}
region = {{us-east-1}}
output = {{text}}
```