AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/ "https://aws.amazon.com/transform/"), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Applications you can containerize using

AWS App2Container

App2Container supports the following application types:

- Java applications (Linux)
- ASP.NET applications (Windows, Linux)
  For supported application frameworks, App2Container targets only the
  application files and dependencies that are needed for containerization, thereby minimizing
  the size of the resulting container image. This is known as _application mode_.

If App2Container does not find a supported framework running on your application
server, or if you have other dependent processes running on your server, App2Container takes a conservative
approach to identifying dependencies. This is known as _process mode_. For process
mode, all non-system files on the application server are included in the container image.

For more details on application and framework support, expand the section that matches
the platform that your application runs on.

###### Important

App2Container does not containerize database layer components. If your application requires access to a
database, you must configure your application container to have access to the database server.

App2Container supports identification and containerization of Java and ASP.NET applications
running on Linux.

###### Supported Linux distributions:

- Ubuntu
- CentOS
- RHEL
- Amazon Linux
  For supported frameworks, and other language-specific details, choose the tab
  that matches the language your application is written in.

Java
For Java applications, App2Container identifies Java processes, and can generate
container images that replicate the running state of each process. App2Container
determines which files to include in the application container image, based
on the Java application framework.

Application mode is supported for the following Java application
frameworks:

###### Supported frameworks

- Tomcat
- TomEE
- JBoss (standalone mode)

###### Note

Containerization is not supported for Java applications
running on frameworks that are using Cluster/HA mode.

ASP.NET
For ASP.NET applications running on Linux, App2Container detects the .NET runtime
version and containerizes the application using the corresponding runtime
base images.

###### Supported .NET Core runtime versions

- **.NET Core 3.1** – uses [SDK version 3.1](https://dotnet.microsoft.com/en-us/download/dotnet/3.1 "https://dotnet.microsoft.com/en-us/download/dotnet/3.1") as the base image for generic .NET
  Core applications (or the highest version if multiple versions
  are used).
- **.NET 5** – uses [SDK version 5.0](https://dotnet.microsoft.com/en-us/download/dotnet/5.0 "https://dotnet.microsoft.com/en-us/download/dotnet/5.0") as the base image for generic .NET
  Core applications (or the highest version if multiple versions
  are used).
- **.NET 6** – uses [SDK version 6.0](https://dotnet.microsoft.com/en-us/download/dotnet/6.0 "https://dotnet.microsoft.com/en-us/download/dotnet/6.0") as the base image for generic .NET
  Core applications (or the highest version if multiple versions
  are used).
- **.NET 7** – uses [SDK version 7.0](https://dotnet.microsoft.com/en-us/download/dotnet/7.0 "https://dotnet.microsoft.com/en-us/download/dotnet/7.0") as the base image for generic .NET
  Core applications (or the highest version if multiple versions
  are used).
- **.NET 8** – uses [SDK version 8.0](https://dotnet.microsoft.com/en-us/download/dotnet/8.0 "https://dotnet.microsoft.com/en-us/download/dotnet/8.0") as the base image for generic .NET
  Core applications (or the highest version if multiple versions
  are used).

###### Important

- Process mode is not supported for ASP.NET applications
  running on .NET Core.
- If you are using `.NET Core 3.1` or `.NET
5`, you must update the
  `analysis.json` file's
  `containerBaseImage` parameter to
  `mcr.microsoft.com/dotnet/sdk:3.1` or
  `mcr.microsoft.com/dotnet/sdk:5.0`,
  respectively. For more information, see [Configuring application containers](config-containers.md "config-containers.md").

App2Container supports containerization of ASP.NET applications deployed on IIS, including
IIS-hosted WCF applications, running on Windows Server 2016, 2019, and 2022. It uses
Windows Server Core as a base image for its container artifacts, matching the
Windows Server Core version to the operating system (OS) version of the server where
you run containerization commands.

If you use a worker machine to containerize your application, the version
matches your worker machine OS. If you are running containerization directly
on application servers, the version matches your application server OS.

If your applications are running on Windows Server 2008 or 2012 R2, you might still be able
to use App2Container by setting up a worker machine for containerization and deployment steps. App2Container does not support applications running on Windows client operating systems, such as Windows 7 or Windows 10.

###### Application framework and system requirements

- Containerization commands must run on Windows OS versions that support
  containers—Windows Server 2016, 2019, or 2022. This can be the worker
  machine, if you configure one, or the application server.
- If you use a worker machine to run containerization commands, App2Container supports
  Windows Server 2008 and up for the application server.

###### Note

Windows Server 2008 and 2012 only support App2Container up to version 1.47.
For more information, see [Release notes for AWS App2Container](release-notes.md "release-notes.md").

- IIS 7.5 or later.
- .NET framework version 3.5 or later.
- Docker version 17.07 or later (to install).

###### Note

App2Container does not support applications running on Windows client operating systems, such as Windows 7 or Windows 10.

###### Supported applications

- Simple ASP.NET applications running in a single container
- A Windows service running in a single container
- Complex ASP.NET applications that depend on WCF, running in a single
  container or multiple containers
- Complex ASP.NET applications that depend on Windows services or processes
  outside of IIS, running in a single container or multiple containers
- Complex, multi-node IIS or Windows service applications, running in a single
  container or multiple containers

###### Unsupported applications

- ASP.NET applications that use files and registries outside of IIS web application directories
- ASP.NET applications that depend on features of a Windows operating system version prior to Windows Server Core 2016
