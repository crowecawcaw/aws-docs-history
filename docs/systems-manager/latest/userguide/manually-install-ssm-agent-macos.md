

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Manually installing and uninstalling SSM Agent on EC2 instances for macOS
<a name="manually-install-ssm-agent-macos"></a>

Connect to your macOS instance and perform the following steps to install AWS Systems Manager Agent (SSM Agent). Perform these steps on each instance that will run commands using Systems Manager. The commands provided in this procedure can also be passed to Amazon EC2 instances as scripts through user data.

**Important**  
We strongly recommend that you avoid using OS versions that have reached End-of-Life (EOL). OS vendors including AWS typically don't provide security patches or other updates for versions that have reached EOL. Continuing to use an EOL system greatly increases the risk of not being able to apply upgrades, including security fixes, and other operational problems. AWS does not test Systems Manager functionality on OS versions that have reached EOL.

**Before you begin**  
Install `wget` using Homebrew.

**To install SSM Agent on macOS**

1. Download the agent installer file for x86\_64 instances using the following command.

   In the following command, replace {{region}} with your own information. For a list of supported {{region}} values, see the **Region** column in [Systems Manager service endpoints](https://docs.aws.amazon.com/general/latest/gr/ssm.html#ssm_region) in the *Amazon Web Services General Reference*.

   ```
   sudo wget https://s3.{{region}}.amazonaws.com/amazon-ssm-{{region}}/latest/darwin_amd64/amazon-ssm-agent.pkg
   ```

   For Apple silicon instances use the following command.

   ```
   sudo wget https://s3.{{region}}.amazonaws.com/amazon-ssm-{{region}}/latest/darwin_arm64/amazon-ssm-agent.pkg
   ```

   Here is an example.

   ```
   sudo wget https://s3.us-east-2.amazonaws.com/amazon-ssm-us-east-2/latest/darwin_amd64/amazon-ssm-agent.pkg
   ```

1. Use the following command to run the SSM Agent installer. 

   x86\_64:

   ```
   sudo installer -pkg amazon-ssm-agent.pkg -target /
   ```

1. Check the status of the agent.

   To determine if SSM Agent is running, check the agent log at `/var/log/amazon/ssm/amazon-ssm-agent.log` .

1. Run the following command to start the service if the the agent log indicates that "amazon-ssm-agent is stopped."

   ```
   sudo launchctl load -w /Library/LaunchDaemons/com.amazon.aws.ssm.plist && sudo launchctl start com.amazon.aws.ssm
   ```

**Important**  
An updated version of SSM Agent is released whenever new tools are added to Systems Manager or updates are made to existing tools. Failing to use the latest version of the agent can prevent your managed node from using various Systems Manager tools and features. For that reason, we recommend that you automate the process of keeping SSM Agent up to date on your machines. For information, see [Automating updates to SSM Agent](ssm-agent-automatic-updates.md). Subscribe to the [SSM Agent Release Notes](https://github.com/aws/amazon-ssm-agent/blob/mainline/RELEASENOTES.md) page on GitHub to get notifications about SSM Agent updates.