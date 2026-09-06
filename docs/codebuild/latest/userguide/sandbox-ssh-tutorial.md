

# Tutorial: Connecting to a sandbox using SSH
<a name="sandbox-ssh-tutorial"></a>

This tutorial shows you how to connect to a CodeBuild sandbox using an SSH client.

To complete this tutorial, you must first:
+ Ensure you have an existing AWS CodeBuild project.
+ Set up appropriate IAM permissions configured for your CodeBuild project role. 
+ Install and configure AWS CLI on your local machine.

## Step 1: Start a sandbox
<a name="sandbox-ssh-tutorial.start-sandbox"></a>

**To start a CodeBuild sandbox in the console**

1. Open the AWS CodeBuild console at [https://console.aws.amazon.com/codesuite/codebuild/home](https://console.aws.amazon.com/codesuite/codebuild/home).

1. In the navigation pane, choose **Build projects**. Choose the build project, and then choose **Debug build**.  
![The build project detail page in the console.](http://docs.aws.amazon.com/codebuild/latest/userguide/images/project-debug-build.png)

1. In the **SSH Client** tab and choose **Start sandbox**.  
![The "SSH Client" tab in the console with "Start sandbox" button.](http://docs.aws.amazon.com/codebuild/latest/userguide/images/ssh-client-sandbox.png)

1. The sandbox initialization process may take some time. You can connect to the sandbox when its status changes to `RUN_SANDDBOX`.  
![The SSH sandbox connection after the status changes to "RUN_SANDDBOX".](http://docs.aws.amazon.com/codebuild/latest/userguide/images/run-sandbox.png)

## Step 2: Modify local SSH configuration
<a name="sandbox-ssh-tutorial.modify-ssh"></a>

If you're connecting to sandbox for the first time, you need to perform a one-time setup process using the following steps:

**To modify the local SSH configuration in the console**

1. Locate the setup commands for your operating system.

1. Open your local terminal, then copy and execute the provided commands to download and run the script to set up your local SSH configuration. For example, if your operating system is macOS, use the following command:  
![The macOS commands for SSH connection to the CodeBuild sandbox in the console.](http://docs.aws.amazon.com/codebuild/latest/userguide/images/modify-ssh-macOS.png)

1. The configuration script will add the required configurations for connecting to your sandboxes. You'll be prompted to accept these changes.

1. Upon successful configuration, a new SSH configuration entry for CodeBuild sandbox will be created.  
![A successful SSH sandbox connection.](http://docs.aws.amazon.com/codebuild/latest/userguide/images/ssh-terminal-success.png)

## Step 3: Connect to the sandbox
<a name="sandbox-ssh-tutorial.connect-sandbox"></a>

**To modify the local SSH configuration in the console**

1. Configure AWS CLI Authentication and ensure your AWS CLI user has the `codebuild:StartSandboxConnection` permission. For more information, see [ Authenticating using IAM user credentials for the AWS CLI](https://docs.aws.amazon.com/cli/v1/userguide/cli-authentication-user.html) in the *AWS Command Line Interface User Guide for Version 1*.

1. Connect to your sandbox with following command:

   ```
   ssh codebuild-sandbox-ssh=arn:aws:codebuild:us-east-1:{{<account-id>}}:sandbox/{{<sandbox-id>}}
   ```
**Note**  
To troubleshoot connection failures, use the `-v` flag to enable verbose output. For example, `ssh -v codebuild-sandbox-ssh=arn:aws:codebuild:us-east-1:{{<account-id>}}:sandbox/{{<sandbox-id>}}`.  
For additional troubleshooting guidance, see [Troubleshooting AWS CodeBuild sandbox SSH connection issues](sandbox-troubleshooting.md).

## Step 4: Review your results
<a name="sandbox-ssh-tutorial.review-results"></a>

Once connected, you can debug build failures, test build commands, experiment with configuration changes and verify environment variables and dependencies with your sandbox.