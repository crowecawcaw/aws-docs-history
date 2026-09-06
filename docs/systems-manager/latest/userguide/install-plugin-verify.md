

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Verify the Session Manager plugin installation
<a name="install-plugin-verify"></a>

Run the following commands to verify that the Session Manager plugin installed successfully.

```
session-manager-plugin
```

If the installation was successful, the following message is returned.

```
The Session Manager plugin is installed successfully. Use the AWS CLI to start a session.
```

You can also test the installation by running the [start-session](https://docs.aws.amazon.com/cli/latest/reference/ssm/start-session.html) command in the the [AWS Command Line Interface](https://aws.amazon.com/cli/) (AWS CLI). In the following command, replace {{instance-id}} with your own information.

```
aws ssm start-session --target {{instance-id}}
```

This command will work only if you have installed and configured the AWS CLI, and if your Session Manager administrator has granted you the necessary IAM permissions to access the target managed node using Session Manager.