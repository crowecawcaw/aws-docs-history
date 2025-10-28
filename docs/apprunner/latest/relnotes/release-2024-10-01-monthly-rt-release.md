# Release: App Runner runtime updates on October 01, 2024

This release provides minor version updates for the following language runtimes:
Python.

It also provides package updates to the following platforms:
.

**Release date:** October 01, 2024

## App Runner managed platforms

App Runner provides convenient platform-specific managed runtimes. When you use a managed runtime, App Runner starts with a managed runtime base image to build a
container image from your source code. For more information, see [App Runner managed platforms](../dg/service-source-code.md#service-source-code.managed-platforms "../dg/service-source-code.md#service-source-code.managed-platforms") in the
_AWS App Runner Developer Guide_.

## Changes

The following table lists the changes included in this release.

| **Category**                                                                                                                 | **Description**                                                                                                                                                                                                                                           |
| ---------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Base container image updates**                                                                                             | Made the following updates to the base container images:                                                                                                                                                                                                  |
| **Component**                                                                                                                | **Update**                                                                                                                                                                                                                                                |
| ---                                                                                                                          | ---                                                                                                                                                                                                                                                       |
| Base container image for AL2023                                                                                              | Updated base container image to version **2023.5.20240916.0**. NoteThis image only applies to Node.js 18 and Python 3.11 runtimes.                                                                                                                        |
| Base container image for AL2                                                                                                 | Updated base container image to version **2.0.20240916.0**. NoteThis image applies to all runtimes, except for Node.js 18 and Python 3.11.                                                                                                                | To view the Amazon Linux container image on the _Amazon ECR Public Gallery,_ see the _Image tags_ tab on [Amazon ECR Public Gallery - amazonlinux](https://gallery.ecr.aws/amazonlinux/amazonlinux "https://gallery.ecr.aws/amazonlinux/amazonlinux"). |
|                                                                                                                              | **Platform-specific updates**                                                                                                                                                                                                                             | Made these platform-specific updates:                                                                                                                                                                                                                  |
| **Platform**                                                                                                                 | **Update**                                                                                                                                                                                                                                                |
| ---                                                                                                                          | ---                                                                                                                                                                                                                                                       |
| **Python** [Supported runtimes](../dg/service-source-code-python-releases.md "../dg/service-source-code-python-releases.md") | Updated Python 3.11 to 3.11.10. For more information, see the [release notes](https://docs.python.org/release/3.11.10/whatsnew/changelog.html#changelog "https://docs.python.org/release/3.11.10/whatsnew/changelog.html#changelog"). No package updates. |

|
