# Release: Elastic Beanstalk Amazon Linux 2 platform updates for AWS China Regions. on March 16, 2023

This release provides new versions for the AWS Elastic Beanstalk Docker and Python platforms for
the AWS China Regions. These two platform updates were not included in the last release for the AWS China Regions.
This release also includes updates to Apache HTTP server for the Python platform,
which is a security release.

**Release date:** March 16, 2023

## Changes

Today's release provides updates to the Docker and Python platforms for the following Regions. It also includes updates to
Apache HTTP server for the Python platform, which is a security release. These updates were part of the prior release, but not included for
these two Regions.

- China (Ningxia)—cn-northwest-1
- China (Beijing)—cn-north-1

Today's release is cumulative. It includes all of the updates listed in the [March 7 Amazon Linux 2 platform
release](release-2023-03-07-linux.md "release-2023-03-07-linux.md"). The Docker and Python updates listed here were also part of the last release, but were not included for the
AWS China Regions.

###### Notes

- These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated)
  platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](../platforms/platforms-retiring.md "../platforms/platforms-retiring.md") in the
  _AWS Elastic Beanstalk Platforms_ guide.
- Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that
  Elastic Beanstalk supports. It might take a few hours for the release to complete.

## New platform versions

###### Note

Today's release is cumulative. It includes all of the updates listed in the [March 7 Amazon Linux 2 platform
release](release-2023-03-07-linux.md "release-2023-03-07-linux.md").

###### These platforms are updated:

- [Docker](#release-2023-03-07-linux.platforms.docker "#release-2023-03-07-linux.platforms.docker")
- [Python](#release-2023-03-07-linux.platforms.python "#release-2023-03-07-linux.platforms.python")

### Docker

| Platform Version and _Solution Stack Name_
| AMI | ECS Agent | Docker | Docker Compose | Proxy Server |
| --- | --- | --- | --- | --- | --- |
| **Docker AL2 version 3.5.5** _64bit Amazon Linux 2 v3.5.5 running Docker_ | 2.0.20230221 | | 20.10.17-1 | 1.29.2 | nginx 1.22.1 |
| **ECS AL2 version 3.2.5** _64bit Amazon Linux 2 v3.2.5 running ECS_ | 2.0.20230221 | 1.68.2 | | | | ### Python
| Platform Version and _Solution Stack Name_
| AMI | Language | Package Manager | Packager | meld3 | AWS X-Ray | Proxy Server |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Python 3.8 AL2 version 3.5.0** _64bit Amazon Linux 2 v3.5.0 running Python 3.8_ | 2.0.20230221 | Python 3.8.16 | pipenv 2023.2.18 | | | 3.2.0 | nginx 1.22.1 (default), Apache 2.4.55 |
| **Python 3.7 AL2 version 3.5.0** _64bit Amazon Linux 2 v3.5.0 running Python 3.7_ | 2.0.20230221 | Python 3.7.16 | pipenv 2023.2.18 | | | 3.2.0 | nginx 1.22.1 (default), Apache 2.4.55 |
