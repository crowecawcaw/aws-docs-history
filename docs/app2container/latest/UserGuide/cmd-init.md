AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/ "https://aws.amazon.com/transform/"), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# app2container init command

The **init** command performs one-time initialization tasks for App2Container. This interactive command prompts
for the information required to set up the local App2Container environment. Run this command before you run any other
App2Container commands.

###### Note

If the command fails, an error message is displayed in the console, followed by
additional messaging to help you troubleshoot.

When you ran the **init** command, if you chose to automatically
upload logs to App2Container support if an error occurs, App2Container notifies you of the
success of the automatic upload of your application support bundle.

Otherwise, App2Container messaging directs you to upload application artifacts by
running the [upload-support-bundle](cmd-upload-support-bundle.md "cmd-upload-support-bundle.md") command for additional support.

## Syntax

```
app2container init [--advanced] [--help]
```

## Parameters and options

###### Options

**--advanced**

This option allows you to use features that are in the experimental phase, if any exist.

**--help**

Displays the command help.

## Output

The **init** command prompts you for the information that it needs
for initialization.

You must provide a local directory for application containerization artifacts.
Ensure that only authorized users can access the local directory. If you do not
specify a local directory, one is created for you at the default output location.
The default locations are as follows:

- Linux: `/root/app2container`
- Windows: `C:\Users\Administrator\AppData\Local\app2container`

You can optionally provide an Amazon S3 bucket for application containerization artifacts.
If you choose to set up an Amazon S3 bucket, you must ensure that only authorized users can
access the bucket. We recommend that you use server-side encryption for your bucket. See
[Protecting data using server-side
encryption](../../../AmazonS3/latest/userguide/serv-side-encryption.md "../../../AmazonS3/latest/userguide/serv-side-encryption.md") in the _Amazon Simple Storage Service User Guide_ for more information
about how to set it up.

You can optionally upload logs and command-generated artifacts automatically to
App2Container support when an app2container command crashes or encounters internal errors. Log
files are retained for 90 days.

You can optionally consent to allow App2Container to collect and export the following metrics to AWS
each time that you run an **app2container** command:

- Host OS name
- Host OS version
- Application stack type
- Application stack version
- JRE version (Linux only, for Java applications)
- App2Container CLI version
- Command that ran
- Command status
- Command duration
- Command features and flags
- Command errors
- Container base image

## Examples

Choose the operating system platform tab for the application server or worker machine where
you run the command.

Linux
The following example shows the **init** command with no additional options.

```
`$` `sudo app2container init``Please enter a workspace directory path to use for artifacts[default: /root/app2container]:
Please enter an AWS Profile to use. (The same can be configured with 'aws configure --profile <name>')[default: default]:
Please provide an S3 bucket to store application artifacts (Optional):
Automatically upload logs and App2Container generated artifacts on crashes and internal errors? (Y/N):
Please confirm permission to report usage metrics to AWS (Y/N)[default: y]:
Would you like to enforce the use of only signed images using Docker Content Trust (DCT)? (Y/N)[default: n]:
All application artifacts will be created under the above workspace. Please ensure that the folder permissions are secure.
Init configuration saved`
```

The following example shows the **init** command with the `--advanced`
option and default values.

```
`PS>` `sudo app2container init --advanced``Please enter a workspace directory path to use for artifacts[default: /root/app2container]:
Please enter an AWS Profile to use. (The same can be configured with 'aws configure --profile <name>')[default: default]:
Please provide an S3 bucket to store application artifacts (Optional):
Automatically upload logs and App2Container generated artifacts on crashes and internal errors? (Y/N):
Please confirm permission to report usage metrics to AWS (Y/N)[default: y]:
Would you like to enforce the use of only signed images using Docker Content Trust (DCT)? (Y/N)[default: n]:
Would you like to enable experimental features? (Y/N)[default: n]:
All application artifacts will be created under the above workspace. Please ensure that the folder permissions are secure.
Init configuration saved`
```

Windows
The following example shows the **init** command with no additional options.

```
`PS>` `app2container init``Please enter a workspace directory path to use for artifacts[default: C:\Users\Administrator\AppData\Local\app2container]:
Please enter an AWS Profile to use. (The same can be configured with 'aws configure --profile <name>')[default: default]:
Please provide an S3 bucket to store application artifacts (Optional):
Automatically upload logs and App2Container generated artifacts on crashes and internal errors? (Y/N):
Please confirm permission to report usage metrics to AWS (Y/N)[default: y]:
Would you like to enforce the use of only signed images using Docker Content Trust (DCT)? (Y/N)[default: n]:
All application artifacts will be created under the above workspace. Please ensure that the folder permissions are secure.
Init configuration saved`
```

The following example shows the **init** command with the `--advanced`
option and default values.

```
`PS>` `app2container init --advanced``Please enter a workspace directory path to use for artifacts[default: C:\Users\Administrator\AppData\Local\app2container]:
Please enter an AWS Profile to use. (The same can be configured with 'aws configure --profile <name>')[default: default]:
Please provide an S3 bucket to store application artifacts (Optional):
Automatically upload logs and App2Container generated artifacts on crashes and internal errors? (Y/N):
Please confirm permission to report usage metrics to AWS (Y/N)[default: y]:
Would you like to enforce the use of only signed images using Docker Content Trust (DCT)? (Y/N)[default: n]:
Please enter if we can enable checking for upgrades automatically (Y/N)[default: y]:
Would you like to enable experimental features? (Y/N)[default: n]:
All application artifacts will be created under the above workspace. Please ensure that the folder permissions are secure.
Init configuration saved`
```
