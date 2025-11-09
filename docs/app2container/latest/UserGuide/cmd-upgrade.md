AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/ "https://aws.amazon.com/transform/"), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# app2container upgrade command

Run this command to upgrade your existing installation of App2Container.

If a newer version of AWS App2Container will break backwards compatibility with previously
generated container artifacts when you do an upgrade, the upgrade command notifies you and
requests permission to continue. If you choose to continue with the upgrade, you will be
required to restart any ongoing analysis and containerization workflows for your
applications.

## Syntax

```
app2container upgrade [--help]
```

## Options

**--help**

Displays the command help.

## Output

Console output is included in the Examples section for this command.

## Examples

Choose the operating system platform tab for the application server or worker machine where
you run the command.

Linux
Run the command shown below to upgrade your existing App2Container for
Linux.

```
`$` `sudo app2container upgrade`
`Using version 1.0
Version 1.1 available for download
Starting Download...
Starting Installation...
Installation successful!`
```

Windows
Run the command shown below to upgrade your existing App2Container for
Windows.

```
`PS>` `app2container upgrade`
`Using version 0.0
Version 2.0 available for download Starting Download...
Starting Installation...Installation successful!`
```
