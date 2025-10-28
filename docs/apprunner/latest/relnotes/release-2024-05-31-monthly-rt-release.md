# Release: App Runner runtime updates on May 31, 2024

This release provides minor version updates for the following language runtimes:
.NET, Node.js.

It also provides package updates to the following platforms:
Java, .NET, Node.js, Python, Ruby.

**Release date:** May 31, 2024

## App Runner managed platforms

App Runner provides convenient platform-specific managed runtimes. When you use a managed runtime, App Runner starts with a managed runtime base image to build a
container image from your source code. For more information, see [App Runner managed platforms](../dg/service-source-code.md#service-source-code.managed-platforms "../dg/service-source-code.md#service-source-code.managed-platforms") in the
_AWS App Runner Developer Guide_.

## Changes

The following table lists the changes included in this release.

| **Category**                                                                                                                    | **Description**                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Base container image updates**                                                                                                | Made the following updates to the base container images:                                                                                   |
| **Component**                                                                                                                   | **Update**                                                                                                                                 |
| ---                                                                                                                             | ---                                                                                                                                        |
| Base container image for AL2023                                                                                                 | Updated base container image to version **2023.4.20240528**. NoteThis image only applies to Node.js 18 and Python 3.11 runtimes.           |
| Base container image for AL2                                                                                                    | Updated base container image to version **2.0.20240521.0**. NoteThis image applies to all runtimes, except for Node.js 18 and Python 3.11. | To view the Amazon Linux container image on the _Amazon ECR Public Gallery,_ see the _Image tags_ tab on [Amazon ECR Public Gallery - amazonlinux](https://gallery.ecr.aws/amazonlinux/amazonlinux "https://gallery.ecr.aws/amazonlinux/amazonlinux"). |
|                                                                                                                                 | **Platform-specific updates**                                                                                                              | Made these platform-specific updates:                                                                                                                                                                                                                  |
| **Platform**                                                                                                                    | **Update**                                                                                                                                 |
| ---                                                                                                                             | ---                                                                                                                                        |
| **Corretto**                                                                                                                    | No updates to language versions. Tools Updates: <br>• Updated Maven to 3.9.7.                                                              |
| **.NET Core** [Supported runtimes](../dg/service-source-code-dotnet-releases.md "../dg/service-source-code-dotnet-releases.md") | Updated **.NET Core 6.0** to 6.0.30. Package updates: <br>• Updated .NET SDK to 6.0.422.                                                   |
| **Node.js** [Supported runtimes](../dg/service-source-code-nodejs-releases.md "../dg/service-source-code-nodejs-releases.md")   | Updated Node.js 18 to 18.20.3. Tools Updates: <br>• Updated yarn to 1.22.22.                                                               |
| **Python** [Supported runtimes](../dg/service-source-code-python-releases.md "../dg/service-source-code-python-releases.md")    | No updates to language versions. Package updates: <br>• Updated SQLite to 3.46.0.                                                          |
| **Ruby** [Supported runtimes](../dg/service-source-code-ruby-releases.md "../dg/service-source-code-ruby-releases.md")          | No updates to language versions. Package updates: <br>• Updated SQLite to 3.46.0.                                                          |

|
