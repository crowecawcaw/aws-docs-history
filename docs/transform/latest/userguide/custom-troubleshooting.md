

# Troubleshooting
<a name="custom-troubleshooting"></a>

This section provides guidance for troubleshooting common issues with AWS Transform custom.

## Log Locations
<a name="custom-log-locations"></a>

AWS Transform CLI maintains logs in the following locations:

**Conversation logs:**

------
#### [ Linux and macOS ]

```
~/.aws/atx/custom/<conversation_id>/logs/<timestamp>-conversation.log
```

------
#### [ Windows ]

```
%USERPROFILE%\.aws\atx\custom\<conversation_id>\logs\<timestamp>-conversation.log
```

------

These logs contain the full conversation history for debugging specific transformation executions.

**Subagent logs:**

------
#### [ Linux and macOS ]

```
~/.aws/atx/custom/<conversation_id>/logs/subagents/<name>.log
```

------
#### [ Windows ]

```
%USERPROFILE%\.aws\atx\custom\<conversation_id>\logs\subagents\<name>.log
```

------

These logs contain output from subagents that the main agent spawns during transformations. You do not need to manage subagents directly.

**Developer debug logs:**

------
#### [ Linux and macOS ]

```
~/.aws/atx/logs/debug*.log
~/.aws/atx/logs/error.log
```

------
#### [ Windows ]

```
%USERPROFILE%\.aws\atx\logs\debug*.log
%USERPROFILE%\.aws\atx\logs\error.log
```

------

These logs provide detailed information about CLI operations and errors. Each log file has a 5MB limit before it rolls over. There may be multiple debug logs in this directory, such as debug1.log and debug2.log.

## Common Issues
<a name="custom-common-issues"></a>

**Installation issues:**

If installation fails, ensure you have Node.js 22 or later installed:

```
node --version
```

Download Node.js from https://nodejs.org/en/download if needed.

**Authentication issues:**

Verify your AWS credentials are configured correctly:

```
aws sts get-caller-identity
```

Ensure your IAM user or role has the required `transform-custom:*` permissions.

**Network connectivity issues:**

If you encounter connection errors, verify network access to required endpoints:
+ `transform-cli.awsstatic.com`
+ `transform-custom.<region>.api.aws`
+ `*.s3.amazonaws.com`

If working in an internet-restricted environment, update firewall rules to allowlist these URLs.

**Region configuration issues:**

If you encounter region-related errors:
+ Verify your region is supported
+ Check for environment variables that may override your configuration: `echo $AWS_REGION $AWS_DEFAULT_REGION`
+ Check your region configuration: `aws configure get region`
+ Update your region if needed: `aws configure set region <your-region>`
+ Check debug logs for region resolution details

**Git issues:**

Ensure Git is installed and your repository is under git source control:

```
git --version
git status
```

AWS Transform custom requires repositories to be under git source control.

**Transformation execution issues:**

If a transformation fails:

1. Review the conversation logs at `~/.aws/atx/custom/<conversation_id>/logs/`

1. Check for build or test failures in the transformation output

1. Verify the build command is correct for your project

1. Try running the transformation in interactive mode to provide feedback

**Conversation resumption issues:**

If you cannot resume a conversation:
+ Verify the conversation is less than 30 days old
+ Check the conversation ID is correct
+ Ensure you have network connectivity

## Continuing a transformation campaign using the CLI
<a name="custom-continue-campaign-cli"></a>

If you started a transformation in the AWS Transform web application, AWS Transform created a campaign for it. You can continue to run and track that campaign using the AWS Transform command line interface (CLI). Use the following procedure when you want to transform more repositories in an existing campaign, or check the progress of its repositories, without using the web application. For AWS managed transformations (transformation names that start with `AWS/`) in non-interactive mode, you need to provide `additionalPlanContext` in the `--configuration` option to specify the target of the transformation, such as the target language version.

Before you begin, your AWS credentials need to be for the same AWS account where you created the campaign, and you need to set the same AWS Region. In the following example, replace {{aa-example-1}} with the Region where you created the campaign.

```
export AWS_REGION={{aa-example-1}}
```

**To continue a campaign using the CLI**

1. Run the following command to list the campaigns in your account, and then find the campaign that you want to continue. The campaign name is the job ID of the transformation that you started in the web application.

   ```
   atx custom campaign list
   ```

   To also view the description of each campaign, add `--json` to the command.

1. (Optional) Run the following commands to view the campaign details and the repositories that are already in the campaign. Replace {{campaign-name}} with the name of your campaign.

   ```
   atx custom campaign get --name {{campaign-name}}
   atx custom campaign list-repos --name {{campaign-name}}
   ```

1. Run the following command to transform a repository and record the result in the campaign.

   ```
   atx custom def exec \
       --code-repository-path {{path-to-repo}} \
       --non-interactive \
       --trust-all-tools \
       --campaign {{campaign-name}} \
       --repo-name {{repo-name}} \
       --add-repo \
       --configuration "additionalPlanContext={{target-details}}"
   ```

   Replace the following values:
   + {{path-to-repo}} – The local path to the code repository that you want to transform.
   + {{campaign-name}} – The name of the campaign that you want to continue.
   + {{repo-name}} – The name of the repository in the campaign. The `--add-repo` option adds the repository to the campaign if it isn't already in the campaign.
   + {{target-details}} – The target of the transformation, for example `The target Java version to upgrade to is Java 21`.

   To run the transformation interactively instead, omit `--non-interactive` and `--trust-all-tools`. If the command returns an error, review the error message, verify the `--configuration` value and the repository path, and then run the command again. For common errors, see the troubleshooting list that follows this procedure.

1. Run the following command to track the progress of the repositories in the campaign. A repository shows `TRANSFORMING` while the transformation runs and `VALIDATED` after it completes.

   ```
   atx custom campaign list-repos --name {{campaign-name}}
   ```

When the transformation completes successfully, the repository shows `VALIDATED` in the campaign.

You can also manage campaigns using the following commands:
+ To add repositories to a campaign without running a transformation, run `atx custom campaign add-repos --name {{campaign-name}} --repos {{repo-a,repo-b}}`.
+ To create a new campaign, run `atx custom campaign create --name {{campaign-name}} --transformation-name {{transformation-name}} --description "{{description}}"`.
+ To close a campaign when you finish, run `atx custom campaign update-status --name {{campaign-name}} --status CLOSED`.

If you encounter the following errors while you work with campaigns, use these solutions:
+ **Campaign '{{campaign-name}}' not found.** – This error usually occurs when the CLI uses credentials or a Region that differ from the ones that you used to create the campaign. Campaigns are stored per AWS account and Region. Verify that your credentials and the `AWS_REGION` value match the account and Region where you created the campaign.
+ **Could not resolve the AWS Transform endpoint** – This error occurs when the value of `AWS_REGION` is a Region that AWS Transform custom doesn't support. Set `AWS_REGION` to the Region where you created the campaign.
+ **Running this transformation in non-interactive mode requires the --configuration (or -g) input provided with the "additionalPlanContext" section populated.** – This error occurs when you run an AWS managed transformation in non-interactive mode without a target. Add `--configuration "additionalPlanContext={{target-details}}"` to the command, or run the command without `--non-interactive`.
+ **No repositories found for this campaign.** – This message appears when the transformation command stopped before it added the repository to the campaign. Review the error message that the transformation command returned, fix the issue, and then run the command again with `--add-repo`.

## Getting Support
<a name="custom-getting-support"></a>

For additional assistance, visit AWS Support through the [AWS Console](https://support.console.aws.amazon.com/support/home#/).

When opening a support ticket, include:
+ Conversation logs from `~/.aws/atx/custom/<conversation_id>/logs/`
+ Subagent logs from `~/.aws/atx/custom/<conversation_id>/logs/subagents/`
+ Debug logs from `~/.aws/atx/logs/`
+ Steps to reproduce the issue
+ AWS Transform CLI version (`atx --version`)

## S3 access issues
<a name="custom-s3-access-issues"></a>

The AWS Transform custom service vends S3 pre-signed URLs to facilitate uploading and downloading the potentially large transformation files to/from client machines. This means that not only does the CLI interact with the AWS Transform service endpoints but it also interacts with the S3 service endpoints. These interactions use pre-signed URLs so your client's IAM credentials **do not** require any S3 permissions but sometimes your local machine's proxy server configurations and your network's S3 VPC Endpoint Policies can restrict this traffic.

Please examine the [Log Locations](#custom-log-locations) for more detailed error messages to help root cause any tool failures or S3 access denied relating to downloading and uploading transformation files.

If you are using a VPN/Proxy server that leverages the `https_proxy` and `no_proxy` environment variables, consider adding the following values to your `no_proxy` environment variable value to bypass the proxy for the S3 and AWS Transform custom service endpoints, for example:

------
#### [ Linux and macOS ]

```
export no_proxy=.s3.amazonaws.com,transform-custom.<region>.api.aws
```

------
#### [ Windows (PowerShell) ]

```
$env:no_proxy=".s3.amazonaws.com,transform-custom.<region>.api.aws"
```

------

If you are using an [AWS PrivateLink for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/privatelink-interface-endpoints.html) in your VPC, this may have a policy defined to restrict S3 traffic. Please ensure your S3 VPC endpoint policy allows `GetObject` and `PutObject` operations for the AWS Transform custom service-owned buckets. This can be accomplished by adding the following statement to your VPC endpoint policy:

```
{
    "Effect": "Allow",
    "Principal": "*",
    "Action": ["s3:PutObject","s3:GetObject"],
    "Resource": "arn:aws:s3:::aws-transform-custom-*/*"
}
```

Explicit `Deny` statements in policies take precedence over `Allow` statements. Review S3 VPC Endpoint policies for `Deny` statements that may be restricting access.