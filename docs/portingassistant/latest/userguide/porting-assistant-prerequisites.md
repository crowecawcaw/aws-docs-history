AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/ "https://aws.amazon.com/transform/"), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Prerequisites

The following prerequisites must be verified in order to successfully port your
existing .NET applications to .NET Core using the Porting Assistant for .NET tool.

###### Topics

- [Prerequisites](#porting-assistant-prereq-versions-dependencies "#porting-assistant-prereq-versions-dependencies")
- [Memory requirements](#porting-assistant-vs-ide-memory-requirements "#porting-assistant-vs-ide-memory-requirements")

## Prerequisites

The Porting Assistant for .NET tool requires the following prerequisites for installation and
usage.

- **.NET 6 SDK**: [Download
  .NET](https://dotnet.microsoft.com/download/dotnet-core "https://dotnet.microsoft.com/download/dotnet-core").
- Windows 7 or later
- Internet connectivity on the machine running the assessment
- If your machine is behind a proxy with restricted internet access, you
  must permit access to the following:
  - **Amazon S3 Datastore** —
    `https://s3.us-west-2.amazonaws.com/aws.portingassistant.dotnet.datastore/`
  - **Amazon S3 Datastore authentication
    endpoint** —
    `https://encore-telemetry.us-east-1.amazonaws.com/`
  - **GitHub datastore** —
    `hhttps://github.com/aws/porting-assistant-dotnet-datastore/tree/master/data`
  - **GitHub user content** —
    `http://raw.githubusercontent.com/`
  - **NuGet or additional package
    addresses** — any addresses required to restore
    your project packages (the most common one being
    `api.nuget.com`)

- Administrator access
- Processor with 1.8 GHz or above processing speed
- 4 GB minimum of available memory
- 5 GB minimum of free disk space

## Memory requirements

for the Porting Assistant for .NET Visual Studio for .NET IDE extension.

The following memory requirements must be met to use the Porting Assistant for .NET Visual Studio
for .NET IDE extension.

| Solution size                                      | Minimum memory requirements                     |
| -------------------------------------------------- | ----------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| Small solutions (1,000 to 50,000 lines of code)    | 4 GB                                            |
| Medium solutions (50,000 to 400,000 lines of code) | 8 GB                                            |
| Large solutions (400,000 or more lines of code)    | 16 GB or more, depending on size of source code | ###### Note These requirements are provided as estimates. Individual solutions can vary for memory usage. |
