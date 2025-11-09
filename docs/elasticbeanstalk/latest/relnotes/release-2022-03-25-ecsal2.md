# Release: Elastic Beanstalk introduces ECS running on Amazon Linux 2 to Docker platform on March 25, 2022

This release introduces a new platform branch based on Amazon Linux 2 to the AWS Elastic Beanstalk Docker platform:
**Amazon ECS running on 64bit Amazon Linux 2**.

**Release date:** March 25, 2022

## Changes

The following table lists the changes included in this release.

###### Note

Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that
Elastic Beanstalk supports. It might take a few hours for the release to complete.

| **Category**                  | **Description**                           |
| ----------------------------- | ----------------------------------------- | ----------------- | --------------- | ---- | ------- | ------- | ---- | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| **Platform-specific updates** | Made these platform-specific updates:<br> | \*_Platform_<br>• | \*_Update_<br>• | <br> | --<br>• | --<br>• | <br> | \*_Docker_<br>• | Added a new platform branch, **Amazon Elastic Container Service (Amazon ECS) running on Amazon Linux 2**, also known as **ECS<br>AL2.**<br>This platform branch is the Amazon Linux 2 based version of the **Multicontainer Docker\*<br>• platform branch that<br>runs on Amazon Linux AMI. Like the previous **Multicontainer Docker AL1*<br>• version, the new \*\*ECS AL2*<br>• platform branch uses<br>Amazon ECS to coordinate a deployment of multiple Docker containers to an Amazon ECS cluster in an Elastic Beanstalk environment.<br>The new **ECS AL2\*<br>• platform branch supports all of the features in the previous **Multicontainer Docker AL1*<br>• platform branch. You can deploy the same source code that's running on the<br>\*\*Multicontainer Docker AL1*<br>• platform branch to the new **ECS AL2**<br>platform branch without making any changes.<br>For more information, see<br>[The Docker platform family](../dg/create_deploy_docker.md#docker-platform "../dg/create_deploy_docker.md#docker-platform")<br>in the _AWS Elastic Beanstalk Developer Guide_. |     |

## New platform versions

###### Note

The following tables list all supported platform branches for each platform. Only Amazon Linux 2 platform branches are updated.

###### These platforms are updated:

- [Docker](#release-2022-03-25-ecsal2.platforms.docker "#release-2022-03-25-ecsal2.platforms.docker")

###### Note

Platform version _ECS Amazon Linux 2 version 3.0.0_ is running ECS Agent 1.57.1.

### Docker

| Platform Version and _Solution Stack Name_                                     | AMI          | Docker    | Docker Compose | Proxy Server |
| ------------------------------------------------------------------------------ | ------------ | --------- | -------------- | ------------ |
| **Docker AL2 version 3.4.12**<br>_64bit Amazon Linux 2 v3.4.12 running Docker_ | 2.0.20220207 | 20.10.7-5 | 1.29.2         | nginx 1.20.0 |
| **ECS AL2 version 3.0.0**<br>_64bit Amazon Linux 2 v3.0.0 running ECS_         | 2.0.20220218 |           |                |              |
