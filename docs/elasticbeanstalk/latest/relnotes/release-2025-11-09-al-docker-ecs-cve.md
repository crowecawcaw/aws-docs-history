# Release: Elastic Beanstalk Amazon Linux 2023 and Amazon Linux 2 Docker platform updates on November 9, 2025

This release is an emergent AWS Elastic Beanstalk Docker platform update for Amazon Linux 2023 and Amazon Linux 2.
It addresses a regression in the runc-1.3.2-2 library that causes directory permission issues preventing the ECS agent from starting.

**Release date:** November 9, 2025

## Changes

The following table lists the changes included in this release.

###### Notes

- These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated)
  platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](../platforms/platforms-retiring.md "../platforms/platforms-retiring.md") in the
  _AWS Elastic Beanstalk Platforms_ guide.
- Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that
  Elastic Beanstalk supports. It might take a few hours for the release to complete.

| **Category**                  | **Description**                           |
| ----------------------------- | ----------------------------------------- | ----------------- | --------------- | ---- | ------- | ------- | ---- | --------------- | ------------------------------------------------------------------------ | --- |
| **Platform-specific updates** | Made these platform-specific updates:<br> | \*_Platform_<br>• | \*_Update_<br>• | <br> | --<br>• | --<br>• | <br> | \*_Docker_<br>• | **AL2/AL2023 Docker platform branch**<br>• Updated runc to version 1.3.3 |     |

## New platform versions

###### Notes

- The following tables list _only supported_ platform branches. They do not list platform branches that are
  scheduled for retirement (deprecated). For full version information of Elastic Beanstalk _retiring_ (deprecated) platform
  branches, see [Elastic Beanstalk platform versions scheduled for retirement](../platforms/platforms-retiring.md "../platforms/platforms-retiring.md") in the
  _AWS Elastic Beanstalk Platforms_ guide.

###### These platforms are updated:

- [Docker](#2025-11-09-al-docker-ecs-runc.platforms.docker "#2025-11-09-al-docker-ecs-runc.platforms.docker")

### Docker

| Platform Version and _Solution Stack Name_                                         | AMI             | ECS Agent | Docker  | Docker Compose | Proxy Server |
| ---------------------------------------------------------------------------------- | --------------- | --------- | ------- | -------------- | ------------ |
| **Docker AL2023 version 4.7.5**<br>_64bit Amazon Linux 2023 v4.7.5 running Docker_ | 2023.9.20251105 |           | 25.0.13 | 2.40.0         | nginx 1.28.0 |
| **ECS AL2023 version 4.2.9**<br>_64bit Amazon Linux 2023 v4.2.9 running ECS_       | 2023.9.20251105 | 1.100.0   | 25.0.13 |                |              |
| **Docker AL2 version 4.3.5**<br>_64bit Amazon Linux 2 v4.3.5 running Docker_       | 2.0.20251105    |           | 25.0.13 | 2.40.0         | nginx 1.28.0 |
| **ECS AL2 version 3.5.9**<br>_64bit Amazon Linux 2 v3.5.9 running ECS_             | 2.0.20251105    | 1.100.0   | 25.0.13 |                |              |
