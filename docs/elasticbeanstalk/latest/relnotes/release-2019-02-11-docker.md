# Release: AWS Elastic Beanstalk Docker platform updates on February 11, 2019

This release provides new Docker platform versions for AWS Elastic Beanstalk. The release includes security updates.

**Release date:** February 11, 2019

## Changes

Here is a list of the key changes in this release.

| **Category**         | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------- |
| **Security updates** | Applied a fix to a recently disclosed security issue, which affects several open-source container management systems. For information on this issue, see [CVE-2019-5736](https://access.redhat.com/security/cve/cve-2019-5736 "https://access.redhat.com/security/cve/cve-2019-5736"). See also the [Container Security Issue (CVE-2019-5736)](https://aws.amazon.com/security/security-bulletins/AWS-2019-002/ "https://aws.amazon.com/security/security-bulletins/AWS-2019-002/") AWS security bulletin. In addition, applied all security updates published in the [Amazon Linux Security Center](https://alas.aws.amazon.com/ "https://alas.aws.amazon.com/") on or before January 25, 2019 to the Docker platforms. | ## New platform versions ### Single Container Docker |

| Platform Version and _Solution Stack Name_
| AMI | Docker Version | Proxy Server |
| --- | --- | --- | --- |
| **Single Container Docker 18.03 version 2.12.8** _64bit Amazon Linux 2018.03 v2.12.8 running Docker 18.06.1-ce_ | 2018.03.0 | 18.06.1-ce | nginx 1.14.1 | ### Multicontainer Docker
| Platform Version and _Solution Stack Name_ | AMI | Docker Version | ECS Agent |
| --- | --- | --- | --- |
| **Multicontainer Docker 18.03 version 2.11.8** _64bit Amazon Linux 2018.03 v2.11.8 running Multi-container Docker 18.06.1-ce (Generic)_ | 2018.03.0 | 18.06.1-ce | 1.25.0 | ### Preconfigured Docker
| Platform Version and _Solution Stack Name_
| AMI | Platform | Container OS | Language | Proxy Server | Application Server | Docker Image |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Glassfish 5.0 (Docker) version 2.12.8** _64bit Amazon Linux v2.12.8 running GlassFish 5.0 Java 8 (Preconfigured - Docker)_ | 2018.03.0 | Docker 18.06.1-ce | Amazon Linux 2018.03 | Java 8 | nginx 1.14.1 | Glassfish 5.0 | amazon/aws-eb-glassfish:5.0-al-onbuild-2.11.1 |
| **Go 1.4 (Docker) version 2.12.8** _64bit Debian jessie v2.12.8 running Go 1.4 (Preconfigured - Docker)_ | 2018.03.0 | Docker 18.06.1-ce | Debian Jessie | Go 1.4.2 | nginx 1.14.1 | none | golang:1.4.2-onbuild |
| **Go 1.3 (Docker) version 2.12.8** _64bit Debian jessie v2.12.8 running Go 1.3 (Preconfigured - Docker)_ | 2018.03.0 | Docker 18.06.1-ce | Debian Jessie | Go 1.3.3 | nginx 1.14.1 | none | golang:1.3.3-onbuild |
| **Python 3.4 with uWSGI 2 (Docker) version 2.12.8** _64bit Debian jessie v2.12.8 running Python 3.4 (Preconfigured - Docker)_ | 2018.03.0 | Docker 18.06.1-ce | Debian Jessie | Python 3.4 | nginx 1.14.1 | uWSGI 2.0.8 | amazon/aws-eb-python:3.4.2-onbuild-3.5.1 |
