AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/ "https://aws.amazon.com/transform/"), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# app2container remote extract command

Run this command from a worker machine to generate an application archive for the specified application
on the target application server. The target application server is specified by its IP address or Fully Qualified Domain Name (FQDN). Before you call this command,
you must call the [remote analyze](cmd-remote-analyze.md "cmd-remote-analyze.md") command.

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
app2container remote extract --application-id `id` --target `IP/FQDN` [--help]
```

## Parameters and options

**--application-id `id`**

The application ID _(required)_. After you run the
[remote inventory](cmd-remote-inventory.md "cmd-remote-inventory.md") command, you can find
the application ID in the `inventory.json` file in one of the following locations:

- Linux: `<workspace>/remote/`<target server IP or FQDN>`/inventory.json`
- Windows: `<workspace>\remote\`<target server IP or FQDN>`\.app2container-config\inventory.json`

**--target `IP/FQDN`**

Specifies the IP address or FQDN of the application server
targeted for the inventory _(required)_.

###### Options

**--help**

Displays the command help.

## Output

This command creates an archive file. The archive is written to the output
location that you specified when you ran the **init** command.

## Examples

Choose the operating system platform tab for the application server or worker machine where
you run the command.

Linux
The following example shows the **remote extract** command with
the `--target` and `--application-id` parameters and no additional options.

````
`$` `sudo app2container extract --target `192.0.2.0` --application-id `java-tomcat-9e8e4799```Extraction successful for application java-tomcat-9e8e4799
 Next Steps:
1. Please initiate containerization using "app2container containerize --input-archive <workspace>/remote/`<target server IP or FQDN>`/java-tomcat-9e8e4799/java-tomcat-9e8e4799-extraction.tar"`
````

Windows
The following example shows the **remote extract** command with
the `--target` and `--application-id` parameters and no additional options.

````
`PS>` `app2container extract --target `192.0.2.0` --application-id `iis-smarts-51d2dbf8```Extraction successful for application iis-smarts-51d2dbf8

 Next Steps:
1. Please initiate containerization using "app2container containerize --input-archive <workspace>\remote\`<target server IP or FQDN>`/iis-smarts-51d2dbf8/iis-smarts-51d2dbf8.zip"`
````
