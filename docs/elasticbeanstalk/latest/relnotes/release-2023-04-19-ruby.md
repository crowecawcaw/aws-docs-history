# Release: Elastic Beanstalk Amazon Linux 2 Ruby platform update on

April 19, 2023

This release provides new branch versions for the AWS Elastic Beanstalk Ruby platform based on Amazon Linux 2.
The release includes Ruby language updates that address security vulnerabilities CVE-2023-28755 and CVE-2023-28756.
It also includes AMI and Puma server updates for the Ruby platform.

**Release date:** April 19, 2023

## Changes

The following changes for the Ruby platform are included in this release.

- Updated the base AMI to version 2.0.20230404.
- Updated Puma to version [6.2.1](https://github.com/puma/puma/releases/tag/v6.2.1 "https://github.com/puma/puma/releases/tag/v6.2.1").
- Updated Ruby 3.0 and Ruby 2.7 to releases [3.0.6](https://www.ruby-lang.org/en/news/2023/03/30/ruby-3-0-6-released/ "https://www.ruby-lang.org/en/news/2023/03/30/ruby-3-0-6-released/") and [2.7.8](https://www.ruby-lang.org/en/news/2023/03/30/ruby-2-7-8-released/ "https://www.ruby-lang.org/en/news/2023/03/30/ruby-2-7-8-released/"), respectively.

Both of these Ruby language updates address the following security
vulnerabilities.

    + [CVE-2023-28755: ReDoS vulnerability in URI](https://www.ruby-lang.org/en/news/2023/03/28/redos-in-uri-cve-2023-28755/ "https://www.ruby-lang.org/en/news/2023/03/28/redos-in-uri-cve-2023-28755/")
    + [CVE-2023-28756: ReDoS vulnerability in Time](https://www.ruby-lang.org/en/news/2023/03/30/redos-in-time-cve-2023-28756/ "https://www.ruby-lang.org/en/news/2023/03/30/redos-in-time-cve-2023-28756/")

###### Note

Be aware that at the time these release notes are published, the new platform
versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It
might take a few hours for the release to complete.

## New platform

versions

###### These platforms are updated:

- [Ruby](#release-2023-04-18-ruby.platforms.ruby "#release-2023-04-18-ruby.platforms.ruby")

### Ruby

| Platform Version and _Solution Stack Name_                                       | AMI          | Language        | Package Manager | Application Server | AWS X-Ray | Proxy Server |
| -------------------------------------------------------------------------------- | ------------ | --------------- | --------------- | ------------------ | --------- | ------------ |
| **Ruby 3.0 AL2 version 3.6.6**<br>_64bit Amazon Linux 2 v3.6.6 running Ruby 3.0_ | 2.0.20230404 | Ruby 3.0.6-p216 | RubyGems 3.4.10 | Puma 6.2.1         | 3.2.0     | nginx 1.22.1 |
| **Ruby 2.7 AL2 version 3.6.6**<br>_64bit Amazon Linux 2 v3.6.6 running Ruby 2.7_ | 2.0.20230404 | Ruby 2.7.8-p225 | RubyGems 3.4.10 | Puma 6.2.1         | 3.2.0     | nginx 1.22.1 |
