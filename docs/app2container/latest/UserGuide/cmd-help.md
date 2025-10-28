AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/ "https://aws.amazon.com/transform/"), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# app2container help command

Lists the commands for App2Container, grouped into the phases where they would normally
run.

###### Note

Commands are shown in alphabetical order within the phases where they run. For
example, in the _Analyze_ phase, you would run the
**inventory** command first, then the **analyze**
command. Utility commands are included after the containerization phases.

## Syntax

```
app2container help
```

## Parameters and options

None

## Output

The list of app2container commands.

## Examples

```
`app2container help``App2Container is an application from Amazon Web Services (AWS),
that provides commands to discover and containerize applications.

Commands
 Getting Started
 init Sets up workspace for artifacts

 Analyze
 analyze Analyzes the selected application to identify dependencies required for containerization
 inventory Lists all applications that can be containerized

 Transform
 containerize Generates Dockerfile, container images, and deployment metadata
 extract Creates an archive of application artifacts for containerization

 Deploy
 generate Generates ECS, EKS, or Pipeline artifacts

 Settings
 upgrade Upgrades app2container CLI to latest version
 upload-support-bundle Uploads user's app2container logs and supporting artifacts to the support team

Flags
 --debug enable debug logging
 -h, --help help for app2container
 --version version for app2container`
```
