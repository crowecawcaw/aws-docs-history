AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/ "https://aws.amazon.com/transform/"), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# app2container remote analyze command

Run this command from a worker machine to analyze the specified application on the target
application server, and generate a report. The target application server is specified by its IP address or Fully Qualified Domain Name (FQDN).

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
app2container remote analyze --application-id `id` --target `IP/FQDN` [--help]
```

## Parameters and options

###### Parameters

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

The **remote analyze** command creates files and directories on the
worker machine for the specified application on the target application server. Each
application has its own directory, named for the application ID. Output varies
slightly, depending on your application language and the application server operating system.

The application directory contains analysis output and editable
application configuration files. The files are stored in subdirectories that match the
application structure on the application server.

An `analysis.json` file is created for the application that is
specified in the `--application-id` parameter. The file contains information
about the application found during analysis, and configurable fields for container
settings. See [Configuring application containers](config-containers.md "config-containers.md"),
and choose the platform that your application container runs on for more information
about configurable fields, and for an example of what the file looks like.

For .NET applications and Windows services, App2Container detects connection strings and
produces the `report.txt` file. The report location is specified in
the `analysis.json` file, in the `reportPath` attribute of
the `analysisInfo` section. You can use this report to identify the changes
that you need to make in application configuration files to connect your application
container to new database endpoints, if needed. The report also contains the locations
of other configuration files that might need changes.

## Examples

Choose the operating system platform tab for the application server or worker machine where
you run the command.

Linux
The following example shows the **remote analyze** command with the
`--target` and `--application-id` parameters and no additional options.

````
`$` `sudo app2container remote analyze --target `192.0.2.0` --application-id `java-tomcat-9e8e4799```Analysis successful for application java-tomcat-9e8e4799

 Next Steps:
1. View the application analysis file at <workspace>/remote/`<target server IP or FQDN>`/java-tomcat-9e8e4799/analysis.json.
2. Edit the application analysis file as needed.
3. Start the extraction process using the following command: app2container remote extract --target `192.0.2.0` java-tomcat-9e8e4799`
````

Windows
The following example shows the **remote analyze** command with the
`--target` and `--application-id` parameters and no additional options.

````
`PS>` `app2container remote analyze --target `192.0.2.0` --application-id `iis-smarts-51d2dbf8```Analysis successful for application iis-smarts-51d2dbf8;

 Next Steps:
1. View the application analysis file at <workspace>\remote\`<target server IP or FQDN>`/iis-smarts-51d2dbf8/analysis.json.
2. Edit the application analysis file as needed.
3. Start the extraction process using the following command: app2container remote extract --target `192.0.2.0` iis-smarts-51d2dbf8`
````
