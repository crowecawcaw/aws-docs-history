

# Release: Elastic Beanstalk Amazon Linux 2 Docker platform update on September 10, 2020
<a name="release-2020-09-10-al2docker"></a>

This release is an emergent AWS Elastic Beanstalk Amazon Linux 2 Docker platform update. The release includes a kernel security update released after the latest Amazon Linux 2 platform update.

**Release date:** September 10, 2020

## Changes
<a name="release-2020-09-10-al2docker.changes"></a>

The following table lists the changes included in this release.

**Note**  
Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.


| **Category** | **Description** | 
| --- | --- | 
| **Security updates** | [ALAS2-2020-1488](https://alas.aws.amazon.com/AL2/ALAS-2020-1488.html), an Amazon Linux 2 kernel security update, was released after the most recent [Amazon Linux 2 update](https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2020-09-03-al2.html). The update fixes a vulnerability that affects containers. Today we're releasing a new version of the Docker platform that includes this kernel security update.<br />The release applies all security updates published in the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2.html) on or before **September 4, 2020** to the Amazon Linux 2 Docker platform. | 

## New platform versions
<a name="release-2020-09-10-al2docker.platforms"></a>

**Note**  
The following tables list all supported platform branches for each platform. Only Amazon Linux 2 platform branches are updated.

**Topics**
+ [Docker](#release-2020-09-10-al2docker.platforms.docker)

### Docker
<a name="release-2020-09-10-al2docker.platforms.docker"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Docker Version  |  Proxy Server  | 
| --- | --- | --- | --- | 
|  ** Docker AL2 version 3.1.2** <br /> * 64bit Amazon Linux 2 v3.1.2 running Docker *  | 2.0.20200905 | 19.03.6-ce | nginx 1.18.0 | 
|  ** Single Container Docker version 2.15.3** <br /> * 64bit Amazon Linux 2018.03 v2.15.3 running Docker 19.03.6-ce *  | 2018.03.0 | 19.03.6-ce | nginx 1.16.1 | 