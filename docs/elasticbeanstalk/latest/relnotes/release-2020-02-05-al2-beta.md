# Release: Elastic Beanstalk public beta update for Amazon Linux 2 platforms on February 5, 2020

AWS Elastic Beanstalk releases a Python beta platform version based on the Amazon Linux 2 operating system (OS), and provides updated
Amazon Corretto beta platform versions.

**Release date:** February 5, 2020

## Changes

|                                                                                               |
| --------------------------------------------------------------------------------------------- |
| AWS Elastic Beanstalk support for Amazon Linux 2 is in beta release and is subject to change. |

Today's release is an update to the Elastic Beanstalk Amazon Linux 2 public beta program that we announced on [November 25,
2019](release-2019-11-25-al2-beta.md "release-2019-11-25-al2-beta.md"). We released a new platform into the program—Python. We updated the Amazon Corretto beta platform versions. And we added some
missing features to all of the beta versions. Here's the list of added features:

- [Worker environments](../dg/using-features-managing-env-tiers.md "../dg/using-features-managing-env-tiers.md")
- [Log streaming to Amazon CloudWatch Logs](../dg/using-features.md#health-logs-cloudwatchlogs "../dg/using-features.md#health-logs-cloudwatchlogs")
- Immutable deployments – see [Deployment Policies and Settings](../dg/using-features.md "../dg/using-features.md")
- [AWS X-Ray integration](../dg/environment-configuration-debugging.md "../dg/environment-configuration-debugging.md")
- [Amazon Relational Database Service (Amazon RDS) integration](../dg/AWSHowTo.md "../dg/AWSHowTo.md")

The only key feature that beta platform versions still don't support is [serving static
files](../dg/environment-cfg-staticfiles.md "../dg/environment-cfg-staticfiles.md"). Stay tuned for its addition in a future beta update.

For a list of beta program platform versions, see [Elastic Beanstalk Platform Versions in Public Beta](../platforms/platforms-beta.md "../platforms/platforms-beta.md").
For considerations about migrating your existing Elastic Beanstalk application to Amazon Linux 2, see [Migrating Your
Linux Application to Amazon Linux 2](../dg/using-features.md "../dg/using-features.md").

###### Notes

- Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that
  Elastic Beanstalk supports. It might take a few hours for the release to complete.
- We initially also included a Docker AL2 beta platform version in this release. We later discovered issues with it and had to pull it out. Look
  for it in a coming update.

## New platform versions

###### These platforms are updated:

- [Java SE](#release-2020-02-05-al2-beta.platforms.javase "#release-2020-02-05-al2-beta.platforms.javase")
- [Python](#release-2020-02-05-al2-beta.platforms.python "#release-2020-02-05-al2-beta.platforms.python")

### Java SE

| Platform Version and _Solution Stack Name_                                                       | AMI          | Language             | Tools                                 | Proxy Server |
| ------------------------------------------------------------------------------------------------ | ------------ | -------------------- | ------------------------------------- | ------------ |
| **(BETA) Corretto 11 version 0.1.1**<br>_64bit Amazon Linux 2 v0.1.1 running Corretto 11 (BETA)_ | 2.0.20200115 | Corretto 11.0.6.10.1 | Ant 1.10.7, Gradle 5.6.2, Maven 3.6.2 | nginx 1.16.1 |
| **(BETA) Corretto 8 version 0.1.1**<br>_64bit Amazon Linux 2 v0.1.1 running Corretto 8 (BETA)_   | 2.0.20200115 | Corretto 8.242.08.1  | Ant 1.10.7, Gradle 5.6.2, Maven 3.6.2 | nginx 1.16.1 |

### Python

| Platform Version and _Solution Stack Name_                                                                                     | AMI          | Language     | Package Manager                                   | Packager | meld3   | AWS X‑Ray | Proxy Server |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------ | ------------ | ------------------------------------------------- | -------- | ------- | --------- | ------------ |
| **(BETA) Python 3.7 running on 64bit Amazon Linux 2 version 0.1.0**<br>_64bit Amazon Linux 2 v0.1.0 running Python 3.7 (BETA)_ | 2.0.20200115 | Python 3.7.4 | pip (latest at launch), pipenv (latest at launch) | removed  | removed | 3.1.0     | nginx 1.16.1 |
