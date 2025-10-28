# Supported operating systems and system

architectures for using MediaConnect Gateway

Before you can use AWS Elemental MediaConnect Gateway, you need an AWS account and the appropriate
permissions to access, view, and edit MediaConnect components. Additionally, you will
need physical hardware that complies to the MediaConnect Gateway requirements listed in the following
sections.

###### Contents

- [General information](gateway-prerequisites.md#system-requirements-general "gateway-prerequisites.md#system-requirements-general")
- [Supported system
  architectures](gateway-prerequisites.md#system-requirements-hardware "gateway-prerequisites.md#system-requirements-hardware")
- [Supported operating systems](gateway-prerequisites.md#system-requirements-os "gateway-prerequisites.md#system-requirements-os")

## General information

AWS Elemental MediaConnect Gateway is built on the Amazon Elastic Container Service Anywhere (ECS Anywhere) service. Amazon ECS
Anywhere enables you to register an _external
instance_, such as an on-premises server, to your AWS
infrastructure. This architecture requires that external instances using MediaConnect Gateway
comply with both Amazon ECS Anywhere requirements and additional MediaConnect Gateway requirements.

For a detailed understanding of Amazon ECS Anywhere and its cluster management
capabilities for on-premises hardware, refer to the following resources:

- [Amazon ECS clusters
  for the external launch type](../../../AmazonECS/latest/developerguide/ecs-anywhere.md "../../../AmazonECS/latest/developerguide/ecs-anywhere.md") in the _Amazon Elastic Container Service Developer Guide_
- [Amazon ECS Anywhere
  FAQs](https://aws.amazon.com/ecs/anywhere/faqs "https://aws.amazon.com/ecs/anywhere/faqs")

The following sections of this page outline hardware and operating system (OS)
requirements, as well as MediaConnect Gateway-specific requirements.

The following table contains the default quotas for each MediaConnect Gateway component.

| Component                                      | Default quota        | Can this quota be increased? |
| ---------------------------------------------- | -------------------- | ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Maximum number of gateways for each AWS Region | 3                    | Yes                          |
| Maximum number of instances for each gateway   | 20                   | No                           |
| Maximum number of bridges for each gateway     | 40                   | No                           |
| Maximum bitrate for each bridge                | 100 Mbps             | No                           | ## Supported system architectures The following table contains the recommended system architectures for your individual gateway instances. The system will determine the maximum number of bridges that can run on the instance. Only x86_64 CPU architectures are supported. MediaConnect Gateway does not support ARM-based CPUs: |
| Number of bridges                              | vCPU cores (2.6 GHz) | vCPU cores (3.0 GHz)         | Minimum RAM (GB)                                                                                                                                                                                                                                                                                                                    | Minimum disk space (GB) |
| ---                                            | ---                  | ---                          | ---                                                                                                                                                                                                                                                                                                                                 | ---                     |
| 10                                             | 2                    | 2                            | 4                                                                                                                                                                                                                                                                                                                                   | 25                      |
| 25                                             | 6                    | 4                            | 8                                                                                                                                                                                                                                                                                                                                   | 25                      |
| 40                                             | 10                   | 8                            | 16                                                                                                                                                                                                                                                                                                                                  | 25                      | **CPU references** The CPU architectures are benchmarked using these CPUs: <br>• 2.6 GHz - Intel E5-2660 v3 <br>• 3.0 GHz - AMD 7302 ## Supported operating systems The following list contains the supported operating systems (OS) and software configurations for your MediaConnect Gateway instances. **Supported operating systems** <br>• Ubuntu 20.04 **Required software** <br>• Docker - MediaConnect Gateway requires that you install the latest release of Docker. If you are using a Linux distribution other than RHEL, the instance registration script provided by MediaConnect will install Docker for you. Neither Docker or RHEL's open package repositories support installing Docker natively on RHEL. When using RHEL, you must ensure that Docker is installed before you run the instance registration script that's described in this document. |
