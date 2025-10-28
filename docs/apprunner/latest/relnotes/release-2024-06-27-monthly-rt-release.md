# Release: App Runner runtime updates on June 27, 2024

This release provides minor version updates for the following language runtimes:
.NET, PHP, Ruby.

It also provides package updates to the following platforms:
Java, .NET.

**Release date:** June 27, 2024

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
| Base container image for AL2023                                                                                                 | Updated base container image to version **2023.4.20240611**. NoteThis image only applies to Node.js 18 and Python 3.11 runtimes.           |
| Base container image for AL2                                                                                                    | Updated base container image to version **2.0.20240620.0**. NoteThis image applies to all runtimes, except for Node.js 18 and Python 3.11. | To view the Amazon Linux container image on the _Amazon ECR Public Gallery,_ see the _Image tags_ tab on [Amazon ECR Public Gallery - amazonlinux](https://gallery.ecr.aws/amazonlinux/amazonlinux "https://gallery.ecr.aws/amazonlinux/amazonlinux"). |
|                                                                                                                                 | **Platform-specific updates**                                                                                                              | Made these platform-specific updates:                                                                                                                                                                                                                  |
| **Platform**                                                                                                                    | **Update**                                                                                                                                 |
| ---                                                                                                                             | ---                                                                                                                                        |
| **Corretto**                                                                                                                    | No updates to language versions. Tools Updates: <br>• Updated Maven to 3.9.8.                                                              |
| **.NET Core** [Supported runtimes](../dg/service-source-code-dotnet-releases.md "../dg/service-source-code-dotnet-releases.md") | Updated **.NET Core 6.0** to 6.0.31. Package updates: <br>• Updated .NET SDK to 6.0.423.                                                   |
| **PHP** [Supported runtimes](../dg/service-source-code-php-releases.md "../dg/service-source-code-php-releases.md")             | Updated PHP 8.1 to 8.1.29. No package updates.                                                                                             |
| **Ruby** [Supported runtimes](../dg/service-source-code-ruby-releases.md "../dg/service-source-code-ruby-releases.md")          | Updated Ruby 3.1 to 3.1.6. No package updates.                                                                                             |

|
