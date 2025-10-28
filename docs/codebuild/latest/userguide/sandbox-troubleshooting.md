# Troubleshooting AWS CodeBuild sandbox SSH connection issues

Use the information in this topic to help you identify, diagnose, and address
CodeBuild sandbox SSH connection issues.

###### Topics

- [StartSandboxConnectionInvalidInputException error when SSH into CodeBuild sandbox environment](#sandbox-troubleshooting.invalid-input "#sandbox-troubleshooting.invalid-input")
- [Error: "Unable to locate credentials"
  when SSH into CodeBuild sandbox environment](#sandbox-troubleshooting.credentials "#sandbox-troubleshooting.credentials")
- [StartSandboxConnectionAccessDeniedException
  error when SSH into CodeBuild sandbox environment](#sandbox-troubleshooting.access-denied "#sandbox-troubleshooting.access-denied")
- [Error: "ssh: Could not resolve hostname"
  when SSH into CodeBuild sandbox environment](#sandbox-troubleshooting.hostname "#sandbox-troubleshooting.hostname")

## `StartSandboxConnection``InvalidInputException` error when SSH into CodeBuild sandbox environment

**Issue:** When attempting to connect to a CodeBuild sandbox
environment using the command `ssh codebuild-sandbox-ssh=`<sandbox-arn>``, 
 you may encounter an `InvalidInputException` error such as:

```
An error occurred (InvalidInputException) when calling the StartSandboxConnection
operation: Failed to start SSM session for {sandbox-arn}
User: arn:aws:sts::`<account-ID>`:assumed-role/`<service-role-name>`/AWSCodeBuild-`<UUID>`
is not authorized to perform: ssm:StartSession on resource.
```

```
An error occurred (InvalidInputException) when calling the StartSandboxConnection
operation: Failed to start SSM session for
sandbox `<sandbox-arn>`: codebuild:`<UUID>` is not connected.
```

**Possible cause:**

- Missing Amazon EC2 Systems Manager Agent: The build image does not have the SSM agent properly installed or configured.
- Insufficient Permissions: The CodeBuild project service role lacks the required SSM permissions.

**Recommended solution:** If you are using a custom image for your build, do the following.

1. Install the SSM Agent. For more information, see
   [Manually installing and uninstalling SSM Agent on Amazon EC2 instances for Linux](../../../systems-manager/latest/userguide/manually-install-ssm-agent-linux.md "../../../systems-manager/latest/userguide/manually-install-ssm-agent-linux.md") in the .
   The SSM Agent version must be `3.0.1295.0` or later.
2. Copy the file, [https://github.com/aws/aws-codebuild-docker-images/blob/master/ubuntu/standard/7.0/amazon-ssm-agent.json](https://github.com/aws/aws-codebuild-docker-images/blob/master/ubuntu/standard/7.0/amazon-ssm-agent.json "https://github.com/aws/aws-codebuild-docker-images/blob/master/ubuntu/standard/7.0/amazon-ssm-agent.json")
   to the `/etc/amazon/ssm/` directory in your image. This enables **Container Mode** in the SSM agent.
3. Ensure your CodeBuild project's service role has the following permissions, then restart the sandbox environment:

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
        "arn:aws:codebuild:`region`:`account-id`:build/*",
        "arn:aws:ssm:`region`::document/AWS-StartSSHSession"
     ]
 }
```

## Error: "Unable to locate credentials"

when SSH into CodeBuild sandbox environment

**Issue:** When attempting to connect to a CodeBuild sandbox
environment using the command `ssh codebuild-sandbox-ssh=`<sandbox-arn>``,
you may encounter the following credentials error:

```
Unable to locate credentials. You can configure credentials by running
"aws configure".
```

**Possible cause:** AWS credentials have not been properly configured in your local environment.

**Recommended solution:** Configure your AWS CLI credentials by following the official documentation:
[Configuring settings for the AWS CLI](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md") in the _AWS Command Line Interface User Guide for Version 2_.

## `StartSandboxConnection``AccessDeniedException`

error when SSH into CodeBuild sandbox environment

**Issue:** When attempting to connect to a CodeBuild sandbox
environment using the command `ssh codebuild-sandbox-ssh=`<sandbox-arn>``,
you may encounter the following permission error:

```
An error occurred (AccessDeniedException) when calling the StartSandboxConnection
operation:
User: arn:aws:sts::`account-id`:assumed-role/`role-name`
is not authorized to perform: codebuild:StartSandboxConnection on resource:
`sandbox-arn`
because no identity-based policy allows the codebuild:StartSandboxConnection action
```

**Possible cause:** Your AWS credentials lack the necessary CodeBuild permissions
to perform this operation.

**Recommended solution:** Ensure that the IAM user or role associated
with your AWS CLI credentials has the following permissions:

```
{
    "Effect": "Allow",
    "Action": [
       "codebuild:StartSandboxConnection"
     ],
     "Resource": [
        "arn:aws:codebuild:`region`:`account-id`:sandbox/*"
     ]
}
```

## Error: "ssh: Could not resolve hostname"

when SSH into CodeBuild sandbox environment

**Issue:** When attempting to connect to a CodeBuild sandbox
environment using the command `ssh codebuild-sandbox-ssh=`<sandbox-arn>``,
you encounter the following hostname resolution error:

```
ssh: Could not resolve hostname
```

**Possible cause:** This error typically occurs when the required CodeBuild
sandbox connection script has not been properly executed in your local environment.

**Recommended solution:**

1. Download the CodeBuild sandbox connection script.
2. Execute the script in your terminal to establish the necessary SSH configuration.
3. Retry your SSH connection to the sandbox environment.
