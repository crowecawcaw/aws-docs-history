

# Manage Lightsail resources with AWS CloudShell
<a name="amazon-lightsail-cloudshell"></a>

AWS CloudShell is a browser-based, pre-authenticated shell that you can launch directly from the Amazon Lightsail console. You can use CloudShell to manage your Lightsail resources from the command line interface. You can run AWS Command Line Interface (AWS CLI) commands using your preferred shell, such as Bash, PowerShell, or Z shell. You can do this without downloading or installing command line tools. For more information, see [What is AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html).

When you launch CloudShell, a [compute environment](https://docs.aws.amazon.com/cloudshell/latest/userguide/vm-specs.html#vm-configuration) that's based on Amazon Linux 2 is created. Within this environment, you can access an extensive range of pre-installed development tools, such as the AWS CLI. For a complete list of pre-installed tools, see [Pre-installed software](https://docs.aws.amazon.com/cloudshell/latest/userguide/vm-specs.html#pre-installed-software) in the *CloudShell User Guide*.

## Persistent storage
<a name="lightsail-cloudshell-persistent-storage"></a>

With AWS CloudShell, you can use up to 1 GB of persistent storage in each AWS Region at no additional cost. Persistent storage is located in your home directory (`$HOME`) and is private to you. Unlike ephemeral environment resources that are deleted after each shell session ends, data in your home directory persists between sessions.

If you stop using AWS CloudShell in an AWS Region, data is retained in the persistent storage of that Region for **120 days** after the end of your last session. After 120 days, unless you take action, your data is automatically deleted from the persistent storage of that Region. You can prevent removal by launching AWS CloudShell again in that AWS Region. For more information about the retention of data in persistent storage, see [Persistent storage](https://docs.aws.amazon.com/cloudshell/latest/userguide/limits.html#persistent-storage-limitations) in the *CloudShell User Guide*.

## AWS Regions
<a name="lightsail-cloudshell-choose-region"></a>

In Lightsail, a CloudShell session will open in the AWS Region that provides the least latency to your physical location. This means that AWS Regions can change between sessions. Take note of which AWS Region--> your CloudShell session is located in so that you can use the 1 GB persistent storage. To change the session’s AWS Region, choose the **Open in new browser tab** icon. This provides the option to access your CloudShell session in a new browser window.

![CloudShell open in new browser tab](http://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-cloudshell-new-browser-tab.png)


In the navigation bar of the new browser tab, choose the name of the AWS Region that's currently displayed. Then choose the AWS Region that you want to switch to.

![Change the AWS Region in CloudShell.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-cloudshell-region-select.png)


For more information about CloudShell, see the *[CloudShell User Guide](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html)*.

## Launch and use AWS CloudShell
<a name="lightsail-cloudshell-launch-and-use"></a>

Learn how to launch and use an AWS CloudShell session within Lightsail. If you don’t have permission to run CloudShell, you must add the `arn:aws:iam::aws:policy/AWSCloudShellFullAccess` policy to the AWS Identity and Access Management (IAM) identity that you’re using. If you already have the `arn:aws:iam::aws:policy/AdministratorAccess` policy attached, you should be able to access CloudShell. For more information, see [Identity and access management for Amazon Lightsail](security_iam.md).

**Launch AWS CloudShell**

You can launch CloudShell from the Amazon Lightsail console. After the session begins, you can switch to your preferred shell, such as `Bash`, `PowerShell`, or `Z shell`.

Complete the following steps to launch a new AWS CloudShell session in Lightsail:

1. Sign in to the Lightsail console at [https://lightsail.aws.amazon.com/](https://lightsail.aws.amazon.com/).

1. Choose **CloudShell** on the Console Toolbar. When the command prompt displays, the shell is ready for interaction.  
![AWS CloudShell on the Lightsail console toolbar.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-cloudshell-console-toolbar.png)

1. (Optional) To choose a pre-installed shell to work with, enter one of the following program names at the command line prompt:  
**Bash: `bash`**  
If you switch to Bash, the symbol at the command prompt updates to `$`. Bash is the default shell in AWS CloudShell.  
**PowerShell: `pwsh`**  
If you switch to PowerShell, the symbol at the command prompt updates to `PS>`.  
**Z shell: `zsh`**  
If you switch to Z shell, the symbol at the command prompt updates to `%`.

**Example Lightsail API command in AWS CloudShell**  
There are multiple command line tools that are pre-installed on the CloudShell session for you to use. In this example, you use the Lightsail `GetInstances` API operation to view the instances that are in your Lightsail account. To learn more about the `GetInstances` API operation, see [GetInstances](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetInstances.html) in the *Amazon Lightsail API Reference*.  

1. Sign in to the Lightsail console at [https://lightsail.aws.amazon.com/](https://lightsail.aws.amazon.com/).

1. Choose **CloudShell** on the Console Toolbar.

1. Enter the following command after the AWS CloudShell prompt:

   ```
   aws lightsail get-instances
   ```

   You should now see a complete list of instances that are in your Lightsail account.

![Amazon Lightsail get instances API command output.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-cloudshell-getinstances-api.png)


## Additional information
<a name="lightsail-cloudshell-additional-info"></a>

See the following documentation for more information about AWS CloudShell: 
+ [Amazon Lightsail API Reference](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/Welcome.html)
+ [Frequently asked questions in AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/faq-list.html)
+ [Supported browsers in AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/browsers.html)
+ [Troubleshooting in AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/troubleshooting.html)
+ [Working with AWS services in AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/working-with-aws-cli.html)