# Release: Elastic Beanstalk public beta update for Amazon Linux 2 platforms on March 2, 2020

AWS Elastic Beanstalk releases a Docker beta platform version based on the Amazon Linux 2 operating system (OS).

**Release date:** March 2, 2020

## Changes

|                                                                                               |
| --------------------------------------------------------------------------------------------- |
| AWS Elastic Beanstalk support for Amazon Linux 2 is in beta release and is subject to change. |

On February 5, 2020, when we [released the Amazon Linux 2 Python beta platform](release-2020-02-05-al2-beta.md "release-2020-02-05-al2-beta.md"), we also intended to include
an Amazon Linux 2 Docker beta platform version. We ended up having to pull it out due to some last minute issues we discovered with it.

Today we're re-releasing the Elastic Beanstalk Amazon Linux 2 Docker beta platform version. It's available for all customers to evaluate.

For a list of beta program platform versions, see [Elastic Beanstalk Platform Versions in Public Beta](../platforms/platforms-beta.md "../platforms/platforms-beta.md").
For considerations about migrating your existing Elastic Beanstalk application to Amazon Linux 2, see [Migrating Your
Linux Application to Amazon Linux 2](../dg/using-features.md "../dg/using-features.md").

###### Note

Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that
Elastic Beanstalk supports. It might take a few hours for the release to complete.

## New platform versions

###### These platforms are updated:

- [Single Container Docker](#release-2020-03-02-al2-beta.platforms.docker "#release-2020-03-02-al2-beta.platforms.docker")

### Single Container Docker

| Platform Version and _Solution Stack Name_                                                                             | AMI          | Docker Version | Proxy Server |
| ---------------------------------------------------------------------------------------------------------------------- | ------------ | -------------- | ------------ |
| **(BETA) Docker running on 64bit Amazon Linux 2 version 0.1.1**<br>_64bit Amazon Linux 2 v0.1.1 running Docker (BETA)_ | 2.0.20200207 | 18.09.9-ce     | nginx 1.16.1 |
