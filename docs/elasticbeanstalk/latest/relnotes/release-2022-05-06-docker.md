# Release: Elastic Beanstalk Amazon Linux 2 Docker platform update on May 6, 2022

This release provides a new version for the _AWS Elastic Beanstalk Docker Amazon Linux 2_ platform (_Docker AL2_).
The release includes a new Docker version along with security updates.

**Release date:** May 6, 2022

## Changes

This release updates the _Docker AL2_ platform to version 3.4.15. It provides the following updates in this platform:

- Docker Engine version [20.10.13](https://docs.docker.com/engine/release-notes/#201013 "https://docs.docker.com/engine/release-notes/#201013").
- Base AMI version **2.0.20220426**
- Applies all security updates published in the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2.html "https://alas.aws.amazon.com/alas2.html") on or before **May 4, 2022**.

###### Notes

- These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated)
  platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](../platforms/platforms-retiring.md "../platforms/platforms-retiring.md") in the
  _AWS Elastic Beanstalk Platforms_ guide.
- Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that
  Elastic Beanstalk supports. It might take a few hours for the release to complete.

## New platform versions

###### These currently supported platforms are updated:

- [Docker](#release-2022-05-06-docker.platforms.docker "#release-2022-05-06-docker.platforms.docker")

### Docker

| Platform Version and _Solution Stack Name_
| AMI | Docker | Docker Compose | Proxy Server |
| --- | --- | --- | --- | --- |
| **Docker AL2 version 3.4.15** _64bit Amazon Linux 2 v3.4.15 running Docker_ | 2.0.20220426 | 20.10.13-2 | 1.29.2 | nginx 1.20.0 |
| **ECS AL2 version 3.1.1** _64bit Amazon Linux 2 v3.1.1 running ECS_ | 2.0.20220419 | | | |
