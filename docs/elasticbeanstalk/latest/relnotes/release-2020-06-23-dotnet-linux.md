# Release: Elastic Beanstalk introduces .NET Core on Linux on June 23, 2020

This release introduces _.NET Core on Linux_, a new AWS Elastic Beanstalk platform.

**Release date:** June 23, 2020

## Changes

Today we're releasing an entirely new platform, _.NET Core on Linux_. With this platform, Elastic Beanstalk is extending its support for .NET
Core applications beyond Windows Server. You can now run your .NET Core application on Amazon Linux 2 using the new platform. The platform comes with the nginx
reverse proxy server and supports .NET Core 3.1 and .NET Core 2.1 frameworks.

For more information about the new platform, see [Working with .NET Core on
Linux](../dg/create-deploy-dotnet-core-linux.md "../dg/create-deploy-dotnet-core-linux.md").

###### Note

Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that
Elastic Beanstalk supports. It might take a few hours for the release to complete.

## New platform versions

### .NET Core on Linux

| Platform Version and _Solution Stack Name_                                            | Framework                               | Proxy Server | AMI          | AWS X‑Ray |
| ------------------------------------------------------------------------------------- | --------------------------------------- | ------------ | ------------ | --------- |
| **.NET Core on AL2 version 1.0.0**<br>_64bit Amazon Linux 2 v1.0.0 running .NET Core_ | .NET Core 3.1.5, supports 3.1.5, 2.1.19 | nginx 1.16.1 | 2.0.20200603 | 3.2.0     |
