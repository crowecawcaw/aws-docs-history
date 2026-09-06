

# Release: Elastic Beanstalk Amazon Linux 2023 and Amazon Linux 2 Docker platform updates on November 9, 2025
<a name="release-2025-11-09-al-docker-ecs-cve"></a>

This release is an emergent AWS Elastic Beanstalk Docker platform update for Amazon Linux 2023 and Amazon Linux 2. It addresses a regression in the runc-1.3.2-2 library that causes directory permission issues preventing the ECS agent from starting.

**Release date:** November 9, 2025

## Changes
<a name="release-2025-11-09-al-docker-ecs-cve.changes"></a>

The following table lists the changes included in this release.

**Notes**  
These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated) platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-retiring.html) in the *AWS Elastic Beanstalk Platforms* guide.
Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Platform-specific updates</b></td><td>Made these platform-specific updates:
<table>
<thead>
  <tr><th><b>Platform</b></th><th><b>Update</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Docker</b></td><td><b>AL2/AL2023 Docker platform branch</b><ul><li> Updated runc to version 1.3.3  </li></ul></td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>


## New platform versions
<a name="release-2025-11-09-al-docker-ecs-cve.platforms"></a>

**Notes**  
The following tables list *only supported* platform branches. They do not list platform branches that are scheduled for retirement (deprecated). For full version information of Elastic Beanstalk *retiring* (deprecated) platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-retiring.html) in the *AWS Elastic Beanstalk Platforms* guide.

**Topics**
+ [Docker](#2025-11-09-al-docker-ecs-runc.platforms.docker)

### Docker
<a name="2025-11-09-al-docker-ecs-runc.platforms.docker"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  ECS Agent  |  Docker  |  Docker Compose  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | 
|  ** Docker AL2023 version 4.7.5** <br /> * 64bit Amazon Linux 2023 v4.7.5 running Docker *  | 2023.9.20251105 |  | 25.0.13 | 2.40.0 | nginx 1.28.0 | 
|  ** ECS AL2023 version 4.2.9** <br /> * 64bit Amazon Linux 2023 v4.2.9 running ECS *  | 2023.9.20251105 | 1.100.0 | 25.0.13 |  |  | 
|  ** Docker AL2 version 4.3.5** <br /> * 64bit Amazon Linux 2 v4.3.5 running Docker *  | 2.0.20251105 |  | 25.0.13 | 2.40.0 | nginx 1.28.0 | 
|  ** ECS AL2 version 3.5.9** <br /> * 64bit Amazon Linux 2 v3.5.9 running ECS *  | 2.0.20251105 | 1.100.0 | 25.0.13 |  |  | 