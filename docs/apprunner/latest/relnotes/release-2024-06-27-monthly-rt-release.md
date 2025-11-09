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

| **Category**                     | **Description**                                              |
| -------------------------------- | ------------------------------------------------------------ | ------------------ | --------------- | ---- | ------- | ------- | ---- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ---- | ---------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- | ---- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- | --- |
| **Base container image updates** | Made the following updates to the base container images:<br> | \*_Component_<br>• | \*_Update_<br>• | <br> | --<br>• | --<br>• | <br> | Base container image for AL2023 | Updated base container image to version **2023.4.20240611**.<br>NoteThis image only applies to Node.js 18 and Python 3.11 runtimes. | <br> | Base container image for AL2                                                                                                       | Updated base container image to version **2.0.20240620.0**.<br>NoteThis image applies to all runtimes, except for Node.js 18 and Python 3.11. | <br>To view the Amazon Linux container image on the *Amazon ECR Public Gallery,<br>• see the *Image tags<br>• tab on [Amazon ECR Public Gallery -<br>amazonlinux](https://gallery.ecr.aws/amazonlinux/amazonlinux "https://gallery.ecr.aws/amazonlinux/amazonlinux"). |
| **Platform-specific updates**    | Made these platform-specific updates:<br>                    | \*_Platform_<br>•  | \*_Update_<br>• | <br> | --<br>• | --<br>• | <br> | \*_Corretto_<br>•               | No updates to language versions.<br>Tools Updates:<br>• Updated Maven to 3.9.8.                                                     | <br> | **.NET Core**<br>[Supported runtimes](../dg/service-source-code-dotnet-releases.md "../dg/service-source-code-dotnet-releases.md") | Updated \*_.NET Core 6.0_<br>• to 6.0.31.<br>Package updates:<br>• Updated .NET SDK to 6.0.423.                                               | <br>                                                                                                                                                                                                                                                                  | **PHP**<br>[Supported runtimes](../dg/service-source-code-php-releases.md "../dg/service-source-code-php-releases.md") | Updated PHP 8.1 to 8.1.29.<br>No package updates. | <br> | **Ruby**<br>[Supported runtimes](../dg/service-source-code-ruby-releases.md "../dg/service-source-code-ruby-releases.md") | Updated Ruby 3.1 to 3.1.6.<br>No package updates. |     |
