AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/ "https://aws.amazon.com/transform/"), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# app2container inventory command

Records all Java or .Net processes (Linux) or all IIS websites and Windows services
(Windows) that are running on the application server.

## Syntax

```
app2container inventory --type [`iis` | `service` | `java` | `dotnet`] [--nofilter] [--help]
```

## Parameters and options

###### Parameters

**--type [`iis` | `service` |
`java` | `dotnet`]**

Use this parameter to specify the application type _(required)_,
as follows.

- For .NET applications running on Windows, you can specify an IIS web application
  (`iis`), or a Windows service (`service`).
- For Java applications running on Linux, you must specify `java`.
- For .NET applications running on Linux, you must specify `dotnet`.

###### Options

**--nofilter**

For applications running on Windows, this option prevents
App2Container from filtering out default system services when building
the inventory output. This can be used for complex Windows .NET
applications that have dependent web apps that need to be
included in the container.

**--help**

Displays the command help.

## Output

Information about the Java processes, .NET applications, or IIS websites is saved to the
`inventory.json` file in one of the following locations:

- Linux: `/root/inventory.json`
- Windows: `C:\Users\Administrator\AppData\Local\.app2container-config\inventory.json`

The application ID that is used by other App2Container commands is the key for each application object in the
JSON file. The application objects are slightly different depending on your application language and the
application server operating system. Choose the operating system platform for your application in
the Examples section to see the differences.

## Examples

Expand the section that matches the operating system platform for the application server
or worker machine where you run the command.

Each Java process or ASP.NET application running on Linux has a unique application
ID (for example, java-tomcat-9e8e4799, or dotnet-single-c2930d3132).
You can use this application ID with other AWS App2Container commands. Inventory information
is saved to `/root/inventory.json`.

Java
The following example shows the **inventory** command with results for Java processes running on Linux, with no additional options.

```
`$` `sudo app2container inventory``{
 "java-jboss-5bbe0bec": {
 "processId": 27366,
 "cmdline": "java ...",
 "applicationType": "java-jboss"
 },
 "java-tomcat-9e8e4799": {
 "processId": 2537,
 "cmdline": "/usr/bin/java ...",
 "applicationType": "java-tomcat"
 }
}`
```

ASP.NET
The following example shows the **inventory** command with results for .NET applications running on Linux, with no additional options.

```
`$` `sudo app2container inventory``{
 "dotnet-single-c2930d3132": {
 processId": 1,
 "cmdline": "./MyCoreWebApp.3.1 ...",
 "applicationType": "dotnet-single",
 "webApp": ""
 },
 "dotnet-generic-a27b2829": {
 processId": 2,
 "cmdline": "./MyCoreWebApp.3.1 ...",
 "applicationType": "dotnet-generic",
 "webApp": ""
 }
}`
```

Each IIS website has a unique application ID (for example, iis-smarts-51d2dbf8).
You can use this application ID with other AWS App2Container commands. Inventory information
is saved to `C:\Users\Administrator\AppData\Local\.app2container-config\inventory.json`.

The following example shows the **inventory** command with results for .NET applications running in IIS on Windows, with no additional options.

```
`PS>` `app2container inventory``{
 "iis-smarts-51d2dbf8": {
 "siteName": "Default Web Site",
 "bindings": "http/*:80:,net.tcp/808:*",
 "applicationType": "iis",
 "discoveredWebApps": []
 },
 "iis-smart-544e2d61": {
 "siteName": "smart",
 "bindings": "http/*:82:",
 "applicationType": "iis",
 "discoveredWebApps": []
 },
 "service-colorwindowsservice-69f90194": {
 "serviceName": "colorwindowsservice",
 "applicationType": "service"
 }
}`
```
