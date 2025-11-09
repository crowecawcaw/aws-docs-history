# Release: Elastic Beanstalk launches public beta Corretto platforms based on Amazon Linux 2 on November 25, 2019

AWS Elastic Beanstalk is releasing Amazon Corretto platform versions based on the Amazon Linux 2 operating system (OS), available as a public beta program.

**Release date:** November 25, 2019

## Changes

|                                                                                               |
| --------------------------------------------------------------------------------------------- |
| AWS Elastic Beanstalk support for Amazon Linux 2 is in beta release and is subject to change. |

Today we're starting a public beta program for customers who want to try out running their Elastic Beanstalk applications on the newer AWS Linux distribution
known as [Amazon Linux 2](https://aws.amazon.com/amazon-linux-2/ "https://aws.amazon.com/amazon-linux-2/"). We're initially releasing two Amazon Linux 2 platform versions for Amazon Corretto (one for
Corretto 8 and one for Corretto 11). [Amazon Corretto](https://aws.amazon.com/corretto "https://aws.amazon.com/corretto") is an AWS distribution of the Open Java Development Kit
(OpenJDK). We're working on adding additional platform versions based on Amazon Linux 2 for other languages to the beta program.

This is a beta release, and we recommend that you don't use these beta platform versions for production environments. We might change some naming and
implementation details before we fully support these platforms. In addition, Amazon Linux 2 platforms are missing some features in the beta versions. We're working
on adding support for these features. Here's a list of features that aren't supported at this time.

- [Worker environments](../dg/using-features-managing-env-tiers.md "../dg/using-features-managing-env-tiers.md")
- [Log streaming to Amazon CloudWatch Logs](../dg/using-features.md#health-logs-cloudwatchlogs "../dg/using-features.md#health-logs-cloudwatchlogs")
- Immutable deployments – see [Deployment Policies and Settings](../dg/using-features.md "../dg/using-features.md")
- [Serving static files](../dg/environment-cfg-staticfiles.md "../dg/environment-cfg-staticfiles.md")
- [AWS X-Ray integration](../dg/environment-configuration-debugging.md "../dg/environment-configuration-debugging.md")

For a list of beta program platform versions, see [Elastic Beanstalk Platform Versions in Public Beta](../platforms/platforms-beta.md "../platforms/platforms-beta.md").
For considerations about migrating your existing Elastic Beanstalk application to Amazon Linux 2, see [Migrating Your
Linux Application to Amazon Linux 2](../dg/using-features.md "../dg/using-features.md").

## New platform versions

### Java SE

| Platform Version and _Solution Stack Name_                                                       | AMI          | Language             | Tools                                 | Proxy Server |
| ------------------------------------------------------------------------------------------------ | ------------ | -------------------- | ------------------------------------- | ------------ |
| **(BETA) Corretto 11 version 0.1.0**<br>_64bit Amazon Linux 2 v0.1.0 running Corretto 11 (BETA)_ | 2.0.20191116 | Corretto 11.0.5.10.1 | Ant 1.10.7, Gradle 5.6.2, Maven 3.6.2 | nginx 1.16.1 |
| **(BETA) Corretto 8 version 0.1.0**<br>_64bit Amazon Linux 2 v0.1.0 running Corretto 8 (BETA)_   | 2.0.20191116 | Corretto 8.232.09.1  | Ant 1.10.7, Gradle 5.6.2, Maven 3.6.2 | nginx 1.16.1 |
