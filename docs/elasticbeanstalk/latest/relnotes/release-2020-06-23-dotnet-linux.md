

# Release: Elastic Beanstalk introduces .NET Core on Linux on June 23, 2020
<a name="release-2020-06-23-dotnet-linux"></a>

This release introduces *.NET Core on Linux*, a new AWS Elastic Beanstalk platform.

**Release date:** June 23, 2020

## Changes
<a name="release-2020-06-23-dotnet-linux.changes"></a>

Today we're releasing an entirely new platform, *.NET Core on Linux*. With this platform, Elastic Beanstalk is extending its support for .NET Core applications beyond Windows Server. You can now run your .NET Core application on Amazon Linux 2 using the new platform. The platform comes with the nginx reverse proxy server and supports .NET Core 3.1 and .NET Core 2.1 frameworks.

For more information about the new platform, see [Working with .NET Core on Linux](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-dotnet-core-linux.html).

**Note**  
Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.

## New platform versions
<a name="release-2020-06-23-dotnet-linux.platforms"></a>

### .NET Core on Linux
<a name="release-2020-06-23-dotnet-linux.platforms.dotnetlinux"></a>



|  Platform Version and *Solution Stack Name*   |  Framework  |  Proxy Server  |  AMI  |  AWS X‑Ray  | 
| --- | --- | --- | --- | --- | 
|  ** .NET Core on AL2 version 1.0.0** <br /> * 64bit Amazon Linux 2 v1.0.0 running .NET Core *  | .NET Core 3.1.5, supports 3.1.5, 2.1.19 | nginx 1.16.1 | 2.0.20200603 | 3.2.0 | 