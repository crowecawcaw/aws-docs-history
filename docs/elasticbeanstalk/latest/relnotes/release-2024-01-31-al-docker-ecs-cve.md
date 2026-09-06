

# Release: Elastic Beanstalk Amazon Linux 2023 and Amazon Linux 2 Docker platform updates on January 31, 2024
<a name="release-2024-01-31-al-docker-ecs-cve"></a>

This release is an emergent AWS Elastic Beanstalk Docker platform update for Amazon Linux 2023 and Amazon Linux 2. It addresses a security vulnerability and updates Docker Compose for the AL2023 platform.

**Release date:** January 31, 2024

## Changes
<a name="release-2024-01-31-al-docker-ecs-cve.changes"></a>

The following table lists the changes included in this release.

**Notes**  
This release is cumulative from this month's prior AL2 and AL2023 platform releases. See [Platform history](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platform-history-docker.html) in the *AWS Elastic Beanstalk Platforms* guide for more information. Detailed release notes for the January AL2 and AL2023 platform releases will be published in this Release Notes guide. 
Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.


<table>
<thead>
  <tr><th><b>Category</b></th><th><b>Description</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Security updates</b></td><td>Applied security updates to the Docker and ECS-based platform branches based on Amazon Linux 2023 and Amazon Linux 2. The security updates address <a href="https://aws.amazon.com/security/security-bulletins/AWS-2024-001/">CVE-2024-21626</a>. </td></tr>
  <tr><td><b>Platform-specific updates</b></td><td>Made these platform-specific updates:
<table>
<thead>
  <tr><th><b>Platform</b></th><th><b>Update</b></th></tr>
</thead>
<tbody>
  <tr><td><b>Docker</b></td><td><b>AL2023 Docker platform branch</b><ul><li> Updated Docker Compose to version <a href="https://docs.docker.com/compose/release-notes/#2243">2.24.3</a>. </li></ul></td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>


## New platform versions
<a name="release-2024-01-31-al-docker-ecs-cve.platforms"></a>

**Notes**  
The following tables list all *supported* platform branches for each platform, including Amazon Linux 2. Only Amazon Linux 2023 platform branches are updated with this release.
The following tables list *only supported* platform branches. They do not list platform branches that are scheduled for retirement (deprecated). For full version information of Elastic Beanstalk *retiring* (deprecated) platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-retiring.html) in the *AWS Elastic Beanstalk Platforms* guide.

**Topics**
+ [Docker](#release-2024-01-31-docker-ecs-cve.platforms.docker)

### Docker
<a name="release-2024-01-31-docker-ecs-cve.platforms.docker"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  ECS Agent  |  Docker  |  Docker Compose  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | 
|  ** Docker AL2023 version 4.2.1** <br /> * 64bit Amazon Linux 2023 v4.2.1 running Docker *  | 2023.3.20240122 |  | 24.0.5-1 | 2.24.3 | nginx 1.24.0 | 
|  ** ECS AL2023 version 4.0.4** <br /> * 64bit Amazon Linux 2023 v4.0.4 running ECS *  | 2023.3.20240122 | 1.80.0 |  |  |  | 
|  ** Docker AL2 version 3.7.1** <br /> * 64bit Amazon Linux 2 v3.7.1 running Docker *  | 2.0.20240124 |  | 20.10.25-1 | 2.24.3 | nginx 1.22.1 | 
|  ** ECS AL2 version 3.2.17** <br /> * 64bit Amazon Linux 2 v3.2.17 running ECS *  | 2.0.20240124 | 1.80.0 |  |  |  | 