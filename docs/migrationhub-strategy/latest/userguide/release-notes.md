AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Release notes

###### Topics

- [November 17, 2023](#nov17-releasenote "#nov17-releasenote")
- [October 12, 2023](#oct12-releasenote "#oct12-releasenote")
- [April 17, 2023](#april17-releasenote "#april17-releasenote")
- [March 17, 2023](#march17-releasenote "#march17-releasenote")
- [November 07, 2022](#nov07-releasenote "#nov07-releasenote")
- [September 27, 2022](#sep27-releasenote "#sep27-releasenote")
- [June 30, 2022](#jun20-releasenote "#jun20-releasenote")
- [April 18, 2022](#apr18-releasenote "#apr18-releasenote")
- [February 25, 2022](#feb25-releasenote "#feb25-releasenote")
- [February 10, 2022](#feb10-releasenote "#feb10-releasenote")
- [January 28, 2022](#jan28-releasenote "#jan28-releasenote")
- [January 14, 2022](#jan14-releasenote "#jan14-releasenote")
- [December 21, 2021](#dec21-releasenote "#dec21-releasenote")
- [December 15, 2021](#dec15-releasenote "#dec15-releasenote")
- [October 25, 2021](#oct25-releasenote "#oct25-releasenote")

## November 17, 2023

**New features**

- Collector v1.1.47
- Support for .NET 8 applications.

## October 12, 2023

**New features**

- Collector v1.1.45
- Support for Multi-data sources.

## April 17, 2023

**New features**

- Collector v1.1.22
- Upgrade script enhancements. This requires the latest version of the Collector.

## March 17, 2023

**New feature**

Added binary analysis, which provides anti-patterns and incompatibilities detection without
source code.

## November 07, 2022

**New feature**

- Application filtering for applications
- Server filtering by AWS Application Discovery Service tags

## September 27, 2022

**New feature**

- Collector v1.1.12
  - SCT version 667
  - EMPAnalyzer 2.2.0.368

- Added `diag check` commands for server insights.
- Added support for _Potential_ recommendations.
- Enhanced user interface to check configuration and assessment status.

**Bug fixes**

- Porting assistant translator and other fixes.

## June 30, 2022

**New feature**

- Collector v1.1.11
  - Added VMware API support.
  - A2C requested changes to add user header while downloading the binary file.
  - Added Linux home path, default shell, and remote termination of all shells.

- A2C v1.17 public binary
  - Added support for Azure DevOps as a pipeline deployment target.

## April 18, 2022

**New feature**

- Collector v1.1.7
- Added the capability to dynamically download A2C binary from the public URL.

**Bug fixes**

- A2C v1.1.5

## February 25, 2022

**Bug fixes**

- SCT v5.6.9
- A2C v1.1.2
- Collector v1.1.4

## February 10, 2022

**Bug fixes**

- SCT v5.6.8
- A2C v1.1.1
  - Added a check for the **tar** command on Linux.
  - Fixed the issue of checking application images in Amazon ECR.
  - Fixed the issue requiring container removal for pre-validation.

- Collector v1.1.3
  - Fixed the 4xx error for remote 32-bit machine.
  - Updated the A2C error codes.
  - Validated the IP address in `C#` for source code analysis of the remote
    machine.

## January 28, 2022

**New feature**

- Collector v1.1.2
- Added Azure DevOps Git repository support for source code analysis.

## January 14, 2022

**New feature**

- Collector v1.1.1
- Added Babelfish recommendations for SQL databases.

## December 21, 2021

**Issue resolved**

- Collector v1.1.0
- Database analysis has been restored.

## December 15, 2021

**Known issue**

- Collector v1.0.4
- Database analysis is currently unsupported (CVE-2021-44228).

## October 25, 2021

**New feature**

- Collector v1.0.0
- Initial release of the Migration Hub Strategy Recommendations User Guide.
