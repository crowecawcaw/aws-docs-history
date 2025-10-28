AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/ "https://aws.amazon.com/transform/"), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# app2container upload-support-bundle command

For assistance with troubleshooting, run this command to securely upload
App2Container logs and supporting artifacts to the AWS App2Container support team.
The following list shows the types of files that you can upload with the
**upload-support-bundle** command:

- App2Container logs
- The `analysis.json` file
- The `Dockerfile`
- The `deployment.json` file
- The `EcsDeployment.yml` or `ecs-master.yml` deployment artifacts

## Syntax

```
app2container upload-support-bundle [--application-id `id`] [--support-message "`message`"] [--help]
```

## Options

**--application-id `id`**

The application ID _(required)_. After you run the [inventory](cmd-inventory.md "cmd-inventory.md") command, you can find the application ID in the `inventory.json`
file in one of the following locations:

- Linux: `/root/inventory.json`
- Windows: `C:\Users\Administrator\AppData\Local\.app2container-config\inventory.json`

**--support-message**

Include a message for the App2Container support team with your bundle.

**--help**

Displays the command help.

## Output

Console output is included in the Examples section for this command.

## Examples

Choose the operating system platform tab for the application server or worker machine where
you run the command.

Linux
Run the following command to upload a support bundle from a Linux operating system,
including the application ID and a message for the support team.

```
`$` `sudo app2container upload-support-bundle --application-id `java-tomcat-9e8e4799` --support-message "I ran into an issue during deployment ..."`
`Support Message: I ran into an issue during deployment ...
[displays while bundle is uploading] Uploading logs and supporting artifacts to App2Container support
Support bundle upload successful`
```

Windows
Run the following command to upload a support bundle from a Windows operating system,
including the application ID and a message for the support team.

```
`PS>` `app2container upload-support-bundle --application-id `iis-smarts-51d2dbf8` --support-message "I ran into an issue during deployment ..."`
`Support Message: I ran into an issue during deployment ...
[displays while bundle is uploading] Uploading logs and supporting artifacts to App2Container support
Support bundle upload successful`
```
