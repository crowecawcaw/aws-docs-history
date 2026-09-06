

# Release: Elastic Beanstalk Docker platform updates on December 7, 2020
<a name="release-2020-12-07-docker"></a>

This release provides new versions for AWS Elastic Beanstalk Docker platforms. The release includes security updates.

**Release date:** December 7, 2020

## Changes
<a name="release-2020-12-07-docker.changes"></a>

This release applies a fix for an elevated privilege vulnerability to all Elastic Beanstalk Docker platforms. The release applies the fix to Amazon Linux AMI and Amazon Linux 2 Docker platform branches. For vulnerability details, see [https://alas.aws.amazon.com/ALAS-2020-1455.html](https://alas.aws.amazon.com/ALAS-2020-1455.html).

## New platform versions
<a name="release-2020-12-07-docker.platforms"></a>

**Topics**
+ [Docker](#release-2020-12-07-docker.platforms.docker)
+ [Multicontainer Docker](#release-2020-12-07-docker.platforms.mcdocker)
+ [Preconfigured Docker](#release-2020-12-07-docker.platforms.dockerpreconfig)

### Docker
<a name="release-2020-12-07-docker.platforms.docker"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Docker Version  |  Proxy Server  | 
| --- | --- | --- | --- | 
|  ** Docker AL2 version 3.2.2** <br /> * 64bit Amazon Linux 2 v3.2.2 running Docker *  | 2.0.20201130 | 19.03.13-ce | nginx 1.18.0 | 
|  ** Single Container Docker version 2.16.2** <br /> * 64bit Amazon Linux 2018.03 v2.16.2 running Docker 19.03.13-ce *  | 2018.03.0 | 19.03.13-ce | nginx 1.18.0 | 

### Multicontainer Docker
<a name="release-2020-12-07-docker.platforms.mcdocker"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Docker Version  |  ECS Agent  | 
| --- | --- | --- | --- | 
|  ** Multicontainer Docker version 2.24.0** <br /> * 64bit Amazon Linux 2018.03 v2.24.0 running Multi-container Docker 19.03.13-ce (Generic) *  | 2018.03.0 | 19.03.13-ce | 1.47.0 | 

### Preconfigured Docker
<a name="release-2020-12-07-docker.platforms.dockerpreconfig"></a>



|  Platform Version and *Solution Stack Name*   |  AMI  |  Platform  |  Container OS  |  Language  |  Proxy Server  |  Application Server  |  Docker Image  | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
|  ** Glassfish 5.0 (Docker) version 2.16.2** <br /> * 64bit Amazon Linux v2.16.2 running GlassFish 5.0 Java 8 (Preconfigured - Docker) *  | 2018.03.0 | Docker 19.03.13-ce | Amazon Linux 2018.03 | Java 8 | nginx 1.18.0 | Glassfish 5.0 | amazon/aws-eb-glassfish:5.0-al-onbuild-2.11.1 | 