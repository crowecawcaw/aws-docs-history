# Release: App Runner runtime updates on March 28, 2024

This release provides minor version updates for the

Node.js

and .NET Core

language runtimes.

It also provides package updates to the
Python,
Node.js,

.NET Core,

and Ruby

platforms.

**Release date:** March 28, 2024

## App Runner managed platforms

App Runner provides convenient platform-specific managed runtimes. When you use a managed runtime, App Runner starts with a managed runtime base image to build a
container image from your source code. For more information, see [App Runner managed platforms](../dg/service-source-code.md#service-source-code.managed-platforms "../dg/service-source-code.md#service-source-code.managed-platforms") in the
_AWS App Runner Developer Guide_.

## Changes

The following table lists the changes included in this release.

| **Category**                     | **Description**                                              |
| -------------------------------- | ------------------------------------------------------------ | ------------------ | --------------- | ---- | ------- | ------- | ---- | ------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| **Base container image updates** | Made the following updates to the base container images:<br> | \*_Component_<br>• | \*_Update_<br>• | <br> | --<br>• | --<br>• | <br> | Base container image for AL2023                                                                                                | Updated base container image to version **2023.3.20240312.0**.<br>NoteThis image only applies to Node.js 18 and Python 3.11 runtimes.                                                                                                                                                                                                                                                                                                                                                                                  | <br> | Base container image for AL2                                                                                                     | Updated base container image to version **2.0.20240306.2**.<br>NoteThis image applies to all runtimes, except for Node.js 18 and Python 3.11. | <br>To view the Amazon Linux container image on the *Amazon ECR Public Gallery,<br>• see the *Image tags<br>• tab on [Amazon ECR Public Gallery -<br>amazonlinux](https://gallery.ecr.aws/amazonlinux/amazonlinux "https://gallery.ecr.aws/amazonlinux/amazonlinux"). |
| **Platform-specific updates**    | Made these platform-specific updates:<br>                    | \*_Platform_<br>•  | \*_Update_<br>• | <br> | --<br>• | --<br>• | <br> | **.NET Core**<br>[Supported runtimes](../dg/service-source-code-net6-releases.md "../dg/service-source-code-net6-releases.md") | Updated **.NET Core 6.0\*<br>• to version [6.0.28](https://github.com/dotnet/core/blob/main/release-notes/6.0/6.0.28/6.0.28.md "https://github.com/dotnet/core/blob/main/release-notes/6.0/6.0.28/6.0.28.md").<br>Package updates:<br>• Updated **dotnet6-sdk\*<br>• package to version **6.0.420**. For more<br>information see [6.0.28](https://github.com/dotnet/core/blob/main/release-notes/6.0/6.0.28/6.0.28.md "https://github.com/dotnet/core/blob/main/release-notes/6.0/6.0.28/6.0.28.md") Release<br>Notes. | <br> | **Node.js**<br>[Supported runtimes](../dg/service-source-code-nodejs-releases.md "../dg/service-source-code-nodejs-releases.md") | Updated Node.js 18 to version [18.19.1](https://nodejs.org/en/blog/release/v18.19.1 "https://nodejs.org/en/blog/release/v18.19.1")            | <br>                                                                                                                                                                                                                                                                  | **Python**<br>[Supported runtimes](../dg/service-source-code-python-releases.md "../dg/service-source-code-python-releases.md") | No updates to language versions.<br>Package updates:<br>• Updated **SQLite\*<br>• package to version **3.45.2\*<br>• for<br>**Python 3.7**,<br>**Python 3.8**,<br>and **Python 3.11**.<br>For more information see [SQLite Release History](https://www.sqlite.org/chronology.html "https://www.sqlite.org/chronology.html"). | <br> | **Ruby**<br>[Supported runtimes](../dg/service-source-code-ruby-releases.md "../dg/service-source-code-ruby-releases.md") | No updates to language versions.<br>Package updates:<br>• Updated **SQLite\*<br>• package to version **3.45.2\*<br>• for **Ruby 3.1**. For more information see [SQLite Release<br>History](https://www.sqlite.org/chronology.html "https://www.sqlite.org/chronology.html"). |     |
