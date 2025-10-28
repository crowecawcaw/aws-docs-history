# Release: Elastic Beanstalk Amazon Linux 2 Docker platform update on October 6, 2021

This release provides a new version for the AWS Elastic Beanstalk Docker platform based on Amazon Linux 2. The release includes a new Docker version
with security updates.

**Release date:** October 6, 2021

## Changes

This release updates the Docker platform to AWS Docker version 20.10.7-3, which is equivalent to the Docker organization version [20.10.9](https://docs.docker.com/engine/release-notes/#20109 "https://docs.docker.com/engine/release-notes/#20109").

This Docker version addresses the following security vulnerabilities:

- [CVE-2021-41089](https://nvd.nist.gov/vuln/detail/CVE-2021-41089 "https://nvd.nist.gov/vuln/detail/CVE-2021-41089")
- [CVE-2021-41091](https://nvd.nist.gov/vuln/detail/CVE-2021-41091 "https://nvd.nist.gov/vuln/detail/CVE-2021-41091")
- [CVE-2021-41092](https://nvd.nist.gov/vuln/detail/CVE-2021-41092 "https://nvd.nist.gov/vuln/detail/CVE-2021-41092")
- [CVE-2021-41103](https://nvd.nist.gov/vuln/detail/CVE-2021-41103 "https://nvd.nist.gov/vuln/detail/CVE-2021-41103")

###### Note

Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that
Elastic Beanstalk supports. It might take a few hours for the release to complete.

## New platform versions

### Docker

| Platform Version and _Solution Stack Name_
| AMI | Docker | Docker Compose | Proxy Server |
| --- | --- | --- | --- | --- |
| **Docker AL2 version 3.4.7** _64bit Amazon Linux 2 v3.4.7 running Docker_ | 2.0.20210813 | 20.10.7-3 | 1.29.2 | nginx 1.20.0 |
