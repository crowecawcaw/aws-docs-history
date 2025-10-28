# Release: Elastic Beanstalk Amazon Linux Java and Tomcat platform updates on December 28, 2021

This release provides new versions for AWS Elastic Beanstalk Java and Tomcat platforms.
The release includes an additional Log4j-related security update.

**Release date:** December 28, 2021

## Changes

This release applies an additional update to the Apache Log4j hotpatch package that we initially released in the [December 21, 2021 platform release](release-2021-12-21-linux.md "release-2021-12-21-linux.md").

The release applies all security updates published in the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2.html "https://alas.aws.amazon.com/alas2.html") on or before **December 23, 2021** to all released platforms.

###### Notes

- These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated)
  platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](../platforms/platforms-retiring.md "../platforms/platforms-retiring.md") in the
  _AWS Elastic Beanstalk Platforms_ guide.
- Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that
  Elastic Beanstalk supports. It might take a few hours for the release to complete.

## New platform versions

###### These currently supported platforms are updated:

- [Java SE](#release-2021-12-28-java.platforms.javase "#release-2021-12-28-java.platforms.javase")
- [Tomcat](#release-2021-12-28-java.platforms.java "#release-2021-12-28-java.platforms.java")

### Java SE

| Platform Version and _Solution Stack Name_
| AMI | Language | Tools | AWS X-Ray | Proxy Server |
| --- | --- | --- | --- | --- | --- |
| **Corretto 11 version 3.2.10** _64bit Amazon Linux 2 v3.2.10 running Corretto 11_ | 2.0.20211201 | Corretto 11.0.13.8.2 | Ant 1.10.7, Gradle 5.6.2, Maven 3.6.2 | 3.2.0 | nginx 1.20.0 |
| **Corretto 8 version 3.2.10** _64bit Amazon Linux 2 v3.2.10 running Corretto 8_ | 2.0.20211201 | Corretto 8.312.07.2 | Ant 1.10.7, Gradle 5.6.2, Maven 3.6.2 | 3.2.0 | nginx 1.20.0 | ### Tomcat
| Platform Version and _Solution Stack Name_ | AMI | Language | AWS X-Ray | Application Server | Proxy Server |
| --- | --- | --- | --- | --- | --- |
| **Corretto 11 with Tomcat 8.5 AL2 version 4.2.10** _64bit Amazon Linux 2 v4.2.10 running Tomcat 8.5 Corretto 11_ | 2.0.20211201 | Corretto 11.0.13.8.2 | 3.2.0 | Tomcat 8.5.72 | nginx 1.20.0 (default), Apache 2.4.51 |
| **Corretto 8 with Tomcat 8.5 AL2 version 4.2.10** _64bit Amazon Linux 2 v4.2.10 running Tomcat 8.5 Corretto 8_ | 2.0.20211201 | Corretto 8.312.07.2 | 3.2.0 | Tomcat 8.5.72 | nginx 1.20.0 (default), Apache 2.4.51 |
