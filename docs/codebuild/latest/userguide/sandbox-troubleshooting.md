

# Troubleshooting AWS CodeBuild sandbox SSH connection issues
<a name="sandbox-troubleshooting"></a>

Use the information in this topic to help you identify, diagnose, and address CodeBuild sandbox SSH connection issues.

**Topics**
+ [`StartSandboxConnection` `InvalidInputException` error when SSH into CodeBuild sandbox environment](#sandbox-troubleshooting.invalid-input)
+ [Error: "Unable to locate credentials" when SSH into CodeBuild sandbox environment](#sandbox-troubleshooting.credentials)
+ [`StartSandboxConnection` `AccessDeniedException` error when SSH into CodeBuild sandbox environment](#sandbox-troubleshooting.access-denied)
+ [Error: "ssh: Could not resolve hostname" when SSH into CodeBuild sandbox environment](#sandbox-troubleshooting.hostname)
+ [Error: "percent\_expand: unknown key %n" when SSH into CodeBuild sandbox environment](#sandbox-troubleshooting.percent-expand)
+ [Error: "ControlPath too long" when SSH into CodeBuild sandbox environment](#sandbox-troubleshooting.controlpath)

## `StartSandboxConnection` `InvalidInputException` error when SSH into CodeBuild sandbox environment
<a name="sandbox-troubleshooting.invalid-input"></a>

**Issue:** When attempting to connect to a CodeBuild sandbox environment using the command `ssh codebuild-sandbox-ssh={{<sandbox-arn>}}`, you may encounter an `InvalidInputException` error such as:

```
An error occurred (InvalidInputException) when calling the StartSandboxConnection 
operation: Failed to start SSM session for {sandbox-arn}
User: arn:aws:sts::{{<account-ID>}}:assumed-role/{{<service-role-name>}}/AWSCodeBuild-{{<UUID>}} 
is not authorized to perform: ssm:StartSession on resource.
```

```
An error occurred (InvalidInputException) when calling the StartSandboxConnection 
operation: Failed to start SSM session for 
sandbox {{<sandbox-arn>}}: codebuild:{{<UUID>}} is not connected.
```

**Possible cause:**
+ Missing Amazon EC2 Systems Manager Agent: The build image does not have the SSM agent properly installed or configured.
+ Insufficient Permissions: The CodeBuild project service role lacks the required SSM permissions.

**Recommended solution:** If you are using a custom image for your build, do the following.

1. Install the SSM Agent. For more information, see [ Manually installing and uninstalling SSM Agent on Amazon EC2 instances for Linux](https://docs.aws.amazon.com/systems-manager/latest/userguide/manually-install-ssm-agent-linux.html) in the **. The SSM Agent version must be `3.0.1295.0` or later.

1. Copy the file, [ https://github.com/aws/aws-codebuild-docker-images/blob/master/ubuntu/standard/7.0/amazon-ssm-agent.json](https://github.com/aws/aws-codebuild-docker-images/blob/master/ubuntu/standard/7.0/amazon-ssm-agent.json) to the `/etc/amazon/ssm/` directory in your image. This enables **Container Mode** in the SSM agent.

1. Ensure your CodeBuild project's service role has the following permissions, then restart the sandbox environment:

   ```
   {
      "Effect": "Allow",
         "Action": [
            "ssmmessages:CreateControlChannel",
            "ssmmessages:CreateDataChannel",
            "ssmmessages:OpenControlChannel",
            "ssmmessages:OpenDataChannel"
         ],
         "Resource": "*"
    },
    {
       "Effect": "Allow",
       "Action": [
          "ssm:StartSession"
        ],
        "Resource": [
           "arn:aws:codebuild:{{region}}:{{account-id}}:build/*",
           "arn:aws:ssm:{{region}}::document/AWS-StartSSHSession"
        ]
    }
   ```

## Error: "Unable to locate credentials" when SSH into CodeBuild sandbox environment
<a name="sandbox-troubleshooting.credentials"></a>

**Issue:** When attempting to connect to a CodeBuild sandbox environment using the command `ssh codebuild-sandbox-ssh={{<sandbox-arn>}}`, you may encounter the following credentials error:

```
Unable to locate credentials. You can configure credentials by running 
"aws configure".
```

**Possible cause:** AWS credentials have not been properly configured in your local environment.

**Recommended solution:** Configure your AWS CLI credentials by following the official documentation: [ Configuring settings for the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) in the *AWS Command Line Interface User Guide for Version 2*.

## `StartSandboxConnection` `AccessDeniedException` error when SSH into CodeBuild sandbox environment
<a name="sandbox-troubleshooting.access-denied"></a>

**Issue:** When attempting to connect to a CodeBuild sandbox environment using the command `ssh codebuild-sandbox-ssh={{<sandbox-arn>}}`, you may encounter the following permission error:

```
An error occurred (AccessDeniedException) when calling the StartSandboxConnection 
operation: 
User: arn:aws:sts::{{account-id}}:assumed-role/{{role-name}}
is not authorized to perform: codebuild:StartSandboxConnection on resource: 
{{sandbox-arn}}
because no identity-based policy allows the codebuild:StartSandboxConnection action
```

**Possible cause:** Your AWS credentials lack the necessary CodeBuild permissions to perform this operation.

**Recommended solution:** Ensure that the IAM user or role associated with your AWS CLI credentials has the following permissions:

```
{
    "Effect": "Allow",
    "Action": [
       "codebuild:StartSandboxConnection"
     ],
     "Resource": [
        "arn:aws:codebuild:{{region}}:{{account-id}}:sandbox/*"
     ]
}
```

## Error: "ssh: Could not resolve hostname" when SSH into CodeBuild sandbox environment
<a name="sandbox-troubleshooting.hostname"></a>

**Issue:** When attempting to connect to a CodeBuild sandbox environment using the command `ssh codebuild-sandbox-ssh={{<sandbox-arn>}}`, you encounter the following hostname resolution error:

```
ssh: Could not resolve hostname
```

**Possible cause:** This error typically occurs when the required CodeBuild sandbox connection script has not been properly executed in your local environment.

**Recommended solution:**

1. Download the CodeBuild sandbox connection script.

1. Execute the script in your terminal to establish the necessary SSH configuration.

1. Retry your SSH connection to the sandbox environment.

## Error: "percent\_expand: unknown key %n" when SSH into CodeBuild sandbox environment
<a name="sandbox-troubleshooting.percent-expand"></a>

**Issue:** When attempting to connect to a CodeBuild sandbox environment using the command `ssh codebuild-sandbox-ssh={{<sandbox-arn>}}`, the command exits immediately, before any connection attempt, with the following error:

```
percent_expand: unknown key %n
```

**Possible cause:** The OpenSSH client on your local machine is older than version 8.1. The SSH configuration that the CodeBuild sandbox connection script adds to `~/.ssh/config` uses the `%n` token in `ProxyCommand`. OpenSSH added support for this token in version 8.1.

**Recommended solution:**

1. Run `ssh -V` to check the installed OpenSSH client version.

1. Upgrade the OpenSSH client to version 8.1 or later. On Amazon Linux 2, use an Amazon Linux 2023 host or install a newer OpenSSH client. If the setup script stopped with an OpenSSH version error, run the setup script again after the upgrade. A run that stopped at the version check did not change your configuration. If the setup script completed earlier, you do not need to run it again.

1. Retry your SSH connection to the sandbox environment.

## Error: "ControlPath too long" when SSH into CodeBuild sandbox environment
<a name="sandbox-troubleshooting.controlpath"></a>

**Issue:** When attempting to connect to a CodeBuild sandbox environment using the command `ssh codebuild-sandbox-ssh={{<sandbox-arn>}}`, the command prints the following error and exits, where {{<limit>}} is 104 on macOS and 108 on Linux:

```
ControlPath too long ('{{<path>}}' >= {{<limit>}} bytes)
```

**Possible cause:** Your `~/.ssh/config` sets a `ControlPath` for all hosts that includes the hostname token `%h`. The hostname of a CodeBuild sandbox is the full sandbox ARN, so the resulting socket path exceeds the operating system limit for Unix socket paths (104 bytes on macOS, 108 bytes on Linux).

**Recommended solution:** The current CodeBuild sandbox SSH setup script adds a `ControlPath` that does not include the hostname to the `Host codebuild-sandbox-ssh*` entry. The script also places that entry before the other `Host` entries, because OpenSSH uses the first value it finds for each option. When you run the script again, it updates the existing entry and prompts you before it changes `~/.ssh/config`.

1. Download and run the CodeBuild sandbox SSH setup script again, as described in [Step 2: Modify local SSH configuration](sandbox-ssh-tutorial.md#sandbox-ssh-tutorial.modify-ssh). Accept the change when prompted.

1. Retry your SSH connection to the sandbox environment.

If you cannot run the setup script again, edit `~/.ssh/config` manually.

1. Open `~/.ssh/config` in a text editor.

1. Add a `ControlPath` line to the existing `Host codebuild-sandbox-ssh*` entry, as shown in the following example.

   ```
   Host codebuild-sandbox-ssh*
       ControlPath ~/.ssh/codebuild-sandbox-%C
   ```

   `%C` is an OpenSSH token that expands to a short hash of the connection parameters.

1. Move the `Host codebuild-sandbox-ssh*` entry so that it comes before any `Host *` entry.

To connect once without changing `~/.ssh/config`, pass the option on the command line:

```
ssh -o ControlPath=~/.ssh/codebuild-sandbox-%C codebuild-sandbox-ssh={{<sandbox-arn>}}
```