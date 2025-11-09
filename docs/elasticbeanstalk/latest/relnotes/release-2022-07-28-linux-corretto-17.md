# Release: Elastic Beanstalk Amazon Linux 2 Corretto platform updates on July 28, 2022

This release provides new versions for the AWS Elastic Beanstalk Corretto platforms based on Amazon Linux 2. It includes Amazon Linux 2 security updates.
This release also introduces a new platform branch, **Corretto 17**, based on Amazon Linux 2.

**Release date:** July 28, 2022

## Changes

The following table lists the changes included in this release.

###### Notes

- These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated)
  platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](../platforms/platforms-retiring.md "../platforms/platforms-retiring.md") in the
  _AWS Elastic Beanstalk Platforms_ guide.
- Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that
  Elastic Beanstalk supports. It might take a few hours for the release to complete.

| **Category**                  | **Description**                                                                                                                                                                                                                                      |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | --------------- | ---- | ------- | ------- | ---- | ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| **Security updates**          | Applied all security updates published in the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2.html "https://alas.aws.amazon.com/alas2.html") on or before \*_July 14, 2022_<br>• to all released Amazon Linux 2 Corretto platforms. |
| **Platform-specific updates** | Made these platform-specific updates:<br>                                                                                                                                                                                                            | \*_Platform_<br>• | \*_Update_<br>• | <br> | --<br>• | --<br>• | <br> | \*_Corretto_<br>• | **\*\*New!\*\*\*<br>• —<br>Introduced new **Corretto 17*<br>• platform branch, running Corretto version **17.0.3.6.1**.<br>For more information, see [Change Log for<br>Amazon Corretto 17](https://github.com/corretto/corretto-17/blob/develop/CHANGELOG.md#corretto-version-170361 "https://github.com/corretto/corretto-17/blob/develop/CHANGELOG.md#corretto-version-170361") in the Corretto 17 repository on GitHub. Also, see the [Amazon Corretto](https://aws.amazon.com/corretto "https://aws.amazon.com/corretto") website.<br>NoteRefer to the following \*\*Note*<br>• in the next section if you use the AWS CLI or EB CLI to create environments based on the<br>**Corretto 11\*<br>• or **Corretto 8\*<br>• platform versions in this release. |     |

## New platform versions

###### These currently supported platforms are updated:

- [Java SE](#release-2022-07-28-linux-corretto-17.platforms.javase "#release-2022-07-28-linux-corretto-17.platforms.javase")

### Java SE

###### Note - Customers that use the AWS CLI or EB CLI to create environments should be aware of the following:

In this release, for Corretto 8 and Corretto 11, there is a mismatch between the platform version of the branch and the version listed in the
_Solution Stack Name_.

- Corretto 8 **v3.2.17** has Solution Stack Name _64bit Amazon Linux 2 **v3.3.0** running
  Corretto 8_.
- Corretto 11 **v3.2.17** has Solution Stack Name _64bit Amazon Linux 2 **v3.3.0** running Corretto 11_.
  If you use the AWS CLI or EB CLI to create environments for these two platform branches in this release, be sure to use these solution stack names
  in parameters that require them.

This mismatch occurs in _this release only_. The platform releases that follow will have the
standard matching version names in their corresponding Solution Stack Name. The Elastic Beanstalk console does not display the Solution Stack Name, and is therefore not
affected.

| Platform Version and _Solution Stack Name_                                          | AMI          | Language             | Tools                                 | AWS X-Ray | Proxy Server |
| ----------------------------------------------------------------------------------- | ------------ | -------------------- | ------------------------------------- | --------- | ------------ |
| **Corretto 17 version 3.3.0**<br>_64bit Amazon Linux 2 v3.3.0 running Corretto 17_  | 2.0.20220606 | Corretto 17.0.3.6.1  | Ant 1.10.7, Gradle 7.4.2, Maven 3.6.2 | 3.2.0     | nginx 1.20.0 |
| **Corretto 11 version 3.2.17**<br>_64bit Amazon Linux 2 v3.3.0 running Corretto 11_ | 2.0.20220606 | Corretto 11.0.15.9.1 | Ant 1.10.7, Gradle 5.6.2, Maven 3.6.2 | 3.2.0     | nginx 1.20.0 |
| **Corretto 8 version 3.2.17**<br>_64bit Amazon Linux 2 v3.3.0 running Corretto 8_   | 2.0.20220606 | Corretto 8.332.08.1  | Ant 1.10.7, Gradle 5.6.2, Maven 3.6.2 | 3.2.0     | nginx 1.20.0 |
