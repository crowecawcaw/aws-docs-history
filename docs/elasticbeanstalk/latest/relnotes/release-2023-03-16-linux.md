

# Release: Elastic Beanstalk Amazon Linux 2 platform updates for AWS China Regions. on March 16, 2023
<a name="release-2023-03-16-linux"></a>

This release provides new versions for the AWS Elastic Beanstalk Docker and Python platforms for the AWS China Regions. These two platform updates were not included in the last release for the AWS China Regions. This release also includes updates to Apache HTTP server for the Python platform, which is a security release.

**Release date:** March 16, 2023

## Changes
<a name="release-2023-03-16-linux.changes"></a>

Today's release provides updates to the Docker and Python platforms for the following Regions. It also includes updates to Apache HTTP server for the Python platform, which is a security release. These updates were part of the prior release, but not included for these two Regions. 
+ China (Ningxia)—cn-northwest-1
+ China (Beijing)—cn-north-1

Today's release is cumulative. It includes all of the updates listed in the [March 7 Amazon Linux 2 platform release](release-2023-03-07-linux.md). The Docker and Python updates listed here were also part of the last release, but were not included for the AWS China Regions.

**Notes**  
These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated) platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-retiring.html) in the *AWS Elastic Beanstalk Platforms* guide.
Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.

## New platform versions
<a name="release-2023-03-16-linux.platforms"></a>

**Note**  
Today's release is cumulative. It includes all of the updates listed in the [March 7 Amazon Linux 2 platform release](release-2023-03-07-linux.md).

**Topics**
+ [Docker](#release-2023-03-07-linux.platforms.docker)
+ [Python](#release-2023-03-07-linux.platforms.python)

### Docker
<a name="release-2023-03-07-linux.platforms.docker"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  ECS Agent  |  Docker  |  Docker Compose  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | 
|  ** Docker AL2 version 3.5.5** <br /> * 64bit Amazon Linux 2 v3.5.5 running Docker *  | 2.0.20230221 |  | 20.10.17-1 | 1.29.2 | nginx 1.22.1 | 
|  ** ECS AL2 version 3.2.5** <br /> * 64bit Amazon Linux 2 v3.2.5 running ECS *  | 2.0.20230221 | 1.68.2 |  |  |  | 

### Python
<a name="release-2023-03-07-linux.platforms.python"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Language  |  Package Manager  |  Packager  |  meld3  |  AWS X-Ray  |  Proxy Server  | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
|  ** Python 3.8 AL2 version 3.5.0** <br /> * 64bit Amazon Linux 2 v3.5.0 running Python 3.8 *  | 2.0.20230221 | Python 3.8.16 | pipenv 2023.2.18 |  |  | 3.2.0 | nginx 1.22.1 (default), Apache 2.4.55 | 
|  ** Python 3.7 AL2 version 3.5.0** <br /> * 64bit Amazon Linux 2 v3.5.0 running Python 3.7 *  | 2.0.20230221 | Python 3.7.16 | pipenv 2023.2.18 |  |  | 3.2.0 | nginx 1.22.1 (default), Apache 2.4.55 | 