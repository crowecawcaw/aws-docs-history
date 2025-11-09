# Release: Elastic Beanstalk Amazon Linux 2023 and Amazon Linux 2 Docker platform updates on January 31, 2024

This release is an emergent AWS Elastic Beanstalk Docker platform update for Amazon Linux 2023 and Amazon Linux 2.
It addresses a security vulnerability and updates Docker Compose for the AL2023 platform.

**Release date:** January 31, 2024

## Changes

The following table lists the changes included in this release.

###### Notes

- This release is cumulative from this month's prior AL2 and AL2023 platform releases. See [Platform history](../platforms/platform-history-docker.md "../platforms/platform-history-docker.md") in the _AWS Elastic Beanstalk Platforms_ guide for more
  information. Detailed release notes for the January AL2 and AL2023 platform releases will be published in this Release Notes guide.
- Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that
  Elastic Beanstalk supports. It might take a few hours for the release to complete.

| **Category**                  | **Description**                                                                                                                                                                                                                                                                                           |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | --------------- | ---- | ------- | ------- | ---- | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| **Security updates**          | Applied security updates to the Docker and ECS-based platform branches based on Amazon Linux 2023 and Amazon Linux 2. The security updates address [CVE-2024-21626](https://aws.amazon.com/security/security-bulletins/AWS-2024-001/ "https://aws.amazon.com/security/security-bulletins/AWS-2024-001/"). |
| **Platform-specific updates** | Made these platform-specific updates:<br>                                                                                                                                                                                                                                                                 | \*_Platform_<br>• | \*_Update_<br>• | <br> | --<br>• | --<br>• | <br> | \*_Docker_<br>• | **AL2023 Docker platform branch**<br>• Updated Docker Compose to version [2.24.3](https://docs.docker.com/compose/release-notes/#2243 "https://docs.docker.com/compose/release-notes/#2243"). |     |

## New platform versions

###### Notes

- The following tables list all _supported_ platform branches for each platform, including Amazon Linux 2. Only
  Amazon Linux 2023 platform branches are updated with this release.
- The following tables list _only supported_ platform branches. They do not list platform branches that are
  scheduled for retirement (deprecated). For full version information of Elastic Beanstalk _retiring_ (deprecated) platform
  branches, see [Elastic Beanstalk platform versions scheduled for retirement](../platforms/platforms-retiring.md "../platforms/platforms-retiring.md") in the
  _AWS Elastic Beanstalk Platforms_ guide.

###### These platforms are updated:

- [Docker](#release-2024-01-31-docker-ecs-cve.platforms.docker "#release-2024-01-31-docker-ecs-cve.platforms.docker")

### Docker

| Platform Version and _Solution Stack Name_                                         | AMI             | ECS Agent | Docker     | Docker Compose | Proxy Server |
| ---------------------------------------------------------------------------------- | --------------- | --------- | ---------- | -------------- | ------------ |
| **Docker AL2023 version 4.2.1**<br>_64bit Amazon Linux 2023 v4.2.1 running Docker_ | 2023.3.20240122 |           | 24.0.5-1   | 2.24.3         | nginx 1.24.0 |
| **ECS AL2023 version 4.0.4**<br>_64bit Amazon Linux 2023 v4.0.4 running ECS_       | 2023.3.20240122 | 1.80.0    |            |                |              |
| **Docker AL2 version 3.7.1**<br>_64bit Amazon Linux 2 v3.7.1 running Docker_       | 2.0.20240124    |           | 20.10.25-1 | 2.24.3         | nginx 1.22.1 |
| **ECS AL2 version 3.2.17**<br>_64bit Amazon Linux 2 v3.2.17 running ECS_           | 2.0.20240124    | 1.80.0    |            |                |              |
