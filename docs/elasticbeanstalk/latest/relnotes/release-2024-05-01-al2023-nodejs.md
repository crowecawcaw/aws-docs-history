# Release: Elastic Beanstalk Amazon Linux 2023 Node.js platform updates on May 01, 2024

This release is an emergent AWS Elastic Beanstalk Node.js platform update for
Amazon Linux 2023. It addresses a security vulnerability
and also updates Apache HTTP server on the Node.js AL2023 platforms.

**Release date:** May 01, 2024

## Changes

The following table lists the changes included in this release.

###### Notes

- These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated)
  platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](../platforms/platforms-retiring.md "../platforms/platforms-retiring.md") in the
  _AWS Elastic Beanstalk Platforms_ guide.
- Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that
  Elastic Beanstalk supports. It might take a few hours for the release to complete.

| **Category**                  | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | --------------- | ---- | ------- | ------- | ---- | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| **Security updates**          | Applied all security updates published in the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html "https://alas.aws.amazon.com/alas2023.html") on or before<br>\*_April 25, 2024_<br>• to all AL2023 platforms.<br>Applied security updates that address [CVE-2024-27983](https://explore.alas.aws.amazon.com/CVE-2024-27983.html "https://explore.alas.aws.amazon.com/CVE-2024-27983.html") to the<br>Node.js AL2023 platform branches. |
| **Cross-platform updates**    | Made these cross-platform updates:<br>                                                                                                                                                                                                                                                                                                                                                                                                                        | \*_Component_<br>• | \*_Update_<br>• | <br> | --<br>• | --<br>• | <br> | \*_AMI_<br>•     | Updated the base AMI to version 2023.4.20240429.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |     |
| **Platform-specific updates** | Made these platform-specific updates:<br>                                                                                                                                                                                                                                                                                                                                                                                                                     | \*_Platform_<br>•  | \*_Update_<br>• | <br> | --<br>• | --<br>• | <br> | \*_Node.js_<br>• | **Language runtime updates**<br>• Updated Node.js 20 to version [20.12.2](https://nodejs.org/en/blog/release/v20.12.2 "https://nodejs.org/en/blog/release/v20.12.2").<br>• For Node.js 18, the security updates were backported to the existing [18.18.2](https://nodejs.org/en/blog/release/v18.18.2 "https://nodejs.org/en/blog/release/v18.18.2") language release on the platform branch.<br>This Node.js update is a security release.<br>**Apache HTTP Server**<br>• Updated Apache HTTP Server 2.4 to version 2.4.59. For details, see [Changes with Apache 2.4.59](https://downloads.apache.org/httpd/CHANGES_2.4.59 "https://downloads.apache.org/httpd/CHANGES_2.4.59") on the \*Apache Software<br>Foundation<br>• website.<br>This Apache update is security release. |     |

## New platform versions

###### These platforms are updated:

- [Node.js](#release-2024-05-01-nodejs-al2023.platforms.nodejs "#release-2024-05-01-nodejs-al2023.platforms.nodejs")

### Node.js

| Platform Version and _Solution Stack Name_                                                 | AMI             | Node.js versions (npm versions)              | Proxy Server                          | Git    | AWS X-Ray |
| ------------------------------------------------------------------------------------------ | --------------- | -------------------------------------------- | ------------------------------------- | ------ | --------- |
| **Node.js 20 AL2023 version 6.1.4**<br>_64bit Amazon Linux 2023 v6.1.4 running Node.js 20_ | 2023.4.20240429 | 20.12.2 (10.5.0)<br>Default version: 20.12.2 | nginx 1.24.0 (default), Apache 2.4.59 | 2.40.1 | 3.2.0     |
| **Node.js 18 AL2023 version 6.1.4**<br>_64bit Amazon Linux 2023 v6.1.4 running Node.js 18_ | 2023.4.20240429 | 18.18.2 (9.8.1)<br>Default version: 18.18.2  | nginx 1.24.0 (default), Apache 2.4.59 | 2.40.1 | 3.2.0     |
