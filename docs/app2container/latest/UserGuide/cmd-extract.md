AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/ "https://aws.amazon.com/transform/"), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# app2container extract command

Generates an application archive for the specified application. Before you call this command,
you must call the [analyze](cmd-analyze.md "cmd-analyze.md") command.

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
app2container extract --application-id `id` [--output s3] [--help]
```

## Parameters and options

###### Parameters

**--application-id `id`**

The application ID _(required)_. After you run the [inventory](cmd-inventory.md "cmd-inventory.md") command, you can find the application ID in the `inventory.json`
file in one of the following locations:

- Linux: `/root/inventory.json`
- Windows: `C:\Users\Administrator\AppData\Local\.app2container-config\inventory.json`

**--profile `admin-profile`**

Use this option to specify a _named profile_ to run this
command. For more information about named profiles in AWS, see
[Named profiles](../../../cli/latest/userguide/cli-configure-files.md "../../../cli/latest/userguide/cli-configure-files.md")
in the AWS Command Line Interface User Guide

###### Options

**--output s3**

If specified, this option writes the archive file to the Amazon S3 bucket that
you specified when you ran the **init** command.

**--force**

Bypasses the disk space prerequisite check.

**--help**

Displays the command help.

## Output

This command creates an archive file. When you use the `--output s3`
option, the archive is written to the Amazon S3 bucket that you specified when you ran the
**init** command. Otherwise, the archive is written to the output
location that you specified when you ran the **init** command.

## Examples

Choose the operating system platform tab for the application server or worker machine where
you run the command.

Linux
The following example shows the **extract** command with the `--application-id`
parameter and no additional options.

````
`$` `sudo app2container extract --application-id `java-tomcat-9e8e4799```√ Extracted container artifacts for application
√ Application archive file created at: /root/app2container/java-tomcat-9e8e4799/java-tomcat-9e8e4799-extraction.tar
Extraction successful for application java-tomcat-9e8e4799

Please transfer this tar file to your worker machine and run, "app2container containerize --input-archive <extraction-tar-filepath>"`
````

Windows
The following example shows the **extract** command with the `--application-id`
parameter and no additional options.

````
`PS>` `app2container extract --application-id `iis-smarts-51d2dbf8```√ Extracted container artifacts for application
Extraction successful for application iis-smarts-51d2dbf8`
````
