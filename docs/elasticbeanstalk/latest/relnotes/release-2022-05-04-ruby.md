# Release: Elastic Beanstalk Amazon Linux 2 Ruby platform update on May 4, 2022

This release provides a new version for the AWS Elastic Beanstalk Ruby platforms based on Amazon Linux 2.
The release provides runtime updates to Ruby 3.0 along with security updates for the Amazon Linux 2 operating system running on the Ruby platforms.

**Release date:** May 4, 2022

## Changes

This release updates all of the Amazon Linux 2 Ruby platforms to AWS Ruby platform version 3.4.6. The following updates were applied.

- Updated Ruby 3.0 to release [3.0.4](https://www.ruby-lang.org/en/news/2022/04/12/ruby-3-0-4-released/ "https://www.ruby-lang.org/en/news/2022/04/12/ruby-3-0-4-released/").
- Applied the following security updates.
  - [ALAS-2022-1580](https://alas.aws.amazon.com/ALAS-2022-1580.html "https://alas.aws.amazon.com/ALAS-2022-1580.html"): [CVE-2022-0070](https://alas.aws.amazon.com/cve/html/CVE-2022-0070.html "https://alas.aws.amazon.com/cve/html/CVE-2022-0070.html")
  - [ALAS-2022-1581](https://alas.aws.amazon.com/ALAS-2022-1581.html "https://alas.aws.amazon.com/ALAS-2022-1581.html"): [CVE-2022-26490](https://alas.aws.amazon.com/cve/html/CVE-2022-26490.html "https://alas.aws.amazon.com/cve/html/CVE-2022-26490.html")
    [CVE-2022-27666](https://alas.aws.amazon.com/cve/html/CVE-2022-27666.html "https://alas.aws.amazon.com/cve/html/CVE-2022-27666.html")
    [CVE-2022-28356](https://alas.aws.amazon.com/cve/html/CVE-2022-28356.html "https://alas.aws.amazon.com/cve/html/CVE-2022-28356.html")

###### Note

The CVEs in this list are part of the prior [April 29,2022 Linux platform release](release-2022-04-29-linux.md "release-2022-04-29-linux.md"), but were missing
for the Ruby platforms update. Today's release also includes all of the CVEs delivered in the Ruby platforms from the prior release.

Today's release is cumulative. It also includes the following updates from the prior [April 29,2022 Linux
platform release](release-2022-04-29-linux.md "release-2022-04-29-linux.md").

- Updated Ruby 2.7 and 2.6 to releases [2.7.6](https://www.ruby-lang.org/en/news/2022/04/12/ruby-2-7-6-released/ "https://www.ruby-lang.org/en/news/2022/04/12/ruby-2-7-6-released/") and [2.6.10](https://www.ruby-lang.org/en/news/2022/04/12/ruby-2-6-10-released/ "https://www.ruby-lang.org/en/news/2022/04/12/ruby-2-6-10-released/"), respectively.
- Updated RubyGems to release [3.3.12](https://blog.rubygems.org/2022/04/20/3.3.12-released.html "https://blog.rubygems.org/2022/04/20/3.3.12-released.html").
- Updated Puma to version [5.6.4](https://github.com/puma/puma/releases/tag/v5.6.4 "https://github.com/puma/puma/releases/tag/v5.6.4"). The new Puma version is a security release.

###### Notes

- These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated)
  platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](../platforms/platforms-retiring.md "../platforms/platforms-retiring.md") in the
  _AWS Elastic Beanstalk Platforms_ guide.
- Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that
  Elastic Beanstalk supports. It might take a few hours for the release to complete.

## New platform versions

### Ruby

| Platform Version and _Solution Stack Name_
| AMI | Language | Package Manager | Application Server | AWS X-Ray | Proxy Server |
| --- | --- | --- | --- | --- | --- | --- |
| **Ruby 3.0 AL2 version 3.4.6** _64bit Amazon Linux 2 v3.4.6 running Ruby 3.0_ | 2.0.20220419 | Ruby 3.0.4-p208 | RubyGems 3.3.12 | Puma 5.6.4 | 3.2.0 | nginx 1.20.0 |
| **Ruby 2.7 AL2 version 3.4.6** _64bit Amazon Linux 2 v3.4.6 running Ruby 2.7_ | 2.0.20220419 | Ruby 2.7.6-p219 | RubyGems 3.3.12 | Puma 5.6.4 | 3.2.0 | nginx 1.20.0 |
