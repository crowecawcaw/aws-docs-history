AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/ "https://aws.amazon.com/transform/"), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# App2Container compatibility

The following documentation provides information for the operating systems, software, and
tooling that you can use with App2Container.

###### Contents

- [Operating system compatibility](#os-info-a2c "#os-info-a2c")
- [Containerization features](#containers-a2c "#containers-a2c")
- [Deployment features](#deployments-a2c "#deployments-a2c")
- [Pipeline support](#pipelines-a2c "#pipelines-a2c")

## Operating system compatibility

The following table contains information about the applications that App2Container supports
for each operating system.

| Compatibility item                                  | Linux                                                                                                                                                                                | Windows                                                                                                                                                                                                                                                                                                                            |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Supported application server operating systems<br>1 | • Ubuntu (version 18.04 and later)<br>• CentOS (version 8 and later)<br>• RHEL (version 7 and later)<br>• Amazon Linux 2 (AL2)<br>• Amazon Linux 2023 (AL2023)                       | • Windows Server 2016 and later<br>2                                                                                                                                                                                                                                                                                               |
| Container hosts                                     | The container host can be any supported application server operating<br>system. The major kernel version of the container host must match with<br>the container image.               | The container host operating system must be either Windows Server<br>2016, 2019, or 2022. The Windows Server operating system version of the<br>container host must match the container image. App2Container<br>automatically deploys the container host using the same operating<br>system used for the containerization process. |
| Application types                                   | • Java applications<br>• .NET applications                                                                                                                                           | • IIS .NET applications                                                                                                                                                                                                                                                                                                            |
| Supported frameworks                                | • Java (JDK 1.8 and later)<br>+ Tomcat<br>+ TomEE<br>+ JBoss (standalone mode)<br>• .NET applications<br>+ .NET Core 3.1<br>+ .NET 5<br>+ .NET 6<br>+ .NET 7<br>+ .NET 8<br>+ .NET 9 | .NET Framework version 3.5 and 4.x                                                                                                                                                                                                                                                                                                 |
| Unsupported application features                    | High Availability (HA) clusters                                                                                                                                                      | • IIS applications that use files and registries outside of<br>IIS web application directories                                                                                                                                                                                                                                     |
| Additional system requirements                      | • Docker version 17.07 and later<br>3<br>• kubectl versions up to v1.30 for Amazon EKS deployments.                                                                                  | • Docker version 17.07 and later<br>3<br>• kubectl versions up to v1.30 for Amazon EKS deployments.<br>• Windows IIS (7.5 and later)<br>• Windows PowerShell version 5.1 or PowerShell version 6 and<br>later                                                                                                                      |

1 We have only tested the operating systems and
configurations listed. Other operating systems could be compatible, but have not been
tested.

2 App2Container v1.47 is the last version that supports Windows
2008 and 2012. These operating systems also require a worker machine. We recommend using
a later version of the Windows Server operating system to be able to use the latest
version of App2Container. For more information, see [Applications you can containerize using AWS App2Container](supported-applications.md "supported-applications.md").

3 Docker must be installed to use App2Container. For more
information, see [Prerequisites: Set up your servers](start-intro.md#start-containerize-prereq "start-intro.md#start-containerize-prereq").

###### Note

Windows client operating systems such as Windows 7 and Windows 10 aren't
supported.

## Containerization features

App2Container supports the following containerization features.

| Containerization feature                                           | Linux         | Windows      |
| ------------------------------------------------------------------ | ------------- | ------------ |
| gMSA for connection with Active Directory                          | Not supported | Supported    |
| Containerization of multiple applications in the same<br>container | Not supported | Supported \* |
| Containerization of applications that use multiple ports           | Not supported | Supported    |

\* Containerizing multiple applications in the same container for Windows requires that
the applications are nested under a main IIS site.

For more information about configuring Windows containers with additional ports and
multiple applications, see [Configuring application containers](config-containers.md "config-containers.md").

For more information about group managed service accounts (gMSAs), see [Configuring container deployment](config-deployment.md "config-deployment.md").

## Deployment features

The following table lists the deployment services that App2Container supports.

| Deployment feature                                        | Linux                         | Windows                                                     |
| --------------------------------------------------------- | ----------------------------- | ----------------------------------------------------------- | -------------- | ------------------------- | ------------------------- | ----------------------------------------------------------- |
|                                                           | Amazon ECS (AWS Fargate only) | Amazon EKS (Amazon EC2 only)                                | AWS App Runner | Amazon ECS (AWS Fargate)  | Amazon ECS (Amazon EC2)   | Amazon EKS (Amazon EC2 only)                                |
| Modify memory usage                                       | Supported                     | Supported                                                   | Not supported  | Supported 1               | Supported                 | Supported                                                   |
| Modify CPU usage                                          | Supported                     | Supported                                                   | Not supported  | Supported                 | Supported                 | Supported                                                   |
| Load balancer types                                       | Application Load Balancer     | Application Load Balancer, Network Load Balancer with Nginx | N/A            | Application Load Balancer | Application Load Balancer | Application Load Balancer, Network Load Balancer with Nginx |
| Reuse VPC ²                                               | Supported                     | Supported                                                   | Not supported  | Supported                 | Supported                 | Supported                                                   |
| Reuse cluster previously deployed with App2Container<br>2 | Supported                     | Supported                                                   | N/A            | Supported                 | Supported                 | Supported                                                   |
| FireLens logging                                          | Supported                     | Not supported                                               | Not supported  | Not supported             | Not supported             | Not supported                                               |
| gMSA for connection with Active Directory                 | Not supported                 | Not supported                                               | Not supported  | Not supported             | Supported                 | Supported                                                   |
| Deploy complex .NET applications 3                        | N/A                           | N/A                                                         | N/A            | Supported                 | Supported                 | Supported                                                   |

1 AWS Fargate only supports certain Windows Server
operating systems for running Windows containers. Select a Windows Server operating
system that both Fargate and App2Container support. For more information, see [Windows platform versions](../../../AmazonECS/latest/developerguide/platform-windows-fargate.md "../../../AmazonECS/latest/developerguide/platform-windows-fargate.md") in the _Amazon ECS User Guide for
AWS Fargate_.

2 You can reuse certain components that App2Container created for a
prior deployment. For more information about the `reuseResources` object, see
[Configuring container deployment](config-deployment.md "config-deployment.md").

3 A complex .NET application has multiple Windows .NET
application components running in a single container. For more information, see [Containerizing complex Windows .NET applications with App2Container](summary-complex-win-apps.md "summary-complex-win-apps.md").

For more information about FireLens for Amazon ECS, see [Custom log routing](../../../AmazonECS/latest/developerguide/using_firelens.md "../../../AmazonECS/latest/developerguide/using_firelens.md") in the _Amazon Elastic Container Service Developer
Guide_.

For more information about deployment settings for group managed service accounts
(gMSAs), see [Configuring container deployment](config-deployment.md "config-deployment.md").

## Pipeline support

App2Container supports AWS CodePipeline, Jenkins, and Azure DevOps
Services pipeline types for both Windows and Linux. For more information
about configuring pipelines, see [Configuring container pipelines](config-pipeline.md "config-pipeline.md") and [Examples](cmd-generate-pipeline.md#generate-pipeline-examples "cmd-generate-pipeline.md#generate-pipeline-examples").
