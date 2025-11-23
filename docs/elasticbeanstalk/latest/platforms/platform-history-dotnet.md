# .NET on Windows Server platform history

This page lists the current and previous versions of AWS Elastic Beanstalk's .NET platform branches and the dates that each version was current.
Previous platform versions remain accessible to accounts with active or terminated environments using them at the time they were superseded by a new version.

See the [Supported platforms](platforms-supported.md "platforms-supported.md") page for information on the latest version of each platform
supported by Elastic Beanstalk. Detailed release notes are available for recent releases at [AWS Elastic Beanstalk Release Notes](../relnotes.md "../relnotes.md").

## November 19, 2025 – present

The following Elastic Beanstalk platform versions for .NET on Windows Server have been current since November 19, 2025:

### Configuration basics

| Platform Version                                          | Solution Stack Name                                       | Framework                                                                       | Proxy Server |
| --------------------------------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2025 with IIS 10.0 version 2.21.1**      | _64bit Windows Server 2025 v2.21.1 running IIS 10.0_      | .NET 9.0.11, supports 9.0.11, 8.0.22<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2025 with IIS 10.0 version 2.21.1** | _64bit Windows Server Core 2025 v2.21.1 running IIS 10.0_ | .NET 9.0.11, supports 9.0.11, 8.0.22<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2022 with IIS 10.0 version 2.21.1**      | _64bit Windows Server 2022 v2.21.1 running IIS 10.0_      | .NET 9.0.11, supports 9.0.11, 8.0.22<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2022 with IIS 10.0 version 2.21.1** | _64bit Windows Server Core 2022 v2.21.1 running IIS 10.0_ | .NET 9.0.11, supports 9.0.11, 8.0.22<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2019 with IIS 10.0 version 2.21.1**      | _64bit Windows Server 2019 v2.21.1 running IIS 10.0_      | .NET 9.0.11, supports 9.0.11, 8.0.22<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.21.1** | _64bit Windows Server Core 2019 v2.21.1 running IIS 10.0_ | .NET 9.0.11, supports 9.0.11, 8.0.22<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.21.1**      | _64bit Windows Server 2016 v2.21.1 running IIS 10.0_      | .NET 9.0.11, supports 9.0.11, 8.0.22<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.21.1** | _64bit Windows Server Core 2016 v2.21.1 running IIS 10.0_ | .NET 9.0.11, supports 9.0.11, 8.0.22<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |

### More details

| Platform Version                                          | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| --------------------------------------------------------- | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2025 with IIS 10.0 version 2.21.1**      | 2025.11.12  | 3.7.1163.0       |           | 3.3.3050.0 | 4.0        | 3.6.1     |
| **Windows Server Core 2025 with IIS 10.0 version 2.21.1** | 2025.11.12  | 3.7.1163.0       |           | 3.3.3050.0 | 4.0        | 3.6.1     |
| **Windows Server 2022 with IIS 10.0 version 2.21.1**      | 2025.11.12  | 3.7.1163.0       |           | 3.3.3050.0 | 4.0        | 3.6.1     |
| **Windows Server Core 2022 with IIS 10.0 version 2.21.1** | 2025.11.12  | 3.7.1163.0       |           | 3.3.3050.0 | 4.0        | 3.6.1     |
| **Windows Server 2019 with IIS 10.0 version 2.21.1**      | 2025.11.12  | 3.7.1163.0       |           | 3.3.3050.0 | 4.0        | 3.6.1     |
| **Windows Server Core 2019 with IIS 10.0 version 2.21.1** | 2025.11.12  | 3.7.1163.0       |           | 3.3.3050.0 | 4.0        | 3.6.1     |
| **Windows Server 2016 with IIS 10.0 version 2.21.1**      | 2025.11.12  | 3.7.1163.0       |           | 3.3.3050.0 | 4.0        | 3.6.1     |
| **Windows Server Core 2016 with IIS 10.0 version 2.21.1** | 2025.11.12  | 3.7.1163.0       |           | 3.3.3050.0 | 4.0        | 3.6.1     |

## October 23, 2025 – November 18, 2025

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between October 23, 2025 and November 18, 2025:

### Configuration basics

| Platform Version                                          | Solution Stack Name                                       | Framework                                                                       | Proxy Server |
| --------------------------------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2025 with IIS 10.0 version 2.21.0**      | _64bit Windows Server 2025 v2.21.0 running IIS 10.0_      | .NET 9.0.10, supports 9.0.10, 8.0.21<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2025 with IIS 10.0 version 2.21.0** | _64bit Windows Server Core 2025 v2.21.0 running IIS 10.0_ | .NET 9.0.10, supports 9.0.10, 8.0.21<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2022 with IIS 10.0 version 2.21.0**      | _64bit Windows Server 2022 v2.21.0 running IIS 10.0_      | .NET 9.0.10, supports 9.0.10, 8.0.21<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2022 with IIS 10.0 version 2.21.0** | _64bit Windows Server Core 2022 v2.21.0 running IIS 10.0_ | .NET 9.0.10, supports 9.0.10, 8.0.21<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2019 with IIS 10.0 version 2.21.0**      | _64bit Windows Server 2019 v2.21.0 running IIS 10.0_      | .NET 9.0.10, supports 9.0.10, 8.0.21<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.21.0** | _64bit Windows Server Core 2019 v2.21.0 running IIS 10.0_ | .NET 9.0.10, supports 9.0.10, 8.0.21<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.21.0**      | _64bit Windows Server 2016 v2.21.0 running IIS 10.0_      | .NET 9.0.10, supports 9.0.10, 8.0.21<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.21.0** | _64bit Windows Server Core 2016 v2.21.0 running IIS 10.0_ | .NET 9.0.10, supports 9.0.10, 8.0.21<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |

### More details

| Platform Version                                          | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| --------------------------------------------------------- | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2025 with IIS 10.0 version 2.21.0**      | 2025.10.15  | 3.7.1144.0       |           | 3.3.3050.0 | 4.0        | 3.6.1     |
| **Windows Server Core 2025 with IIS 10.0 version 2.21.0** | 2025.10.15  | 3.7.1144.0       |           | 3.3.3050.0 | 4.0        | 3.6.1     |
| **Windows Server 2022 with IIS 10.0 version 2.21.0**      | 2025.10.15  | 3.7.1144.0       |           | 3.3.3050.0 | 4.0        | 3.6.1     |
| **Windows Server Core 2022 with IIS 10.0 version 2.21.0** | 2025.10.15  | 3.7.1144.0       |           | 3.3.3050.0 | 4.0        | 3.6.1     |
| **Windows Server 2019 with IIS 10.0 version 2.21.0**      | 2025.10.15  | 3.7.1144.0       |           | 3.3.3050.0 | 4.0        | 3.6.1     |
| **Windows Server Core 2019 with IIS 10.0 version 2.21.0** | 2025.10.15  | 3.7.1144.0       |           | 3.3.3050.0 | 4.0        | 3.6.1     |
| **Windows Server 2016 with IIS 10.0 version 2.21.0**      | 2025.10.15  | 3.7.1144.0       |           | 3.3.3050.0 | 4.0        | 3.6.1     |
| **Windows Server Core 2016 with IIS 10.0 version 2.21.0** | 2025.10.15  | 3.7.1144.0       |           | 3.3.3050.0 | 4.0        | 3.6.1     |

## September 22, 2025 – October 22, 2025

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between September 22, 2025 and October 22, 2025:

### Configuration basics

| Platform Version                                          | Solution Stack Name                                       | Framework                                                                     | Proxy Server |
| --------------------------------------------------------- | --------------------------------------------------------- | ----------------------------------------------------------------------------- | ------------ |
| **Windows Server 2025 with IIS 10.0 version 2.20.0**      | _64bit Windows Server 2025 v2.20.0 running IIS 10.0_      | .NET 9.0.9, supports 9.0.9, 8.0.20<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2025 with IIS 10.0 version 2.20.0** | _64bit Windows Server Core 2025 v2.20.0 running IIS 10.0_ | .NET 9.0.9, supports 9.0.9, 8.0.20<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2022 with IIS 10.0 version 2.20.0**      | _64bit Windows Server 2022 v2.20.0 running IIS 10.0_      | .NET 9.0.9, supports 9.0.9, 8.0.20<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2022 with IIS 10.0 version 2.20.0** | _64bit Windows Server Core 2022 v2.20.0 running IIS 10.0_ | .NET 9.0.9, supports 9.0.9, 8.0.20<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2019 with IIS 10.0 version 2.20.0**      | _64bit Windows Server 2019 v2.20.0 running IIS 10.0_      | .NET 9.0.9, supports 9.0.9, 8.0.20<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.20.0** | _64bit Windows Server Core 2019 v2.20.0 running IIS 10.0_ | .NET 9.0.9, supports 9.0.9, 8.0.20<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.20.0**      | _64bit Windows Server 2016 v2.20.0 running IIS 10.0_      | .NET 9.0.9, supports 9.0.9, 8.0.20<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.20.0** | _64bit Windows Server Core 2016 v2.20.0 running IIS 10.0_ | .NET 9.0.9, supports 9.0.9, 8.0.20<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |

### More details

| Platform Version                                          | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| --------------------------------------------------------- | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2025 with IIS 10.0 version 2.20.0**      | 2025.09.10  | 3.7.1120.0       |           | 3.3.3050.0 | 3.6        | 3.6.0     |
| **Windows Server Core 2025 with IIS 10.0 version 2.20.0** | 2025.09.10  | 3.7.1120.0       |           | 3.3.3050.0 | 3.6        | 3.6.0     |
| **Windows Server 2022 with IIS 10.0 version 2.20.0**      | 2025.09.10  | 3.7.1120.0       |           | 3.3.3050.0 | 3.6        | 3.6.0     |
| **Windows Server Core 2022 with IIS 10.0 version 2.20.0** | 2025.09.10  | 3.7.1120.0       |           | 3.3.3050.0 | 3.6        | 3.6.0     |
| **Windows Server 2019 with IIS 10.0 version 2.20.0**      | 2025.09.10  | 3.7.1120.0       |           | 3.3.3050.0 | 3.6        | 3.6.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.20.0** | 2025.09.10  | 3.7.1120.0       |           | 3.3.3050.0 | 3.6        | 3.6.0     |
| **Windows Server 2016 with IIS 10.0 version 2.20.0**      | 2025.09.10  | 3.7.1120.0       |           | 3.3.3050.0 | 3.6        | 3.6.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.20.0** | 2025.09.10  | 3.7.1120.0       |           | 3.3.3050.0 | 3.6        | 3.6.0     |

## August 19, 2025 – September 21, 2025

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between August 19, 2025 and September 21, 2025:

### Configuration basics

| Platform Version                                          | Solution Stack Name                                       | Framework                                                                     | Proxy Server |
| --------------------------------------------------------- | --------------------------------------------------------- | ----------------------------------------------------------------------------- | ------------ |
| **Windows Server 2025 with IIS 10.0 version 2.19.4**      | _64bit Windows Server 2025 v2.19.4 running IIS 10.0_      | .NET 9.0.8, supports 9.0.8, 8.0.19<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2025 with IIS 10.0 version 2.19.4** | _64bit Windows Server Core 2025 v2.19.4 running IIS 10.0_ | .NET 9.0.8, supports 9.0.8, 8.0.19<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2022 with IIS 10.0 version 2.19.4**      | _64bit Windows Server 2022 v2.19.4 running IIS 10.0_      | .NET 9.0.8, supports 9.0.8, 8.0.19<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2022 with IIS 10.0 version 2.19.4** | _64bit Windows Server Core 2022 v2.19.4 running IIS 10.0_ | .NET 9.0.8, supports 9.0.8, 8.0.19<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2019 with IIS 10.0 version 2.19.4**      | _64bit Windows Server 2019 v2.19.4 running IIS 10.0_      | .NET 9.0.8, supports 9.0.8, 8.0.19<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.19.4** | _64bit Windows Server Core 2019 v2.19.4 running IIS 10.0_ | .NET 9.0.8, supports 9.0.8, 8.0.19<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.19.4**      | _64bit Windows Server 2016 v2.19.4 running IIS 10.0_      | .NET 9.0.8, supports 9.0.8, 8.0.19<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.19.4** | _64bit Windows Server Core 2016 v2.19.4 running IIS 10.0_ | .NET 9.0.8, supports 9.0.8, 8.0.19<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |

### More details

| Platform Version                                          | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| --------------------------------------------------------- | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2025 with IIS 10.0 version 2.19.4**      | 2025.08.13  | 3.7.1101.0       |           | 3.3.2656.0 | 3.6        | 3.3.15    |
| **Windows Server Core 2025 with IIS 10.0 version 2.19.4** | 2025.08.13  | 3.7.1101.0       |           | 3.3.2656.0 | 3.6        | 3.3.15    |
| **Windows Server 2022 with IIS 10.0 version 2.19.4**      | 2025.08.13  | 3.7.1101.0       |           | 3.3.2656.0 | 3.6        | 3.3.15    |
| **Windows Server Core 2022 with IIS 10.0 version 2.19.4** | 2025.08.13  | 3.7.1101.0       |           | 3.3.2656.0 | 3.6        | 3.3.15    |
| **Windows Server 2019 with IIS 10.0 version 2.19.4**      | 2025.08.13  | 3.7.1101.0       |           | 3.3.2656.0 | 3.6        | 3.3.15    |
| **Windows Server Core 2019 with IIS 10.0 version 2.19.4** | 2025.08.13  | 3.7.1101.0       |           | 3.3.2656.0 | 3.6        | 3.3.15    |
| **Windows Server 2016 with IIS 10.0 version 2.19.4**      | 2025.08.13  | 3.7.1101.0       |           | 3.3.2656.0 | 3.6        | 3.3.15    |
| **Windows Server Core 2016 with IIS 10.0 version 2.19.4** | 2025.08.13  | 3.7.1101.0       |           | 3.3.2656.0 | 3.6        | 3.3.15    |

## July 17, 2025 – August 18, 2025

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between July 17, 2025 and August 18, 2025:

### Configuration basics

| Platform Version                                          | Solution Stack Name                                       | Framework                                                                     | Proxy Server |
| --------------------------------------------------------- | --------------------------------------------------------- | ----------------------------------------------------------------------------- | ------------ |
| **Windows Server 2025 with IIS 10.0 version 2.19.3**      | _64bit Windows Server 2025 v2.19.3 running IIS 10.0_      | .NET 9.0.7, supports 9.0.7, 8.0.18<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2025 with IIS 10.0 version 2.19.3** | _64bit Windows Server Core 2025 v2.19.3 running IIS 10.0_ | .NET 9.0.7, supports 9.0.7, 8.0.18<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2022 with IIS 10.0 version 2.19.3**      | _64bit Windows Server 2022 v2.19.3 running IIS 10.0_      | .NET 9.0.7, supports 9.0.7, 8.0.18<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2022 with IIS 10.0 version 2.19.3** | _64bit Windows Server Core 2022 v2.19.3 running IIS 10.0_ | .NET 9.0.7, supports 9.0.7, 8.0.18<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2019 with IIS 10.0 version 2.19.3**      | _64bit Windows Server 2019 v2.19.3 running IIS 10.0_      | .NET 9.0.7, supports 9.0.7, 8.0.18<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.19.3** | _64bit Windows Server Core 2019 v2.19.3 running IIS 10.0_ | .NET 9.0.7, supports 9.0.7, 8.0.18<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.19.3**      | _64bit Windows Server 2016 v2.19.3 running IIS 10.0_      | .NET 9.0.7, supports 9.0.7, 8.0.18<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.19.3** | _64bit Windows Server Core 2016 v2.19.3 running IIS 10.0_ | .NET 9.0.7, supports 9.0.7, 8.0.18<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |

### More details

| Platform Version                                          | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| --------------------------------------------------------- | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2025 with IIS 10.0 version 2.19.3**      | 2025.07.09  | 3.7.1077.0       |           | 3.3.2471.0 | 3.6        | 3.3.15    |
| **Windows Server Core 2025 with IIS 10.0 version 2.19.3** | 2025.07.09  | 3.7.1077.0       |           | 3.3.2471.0 | 3.6        | 3.3.15    |
| **Windows Server 2022 with IIS 10.0 version 2.19.3**      | 2025.07.09  | 3.7.1077.0       |           | 3.3.2471.0 | 3.6        | 3.3.15    |
| **Windows Server Core 2022 with IIS 10.0 version 2.19.3** | 2025.07.09  | 3.7.1077.0       |           | 3.3.2471.0 | 3.6        | 3.3.15    |
| **Windows Server 2019 with IIS 10.0 version 2.19.3**      | 2025.07.09  | 3.7.1077.0       |           | 3.3.2471.0 | 3.6        | 3.3.15    |
| **Windows Server Core 2019 with IIS 10.0 version 2.19.3** | 2025.07.09  | 3.7.1077.0       |           | 3.3.2471.0 | 3.6        | 3.3.15    |
| **Windows Server 2016 with IIS 10.0 version 2.19.3**      | 2025.07.09  | 3.7.1077.0       |           | 3.3.2471.0 | 3.6        | 3.3.15    |
| **Windows Server Core 2016 with IIS 10.0 version 2.19.3** | 2025.07.09  | 3.7.1077.0       |           | 3.3.2471.0 | 3.6        | 3.3.15    |

## June 19, 2025 – July 16, 2025

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between June 19, 2025 and July 16, 2025:

### Configuration basics

| Platform Version                                          | Solution Stack Name                                       | Framework                                                                     | Proxy Server |
| --------------------------------------------------------- | --------------------------------------------------------- | ----------------------------------------------------------------------------- | ------------ |
| **Windows Server 2025 with IIS 10.0 version 2.19.2**      | _64bit Windows Server 2025 v2.19.2 running IIS 10.0_      | .NET 9.0.6, supports 9.0.6, 8.0.17<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2025 with IIS 10.0 version 2.19.2** | _64bit Windows Server Core 2025 v2.19.2 running IIS 10.0_ | .NET 9.0.6, supports 9.0.6, 8.0.17<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2022 with IIS 10.0 version 2.19.2**      | _64bit Windows Server 2022 v2.19.2 running IIS 10.0_      | .NET 9.0.6, supports 9.0.6, 8.0.17<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2022 with IIS 10.0 version 2.19.2** | _64bit Windows Server Core 2022 v2.19.2 running IIS 10.0_ | .NET 9.0.6, supports 9.0.6, 8.0.17<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2019 with IIS 10.0 version 2.19.2**      | _64bit Windows Server 2019 v2.19.2 running IIS 10.0_      | .NET 9.0.6, supports 9.0.6, 8.0.17<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.19.2** | _64bit Windows Server Core 2019 v2.19.2 running IIS 10.0_ | .NET 9.0.6, supports 9.0.6, 8.0.17<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.19.2**      | _64bit Windows Server 2016 v2.19.2 running IIS 10.0_      | .NET 9.0.6, supports 9.0.6, 8.0.17<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.19.2** | _64bit Windows Server Core 2016 v2.19.2 running IIS 10.0_ | .NET 9.0.6, supports 9.0.6, 8.0.17<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |

### More details

| Platform Version                                          | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| --------------------------------------------------------- | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2025 with IIS 10.0 version 2.19.2**      | 2025.06.11  | 3.7.1062.0       |           | 3.3.2299.0 | 3.6        | 3.3.14    |
| **Windows Server Core 2025 with IIS 10.0 version 2.19.2** | 2025.06.11  | 3.7.1062.0       |           | 3.3.2299.0 | 3.6        | 3.3.14    |
| **Windows Server 2022 with IIS 10.0 version 2.19.2**      | 2025.06.11  | 3.7.1062.0       |           | 3.3.2299.0 | 3.6        | 3.3.14    |
| **Windows Server Core 2022 with IIS 10.0 version 2.19.2** | 2025.06.11  | 3.7.1062.0       |           | 3.3.2299.0 | 3.6        | 3.3.14    |
| **Windows Server 2019 with IIS 10.0 version 2.19.2**      | 2025.06.11  | 3.7.1062.0       |           | 3.3.2299.0 | 3.6        | 3.3.14    |
| **Windows Server Core 2019 with IIS 10.0 version 2.19.2** | 2025.06.11  | 3.7.1062.0       |           | 3.3.2299.0 | 3.6        | 3.3.14    |
| **Windows Server 2016 with IIS 10.0 version 2.19.2**      | 2025.06.11  | 3.7.1062.0       |           | 3.3.2299.0 | 3.6        | 3.3.14    |
| **Windows Server Core 2016 with IIS 10.0 version 2.19.2** | 2025.06.11  | 3.7.1062.0       |           | 3.3.2299.0 | 3.6        | 3.3.14    |

## May 20, 2025 – June 18, 2025

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between May 20, 2025 and June 18, 2025:

### Configuration basics

| Platform Version                                          | Solution Stack Name                                       | Framework                                                                     | Proxy Server |
| --------------------------------------------------------- | --------------------------------------------------------- | ----------------------------------------------------------------------------- | ------------ |
| **Windows Server 2025 with IIS 10.0 version 2.19.1**      | _64bit Windows Server 2025 v2.19.1 running IIS 10.0_      | .NET 9.0.5, supports 9.0.5, 8.0.16<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2025 with IIS 10.0 version 2.19.1** | _64bit Windows Server Core 2025 v2.19.1 running IIS 10.0_ | .NET 9.0.5, supports 9.0.5, 8.0.16<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2022 with IIS 10.0 version 2.19.1**      | _64bit Windows Server 2022 v2.19.1 running IIS 10.0_      | .NET 9.0.5, supports 9.0.5, 8.0.16<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2022 with IIS 10.0 version 2.19.1** | _64bit Windows Server Core 2022 v2.19.1 running IIS 10.0_ | .NET 9.0.5, supports 9.0.5, 8.0.16<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2019 with IIS 10.0 version 2.19.1**      | _64bit Windows Server 2019 v2.19.1 running IIS 10.0_      | .NET 9.0.5, supports 9.0.5, 8.0.16<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.19.1** | _64bit Windows Server Core 2019 v2.19.1 running IIS 10.0_ | .NET 9.0.5, supports 9.0.5, 8.0.16<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.19.1**      | _64bit Windows Server 2016 v2.19.1 running IIS 10.0_      | .NET 9.0.5, supports 9.0.5, 8.0.16<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.19.1** | _64bit Windows Server Core 2016 v2.19.1 running IIS 10.0_ | .NET 9.0.5, supports 9.0.5, 8.0.16<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |

### More details

| Platform Version                                          | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| --------------------------------------------------------- | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2025 with IIS 10.0 version 2.19.1**      | 2025.05.15  | 3.7.1044.0       |           | 3.3.2299.0 | 3.6        | 3.3.14    |
| **Windows Server Core 2025 with IIS 10.0 version 2.19.1** | 2025.05.15  | 3.7.1044.0       |           | 3.3.2299.0 | 3.6        | 3.3.14    |
| **Windows Server 2022 with IIS 10.0 version 2.19.1**      | 2025.05.15  | 3.7.1044.0       |           | 3.3.2299.0 | 3.6        | 3.3.14    |
| **Windows Server Core 2022 with IIS 10.0 version 2.19.1** | 2025.05.15  | 3.7.1044.0       |           | 3.3.2299.0 | 3.6        | 3.3.14    |
| **Windows Server 2019 with IIS 10.0 version 2.19.1**      | 2025.05.15  | 3.7.1044.0       |           | 3.3.2299.0 | 3.6        | 3.3.14    |
| **Windows Server Core 2019 with IIS 10.0 version 2.19.1** | 2025.05.15  | 3.7.1044.0       |           | 3.3.2299.0 | 3.6        | 3.3.14    |
| **Windows Server 2016 with IIS 10.0 version 2.19.1**      | 2025.05.15  | 3.7.1044.0       |           | 3.3.2299.0 | 3.6        | 3.3.14    |
| **Windows Server Core 2016 with IIS 10.0 version 2.19.1** | 2025.05.15  | 3.7.1044.0       |           | 3.3.2299.0 | 3.6        | 3.3.14    |

## April 17, 2025 – May 19, 2025

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between April 17, 2025 and May 19, 2025:

### Configuration basics

| Platform Version                                          | Solution Stack Name                                       | Framework                                                               | Proxy Server |
| --------------------------------------------------------- | --------------------------------------------------------- | ----------------------------------------------------------------------- | ------------ |
| **Windows Server 2025 with IIS 10.0 version 2.19.0**      | _64bit Windows Server 2025 v2.19.0 running IIS 10.0_      | .NET 8.0.15, supports 8.0.15<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2025 with IIS 10.0 version 2.19.0** | _64bit Windows Server Core 2025 v2.19.0 running IIS 10.0_ | .NET 8.0.15, supports 8.0.15<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2022 with IIS 10.0 version 2.19.0**      | _64bit Windows Server 2022 v2.19.0 running IIS 10.0_      | .NET 8.0.15, supports 8.0.15<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2022 with IIS 10.0 version 2.19.0** | _64bit Windows Server Core 2022 v2.19.0 running IIS 10.0_ | .NET 8.0.15, supports 8.0.15<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2019 with IIS 10.0 version 2.19.0**      | _64bit Windows Server 2019 v2.19.0 running IIS 10.0_      | .NET 8.0.15, supports 8.0.15<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.19.0** | _64bit Windows Server Core 2019 v2.19.0 running IIS 10.0_ | .NET 8.0.15, supports 8.0.15<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.19.0**      | _64bit Windows Server 2016 v2.19.0 running IIS 10.0_      | .NET 8.0.15, supports 8.0.15<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.19.0** | _64bit Windows Server Core 2016 v2.19.0 running IIS 10.0_ | .NET 8.0.15, supports 8.0.15<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |

### More details

| Platform Version                                          | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| --------------------------------------------------------- | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2025 with IIS 10.0 version 2.19.0**      | 2025.04.09  | 3.7.1020.0       |           | 3.3.1957.0 | 3.6        | 3.3.14    |
| **Windows Server Core 2025 with IIS 10.0 version 2.19.0** | 2025.04.09  | 3.7.1020.0       |           | 3.3.1957.0 | 3.6        | 3.3.14    |
| **Windows Server 2022 with IIS 10.0 version 2.19.0**      | 2025.04.09  | 3.7.1020.0       |           | 3.3.1957.0 | 3.6        | 3.3.14    |
| **Windows Server Core 2022 with IIS 10.0 version 2.19.0** | 2025.04.09  | 3.7.1020.0       |           | 3.3.1957.0 | 3.6        | 3.3.14    |
| **Windows Server 2019 with IIS 10.0 version 2.19.0**      | 2025.04.09  | 3.7.1020.0       |           | 3.3.1957.0 | 3.6        | 3.3.14    |
| **Windows Server Core 2019 with IIS 10.0 version 2.19.0** | 2025.04.09  | 3.7.1020.0       |           | 3.3.1957.0 | 3.6        | 3.3.14    |
| **Windows Server 2016 with IIS 10.0 version 2.19.0**      | 2025.04.09  | 3.7.1020.0       |           | 3.3.1957.0 | 3.6        | 3.3.14    |
| **Windows Server Core 2016 with IIS 10.0 version 2.19.0** | 2025.04.09  | 3.7.1020.0       |           | 3.3.1957.0 | 3.6        | 3.3.14    |

## March 26, 2025 – April 16, 2025

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between March 26, 2025 and April 16, 2025:

### Configuration basics

| Platform Version                                          | Solution Stack Name                                       | Framework                                                                       | Proxy Server |
| --------------------------------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2025 with IIS 10.0 version 2.18.0**      | _64bit Windows Server 2025 v2.18.0 running IIS 10.0_      | .NET 8.0.14, supports 8.0.14, 6.0.36<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2025 with IIS 10.0 version 2.18.0** | _64bit Windows Server Core 2025 v2.18.0 running IIS 10.0_ | .NET 8.0.14, supports 8.0.14, 6.0.36<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2022 with IIS 10.0 version 2.18.0**      | _64bit Windows Server 2022 v2.18.0 running IIS 10.0_      | .NET 8.0.14, supports 8.0.14, 6.0.36<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2022 with IIS 10.0 version 2.18.0** | _64bit Windows Server Core 2022 v2.18.0 running IIS 10.0_ | .NET 8.0.14, supports 8.0.14, 6.0.36<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2019 with IIS 10.0 version 2.18.0**      | _64bit Windows Server 2019 v2.18.0 running IIS 10.0_      | .NET 8.0.14, supports 8.0.14, 6.0.36<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.18.0** | _64bit Windows Server Core 2019 v2.18.0 running IIS 10.0_ | .NET 8.0.14, supports 8.0.14, 6.0.36<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.18.0**      | _64bit Windows Server 2016 v2.18.0 running IIS 10.0_      | .NET 8.0.14, supports 8.0.14, 6.0.36<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.18.0** | _64bit Windows Server Core 2016 v2.18.0 running IIS 10.0_ | .NET 8.0.14, supports 8.0.14, 6.0.36<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |

### More details

| Platform Version                                          | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| --------------------------------------------------------- | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2025 with IIS 10.0 version 2.18.0**      | 2025.03.12  | 3.7.1000.0       |           | 3.3.1611.0 | 3.6        | 3.3.14    |
| **Windows Server Core 2025 with IIS 10.0 version 2.18.0** | 2025.03.12  | 3.7.1000.0       |           | 3.3.1611.0 | 3.6        | 3.3.14    |
| **Windows Server 2022 with IIS 10.0 version 2.18.0**      | 2025.03.12  | 3.7.1000.0       |           | 3.3.1611.0 | 3.6        | 3.3.14    |
| **Windows Server Core 2022 with IIS 10.0 version 2.18.0** | 2025.03.12  | 3.7.1000.0       |           | 3.3.1611.0 | 3.6        | 3.3.14    |
| **Windows Server 2019 with IIS 10.0 version 2.18.0**      | 2025.03.12  | 3.7.1000.0       |           | 3.3.1611.0 | 3.6        | 3.3.14    |
| **Windows Server Core 2019 with IIS 10.0 version 2.18.0** | 2025.03.12  | 3.7.1000.0       |           | 3.3.1611.0 | 3.6        | 3.3.14    |
| **Windows Server 2016 with IIS 10.0 version 2.18.0**      | 2025.03.12  | 3.7.1000.0       |           | 3.3.1611.0 | 3.6        | 3.3.14    |
| **Windows Server Core 2016 with IIS 10.0 version 2.18.0** | 2025.03.12  | 3.7.1000.0       |           | 3.3.1611.0 | 3.6        | 3.3.14    |

## February 19, 2025 – March 25, 2025

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between February 19, 2025 and March 25, 2025:

### Configuration basics

| Platform Version                                          | Solution Stack Name                                       | Framework                                                                       | Proxy Server |
| --------------------------------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2025 with IIS 10.0 version 2.17.0**      | _64bit Windows Server 2025 v2.17.0 running IIS 10.0_      | .NET 8.0.13, supports 8.0.13, 6.0.36<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2025 with IIS 10.0 version 2.17.0** | _64bit Windows Server Core 2025 v2.17.0 running IIS 10.0_ | .NET 8.0.13, supports 8.0.13, 6.0.36<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2022 with IIS 10.0 version 2.17.0**      | _64bit Windows Server 2022 v2.17.0 running IIS 10.0_      | .NET 8.0.13, supports 8.0.13, 6.0.36<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2022 with IIS 10.0 version 2.17.0** | _64bit Windows Server Core 2022 v2.17.0 running IIS 10.0_ | .NET 8.0.13, supports 8.0.13, 6.0.36<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2019 with IIS 10.0 version 2.17.0**      | _64bit Windows Server 2019 v2.17.0 running IIS 10.0_      | .NET 8.0.13, supports 8.0.13, 6.0.36<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.17.0** | _64bit Windows Server Core 2019 v2.17.0 running IIS 10.0_ | .NET 8.0.13, supports 8.0.13, 6.0.36<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.17.0**      | _64bit Windows Server 2016 v2.17.0 running IIS 10.0_      | .NET 8.0.13, supports 8.0.13, 6.0.36<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.17.0** | _64bit Windows Server Core 2016 v2.17.0 running IIS 10.0_ | .NET 8.0.13, supports 8.0.13, 6.0.36<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |

### More details

| Platform Version                                          | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| --------------------------------------------------------- | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2025 with IIS 10.0 version 2.17.0**      | 2025.02.13  | 3.7.981.0        |           | 3.3.1611.0 | 3.6        | 3.3.13    |
| **Windows Server Core 2025 with IIS 10.0 version 2.17.0** | 2025.02.13  | 3.7.981.0        |           | 3.3.1611.0 | 3.6        | 3.3.13    |
| **Windows Server 2022 with IIS 10.0 version 2.17.0**      | 2025.02.13  | 3.7.981.0        |           | 3.3.1611.0 | 3.6        | 3.3.13    |
| **Windows Server Core 2022 with IIS 10.0 version 2.17.0** | 2025.02.13  | 3.7.981.0        |           | 3.3.1611.0 | 3.6        | 3.3.13    |
| **Windows Server 2019 with IIS 10.0 version 2.17.0**      | 2025.02.13  | 3.7.981.0        |           | 3.3.1611.0 | 3.6        | 3.3.13    |
| **Windows Server Core 2019 with IIS 10.0 version 2.17.0** | 2025.02.13  | 3.7.981.0        |           | 3.3.1611.0 | 3.6        | 3.3.13    |
| **Windows Server 2016 with IIS 10.0 version 2.17.0**      | 2025.02.13  | 3.7.981.0        |           | 3.3.1611.0 | 3.6        | 3.3.13    |
| **Windows Server Core 2016 with IIS 10.0 version 2.17.0** | 2025.02.13  | 3.7.981.0        |           | 3.3.1611.0 | 3.6        | 3.3.13    |

## January 22, 2025 – February 18, 2025

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between January 22, 2025 and February 18, 2025:

### Configuration basics

| Platform Version                                          | Solution Stack Name                                       | Framework                                                                       | Proxy Server |
| --------------------------------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2022 with IIS 10.0 version 2.16.2**      | _64bit Windows Server 2022 v2.16.2 running IIS 10.0_      | .NET 8.0.12, supports 8.0.12, 6.0.36<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2022 with IIS 10.0 version 2.16.2** | _64bit Windows Server Core 2022 v2.16.2 running IIS 10.0_ | .NET 8.0.12, supports 8.0.12, 6.0.36<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2019 with IIS 10.0 version 2.16.2**      | _64bit Windows Server 2019 v2.16.2 running IIS 10.0_      | .NET 8.0.12, supports 8.0.12, 6.0.36<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.16.2** | _64bit Windows Server Core 2019 v2.16.2 running IIS 10.0_ | .NET 8.0.12, supports 8.0.12, 6.0.36<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.16.2**      | _64bit Windows Server 2016 v2.16.2 running IIS 10.0_      | .NET 8.0.12, supports 8.0.12, 6.0.36<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.16.2** | _64bit Windows Server Core 2016 v2.16.2 running IIS 10.0_ | .NET 8.0.12, supports 8.0.12, 6.0.36<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |

### More details

| Platform Version                                          | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| --------------------------------------------------------- | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2022 with IIS 10.0 version 2.16.2**      | 2025.01.15  | 3.7.962.0        |           | 3.3.1345.0 | 3.6        | 3.3.13    |
| **Windows Server Core 2022 with IIS 10.0 version 2.16.2** | 2025.01.15  | 3.7.962.0        |           | 3.3.1345.0 | 3.6        | 3.3.13    |
| **Windows Server 2019 with IIS 10.0 version 2.16.2**      | 2025.01.15  | 3.7.962.0        |           | 3.3.1345.0 | 3.6        | 3.3.13    |
| **Windows Server Core 2019 with IIS 10.0 version 2.16.2** | 2025.01.15  | 3.7.962.0        |           | 3.3.1345.0 | 3.6        | 3.3.13    |
| **Windows Server 2016 with IIS 10.0 version 2.16.2**      | 2025.01.15  | 3.7.962.0        |           | 3.3.1345.0 | 3.6        | 3.3.13    |
| **Windows Server Core 2016 with IIS 10.0 version 2.16.2** | 2025.01.15  | 3.7.962.0        |           | 3.3.1345.0 | 3.6        | 3.3.13    |

## December 19, 2024 – January 21, 2025

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between December 19, 2024 and January 21, 2025:

### Configuration basics

| Platform Version                                          | Solution Stack Name                                       | Framework                                                                       | Proxy Server |
| --------------------------------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2022 with IIS 10.0 version 2.16.1**      | _64bit Windows Server 2022 v2.16.1 running IIS 10.0_      | .NET 8.0.11, supports 8.0.11, 6.0.36<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2022 with IIS 10.0 version 2.16.1** | _64bit Windows Server Core 2022 v2.16.1 running IIS 10.0_ | .NET 8.0.11, supports 8.0.11, 6.0.36<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2019 with IIS 10.0 version 2.16.1**      | _64bit Windows Server 2019 v2.16.1 running IIS 10.0_      | .NET 8.0.11, supports 8.0.11, 6.0.36<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.16.1** | _64bit Windows Server Core 2019 v2.16.1 running IIS 10.0_ | .NET 8.0.11, supports 8.0.11, 6.0.36<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.16.1**      | _64bit Windows Server 2016 v2.16.1 running IIS 10.0_      | .NET 8.0.11, supports 8.0.11, 6.0.36<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.16.1** | _64bit Windows Server Core 2016 v2.16.1 running IIS 10.0_ | .NET 8.0.11, supports 8.0.11, 6.0.36<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |

### More details

| Platform Version                                          | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| --------------------------------------------------------- | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2022 with IIS 10.0 version 2.16.1**      | 2024.12.13  | 3.7.945.0        |           | 3.3.1345.0 | 3.6        | 3.3.13    |
| **Windows Server Core 2022 with IIS 10.0 version 2.16.1** | 2024.12.13  | 3.7.945.0        |           | 3.3.1345.0 | 3.6        | 3.3.13    |
| **Windows Server 2019 with IIS 10.0 version 2.16.1**      | 2024.12.13  | 3.7.945.0        |           | 3.3.1345.0 | 3.6        | 3.3.13    |
| **Windows Server Core 2019 with IIS 10.0 version 2.16.1** | 2024.12.13  | 3.7.945.0        |           | 3.3.1345.0 | 3.6        | 3.3.13    |
| **Windows Server 2016 with IIS 10.0 version 2.16.1**      | 2024.12.13  | 3.7.945.0        |           | 3.3.1345.0 | 3.6        | 3.3.13    |
| **Windows Server Core 2016 with IIS 10.0 version 2.16.1** | 2024.12.13  | 3.7.945.0        |           | 3.3.1345.0 | 3.6        | 3.3.13    |

## November 20, 2024 – December 18, 2024

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between November 20, 2024 and December 18, 2024:

### Configuration basics

| Platform Version                                          | Solution Stack Name                                       | Framework                                                                       | Proxy Server |
| --------------------------------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2022 with IIS 10.0 version 2.16.0**      | _64bit Windows Server 2022 v2.16.0 running IIS 10.0_      | .NET 8.0.11, supports 8.0.11, 6.0.36<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2022 with IIS 10.0 version 2.16.0** | _64bit Windows Server Core 2022 v2.16.0 running IIS 10.0_ | .NET 8.0.11, supports 8.0.11, 6.0.36<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2019 with IIS 10.0 version 2.16.0**      | _64bit Windows Server 2019 v2.16.0 running IIS 10.0_      | .NET 8.0.11, supports 8.0.11, 6.0.36<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.16.0** | _64bit Windows Server Core 2019 v2.16.0 running IIS 10.0_ | .NET 8.0.11, supports 8.0.11, 6.0.36<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.16.0**      | _64bit Windows Server 2016 v2.16.0 running IIS 10.0_      | .NET 8.0.11, supports 8.0.11, 6.0.36<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.16.0** | _64bit Windows Server Core 2016 v2.16.0 running IIS 10.0_ | .NET 8.0.11, supports 8.0.11, 6.0.36<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |

### More details

| Platform Version                                          | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| --------------------------------------------------------- | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2022 with IIS 10.0 version 2.16.0**      | 2024.11.13  | 3.7.925.0        |           | 3.3.1230.0 | 3.6        | 3.3.13    |
| **Windows Server Core 2022 with IIS 10.0 version 2.16.0** | 2024.11.13  | 3.7.925.0        |           | 3.3.1230.0 | 3.6        | 3.3.13    |
| **Windows Server 2019 with IIS 10.0 version 2.16.0**      | 2024.11.13  | 3.7.925.0        |           | 3.3.1230.0 | 3.6        | 3.3.13    |
| **Windows Server Core 2019 with IIS 10.0 version 2.16.0** | 2024.11.13  | 3.7.925.0        |           | 3.3.1230.0 | 3.6        | 3.3.13    |
| **Windows Server 2016 with IIS 10.0 version 2.16.0**      | 2024.11.13  | 3.7.925.0        |           | 3.3.1230.0 | 3.6        | 3.3.13    |
| **Windows Server Core 2016 with IIS 10.0 version 2.16.0** | 2024.11.13  | 3.7.925.0        |           | 3.3.1230.0 | 3.6        | 3.3.13    |

## October 16, 2024 – November 19, 2024

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between October 16, 2024 and November 19, 2024:

### Configuration basics

| Platform Version                                          | Solution Stack Name                                       | Framework                                                                       | Proxy Server |
| --------------------------------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2022 with IIS 10.0 version 2.15.6**      | _64bit Windows Server 2022 v2.15.6 running IIS 10.0_      | .NET 8.0.10, supports 8.0.10, 6.0.35<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2022 with IIS 10.0 version 2.15.6** | _64bit Windows Server Core 2022 v2.15.6 running IIS 10.0_ | .NET 8.0.10, supports 8.0.10, 6.0.35<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2019 with IIS 10.0 version 2.15.6**      | _64bit Windows Server 2019 v2.15.6 running IIS 10.0_      | .NET 8.0.10, supports 8.0.10, 6.0.35<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.15.6** | _64bit Windows Server Core 2019 v2.15.6 running IIS 10.0_ | .NET 8.0.10, supports 8.0.10, 6.0.35<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.15.6**      | _64bit Windows Server 2016 v2.15.6 running IIS 10.0_      | .NET 8.0.10, supports 8.0.10, 6.0.35<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.15.6** | _64bit Windows Server Core 2016 v2.15.6 running IIS 10.0_ | .NET 8.0.10, supports 8.0.10, 6.0.35<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |

### More details

| Platform Version                                          | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X-Ray |
| --------------------------------------------------------- | ----------- | ---------------- | --------- | --------- | ---------- | --------- |
| **Windows Server 2022 with IIS 10.0 version 2.15.6**      | 2024.10.09  | 3.7.901.0        |           | 3.3.859.0 | 3.6        | 3.3.13    |
| **Windows Server Core 2022 with IIS 10.0 version 2.15.6** | 2024.10.09  | 3.7.901.0        |           | 3.3.859.0 | 3.6        | 3.3.13    |
| **Windows Server 2019 with IIS 10.0 version 2.15.6**      | 2024.10.09  | 3.7.901.0        |           | 3.3.859.0 | 3.6        | 3.3.13    |
| **Windows Server Core 2019 with IIS 10.0 version 2.15.6** | 2024.10.09  | 3.7.901.0        |           | 3.3.859.0 | 3.6        | 3.3.13    |
| **Windows Server 2016 with IIS 10.0 version 2.15.6**      | 2024.10.09  | 3.7.901.0        |           | 3.3.859.0 | 3.6        | 3.3.13    |
| **Windows Server Core 2016 with IIS 10.0 version 2.15.6** | 2024.10.09  | 3.7.901.0        |           | 3.3.859.0 | 3.6        | 3.3.13    |

## September 19, 2024 – October 15, 2024

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between September 19, 2024 and October 15, 2024:

### Configuration basics

| Platform Version                                          | Solution Stack Name                                       | Framework                                                                     | Proxy Server |
| --------------------------------------------------------- | --------------------------------------------------------- | ----------------------------------------------------------------------------- | ------------ |
| **Windows Server 2022 with IIS 10.0 version 2.15.5**      | _64bit Windows Server 2022 v2.15.5 running IIS 10.0_      | .NET 8.0.8, supports 8.0.8, 6.0.33<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2022 with IIS 10.0 version 2.15.5** | _64bit Windows Server Core 2022 v2.15.5 running IIS 10.0_ | .NET 8.0.8, supports 8.0.8, 6.0.33<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2019 with IIS 10.0 version 2.15.5**      | _64bit Windows Server 2019 v2.15.5 running IIS 10.0_      | .NET 8.0.8, supports 8.0.8, 6.0.33<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.15.5** | _64bit Windows Server Core 2019 v2.15.5 running IIS 10.0_ | .NET 8.0.8, supports 8.0.8, 6.0.33<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.15.5**      | _64bit Windows Server 2016 v2.15.5 running IIS 10.0_      | .NET 8.0.8, supports 8.0.8, 6.0.33<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.15.5** | _64bit Windows Server Core 2016 v2.15.5 running IIS 10.0_ | .NET 8.0.8, supports 8.0.8, 6.0.33<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |

### More details

| Platform Version                                          | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X-Ray |
| --------------------------------------------------------- | ----------- | ---------------- | --------- | --------- | ---------- | --------- |
| **Windows Server 2022 with IIS 10.0 version 2.15.5**      | 2024.09.11  | 3.7.883.0        |           | 3.3.551.0 | 3.6        | 3.3.13    |
| **Windows Server Core 2022 with IIS 10.0 version 2.15.5** | 2024.09.11  | 3.7.883.0        |           | 3.3.551.0 | 3.6        | 3.3.13    |
| **Windows Server 2019 with IIS 10.0 version 2.15.5**      | 2024.09.11  | 3.7.883.0        |           | 3.3.551.0 | 3.6        | 3.3.13    |
| **Windows Server Core 2019 with IIS 10.0 version 2.15.5** | 2024.09.11  | 3.7.883.0        |           | 3.3.551.0 | 3.6        | 3.3.13    |
| **Windows Server 2016 with IIS 10.0 version 2.15.5**      | 2024.09.11  | 3.7.883.0        |           | 3.3.551.0 | 3.6        | 3.3.13    |
| **Windows Server Core 2016 with IIS 10.0 version 2.15.5** | 2024.09.11  | 3.7.883.0        |           | 3.3.551.0 | 3.6        | 3.3.13    |

## August 20, 2024 – September 18, 2024

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between August 20, 2024 and September 18, 2024:

### Configuration basics

| Platform Version                                          | Solution Stack Name                                       | Framework                                                                     | Proxy Server |
| --------------------------------------------------------- | --------------------------------------------------------- | ----------------------------------------------------------------------------- | ------------ |
| **Windows Server 2022 with IIS 10.0 version 2.15.4**      | _64bit Windows Server 2022 v2.15.4 running IIS 10.0_      | .NET 8.0.8, supports 8.0.8, 6.0.33<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2022 with IIS 10.0 version 2.15.4** | _64bit Windows Server Core 2022 v2.15.4 running IIS 10.0_ | .NET 8.0.8, supports 8.0.8, 6.0.33<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2019 with IIS 10.0 version 2.15.4**      | _64bit Windows Server 2019 v2.15.4 running IIS 10.0_      | .NET 8.0.8, supports 8.0.8, 6.0.33<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.15.4** | _64bit Windows Server Core 2019 v2.15.4 running IIS 10.0_ | .NET 8.0.8, supports 8.0.8, 6.0.33<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.15.4**      | _64bit Windows Server 2016 v2.15.4 running IIS 10.0_      | .NET 8.0.8, supports 8.0.8, 6.0.33<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.15.4** | _64bit Windows Server Core 2016 v2.15.4 running IIS 10.0_ | .NET 8.0.8, supports 8.0.8, 6.0.33<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |

### More details

| Platform Version                                          | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X-Ray |
| --------------------------------------------------------- | ----------- | ---------------- | --------- | --------- | ---------- | --------- |
| **Windows Server 2022 with IIS 10.0 version 2.15.4**      | 2024.08.14  | 3.7.864.0        |           | 3.3.551.0 | 3.6        | 3.3.13    |
| **Windows Server Core 2022 with IIS 10.0 version 2.15.4** | 2024.08.14  | 3.7.864.0        |           | 3.3.551.0 | 3.6        | 3.3.13    |
| **Windows Server 2019 with IIS 10.0 version 2.15.4**      | 2024.08.14  | 3.7.864.0        |           | 3.3.551.0 | 3.6        | 3.3.13    |
| **Windows Server Core 2019 with IIS 10.0 version 2.15.4** | 2024.08.14  | 3.7.864.0        |           | 3.3.551.0 | 3.6        | 3.3.13    |
| **Windows Server 2016 with IIS 10.0 version 2.15.4**      | 2024.08.14  | 3.7.864.0        |           | 3.3.551.0 | 3.6        | 3.3.13    |
| **Windows Server Core 2016 with IIS 10.0 version 2.15.4** | 2024.08.14  | 3.7.864.0        |           | 3.3.551.0 | 3.6        | 3.3.13    |

## July 18, 2024 – August 19, 2024

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between July 18, 2024 and August 19, 2024:

### Configuration basics

| Platform Version                                          | Solution Stack Name                                       | Framework                                                                     | Proxy Server |
| --------------------------------------------------------- | --------------------------------------------------------- | ----------------------------------------------------------------------------- | ------------ |
| **Windows Server 2022 with IIS 10.0 version 2.15.3**      | _64bit Windows Server 2022 v2.15.3 running IIS 10.0_      | .NET 8.0.7, supports 8.0.7, 6.0.32<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2022 with IIS 10.0 version 2.15.3** | _64bit Windows Server Core 2022 v2.15.3 running IIS 10.0_ | .NET 8.0.7, supports 8.0.7, 6.0.32<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2019 with IIS 10.0 version 2.15.3**      | _64bit Windows Server 2019 v2.15.3 running IIS 10.0_      | .NET 8.0.7, supports 8.0.7, 6.0.32<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.15.3** | _64bit Windows Server Core 2019 v2.15.3 running IIS 10.0_ | .NET 8.0.7, supports 8.0.7, 6.0.32<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.15.3**      | _64bit Windows Server 2016 v2.15.3 running IIS 10.0_      | .NET 8.0.7, supports 8.0.7, 6.0.32<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.15.3** | _64bit Windows Server Core 2016 v2.15.3 running IIS 10.0_ | .NET 8.0.7, supports 8.0.7, 6.0.32<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |

### More details

| Platform Version                                          | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X-Ray |
| --------------------------------------------------------- | ----------- | ---------------- | --------- | --------- | ---------- | --------- |
| **Windows Server 2022 with IIS 10.0 version 2.15.3**      | 2024.07.10  | 3.7.847.0        |           | 3.3.551.0 | 3.6        | 3.3.12    |
| **Windows Server Core 2022 with IIS 10.0 version 2.15.3** | 2024.07.10  | 3.7.847.0        |           | 3.3.551.0 | 3.6        | 3.3.12    |
| **Windows Server 2019 with IIS 10.0 version 2.15.3**      | 2024.07.10  | 3.7.847.0        |           | 3.3.551.0 | 3.6        | 3.3.12    |
| **Windows Server Core 2019 with IIS 10.0 version 2.15.3** | 2024.07.10  | 3.7.847.0        |           | 3.3.551.0 | 3.6        | 3.3.12    |
| **Windows Server 2016 with IIS 10.0 version 2.15.3**      | 2024.07.10  | 3.7.847.0        |           | 3.3.551.0 | 3.6        | 3.3.12    |
| **Windows Server Core 2016 with IIS 10.0 version 2.15.3** | 2024.07.10  | 3.7.847.0        |           | 3.3.551.0 | 3.6        | 3.3.12    |

## June 18, 2024 – July 17, 2024

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between June 18, 2024 and July 17, 2024:

### Configuration basics

| Platform Version                                          | Solution Stack Name                                       | Framework                                                                     | Proxy Server |
| --------------------------------------------------------- | --------------------------------------------------------- | ----------------------------------------------------------------------------- | ------------ |
| **Windows Server 2022 with IIS 10.0 version 2.15.2**      | _64bit Windows Server 2022 v2.15.2 running IIS 10.0_      | .NET 8.0.6, supports 8.0.6, 6.0.31<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2022 with IIS 10.0 version 2.15.2** | _64bit Windows Server Core 2022 v2.15.2 running IIS 10.0_ | .NET 8.0.6, supports 8.0.6, 6.0.31<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2019 with IIS 10.0 version 2.15.2**      | _64bit Windows Server 2019 v2.15.2 running IIS 10.0_      | .NET 8.0.6, supports 8.0.6, 6.0.31<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.15.2** | _64bit Windows Server Core 2019 v2.15.2 running IIS 10.0_ | .NET 8.0.6, supports 8.0.6, 6.0.31<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.15.2**      | _64bit Windows Server 2016 v2.15.2 running IIS 10.0_      | .NET 8.0.6, supports 8.0.6, 6.0.31<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.15.2** | _64bit Windows Server Core 2016 v2.15.2 running IIS 10.0_ | .NET 8.0.6, supports 8.0.6, 6.0.31<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |

### More details

| Platform Version                                          | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X-Ray |
| --------------------------------------------------------- | ----------- | ---------------- | --------- | --------- | ---------- | --------- |
| **Windows Server 2022 with IIS 10.0 version 2.15.2**      | 2024.06.13  | 3.7.830.0        |           | 3.3.484.0 | 3.6        | 3.3.11    |
| **Windows Server Core 2022 with IIS 10.0 version 2.15.2** | 2024.06.13  | 3.7.830.0        |           | 3.3.484.0 | 3.6        | 3.3.11    |
| **Windows Server 2019 with IIS 10.0 version 2.15.2**      | 2024.06.13  | 3.7.830.0        |           | 3.3.484.0 | 3.6        | 3.3.11    |
| **Windows Server Core 2019 with IIS 10.0 version 2.15.2** | 2024.06.13  | 3.7.830.0        |           | 3.3.484.0 | 3.6        | 3.3.11    |
| **Windows Server 2016 with IIS 10.0 version 2.15.2**      | 2024.06.13  | 3.7.830.0        |           | 3.3.484.0 | 3.6        | 3.3.11    |
| **Windows Server Core 2016 with IIS 10.0 version 2.15.2** | 2024.06.13  | 3.7.830.0        |           | 3.3.484.0 | 3.6        | 3.3.11    |

## May 21, 2024 – June 17, 2024

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between May 21, 2024 and June 17, 2024:

### Configuration basics

| Platform Version                                          | Solution Stack Name                                       | Framework                                                                     | Proxy Server |
| --------------------------------------------------------- | --------------------------------------------------------- | ----------------------------------------------------------------------------- | ------------ |
| **Windows Server 2022 with IIS 10.0 version 2.15.1**      | _64bit Windows Server 2022 v2.15.1 running IIS 10.0_      | .NET 8.0.5, supports 8.0.5, 6.0.30<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2022 with IIS 10.0 version 2.15.1** | _64bit Windows Server Core 2022 v2.15.1 running IIS 10.0_ | .NET 8.0.5, supports 8.0.5, 6.0.30<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2019 with IIS 10.0 version 2.15.1**      | _64bit Windows Server 2019 v2.15.1 running IIS 10.0_      | .NET 8.0.5, supports 8.0.5, 6.0.30<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.15.1** | _64bit Windows Server Core 2019 v2.15.1 running IIS 10.0_ | .NET 8.0.5, supports 8.0.5, 6.0.30<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.15.1**      | _64bit Windows Server 2016 v2.15.1 running IIS 10.0_      | .NET 8.0.5, supports 8.0.5, 6.0.30<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.15.1** | _64bit Windows Server Core 2016 v2.15.1 running IIS 10.0_ | .NET 8.0.5, supports 8.0.5, 6.0.30<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |

### More details

| Platform Version                                          | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X-Ray |
| --------------------------------------------------------- | ----------- | ---------------- | --------- | --------- | ---------- | --------- |
| **Windows Server 2022 with IIS 10.0 version 2.15.1**      | 2024.05.15  | 3.7.810.0        |           | 3.3.380.0 | 3.6        | 3.3.11    |
| **Windows Server Core 2022 with IIS 10.0 version 2.15.1** | 2024.05.15  | 3.7.810.0        |           | 3.3.380.0 | 3.6        | 3.3.11    |
| **Windows Server 2019 with IIS 10.0 version 2.15.1**      | 2024.05.15  | 3.7.810.0        |           | 3.3.380.0 | 3.6        | 3.3.11    |
| **Windows Server Core 2019 with IIS 10.0 version 2.15.1** | 2024.05.15  | 3.7.810.0        |           | 3.3.380.0 | 3.6        | 3.3.11    |
| **Windows Server 2016 with IIS 10.0 version 2.15.1**      | 2024.05.15  | 3.7.810.0        |           | 3.3.380.0 | 3.6        | 3.3.11    |
| **Windows Server Core 2016 with IIS 10.0 version 2.15.1** | 2024.05.15  | 3.7.810.0        |           | 3.3.380.0 | 3.6        | 3.3.11    |

## April 18, 2024 – May 20, 2024

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between April 18, 2024 and May 20, 2024:

### Configuration basics

| Platform Version                                          | Solution Stack Name                                       | Framework                                                                     | Proxy Server |
| --------------------------------------------------------- | --------------------------------------------------------- | ----------------------------------------------------------------------------- | ------------ |
| **Windows Server 2022 with IIS 10.0 version 2.15.0**      | _64bit Windows Server 2022 v2.15.0 running IIS 10.0_      | .NET 8.0.4, supports 8.0.4, 6.0.29<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2022 with IIS 10.0 version 2.15.0** | _64bit Windows Server Core 2022 v2.15.0 running IIS 10.0_ | .NET 8.0.4, supports 8.0.4, 6.0.29<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2019 with IIS 10.0 version 2.15.0**      | _64bit Windows Server 2019 v2.15.0 running IIS 10.0_      | .NET 8.0.4, supports 8.0.4, 6.0.29<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.15.0** | _64bit Windows Server Core 2019 v2.15.0 running IIS 10.0_ | .NET 8.0.4, supports 8.0.4, 6.0.29<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.15.0**      | _64bit Windows Server 2016 v2.15.0 running IIS 10.0_      | .NET 8.0.4, supports 8.0.4, 6.0.29<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.15.0** | _64bit Windows Server Core 2016 v2.15.0 running IIS 10.0_ | .NET 8.0.4, supports 8.0.4, 6.0.29<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |

### More details

| Platform Version                                          | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X-Ray |
| --------------------------------------------------------- | ----------- | ---------------- | --------- | --------- | ---------- | --------- |
| **Windows Server 2022 with IIS 10.0 version 2.15.0**      | 2024.04.10  | 3.7.766.0        |           | 3.3.131.0 | 3.6        | 3.3.11    |
| **Windows Server Core 2022 with IIS 10.0 version 2.15.0** | 2024.04.10  | 3.7.766.0        |           | 3.3.131.0 | 3.6        | 3.3.11    |
| **Windows Server 2019 with IIS 10.0 version 2.15.0**      | 2024.04.10  | 3.7.766.0        |           | 3.3.131.0 | 3.6        | 3.3.11    |
| **Windows Server Core 2019 with IIS 10.0 version 2.15.0** | 2024.04.10  | 3.7.766.0        |           | 3.3.131.0 | 3.6        | 3.3.11    |
| **Windows Server 2016 with IIS 10.0 version 2.15.0**      | 2024.04.10  | 3.7.766.0        |           | 3.3.131.0 | 3.6        | 3.3.11    |
| **Windows Server Core 2016 with IIS 10.0 version 2.15.0** | 2024.04.10  | 3.7.766.0        |           | 3.3.131.0 | 3.6        | 3.3.11    |

## March 21, 2024 – April 17, 2024

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between March 21, 2024 and April 17, 2024:

### Configuration basics

| Platform Version                                          | Solution Stack Name                                       | Framework                                                                     | Proxy Server |
| --------------------------------------------------------- | --------------------------------------------------------- | ----------------------------------------------------------------------------- | ------------ |
| **Windows Server 2022 with IIS 10.0 version 2.14.1**      | _64bit Windows Server 2022 v2.14.1 running IIS 10.0_      | .NET 8.0.3, supports 8.0.3, 6.0.28<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2022 with IIS 10.0 version 2.14.1** | _64bit Windows Server Core 2022 v2.14.1 running IIS 10.0_ | .NET 8.0.3, supports 8.0.3, 6.0.28<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2019 with IIS 10.0 version 2.14.1**      | _64bit Windows Server 2019 v2.14.1 running IIS 10.0_      | .NET 8.0.3, supports 8.0.3, 6.0.28<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.14.1** | _64bit Windows Server Core 2019 v2.14.1 running IIS 10.0_ | .NET 8.0.3, supports 8.0.3, 6.0.28<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.14.1**      | _64bit Windows Server 2016 v2.14.1 running IIS 10.0_      | .NET 8.0.3, supports 8.0.3, 6.0.28<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.14.1** | _64bit Windows Server Core 2016 v2.14.1 running IIS 10.0_ | .NET 8.0.3, supports 8.0.3, 6.0.28<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |

### More details

| Platform Version                                          | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| --------------------------------------------------------- | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2022 with IIS 10.0 version 2.14.1**      | 2024.03.13  | 3.7.766.0        |           | 3.2.2303.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2022 with IIS 10.0 version 2.14.1** | 2024.03.13  | 3.7.766.0        |           | 3.2.2303.0 | 3.6        | 3.2.0     |
| **Windows Server 2019 with IIS 10.0 version 2.14.1**      | 2024.03.13  | 3.7.766.0        |           | 3.2.2303.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.14.1** | 2024.03.13  | 3.7.766.0        |           | 3.2.2303.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.14.1**      | 2024.03.13  | 3.7.766.0        |           | 3.2.2303.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.14.1** | 2024.03.13  | 3.7.766.0        |           | 3.2.2303.0 | 3.6        | 3.2.0     |

## February 21, 2024 – March 20, 2024

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between February 21, 2024 and March 20, 2024:

### Configuration basics

| Platform Version                                          | Solution Stack Name                                       | Framework                                                                     | Proxy Server |
| --------------------------------------------------------- | --------------------------------------------------------- | ----------------------------------------------------------------------------- | ------------ |
| **Windows Server 2022 with IIS 10.0 version 2.14.0**      | _64bit Windows Server 2022 v2.14.0 running IIS 10.0_      | .NET 8.0.2, supports 8.0.2, 6.0.27<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server Core 2022 with IIS 10.0 version 2.14.0** | _64bit Windows Server Core 2022 v2.14.0 running IIS 10.0_ | .NET 8.0.2, supports 8.0.2, 6.0.27<br>.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0     |
| **Windows Server 2019 with IIS 10.0 version 2.14.0**      | _64bit Windows Server 2019 v2.14.0 running IIS 10.0_      | .NET 8.0.2, supports 8.0.2, 6.0.27<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.14.0** | _64bit Windows Server Core 2019 v2.14.0 running IIS 10.0_ | .NET 8.0.2, supports 8.0.2, 6.0.27<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.14.0**      | _64bit Windows Server 2016 v2.14.0 running IIS 10.0_      | .NET 8.0.2, supports 8.0.2, 6.0.27<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.14.0** | _64bit Windows Server Core 2016 v2.14.0 running IIS 10.0_ | .NET 8.0.2, supports 8.0.2, 6.0.27<br>.NET Framework 4.8, supports 4.x, 2.0   | IIS 10.0     |

### More details

| Platform Version                                          | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| --------------------------------------------------------- | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2022 with IIS 10.0 version 2.14.0**      | 2024.02.14  | 3.7.747.0        |           | 3.2.2222.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2022 with IIS 10.0 version 2.14.0** | 2024.02.14  | 3.7.747.0        |           | 3.2.2222.0 | 3.6        | 3.2.0     |
| **Windows Server 2019 with IIS 10.0 version 2.14.0**      | 2024.02.14  | 3.7.747.0        |           | 3.2.2222.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.14.0** | 2024.02.14  | 3.7.747.0        |           | 3.2.2222.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.14.0**      | 2024.02.14  | 3.7.747.0        |           | 3.2.2222.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.14.0** | 2024.02.14  | 3.7.747.0        |           | 3.2.2222.0 | 3.6        | 3.2.0     |

## January 18, 2024 – February 20, 2024

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between January 18, 2024 and February 20, 2024:

### Configuration basics

| Platform Version                                          | Solution Stack Name                                       | Framework                                                                        | Proxy Server |
| --------------------------------------------------------- | --------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.13.2**      | _64bit Windows Server 2019 v2.13.2 running IIS 10.0_      | .NET 8.0.1, supports 8.0.1, 6.0.26<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.13.2** | _64bit Windows Server Core 2019 v2.13.2 running IIS 10.0_ | .NET 8.0.1, supports 8.0.1, 6.0.26<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.13.2**      | _64bit Windows Server 2016 v2.13.2 running IIS 10.0_      | .NET 8.0.1, supports 8.0.1, 6.0.26<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.13.2** | _64bit Windows Server Core 2016 v2.13.2 running IIS 10.0_ | .NET 8.0.1, supports 8.0.1, 6.0.26<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |

### More details

| Platform Version                                          | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| --------------------------------------------------------- | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.13.2**      | 2024.01.10  | 3.7.722.0        |           | 3.2.1705.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.13.2** | 2024.01.10  | 3.7.722.0        |           | 3.2.1705.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.13.2**      | 2024.01.10  | 3.7.722.0        |           | 3.2.1705.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.13.2** | 2024.01.10  | 3.7.722.0        |           | 3.2.1705.0 | 3.6        | 3.2.0     |

## December 21, 2023 – January 17, 2024

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between December 21, 2023 and January 17, 2024:

### Configuration basics

| Platform Version                                          | Solution Stack Name                                       | Framework                                                                        | Proxy Server |
| --------------------------------------------------------- | --------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.13.1**      | _64bit Windows Server 2019 v2.13.1 running IIS 10.0_      | .NET 8.0.0, supports 8.0.0, 6.0.25<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.13.1** | _64bit Windows Server Core 2019 v2.13.1 running IIS 10.0_ | .NET 8.0.0, supports 8.0.0, 6.0.25<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.13.1**      | _64bit Windows Server 2016 v2.13.1 running IIS 10.0_      | .NET 8.0.0, supports 8.0.0, 6.0.25<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.13.1** | _64bit Windows Server Core 2016 v2.13.1 running IIS 10.0_ | .NET 8.0.0, supports 8.0.0, 6.0.25<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |

### More details

| Platform Version                                          | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| --------------------------------------------------------- | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.13.1**      | 2023.12.13  | 3.7.707.0        |           | 3.2.1705.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.13.1** | 2023.12.13  | 3.7.707.0        |           | 3.2.1705.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.13.1**      | 2023.12.13  | 3.7.707.0        |           | 3.2.1705.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.13.1** | 2023.12.13  | 3.7.707.0        |           | 3.2.1705.0 | 3.6        | 3.2.0     |

## December 5, 2023 – December 20, 2023

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between December 5, 2023 and December 20, 2023:

### Configuration basics

| Platform Version                                          | Solution Stack Name                                       | Framework                                                                        | Proxy Server |
| --------------------------------------------------------- | --------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.13.0**      | _64bit Windows Server 2019 v2.13.0 running IIS 10.0_      | .NET 8.0.0, supports 8.0.0, 6.0.25<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.13.0** | _64bit Windows Server Core 2019 v2.13.0 running IIS 10.0_ | .NET 8.0.0, supports 8.0.0, 6.0.25<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.13.0**      | _64bit Windows Server 2016 v2.13.0 running IIS 10.0_      | .NET 8.0.0, supports 8.0.0, 6.0.25<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.13.0** | _64bit Windows Server Core 2016 v2.13.0 running IIS 10.0_ | .NET 8.0.0, supports 8.0.0, 6.0.25<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |

### More details

| Platform Version                                          | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| --------------------------------------------------------- | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.13.0**      | 2023.11.15  | 3.7.686.0        |           | 3.2.1705.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.13.0** | 2023.11.15  | 3.7.686.0        |           | 3.2.1705.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.13.0**      | 2023.11.15  | 3.7.686.0        |           | 3.2.1705.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.13.0** | 2023.11.15  | 3.7.686.0        |           | 3.2.1705.0 | 3.6        | 3.2.0     |

## December 4, 2023 – December 4, 2023

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between December 4, 2023 and December 4, 2023:

### Configuration basics

| Platform Version                                          | Solution Stack Name                                       | Framework                                                                  | Proxy Server |
| --------------------------------------------------------- | --------------------------------------------------------- | -------------------------------------------------------------------------- | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.12.0**      | _64bit Windows Server 2019 v2.12.0 running IIS 10.0_      | .NET 6.0.23, supports 6.0.23<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.12.0** | _64bit Windows Server Core 2019 v2.12.0 running IIS 10.0_ | .NET 6.0.23, supports 6.0.23<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.12.0**      | _64bit Windows Server 2016 v2.12.0 running IIS 10.0_      | .NET 6.0.23, supports 6.0.23<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.12.0** | _64bit Windows Server Core 2016 v2.12.0 running IIS 10.0_ | .NET 6.0.23, supports 6.0.23<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |

### More details

| Platform Version                                          | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| --------------------------------------------------------- | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.12.0**      | 2023.10.11  | 3.7.661.0        |           | 3.2.1630.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.12.0** | 2023.10.11  | 3.7.661.0        |           | 3.2.1630.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.12.0**      | 2023.10.11  | 3.7.661.0        |           | 3.2.1630.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.12.0** | 2023.10.11  | 3.7.661.0        |           | 3.2.1630.0 | 3.6        | 3.2.0     |

## October 17, 2023 – December 3, 2023

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between October 17, 2023 and December 3, 2023:

### Configuration basics

| Platform Version                                                   | Solution Stack Name                                         | Framework                                                                       | Proxy Server |
| ------------------------------------------------------------------ | ----------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.12.0**               | _64bit Windows Server 2019 v2.12.0 running IIS 10.0_        | .NET 6.0.23, supports 6.0.23<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x      | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.12.0**          | _64bit Windows Server Core 2019 v2.12.0 running IIS 10.0_   | .NET 6.0.23, supports 6.0.23<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x      | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.12.0**               | _64bit Windows Server 2016 v2.12.0 running IIS 10.0_        | .NET 6.0.23, supports 6.0.23<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x      | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.12.0**          | _64bit Windows Server Core 2016 v2.12.0 running IIS 10.0_   | .NET 6.0.23, supports 6.0.23<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x      | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.11.8**             | _64bit Windows Server 2012 R2 v2.11.8 running IIS 8.5_      | .NET Core 2.1.30, supports 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.11.8** | _64bit Windows Server Core 2012 R2 v2.11.8 running IIS 8.5_ | .NET Core 2.1.30, supports 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5      |

### More details

| Platform Version                                                   | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| ------------------------------------------------------------------ | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.12.0**               | 2023.10.11  | 3.15.2072        |           | 3.2.1630.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.12.0**          | 2023.10.11  | 3.15.2072        |           | 3.2.1630.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.12.0**               | 2023.10.11  | 3.15.2072        |           | 3.2.1630.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.12.0**          | 2023.10.11  | 3.15.2072        |           | 3.2.1630.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.11.8**             | 2023.09.13  | 3.15.2072        |           | 3.1.2282.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.11.8** | 2023.09.13  | 3.15.2072        | 4.9.5467  | 3.1.2282.0 | 3.6        | 3.2.0     |

## September 22, 2023 – October 16, 2023

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between September 22, 2023 and October 16, 2023:

### Configuration basics

| Platform Version                                                   | Solution Stack Name                                         | Framework                                                                          | Proxy Server |
| ------------------------------------------------------------------ | ----------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.11.8**               | _64bit Windows Server 2019 v2.11.8 running IIS 10.0_        | .NET 6.0.22, supports 6.0.22, 3.1.32<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.11.8**          | _64bit Windows Server Core 2019 v2.11.8 running IIS 10.0_   | .NET 6.0.22, supports 6.0.22, 3.1.32<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.11.8**               | _64bit Windows Server 2016 v2.11.8 running IIS 10.0_        | .NET 6.0.22, supports 6.0.22, 3.1.32<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.11.8**          | _64bit Windows Server Core 2016 v2.11.8 running IIS 10.0_   | .NET 6.0.22, supports 6.0.22, 3.1.32<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.11.8**             | _64bit Windows Server 2012 R2 v2.11.8 running IIS 8.5_      | .NET Core 2.1.30, supports 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x    | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.11.8** | _64bit Windows Server Core 2012 R2 v2.11.8 running IIS 8.5_ | .NET Core 2.1.30, supports 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x    | IIS 8.5      |

### More details

| Platform Version                                                   | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| ------------------------------------------------------------------ | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.11.8**               | 2023.09.13  | 3.7.643.0        |           | 3.2.1377.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.11.8**          | 2023.09.13  | 3.7.643.0        |           | 3.2.1377.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.11.8**               | 2023.09.13  | 3.7.643.0        |           | 3.2.1377.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.11.8**          | 2023.09.13  | 3.7.643.0        |           | 3.2.1377.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.11.8**             | 2023.09.13  | 3.7.643.0        |           | 3.1.2282.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.11.8** | 2023.09.13  | 3.7.643.0        | 4.9.5467  | 3.1.2282.0 | 3.6        | 3.2.0     |

## August 25, 2023 – September 21, 2023

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between August 25, 2023 and September 21, 2023:

### Configuration basics

| Platform Version                                                   | Solution Stack Name                                         | Framework                                                                          | Proxy Server |
| ------------------------------------------------------------------ | ----------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.11.7**               | _64bit Windows Server 2019 v2.11.7 running IIS 10.0_        | .NET 6.0.21, supports 6.0.21, 3.1.32<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.11.7**          | _64bit Windows Server Core 2019 v2.11.7 running IIS 10.0_   | .NET 6.0.21, supports 6.0.21, 3.1.32<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.11.7**               | _64bit Windows Server 2016 v2.11.7 running IIS 10.0_        | .NET 6.0.21, supports 6.0.21, 3.1.32<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.11.7**          | _64bit Windows Server Core 2016 v2.11.7 running IIS 10.0_   | .NET 6.0.21, supports 6.0.21, 3.1.32<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.11.7**             | _64bit Windows Server 2012 R2 v2.11.7 running IIS 8.5_      | .NET Core 2.1.30, supports 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x    | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.11.7** | _64bit Windows Server Core 2012 R2 v2.11.7 running IIS 8.5_ | .NET Core 2.1.30, supports 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x    | IIS 8.5      |

### More details

| Platform Version                                                   | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| ------------------------------------------------------------------ | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.11.7**               | 2023.08.10  | 3.7.617.0        |           | 3.1.2282.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.11.7**          | 2023.08.10  | 3.7.617.0        |           | 3.1.2282.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.11.7**               | 2023.08.10  | 3.7.617.0        |           | 3.1.2282.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.11.7**          | 2023.08.10  | 3.7.617.0        |           | 3.1.2282.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.11.7**             | 2023.08.10  | 3.7.617.0        |           | 3.1.2282.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.11.7** | 2023.08.10  | 3.7.617.0        | 4.9.5467  | 3.1.2282.0 | 3.6        | 3.2.0     |

## July 18, 2023 – August 24, 2023

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between July 18, 2023 and August 24, 2023:

### Configuration basics

| Platform Version                                                   | Solution Stack Name                                         | Framework                                                                          | Proxy Server |
| ------------------------------------------------------------------ | ----------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.11.6**               | _64bit Windows Server 2019 v2.11.6 running IIS 10.0_        | .NET 6.0.20, supports 6.0.20, 3.1.32<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.11.6**          | _64bit Windows Server Core 2019 v2.11.6 running IIS 10.0_   | .NET 6.0.20, supports 6.0.20, 3.1.32<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.11.6**               | _64bit Windows Server 2016 v2.11.6 running IIS 10.0_        | .NET 6.0.20, supports 6.0.20, 3.1.32<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.11.6**          | _64bit Windows Server Core 2016 v2.11.6 running IIS 10.0_   | .NET 6.0.20, supports 6.0.20, 3.1.32<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.11.6**             | _64bit Windows Server 2012 R2 v2.11.6 running IIS 8.5_      | .NET Core 2.1.30, supports 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x    | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.11.6** | _64bit Windows Server Core 2012 R2 v2.11.6 running IIS 8.5_ | .NET Core 2.1.30, supports 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x    | IIS 8.5      |

### More details

| Platform Version                                                   | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| ------------------------------------------------------------------ | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.11.6**               | 2023.07.12  | 3.7.587.0        |           | 3.1.2144.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.11.6**          | 2023.07.12  | 3.7.587.0        |           | 3.1.2144.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.11.6**               | 2023.07.12  | 3.7.587.0        |           | 3.1.2144.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.11.6**          | 2023.07.12  | 3.7.587.0        |           | 3.1.2144.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.11.6**             | 2023.07.12  | 3.7.587.0        |           | 3.1.2144.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.11.6** | 2023.07.12  | 3.7.587.0        | 4.9.5288  | 3.1.2144.0 | 3.6        | 3.2.0     |

## June 26, 2023 – July 17, 2023

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between June 26, 2023 and July 17, 2023:

### Configuration basics

| Platform Version                                                   | Solution Stack Name                                         | Framework                                                                          | Proxy Server |
| ------------------------------------------------------------------ | ----------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.11.5**               | _64bit Windows Server 2019 v2.11.5 running IIS 10.0_        | .NET 6.0.18, supports 6.0.18, 3.1.32<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.11.5**          | _64bit Windows Server Core 2019 v2.11.5 running IIS 10.0_   | .NET 6.0.18, supports 6.0.18, 3.1.32<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.11.5**               | _64bit Windows Server 2016 v2.11.5 running IIS 10.0_        | .NET 6.0.18, supports 6.0.18, 3.1.32<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.11.5**          | _64bit Windows Server Core 2016 v2.11.5 running IIS 10.0_   | .NET 6.0.18, supports 6.0.18, 3.1.32<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.11.5**             | _64bit Windows Server 2012 R2 v2.11.5 running IIS 8.5_      | .NET Core 2.1.30, supports 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x    | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.11.5** | _64bit Windows Server Core 2012 R2 v2.11.5 running IIS 8.5_ | .NET Core 2.1.30, supports 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x    | IIS 8.5      |

### More details

| Platform Version                                                   | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| ------------------------------------------------------------------ | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.11.5**               | 2023.06.14  | 3.7.568.0        |           | 3.1.2144.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.11.5**          | 2023.06.14  | 3.7.568.0        |           | 3.1.2144.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.11.5**               | 2023.06.14  | 3.7.568.0        |           | 3.1.2144.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.11.5**          | 2023.06.14  | 3.7.568.0        |           | 3.1.2144.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.11.5**             | 2023.06.14  | 3.7.568.0        |           | 3.1.2144.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.11.5** | 2023.06.14  | 3.7.568.0        | 4.9.5288  | 3.1.2144.0 | 3.6        | 3.2.0     |

## May 19, 2023 – June 25, 2023

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between May 19, 2023 and June 25, 2023:

### Configuration basics

| Platform Version                                                   | Solution Stack Name                                         | Framework                                                                          | Proxy Server |
| ------------------------------------------------------------------ | ----------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.11.4**               | _64bit Windows Server 2019 v2.11.4 running IIS 10.0_        | .NET 6.0.16, supports 6.0.16, 3.1.32<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.11.4**          | _64bit Windows Server Core 2019 v2.11.4 running IIS 10.0_   | .NET 6.0.16, supports 6.0.16, 3.1.32<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.11.4**               | _64bit Windows Server 2016 v2.11.4 running IIS 10.0_        | .NET 6.0.16, supports 6.0.16, 3.1.32<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.11.4**          | _64bit Windows Server Core 2016 v2.11.4 running IIS 10.0_   | .NET 6.0.16, supports 6.0.16, 3.1.32<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.11.4**             | _64bit Windows Server 2012 R2 v2.11.4 running IIS 8.5_      | .NET Core 2.1.30, supports 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x    | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.11.4** | _64bit Windows Server Core 2012 R2 v2.11.4 running IIS 8.5_ | .NET Core 2.1.30, supports 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x    | IIS 8.5      |

### More details

| Platform Version                                                   | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| ------------------------------------------------------------------ | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.11.4**               | 2023.05.10  | 3.15.2072        |           | 3.1.2144.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.11.4**          | 2023.05.10  | 3.15.2072        |           | 3.1.2144.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.11.4**               | 2023.05.10  | 3.15.2072        |           | 3.1.2144.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.11.4**          | 2023.05.10  | 3.15.2072        |           | 3.1.2144.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.11.4**             | 2023.05.10  | 3.15.2072        |           | 3.1.2144.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.11.4** | 2023.05.10  | 3.15.2072        | 4.9.5288  | 3.1.2144.0 | 3.6        | 3.2.0     |

## April 20, 2023 – May 18, 2023

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between April 20, 2023 and May 18, 2023:

### Configuration basics

| Platform Version                                                   | Solution Stack Name                                         | Framework                                                                          | Proxy Server |
| ------------------------------------------------------------------ | ----------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.11.3**               | _64bit Windows Server 2019 v2.11.3 running IIS 10.0_        | .NET 6.0.16, supports 6.0.16, 3.1.32<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.11.3**          | _64bit Windows Server Core 2019 v2.11.3 running IIS 10.0_   | .NET 6.0.16, supports 6.0.16, 3.1.32<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.11.3**               | _64bit Windows Server 2016 v2.11.3 running IIS 10.0_        | .NET 6.0.16, supports 6.0.16, 3.1.32<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.11.3**          | _64bit Windows Server Core 2016 v2.11.3 running IIS 10.0_   | .NET 6.0.16, supports 6.0.16, 3.1.32<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.11.3**             | _64bit Windows Server 2012 R2 v2.11.3 running IIS 8.5_      | .NET Core 2.1.30, supports 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x    | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.11.3** | _64bit Windows Server Core 2012 R2 v2.11.3 running IIS 8.5_ | .NET Core 2.1.30, supports 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x    | IIS 8.5      |

### More details

| Platform Version                                                   | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| ------------------------------------------------------------------ | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.11.3**               | 2023.04.12  | 3.15.2035        |           | 3.1.2144.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.11.3**          | 2023.04.12  | 3.15.2035        |           | 3.1.2144.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.11.3**               | 2023.04.12  | 3.15.2035        |           | 3.1.2144.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.11.3**          | 2023.04.12  | 3.15.2035        |           | 3.1.2144.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.11.3**             | 2023.04.12  | 3.15.2035        |           | 3.1.2144.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.11.3** | 2023.04.12  | 3.15.2035        | 4.9.5288  | 3.1.2144.0 | 3.6        | 3.2.0     |

## March 28, 2023 – April 19, 2023

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between March 28, 2023 and April 19, 2023:

### Configuration basics

| Platform Version                                                   | Solution Stack Name                                         | Framework                                                                          | Proxy Server |
| ------------------------------------------------------------------ | ----------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.11.2**               | _64bit Windows Server 2019 v2.11.2 running IIS 10.0_        | .NET 6.0.15, supports 6.0.15, 3.1.32<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.11.2**          | _64bit Windows Server Core 2019 v2.11.2 running IIS 10.0_   | .NET 6.0.15, supports 6.0.15, 3.1.32<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.11.2**               | _64bit Windows Server 2016 v2.11.2 running IIS 10.0_        | .NET 6.0.15, supports 6.0.15, 3.1.32<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.11.2**          | _64bit Windows Server Core 2016 v2.11.2 running IIS 10.0_   | .NET 6.0.15, supports 6.0.15, 3.1.32<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.11.2**             | _64bit Windows Server 2012 R2 v2.11.2 running IIS 8.5_      | .NET Core 2.1.30, supports 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x    | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.11.2** | _64bit Windows Server Core 2012 R2 v2.11.2 running IIS 8.5_ | .NET Core 2.1.30, supports 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x    | IIS 8.5      |

### More details

| Platform Version                                                   | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| ------------------------------------------------------------------ | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.11.2**               | 2023.03.15  | 3.15.1998        |           | 3.1.1856.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.11.2**          | 2023.03.15  | 3.15.1998        |           | 3.1.1856.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.11.2**               | 2023.03.15  | 3.15.1998        |           | 3.1.1856.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.11.2**          | 2023.03.15  | 3.15.1998        |           | 3.1.1856.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.11.2**             | 2023.03.15  | 3.15.1998        |           | 3.1.2144.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.11.2** | 2023.03.15  | 3.15.1998        | 4.9.5288  | 3.1.2144.0 | 3.6        | 3.2.0     |

## February 21, 2023 – March 27, 2023

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between February 21, 2023 and March 27, 2023:

### Configuration basics

| Platform Version                                                   | Solution Stack Name                                         | Framework                                                                          | Proxy Server |
| ------------------------------------------------------------------ | ----------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.11.1**               | _64bit Windows Server 2019 v2.11.1 running IIS 10.0_        | .NET 6.0.14, supports 6.0.14, 3.1.32<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.11.1**          | _64bit Windows Server Core 2019 v2.11.1 running IIS 10.0_   | .NET 6.0.14, supports 6.0.14, 3.1.32<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.11.1**               | _64bit Windows Server 2016 v2.11.1 running IIS 10.0_        | .NET 6.0.14, supports 6.0.14, 3.1.32<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.11.1**          | _64bit Windows Server Core 2016 v2.11.1 running IIS 10.0_   | .NET 6.0.14, supports 6.0.14, 3.1.32<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.11.1**             | _64bit Windows Server 2012 R2 v2.11.1 running IIS 8.5_      | .NET Core 2.1.30, supports 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x    | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.11.1** | _64bit Windows Server Core 2012 R2 v2.11.1 running IIS 8.5_ | .NET Core 2.1.30, supports 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x    | IIS 8.5      |

### More details

| Platform Version                                                   | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| ------------------------------------------------------------------ | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.11.1**               | 2023.02.15  | 3.15.1958        |           | 3.1.1856.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.11.1**          | 2023.02.15  | 3.15.1958        |           | 3.1.1856.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.11.1**               | 2023.02.15  | 3.15.1958        |           | 3.1.1856.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.11.1**          | 2023.02.15  | 3.15.1958        |           | 3.1.1856.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.11.1**             | 2023.02.15  | 3.15.1958        |           | 3.1.1856.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.11.1** | 2023.02.15  | 3.15.1958        | 4.9.5103  | 3.1.1856.0 | 3.6        | 3.2.0     |

## January 24, 2023 – February 20, 2023

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between January 24, 2023 and February 20, 2023:

### Configuration basics

| Platform Version                                                   | Solution Stack Name                                         | Framework                                                                          | Proxy Server |
| ------------------------------------------------------------------ | ----------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.11.0**               | _64bit Windows Server 2019 v2.11.0 running IIS 10.0_        | .NET 6.0.13, supports 6.0.13, 3.1.32<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.11.0**          | _64bit Windows Server Core 2019 v2.11.0 running IIS 10.0_   | .NET 6.0.13, supports 6.0.13, 3.1.32<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.11.0**               | _64bit Windows Server 2016 v2.11.0 running IIS 10.0_        | .NET 6.0.13, supports 6.0.13, 3.1.32<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.11.0**          | _64bit Windows Server Core 2016 v2.11.0 running IIS 10.0_   | .NET 6.0.13, supports 6.0.13, 3.1.32<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.11.0**             | _64bit Windows Server 2012 R2 v2.11.0 running IIS 8.5_      | .NET Core 2.1.30, supports 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x    | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.11.0** | _64bit Windows Server Core 2012 R2 v2.11.0 running IIS 8.5_ | .NET Core 2.1.30, supports 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x    | IIS 8.5      |

### More details

| Platform Version                                                   | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| ------------------------------------------------------------------ | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.11.0**               | 2023.01.11  | 3.15.1919        |           | 3.1.1856.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.11.0**          | 2023.01.11  | 3.15.1919        |           | 3.1.1856.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.11.0**               | 2023.01.11  | 3.15.1919        |           | 3.1.1856.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.11.0**          | 2023.01.11  | 3.15.1919        |           | 3.1.1856.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.11.0**             | 2023.01.11  | 3.15.1919        |           | 3.1.1856.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.11.0** | 2023.01.11  | 3.15.1919        | 4.9.5103  | 3.1.1856.0 | 3.6        | 3.2.0     |

## December 28, 2022 – January 23, 2023

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between December 28, 2022 and January 23, 2023:

### Configuration basics

| Platform Version                                                   | Solution Stack Name                                         | Framework                                                                                  | Proxy Server |
| ------------------------------------------------------------------ | ----------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.10.7**               | _64bit Windows Server 2019 v2.10.7 running IIS 10.0_        | .NET 6.0.12, supports 6.0.12, 5.0.17, 3.1.32<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.10.7**          | _64bit Windows Server Core 2019 v2.10.7 running IIS 10.0_   | .NET 6.0.12, supports 6.0.12, 5.0.17, 3.1.32<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.10.7**               | _64bit Windows Server 2016 v2.10.7 running IIS 10.0_        | .NET 6.0.12, supports 6.0.12, 5.0.17, 3.1.32<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.10.7**          | _64bit Windows Server Core 2016 v2.10.7 running IIS 10.0_   | .NET 6.0.12, supports 6.0.12, 5.0.17, 3.1.32<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.10.7**             | _64bit Windows Server 2012 R2 v2.10.7 running IIS 8.5_      | .NET Core 2.1.30, supports 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x            | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.10.7** | _64bit Windows Server Core 2012 R2 v2.10.7 running IIS 8.5_ | .NET Core 2.1.30, supports 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x            | IIS 8.5      |

### More details

| Platform Version                                                   | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| ------------------------------------------------------------------ | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.10.7**               | 2022.12.14  | 3.15.1886        |           | 3.1.1856.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.10.7**          | 2022.12.14  | 3.15.1886        |           | 3.1.1856.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.10.7**               | 2022.12.14  | 3.15.1886        |           | 3.1.1856.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.10.7**          | 2022.12.14  | 3.15.1886        |           | 3.1.1856.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.10.7**             | 2022.12.14  | 3.15.1886        |           | 3.1.1856.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.10.7** | 2022.12.14  | 3.15.1886        | 4.9.5103  | 3.1.1856.0 | 3.6        | 3.2.0     |

## November 18, 2022 – December 27, 2022

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between November 18, 2022 and December 27, 2022:

### Configuration basics

| Platform Version                                                   | Solution Stack Name                                         | Framework                                                                                  | Proxy Server |
| ------------------------------------------------------------------ | ----------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.10.6**               | _64bit Windows Server 2019 v2.10.6 running IIS 10.0_        | .NET 6.0.11, supports 6.0.11, 5.0.17, 3.1.31<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.10.6**          | _64bit Windows Server Core 2019 v2.10.6 running IIS 10.0_   | .NET 6.0.11, supports 6.0.11, 5.0.17, 3.1.31<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.10.6**               | _64bit Windows Server 2016 v2.10.6 running IIS 10.0_        | .NET 6.0.11, supports 6.0.11, 5.0.17, 3.1.31<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.10.6**          | _64bit Windows Server Core 2016 v2.10.6 running IIS 10.0_   | .NET 6.0.11, supports 6.0.11, 5.0.17, 3.1.31<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.10.6**             | _64bit Windows Server 2012 R2 v2.10.6 running IIS 8.5_      | .NET Core 2.1.30, supports 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x            | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.10.6** | _64bit Windows Server Core 2012 R2 v2.10.6 running IIS 8.5_ | .NET Core 2.1.30, supports 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x            | IIS 8.5      |

### More details

| Platform Version                                                   | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| ------------------------------------------------------------------ | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.10.6**               | 2022.10.27  | 3.15.1809        |           | 3.1.1732.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.10.6**          | 2022.10.27  | 3.15.1809        |           | 3.1.1732.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.10.6**               | 2022.10.27  | 3.15.1809        |           | 3.1.1732.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.10.6**          | 2022.10.27  | 3.15.1809        |           | 3.1.1732.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.10.6**             | 2022.10.27  | 3.15.1809        |           | 3.1.1188.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.10.6** | 2022.10.27  | 3.15.1809        | 4.9.4588  | 3.1.1188.0 | 3.6        | 3.2.0     |

## October 24, 2022 – November 17, 2022

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between October 24, 2022 and November 17, 2022:

### Configuration basics

| Platform Version                                                   | Solution Stack Name                                         | Framework                                                                                  | Proxy Server |
| ------------------------------------------------------------------ | ----------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.10.5**               | _64bit Windows Server 2019 v2.10.5 running IIS 10.0_        | .NET 6.0.10, supports 6.0.10, 5.0.17, 3.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.10.5**          | _64bit Windows Server Core 2019 v2.10.5 running IIS 10.0_   | .NET 6.0.10, supports 6.0.10, 5.0.17, 3.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.10.5**               | _64bit Windows Server 2016 v2.10.5 running IIS 10.0_        | .NET 6.0.10, supports 6.0.10, 5.0.17, 3.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.10.5**          | _64bit Windows Server Core 2016 v2.10.5 running IIS 10.0_   | .NET 6.0.10, supports 6.0.10, 5.0.17, 3.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.10.5**             | _64bit Windows Server 2012 R2 v2.10.5 running IIS 8.5_      | .NET Core 2.1.30, supports 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x            | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.10.5** | _64bit Windows Server Core 2012 R2 v2.10.5 running IIS 8.5_ | .NET Core 2.1.30, supports 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x            | IIS 8.5      |

### More details

| Platform Version                                                   | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| ------------------------------------------------------------------ | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.10.5**               | 2022.10.12  | 3.15.1809        |           | 3.1.1732.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.10.5**          | 2022.10.12  | 3.15.1809        |           | 3.1.1732.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.10.5**               | 2022.10.12  | 3.15.1809        |           | 3.1.1732.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.10.5**          | 2022.10.12  | 3.15.1809        |           | 3.1.1732.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.10.5**             | 2022.10.12  | 3.15.1809        |           | 3.1.1188.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.10.5** | 2022.10.12  | 3.15.1809        | 4.9.4588  | 3.1.1188.0 | 3.6        | 3.2.0     |

## September 21, 2022 – October 23, 2022

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between September 21, 2022 and October 23, 2022:

### Configuration basics

| Platform Version                                                   | Solution Stack Name                                         | Framework                                                                                | Proxy Server |
| ------------------------------------------------------------------ | ----------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.10.4**               | _64bit Windows Server 2019 v2.10.4 running IIS 10.0_        | .NET 6.0.9, supports 6.0.9, 5.0.17, 3.1.29<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.10.4**          | _64bit Windows Server Core 2019 v2.10.4 running IIS 10.0_   | .NET 6.0.9, supports 6.0.9, 5.0.17, 3.1.29<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.10.4**               | _64bit Windows Server 2016 v2.10.4 running IIS 10.0_        | .NET 6.0.9, supports 6.0.9, 5.0.17, 3.1.29<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.10.4**          | _64bit Windows Server Core 2016 v2.10.4 running IIS 10.0_   | .NET 6.0.9, supports 6.0.9, 5.0.17, 3.1.29<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.10.4**             | _64bit Windows Server 2012 R2 v2.10.4 running IIS 8.5_      | .NET Core 2.1.30, supports 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x          | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.10.4** | _64bit Windows Server Core 2012 R2 v2.10.4 running IIS 8.5_ | .NET Core 2.1.30, supports 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x          | IIS 8.5      |

### More details

| Platform Version                                                   | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| ------------------------------------------------------------------ | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.10.4**               | 2022.09.14  | 3.15.1772        |           | 3.1.1634.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.10.4**          | 2022.09.14  | 3.15.1772        |           | 3.1.1634.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.10.4**               | 2022.09.14  | 3.15.1772        |           | 3.1.1634.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.10.4**          | 2022.09.14  | 3.15.1772        |           | 3.1.1634.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.10.4**             | 2022.09.14  | 3.15.1772        |           | 3.1.1188.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.10.4** | 2022.09.14  | 3.15.1772        | 4.9.4588  | 3.1.1188.0 | 3.6        | 3.2.0     |

## August 25, 2022 – September 20, 2022

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between August 25, 2022 and September 20, 2022:

### Configuration basics

| Platform Version                                                   | Solution Stack Name                                         | Framework                                                                                | Proxy Server |
| ------------------------------------------------------------------ | ----------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.10.3**               | _64bit Windows Server 2019 v2.10.3 running IIS 10.0_        | .NET 6.0.8, supports 6.0.8, 5.0.17, 3.1.28<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.10.3**          | _64bit Windows Server Core 2019 v2.10.3 running IIS 10.0_   | .NET 6.0.8, supports 6.0.8, 5.0.17, 3.1.28<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.10.3**               | _64bit Windows Server 2016 v2.10.3 running IIS 10.0_        | .NET 6.0.8, supports 6.0.8, 5.0.17, 3.1.28<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.10.3**          | _64bit Windows Server Core 2016 v2.10.3 running IIS 10.0_   | .NET 6.0.8, supports 6.0.8, 5.0.17, 3.1.28<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.10.3**             | _64bit Windows Server 2012 R2 v2.10.3 running IIS 8.5_      | .NET Core 2.1.30, supports 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x          | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.10.3** | _64bit Windows Server Core 2012 R2 v2.10.3 running IIS 8.5_ | .NET Core 2.1.30, supports 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x          | IIS 8.5      |

### More details

| Platform Version                                                   | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| ------------------------------------------------------------------ | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.10.3**               | 2022.08.10  | 3.15.1737        |           | 3.1.1634.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.10.3**          | 2022.08.10  | 3.15.1737        |           | 3.1.1634.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.10.3**               | 2022.08.10  | 3.15.1737        |           | 3.1.1634.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.10.3**          | 2022.08.10  | 3.15.1737        |           | 3.1.1634.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.10.3**             | 2022.08.10  | 3.15.1737        |           | 3.1.1188.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.10.3** | 2022.08.10  | 3.15.1737        | 4.9.4588  | 3.1.1188.0 | 3.6        | 3.2.0     |

## July 29, 2022 – August 24, 2022

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between July 29, 2022 and August 24, 2022:

### Configuration basics

| Platform Version                                                   | Solution Stack Name                                         | Framework                                                                                | Proxy Server |
| ------------------------------------------------------------------ | ----------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.10.2**               | _64bit Windows Server 2019 v2.10.2 running IIS 10.0_        | .NET 6.0.7, supports 6.0.7, 5.0.17, 3.1.27<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.10.2**          | _64bit Windows Server Core 2019 v2.10.2 running IIS 10.0_   | .NET 6.0.7, supports 6.0.7, 5.0.17, 3.1.27<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.10.2**               | _64bit Windows Server 2016 v2.10.2 running IIS 10.0_        | .NET 6.0.7, supports 6.0.7, 5.0.17, 3.1.27<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.10.2**          | _64bit Windows Server Core 2016 v2.10.2 running IIS 10.0_   | .NET 6.0.7, supports 6.0.7, 5.0.17, 3.1.27<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.10.2**             | _64bit Windows Server 2012 R2 v2.10.2 running IIS 8.5_      | .NET Core 2.1.30, supports 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x          | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.10.2** | _64bit Windows Server Core 2012 R2 v2.10.2 running IIS 8.5_ | .NET Core 2.1.30, supports 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x          | IIS 8.5      |

### More details

| Platform Version                                                   | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| ------------------------------------------------------------------ | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.10.2**               | 2022.06.15  | 3.15.1678        |           | 3.1.1188.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.10.2**          | 2022.06.15  | 3.15.1678        |           | 3.1.1188.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.10.2**               | 2022.06.15  | 3.15.1678        |           | 3.1.1188.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.10.2**          | 2022.06.15  | 3.15.1678        |           | 3.1.1188.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.10.2**             | 2022.06.15  | 3.15.1678        |           | 3.1.1188.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.10.2** | 2022.06.15  | 3.15.1678        | 4.9.4588  | 3.1.1188.0 | 3.6        | 3.2.0     |

## June 29, 2022 – July 28, 2022

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between June 29, 2022 and July 28, 2022:

### Configuration basics

| Platform Version                                                   | Solution Stack Name                                         | Framework                                                                                | Proxy Server |
| ------------------------------------------------------------------ | ----------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.10.1**               | _64bit Windows Server 2019 v2.10.1 running IIS 10.0_        | .NET 6.0.6, supports 6.0.6, 5.0.17, 3.1.26<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.10.1**          | _64bit Windows Server Core 2019 v2.10.1 running IIS 10.0_   | .NET 6.0.6, supports 6.0.6, 5.0.17, 3.1.26<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.10.1**               | _64bit Windows Server 2016 v2.10.1 running IIS 10.0_        | .NET 6.0.6, supports 6.0.6, 5.0.17, 3.1.26<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.10.1**          | _64bit Windows Server Core 2016 v2.10.1 running IIS 10.0_   | .NET 6.0.6, supports 6.0.6, 5.0.17, 3.1.26<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.10.1**             | _64bit Windows Server 2012 R2 v2.10.1 running IIS 8.5_      | .NET Core 2.1.30, supports 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x          | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.10.1** | _64bit Windows Server Core 2012 R2 v2.10.1 running IIS 8.5_ | .NET Core 2.1.30, supports 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x          | IIS 8.5      |

### More details

| Platform Version                                                   | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| ------------------------------------------------------------------ | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.10.1**               | 2022.06.15  | 3.15.1678        |           | 3.1.1188.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.10.1**          | 2022.06.15  | 3.15.1678        |           | 3.1.1188.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.10.1**               | 2022.06.15  | 3.15.1678        |           | 3.1.1188.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.10.1**          | 2022.06.15  | 3.15.1678        |           | 3.1.1188.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.10.1**             | 2022.06.15  | 3.15.1678        |           | 3.1.1188.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.10.1** | 2022.06.15  | 3.15.1678        | 4.9.4588  | 3.1.1188.0 | 3.6        | 3.2.0     |

## June 22, 2022 – June 28, 2022

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between June 22, 2022 and June 28, 2022:

### Configuration basics

| Platform Version                                                   | Solution Stack Name                                         | Framework                                                                                | Proxy Server |
| ------------------------------------------------------------------ | ----------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.10.1**               | _64bit Windows Server 2019 v2.10.1 running IIS 10.0_        | .NET 6.0.6, supports 6.0.6, 5.0.17, 3.1.26<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.10.1**          | _64bit Windows Server Core 2019 v2.10.1 running IIS 10.0_   | .NET 6.0.6, supports 6.0.6, 5.0.17, 3.1.26<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.10.1**               | _64bit Windows Server 2016 v2.10.1 running IIS 10.0_        | .NET 6.0.6, supports 6.0.6, 5.0.17, 3.1.26<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.10.1**          | _64bit Windows Server Core 2016 v2.10.1 running IIS 10.0_   | .NET 6.0.6, supports 6.0.6, 5.0.17, 3.1.26<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.10.1**             | _64bit Windows Server 2012 R2 v2.10.1 running IIS 8.5_      | .NET Core 2.1.30, supports 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x          | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.10.1** | _64bit Windows Server Core 2012 R2 v2.10.1 running IIS 8.5_ | .NET Core 2.1.30, supports 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x          | IIS 8.5      |

### More details

| Platform Version                                                   | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| ------------------------------------------------------------------ | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.10.1**               | 2022.06.15  | 3.15.1678        |           | 3.1.1188.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.10.1**          | 2022.06.15  | 3.15.1678        |           | 3.1.1188.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.10.1**               | 2022.06.15  | 3.15.1678        |           | 3.1.1188.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.10.1**          | 2022.06.15  | 3.15.1678        |           | 3.1.1188.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.10.1**             | 2022.06.15  | 3.15.1678        |           | 3.1.1188.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.10.1** | 2022.06.15  | 3.15.1678        | 4.9.4588  | 3.1.1188.0 | 3.6        | 3.2.0     |

## May 27, 2022 – June 21, 2022

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between May 27, 2022 and June 21, 2022:

### Configuration basics

| Platform Version                                                   | Solution Stack Name                                         | Framework                                                                                                    | Proxy Server |
| ------------------------------------------------------------------ | ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.10.0**               | _64bit Windows Server 2019 v2.10.0 running IIS 10.0_        | .NET 6.0.5, supports 6.0.5, 5.0.17, 3.1.25<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                     | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.10.0**          | _64bit Windows Server Core 2019 v2.10.0 running IIS 10.0_   | .NET 6.0.5, supports 6.0.5, 5.0.17, 3.1.25<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                     | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.10.0**               | _64bit Windows Server 2016 v2.10.0 running IIS 10.0_        | .NET 6.0.5, supports 6.0.5, 5.0.17, 3.1.25<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                     | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.10.0**          | _64bit Windows Server Core 2016 v2.10.0 running IIS 10.0_   | .NET 6.0.5, supports 6.0.5, 5.0.17, 3.1.25<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                     | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.10.0**             | _64bit Windows Server 2012 R2 v2.10.0 running IIS 8.5_      | .NET Core 2.1.30, supports 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                              | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.10.0** | _64bit Windows Server Core 2012 R2 v2.10.0 running IIS 8.5_ | .NET Core 2.1.30, supports 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                              | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                   | _64bit Windows Server 2012 v1.2.0 running IIS 8_            | .NET Core 2.2.8, supports 2.2.8, 2.1.30, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8        |
| **Windows Server 2012 with IIS 8 version 0.1.0**                   | _64bit Windows Server 2012 running IIS 8_                   | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                   | IIS 8        |

### More details

| Platform Version                                                   | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| ------------------------------------------------------------------ | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.10.0**               | 2022.05.11  | 3.15.1620        |           | 3.1.1045.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.10.0**          | 2022.05.11  | 3.15.1620        |           | 3.1.1045.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.10.0**               | 2022.05.11  | 3.15.1620        |           | 3.1.1045.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.10.0**          | 2022.05.11  | 3.15.1620        |           | 3.1.1045.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.10.0**             | 2022.05.11  | 3.15.1620        |           | 3.1.1045.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.10.0** | 2022.05.11  | 3.15.1620        | 4.9.4556  | 3.1.1045.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                   | 2022.05.11  | 3.15.1583        |           | 3.1.1045.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 with IIS 8 version 0.1.0**                   | 2022.05.11  | 3.15.1583        |           | 3.1.1045.0 | 3.6        | 3.1.0     |

## April 30, 2022 – May 26, 2022

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between April 30, 2022 and May 26, 2022:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                                    | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.9.1**               | _64bit Windows Server 2019 v2.9.1 running IIS 10.0_        | .NET 5.0.16, supports 5.0.16, 3.1.24<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                           | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.9.1**          | _64bit Windows Server Core 2019 v2.9.1 running IIS 10.0_   | .NET 5.0.16, supports 5.0.16, 3.1.24<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                           | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.9.1**               | _64bit Windows Server 2016 v2.9.1 running IIS 10.0_        | .NET 5.0.16, supports 5.0.16, 3.1.24<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                           | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.9.1**          | _64bit Windows Server Core 2016 v2.9.1 running IIS 10.0_   | .NET 5.0.16, supports 5.0.16, 3.1.24<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                           | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.9.1**             | _64bit Windows Server 2012 R2 v2.9.1 running IIS 8.5_      | .NET Core 2.1.30, supports 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                              | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.9.1** | _64bit Windows Server Core 2012 R2 v2.9.1 running IIS 8.5_ | .NET Core 2.1.30, supports 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                              | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | _64bit Windows Server 2012 v1.2.0 running IIS 8_           | .NET Core 2.2.8, supports 2.2.8, 2.1.30, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8        |
| **Windows Server 2012 with IIS 8 version 0.1.0**                  | _64bit Windows Server 2012 running IIS 8_                  | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                   | IIS 8        |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.9.1**               | 2022.04.13  | 3.15.1620        |           | 3.1.1045.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.9.1**          | 2022.04.13  | 3.15.1620        |           | 3.1.1045.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.9.1**               | 2022.04.13  | 3.15.1620        |           | 3.1.1045.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.9.1**          | 2022.04.13  | 3.15.1620        |           | 3.1.1045.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.9.1**             | 2022.04.13  | 3.15.1620        |           | 3.1.1045.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.9.1** | 2022.04.13  | 3.15.1620        | 4.9.4556  | 3.1.1045.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | 2022.03.09  | 3.15.1583        |           | 3.1.1045.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 with IIS 8 version 0.1.0**                  | 2022.03.09  | 3.15.1583        |           | 3.1.1045.0 | 3.6        | 3.1.0     |

## March 16, 2022 – April 29, 2022

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between March 16, 2022 and April 29, 2022:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                                    | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.9.0**               | _64bit Windows Server 2019 v2.9.0 running IIS 10.0_        | .NET 5.0.15, supports 5.0.15, 3.1.23<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                           | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.9.0**          | _64bit Windows Server Core 2019 v2.9.0 running IIS 10.0_   | .NET 5.0.15, supports 5.0.15, 3.1.23<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                           | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.9.0**               | _64bit Windows Server 2016 v2.9.0 running IIS 10.0_        | .NET 5.0.15, supports 5.0.15, 3.1.23<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                           | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.9.0**          | _64bit Windows Server Core 2016 v2.9.0 running IIS 10.0_   | .NET 5.0.15, supports 5.0.15, 3.1.23<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                           | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.9.0**             | _64bit Windows Server 2012 R2 v2.9.0 running IIS 8.5_      | .NET Core 2.1.30, supports 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                              | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.9.0** | _64bit Windows Server Core 2012 R2 v2.9.0 running IIS 8.5_ | .NET Core 2.1.30, supports 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                              | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | _64bit Windows Server 2012 v1.2.0 running IIS 8_           | .NET Core 2.2.8, supports 2.2.8, 2.1.30, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8        |
| **Windows Server 2012 with IIS 8 version 0.1.0**                  | _64bit Windows Server 2012 v0.1.0 running IIS 8_           | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                   | IIS 8        |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.9.0**               | 2022.03.09  | 3.15.1583        |           | 3.1.1045.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.9.0**          | 2022.03.09  | 3.15.1583        |           | 3.1.1045.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.9.0**               | 2022.03.09  | 3.15.1583        |           | 3.1.1045.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.9.0**          | 2022.03.09  | 3.15.1583        |           | 3.1.1045.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.9.0**             | 2022.03.09  | 3.15.1583        |           | 3.1.1045.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.9.0** | 2022.03.09  | 3.15.1583        | 4.9.4556  | 3.1.1045.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | 2022.03.09  | 3.15.1583        |           | 3.1.1045.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 with IIS 8 version 0.1.0**                  | 2022.03.09  | 3.15.1583        |           | 3.1.1045.0 | 3.6        | 3.1.0     |

## February 18, 2022 – March 15, 2022

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between February 18, 2022 and March 15, 2022:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                                    | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.8.3**               | _64bit Windows Server 2019 v2.8.3 running IIS 10.0_        | .NET 5.0.14, supports 5.0.14, 3.1.22, 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                   | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.8.3**          | _64bit Windows Server Core 2019 v2.8.3 running IIS 10.0_   | .NET 5.0.14, supports 5.0.14, 3.1.22, 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                   | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.8.3**               | _64bit Windows Server 2016 v2.8.3 running IIS 10.0_        | .NET 5.0.14, supports 5.0.14, 3.1.22, 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                   | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.8.3**          | _64bit Windows Server Core 2016 v2.8.3 running IIS 10.0_   | .NET 5.0.14, supports 5.0.14, 3.1.22, 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                   | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.8.3**             | _64bit Windows Server 2012 R2 v2.8.3 running IIS 8.5_      | .NET Core 3.0.0, supports 3.0.0, 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.8.3** | _64bit Windows Server Core 2012 R2 v2.8.3 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | _64bit Windows Server 2012 v1.2.0 running IIS 8_           | .NET Core 2.2.8, supports 2.2.8, 2.1.30, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8        |
| **Windows Server 2012 with IIS 8 version 0.1.0**                  | _64bit Windows Server 2012 v0.1.0 running IIS 8_           | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                   | IIS 8        |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------- | --------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.8.3**               | 2022.02.10  | 3.15.1546        |           | 3.1.804.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.8.3**          | 2022.02.10  | 3.15.1546        |           | 3.1.804.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.8.3**               | 2022.02.10  | 3.15.1546        |           | 3.1.804.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.8.3**          | 2022.02.10  | 3.15.1546        |           | 3.1.804.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.8.3**             | 2022.02.10  | 3.15.1546        |           | 3.1.804.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.8.3** | 2022.02.10  | 3.15.1546        | 4.9.4536  | 3.1.804.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | 2022.02.10  | 3.15.1546        |           | 3.1.804.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 with IIS 8 version 0.1.0**                  | 2022.02.10  | 3.15.1546        |           | 3.1.804.0 | 3.6        | 3.1.0     |

## January 27, 2022 – February 17, 2022

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between January 27, 2022 and February 17, 2022:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                                    | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.8.2**               | _64bit Windows Server 2019 v2.8.2 running IIS 10.0_        | .NET 5.0.13, supports 5.0.13, 3.1.22, 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                   | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.8.2**          | _64bit Windows Server Core 2019 v2.8.2 running IIS 10.0_   | .NET 5.0.13, supports 5.0.13, 3.1.22, 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                   | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.8.2**               | _64bit Windows Server 2016 v2.8.2 running IIS 10.0_        | .NET 5.0.13, supports 5.0.13, 3.1.22, 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                   | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.8.2**          | _64bit Windows Server Core 2016 v2.8.2 running IIS 10.0_   | .NET 5.0.13, supports 5.0.13, 3.1.22, 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                   | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.8.2**             | _64bit Windows Server 2012 R2 v2.8.2 running IIS 8.5_      | .NET Core 3.0.0, supports 3.0.0, 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.8.2** | _64bit Windows Server Core 2012 R2 v2.8.2 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | _64bit Windows Server 2012 v1.2.0 running IIS 8_           | .NET Core 2.2.8, supports 2.2.8, 2.1.30, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8        |
| **Windows Server 2012 with IIS 8 version 0.1.0**                  | _64bit Windows Server 2012 v0.1.0 running IIS 8_           | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                   | IIS 8        |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------- | --------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.8.2**               | 2022.01.19  | 3.15.1511        |           | 3.1.338.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.8.2**          | 2022.01.19  | 3.15.1511        |           | 3.1.338.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.8.2**               | 2022.01.19  | 3.15.1511        |           | 3.1.338.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.8.2**          | 2022.01.19  | 3.15.1511        |           | 3.1.338.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.8.2**             | 2022.01.19  | 3.15.1511        | 4.9.4508  | 3.1.338.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.8.2** | 2022.01.19  | 3.15.1511        | 4.9.4508  | 3.1.338.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | 2021.12.15  | 3.15.1451        | 4.9.4508  | 3.1.338.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 with IIS 8 version 0.1.0**                  | 2021.12.15  | 3.15.1451        | 4.9.4508  | 3.1.338.0 | 3.6        | 3.1.0     |

## January 5, 2022 – January 26, 2022

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between January 5, 2022 and January 26, 2022:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                                    | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.8.1**               | _64bit Windows Server 2019 v2.8.1 running IIS 10.0_        | .NET 5.0.13, supports 5.0.13, 3.1.22, 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                   | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.8.1**          | _64bit Windows Server Core 2019 v2.8.1 running IIS 10.0_   | .NET 5.0.13, supports 5.0.13, 3.1.22, 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                   | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.8.1**               | _64bit Windows Server 2016 v2.8.1 running IIS 10.0_        | .NET 5.0.13, supports 5.0.13, 3.1.22, 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                   | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.8.1**          | _64bit Windows Server Core 2016 v2.8.1 running IIS 10.0_   | .NET 5.0.13, supports 5.0.13, 3.1.22, 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                   | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.8.1**             | _64bit Windows Server 2012 R2 v2.8.1 running IIS 8.5_      | .NET Core 3.0.0, supports 3.0.0, 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.8.1** | _64bit Windows Server Core 2012 R2 v2.8.1 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | _64bit Windows Server 2012 v1.2.0 running IIS 8_           | .NET Core 2.2.8, supports 2.2.8, 2.1.30, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8        |
| **Windows Server 2012 with IIS 8 version 0.1.0**                  | _64bit Windows Server 2012 v0.1.0 running IIS 8_           | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                   | IIS 8        |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------- | --------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.8.1**               | 2021.12.15  | 3.15.1451        |           | 3.1.338.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.8.1**          | 2021.12.15  | 3.15.1451        |           | 3.1.338.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.8.1**               | 2021.12.15  | 3.15.1451        |           | 3.1.338.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.8.1**          | 2021.12.15  | 3.15.1451        |           | 3.1.338.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.8.1**             | 2021.12.15  | 3.15.1451        | 4.9.4508  | 3.1.338.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.8.1** | 2021.12.15  | 3.15.1451        | 4.9.4508  | 3.1.338.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | 2021.12.15  | 3.15.1451        | 4.9.4508  | 3.1.338.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 with IIS 8 version 0.1.0**                  | 2021.12.15  | 3.15.1451        | 4.9.4508  | 3.1.338.0 | 3.6        | 3.1.0     |

## November 23, 2021 – January 4, 2022

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between November 23, 2021 and January 4, 2022:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                                    | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.8.0**               | _64bit Windows Server 2019 v2.8.0 running IIS 10.0_        | .NET 5.0.12, supports 5.0.12, 3.1.21, 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                   | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.8.0**          | _64bit Windows Server Core 2019 v2.8.0 running IIS 10.0_   | .NET 5.0.12, supports 5.0.12, 3.1.21, 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                   | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.8.0**               | _64bit Windows Server 2016 v2.8.0 running IIS 10.0_        | .NET 5.0.12, supports 5.0.12, 3.1.21, 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                   | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.8.0**          | _64bit Windows Server Core 2016 v2.8.0 running IIS 10.0_   | .NET 5.0.12, supports 5.0.12, 3.1.21, 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                   | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.8.0**             | _64bit Windows Server 2012 R2 v2.8.0 running IIS 8.5_      | .NET Core 3.0.0, supports 3.0.0, 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.8.0** | _64bit Windows Server Core 2012 R2 v2.8.0 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | _64bit Windows Server 2012 v1.2.0 running IIS 8_           | .NET Core 2.2.8, supports 2.2.8, 2.1.30, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8        |
| **Windows Server 2012 with IIS 8 version 0.1.0**                  | _64bit Windows Server 2012 v0.1.0 running IIS 8_           | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                   | IIS 8        |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------- | --------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.8.0**               | 2021.11.10  | 3.15.1451        |           | 3.1.338.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.8.0**          | 2021.11.10  | 3.15.1451        |           | 3.1.338.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.8.0**               | 2021.11.10  | 3.15.1451        |           | 3.1.338.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.8.0**          | 2021.11.10  | 3.15.1451        |           | 3.1.338.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.8.0**             | 2021.11.10  | 3.15.1451        | 4.9.4508  | 3.1.338.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.8.0** | 2021.11.10  | 3.15.1451        | 4.9.4508  | 3.1.338.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | 2021.11.10  | 3.15.1451        | 4.9.4508  | 3.1.338.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 with IIS 8 version 0.1.0**                  | 2021.11.10  | 3.15.1451        | 4.9.4508  | 3.1.338.0 | 3.6        | 3.1.0     |

## October 22, 2021 – November 22, 2021

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between October 22, 2021 and November 22, 2021:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                                    | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.7.2**               | _64bit Windows Server 2019 v2.7.2 running IIS 10.0_        | .NET 5.0.11, supports 5.0.11, 3.1.20, 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                   | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.7.2**          | _64bit Windows Server Core 2019 v2.7.2 running IIS 10.0_   | .NET 5.0.11, supports 5.0.11, 3.1.20, 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                   | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.7.2**               | _64bit Windows Server 2016 v2.7.2 running IIS 10.0_        | .NET 5.0.11, supports 5.0.11, 3.1.20, 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                   | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.7.2**          | _64bit Windows Server Core 2016 v2.7.2 running IIS 10.0_   | .NET 5.0.11, supports 5.0.11, 3.1.20, 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                   | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.7.2**             | _64bit Windows Server 2012 R2 v2.7.2 running IIS 8.5_      | .NET Core 3.0.0, supports 3.0.0, 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.7.2** | _64bit Windows Server Core 2012 R2 v2.7.2 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | _64bit Windows Server 2012 v1.2.0 running IIS 8_           | .NET Core 2.2.8, supports 2.2.8, 2.1.30, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8        |
| **Windows Server 2012 with IIS 8 version 0.1.0**                  | _64bit Windows Server 2012 v0.1.0 running IIS 8_           | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                   | IIS 8        |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------- | --------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.7.2**               | 2021.10.13  | 3.15.1421        |           | 3.1.338.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.7.2**          | 2021.10.13  | 3.15.1421        |           | 3.1.338.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.7.2**               | 2021.10.13  | 3.15.1421        |           | 3.1.338.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.7.2**          | 2021.10.13  | 3.15.1421        |           | 3.1.338.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.7.2**             | 2021.10.13  | 3.15.1421        | 4.9.4508  | 3.1.338.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.7.2** | 2021.10.13  | 3.15.1421        | 4.9.4508  | 3.1.338.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | 2021.10.13  | 3.15.1421        | 4.9.4508  | 3.1.338.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 with IIS 8 version 0.1.0**                  | 2021.10.13  | 3.15.1421        | 4.9.4508  | 3.1.338.0 | 3.6        | 3.1.0     |

## October 5, 2021 – October 21, 2021

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between October 5, 2021 and October 21, 2021:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                                    | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.7.1**               | _64bit Windows Server 2019 v2.7.1 running IIS 10.0_        | .NET 5.0.10, supports 5.0.10, 3.1.19, 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                   | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.7.1**          | _64bit Windows Server Core 2019 v2.7.1 running IIS 10.0_   | .NET 5.0.10, supports 5.0.10, 3.1.19, 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                   | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.7.1**               | _64bit Windows Server 2016 v2.7.1 running IIS 10.0_        | .NET 5.0.10, supports 5.0.10, 3.1.19, 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                   | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.7.1**          | _64bit Windows Server Core 2016 v2.7.1 running IIS 10.0_   | .NET 5.0.10, supports 5.0.10, 3.1.19, 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                   | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.7.1**             | _64bit Windows Server 2012 R2 v2.7.1 running IIS 8.5_      | .NET Core 3.0.0, supports 3.0.0, 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.7.1** | _64bit Windows Server Core 2012 R2 v2.7.1 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.1.30<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | _64bit Windows Server 2012 v1.2.0 running IIS 8_           | .NET Core 2.2.8, supports 2.2.8, 2.1.30, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8        |
| **Windows Server 2012 with IIS 8 version 0.1.0**                  | _64bit Windows Server 2012 v0.1.0 running IIS 8_           | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                   | IIS 8        |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------- | --------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.7.1**               | 2021.09.15  | 3.15.1398        |           | 3.1.282.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.7.1**          | 2021.09.15  | 3.15.1398        |           | 3.1.282.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.7.1**               | 2021.09.15  | 3.15.1398        |           | 3.1.282.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.7.1**          | 2021.09.15  | 3.15.1398        |           | 3.1.282.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.7.1**             | 2021.09.15  | 3.15.1398        | 4.9.4500  | 3.1.282.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.7.1** | 2021.09.15  | 3.15.1398        | 4.9.4500  | 3.1.282.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | 2021.09.15  | 3.15.1398        | 4.9.4500  | 3.1.282.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 with IIS 8 version 0.1.0**                  | 2021.09.15  | 3.15.1398        | 4.9.4500  | 3.1.282.0 | 3.6        | 3.1.0     |

## August 23, 2021 – October 4, 2021

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between August 23, 2021 and October 4, 2021:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                                    | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.7.0**               | _64bit Windows Server 2019 v2.7.0 running IIS 10.0_        | .NET 5.0.9, supports 5.0.9, 3.1.18, 2.1.29<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                     | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.7.0**          | _64bit Windows Server Core 2019 v2.7.0 running IIS 10.0_   | .NET 5.0.9, supports 5.0.9, 3.1.18, 2.1.29<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                     | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.7.0**               | _64bit Windows Server 2016 v2.7.0 running IIS 10.0_        | .NET 5.0.9, supports 5.0.9, 3.1.18, 2.1.29<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                     | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.7.0**          | _64bit Windows Server Core 2016 v2.7.0 running IIS 10.0_   | .NET 5.0.9, supports 5.0.9, 3.1.18, 2.1.29<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                     | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.7.0**             | _64bit Windows Server 2012 R2 v2.7.0 running IIS 8.5_      | .NET Core 3.0.0, supports 3.0.0, 2.1.29<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.7.0** | _64bit Windows Server Core 2012 R2 v2.7.0 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.1.29<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | _64bit Windows Server 2012 v1.2.0 running IIS 8_           | .NET Core 2.2.8, supports 2.2.8, 2.1.29, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8        |
| **Windows Server 2012 with IIS 8 version 0.1.0**                  | _64bit Windows Server 2012 v0.1.0 running IIS 8_           | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                   | IIS 8        |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.7.0**               | 2021.08.11  | 3.15.1371        |           | 3.0.1124.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.7.0**          | 2021.08.11  | 3.15.1371        |           | 3.0.1124.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.7.0**               | 2021.08.11  | 3.15.1371        |           | 3.0.1124.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.7.0**          | 2021.08.11  | 3.15.1371        |           | 3.0.1124.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.7.0**             | 2021.08.11  | 3.15.1371        | 4.9.4419  | 3.0.1124.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.7.0** | 2021.08.11  | 3.15.1371        | 4.9.4419  | 3.0.1124.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | 2021.08.11  | 3.15.1371        | 4.9.4419  | 3.0.1124.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 with IIS 8 version 0.1.0**                  | 2021.08.11  | 3.15.1371        | 4.9.4419  | 3.0.1124.0 | 3.6        | 3.1.0     |

## July 20, 2021 – August 22, 2021

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between July 20, 2021 and August 22, 2021:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                                    | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.6.8**               | _64bit Windows Server 2019 v2.6.8 running IIS 10.0_        | .NET 5.0.8, supports 5.0.8, 3.1.17, 2.2.8, 2.1.28<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x              | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.6.8**          | _64bit Windows Server Core 2019 v2.6.8 running IIS 10.0_   | .NET 5.0.8, supports 5.0.8, 3.1.17, 2.2.8, 2.1.28<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x              | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.6.8**               | _64bit Windows Server 2016 v2.6.8 running IIS 10.0_        | .NET 5.0.8, supports 5.0.8, 3.1.17, 2.2.8, 2.1.28<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x              | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.6.8**          | _64bit Windows Server Core 2016 v2.6.8 running IIS 10.0_   | .NET 5.0.8, supports 5.0.8, 3.1.17, 2.2.8, 2.1.28<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x              | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.6.8**             | _64bit Windows Server 2012 R2 v2.6.8 running IIS 8.5_      | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.28<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                 | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.6.8** | _64bit Windows Server Core 2012 R2 v2.6.8 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.28<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                 | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | _64bit Windows Server 2012 v1.2.0 running IIS 8_           | .NET Core 2.2.8, supports 2.2.8, 2.1.15, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8        |
| **Windows Server 2012 with IIS 8 version 0.1.0**                  | _64bit Windows Server 2012 v0.1.0 running IIS 8_           | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                   | IIS 8        |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.6.8**               | 2021.07.14  | 3.15.1350        |           | 3.0.1124.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.6.8**          | 2021.07.14  | 3.15.1350        |           | 3.0.1124.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.6.8**               | 2021.07.14  | 3.15.1350        |           | 3.0.1124.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.6.8**          | 2021.07.14  | 3.15.1350        |           | 3.0.1124.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.6.8**             | 2021.07.14  | 3.15.1350        | 4.9.4419  | 3.0.1124.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.6.8** | 2021.07.14  | 3.15.1350        | 4.9.4419  | 3.0.1124.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | 2021.07.14  | 3.15.1350        | 4.9.4419  | 3.0.1124.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 with IIS 8 version 0.1.0**                  | 2021.07.14  | 3.15.1350        | 4.9.4419  | 3.0.1124.0 | 3.6        | 3.1.0     |

## July 2, 2021 – July 19, 2021

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between July 2, 2021 and July 19, 2021:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                                    | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.6.7**               | _64bit Windows Server 2019 v2.6.7 running IIS 10.0_        | .NET 5.0.7, supports 5.0.7, 3.1.16, 2.2.8, 2.1.28<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x              | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.6.7**          | _64bit Windows Server Core 2019 v2.6.7 running IIS 10.0_   | .NET 5.0.7, supports 5.0.7, 3.1.16, 2.2.8, 2.1.28<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x              | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.6.7**               | _64bit Windows Server 2016 v2.6.7 running IIS 10.0_        | .NET 5.0.7, supports 5.0.7, 3.1.16, 2.2.8, 2.1.28<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x              | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.6.7**          | _64bit Windows Server Core 2016 v2.6.7 running IIS 10.0_   | .NET 5.0.7, supports 5.0.7, 3.1.16, 2.2.8, 2.1.28<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x              | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.6.7**             | _64bit Windows Server 2012 R2 v2.6.7 running IIS 8.5_      | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.28<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                 | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.6.7** | _64bit Windows Server Core 2012 R2 v2.6.7 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.28<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                 | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | _64bit Windows Server 2012 v1.2.0 running IIS 8_           | .NET Core 2.2.8, supports 2.2.8, 2.1.15, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8        |
| **Windows Server 2012 with IIS 8 version 0.1.0**                  | _64bit Windows Server 2012 v0.1.0 running IIS 8_           | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                   | IIS 8        |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.6.7**               | 2021.06.09  | 3.15.1326        |           | 3.0.1124.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.6.7**          | 2021.06.09  | 3.15.1326        |           | 3.0.1124.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.6.7**               | 2021.06.09  | 3.15.1326        |           | 3.0.1124.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.6.7**          | 2021.06.09  | 3.15.1326        |           | 3.0.1124.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.6.7**             | 2021.06.09  | 3.15.1326        | 4.9.4419  | 3.0.1124.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.6.7** | 2021.06.09  | 3.15.1326        | 4.9.4419  | 3.0.1124.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | 2020.02.12  | 3.15.945         | 4.9.3865  | 2.3.722.0  | 3.6        | 3.1.0     |
| **Windows Server 2012 with IIS 8 version 0.1.0**                  | 2020.02.12  | 3.15.945         | 4.9.3865  | 2.3.722.0  | 3.6        | 3.1.0     |

## June 3, 2021 – July 1, 2021

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between June 3, 2021 and July 1, 2021:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                                    | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.6.6**               | _64bit Windows Server 2019 v2.6.6 running IIS 10.0_        | .NET 5.0.6, supports 5.0.6, 3.1.15, 2.2.8, 2.1.28<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x              | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.6.6**          | _64bit Windows Server Core 2019 v2.6.6 running IIS 10.0_   | .NET 5.0.6, supports 5.0.6, 3.1.15, 2.2.8, 2.1.28<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x              | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.6.6**               | _64bit Windows Server 2016 v2.6.6 running IIS 10.0_        | .NET 5.0.6, supports 5.0.6, 3.1.15, 2.2.8, 2.1.28<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x              | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.6.6**          | _64bit Windows Server Core 2016 v2.6.6 running IIS 10.0_   | .NET 5.0.6, supports 5.0.6, 3.1.15, 2.2.8, 2.1.28<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x              | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.6.6**             | _64bit Windows Server 2012 R2 v2.6.6 running IIS 8.5_      | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.28<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                 | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.6.6** | _64bit Windows Server Core 2012 R2 v2.6.6 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.28<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                 | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | _64bit Windows Server 2012 v1.2.0 running IIS 8_           | .NET Core 2.2.8, supports 2.2.8, 2.1.15, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8        |
| **Windows Server 2012 with IIS 8 version 0.1.0**                  | _64bit Windows Server 2012 v0.1.0 running IIS 8_           | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                   | IIS 8        |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------- | --------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.6.6**               | 2021.05.11  | 3.15.1302        |           | 3.0.529.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.6.6**          | 2021.05.11  | 3.15.1302        |           | 3.0.529.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.6.6**               | 2021.05.11  | 3.15.1302        |           | 3.0.529.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.6.6**          | 2021.05.11  | 3.15.1302        |           | 3.0.529.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.6.6**             | 2021.05.11  | 3.15.1302        | 4.9.4381  | 3.0.529.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.6.6** | 2021.05.11  | 3.15.1302        | 4.9.4381  | 3.0.529.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | 2020.02.12  | 3.15.945         | 4.9.3865  | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 with IIS 8 version 0.1.0**                  | 2020.02.12  | 3.15.945         | 4.9.3865  | 2.3.722.0 | 3.6        | 3.1.0     |

## April 22, 2021 – June 2, 2021

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between April 22, 2021 and June 2, 2021:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                       | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.6.5**               | _64bit Windows Server 2019 v2.6.5 running IIS 10.0_        | .NET 5.0.5, supports 5.0.5, 3.1.14, 2.2.8, 2.1.27<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.6.5**          | _64bit Windows Server Core 2019 v2.6.5 running IIS 10.0_   | .NET 5.0.5, supports 5.0.5, 3.1.14, 2.2.8, 2.1.27<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.6.5**               | _64bit Windows Server 2016 v2.6.5 running IIS 10.0_        | .NET 5.0.5, supports 5.0.5, 3.1.14, 2.2.8, 2.1.27<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.6.5**          | _64bit Windows Server Core 2016 v2.6.5 running IIS 10.0_   | .NET 5.0.5, supports 5.0.5, 3.1.14, 2.2.8, 2.1.27<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.6.5**             | _64bit Windows Server 2012 R2 v2.6.5 running IIS 8.5_      | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.27<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x    | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.6.5** | _64bit Windows Server Core 2012 R2 v2.6.5 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.27<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x    | IIS 8.5      |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------- | --------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.6.5**               | 2021.04.14  | 3.15.1280        |           | 3.0.529.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.6.5**          | 2021.04.14  | 3.15.1280        |           | 3.0.529.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.6.5**               | 2021.04.14  | 3.15.1280        |           | 3.0.529.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.6.5**          | 2021.04.14  | 3.15.1280        |           | 3.0.529.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.6.5**             | 2021.04.14  | 3.15.1280        | 4.9.4326  | 3.0.431.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.6.5** | 2021.04.14  | 3.15.1280        | 4.9.4326  | 3.0.431.0 | 3.6        | 3.2.0     |

## March 19, 2021 – April 21, 2021

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between March 19, 2021 and April 21, 2021:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                       | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.6.4**               | _64bit Windows Server 2019 v2.6.4 running IIS 10.0_        | .NET 5.0.4, supports 5.0.4, 3.1.13, 2.2.8, 2.1.26<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.6.4**          | _64bit Windows Server Core 2019 v2.6.4 running IIS 10.0_   | .NET 5.0.4, supports 5.0.4, 3.1.13, 2.2.8, 2.1.26<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.6.4**               | _64bit Windows Server 2016 v2.6.4 running IIS 10.0_        | .NET 5.0.4, supports 5.0.4, 3.1.13, 2.2.8, 2.1.26<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.6.4**          | _64bit Windows Server Core 2016 v2.6.4 running IIS 10.0_   | .NET 5.0.4, supports 5.0.4, 3.1.13, 2.2.8, 2.1.26<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.6.4**             | _64bit Windows Server 2012 R2 v2.6.4 running IIS 8.5_      | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.26<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x    | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.6.4** | _64bit Windows Server Core 2012 R2 v2.6.4 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.26<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x    | IIS 8.5      |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------- | --------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.6.4**               | 2021.03.10  | 3.15.1248        |           | 3.0.529.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.6.4**          | 2021.03.10  | 3.15.1248        |           | 3.0.529.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.6.4**               | 2021.03.10  | 3.15.1248        |           | 3.0.529.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.6.4**          | 2021.03.10  | 3.15.1248        |           | 3.0.529.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.6.4**             | 2021.03.10  | 3.15.1248        | 4.9.4326  | 3.0.431.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.6.4** | 2021.03.10  | 3.15.1248        | 4.9.4326  | 3.0.431.0 | 3.6        | 3.2.0     |

## February 16, 2021 – March 18, 2021

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between February 16, 2021 and March 18, 2021:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                       | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.6.3**               | _64bit Windows Server 2019 v2.6.3 running IIS 10.0_        | .NET 5.0.3, supports 5.0.3, 3.1.12, 2.2.8, 2.1.25<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.6.3**          | _64bit Windows Server Core 2019 v2.6.3 running IIS 10.0_   | .NET 5.0.3, supports 5.0.3, 3.1.12, 2.2.8, 2.1.25<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.6.3**               | _64bit Windows Server 2016 v2.6.3 running IIS 10.0_        | .NET 5.0.3, supports 5.0.3, 3.1.12, 2.2.8, 2.1.25<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.6.3**          | _64bit Windows Server Core 2016 v2.6.3 running IIS 10.0_   | .NET 5.0.3, supports 5.0.3, 3.1.12, 2.2.8, 2.1.25<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.6.3**             | _64bit Windows Server 2012 R2 v2.6.3 running IIS 8.5_      | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.25<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x    | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.6.3** | _64bit Windows Server Core 2012 R2 v2.6.3 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.25<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x    | IIS 8.5      |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------- | --------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.6.3**               | 2021.02.10  | 3.15.1224        |           | 3.0.431.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.6.3**          | 2021.02.10  | 3.15.1224        |           | 3.0.431.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.6.3**               | 2021.02.10  | 3.15.1224        |           | 3.0.431.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.6.3**          | 2021.02.10  | 3.15.1224        |           | 3.0.431.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.6.3**             | 2021.02.10  | 3.15.1224        | 4.9.4279  | 2.3.871.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.6.3** | 2021.02.10  | 3.15.1224        | 4.9.4279  | 2.3.871.0 | 3.6        | 3.2.0     |

## January 22, 2021 – February 15, 2021

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between January 22, 2021 and February 15, 2021:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                       | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.6.2**               | _64bit Windows Server 2019 v2.6.2 running IIS 10.0_        | .NET 5.0.2, supports 5.0.2, 3.1.11, 2.2.8, 2.1.24<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.6.2**          | _64bit Windows Server Core 2019 v2.6.2 running IIS 10.0_   | .NET 5.0.2, supports 5.0.2, 3.1.11, 2.2.8, 2.1.24<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.6.2**               | _64bit Windows Server 2016 v2.6.2 running IIS 10.0_        | .NET 5.0.2, supports 5.0.2, 3.1.11, 2.2.8, 2.1.24<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.6.2**          | _64bit Windows Server Core 2016 v2.6.2 running IIS 10.0_   | .NET 5.0.2, supports 5.0.2, 3.1.11, 2.2.8, 2.1.24<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.6.2**             | _64bit Windows Server 2012 R2 v2.6.2 running IIS 8.5_      | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.24<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x    | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.6.2** | _64bit Windows Server Core 2012 R2 v2.6.2 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.24<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x    | IIS 8.5      |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------- | --------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.6.2**               | 2021.01.13  | 3.15.1204        |           | 3.0.431.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.6.2**          | 2021.01.13  | 3.15.1204        |           | 3.0.431.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.6.2**               | 2021.01.13  | 3.15.1204        |           | 3.0.431.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.6.2**          | 2021.01.13  | 3.15.1204        |           | 3.0.431.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.6.2**             | 2021.01.13  | 3.15.1204        | 4.9.4279  | 2.3.871.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.6.2** | 2021.01.13  | 3.15.1204        | 4.9.4279  | 2.3.871.0 | 3.6        | 3.2.0     |

## January 7, 2021 – January 21, 2021

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between January 7, 2021 and January 21, 2021:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                       | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.6.1**               | _64bit Windows Server 2019 v2.6.1 running IIS 10.0_        | .NET 5.0.0, supports 5.0.0, 3.1.10, 2.2.8, 2.1.23<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.6.1**          | _64bit Windows Server Core 2019 v2.6.1 running IIS 10.0_   | .NET 5.0.0, supports 5.0.0, 3.1.10, 2.2.8, 2.1.23<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.6.1**               | _64bit Windows Server 2016 v2.6.1 running IIS 10.0_        | .NET 5.0.0, supports 5.0.0, 3.1.10, 2.2.8, 2.1.23<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.6.1**          | _64bit Windows Server Core 2016 v2.6.1 running IIS 10.0_   | .NET 5.0.0, supports 5.0.0, 3.1.10, 2.2.8, 2.1.23<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.6.1**             | _64bit Windows Server 2012 R2 v2.6.1 running IIS 8.5_      | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.23<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x    | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.6.1** | _64bit Windows Server Core 2012 R2 v2.6.1 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.23<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x    | IIS 8.5      |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.6.1**               | 2020.12.09  | 3.15.1181        |           | 2.3.1644.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.6.1**          | 2020.12.09  | 3.15.1181        |           | 2.3.1644.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.6.1**               | 2020.12.09  | 3.15.1181        |           | 2.3.1644.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.6.1**          | 2020.12.09  | 3.15.1181        |           | 2.3.1644.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.6.1**             | 2020.12.09  | 3.15.1181        | 4.9.4279  | 2.3.871.0  | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.6.1** | 2020.12.09  | 3.15.1181        | 4.9.4279  | 2.3.871.0  | 3.6        | 3.2.0     |

## November 20, 2020 – January 6, 2021

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between November 20, 2020 and January 6, 2021:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                       | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.6.0**               | _64bit Windows Server 2019 v2.6.0 running IIS 10.0_        | .NET 5.0.0, supports 5.0.0, 3.1.10, 2.2.8, 2.1.23<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.6.0**          | _64bit Windows Server Core 2019 v2.6.0 running IIS 10.0_   | .NET 5.0.0, supports 5.0.0, 3.1.10, 2.2.8, 2.1.23<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.6.0**               | _64bit Windows Server 2016 v2.6.0 running IIS 10.0_        | .NET 5.0.0, supports 5.0.0, 3.1.10, 2.2.8, 2.1.23<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.6.0**          | _64bit Windows Server Core 2016 v2.6.0 running IIS 10.0_   | .NET 5.0.0, supports 5.0.0, 3.1.10, 2.2.8, 2.1.23<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.6.0**             | _64bit Windows Server 2012 R2 v2.6.0 running IIS 8.5_      | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.23<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x    | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.6.0** | _64bit Windows Server Core 2012 R2 v2.6.0 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.23<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x    | IIS 8.5      |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config | SSM Agent  | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------- | ---------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.6.0**               | 2020.11.11  | 3.15.1160        |           | 2.3.1644.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.6.0**          | 2020.11.11  | 3.15.1160        |           | 2.3.1644.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.6.0**               | 2020.11.11  | 3.15.1160        |           | 2.3.1644.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.6.0**          | 2020.11.11  | 3.15.1160        |           | 2.3.1644.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.6.0**             | 2020.11.11  | 3.15.1160        | 4.9.4222  | 2.3.842.0  | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.6.0** | 2020.11.11  | 3.15.1160        | 4.9.4222  | 2.3.842.0  | 3.6        | 3.2.0     |

## November 5, 2020 – November 19, 2020

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between November 5, 2020 and November 19, 2020:

### Configuration basics

| Platform Version                                                   | Solution Stack Name                                         | Framework                                                                                    | Proxy Server |
| ------------------------------------------------------------------ | ----------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.5.11**               | _64bit Windows Server 2019 v2.5.11 running IIS 10.0_        | .NET Core 3.1.9, supports 3.1.9, 2.2.8, 2.1.23<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.5.11**          | _64bit Windows Server Core 2019 v2.5.11 running IIS 10.0_   | .NET Core 3.1.9, 2.2.8, 2.1.23, supports<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x       | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.5.11**               | _64bit Windows Server 2016 v2.5.11 running IIS 10.0_        | .NET Core 3.1.9, 2.2.8, 2.1.23, supports<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x       | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.5.11**          | _64bit Windows Server Core 2016 v2.5.11 running IIS 10.0_   | .NET Core 3.1.9, 2.2.8, 2.1.23, supports<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x       | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.5.11**             | _64bit Windows Server 2012 R2 v2.5.11 running IIS 8.5_      | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.23<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.5.11** | _64bit Windows Server Core 2012 R2 v2.5.11 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.23<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5      |

### More details

| Platform Version                                                   | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X-Ray |
| ------------------------------------------------------------------ | ----------- | ---------------- | --------- | --------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.5.11**               | 2020.10.14  | 3.15.1140        |           | 2.3.842.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.5.11**          | 2020.10.14  | 3.15.1140        |           | 2.3.842.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.5.11**               | 2020.10.14  | 3.15.1140        |           | 2.3.842.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.5.11**          | 2020.10.14  | 3.15.1140        |           | 2.3.842.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.5.11**             | 2020.10.14  | 3.15.1140        | 4.9.4222  | 2.3.842.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.5.11** | 2020.10.14  | 3.15.1140        | 4.9.4222  | 2.3.842.0 | 3.6        | 3.2.0     |

## October 7, 2020 – November 4, 2020

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between October 7, 2020 and November 4, 2020:

### Configuration basics

| Platform Version                                                   | Solution Stack Name                                         | Framework                                                                                    | Proxy Server |
| ------------------------------------------------------------------ | ----------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.5.10**               | _64bit Windows Server 2019 v2.5.10 running IIS 10.0_        | .NET Core 3.1.8, supports 3.1.8, 2.2.8, 2.1.22<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.5.10**          | _64bit Windows Server Core 2019 v2.5.10 running IIS 10.0_   | .NET Core 3.1.8, supports 3.1.8, 2.2.8, 2.1.22<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.5.10**               | _64bit Windows Server 2016 v2.5.10 running IIS 10.0_        | .NET Core 3.1.8, supports 3.1.8, 2.2.8, 2.1.22<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.5.10**          | _64bit Windows Server Core 2016 v2.5.10 running IIS 10.0_   | .NET Core 3.1.8, supports 3.1.8, 2.2.8, 2.1.22<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.5.10**             | _64bit Windows Server 2012 R2 v2.5.10 running IIS 8.5_      | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.22<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.5.10** | _64bit Windows Server Core 2012 R2 v2.5.10 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.22<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5      |

### More details

| Platform Version                                                   | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X-Ray |
| ------------------------------------------------------------------ | ----------- | ---------------- | --------- | --------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.5.10**               | 2020.09.09  | 3.15.1110        |           | 2.3.842.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.5.10**          | 2020.09.09  | 3.15.1110        |           | 2.3.842.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.5.10**               | 2020.09.09  | 3.15.1110        |           | 2.3.842.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.5.10**          | 2020.09.09  | 3.15.1110        |           | 2.3.842.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.5.10**             | 2020.09.09  | 3.15.1110        | 4.9.4222  | 2.3.842.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.5.10** | 2020.09.09  | 3.15.1110        | 4.9.4222  | 2.3.842.0 | 3.6        | 3.2.0     |

## September 4, 2020 – October 6, 2020

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between September 4, 2020 and October 6, 2020:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                    | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.5.9**               | _64bit Windows Server 2019 v2.5.9 running IIS 10.0_        | .NET Core 3.1.7, supports 3.1.7, 2.2.8, 2.1.21<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.5.9**          | _64bit Windows Server Core 2019 v2.5.9 running IIS 10.0_   | .NET Core 3.1.7, supports 3.1.7, 2.2.8, 2.1.21<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.5.9**               | _64bit Windows Server 2016 v2.5.9 running IIS 10.0_        | .NET Core 3.1.7, supports 3.1.7, 2.2.8, 2.1.21<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.5.9**          | _64bit Windows Server Core 2016 v2.5.9 running IIS 10.0_   | .NET Core 3.1.7, supports 3.1.7, 2.2.8, 2.1.21<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.5.9**             | _64bit Windows Server 2012 R2 v2.5.9 running IIS 8.5_      | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.21<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.5.9** | _64bit Windows Server Core 2012 R2 v2.5.9 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.21<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5      |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------- | --------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.5.9**               | 2020.08.12  | 3.15.1084        |           | 2.3.842.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.5.9**          | 2020.08.12  | 3.15.1084        |           | 2.3.842.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.5.9**               | 2020.08.12  | 3.15.1084        |           | 2.3.842.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.5.9**          | 2020.08.12  | 3.15.1084        |           | 2.3.842.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.5.9**             | 2020.08.12  | 3.15.1084        | 4.9.4222  | 2.3.842.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.5.9** | 2020.08.12  | 3.15.1084        | 4.9.4222  | 2.3.842.0 | 3.6        | 3.2.0     |

## July 28, 2020 – September 3, 2020

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between July 28, 2020 and September 3, 2020:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                    | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.5.8**               | _64bit Windows Server 2019 v2.5.8 running IIS 10.0_        | .NET Core 3.1.6, supports 3.1.6, 2.2.8, 2.1.20<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.5.8**          | _64bit Windows Server Core 2019 v2.5.8 running IIS 10.0_   | .NET Core 3.1.6, supports 3.1.6, 2.2.8, 2.1.20<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.5.8**               | _64bit Windows Server 2016 v2.5.8 running IIS 10.0_        | .NET Core 3.1.6, supports 3.1.6, 2.2.8, 2.1.20<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.5.8**          | _64bit Windows Server Core 2016 v2.5.8 running IIS 10.0_   | .NET Core 3.1.6, supports 3.1.6, 2.2.8, 2.1.20<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.5.8**             | _64bit Windows Server 2012 R2 v2.5.8 running IIS 8.5_      | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.20<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.5.8** | _64bit Windows Server Core 2012 R2 v2.5.8 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.20<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5      |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------- | --------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.5.8**               | 2020.07.15  | 3.15.1064        |           | 2.3.842.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.5.8**          | 2020.07.15  | 3.15.1064        |           | 2.3.842.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.5.8**               | 2020.07.15  | 3.15.1064        |           | 2.3.842.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.5.8**          | 2020.07.15  | 3.15.1064        |           | 2.3.842.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.5.8**             | 2020.07.15  | 3.15.1064        | 4.9.4222  | 2.3.842.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.5.8** | 2020.07.15  | 3.15.1064        | 4.9.4222  | 2.3.842.0 | 3.6        | 3.2.0     |

## June 29, 2020 – July 27, 2020

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between June 29, 2020 and July 27, 2020:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                    | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.5.7**               | _64bit Windows Server 2019 v2.5.7 running IIS 10.0_        | .NET Core 3.1.5, supports 3.1.5, 2.2.8, 2.1.19<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.5.7**          | _64bit Windows Server Core 2019 v2.5.7 running IIS 10.0_   | .NET Core 3.1.5, supports 3.1.5, 2.2.8, 2.1.19<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.5.7**               | _64bit Windows Server 2016 v2.5.7 running IIS 10.0_        | .NET Core 3.1.5, supports 3.1.5, 2.2.8, 2.1.19<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.5.7**          | _64bit Windows Server Core 2016 v2.5.7 running IIS 10.0_   | .NET Core 3.1.5, supports 3.1.5, 2.2.8, 2.1.19<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.5.7**             | _64bit Windows Server 2012 R2 v2.5.7 running IIS 8.5_      | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.19<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.5.7** | _64bit Windows Server Core 2012 R2 v2.5.7 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.19<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5      |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------- | --------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.5.7**               | 2020.06.10  | 3.15.1034        |           | 2.3.842.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.5.7**          | 2020.06.10  | 3.15.1034        |           | 2.3.842.0 | 3.6        | 3.2.0     |
| **Windows Server 2016 with IIS 10.0 version 2.5.7**               | 2020.06.10  | 3.15.1034        |           | 2.3.842.0 | 3.6        | 3.2.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.5.7**          | 2020.06.10  | 3.15.1034        |           | 2.3.842.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.5.7**             | 2020.06.10  | 3.15.1034        | 4.9.4222  | 2.3.842.0 | 3.6        | 3.2.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.5.7** | 2020.06.10  | 3.15.1034        | 4.9.4222  | 2.3.842.0 | 3.6        | 3.2.0     |

## May 20, 2020 – June 28, 2020

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between May 20, 2020 and June 28, 2020:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                    | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.5.6**               | _64bit Windows Server 2019 v2.5.6 running IIS 10.0_        | .NET Core 3.1.4, supports 3.1.4, 2.2.8, 2.1.18<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.5.6**          | _64bit Windows Server Core 2019 v2.5.6 running IIS 10.0_   | .NET Core 3.1.4, supports 3.1.4, 2.2.8, 2.1.18<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.5.6**               | _64bit Windows Server 2016 v2.5.6 running IIS 10.0_        | .NET Core 3.1.4, supports 3.1.4, 2.2.8, 2.1.18<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.5.6**          | _64bit Windows Server Core 2016 v2.5.6 running IIS 10.0_   | .NET Core 3.1.4, supports 3.1.4, 2.2.8, 2.1.18<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.5.6**             | _64bit Windows Server 2012 R2 v2.5.6 running IIS 8.5_      | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.18<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.5.6** | _64bit Windows Server Core 2012 R2 v2.5.6 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.18<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5      |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------- | --------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.5.6**               | 2020.05.13  | 3.15.1013        |           | 2.3.842.0 | 3.6        | 3.1.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.5.6**          | 2020.05.13  | 3.15.1013        |           | 2.3.842.0 | 3.6        | 3.1.0     |
| **Windows Server 2016 with IIS 10.0 version 2.5.6**               | 2020.05.13  | 3.15.1013        |           | 2.3.842.0 | 3.6        | 3.1.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.5.6**          | 2020.05.13  | 3.15.1013        |           | 2.3.842.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.5.6**             | 2020.05.13  | 3.15.1013        | 4.9.4222  | 2.3.842.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.5.6** | 2020.05.13  | 3.15.1013        | 4.9.4222  | 2.3.842.0 | 3.6        | 3.1.0     |

## May 1, 2020 – May 19, 2020

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between May 1, 2020 and May 19, 2020:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                    | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.5.5**               | _64bit Windows Server 2019 v2.5.5 running IIS 10.0_        | .NET Core 3.1.3, supports 3.1.3, 2.2.8, 2.1.17<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.5.5**          | _64bit Windows Server Core 2019 v2.5.5 running IIS 10.0_   | .NET Core 3.1.3, supports 3.1.3, 2.2.8, 2.1.17<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.5.5**               | _64bit Windows Server 2016 v2.5.5 running IIS 10.0_        | .NET Core 3.1.3, supports 3.1.3, 2.2.8, 2.1.17<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.5.5**          | _64bit Windows Server Core 2016 v2.5.5 running IIS 10.0_   | .NET Core 3.1.3, supports 3.1.3, 2.2.8, 2.1.17<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.5.5**             | _64bit Windows Server 2012 R2 v2.5.5 running IIS 8.5_      | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.17<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.5.5** | _64bit Windows Server Core 2012 R2 v2.5.5 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.17<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5      |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------- | --------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.5.5**               | 2020.04.15  | 3.15.998         |           | 2.3.842.0 | 3.6        | 3.1.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.5.5**          | 2020.04.15  | 3.15.998         |           | 2.3.842.0 | 3.6        | 3.1.0     |
| **Windows Server 2016 with IIS 10.0 version 2.5.5**               | 2020.04.15  | 3.15.998         |           | 2.3.842.0 | 3.6        | 3.1.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.5.5**          | 2020.04.15  | 3.15.998         |           | 2.3.842.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.5.5**             | 2020.04.15  | 3.15.998         | 4.9.4222  | 2.3.842.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.5.5** | 2020.04.15  | 3.15.998         | 4.9.4222  | 2.3.842.0 | 3.6        | 3.1.0     |

## March 31, 2020 – April 30, 2020

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between March 31, 2020 and April 30, 2020:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                    | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.5.2**               | _64bit Windows Server 2019 v2.5.2 running IIS 10.0_        | .NET Core 3.1.2, supports 3.1.2, 2.2.8, 2.1.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.5.2**          | _64bit Windows Server Core 2019 v2.5.2 running IIS 10.0_   | .NET Core 3.1.2, supports 3.1.2, 2.2.8, 2.1.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.5.2**               | _64bit Windows Server 2016 v2.5.2 running IIS 10.0_        | .NET Core 3.1.2, supports 3.1.2, 2.2.8, 2.1.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.5.2**          | _64bit Windows Server Core 2016 v2.5.2 running IIS 10.0_   | .NET Core 3.1.2, supports 3.1.2, 2.2.8, 2.1.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.5.2**             | _64bit Windows Server 2012 R2 v2.5.2 running IIS 8.5_      | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.5.2** | _64bit Windows Server Core 2012 R2 v2.5.2 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5      |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------- | --------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.5.2**               | 2020.03.11  | 3.15.969         |           | 2.3.814.0 | 3.6        | 3.1.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.5.2**          | 2020.03.11  | 3.15.969         |           | 2.3.814.0 | 3.6        | 3.1.0     |
| **Windows Server 2016 with IIS 10.0 version 2.5.2**               | 2020.03.11  | 3.15.969         |           | 2.3.814.0 | 3.6        | 3.1.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.5.2**          | 2020.03.11  | 3.15.969         |           | 2.3.814.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.5.2**             | 2020.03.11  | 3.15.969         | 4.9.4122  | 2.3.814.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.5.2** | 2020.03.11  | 3.15.969         | 4.9.4122  | 2.3.814.0 | 3.6        | 3.1.0     |

## February 24, 2020 – March 30, 2020

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between February 24, 2020 and March 30, 2020:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                                           | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.5.1**               | _64bit Windows Server 2019 v2.5.1 running IIS 10.0_        | .NET Core 3.1.1, supports 3.1.1, 2.2.8, 2.1.15<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.5.1**          | _64bit Windows Server Core 2019 v2.5.1 running IIS 10.0_   | .NET Core 3.1.1, supports 3.1.1, 2.2.8, 2.1.15<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.5.1**               | _64bit Windows Server 2016 v2.5.1 running IIS 10.0_        | .NET Core 3.1.1, supports 3.1.1, 2.2.8, 2.1.15<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.5.1**          | _64bit Windows Server Core 2016 v2.5.1 running IIS 10.0_   | .NET Core 3.1.1, supports 3.1.1, 2.2.8, 2.1.15<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.5.1**             | _64bit Windows Server 2012 R2 v2.5.1 running IIS 8.5_      | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.15<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.5.1** | _64bit Windows Server Core 2012 R2 v2.5.1 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.15<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 8.5      |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | _64bit Windows Server 2016 v1.2.0 running IIS 10.0_        | .NET Core 3.1.1, supports 3.1.1, 2.2.8, 2.1.15, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | _64bit Windows Server Core 2016 v1.2.0 running IIS 10.0_   | .NET Core 3.1.1, supports 3.1.1, 2.2.8, 2.1.15, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | _64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5_      | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.15, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | _64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.15, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | _64bit Windows Server 2012 v1.2.0 running IIS 8_           | .NET Core 2.2.8, supports 2.2.8, 2.1.15, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x        | IIS 8        |
| **Windows Server 2012 R2 with IIS 8.5**                           | _64bit Windows Server 2012 R2 running IIS 8.5_             | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                          | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | _64bit Windows Server Core 2012 R2 running IIS 8.5_        | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                          | IIS 8.5      |
| **Windows Server 2012 with IIS 8**                                | _64bit Windows Server 2012 running IIS 8_                  | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                          | IIS 8        |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------- | --------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.5.1**               | 2020.02.12  | 3.15.945         |           | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.5.1**          | 2020.02.12  | 3.15.945         |           | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2016 with IIS 10.0 version 2.5.1**               | 2020.02.12  | 3.15.945         |           | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.5.1**          | 2020.02.12  | 3.15.945         |           | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.5.1**             | 2020.02.12  | 3.15.945         | 4.9.3865  | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.5.1** | 2020.02.12  | 3.15.945         | 4.9.3865  | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | 2020.02.12  | 3.15.945         |           | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | 2020.02.12  | 3.15.945         |           | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | 2020.02.12  | 3.15.945         | 4.9.3865  | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | 2020.02.12  | 3.15.945         | 4.9.3865  | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | 2020.02.12  | 3.15.945         | 4.9.3865  | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 with IIS 8.5**                           | 2020.02.12  | 3.15.945         | 4.9.3865  | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | 2020.02.12  | 3.15.945         | 4.9.3865  | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 with IIS 8**                                | 2020.02.12  | 3.15.945         | 4.9.3865  | 2.3.722.0 | 3.6        | 3.1.0     |

## January 22, 2020 – February 23, 2020

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between January 22, 2020 and February 23, 2020:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                                           | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.5.0**               | _64bit Windows Server 2019 v2.5.0 running IIS 10.0_        | .NET Core 3.1.1, supports 3.1.1, 2.2.8, 2.1.15<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.5.0**          | _64bit Windows Server Core 2019 v2.5.0 running IIS 10.0_   | .NET Core 3.1.1, supports 3.1.1, 2.2.8, 2.1.15<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.5.0**               | _64bit Windows Server 2016 v2.5.0 running IIS 10.0_        | .NET Core 3.1.1, supports 3.1.1, 2.2.8, 2.1.15<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.5.0**          | _64bit Windows Server Core 2016 v2.5.0 running IIS 10.0_   | .NET Core 3.1.1, supports 3.1.1, 2.2.8, 2.1.15<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.5.0**             | _64bit Windows Server 2012 R2 v2.5.0 running IIS 8.5_      | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.15<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.5.0** | _64bit Windows Server Core 2012 R2 v2.5.0 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.15<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 8.5      |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | _64bit Windows Server 2016 v1.2.0 running IIS 10.0_        | .NET Core 3.1.1, supports 3.1.1, 2.2.8, 2.1.15, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | _64bit Windows Server Core 2016 v1.2.0 running IIS 10.0_   | .NET Core 3.1.1, supports 3.1.1, 2.2.8, 2.1.15, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | _64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5_      | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.15, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | _64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.15, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | _64bit Windows Server 2012 v1.2.0 running IIS 8_           | .NET Core 2.2.8, supports 2.2.8, 2.1.15, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x        | IIS 8        |
| **Windows Server 2012 R2 with IIS 8.5**                           | _64bit Windows Server 2012 R2 running IIS 8.5_             | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                          | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | _64bit Windows Server Core 2012 R2 running IIS 8.5_        | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                          | IIS 8.5      |
| **Windows Server 2012 with IIS 8**                                | _64bit Windows Server 2012 running IIS 8_                  | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                          | IIS 8        |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------- | --------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.5.0**               | 2020.01.15  | 3.15.925         |           | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.5.0**          | 2020.01.15  | 3.15.925         |           | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2016 with IIS 10.0 version 2.5.0**               | 2020.01.15  | 3.15.925         |           | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.5.0**          | 2020.01.15  | 3.15.925         |           | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.5.0**             | 2020.01.15  | 3.15.925         | 4.9.3865  | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.5.0** | 2020.01.15  | 3.15.925         | 4.9.3865  | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | 2020.01.15  | 3.15.925         |           | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | 2020.01.15  | 3.15.925         |           | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | 2020.01.15  | 3.15.925         | 4.9.3865  | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | 2020.01.15  | 3.15.925         | 4.9.3865  | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | 2020.01.15  | 3.15.925         | 4.9.3865  | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 with IIS 8.5**                           | 2020.01.15  | 3.15.925         | 4.9.3865  | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | 2020.01.15  | 3.15.925         | 4.9.3865  | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 with IIS 8**                                | 2020.01.15  | 3.15.925         | 4.9.3865  | 2.3.722.0 | 3.6        | 3.1.0     |

## January 15, 2020 – January 21, 2020

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between January 15, 2020 and January 21, 2020:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                                           | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2019 with IIS 10.0 version 2.4.0**               | _64bit Windows Server 2019 v2.4.0 running IIS 10.0_        | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 10.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.4.0**          | _64bit Windows Server Core 2019 v2.4.0 running IIS 10.0_   | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 10.0     |
| **Windows Server 2016 with IIS 10.0 version 2.4.0**               | _64bit Windows Server 2016 v2.4.0 running IIS 10.0_        | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.4.0**          | _64bit Windows Server Core 2016 v2.4.0 running IIS 10.0_   | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.4.0**             | _64bit Windows Server 2012 R2 v2.4.0 running IIS 8.5_      | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.4.0** | _64bit Windows Server Core 2012 R2 v2.4.0 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 8.5      |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | _64bit Windows Server 2016 v1.2.0 running IIS 10.0_        | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | _64bit Windows Server Core 2016 v1.2.0 running IIS 10.0_   | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | _64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5_      | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | _64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | _64bit Windows Server 2012 v1.2.0 running IIS 8_           | .NET Core 2.2.8, supports 2.2.8, 2.1.14, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x        | IIS 8        |
| **Windows Server 2012 R2 with IIS 8.5**                           | _64bit Windows Server 2012 R2 running IIS 8.5_             | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                          | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | _64bit Windows Server Core 2012 R2 running IIS 8.5_        | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                          | IIS 8.5      |
| **Windows Server 2012 with IIS 8**                                | _64bit Windows Server 2012 running IIS 8_                  | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                          | IIS 8        |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------- | --------- | ---------- | --------- |
| **Windows Server 2019 with IIS 10.0 version 2.4.0**               | 2019.12.16  | 3.15.903         |           | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server Core 2019 with IIS 10.0 version 2.4.0**          | 2019.12.16  | 3.15.903         |           | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2016 with IIS 10.0 version 2.4.0**               | 2019.12.16  | 3.15.903         |           | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.4.0**          | 2019.12.16  | 3.15.903         |           | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.4.0**             | 2019.12.16  | 3.15.903         | 4.9.3865  | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.4.0** | 2019.12.16  | 3.15.903         | 4.9.3865  | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | 2019.12.16  | 3.15.903         |           | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | 2019.12.16  | 3.15.903         |           | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | 2019.12.16  | 3.15.903         | 4.9.3865  | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | 2019.12.16  | 3.15.903         | 4.9.3865  | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | 2019.12.16  | 3.15.903         | 4.9.3865  | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 with IIS 8.5**                           | 2019.12.16  | 3.15.903         | 4.9.3865  | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | 2019.12.16  | 3.15.903         | 4.9.3865  | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 with IIS 8**                                | 2019.12.16  | 3.15.903         | 4.9.3865  | 2.3.722.0 | 3.6        | 3.1.0     |

## December 23, 2019 – January 14, 2020

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between December 23, 2019 and January 14, 2020:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                                           | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2016 with IIS 10.0 version 2.3.2**               | _64bit Windows Server 2016 v2.3.2 running IIS 10.0_        | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.3.2**          | _64bit Windows Server Core 2016 v2.3.2 running IIS 10.0_   | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.3.2**             | _64bit Windows Server 2012 R2 v2.3.2 running IIS 8.5_      | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.3.2** | _64bit Windows Server Core 2012 R2 v2.3.2 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 8.5      |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | _64bit Windows Server 2016 v1.2.0 running IIS 10.0_        | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | _64bit Windows Server Core 2016 v1.2.0 running IIS 10.0_   | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | _64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5_      | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | _64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | _64bit Windows Server 2012 v1.2.0 running IIS 8_           | .NET Core 2.2.8, supports 2.2.8, 2.1.14, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x        | IIS 8        |
| **Windows Server 2012 R2 with IIS 8.5**                           | _64bit Windows Server 2012 R2 running IIS 8.5_             | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                          | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | _64bit Windows Server Core 2012 R2 running IIS 8.5_        | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                          | IIS 8.5      |
| **Windows Server 2012 with IIS 8**                                | _64bit Windows Server 2012 running IIS 8_                  | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                          | IIS 8        |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------- | --------- | ---------- | --------- |
| **Windows Server 2016 with IIS 10.0 version 2.3.2**               | 2019.12.16  | 3.15.903         |           | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.3.2**          | 2019.12.16  | 3.15.903         |           | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.3.2**             | 2019.12.16  | 3.15.903         | 4.9.3865  | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.3.2** | 2019.12.16  | 3.15.903         | 4.9.3865  | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | 2019.12.16  | 3.15.903         |           | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | 2019.12.16  | 3.15.903         |           | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | 2019.12.16  | 3.15.903         | 4.9.3865  | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | 2019.12.16  | 3.15.903         | 4.9.3865  | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | 2019.12.16  | 3.15.903         | 4.9.3865  | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 with IIS 8.5**                           | 2019.12.16  | 3.15.903         | 4.9.3865  | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | 2019.12.16  | 3.15.903         | 4.9.3865  | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 with IIS 8**                                | 2019.12.16  | 3.15.903         | 4.9.3865  | 2.3.722.0 | 3.6        | 3.1.0     |

## December 1, 2019 – December 22, 2019

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between December 1, 2019 and December 22, 2019:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                                           | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2016 with IIS 10.0 version 2.3.1**               | _64bit Windows Server 2016 v2.3.1 running IIS 10.0_        | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.3.1**          | _64bit Windows Server Core 2016 v2.3.1 running IIS 10.0_   | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.3.1**             | _64bit Windows Server 2012 R2 v2.3.1 running IIS 8.5_      | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.3.1** | _64bit Windows Server Core 2012 R2 v2.3.1 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 8.5      |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | _64bit Windows Server 2016 v1.2.0 running IIS 10.0_        | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | _64bit Windows Server Core 2016 v1.2.0 running IIS 10.0_   | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | _64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5_      | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | _64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.14, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | _64bit Windows Server 2012 v1.2.0 running IIS 8_           | .NET Core 2.2.8, supports 2.2.8, 2.1.14, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x        | IIS 8        |
| **Windows Server 2012 R2 with IIS 8.5**                           | _64bit Windows Server 2012 R2 running IIS 8.5_             | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                          | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | _64bit Windows Server Core 2012 R2 running IIS 8.5_        | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                          | IIS 8.5      |
| **Windows Server 2012 with IIS 8**                                | _64bit Windows Server 2012 running IIS 8_                  | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                          | IIS 8        |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------- | --------- | ---------- | --------- |
| **Windows Server 2016 with IIS 10.0 version 2.3.1**               | 2019.11.13  | 3.15.876         |           | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.3.1**          | 2019.11.13  | 3.15.876         |           | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.3.1**             | 2019.11.13  | 3.15.876         | 4.9.3865  | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.3.1** | 2019.11.13  | 3.15.876         | 4.9.3865  | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | 2019.11.13  | 3.15.876         |           | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | 2019.11.13  | 3.15.876         |           | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | 2019.11.13  | 3.15.876         | 4.9.3865  | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | 2019.11.13  | 3.15.876         | 4.9.3865  | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | 2019.11.13  | 3.15.876         | 4.9.3865  | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 with IIS 8.5**                           | 2019.11.13  | 3.15.876         | 4.9.3865  | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | 2019.11.13  | 3.15.876         | 4.9.3865  | 2.3.722.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 with IIS 8**                                | 2019.11.13  | 3.15.876         | 4.9.3865  | 2.3.722.0 | 3.6        | 3.1.0     |

## October 28, 2019 – November 30, 2019

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between October 28, 2019 and November 30, 2019:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                                           | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2016 with IIS 10.0 version 2.3.0**               | _64bit Windows Server 2016 v2.3.0 running IIS 10.0_        | .NET Core 3.0.0, supports 3.0.0, 2.2.7, 2.1.13<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.3.0**          | _64bit Windows Server Core 2016 v2.3.0 running IIS 10.0_   | .NET Core 3.0.0, supports 3.0.0, 2.2.7, 2.1.13<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.3.0**             | _64bit Windows Server 2012 R2 v2.3.0 running IIS 8.5_      | .NET Core 3.0.0, supports 3.0.0, 2.2.7, 2.1.13<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.3.0** | _64bit Windows Server Core 2012 R2 v2.3.0 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.2.7, 2.1.13<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 8.5      |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | _64bit Windows Server 2016 v1.2.0 running IIS 10.0_        | .NET Core 3.0.0, supports 3.0.0, 2.2.7, 2.1.13, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | _64bit Windows Server Core 2016 v1.2.0 running IIS 10.0_   | .NET Core 3.0.0, supports 3.0.0, 2.2.7, 2.1.13, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | _64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5_      | .NET Core 3.0.0, supports 3.0.0, 2.2.7, 2.1.13, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | _64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5_ | .NET Core 3.0.0, supports 3.0.0, 2.2.7, 2.1.13, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | _64bit Windows Server 2012 v1.2.0 running IIS 8_           | .NET Core 2.2.7, supports 2.2.7, 2.1.13, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x        | IIS 8        |
| **Windows Server 2012 R2 with IIS 8.5**                           | _64bit Windows Server 2012 R2 running IIS 8.5_             | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                          | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | _64bit Windows Server Core 2012 R2 running IIS 8.5_        | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                          | IIS 8.5      |
| **Windows Server 2012 with IIS 8**                                | _64bit Windows Server 2012 running IIS 8_                  | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                          | IIS 8        |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------- | --------- | ---------- | --------- |
| **Windows Server 2016 with IIS 10.0 version 2.3.0**               | 2019.10.09  | 3.15.846         |           | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.3.0**          | 2019.10.09  | 3.15.846         |           | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.3.0**             | 2019.10.09  | 3.15.846         | 4.9.3519  | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.3.0** | 2019.10.09  | 3.15.846         | 4.9.3519  | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | 2019.10.09  | 3.15.846         |           | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | 2019.10.09  | 3.15.846         |           | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | 2019.10.09  | 3.15.846         | 4.9.3519  | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | 2019.10.09  | 3.15.846         | 4.9.3519  | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | 2019.10.09  | 3.15.846         | 4.9.3519  | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 with IIS 8.5**                           | 2019.10.09  | 3.15.846         | 4.9.3519  | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | 2019.10.09  | 3.15.846         | 4.9.3519  | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 with IIS 8**                                | 2019.10.09  | 3.15.846         | 4.9.3519  | 2.3.634.0 | 3.6        | 3.1.0     |

## September 24, 2019 – October 27, 2019

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between September 24, 2019 and October 27, 2019:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                                    | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------ |
| **Windows Server 2016 with IIS 10.0 version 2.2.2**               | _64bit Windows Server 2016 v2.2.2 running IIS 10.0_        | .NET Core 2.2.7, supports 2.2.7, 2.1.13<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.2.2**          | _64bit Windows Server Core 2016 v2.2.2 running IIS 10.0_   | .NET Core 2.2.7, supports 2.2.7, 2.1.13<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.2.2**             | _64bit Windows Server 2012 R2 v2.2.2 running IIS 8.5_      | .NET Core 2.2.7, supports 2.2.7, 2.1.13<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.2.2** | _64bit Windows Server Core 2012 R2 v2.2.2 running IIS 8.5_ | .NET Core 2.2.7, supports 2.2.7, 2.1.13<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 8.5      |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | _64bit Windows Server 2016 v1.2.0 running IIS 10.0_        | .NET Core 2.2.7, supports 2.2.7, 2.1.13, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | _64bit Windows Server Core 2016 v1.2.0 running IIS 10.0_   | .NET Core 2.2.7, supports 2.2.7, 2.1.13, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | _64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5_      | .NET Core 2.2.7, supports 2.2.7, 2.1.13, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | _64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5_ | .NET Core 2.2.7, supports 2.2.7, 2.1.13, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | _64bit Windows Server 2012 v1.2.0 running IIS 8_           | .NET Core 2.2.7, supports 2.2.7, 2.1.13, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8        |
| **Windows Server 2012 R2 with IIS 8.5**                           | _64bit Windows Server 2012 R2 running IIS 8.5_             | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                   | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | _64bit Windows Server Core 2012 R2 running IIS 8.5_        | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                   | IIS 8.5      |
| **Windows Server 2012 with IIS 8**                                | _64bit Windows Server 2012 running IIS 8_                  | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                   | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | _64bit Windows Server 2008 R2 v1.2.0 running IIS 7.5_      | .NET Core 2.1.11, supports 2.1.11, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x       | IIS 7.5      |
| **Windows Server 2008 R2 with IIS 7.5**                           | _64bit Windows Server 2008 R2 running IIS 7.5_             | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                   | IIS 7.5      |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------- | --------- | ---------- | --------- |
| **Windows Server 2016 with IIS 10.0 version 2.2.2**               | 2019.09.11  | 3.15.826         |           | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.2.2**          | 2019.09.11  | 3.15.826         |           | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.2.2**             | 2019.09.11  | 3.15.826         | 4.9.3519  | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.2.2** | 2019.09.11  | 3.15.826         | 4.9.3519  | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | 2019.09.11  | 3.15.826         |           | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | 2019.09.11  | 3.15.826         |           | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | 2019.09.11  | 3.15.826         | 4.9.3519  | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | 2019.09.11  | 3.15.826         | 4.9.3519  | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | 2019.09.11  | 3.15.826         | 4.9.3519  | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 with IIS 8.5**                           | 2019.09.11  | 3.15.826         | 4.9.3519  | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | 2019.09.11  | 3.15.826         | 4.9.3519  | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 with IIS 8**                                | 2019.09.11  | 3.15.826         | 4.9.3519  | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | 2019.09.11  | 3.15.826         | 4.9.3519  | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server 2008 R2 with IIS 7.5**                           | 2019.09.11  | 3.15.826         | 4.9.3519  | 2.3.634.0 | 3.6        | 3.1.0     |

## August 26, 2019 – September 23, 2019

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between August 26, 2019 and September 23, 2019:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                                    | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------ |
| **Windows Server 2016 with IIS 10.0 version 2.2.1**               | _64bit Windows Server 2016 v2.2.1 running IIS 10.0_        | .NET Core 2.2.6, supports 2.2.6, 2.1.12<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.2.1**          | _64bit Windows Server Core 2016 v2.2.1 running IIS 10.0_   | .NET Core 2.2.6, supports 2.2.6, 2.1.12<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.2.1**             | _64bit Windows Server 2012 R2 v2.2.1 running IIS 8.5_      | .NET Core 2.2.6, supports 2.2.6, 2.1.12<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.2.1** | _64bit Windows Server Core 2012 R2 v2.2.1 running IIS 8.5_ | .NET Core 2.2.6, supports 2.2.6, 2.1.12<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 8.5      |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | _64bit Windows Server 2016 v1.2.0 running IIS 10.0_        | .NET Core 2.2.6, supports 2.2.6, 2.1.12, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | _64bit Windows Server Core 2016 v1.2.0 running IIS 10.0_   | .NET Core 2.2.6, supports 2.2.6, 2.1.12, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | _64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5_      | .NET Core 2.2.6, supports 2.2.6, 2.1.12, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | _64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5_ | .NET Core 2.2.6, supports 2.2.6, 2.1.12, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | _64bit Windows Server 2012 v1.2.0 running IIS 8_           | .NET Core 2.2.6, supports 2.2.6, 2.1.12, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8        |
| **Windows Server 2012 R2 with IIS 8.5**                           | _64bit Windows Server 2012 R2 running IIS 8.5_             | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                   | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | _64bit Windows Server Core 2012 R2 running IIS 8.5_        | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                   | IIS 8.5      |
| **Windows Server 2012 with IIS 8**                                | _64bit Windows Server 2012 running IIS 8_                  | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                   | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | _64bit Windows Server 2008 R2 v1.2.0 running IIS 7.5_      | .NET Core 2.1.11, supports 2.1.11, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x       | IIS 7.5      |
| **Windows Server 2008 R2 with IIS 7.5**                           | _64bit Windows Server 2008 R2 running IIS 7.5_             | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                   | IIS 7.5      |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------- | --------- | ---------- | --------- |
| **Windows Server 2016 with IIS 10.0 version 2.2.1**               | 2019.08.16  | 3.15.802         |           | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.2.1**          | 2019.08.16  | 3.15.802         |           | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.2.1**             | 2019.08.16  | 3.15.802         | 4.9.3519  | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.2.1** | 2019.08.16  | 3.15.802         | 4.9.3519  | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | 2019.08.16  | 3.15.802         |           | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | 2019.08.16  | 3.15.802         |           | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | 2019.08.16  | 3.15.802         | 4.9.3519  | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | 2019.08.16  | 3.15.802         | 4.9.3519  | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | 2019.08.16  | 3.15.802         | 4.9.3519  | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 with IIS 8.5**                           | 2019.08.16  | 3.15.802         | 4.9.3519  | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | 2019.08.16  | 3.15.802         | 4.9.3519  | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 with IIS 8**                                | 2019.08.16  | 3.15.802         | 4.9.3519  | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | 2019.08.16  | 3.15.802         | 4.9.3519  | 2.3.634.0 | 3.6        | 3.1.0     |
| **Windows Server 2008 R2 with IIS 7.5**                           | 2019.08.16  | 3.15.802         | 4.9.3519  | 2.3.634.0 | 3.6        | 3.1.0     |

## August 8, 2019 – August 25, 2019

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between August 8, 2019 and August 25, 2019:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                                    | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------ |
| **Windows Server 2016 with IIS 10.0 version 2.2.0**               | _64bit Windows Server 2016 v2.2.0 running IIS 10.0_        | .NET Core 2.2.6, supports 2.2.6, 2.1.12<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.2.0**          | _64bit Windows Server Core 2016 v2.2.0 running IIS 10.0_   | .NET Core 2.2.6, supports 2.2.6, 2.1.12<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.2.0**             | _64bit Windows Server 2012 R2 v2.2.0 running IIS 8.5_      | .NET Core 2.2.6, supports 2.2.6, 2.1.12<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.2.0** | _64bit Windows Server Core 2012 R2 v2.2.0 running IIS 8.5_ | .NET Core 2.2.6, supports 2.2.6, 2.1.12<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 8.5      |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | _64bit Windows Server 2016 v1.2.0 running IIS 10.0_        | .NET Core 2.2.6, supports 2.2.6, 2.1.12, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | _64bit Windows Server Core 2016 v1.2.0 running IIS 10.0_   | .NET Core 2.2.6, supports 2.2.6, 2.1.12, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | _64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5_      | .NET Core 2.2.6, supports 2.2.6, 2.1.12, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | _64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5_ | .NET Core 2.2.6, supports 2.2.6, 2.1.12, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | _64bit Windows Server 2012 v1.2.0 running IIS 8_           | .NET Core 2.2.6, supports 2.2.6, 2.1.12, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8        |
| **Windows Server 2012 R2 with IIS 8.5**                           | _64bit Windows Server 2012 R2 running IIS 8.5_             | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                   | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | _64bit Windows Server Core 2012 R2 running IIS 8.5_        | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                   | IIS 8.5      |
| **Windows Server 2012 with IIS 8**                                | _64bit Windows Server 2012 running IIS 8_                  | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                   | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | _64bit Windows Server 2008 R2 v1.2.0 running IIS 7.5_      | .NET Core 2.1.11, supports 2.1.11, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x       | IIS 7.5      |
| **Windows Server 2008 R2 with IIS 7.5**                           | _64bit Windows Server 2008 R2 running IIS 7.5_             | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                   | IIS 7.5      |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------- | --------- | ---------- | --------- |
| **Windows Server 2016 with IIS 10.0 version 2.2.0**               | 2019.07.12  | 3.15.780         |           | 2.3.542.0 | 3.6        | 3.1.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.2.0**          | 2019.07.12  | 3.15.780         |           | 2.3.542.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.2.0**             | 2019.07.12  | 3.15.780         | 4.9.3429  | 2.3.542.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.2.0** | 2019.07.12  | 3.15.780         | 4.9.3429  | 2.3.542.0 | 3.6        | 3.1.0     |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | 2019.07.12  | 3.15.780         |           | 2.3.542.0 | 3.6        | 3.1.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | 2019.07.12  | 3.15.780         |           | 2.3.542.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | 2019.07.12  | 3.15.780         | 4.9.3429  | 2.3.542.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | 2019.07.12  | 3.15.780         | 4.9.3429  | 2.3.542.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | 2019.07.12  | 3.15.780         | 4.9.3429  | 2.3.542.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 with IIS 8.5**                           | 2019.07.12  | 3.15.780         | 4.9.3429  | 2.3.542.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | 2019.07.12  | 3.15.780         | 4.9.3429  | 2.3.542.0 | 3.6        | 3.1.0     |
| **Windows Server 2012 with IIS 8**                                | 2019.07.12  | 3.15.780         | 4.9.3429  | 2.3.542.0 | 3.6        | 3.1.0     |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | 2019.07.12  | 3.15.780         | 4.9.3429  | 2.3.542.0 | 3.6        | 3.1.0     |
| **Windows Server 2008 R2 with IIS 7.5**                           | 2019.07.12  | 3.15.780         | 4.9.3429  | 2.3.542.0 | 3.6        | 3.1.0     |

## June 28, 2019 – August 7, 2019

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between June 28, 2019 and August 7, 2019:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                                    | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------ |
| **Windows Server 2016 with IIS 10.0 version 2.1.0**               | _64bit Windows Server 2016 v2.1.0 running IIS 10.0_        | .NET Core 2.2.5, supports 2.2.5, 2.1.11<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.1.0**          | _64bit Windows Server Core 2016 v2.1.0 running IIS 10.0_   | .NET Core 2.2.5, supports 2.2.5, 2.1.11<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.1.0**             | _64bit Windows Server 2012 R2 v2.1.0 running IIS 8.5_      | .NET Core 2.2.5, supports 2.2.5, 2.1.11<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.1.0** | _64bit Windows Server Core 2012 R2 v2.1.0 running IIS 8.5_ | .NET Core 2.2.5, supports 2.2.5, 2.1.11<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x                        | IIS 8.5      |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | _64bit Windows Server 2016 v1.2.0 running IIS 10.0_        | .NET Core 2.2.5, supports 2.2.5, 2.1.11, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | _64bit Windows Server Core 2016 v1.2.0 running IIS 10.0_   | .NET Core 2.2.5, supports 2.2.5, 2.1.11, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | _64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5_      | .NET Core 2.2.5, supports 2.2.5, 2.1.11, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | _64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5_ | .NET Core 2.2.5, supports 2.2.5, 2.1.11, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | _64bit Windows Server 2012 v1.2.0 running IIS 8_           | .NET Core 2.2.5, supports 2.2.5, 2.1.11, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8        |
| **Windows Server 2012 R2 with IIS 8.5**                           | _64bit Windows Server 2012 R2 running IIS 8.5_             | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                   | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | _64bit Windows Server Core 2012 R2 running IIS 8.5_        | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                   | IIS 8.5      |
| **Windows Server 2012 with IIS 8**                                | _64bit Windows Server 2012 running IIS 8_                  | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                   | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | _64bit Windows Server 2008 R2 v1.2.0 running IIS 7.5_      | .NET Core 2.1.11, supports 2.1.11, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.8, supports 4.x, 2.0, 1.x       | IIS 7.5      |
| **Windows Server 2008 R2 with IIS 7.5**                           | _64bit Windows Server 2008 R2 running IIS 7.5_             | .NET Framework 4.8, supports 4.x, 2.0, 1.x                                                                   | IIS 7.5      |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------- | --------- | ---------- | --------- |
| **Windows Server 2016 with IIS 10.0 version 2.1.0**               | 2019.06.12  | 3.15.756         |           | 2.3.542.0 | 3.6        | 3.0.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.1.0**          | 2019.06.12  | 3.15.756         |           | 2.3.542.0 | 3.6        | 3.0.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.1.0**             | 2019.06.12  | 3.15.756         | 4.9.3429  | 2.3.542.0 | 3.6        | 3.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.1.0** | 2019.06.12  | 3.15.756         | 4.9.3429  | 2.3.542.0 | 3.6        | 3.0.0     |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | 2019.06.12  | 3.15.756         |           | 2.3.542.0 | 3.6        | 1.0.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | 2019.06.12  | 3.15.756         |           | 2.3.542.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | 2019.06.12  | 3.15.756         | 4.9.3429  | 2.3.542.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | 2019.06.12  | 3.15.756         | 4.9.3429  | 2.3.542.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | 2019.06.12  | 3.15.756         | 4.9.3429  | 2.3.542.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5**                           | 2019.06.12  | 3.15.756         | 4.9.3429  | 2.3.542.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | 2019.06.12  | 3.15.756         | 4.9.3429  | 2.3.542.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8**                                | 2019.06.12  | 3.15.756         | 4.9.3429  | 2.3.542.0 | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | 2019.06.12  | 3.15.756         | 4.9.3429  | 2.3.542.0 | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5**                           | 2019.06.12  | 3.15.756         | 4.9.3429  | 2.3.542.0 | 3.6        | 1.0.0     |

## May 22, 2019 – June 27, 2019

The following Elastic Beanstalk platform versions for .NET on Windows Server were current between May 22, 2019 and June 27, 2019:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                                      | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2016 with IIS 10.0 version 2.0.4**               | _64bit Windows Server 2016 v2.0.4 running IIS 10.0_        | .NET Core 2.2.5, supports 2.2.5, 2.1.11<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x                        | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.0.4**          | _64bit Windows Server Core 2016 v2.0.4 running IIS 10.0_   | .NET Core 2.2.5, supports 2.2.5, 2.1.11<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x                        | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.0.4**             | _64bit Windows Server 2012 R2 v2.0.4 running IIS 8.5_      | .NET Core 2.2.5, supports 2.2.5, 2.1.11<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x                        | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.0.4** | _64bit Windows Server Core 2012 R2 v2.0.4 running IIS 8.5_ | .NET Core 2.2.5, supports 2.2.5, 2.1.11<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x                        | IIS 8.5      |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | _64bit Windows Server 2016 v1.2.0 running IIS 10.0_        | .NET Core 2.2.5, supports 2.2.5, 2.1.11, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | _64bit Windows Server Core 2016 v1.2.0 running IIS 10.0_   | .NET Core 2.2.5, supports 2.2.5, 2.1.11, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | _64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5_      | .NET Core 2.2.5, supports 2.2.5, 2.1.11, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | _64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5_ | .NET Core 2.2.5, supports 2.2.5, 2.1.11, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | _64bit Windows Server 2012 v1.2.0 running IIS 8_           | .NET Core 2.2.5, supports 2.2.5, 2.1.11, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8        |
| **Windows Server 2012 R2 with IIS 8.5**                           | _64bit Windows Server 2012 R2 running IIS 8.5_             | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                                   | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | _64bit Windows Server Core 2012 R2 running IIS 8.5_        | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                                   | IIS 8.5      |
| **Windows Server 2012 with IIS 8**                                | _64bit Windows Server 2012 running IIS 8_                  | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                                   | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | _64bit Windows Server 2008 R2 v1.2.0 running IIS 7.5_      | .NET Core 2.1.11, supports 2.1.11, 2.0.9, 1.1.14, 1.0.16<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x       | IIS 7.5      |
| **Windows Server 2008 R2 with IIS 7.5**                           | _64bit Windows Server 2008 R2 running IIS 7.5_             | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                                   | IIS 7.5      |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------- | --------- | ---------- | --------- |
| **Windows Server 2016 with IIS 10.0 version 2.0.4**               | 2019.05.15  | 3.15.735         |           | 2.3.542.0 | 3.6        | 3.0.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.0.4**          | 2019.05.15  | 3.15.735         |           | 2.3.542.0 | 3.6        | 3.0.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.0.4**             | 2019.05.15  | 3.15.735         | 4.9.3429  | 2.3.542.0 | 3.6        | 3.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.0.4** | 2019.05.15  | 3.15.735         | 4.9.3429  | 2.3.542.0 | 3.6        | 3.0.0     |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | 2019.05.15  | 3.15.735         |           | 2.3.542.0 | 3.6        | 1.0.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | 2019.05.15  | 3.15.735         |           | 2.3.542.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | 2019.05.15  | 3.15.735         | 4.9.3429  | 2.3.542.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | 2019.05.15  | 3.15.735         | 4.9.3429  | 2.3.542.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | 2019.05.15  | 3.15.735         | 4.9.3429  | 2.3.542.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5**                           | 2019.05.15  | 3.15.735         | 4.9.3429  | 2.3.542.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | 2019.05.15  | 3.15.735         | 4.9.3429  | 2.3.542.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8**                                | 2019.05.15  | 3.15.735         | 4.9.3429  | 2.3.542.0 | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | 2019.05.15  | 3.15.735         | 4.9.3429  | 2.3.542.0 | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5**                           | 2019.05.15  | 3.15.735         | 4.9.3429  | 2.3.542.0 | 3.6        | 1.0.0     |

## May 2, 2019 – May 21, 2019

The following Elastic Beanstalk platform versions for .NET were current during this date range:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                                      | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2016 with IIS 10.0 version 2.0.3**               | _64bit Windows Server 2016 v2.0.3 running IIS 10.0_        | .NET Core 2.2.4, supports 2.2.4, 2.1.10<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x                        | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.0.3**          | _64bit Windows Server Core 2016 v2.0.3 running IIS 10.0_   | .NET Core 2.2.4, supports 2.2.4, 2.1.10<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x                        | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.0.3**             | _64bit Windows Server 2012 R2 v2.0.3 running IIS 8.5_      | .NET Core 2.2.4, supports 2.2.4, 2.1.10<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x                        | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.0.3** | _64bit Windows Server Core 2012 R2 v2.0.3 running IIS 8.5_ | .NET Core 2.2.4, supports 2.2.4, 2.1.10<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x                        | IIS 8.5      |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | _64bit Windows Server 2016 v1.2.0 running IIS 10.0_        | .NET Core 2.2.4, supports 2.2.4, 2.1.10, 2.0.9, 1.1.12, 1.0.15<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | _64bit Windows Server Core 2016 v1.2.0 running IIS 10.0_   | .NET Core 2.2.4, supports 2.2.4, 2.1.10, 2.0.9, 1.1.12, 1.0.15<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | _64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5_      | .NET Core 2.2.4, supports 2.2.4, 2.1.10, 2.0.9, 1.1.12, 1.0.15<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | _64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5_ | .NET Core 2.2.4, supports 2.2.4, 2.1.10, 2.0.9, 1.1.12, 1.0.15<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | _64bit Windows Server 2012 v1.2.0 running IIS 8_           | .NET Core 2.2.4, supports 2.2.4, 2.1.10, 2.0.9, 1.1.12, 1.0.15<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | _64bit Windows Server 2008 R2 v1.2.0 running IIS 7.5_      | .NET Core 2.1.10, supports 2.1.10, 2.0.9, 1.1.12, 1.0.15<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x       | IIS 7.5      |
| **Windows Server 2012 R2 with IIS 8.5**                           | _64bit Windows Server 2012 R2 running IIS 8.5_             | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                                   | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | _64bit Windows Server Core 2012 R2 running IIS 8.5_        | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                                   | IIS 8.5      |
| **Windows Server 2012 with IIS 8**                                | _64bit Windows Server 2012 running IIS 8_                  | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                                   | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5**                           | _64bit Windows Server 2008 R2 running IIS 7.5_             | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                                   | IIS 7.5      |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config                                                                                                 | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------------------------------------------------------------------------------------------------------- | --------- | ---------- | --------- |
| **Windows Server 2016 with IIS 10.0 version 2.0.3**               | 2019.04.21  | 3.15.715         | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.3.444.0 | 3.6        | 3.0.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.0.3**          | 2019.04.21  | 3.15.715         | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.3.444.0 | 3.6        | 3.0.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.0.3**             | 2019.04.21  | 3.15.715         | 4.9.3289                                                                                                  | 2.3.444.0 | 3.6        | 3.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.0.3** | 2019.04.21  | 3.15.715         | 4.9.3289                                                                                                  | 2.3.444.0 | 3.6        | 3.0.0     |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | 2019.04.21  | 3.15.715         | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.3.444.0 | 3.6        | 1.0.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | 2019.04.21  | 3.15.715         | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.3.444.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | 2019.04.21  | 3.15.715         | 4.9.3289                                                                                                  | 2.3.444.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | 2019.04.21  | 3.15.715         | 4.9.3289                                                                                                  | 2.3.444.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | 2019.04.21  | 3.15.715         | 4.9.3289                                                                                                  | 2.3.444.0 | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | 2019.04.21  | 3.15.715         | 4.9.3289                                                                                                  | 2.3.444.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5**                           | 2019.04.21  | 3.15.715         | 4.9.3289                                                                                                  | 2.3.444.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | 2019.04.21  | 3.15.715         | 4.9.3289                                                                                                  | 2.3.444.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8**                                | 2019.04.21  | 3.15.715         | 4.9.3289                                                                                                  | 2.3.444.0 | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5**                           | 2019.04.21  | 3.15.715         | 4.9.3289                                                                                                  | 2.3.444.0 | 3.6        | 1.0.0     |

## March 27, 2019 – May 1, 2019

The following Elastic Beanstalk platform versions for .NET were current during this date range:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                                     | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2016 with IIS 10.0 version 2.0.2**               | _64bit Windows Server 2016 v2.0.2 running IIS 10.0_        | .NET Core 2.2.3, supports 2.2.3, 2.1.9<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x                        | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.0.2**          | _64bit Windows Server Core 2016 v2.0.2 running IIS 10.0_   | .NET Core 2.2.3, supports 2.2.3, 2.1.9<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x                        | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.0.2**             | _64bit Windows Server 2012 R2 v2.0.2 running IIS 8.5_      | .NET Core 2.2.3, supports 2.2.3, 2.1.9<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x                        | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.0.2** | _64bit Windows Server Core 2012 R2 v2.0.2 running IIS 8.5_ | .NET Core 2.2.3, supports 2.2.3, 2.1.9<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x                        | IIS 8.5      |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | _64bit Windows Server 2016 v1.2.0 running IIS 10.0_        | .NET Core 2.2.3, supports 2.2.3, 2.1.9, 2.0.9, 1.1.12, 1.0.15<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | _64bit Windows Server Core 2016 v1.2.0 running IIS 10.0_   | .NET Core 2.2.3, supports 2.2.3, 2.1.9, 2.0.9, 1.1.12, 1.0.15<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | _64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5_      | .NET Core 2.2.3, supports 2.2.3, 2.1.9, 2.0.9, 1.1.12, 1.0.15<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | _64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5_ | .NET Core 2.2.3, supports 2.2.3, 2.1.9, 2.0.9, 1.1.12, 1.0.15<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | _64bit Windows Server 2012 v1.2.0 running IIS 8_           | .NET Core 2.2.3, supports 2.2.3, 2.1.9, 2.0.9, 1.1.12, 1.0.15<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | _64bit Windows Server 2008 R2 v1.2.0 running IIS 7.5_      | .NET Core 2.1.9, supports 2.1.9, 2.0.9, 1.1.12, 1.0.15<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x        | IIS 7.5      |
| **Windows Server 2012 R2 with IIS 8.5**                           | _64bit Windows Server 2012 R2 running IIS 8.5_             | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                                  | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | _64bit Windows Server Core 2012 R2 running IIS 8.5_        | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                                  | IIS 8.5      |
| **Windows Server 2012 with IIS 8**                                | _64bit Windows Server 2012 running IIS 8_                  | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                                  | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5**                           | _64bit Windows Server 2008 R2 running IIS 7.5_             | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                                  | IIS 7.5      |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config                                                                                                 | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------------------------------------------------------------------------------------------------------- | --------- | ---------- | --------- |
| **Windows Server 2016 with IIS 10.0 version 2.0.2**               | 2019.03.13  | 3.15.693         | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.3.444.0 | 3.6        | 3.0.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.0.2**          | 2019.03.13  | 3.15.693         | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.3.444.0 | 3.6        | 3.0.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.0.2**             | 2019.03.13  | 3.15.693         | 4.9.3289                                                                                                  | 2.3.444.0 | 3.6        | 3.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.0.2** | 2019.03.13  | 3.15.693         | 4.9.3289                                                                                                  | 2.3.444.0 | 3.6        | 3.0.0     |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | 2019.03.13  | 3.15.693         | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.3.444.0 | 3.6        | 1.0.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | 2019.03.13  | 3.15.693         | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.3.444.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | 2019.03.13  | 3.15.693         | 4.9.3289                                                                                                  | 2.3.444.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | 2019.03.13  | 3.15.693         | 4.9.3289                                                                                                  | 2.3.444.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | 2019.03.13  | 3.15.693         | 4.9.3289                                                                                                  | 2.3.444.0 | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | 2019.03.13  | 3.15.693         | 4.9.3289                                                                                                  | 2.3.444.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5**                           | 2019.03.13  | 3.15.693         | 4.9.3289                                                                                                  | 2.3.444.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | 2019.03.13  | 3.15.693         | 4.9.3289                                                                                                  | 2.3.444.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8**                                | 2019.03.13  | 3.15.693         | 4.9.3289                                                                                                  | 2.3.444.0 | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5**                           | 2019.03.13  | 3.15.693         | 4.9.3289                                                                                                  | 2.3.444.0 | 3.6        | 1.0.0     |

## February 21, 2019 – March 26, 2019

The following Elastic Beanstalk platform versions for .NET were current during this date range:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                                     | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2016 with IIS 10.0 version 2.0.1**               | _64bit Windows Server 2016 v2.0.1 running IIS 10.0_        | .NET Core 2.2.2, supports 2.2.2, 2.1.8<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x                        | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.0.1**          | _64bit Windows Server Core 2016 v2.0.1 running IIS 10.0_   | .NET Core 2.2.2, supports 2.2.2, 2.1.8<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x                        | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.0.1**             | _64bit Windows Server 2012 R2 v2.0.1 running IIS 8.5_      | .NET Core 2.2.2, supports 2.2.2, 2.1.8<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x                        | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.0.1** | _64bit Windows Server Core 2012 R2 v2.0.1 running IIS 8.5_ | .NET Core 2.2.2, supports 2.2.2, 2.1.8<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x                        | IIS 8.5      |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | _64bit Windows Server 2016 v1.2.0 running IIS 10.0_        | .NET Core 2.2.2, supports 2.2.2, 2.1.8, 2.0.9, 1.1.11, 1.0.14<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | _64bit Windows Server Core 2016 v1.2.0 running IIS 10.0_   | .NET Core 2.2.2, supports 2.2.2, 2.1.8, 2.0.9, 1.1.11, 1.0.14<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | _64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5_      | .NET Core 2.2.2, supports 2.2.2, 2.1.8, 2.0.9, 1.1.11, 1.0.14<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | _64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5_ | .NET Core 2.2.2, supports 2.2.2, 2.1.8, 2.0.9, 1.1.11, 1.0.14<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | _64bit Windows Server 2012 v1.2.0 running IIS 8_           | .NET Core 2.2.2, supports 2.2.2, 2.1.8, 2.0.9, 1.1.11, 1.0.14<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | _64bit Windows Server 2008 R2 v1.2.0 running IIS 7.5_      | .NET Core 2.1.8, supports 2.1.8, 2.0.9, 1.1.11, 1.0.14<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x        | IIS 7.5      |
| **Windows Server 2012 R2 with IIS 8.5**                           | _64bit Windows Server 2012 R2 running IIS 8.5_             | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                                  | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | _64bit Windows Server Core 2012 R2 running IIS 8.5_        | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                                  | IIS 8.5      |
| **Windows Server 2012 with IIS 8**                                | _64bit Windows Server 2012 running IIS 8_                  | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                                  | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5**                           | _64bit Windows Server 2008 R2 running IIS 7.5_             | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                                  | IIS 7.5      |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config                                                                                                 | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------------------------------------------------------------------------------------------------------- | --------- | ---------- | --------- |
| **Windows Server 2016 with IIS 10.0 version 2.0.1**               | 2019.02.13  | 3.15.666         | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.3.444.0 | 3.6        | 3.0.0     |
| **Windows Server Core 2016 with IIS 10.0 version 2.0.1**          | 2019.02.13  | 3.15.666         | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.3.444.0 | 3.6        | 3.0.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 2.0.1**             | 2019.02.13  | 3.15.666         | 4.9.3289                                                                                                  | 2.3.444.0 | 3.6        | 3.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.0.1** | 2019.02.13  | 3.15.666         | 4.9.3289                                                                                                  | 2.3.444.0 | 3.6        | 3.0.0     |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | 2019.02.13  | 3.15.666         | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.3.444.0 | 3.6        | 1.0.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | 2019.02.13  | 3.15.666         | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.3.444.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | 2019.02.13  | 3.15.666         | 4.9.3289                                                                                                  | 2.3.444.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | 2019.02.13  | 3.15.666         | 4.9.3289                                                                                                  | 2.3.444.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | 2019.02.13  | 3.15.666         | 4.9.3289                                                                                                  | 2.3.444.0 | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | 2019.02.13  | 3.15.666         | 4.9.3289                                                                                                  | 2.3.444.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5**                           | 2019.02.13  | 3.15.666         | 4.9.3289                                                                                                  | 2.3.444.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | 2019.02.13  | 3.15.666         | 4.9.3289                                                                                                  | 2.3.444.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8**                                | 2019.02.13  | 3.15.666         | 4.9.3289                                                                                                  | 2.3.444.0 | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5**                           | 2019.02.13  | 3.15.666         | 4.9.3289                                                                                                  | 2.3.444.0 | 3.6        | 1.0.0     |

## January 24, 2019 – February 20, 2019

The following Elastic Beanstalk platform versions for .NET were current during this date range:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                                     | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | _64bit Windows Server 2016 v1.2.0 running IIS 10.0_        | .NET Core 2.2.1, supports 2.2.1, 2.1.7, 2.0.9, 1.1.10, 1.0.13<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | _64bit Windows Server Core 2016 v1.2.0 running IIS 10.0_   | .NET Core 2.2.1, supports 2.2.1, 2.1.7, 2.0.9, 1.1.10, 1.0.13<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | _64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5_      | .NET Core 2.2.1, supports 2.2.1, 2.1.7, 2.0.9, 1.1.10, 1.0.13<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | _64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5_ | .NET Core 2.2.1, supports 2.2.1, 2.1.7, 2.0.9, 1.1.10, 1.0.13<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | _64bit Windows Server 2012 v1.2.0 running IIS 8_           | .NET Core 2.2.1, supports 2.2.1, 2.1.7, 2.0.9, 1.1.10, 1.0.13<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | _64bit Windows Server 2008 R2 v1.2.0 running IIS 7.5_      | .NET Core 2.1.7, supports 2.1.7, 2.0.9, 1.1.10, 1.0.13<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x        | IIS 7.5      |
| **Windows Server 2012 R2 with IIS 8.5**                           | _64bit Windows Server 2012 R2 running IIS 8.5_             | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                                  | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | _64bit Windows Server Core 2012 R2 running IIS 8.5_        | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                                  | IIS 8.5      |
| **Windows Server 2012 with IIS 8**                                | _64bit Windows Server 2012 running IIS 8_                  | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                                  | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5**                           | _64bit Windows Server 2008 R2 running IIS 7.5_             | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                                  | IIS 7.5      |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config                                                                                                 | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------------------------------------------------------------------------------------------------------- | --------- | ---------- | --------- |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | 2019.01.10  | 3.3.434.0        | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.3.344.0 | 3.6        | 1.0.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | 2019.01.10  | 3.3.434.0        | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.3.344.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | 2019.01.10  | 3.3.434.0        | 4.9.3160                                                                                                  | 2.3.344.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | 2019.01.10  | 3.3.434.0        | 4.9.3160                                                                                                  | 2.3.344.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | 2019.01.10  | 3.3.434.0        | 4.9.3160                                                                                                  | 2.3.344.0 | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | 2019.01.10  | 3.3.434.0        | 4.9.3160                                                                                                  | 2.3.344.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5**                           | 2019.01.10  | 3.3.434.0        | 4.9.3160                                                                                                  | 2.3.344.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | 2019.01.10  | 3.3.434.0        | 4.9.3160                                                                                                  | 2.3.344.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8**                                | 2019.01.10  | 3.3.434.0        | 4.9.3160                                                                                                  | 2.3.344.0 | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5**                           | 2019.01.10  | 3.3.434.0        | 4.9.3160                                                                                                  | 2.3.344.0 | 3.6        | 1.0.0     |

## December 21, 2018 – January 23, 2019

The following Elastic Beanstalk platform versions for .NET were current during this date range:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                              | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ------------ |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | _64bit Windows Server 2016 v1.2.0 running IIS 10.0_        | .NET Core 2.1.6, supports 2.1.6, 2.0.9, 1.1.10, 1.0.13<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | _64bit Windows Server Core 2016 v1.2.0 running IIS 10.0_   | .NET Core 2.1.6, supports 2.1.6, 2.0.9, 1.1.10, 1.0.13<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | _64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5_      | .NET Core 2.1.6, supports 2.1.6, 2.0.9, 1.1.10, 1.0.13<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | _64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5_ | .NET Core 2.1.6, supports 2.1.6, 2.0.9, 1.1.10, 1.0.13<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | _64bit Windows Server 2012 v1.2.0 running IIS 8_           | .NET Core 2.1.6, supports 2.1.6, 2.0.9, 1.1.10, 1.0.13<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | _64bit Windows Server 2008 R2 v1.2.0 running IIS 7.5_      | .NET Core 2.1.6, supports 2.1.6, 2.0.9, 1.1.10, 1.0.13<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 7.5      |
| **Windows Server 2012 R2 with IIS 8.5**                           | _64bit Windows Server 2012 R2 running IIS 8.5_             | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                           | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | _64bit Windows Server Core 2012 R2 running IIS 8.5_        | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                           | IIS 8.5      |
| **Windows Server 2012 with IIS 8**                                | _64bit Windows Server 2012 running IIS 8_                  | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                           | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5**                           | _64bit Windows Server 2008 R2 running IIS 7.5_             | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                           | IIS 7.5      |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config                                                                                                 | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------------------------------------------------------------------------------------------------------- | --------- | ---------- | --------- |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | 2018.12.12  | 3.3.420.0        | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.3.274.0 | 3.6        | 1.0.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | 2018.12.12  | 3.3.420.0        | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.3.274.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | 2018.12.12  | 3.3.420.0        | 4.9.3067                                                                                                  | 2.3.235.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | 2018.12.12  | 3.3.420.0        | 4.9.3067                                                                                                  | 2.3.235.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | 2018.12.12  | 3.3.420.0        | 4.9.3067                                                                                                  | 2.3.235.0 | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | 2018.12.12  | 3.3.420.0        | 4.9.3067                                                                                                  | 2.3.235.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5**                           | 2018.12.12  | 3.3.420.0        | 4.9.3067                                                                                                  | 2.3.235.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | 2018.12.12  | 3.3.420.0        | 4.9.3067                                                                                                  | 2.3.235.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8**                                | 2018.12.12  | 3.3.420.0        | 4.9.3067                                                                                                  | 2.3.235.0 | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5**                           | 2018.12.12  | 3.3.420.0        | 4.9.3067                                                                                                  | 2.3.235.0 | 3.6        | 1.0.0     |

## December 10, 2018 – December 20, 2018

The following Elastic Beanstalk platform versions for .NET were current during this date range:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                              | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ------------ |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | _64bit Windows Server 2016 v1.2.0 running IIS 10.0_        | .NET Core 2.1.6, supports 2.1.6, 2.0.9, 1.1.10, 1.0.13<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | _64bit Windows Server Core 2016 v1.2.0 running IIS 10.0_   | .NET Core 2.1.6, supports 2.1.6, 2.0.9, 1.1.10, 1.0.13<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | _64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5_      | .NET Core 2.1.6, supports 2.1.6, 2.0.9, 1.1.10, 1.0.13<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | _64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5_ | .NET Core 2.1.6, supports 2.1.6, 2.0.9, 1.1.10, 1.0.13<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | _64bit Windows Server 2012 v1.2.0 running IIS 8_           | .NET Core 2.1.6, supports 2.1.6, 2.0.9, 1.1.10, 1.0.13<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | _64bit Windows Server 2008 R2 v1.2.0 running IIS 7.5_      | .NET Core 2.1.6, supports 2.1.6, 2.0.9, 1.1.10, 1.0.13<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 7.5      |
| **Windows Server 2012 R2 with IIS 8.5**                           | _64bit Windows Server 2012 R2 running IIS 8.5_             | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                           | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | _64bit Windows Server Core 2012 R2 running IIS 8.5_        | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                           | IIS 8.5      |
| **Windows Server 2012 with IIS 8**                                | _64bit Windows Server 2012 running IIS 8_                  | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                           | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5**                           | _64bit Windows Server 2008 R2 running IIS 7.5_             | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                           | IIS 7.5      |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config                                                                                                 | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------------------------------------------------------------------------------------------------------- | --------- | ---------- | --------- |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | 2018.11.28  | 3.3.408.0        | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.3.235.0 | 3.6        | 1.0.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | 2018.11.28  | 3.3.408.0        | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.3.235.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | 2018.11.28  | 3.3.408.0        | 4.9.3067                                                                                                  | 2.3.235.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | 2018.11.28  | 3.3.408.0        | 4.9.3067                                                                                                  | 2.3.235.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | 2018.11.28  | 3.3.408.0        | 4.9.3067                                                                                                  | 2.3.235.0 | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | 2018.11.28  | 3.3.408.0        | 4.9.3067                                                                                                  | 2.3.235.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5**                           | 2018.11.28  | 3.3.408.0        | 4.9.3067                                                                                                  | 2.3.235.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | 2018.11.28  | 3.3.408.0        | 4.9.3067                                                                                                  | 2.3.235.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8**                                | 2018.11.28  | 3.3.408.0        | 4.9.3067                                                                                                  | 2.3.235.0 | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5**                           | 2018.11.28  | 3.3.408.0        | 4.9.3067                                                                                                  | 2.3.235.0 | 3.6        | 1.0.0     |

## October 23, 2018 – December 9, 2018

The following Elastic Beanstalk platform versions for .NET were current during this date range:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                              | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ------------ |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | _64bit Windows Server 2016 v1.2.0 running IIS 10.0_        | .NET Core 2.1.5, supports 2.1.5, 2.0.9, 1.1.10, 1.0.13<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | _64bit Windows Server Core 2016 v1.2.0 running IIS 10.0_   | .NET Core 2.1.5, supports 2.1.5, 2.0.9, 1.1.10, 1.0.13<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | _64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5_      | .NET Core 2.1.5, supports 2.1.5, 2.0.9, 1.1.10, 1.0.13<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | _64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5_ | .NET Core 2.1.5, supports 2.1.5, 2.0.9, 1.1.10, 1.0.13<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | _64bit Windows Server 2012 v1.2.0 running IIS 8_           | .NET Core 2.1.5, supports 2.1.5, 2.0.9, 1.1.10, 1.0.13<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | _64bit Windows Server 2008 R2 v1.2.0 running IIS 7.5_      | .NET Core 2.1.5, supports 2.1.5, 2.0.9, 1.1.10, 1.0.13<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 7.5      |
| **Windows Server 2012 R2 with IIS 8.5**                           | _64bit Windows Server 2012 R2 running IIS 8.5_             | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                           | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | _64bit Windows Server Core 2012 R2 running IIS 8.5_        | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                           | IIS 8.5      |
| **Windows Server 2012 with IIS 8**                                | _64bit Windows Server 2012 running IIS 8_                  | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                           | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5**                           | _64bit Windows Server 2008 R2 running IIS 7.5_             | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                           | IIS 7.5      |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config                                                                                                 | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------------------------------------------------------------------------------------------------------- | --------- | ---------- | --------- |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | 2018.10.14  | 3.3.376.0        | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.2.800.0 | 3.6        | 1.0.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | 2018.10.14  | 3.3.376.0        | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.2.800.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | 2018.10.14  | 3.3.376.0        | 4.9.2756                                                                                                  | 2.2.800.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | 2018.10.14  | 3.3.376.0        | 4.9.2756                                                                                                  | 2.2.800.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | 2018.10.14  | 3.3.376.0        | 4.9.2756                                                                                                  | 2.2.800.0 | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | 2018.10.14  | 3.3.376.0        | 4.9.2756                                                                                                  | 2.2.800.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5**                           | 2018.10.14  | 3.3.376.0        | 4.9.2756                                                                                                  | 2.2.800.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | 2018.10.14  | 3.3.376.0        | 4.9.2756                                                                                                  | 2.2.800.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8**                                | 2018.10.14  | 3.3.376.0        | 4.9.2756                                                                                                  | 2.2.800.0 | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5**                           | 2018.10.14  | 3.3.376.0        | 4.9.2756                                                                                                  | 2.2.800.0 | 3.6        | 1.0.0     |

## September 24, 2018 – October 22, 2018

The following Elastic Beanstalk platform versions for .NET were current during this date range:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                             | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | _64bit Windows Server 2016 v1.2.0 running IIS 10.0_        | .NET Core 2.1.4, supports 2.1.4, 2.0.9, 1.1.9, 1.0.12<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | _64bit Windows Server Core 2016 v1.2.0 running IIS 10.0_   | .NET Core 2.1.4, supports 2.1.4, 2.0.9, 1.1.9, 1.0.12<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | _64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5_      | .NET Core 2.1.4, supports 2.1.4, 2.0.9, 1.1.9, 1.0.12<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | _64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5_ | .NET Core 2.1.4, supports 2.1.4, 2.0.9, 1.1.9, 1.0.12<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | _64bit Windows Server 2012 v1.2.0 running IIS 8_           | .NET Core 2.1.4, supports 2.1.4, 2.0.9, 1.1.9, 1.0.12<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | _64bit Windows Server 2008 R2 v1.2.0 running IIS 7.5_      | .NET Core 2.1.4, supports 2.1.4, 2.0.9, 1.1.9, 1.0.12<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 7.5      |
| **Windows Server 2012 R2 with IIS 8.5**                           | _64bit Windows Server 2012 R2 running IIS 8.5_             | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                          | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | _64bit Windows Server Core 2012 R2 running IIS 8.5_        | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                          | IIS 8.5      |
| **Windows Server 2012 with IIS 8**                                | _64bit Windows Server 2012 running IIS 8_                  | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                          | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5**                           | _64bit Windows Server 2008 R2 running IIS 7.5_             | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                          | IIS 7.5      |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config                                                                                                 | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------------------------------------------------------------------------------------------------------- | --------- | ---------- | --------- |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | 2018.09.15  | 3.3.352.0        | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.2.800.0 | 3.6        | 1.0.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | 2018.09.15  | 3.3.352.0        | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.2.800.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | 2018.09.15  | 3.3.352.0        | 4.9.2756                                                                                                  | 2.2.800.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | 2018.09.15  | 3.3.352.0        | 4.9.2756                                                                                                  | 2.2.800.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | 2018.09.15  | 3.3.352.0        | 4.9.2756                                                                                                  | 2.2.800.0 | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | 2018.09.15  | 3.3.352.0        | 4.9.2756                                                                                                  | 2.2.800.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5**                           | 2018.09.15  | 3.3.352.0        | 4.9.2756                                                                                                  | 2.2.800.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | 2018.09.15  | 3.3.352.0        | 4.9.2756                                                                                                  | 2.2.800.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8**                                | 2018.09.15  | 3.3.352.0        | 4.9.2756                                                                                                  | 2.2.800.0 | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5**                           | 2018.09.15  | 3.3.352.0        | 4.9.2756                                                                                                  | 2.2.800.0 | 3.6        | 1.0.0     |

## August 27, 2018 – September 23, 2018

The following Elastic Beanstalk platform versions for .NET were current during this date range:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                          | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | _64bit Windows Server 2016 v1.2.0 running IIS 10.0_        | .NET Core 2.1, supports 2.1.x, 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | _64bit Windows Server Core 2016 v1.2.0 running IIS 10.0_   | .NET Core 2.1, supports 2.1.x, 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | _64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5_      | .NET Core 2.1, supports 2.1.x, 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | _64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5_ | .NET Core 2.1, supports 2.1.x, 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | _64bit Windows Server 2012 v1.2.0 running IIS 8_           | .NET Core 2.1, supports 2.1.x, 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | _64bit Windows Server 2008 R2 v1.2.0 running IIS 7.5_      | .NET Core 2.1, supports 2.1.x, 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 7.5      |
| **Windows Server 2012 R2 with IIS 8.5**                           | _64bit Windows Server 2012 R2 running IIS 8.5_             | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                       | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | _64bit Windows Server Core 2012 R2 running IIS 8.5_        | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                       | IIS 8.5      |
| **Windows Server 2012 with IIS 8**                                | _64bit Windows Server 2012 running IIS 8_                  | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                       | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5**                           | _64bit Windows Server 2008 R2 running IIS 7.5_             | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                       | IIS 7.5      |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config                                                                                                 | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------------------------------------------------------------------------------------------------------- | --------- | ---------- | --------- |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | 2018.08.15  | 3.3.336.0        | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.2.800.0 | 3.6        | 1.0.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | 2018.08.15  | 3.3.336.0        | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.2.800.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | 2018.08.15  | 3.3.336.0        | 4.9.2756                                                                                                  | 2.2.800.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | 2018.08.15  | 3.3.336.0        | 4.9.2756                                                                                                  | 2.2.800.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | 2018.08.15  | 3.3.336.0        | 4.9.2756                                                                                                  | 2.2.800.0 | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | 2018.08.15  | 3.3.336.0        | 4.9.2756                                                                                                  | 2.2.800.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5**                           | 2018.08.15  | 3.3.336.0        | 4.9.2756                                                                                                  | 2.2.800.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | 2018.08.15  | 3.3.336.0        | 4.9.2756                                                                                                  | 2.2.800.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8**                                | 2018.08.15  | 3.3.336.0        | 4.9.2756                                                                                                  | 2.2.800.0 | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5**                           | 2018.08.15  | 3.3.336.0        | 4.9.2756                                                                                                  | 2.2.800.0 | 3.6        | 1.0.0     |

## July 25, 2018 – August 26, 2018

The following Elastic Beanstalk platform versions for .NET were current during this date range:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                          | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | _64bit Windows Server 2016 v1.2.0 running IIS 10.0_        | .NET Core 2.1, supports 2.1.x, 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | _64bit Windows Server Core 2016 v1.2.0 running IIS 10.0_   | .NET Core 2.1, supports 2.1.x, 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | _64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5_      | .NET Core 2.1, supports 2.1.x, 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | _64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5_ | .NET Core 2.1, supports 2.1.x, 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | _64bit Windows Server 2012 v1.2.0 running IIS 8_           | .NET Core 2.1, supports 2.1.x, 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | _64bit Windows Server 2008 R2 v1.2.0 running IIS 7.5_      | .NET Core 2.1, supports 2.1.x, 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 7.5      |
| **Windows Server 2012 R2 with IIS 8.5**                           | _64bit Windows Server 2012 R2 running IIS 8.5_             | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                       | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | _64bit Windows Server Core 2012 R2 running IIS 8.5_        | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                       | IIS 8.5      |
| **Windows Server 2012 with IIS 8**                                | _64bit Windows Server 2012 running IIS 8_                  | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                       | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5**                           | _64bit Windows Server 2008 R2 running IIS 7.5_             | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                       | IIS 7.5      |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config                                                                                                 | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------------------------------------------------------------------------------------------------------- | --------- | ---------- | --------- |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | 2018.07.11  | 3.3.311.0        | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.2.800.0 | 3.6        | 1.0.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | 2018.07.11  | 3.3.311.0        | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.2.800.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | 2018.07.11  | 3.3.311.0        | 4.9.2756                                                                                                  | 2.2.800.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | 2018.07.11  | 3.3.311.0        | 4.9.2756                                                                                                  | 2.2.800.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | 2018.07.11  | 3.3.311.0        | 4.9.2756                                                                                                  | 2.2.800.0 | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | 2018.07.11  | 3.3.311.0        | 4.9.2756                                                                                                  | 2.2.800.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5**                           | 2018.07.11  | 3.3.311.0        | 4.9.2756                                                                                                  | 2.2.800.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | 2018.07.11  | 3.3.311.0        | 4.9.2756                                                                                                  | 2.2.800.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8**                                | 2018.07.11  | 3.3.311.0        | 4.9.2756                                                                                                  | 2.2.800.0 | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5**                           | 2018.07.11  | 3.3.311.0        | 4.9.2756                                                                                                  | 2.2.800.0 | 3.6        | 1.0.0     |

## June 25, 2018 – July 24, 2018

The following Elastic Beanstalk platform versions for .NET were current during this date range:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                          | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | _64bit Windows Server 2016 v1.2.0 running IIS 10.0_        | .NET Core 2.1, supports 2.1.x, 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | _64bit Windows Server Core 2016 v1.2.0 running IIS 10.0_   | .NET Core 2.1, supports 2.1.x, 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | _64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5_      | .NET Core 2.1, supports 2.1.x, 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | _64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5_ | .NET Core 2.1, supports 2.1.x, 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | _64bit Windows Server 2012 v1.2.0 running IIS 8_           | .NET Core 2.1, supports 2.1.x, 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | _64bit Windows Server 2008 R2 v1.2.0 running IIS 7.5_      | .NET Core 2.1, supports 2.1.x, 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 7.5      |
| **Windows Server 2012 R2 with IIS 8.5**                           | _64bit Windows Server 2012 R2 running IIS 8.5_             | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                       | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | _64bit Windows Server Core 2012 R2 running IIS 8.5_        | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                       | IIS 8.5      |
| **Windows Server 2012 with IIS 8**                                | _64bit Windows Server 2012 running IIS 8_                  | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                       | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5**                           | _64bit Windows Server 2008 R2 running IIS 7.5_             | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                       | IIS 7.5      |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config                                                                                                 | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------------------------------------------------------------------------------------------------------- | --------- | ---------- | --------- |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | 2018.06.13  | 3.3.283.0        | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.2.619.0 | 3.6        | 1.0.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | 2018.06.13  | 3.3.283.0        | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.2.619.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | 2018.06.13  | 3.3.283.0        | 4.9.2688                                                                                                  | 2.2.619.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | 2018.06.13  | 3.3.283.0        | 4.9.2688                                                                                                  | 2.2.619.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | 2018.06.13  | 3.3.283.0        | 4.9.2688                                                                                                  | 2.2.619.0 | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | 2018.06.13  | 3.3.283.0        | 4.9.2688                                                                                                  | 2.2.619.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5**                           | 2018.06.13  | 3.3.283.0        | 4.9.2688                                                                                                  | 2.2.619.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | 2018.06.13  | 3.3.283.0        | 4.9.2688                                                                                                  | 2.2.619.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8**                                | 2018.06.13  | 3.3.283.0        | 4.9.2688                                                                                                  | 2.2.619.0 | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5**                           | 2018.06.13  | 3.3.283.0        | 4.9.2688                                                                                                  | 2.2.619.0 | 3.6        | 1.0.0     |

## May 18, 2018 – June 24, 2018

The following Elastic Beanstalk platform versions for .NET were current during this date range:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                   | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | _64bit Windows Server 2016 v1.2.0 running IIS 10.0_        | .NET Core 2.0, supports 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | _64bit Windows Server Core 2016 v1.2.0 running IIS 10.0_   | .NET Core 2.0, supports 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | _64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5_      | .NET Core 2.0, supports 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | _64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5_ | .NET Core 2.0, supports 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | _64bit Windows Server 2012 v1.2.0 running IIS 8_           | .NET Core 2.0, supports 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | _64bit Windows Server 2008 R2 v1.2.0 running IIS 7.5_      | .NET Core 2.0, supports 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 7.5      |
| **Windows Server 2012 R2 with IIS 8.5**                           | _64bit Windows Server 2012 R2 running IIS 8.5_             | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | _64bit Windows Server Core 2012 R2 running IIS 8.5_        | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                | IIS 8.5      |
| **Windows Server 2012 with IIS 8**                                | _64bit Windows Server 2012 running IIS 8_                  | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5**                           | _64bit Windows Server 2008 R2 running IIS 7.5_             | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x                                                | IIS 7.5      |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config                                                                                                 | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------------------------------------------------------------------------------------------------------- | --------- | ---------- | --------- |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | 2018.04.11  | 3.3.260.0        | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.2.392.0 | 3.6        | 1.0.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | 2018.04.11  | 3.3.260.0        | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.2.392.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | 2018.04.11  | 3.3.260.0        | 4.9.2586                                                                                                  | 2.2.392.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | 2018.04.11  | 3.3.260.0        | 4.9.2586                                                                                                  | 2.2.392.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | 2018.04.11  | 3.3.260.0        | 4.9.2586                                                                                                  | 2.2.392.0 | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | 2018.04.11  | 3.3.260.0        | 4.9.2586                                                                                                  | 2.2.392.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5**                           | 2018.04.11  | 3.3.260.0        | 4.9.2586                                                                                                  | 2.2.392.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | 2018.04.11  | 3.3.260.0        | 4.9.2586                                                                                                  | 2.2.392.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8**                                | 2018.04.11  | 3.3.260.0        | 4.9.2586                                                                                                  | 2.2.392.0 | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5**                           | 2018.04.11  | 3.3.260.0        | 4.9.2586                                                                                                  | 2.2.392.0 | 3.6        | 1.0.0     |

## April 18, 2018 – May 17, 2018

The following Elastic Beanstalk platform versions for .NET were current during this date range:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                 | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | _64bit Windows Server 2016 v1.2.0 running IIS 10.0_        | .NET Core 2.0, supports 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | _64bit Windows Server Core 2016 v1.2.0 running IIS 10.0_   | .NET Core 2.0, supports 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | _64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5_      | .NET Core 2.0, supports 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | _64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5_ | .NET Core 2.0, supports 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | _64bit Windows Server 2012 v1.2.0 running IIS 8_           | .NET Core 2.0, supports 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7, supports 4.x, 2.0, 1.x | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | _64bit Windows Server 2008 R2 v1.2.0 running IIS 7.5_      | .NET Core 2.0, supports 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7, supports 4.x, 2.0, 1.x | IIS 7.5      |
| **Windows Server 2012 R2 with IIS 8.5**                           | _64bit Windows Server 2012 R2 running IIS 8.5_             | .NET Framework 4.7, supports 4.x, 2.0, 1.x                                                | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | _64bit Windows Server Core 2012 R2 running IIS 8.5_        | .NET Framework 4.7, supports 4.x, 2.0, 1.x                                                | IIS 8.5      |
| **Windows Server 2012 with IIS 8**                                | _64bit Windows Server 2012 running IIS 8_                  | .NET Framework 4.7, supports 4.x, 2.0, 1.x                                                | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5**                           | _64bit Windows Server 2008 R2 running IIS 7.5_             | .NET Framework 4.7, supports 4.x, 2.0, 1.x                                                | IIS 7.5      |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config                                                                                                 | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------------------------------------------------------------------------------------------------------- | --------- | ---------- | --------- |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | 2018.03.24  | 3.3.245.0        | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.2.355.0 | 3.6        | 1.0.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | 2018.03.24  | 3.3.245.0        | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.2.355.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | 2018.03.24  | 3.3.245.0        | 4.9.2565                                                                                                  | 2.2.355.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | 2018.03.24  | 3.3.245.0        | 4.9.2565                                                                                                  | 2.2.355.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | 2018.03.24  | 3.3.245.0        | 4.9.2565                                                                                                  | 2.2.355.0 | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | 2018.03.24  | 3.3.245.0        | 4.9.2565                                                                                                  | 2.2.355.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5**                           | 2018.03.24  | 3.3.245.0        | 4.9.2565                                                                                                  | 2.2.355.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | 2018.03.24  | 3.3.245.0        | 4.9.2565                                                                                                  | 2.2.355.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8**                                | 2018.03.24  | 3.3.245.0        | 4.9.2565                                                                                                  | 2.2.355.0 | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5**                           | 2018.03.24  | 3.3.245.0        | 4.9.2565                                                                                                  | 2.2.355.0 | 3.6        | 1.0.0     |

## March 16, 2018 – April 17, 2018

The following Elastic Beanstalk platform versions for .NET were current during this date range:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                 | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | _64bit Windows Server 2016 v1.2.0 running IIS 10.0_        | .NET Core 2.0, supports 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | _64bit Windows Server Core 2016 v1.2.0 running IIS 10.0_   | .NET Core 2.0, supports 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | _64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5_      | .NET Core 2.0, supports 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | _64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5_ | .NET Core 2.0, supports 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | _64bit Windows Server 2012 v1.2.0 running IIS 8_           | .NET Core 2.0, supports 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7, supports 4.x, 2.0, 1.x | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | _64bit Windows Server 2008 R2 v1.2.0 running IIS 7.5_      | .NET Core 2.0, supports 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7, supports 4.x, 2.0, 1.x | IIS 7.5      |
| **Windows Server 2012 R2 with IIS 8.5**                           | _64bit Windows Server 2012 R2 running IIS 8.5_             | .NET Framework 4.7, supports 4.x, 2.0, 1.x                                                | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | _64bit Windows Server Core 2012 R2 running IIS 8.5_        | .NET Framework 4.7, supports 4.x, 2.0, 1.x                                                | IIS 8.5      |
| **Windows Server 2012 with IIS 8**                                | _64bit Windows Server 2012 running IIS 8_                  | .NET Framework 4.7, supports 4.x, 2.0, 1.x                                                | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5**                           | _64bit Windows Server 2008 R2 running IIS 7.5_             | .NET Framework 4.7, supports 4.x, 2.0, 1.x                                                | IIS 7.5      |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config                                                                                                 | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------------------------------------------------------------------------------------------------------- | --------- | ---------- | --------- |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | 2018.03.06  | 3.15.345         | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.2.160.0 | 3.6        | 1.0.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | 2018.03.06  | 3.15.345         | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.2.160.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | 2018.03.06  | 3.15.345         | 4.9.2400.0                                                                                                | 2.2.160.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | 2018.03.06  | 3.15.345         | 4.9.2400.0                                                                                                | 2.2.160.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | 2018.03.06  | 3.15.345         | 4.9.2400.0                                                                                                | 2.2.160.0 | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | 2018.03.06  | 3.15.345         | 4.9.2400.0                                                                                                | 2.2.160.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5**                           | 2018.03.06  | 3.15.345         | 4.9.2400.0                                                                                                | 2.2.160.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | 2018.03.06  | 3.15.345         | 4.9.2400.0                                                                                                | 2.2.160.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8**                                | 2018.03.06  | 3.15.345         | 4.9.2400.0                                                                                                | 2.2.160.0 | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5**                           | 2018.03.06  | 3.15.345         | 4.9.2400.0                                                                                                | 2.2.160.0 | 3.6        | 1.0.0     |

## February 15, 2018 – March 15, 2018

The following Elastic Beanstalk platform versions for .NET were current during this date range:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                 | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | _64bit Windows Server 2016 v1.2.0 running IIS 10.0_        | .NET Core 2.0, supports 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | _64bit Windows Server Core 2016 v1.2.0 running IIS 10.0_   | .NET Core 2.0, supports 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | _64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5_      | .NET Core 2.0, supports 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | _64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5_ | .NET Core 2.0, supports 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | _64bit Windows Server 2012 v1.2.0 running IIS 8_           | .NET Core 2.0, supports 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7, supports 4.x, 2.0, 1.x | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | _64bit Windows Server 2008 R2 v1.2.0 running IIS 7.5_      | .NET Core 2.0, supports 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7, supports 4.x, 2.0, 1.x | IIS 7.5      |
| **Windows Server 2012 R2 with IIS 8.5**                           | _64bit Windows Server 2012 R2 running IIS 8.5_             | .NET Framework 4.7, supports 4.x, 2.0, 1.x                                                | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | _64bit Windows Server Core 2012 R2 running IIS 8.5_        | .NET Framework 4.7, supports 4.x, 2.0, 1.x                                                | IIS 8.5      |
| **Windows Server 2012 with IIS 8**                                | _64bit Windows Server 2012 running IIS 8_                  | .NET Framework 4.7, supports 4.x, 2.0, 1.x                                                | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5**                           | _64bit Windows Server 2008 R2 running IIS 7.5_             | .NET Framework 4.7, supports 4.x, 2.0, 1.x                                                | IIS 7.5      |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config                                                                                                 | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------------------------------------------------------------------------------------------------------- | --------- | ---------- | --------- |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | 2018.01.12  | 3.15.304         | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.2.93.0  | 3.6        | 1.0.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | 2018.01.12  | 3.15.304         | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.2.93.0  | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | 2018.01.12  | 3.15.304         | 4.9.2262.0                                                                                                | 2.2.93.0  | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | 2018.01.12  | 3.15.304         | 4.9.2262.0                                                                                                | 2.2.93.0  | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | 2018.01.12  | 3.15.304         | 4.9.2262.0                                                                                                | 2.2.93.0  | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | 2018.01.12  | 3.15.304         | 4.9.2262.0                                                                                                | 2.2.93.0  | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5**                           | 2018.01.12  | 3.15.304         | 4.9.2262.0                                                                                                | 2.2.93.0  | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | 2018.01.12  | 3.15.304         | 4.9.2262.0                                                                                                | 2.2.93.0  | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8**                                | 2018.01.12  | 3.15.304         | 4.9.2262.0                                                                                                | 2.2.93.0  | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5**                           | 2018.01.12  | 3.15.304         | 4.9.2262.0                                                                                                | 2.2.93.0  | 3.6        | 1.0.0     |

## January 11, 2018 – February 14, 2018

The following Elastic Beanstalk platform versions for .NET were current during this date range:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                 | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | _64bit Windows Server 2016 v1.2.0 running IIS 10.0_        | .NET Core 2.0, supports 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | _64bit Windows Server Core 2016 v1.2.0 running IIS 10.0_   | .NET Core 2.0, supports 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | _64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5_      | .NET Core 2.0, supports 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | _64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5_ | .NET Core 2.0, supports 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | _64bit Windows Server 2012 v1.2.0 running IIS 8_           | .NET Core 2.0, supports 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7, supports 4.x, 2.0, 1.x | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | _64bit Windows Server 2008 R2 v1.2.0 running IIS 7.5_      | .NET Core 2.0, supports 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7, supports 4.x, 2.0, 1.x | IIS 7.5      |
| **Windows Server 2012 R2 with IIS 8.5**                           | _64bit Windows Server 2012 R2 running IIS 8.5_             | .NET Framework 4.7, supports 4.x, 2.0, 1.x                                                | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | _64bit Windows Server Core 2012 R2 running IIS 8.5_        | .NET Framework 4.7, supports 4.x, 2.0, 1.x                                                | IIS 8.5      |
| **Windows Server 2012 with IIS 8**                                | _64bit Windows Server 2012 running IIS 8_                  | .NET Framework 4.7, supports 4.x, 2.0, 1.x                                                | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5**                           | _64bit Windows Server 2008 R2 running IIS 7.5_             | .NET Framework 4.7, supports 4.x, 2.0, 1.x                                                | IIS 7.5      |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config                                                                                                 | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------------------------------------------------------------------------------------------------------- | --------- | ---------- | --------- |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | 2018.01.05  | 3.15.304.0       | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.2.93.0  | 3.6        | 1.0.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | 2018.01.05  | 3.15.304.0       | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.2.93.0  | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | 2018.01.05  | 3.15.304.0       | 4.9.2262.0                                                                                                | 2.2.93.0  | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | 2018.01.05  | 3.15.304.0       | 4.9.2262.0                                                                                                | 2.2.93.0  | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | 2017.12.13  | 3.15.277.0       | 4.9.2262.0                                                                                                | 2.2.93.0  | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | 2018.01.05  | 3.15.304.0       | 4.9.2262.0                                                                                                | 2.2.93.0  | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5**                           | 2018.01.05  | 3.15.304.0       | 4.9.2262.0                                                                                                | 2.2.93.0  | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | 2018.01.05  | 3.15.304.0       | 4.9.2262.0                                                                                                | 2.2.93.0  | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8**                                | 2017.12.13  | 3.15.277.0       | 4.9.2262.0                                                                                                | 2.2.93.0  | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5**                           | 2018.01.05  | 3.15.304.0       | 4.9.2262.0                                                                                                | 2.2.93.0  | 3.6        | 1.0.0     |

## December 19, 2017 – January 10, 2018

The following Elastic Beanstalk platform versions for .NET were current during this date range:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                                 | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | _64bit Windows Server 2016 v1.2.0 running IIS 10.0_        | .NET Core 2.0, supports 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | _64bit Windows Server Core 2016 v1.2.0 running IIS 10.0_   | .NET Core 2.0, supports 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | _64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5_      | .NET Core 2.0, supports 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | _64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5_ | .NET Core 2.0, supports 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | _64bit Windows Server 2012 v1.2.0 running IIS 8_           | .NET Core 2.0, supports 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7, supports 4.x, 2.0, 1.x | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | _64bit Windows Server 2008 R2 v1.2.0 running IIS 7.5_      | .NET Core 2.0, supports 2.0.x, 1.1.x, 1.0.x<br>.NET Framework 4.7, supports 4.x, 2.0, 1.x | IIS 7.5      |
| **Windows Server 2012 R2 with IIS 8.5**                           | _64bit Windows Server 2012 R2 running IIS 8.5_             | .NET Framework 4.7, supports 4.x, 2.0, 1.x                                                | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | _64bit Windows Server Core 2012 R2 running IIS 8.5_        | .NET Framework 4.7, supports 4.x, 2.0, 1.x                                                | IIS 8.5      |
| **Windows Server 2012 with IIS 8**                                | _64bit Windows Server 2012 running IIS 8_                  | .NET Framework 4.7, supports 4.x, 2.0, 1.x                                                | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5**                           | _64bit Windows Server 2008 R2 running IIS 7.5_             | .NET Framework 4.7, supports 4.x, 2.0, 1.x                                                | IIS 7.5      |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config                                                                                                 | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------------------------------------------------------------------------------------------------------- | --------- | ---------- | --------- |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | 2017.11.29  | 3.15.244.0       | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.2.64.0  | 3.6        | 1.0.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | 2017.11.29  | 3.15.244.0       | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.2.64.0  | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | 2017.11.29  | 3.15.244.0       | 4.9.2188.0                                                                                                | 2.2.64.0  | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | 2017.11.29  | 3.15.244.0       | 4.9.2188.0                                                                                                | 2.2.64.0  | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | 2017.11.29  | 3.15.244.0       | 4.9.2188.0                                                                                                | 2.2.64.0  | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | 2017.11.29  | 3.15.244.0       | 4.9.2188.0                                                                                                | 2.2.64.0  | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5**                           | 2017.11.29  | 3.15.244.0       | 4.9.2188.0                                                                                                | 2.2.64.0  | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | 2017.11.29  | 3.15.244.0       | 4.9.2188.0                                                                                                | 2.2.64.0  | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8**                                | 2017.11.29  | 3.15.244.0       | 4.9.2188.0                                                                                                | 2.2.64.0  | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5**                           | 2017.11.29  | 3.15.244.0       | 4.9.2188.0                                                                                                | 2.2.64.0  | 3.6        | 1.0.0     |

## November 20, 2017 – December 18, 2017

The following Elastic Beanstalk platform versions for .NET were current during this date range:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                          | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | _64bit Windows Server 2016 v1.2.0 running IIS 10.0_        | .NET Core 2.0, supports 1.1.x, 1.0.x<br>.NET Framework 4.7, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | _64bit Windows Server Core 2016 v1.2.0 running IIS 10.0_   | .NET Core 2.0, supports 1.1.x, 1.0.x<br>.NET Framework 4.7, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | _64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5_      | .NET Core 2.0, supports 1.1.x, 1.0.x<br>.NET Framework 4.7, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | _64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5_ | .NET Core 2.0, supports 1.1.x, 1.0.x<br>.NET Framework 4.7, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | _64bit Windows Server 2012 v1.2.0 running IIS 8_           | .NET Core 2.0, supports 1.1.x, 1.0.x<br>.NET Framework 4.7, supports 4.x, 2.0, 1.x | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | _64bit Windows Server 2008 R2 v1.2.0 running IIS 7.5_      | .NET Core 2.0, supports 1.1.x, 1.0.x<br>.NET Framework 4.7, supports 4.x, 2.0, 1.x | IIS 7.5      |
| **Windows Server 2012 R2 with IIS 8.5**                           | _64bit Windows Server 2012 R2 running IIS 8.5_             | .NET Framework 4.7, supports 4.x, 2.0, 1.x                                         | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | _64bit Windows Server Core 2012 R2 running IIS 8.5_        | .NET Framework 4.7, supports 4.x, 2.0, 1.x                                         | IIS 8.5      |
| **Windows Server 2012 with IIS 8**                                | _64bit Windows Server 2012 running IIS 8_                  | .NET Framework 4.7, supports 4.x, 2.0, 1.x                                         | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5**                           | _64bit Windows Server 2008 R2 running IIS 7.5_             | .NET Framework 4.7, supports 4.x, 2.0, 1.x                                         | IIS 7.5      |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config                                                                                                 | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------------------------------------------------------------------------------------------------------- | --------- | ---------- | --------- |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | 2017.10.13  | 3.15.172.0       | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.2.30.0  | 3.6        | 1.0.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | 2017.10.13  | 3.15.172.0       | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.2.30.0  | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | 2017.10.13  | 3.15.172.0       | 4.9.2188.0                                                                                                | 2.2.30.0  | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | 2017.10.13  | 3.15.172.0       | 4.9.2188.0                                                                                                | 2.2.30.0  | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | 2017.10.13  | 3.15.172.0       | 4.9.2188.0                                                                                                | 2.2.30.0  | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | 2017.10.13  | 3.15.172.0       | 4.9.2188.0                                                                                                | 2.2.30.0  | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5**                           | 2017.10.13  | 3.15.172.0       | 4.9.2188.0                                                                                                | 2.2.30.0  | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | 2017.10.13  | 3.15.172.0       | 4.9.2188.0                                                                                                | 2.2.30.0  | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8**                                | 2017.10.13  | 3.15.172.0       | 4.9.2188.0                                                                                                | 2.2.30.0  | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5**                           | 2017.10.13  | 3.15.172.0       | 4.9.2188.0                                                                                                | 2.2.30.0  | 3.6        | 1.0.0     |

## August 28, 2017 – November 19, 2017

The following Elastic Beanstalk platform versions for .NET were current during this date range:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                          | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------------ |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | _64bit Windows Server 2016 v1.2.0 running IIS 10.0_        | .NET Core 2.0, supports 1.1.x, 1.0.x<br>.NET Framework 4.7, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | _64bit Windows Server Core 2016 v1.2.0 running IIS 10.0_   | .NET Core 2.0, supports 1.1.x, 1.0.x<br>.NET Framework 4.7, supports 4.x, 2.0, 1.x | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | _64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5_      | .NET Core 2.0, supports 1.1.x, 1.0.x<br>.NET Framework 4.7, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | _64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5_ | .NET Core 2.0, supports 1.1.x, 1.0.x<br>.NET Framework 4.7, supports 4.x, 2.0, 1.x | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | _64bit Windows Server 2012 v1.2.0 running IIS 8_           | .NET Core 2.0, supports 1.1.x, 1.0.x<br>.NET Framework 4.7, supports 4.x, 2.0, 1.x | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | _64bit Windows Server 2008 R2 v1.2.0 running IIS 7.5_      | .NET Core 2.0, supports 1.1.x, 1.0.x<br>.NET Framework 4.7, supports 4.x, 2.0, 1.x | IIS 7.5      |
| **Windows Server 2012 R2 with IIS 8.5**                           | _64bit Windows Server 2012 R2 running IIS 8.5_             | .NET Framework 4.7, supports 4.x, 2.0, 1.x                                         | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | _64bit Windows Server Core 2012 R2 running IIS 8.5_        | .NET Framework 4.7, supports 4.x, 2.0, 1.x                                         | IIS 8.5      |
| **Windows Server 2012 with IIS 8**                                | _64bit Windows Server 2012 running IIS 8_                  | .NET Framework 4.7, supports 4.x, 2.0, 1.x                                         | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5**                           | _64bit Windows Server 2008 R2 running IIS 7.5_             | .NET Framework 4.7, supports 4.x, 2.0, 1.x                                         | IIS 7.5      |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config                                                                                                 | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------------------------------------------------------------------------------------------------------- | --------- | ---------- | --------- |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | 2017.08.09  | 3.3.103.0        | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.0.879.0 | 3.6        | 1.0.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | 2017.08.09  | 3.3.103.0        | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.0.879.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | 2017.08.09  | 3.3.58.0         | 4.9.2016                                                                                                  | 2.0.879.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | 2017.08.09  | 3.3.58.0         | 4.9.2016                                                                                                  | 2.0.879.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | 2017.08.09  | 3.3.102.0        | 4.9.2016                                                                                                  | 2.0.879.0 | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | 2017.08.09  | 3.3.102.0        | 4.9.1981                                                                                                  | 2.0.847.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5**                           | 2017.08.09  | 3.3.58.0         | 4.9.2016                                                                                                  | 2.0.879.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | 2017.08.09  | 3.3.58.0         | 4.9.2016                                                                                                  | 2.0.879.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8**                                | 2017.08.09  | 3.3.102.0        | 4.9.2016                                                                                                  | 2.0.879.0 | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5**                           | 2017.08.09  | 3.3.102.0        | 4.9.1981                                                                                                  | 2.0.847.0 | 3.6        | 1.0.0     |

## July 24, 2017 – Aug 27, 2017

The following Elastic Beanstalk platform versions for .NET were current during this date range:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                      | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------ | ------------ |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | _64bit Windows Server 2016 v1.2.0 running IIS 10.0_        | .NET v4.7, supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.1.2, 1.0.5 | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | _64bit Windows Server Core 2016 v1.2.0 running IIS 10.0_   | .NET v4.7, supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.1.2, 1.0.5 | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | _64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5_      | .NET v4.7, supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.1.2, 1.0.5 | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | _64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5_ | .NET v4.7, supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.1.2, 1.0.5 | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | _64bit Windows Server 2012 v1.2.0 running IIS 8_           | .NET v4.7, supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.1.2, 1.0.5 | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | _64bit Windows Server 2008 R2 v1.2.0 running IIS 7.5_      | .NET v4.7, supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.1.2, 1.0.5 | IIS 7.5      |
| **Windows Server 2012 R2 with IIS 8.5**                           | _64bit Windows Server 2012 R2 running IIS 8.5_             | .NET v4.7, supports runtimes 4, 2.0, 1.1 and 1.0                               | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | _64bit Windows Server Core 2012 R2 running IIS 8.5_        | .NET v4.7, supports runtimes 4, 2.0, 1.1 and 1.0                               | IIS 8.5      |
| **Windows Server 2012 with IIS 8**                                | _64bit Windows Server 2012 running IIS 8_                  | .NET v4.7, supports runtimes 4, 2.0, 1.1 and 1.0                               | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5**                           | _64bit Windows Server 2008 R2 running IIS 7.5_             | .NET v4.7, supports runtimes 4, 2.0, 1.1 and 1.0                               | IIS 7.5      |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config                                                                                                 | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------------------------------------------------------------------------------------------------------- | --------- | ---------- | --------- |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | 2017.07.13  | 3.3.103.0        | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.0.847.0 | 3.6        | 1.0.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | 2017.07.13  | 3.3.103.0        | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.0.847.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | 2017.07.13  | 3.3.102.0        | 4.9.1981                                                                                                  | 2.0.847.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | 2017.07.13  | 3.3.102.0        | 4.9.1981                                                                                                  | 2.0.847.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | 2017.07.13  | 3.3.102.0        | 4.9.1981                                                                                                  | 2.0.847.0 | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | 2017.07.13  | 3.3.102.0        | 4.9.1981                                                                                                  | 2.0.847.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5**                           | 2017.07.13  | 3.3.102.0        | 4.9.1981                                                                                                  | 2.0.847.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | 2017.07.13  | 3.3.102.0        | 4.9.1981                                                                                                  | 2.0.847.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8**                                | 2017.07.13  | 3.3.102.0        | 4.9.1981                                                                                                  | 2.0.847.0 | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5**                           | 2017.07.13  | 3.3.102.0        | 4.9.1981                                                                                                  | 2.0.847.0 | 3.6        | 1.0.0     |

## July 17, 2017 – July 23, 2017

The following Elastic Beanstalk platform versions for .NET were current during this date range:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                      | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------ | ------------ |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | _64bit Windows Server 2016 v1.2.0 running IIS 10.0_        | .NET v4.7, supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.1.2, 1.0.5 | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | _64bit Windows Server Core 2016 v1.2.0 running IIS 10.0_   | .NET v4.7, supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.1.2, 1.0.5 | IIS 10.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | _64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5_      | .NET v4.7, supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.1.2, 1.0.5 | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | _64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5_ | .NET v4.7, supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.1.2, 1.0.5 | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | _64bit Windows Server 2012 v1.2.0 running IIS 8_           | .NET v4.7, supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.1.2, 1.0.5 | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | _64bit Windows Server 2008 R2 v1.2.0 running IIS 7.5_      | .NET v4.7, supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.1.2, 1.0.5 | IIS 7.5      |
| **Windows Server 2012 R2 with IIS 8.5**                           | _64bit Windows Server 2012 R2 running IIS 8.5_             | .NET v4.7, supports runtimes 4, 2.0, 1.1 and 1.0                               | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | _64bit Windows Server Core 2012 R2 running IIS 8.5_        | .NET v4.7, supports runtimes 4, 2.0, 1.1 and 1.0                               | IIS 8.5      |
| **Windows Server 2012 with IIS 8**                                | _64bit Windows Server 2012 running IIS 8_                  | .NET v4.7, supports runtimes 4, 2.0, 1.1 and 1.0                               | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5**                           | _64bit Windows Server 2008 R2 running IIS 7.5_             | .NET v4.7, supports runtimes 4, 2.0, 1.1 and 1.0                               | IIS 7.5      |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config                                                                                                 | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | --------------------------------------------------------------------------------------------------------- | --------- | ---------- | --------- |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**               | 2017.06.14  | 3.3.103.0        | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.0.805.0 | 3.6        | 1.0.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0**          | 2017.06.14  | 3.3.103.0        | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.0.805.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | 2017.06.14  | 3.3.102.0        | 4.9.1900.0                                                                                                | 2.0.805.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | 2017.06.14  | 3.3.102.0        | 4.9.1900.0                                                                                                | 2.0.805.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | 2017.06.14  | 3.3.102.0        | 4.9.1900.0                                                                                                | 2.0.682.0 | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | 2017.06.14  | 3.3.102.0        | 4.9.1900.0                                                                                                | 2.0.805.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5**                           | 2017.06.14  | 3.3.102.0        | 4.9.1900.0                                                                                                | 2.0.805.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | 2017.06.14  | 3.3.102.0        | 4.9.1900.0                                                                                                | 2.0.805.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8**                                | 2017.06.14  | 3.3.102.0        | 4.9.1900.0                                                                                                | 2.0.805.0 | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5**                           | 2017.06.14  | 3.3.102.0        | 4.9.1900.0                                                                                                | 2.0.805.0 | 3.6        | 1.0.0     |

## June 26, 2017 – July 16, 2017

The following Elastic Beanstalk platform versions for .NET were current during this date range:

### Configuration basics

| Platform Version                                         | Solution Stack Name                                      | Framework                                                                      | Proxy Server |
| -------------------------------------------------------- | -------------------------------------------------------- | ------------------------------------------------------------------------------ | ------------ |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**      | _64bit Windows Server 2016 v1.2.0 running IIS 10.0_      | .NET v4.7, supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.1.2, 1.0.5 | IIS 10.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0** | _64bit Windows Server Core 2016 v1.2.0 running IIS 10.0_ | .NET v4.7, supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.1.2, 1.0.5 | IIS 10.0     |

### More details

| Platform Version                                         | AMI version | AWS SDK for .NET | EC2Config                                                                                                 | SSM Agent | Web Deploy | AWS X-Ray |
| -------------------------------------------------------- | ----------- | ---------------- | --------------------------------------------------------------------------------------------------------- | --------- | ---------- | --------- |
| **Windows Server 2016 with IIS 10.0 version 1.2.0**      | 2017.05.10  | 3.14.61.0        | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.0.767.0 | 3.6        | 1.0.0     |
| **Windows Server Core 2016 with IIS 10.0 version 1.2.0** | 2017.05.10  | 3.14.61.0        | _[SSM only](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")_ | 2.0.767.0 | 3.6        | 1.0.0     |

## May 16, 2017 – July 16, 2017

The following Elastic Beanstalk platform versions for .NET were current during this date range:

### Configuration basics

| Platform Version                                                  | Solution Stack Name                                        | Framework                                                                      | Proxy Server |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------ | ------------ |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | _64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5_      | .NET v4.7, supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.1.2, 1.0.5 | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | _64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5_ | .NET v4.7, supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.1.2, 1.0.5 | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | _64bit Windows Server 2012 v1.2.0 running IIS 8_           | .NET v4.7, supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.1.2, 1.0.5 | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | _64bit Windows Server 2008 R2 v1.2.0 running IIS 7.5_      | .NET v4.7, supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.1.2, 1.0.5 | IIS 7.5      |
| **Windows Server 2012 R2 with IIS 8.5**                           | _64bit Windows Server 2012 R2 running IIS 8.5_             | .NET v4.7, supports runtimes 4, 2.0, 1.1 and 1.0                               | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | _64bit Windows Server Core 2012 R2 running IIS 8.5_        | .NET v4.7, supports runtimes 4, 2.0, 1.1 and 1.0                               | IIS 8.5      |
| **Windows Server 2012 with IIS 8**                                | _64bit Windows Server 2012 running IIS 8_                  | .NET v4.7, supports runtimes 4, 2.0, 1.1 and 1.0                               | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5**                           | _64bit Windows Server 2008 R2 running IIS 7.5_             | .NET v4.7, supports runtimes 4, 2.0, 1.1 and 1.0                               | IIS 7.5      |

### More details

| Platform Version                                                  | AMI version | AWS SDK for .NET | EC2Config  | SSM Agent | Web Deploy | AWS X-Ray |
| ----------------------------------------------------------------- | ----------- | ---------------- | ---------- | --------- | ---------- | --------- |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**             | 2017.04.12  | 3.14.61.0        | 4.9.1775.0 | 2.0.761.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0** | 2017.04.12  | 3.14.61.0        | 4.9.1775.0 | 2.0.761.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8 version 1.2.0**                  | 2017.04.12  | 3.14.61.0        | 4.9.1775.0 | 2.0.682.0 | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**             | 2017.04.12  | 3.14.61.0        | 4.9.1775.0 | 2.0.761.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 with IIS 8.5**                           | 2017.04.12  | 3.14.61.0        | 4.9.1775.0 | 2.0.761.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 R2 Server Core with IIS 8.5**               | 2017.04.12  | 3.14.61.0        | 4.9.1775.0 | 2.0.761.0 | 3.6        | 1.0.0     |
| **Windows Server 2012 with IIS 8**                                | 2017.04.12  | 3.14.61.0        | 4.9.1775.0 | 2.0.682.0 | 3.6        | 1.0.0     |
| **Windows Server 2008 R2 with IIS 7.5**                           | 2017.04.12  | 3.14.61.0        | 4.9.1775.0 | 2.0.761.0 | 3.6        | 1.0.0     |

## May 4, 2017 – May 15, 2017

The following Elastic Beanstalk platform versions for .NET were current during this date range:

| Platform Version and _Solution Stack Name_                                                                                      | AMI version | Framework                                                                        | AWS SDK for .NET | EC2Config  | WebDeploy | AWS X-Ray | Proxy Server |
| ------------------------------------------------------------------------------------------------------------------------------- | ----------- | -------------------------------------------------------------------------------- | ---------------- | ---------- | --------- | --------- | ------------ |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**<br>_64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5_                  | 2017.04.12  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.1.1, 1.0.4 | 3.14.61.0        | 4.9.1775.0 | 3.6       | 1.0.0     | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0**<br>_64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5_ | 2017.04.12  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.1.1, 1.0.4 | 3.14.61.0        | 4.9.1775.0 | 3.6       | 1.0.0     | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**<br>_64bit Windows Server 2012 v1.2.0 running IIS 8_                            | 2017.04.12  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.1.1, 1.0.4 | 3.14.61.0        | 4.9.1775.0 | 3.6       | 1.0.0     | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**<br>_64bit Windows Server 2008 R2 v1.2.0 running IIS 7.5_                  | 2017.04.12  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.1.1, 1.0.4 | 3.14.61.0        | 4.9.1775.0 | 3.6       | 1.0.0     | IIS 7.5      |
| **Windows Server 2012 R2 with IIS 8.5**<br>_64bit Windows Server 2012 R2 running IIS 8.5_                                       | 2017.04.12  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0                               | 3.14.61.0        | 4.9.1775.0 | 3.6       | 1.0.0     | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5**<br>_64bit Windows Server Core 2012 R2 running IIS 8.5_                      | 2017.04.12  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0                               | 3.14.61.0        | 4.9.1775.0 | 3.6       | 1.0.0     | IIS 8.5      |
| **Windows Server 2012 with IIS 8**<br>_64bit Windows Server 2012 running IIS 8_                                                 | 2017.04.12  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0                               | 3.14.61.0        | 4.9.1775.0 | 3.6       | 1.0.0     | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5**<br>_64bit Windows Server 2008 R2 running IIS 7.5_                                       | 2017.04.12  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0                               | 3.14.61.0        | 4.9.1775.0 | 3.6       | 1.0.0     | IIS 7.5      |

## April 4, 2017 – May 3, 2017

The following Elastic Beanstalk platform versions for .NET were current during this date range:

| Platform Version and _Solution Stack Name_                                                                                      | AMI version | Framework                                                                        | AWS SDK for .NET | EC2Config | WebDeploy | AWS X-Ray | Proxy Server |
| ------------------------------------------------------------------------------------------------------------------------------- | ----------- | -------------------------------------------------------------------------------- | ---------------- | --------- | --------- | --------- | ------------ |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**<br>_64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5_                  | 2017.03.15  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.1.1, 1.0.4 | 3.13.767.0       | 4.7.1631  | 3.6       | 1.0.0     | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0**<br>_64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5_ | 2017.03.15  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.1.1, 1.0.4 | 3.13.767.0       | 4.7.1631  | 3.6       | 1.0.0     | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**<br>_64bit Windows Server 2012 v1.2.0 running IIS 8_                            | 2017.03.15  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.1.1, 1.0.4 | 3.13.767.0       | 4.7.1631  | 3.6       | 1.0.0     | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**<br>_64bit Windows Server 2008 R2 v1.2.0 running IIS 7.5_                  | 2017.03.15  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.1.1, 1.0.4 | 3.13.767.0       | 4.7.1631  | 3.6       | 1.0.0     | IIS 7.5      |
| **Windows Server 2012 R2 with IIS 8.5**<br>_64bit Windows Server 2012 R2 running IIS 8.5_                                       | 2017.03.15  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0                               | 3.13.767.0       | 4.7.1631  | 3.6       | 1.0.0     | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5**<br>_64bit Windows Server Core 2012 R2 running IIS 8.5_                      | 2017.03.15  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0                               | 3.13.767.0       | 4.7.1631  | 3.6       | 1.0.0     | IIS 8.5      |
| **Windows Server 2012 with IIS 8**<br>_64bit Windows Server 2012 running IIS 8_                                                 | 2017.03.15  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0                               | 3.13.767.0       | 4.7.1631  | 3.6       | 1.0.0     | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5**<br>_64bit Windows Server 2008 R2 running IIS 7.5_                                       | 2017.03.15  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0                               | 3.13.767.0       | 4.7.1631  | 3.6       | 1.0.0     | IIS 7.5      |

## January 16, 2017 – Apr 3, 2017

The following Elastic Beanstalk platform versions for .NET were current during this date range:

| Platform Version and _Solution Stack Name_                                                                                         | AMI version | Framework                                                                       | AWS SDK for .NET | EC2Config  | WebDeploy | AWS X-Ray | Proxy Server |
| ---------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------------------------------------------------------------------------------- | ---------------- | ---------- | --------- | --------- | ------------ |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**<br>_64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5_                     | 2016.12.14  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.1.0, 1.03 | 3.9.621.0        | 4.1.1396.0 | 3.6       | 1.0.0     | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version<br>1.2.0**<br>_64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5_ | 2016.12.14  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.1.0, 1.03 | 3.9.621.0        | 4.1.1396.0 | 3.6       | 1.0.0     | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**<br>_64bit Windows Server 2012 v1.2.0 running IIS 8_                               | 2016.12.14  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.1.0, 1.03 | 3.9.621.0        | 4.1.1396.0 | 3.6       | 1.0.0     | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**<br>_64bit Windows Server 2008 R2 v1.2.0 running IIS 7.5_                     | 2016.12.14  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.1.0, 1.03 | 3.9.621.0        | 4.1.1396.0 | 3.6       | 1.0.0     | IIS 7.5      |
| **Windows Server 2012 R2 with IIS 8.5**<br>_64bit Windows Server 2012 R2 running IIS 8.5_                                          | 2016.12.14  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0                              | 3.9.621.0        | 4.1.1396.0 | 3.6       | 1.0.0     | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5**<br>_64bit Windows Server Core 2012 R2 running IIS 8.5_                         | 2016.12.14  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0                              | 3.9.621.0        | 4.1.1396.0 | 3.6       | 1.0.0     | IIS 8.5      |
| **Windows Server 2012 with IIS 8**<br>_64bit Windows Server 2012 running IIS 8_                                                    | 2016.12.14  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0                              | 3.9.621.0        | 4.1.1396.0 | 3.6       | 1.0.0     | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5**<br>_64bit Windows Server 2008 R2 running IIS 7.5_                                          | 2016.12.14  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0                              | 3.9.621.0        | 4.1.1396.0 | 3.6       | 1.0.0     | IIS 7.5      |

1
[Microsoft
Security Bulletin Summary for January 2017](https://technet.microsoft.com/en-us/library/security/ms17-Jan.aspx "https://technet.microsoft.com/en-us/library/security/ms17-Jan.aspx")

## December 18, 2016 – January 15, 2017

The following Elastic Beanstalk platform versions for .NET were current during this date range:

| Platform Version and _Solution Stack Name_                                                                                         | AMI version | Framework                                                                 | AWS SDK for .NET | EC2Config   | WebDeploy | AWS X-Ray | Proxy Server |
| ---------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------------------------------------------------------------------------- | ---------------- | ----------- | --------- | --------- | ------------ |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**<br>_64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5_                     | 2016.11.09  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.1.0 | 3.9.560.0        | 3.19.1153.0 | 3.6       | 1.0.0     | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version<br>1.2.0**<br>_64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5_ | 2016.11.09  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.1.0 | 3.9.560.0        | 3.19.1153.0 | 3.6       | 1.0.0     | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**<br>_64bit Windows Server 2012 v1.2.0 running IIS 8_                               | 2016.11.09  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.1.0 | 3.9.560.0        | 3.19.1153.0 | 3.6       | 1.0.0     | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**<br>_64bit Windows Server 2008 R2 v1.2.0 running IIS 7.5_                     | 2016.11.09  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.1.0 | 3.9.560.0        | 3.19.1153.0 | 3.6       | 1.0.0     | IIS 7.5      |
| **Windows Server 2012 R2 with IIS 8.5**<br>_64bit Windows Server 2012 R2 running IIS 8.5_                                          | 2016.11.09  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0                        | 3.9.560.0        | 3.19.1153.0 | 3.6       | 1.0.0     | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5**<br>_64bit Windows Server Core 2012 R2 running IIS 8.5_                         | 2016.11.09  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0                        | 3.9.560.0        | 3.19.1153.0 | 3.6       | 1.0.0     | IIS 8.5      |
| **Windows Server 2012 with IIS 8**<br>_64bit Windows Server 2012 running IIS 8_                                                    | 2016.11.09  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0                        | 3.9.560.0        | 3.19.1153.0 | 3.6       | 1.0.0     | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5**<br>_64bit Windows Server 2008 R2 running IIS 7.5_                                          | 2016.11.09  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0                        | 3.9.560.0        | 3.19.1153.0 | 3.6       | 1.0.0     | IIS 7.5      |

1
[Microsoft
Security Bulletin Summary for December 2016](https://technet.microsoft.com/en-us/library/security/ms16-Dec.aspx "https://technet.microsoft.com/en-us/library/security/ms16-Dec.aspx")

## November 16, 2016 – December 18, 2016

The following Elastic Beanstalk platform versions for .NET were current during this date range:

| Platform Version and _Solution Stack Name_                                                                                         | AMI version | Framework                                                                 | AWS SDK for .NET | EC2Config   | WebDeploy | Proxy Server |
| ---------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------------------------------------------------------------------------- | ---------------- | ----------- | --------- | ------------ |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**<br>_64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5_                     | 2016.10.12  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.0.1 | 3.9.520.0        | 3.19.1153.0 | 3.6       | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version<br>1.2.0**<br>_64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5_ | 2016.10.12  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.0.1 | 3.9.520.0        | 3.19.1153.0 | 3.6       | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**<br>_64bit Windows Server 2012 v1.2.0 running IIS 8_                               | 2016.10.12  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.0.1 | 3.9.520.0        | 3.19.1153.0 | 3.6       | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**<br>_64bit Windows Server 2008 R2 v1.2.0 running IIS 7.5_                     | 2016.10.12  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.0.1 | 3.9.520.0        | 3.19.1153.0 | 3.6       | IIS 7.5      |
| **Windows Server 2012 R2 with IIS 8.5**<br>_64bit Windows Server 2012 R2 running IIS 8.5_                                          | 2016.10.12  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0                        | 3.9.520.0        | 3.19.1153.0 | 3.6       | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5**<br>_64bit Windows Server Core 2012 R2 running IIS 8.5_                         | 2016.10.12  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0                        | 3.9.520.0        | 3.19.1153.0 | 3.6       | IIS 8.5      |
| **Windows Server 2012 with IIS 8**<br>_64bit Windows Server 2012 running IIS 8_                                                    | 2016.10.12  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0                        | 3.9.520.0        | 3.19.1153.0 | 3.6       | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5**<br>_64bit Windows Server 2008 R2 running IIS 7.5_                                          | 2016.10.12  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0                        | 3.9.520.0        | 3.19.1153.0 | 3.6       | IIS 7.5      |

1
[Microsoft Security
Bulletin Summary for November 2016](https://technet.microsoft.com/en-us/library/security/ms16-Nov "https://technet.microsoft.com/en-us/library/security/ms16-Nov")

## October 21, 2016 – November 16, 2016

The following Elastic Beanstalk platform versions for .NET were current during this date range:

| Platform Version and _Solution Stack Name_                                                                                         | AMI version | Framework                                                                 | AWS SDK for .NET | EC2Config   | WebDeploy | Proxy Server |
| ---------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------------------------------------------------------------------------- | ---------------- | ----------- | --------- | ------------ |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**<br>_64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5_                     | 2016.09.14  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.0.1 | 3.9.459.0        | 3.19.1153.0 | 3.6       | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version<br>1.2.0**<br>_64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5_ | 2016.09.14  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.0.1 | 3.9.459.0        | 3.19.1153.0 | 3.6       | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**<br>_64bit Windows Server 2012 v1.2.0 running IIS 8_                               | 2016.09.14  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.0.1 | 3.9.459.0        | 3.19.1153.0 | 3.6       | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**<br>_64bit Windows Server 2008 R2 v1.2.0 running IIS 7.5_                     | 2016.09.14  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.0.1 | 3.9.459.0        | 3.19.1153.0 | 3.6       | IIS 7.5      |
| **Windows Server 2012 R2 with IIS 8.5**<br>_64bit Windows Server 2012 R2 running IIS 8.5_                                          | 2016.09.14  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0                        | 3.9.459.0        | 3.19.1153.0 | 3.6       | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5**<br>_64bit Windows Server Core 2012 R2 running IIS 8.5_                         | 2016.09.14  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0                        | 3.9.459.0        | 3.19.1153.0 | 3.6       | IIS 8.5      |
| **Windows Server 2012 with IIS 8**<br>_64bit Windows Server 2012 running IIS 8_                                                    | 2016.09.14  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0                        | 3.9.459.0        | 3.19.1153.0 | 3.6       | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5**<br>_64bit Windows Server 2008 R2 running IIS 7.5_                                          | 2016.09.14  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0                        | 3.9.459.0        | 3.19.1153.0 | 3.6       | IIS 7.5      |

1
[Microsoft
Security Bulletin Summary for October 2016](https://technet.microsoft.com/en-us/library/security/ms16-Oct.aspx "https://technet.microsoft.com/en-us/library/security/ms16-Oct.aspx")

## September 26, 2016 – October 21, 2016

The following Elastic Beanstalk platform versions for .NET were current during this date range:

| Platform Version and _Solution Stack Name_                                                                                         | AMI version | Framework                                                                 | AWS SDK for .NET | EC2Config   | WebDeploy | Proxy Server |
| ---------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------------------------------------------------------------------------- | ---------------- | ----------- | --------- | ------------ |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**<br>_64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5_                     | 2016.09.14  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.0.1 | 3.9.459.0        | 3.19.1153.0 | 3.6       | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version<br>1.2.0**<br>_64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5_ | 2016.09.14  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.0.1 | 3.9.459.0        | 3.19.1153.0 | 3.6       | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**<br>_64bit Windows Server 2012 v1.2.0 running IIS 8_                               | 2016.09.14  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.0.1 | 3.9.459.0        | 3.19.1153.0 | 3.6       | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**<br>_64bit Windows Server 2008 R2 v1.2.0 running IIS 7.5_                     | 2016.09.14  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.0.1 | 3.9.459.0        | 3.19.1153.0 | 3.6       | IIS 7.5      |
| **Windows Server 2012 R2 with IIS 8.5**<br>_64bit Windows Server 2012 R2 running IIS 8.5_                                          | 2016.09.14  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0                        | 3.9.459.0        | 3.19.1153.0 | 3.6       | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5**<br>_64bit Windows Server Core 2012 R2 running IIS 8.5_                         | 2016.09.14  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0                        | 3.9.459.0        | 3.19.1153.0 | 3.6       | IIS 8.5      |
| **Windows Server 2012 with IIS 8**<br>_64bit Windows Server 2012 running IIS 8_                                                    | 2016.09.14  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0                        | 3.9.459.0        | 3.19.1153.0 | 3.6       | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5**<br>_64bit Windows Server 2008 R2 running IIS 7.5_                                          | 2016.09.14  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0                        | 3.9.459.0        | 3.19.1153.0 | 3.6       | IIS 7.5      |

1
[Microsoft
Security Bulletin Summary for September 2016](https://technet.microsoft.com/en-us/library/security/ms16-Sep.aspx "https://technet.microsoft.com/en-us/library/security/ms16-Sep.aspx")

## August 23, 2016 – September 26, 2016

The following Elastic Beanstalk platform versions for .NET were current during this date range:

| Platform Version and _Solution Stack Name_                                                                                         | AMI version | Framework                                                               | AWS SDK for .NET | EC2Config | WebDeploy | Proxy Server |
| ---------------------------------------------------------------------------------------------------------------------------------- | ----------- | ----------------------------------------------------------------------- | ---------------- | --------- | --------- | ------------ |
| **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**<br>_64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5_                     | 2016.07.26  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.0 | 3.9.406.0        | 3.18.1118 | 3.6       | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version<br>1.2.0**<br>_64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5_ | 2016.07.26  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.0 | 3.9.406.0        | 3.18.1118 | 3.6       | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.2.0**<br>_64bit Windows Server 2012 v1.2.0 running IIS 8_                               | 2016.07.26  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.0 | 3.9.406.0        | 3.18.1118 | 3.6       | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**<br>_64bit Windows Server 2008 R2 v1.2.0 running IIS 7.5_                     | 2016.07.26  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0<br>ASP.NET Core v1.0 | 3.9.406.0        | 3.18.1118 | 3.6       | IIS 7.5      |
| **Windows Server 2012 R2 with IIS 8.5**<br>_64bit Windows Server 2012 R2 running IIS 8.5_                                          | 2016.07.26  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0                      | 3.9.406.0        | 3.18.1118 | 3.6       | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5**<br>_64bit Windows Server Core 2012 R2 running IIS 8.5_                         | 2016.07.26  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0                      | 3.9.406.0        | 3.18.1118 | 3.6       | IIS 8.5      |
| **Windows Server 2012 with IIS 8**<br>_64bit Windows Server 2012 running IIS 8_                                                    | 2016.07.26  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0                      | 3.9.406.0        | 3.18.1118 | 3.6       | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5**<br>_64bit Windows Server 2008 R2 running IIS 7.5_                                          | 2016.07.26  | .NET v4.6.2, Supports runtimes 4, 2.0, 1.1 and 1.0                      | 3.9.406.0        | 3.18.1118 | 3.6       | IIS 7.5      |

1
[Microsoft
Security Bulletin Summary for July 2016](https://technet.microsoft.com/en-us/library/security/ms16-jul.aspx "https://technet.microsoft.com/en-us/library/security/ms16-jul.aspx"), [Microsoft Security
Bulletin Summary for August 2016](https://technet.microsoft.com/en-us/library/security/ms16-aug.aspx "https://technet.microsoft.com/en-us/library/security/ms16-aug.aspx")

## June 21, 2016 – August 23, 2016

The following Elastic Beanstalk platform versions for .NET were current during this date range:

| Platform Version and _Solution Stack Name_                                                                                         | AMI version | Framework                                          | AWS SDK for .NET | EC2Config | WebDeploy | Proxy Server |
| ---------------------------------------------------------------------------------------------------------------------------------- | ----------- | -------------------------------------------------- | ---------------- | --------- | --------- | ------------ |
| **Windows Server 2012 R2 with IIS 8.5 version 1.1.0**<br>_64bit Windows Server 2012 R2 v1.1.0 running IIS 8.5_                     | 2016.05.11  | .NET v4.6.1, Supports runtimes 4, 2.0, 1.1 and 1.0 | 3.9.329.0        | 3.15.880  | 3.6       | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version<br>1.1.0**<br>_64bit Windows Server Core 2012 R2 v1.1.0 running IIS 8.5_ | 2016.05.11  | .NET v4.6.1, Supports runtimes 4, 2.0, 1.1 and 1.0 | 3.9.329.0        | 3.15.880  | 3.6       | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.1.0**<br>_64bit Windows Server 2012 v1.1.0 running IIS 8_                               | 2016.05.11  | .NET v4.6.1, Supports runtimes 4, 2.0, 1.1 and 1.0 | 3.9.329.0        | 3.15.880  | 3.6       | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5 version 1.1.0**<br>_64bit Windows Server 2008 R2 v1.1.0 running IIS 7.5_                     | 2016.05.11  | .NET v4.6.1, Supports runtimes 4, 2.0, 1.1 and 1.0 | 3.9.329.0        | 3.15.880  | 3.6       | IIS 7.5      |
| **Windows Server 2012 R2 with IIS 8.5**<br>_64bit Windows Server 2012 R2 running IIS 8.5_                                          | 2016.05.11  | .NET v4.6.1, Supports runtimes 4, 2.0, 1.1 and 1.0 | 3.9.329.0        | 3.15.880  | 3.6       | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5**<br>_64bit Windows Server Core 2012 R2 running IIS 8.5_                         | 2016.05.11  | .NET v4.6.1, Supports runtimes 4, 2.0, 1.1 and 1.0 | 3.9.329.0        | 3.15.880  | 3.6       | IIS 8.5      |
| **Windows Server 2012 with IIS 8**<br>_64bit Windows Server 2012 running IIS 8_                                                    | 2016.05.11  | .NET v4.6.1, Supports runtimes 4, 2.0, 1.1 and 1.0 | 3.9.329.0        | 3.15.880  | 3.6       | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5**<br>_64bit Windows Server 2008 R2 running IIS 7.5_                                          | 2016.05.11  | .NET v4.6.1, Supports runtimes 4, 2.0, 1.1 and 1.0 | 3.9.329.0        | 3.15.880  | 3.6       | IIS 7.5      |

1
[Microsoft
Security Bulletin Summary for June 2016](https://technet.microsoft.com/en-us/library/security/ms16-jun.aspx "https://technet.microsoft.com/en-us/library/security/ms16-jun.aspx")

## May 25, 2016 – June 21, 2016

The following Elastic Beanstalk platform versions for .NET were current during this date range:

| Platform Version and _Solution Stack Name_                                                                                         | AMI version | Framework                                          | AWS SDK for .NET | EC2Config | WebDeploy | Proxy Server |
| ---------------------------------------------------------------------------------------------------------------------------------- | ----------- | -------------------------------------------------- | ---------------- | --------- | --------- | ------------ |
| **Windows Server 2012 R2 with IIS 8.5 version 1.1.0**<br>_64bit Windows Server 2012 R2 v1.1.0 running IIS 8.5_                     | 2016.05.11  | .NET v4.6.1, Supports runtimes 4, 2.0, 1.1 and 1.0 | 3.9.329.0        | 3.15.880  | 3.6       | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5 version<br>1.1.0**<br>_64bit Windows Server Core 2012 R2 v1.1.0 running IIS 8.5_ | 2016.05.11  | .NET v4.6.1, Supports runtimes 4, 2.0, 1.1 and 1.0 | 3.9.329.0        | 3.15.880  | 3.6       | IIS 8.5      |
| **Windows Server 2012 with IIS 8 version 1.1.0**<br>_64bit Windows Server 2012 v1.1.0 running IIS 8_                               | 2016.05.11  | .NET v4.6.1, Supports runtimes 4, 2.0, 1.1 and 1.0 | 3.9.329.0        | 3.15.880  | 3.6       | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5 version 1.1.0**<br>_64bit Windows Server 2008 R2 v1.1.0 running IIS 7.5_                     | 2016.05.11  | .NET v4.6.1, Supports runtimes 4, 2.0, 1.1 and 1.0 | 3.9.329.0        | 3.15.880  | 3.6       | IIS 7.5      |
| **Windows Server 2012 R2 with IIS 8.5**<br>_64bit Windows Server 2012 R2 running IIS 8.5_                                          | 2016.05.11  | .NET v4.6.1, Supports runtimes 4, 2.0, 1.1 and 1.0 | 3.9.329.0        | 3.15.880  | 3.6       | IIS 8.5      |
| **Windows Server 2012 R2 Server Core with IIS 8.5**<br>_64bit Windows Server Core 2012 R2 running IIS 8.5_                         | 2016.05.11  | .NET v4.6.1, Supports runtimes 4, 2.0, 1.1 and 1.0 | 3.9.329.0        | 3.15.880  | 3.6       | IIS 8.5      |
| **Windows Server 2012 with IIS 8**<br>_64bit Windows Server 2012 running IIS 8_                                                    | 2016.05.11  | .NET v4.6.1, Supports runtimes 4, 2.0, 1.1 and 1.0 | 3.9.329.0        | 3.15.880  | 3.6       | IIS 8        |
| **Windows Server 2008 R2 with IIS 7.5**<br>_64bit Windows Server 2008 R2 running IIS 7.5_                                          | 2016.05.11  | .NET v4.6.1, Supports runtimes 4, 2.0, 1.1 and 1.0 | 3.9.329.0        | 3.15.880  | 3.6       | IIS 7.5      |

1
[Microsoft
Security Bulletin Summary for May 2016](https://technet.microsoft.com/en-us/library/security/ms16-may.aspx "https://technet.microsoft.com/en-us/library/security/ms16-may.aspx")

## April 25, 2016 – May 25, 2016

The following Elastic Beanstalk platform versions for .NET were current during this date range:

| Platform Version and _Solution Stack Name_                                                                                             | AMI version | Framework                                            | AWS SDK for .NET | EC2Config | WebDeploy | Proxy Server |
| -------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ---------------------------------------------------- | ---------------- | --------- | --------- | ------------ |
| **Windows Server 2012 R21 with<br>IIS 8.5 version 1.1.0**<br>_64bit Windows Server 2012 R2 v1.1.0 running IIS 8.5_                     | 2016.03.09  | .NET v4.6.1<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | 3.8.306.0        | 3.14.786  | 3.6       | IIS 8.5      |
| **Windows Server 2012 R21 Server<br>Core with IIS 8.5 version 1.1.0**<br>_64bit Windows Server Core 2012 R2 v1.1.0 running IIS<br>8.5_ | 2016.03.09  | .NET v4.6.1<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | 3.8.306.0        | 3.14.786  | 3.6       | IIS 8.5      |
| **Windows Server 20121 with IIS 8<br>version 1.1.0**<br>_64bit Windows Server 2012 v1.1.0 running IIS 8_                               | 2016.03.09  | .NET v4.6.1<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | 3.8.306.0        | 3.14.786  | 3.6       | IIS 8        |
| **Windows Server 2008 R21 with<br>IIS 7.5 version 1.1.0**<br>_64bit Windows Server 2008 R2 v1.1.0 running IIS 7.5_                     | 2016.03.09  | .NET v4.6.1<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | 3.8.306.0        | 3.14.786  | 3.6       | IIS 7.5      |
| **Windows Server 2012 R21 with<br>IIS 8.5**<br>_64bit Windows Server 2012 R2 running IIS 8.5_                                          | 2016.03.09  | .NET v4.6.1<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | 3.8.306.0        | 3.14.786  | 3.6       | IIS 8.5      |
| **Windows Server 2012 R21 Server<br>Core with IIS 8.5**<br>_64bit Windows Server Core 2012 R2 running IIS 8.5_                         | 2016.03.09  | .NET v4.6.1<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | 3.8.306.0        | 3.14.786  | 3.6       | IIS 8.5      |
| **Windows Server 20121 with IIS<br>8**<br>_64bit Windows Server 2012 running IIS 8_                                                    | 2016.03.09  | .NET v4.6.1<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | 3.8.306.0        | 3.14.786  | 3.6       | IIS 8        |
| **Windows Server 2008 R21 with<br>IIS 7.5**<br>_64bit Windows Server 2008 R2 running IIS 7.5_                                          | 2016.03.09  | .NET v4.6.1<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | 3.8.306.0        | 3.14.786  | 3.6       | IIS 7.5      |

1[Microsoft Security
Bulletin Summary for April 2016](https://technet.microsoft.com/en-us/library/security/ms16-apr.aspx "https://technet.microsoft.com/en-us/library/security/ms16-apr.aspx")

## March 23, 2016 – April 25, 2016

The following Elastic Beanstalk platform versions for .NET were current during this date range:

| Platform Version and _Solution Stack Name_                                                                                             | AMI version | Framework                                            | AWS SDK for .NET | EC2Config | Proxy Server |
| -------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ---------------------------------------------------- | ---------------- | --------- | ------------ |
| **Windows Server 2012 R21 with<br>IIS 8.5 version 1.1.0**<br>_64bit Windows Server 2012 R2 v1.1.0 running IIS 8.5_                     | 2016.02.10  | .NET v4.6.1<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | v3.1.36.1        | 3.12.649  | IIS 8.5      |
| **Windows Server 2012 R21 Server<br>Core with IIS 8.5 version 1.1.0**<br>_64bit Windows Server Core 2012 R2 v1.1.0 running IIS<br>8.5_ | 2016.02.10  | .NET v4.6.1<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | v3.1.36.1        | 3.12.649  | IIS 8.5      |
| **Windows Server 20121 with IIS 8<br>version 1.1.0**<br>_64bit Windows Server 2012 v1.1.0 running IIS 8_                               | 2016.02.10  | .NET v4.6.1<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | v3.1.36.1        | 3.12.649  | IIS 8        |
| **Windows Server 2008 R21 with<br>IIS 7.5 version 1.1.0**<br>_64bit Windows Server 2008 R2 v1.1.0 running IIS 7.5_                     | 2016.02.10  | .NET v4.6.1<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | v3.1.36.1        | 3.12.649  | IIS 7.5      |
| **Windows Server 2012 R21 with<br>IIS 8.5**<br>_64bit Windows Server 2012 R2 running IIS 8.5_                                          | 2016.02.10  | .NET v4.6.1<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | v3.1.36.1        | 3.12.649  | IIS 8.5      |
| **Windows Server 2012 R21 Server<br>Core with IIS 8.5**<br>_64bit Windows Server Core 2012 R2 running IIS 8.5_                         | 2016.02.10  | .NET v4.6.1<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | v3.1.36.1        | 3.12.649  | IIS 8.5      |
| **Windows Server 20121 with IIS<br>8**<br>_64bit Windows Server 2012 running IIS 8_                                                    | 2016.02.10  | .NET v4.6.1<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | v3.1.36.1        | 3.12.649  | IIS 8        |
| **Windows Server 2008 R21 with<br>IIS 7.5**<br>_64bit Windows Server 2008 R2 running IIS 7.5_                                          | 2016.02.10  | .NET v4.6.1<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | v3.1.36.1        | 3.12.649  | IIS 7.5      |

1[Microsoft Security
Bulletin Summary for March 2016](https://technet.microsoft.com/en-us/library/security/ms16-Mar "https://technet.microsoft.com/en-us/library/security/ms16-Mar")

## February 29, 2016 – March 23, 2016

The following Elastic Beanstalk platform versions for .NET were current during this date range:

| Platform Version and _Solution Stack Name_                                                                                             | AMI version | Framework                                            | AWS SDK for .NET | EC2Config | Web Server |
| -------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ---------------------------------------------------- | ---------------- | --------- | ---------- |
| **Windows Server 2012 R21 with<br>IIS 8.5 version 1.1.0**<br>_64bit Windows Server 2012 R2 v1.1.0 running IIS 8.5_                     | 2016.01.25  | .NET v4.6.1<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | v3.1.36.1        | 3.12.649  | IIS 8.5    |
| **Windows Server 2012 R21 Server<br>Core with IIS 8.5 version 1.1.0**<br>_64bit Windows Server Core 2012 R2 v1.1.0 running IIS<br>8.5_ | 2016.01.25  | .NET v4.6.1<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | v3.1.36.1        | 3.12.649  | IIS 8.5    |
| **Windows Server 20121 with IIS 8<br>version 1.1.0**<br>_64bit Windows Server 2012 v1.1.0 running IIS 8_                               | 2016.01.25  | .NET v4.6.1<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | v3.1.36.1        | 3.12.649  | IIS 8      |
| **Windows Server 2008 R21 with<br>IIS 7.5 version 1.1.0**<br>_64bit Windows Server 2008 R2 v1.1.0 running IIS 7.5_                     | 2016.01.25  | .NET v4.6.1<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | v3.1.36.1        | 3.12.649  | IIS 7.5    |
| **Windows Server 2012 R21 with<br>IIS 8.5**<br>_64bit Windows Server 2012 R2 running IIS 8.5_                                          | 2016.01.25  | .NET v4.6.1<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | v3.1.36.1        | 3.12.649  | IIS 8.5    |
| **Windows Server 2012 R21 Server<br>Core with IIS 8.5**<br>_64bit Windows Server Core 2012 R2 running IIS 8.5_                         | 2016.01.25  | .NET v4.6.1<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | v3.1.36.1        | 3.12.649  | IIS 8.5    |
| **Windows Server 20121 with IIS<br>8**<br>_64bit Windows Server 2012 running IIS 8_                                                    | 2016.01.25  | .NET v4.6.1<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | v3.1.36.1        | 3.12.649  | IIS 8      |
| **Windows Server 2008 R21 with<br>IIS 7.5**<br>_64bit Windows Server 2008 R2 running IIS 7.5_                                          | 2016.01.25  | .NET v4.6.1<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | v3.1.36.1        | 3.12.649  | IIS 7.5    |

1[Microsoft Security
Bulletin Summary for February 2016](https://technet.microsoft.com/en-us/library/security/ms16-Feb "https://technet.microsoft.com/en-us/library/security/ms16-Feb")

## January 28, 2016 – February 29, 2016

The following Elastic Beanstalk platform versions for .NET were current during this date range:

| Platform Version and _Solution Stack Name_                                                                                             | AMI version | Framework                                            | AWS SDK for .NET | Web Server |
| -------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ---------------------------------------------------- | ---------------- | ---------- |
| **Windows Server 2012 R21 with<br>IIS 8.5 version 1.1.0**<br>_64bit Windows Server 2012 R2 v1.1.0 running IIS 8.5_                     | 2015.12.31  | .NET v4.6.1<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | v3.1.36.1        | IIS 8.5    |
| **Windows Server 2012 R21 Server<br>Core with IIS 8.5 version 1.1.0**<br>_64bit Windows Server Core 2012 R2 v1.1.0 running IIS<br>8.5_ | 2015.12.31  | .NET v4.6.1<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | v3.1.36.1        | IIS 8.5    |
| **Windows Server 20121 with IIS 8<br>version 1.1.0**<br>_64bit Windows Server 2012 v1.1.0 running IIS 8_                               | 2015.12.31  | .NET v4.6.1<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | v3.1.36.1        | IIS 8      |
| **Windows Server 2008 R21 with<br>IIS 7.5 version 1.1.0**<br>_64bit Windows Server 2008 R2 v1.1.0 running IIS 7.5_                     | 2015.12.31  | .NET v4.6.1<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | v3.1.36.1        | IIS 7.5    |
| **Windows Server 2012 R21 with<br>IIS 8.5**<br>_64bit Windows Server 2012 R2 running IIS 8.5_                                          | 2015.12.31  | .NET v4.6.1<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | v3.1.36.1        | IIS 8.5    |
| **Windows Server 2012 R21 Server<br>Core with IIS 8.5**<br>_64bit Windows Server Core 2012 R2 running IIS 8.5_                         | 2015.12.31  | .NET v4.6.1<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | v3.1.36.1        | IIS 8.5    |
| **Windows Server 20121 with IIS<br>8**<br>_64bit Windows Server 2012 running IIS 8_                                                    | 2015.12.31  | .NET v4.6.1<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | v3.1.36.1        | IIS 8      |
| **Windows Server 2008 R21 with<br>IIS 7.5**<br>_64bit Windows Server 2008 R2 running IIS 7.5_                                          | 2015.12.31  | .NET v4.6.1<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | v3.1.36.1        | IIS 7.5    |

1[Microsoft Security
Bulletin Summary for January 2016](https://technet.microsoft.com/en-us/library/security/ms16-Jan "https://technet.microsoft.com/en-us/library/security/ms16-Jan")

## December 15, 2015 – January 28, 2016

The following Elastic Beanstalk platform versions for .NET were current during this date range:

| Platform Version and _Solution Stack Name_                                                                                             | Framework                                          | Web Server |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | ---------- |
| **Windows Server 2012 R21 with<br>IIS 8.5 version 1.1.0**<br>_64bit Windows Server 2012 R2 v1.1.0 running IIS 8.5_                     | .NET v4.6<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | IIS 8.5    |
| **Windows Server 2012 R21 Server<br>Core with IIS 8.5 version 1.1.0**<br>_64bit Windows Server Core 2012 R2 v1.1.0 running IIS<br>8.5_ | .NET v4.6<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | IIS 8.5    |
| **Windows Server 20121 with IIS 8<br>version 1.1.0**<br>_64bit Windows Server 2012 v1.1.0 running IIS 8_                               | .NET v4.6<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | IIS 8      |
| **Windows Server 2008 R21 with<br>IIS 7.5 version 1.1.0**<br>_64bit Windows Server 2008 R2 v1.1.0 running IIS 7.5_                     | .NET v4.5<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | IIS 7.5    |
| **Windows Server 2012 R21 with<br>IIS 8.5**<br>_64bit Windows Server 2012 R2 running IIS 8.5_                                          | .NET v4.6<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | IIS 8.5    |
| **Windows Server 2012 R21 Server<br>Core with IIS 8.5**<br>_64bit Windows Server Core 2012 R2 running IIS 8.5_                         | .NET v4.6<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | IIS 8.5    |
| **Windows Server 20121 with IIS<br>8**<br>_64bit Windows Server 2012 running IIS 8_                                                    | .NET v4.6<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | IIS 8      |
| **Windows Server 2008 R21 with<br>IIS 7.5**<br>_64bit Windows Server 2008 R2 running IIS 7.5_                                          | .NET v4.5<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | IIS 7.5    |

1[Microsoft Security
Bulletin Summary for November 2015](https://technet.microsoft.com/en-us/library/security/ms15-nov.aspx "https://technet.microsoft.com/en-us/library/security/ms15-nov.aspx"), [Microsoft Security
Bulletin Summary for December 2015](https://technet.microsoft.com/en-us/library/security/ms15-dec.aspx "https://technet.microsoft.com/en-us/library/security/ms15-dec.aspx")

## October 21, 2015 – December 15, 2015

The following Elastic Beanstalk platform versions for .NET were current during this date range:

| Platform Version and _Solution Stack Name_                                                                                             | Framework                                          | Web Server |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | ---------- |
| **Windows Server 2012 R21 with<br>IIS 8.5 version 1.0.0**<br>_64bit Windows Server 2012 R2 v1.0.0 running IIS 8.5_                     | .NET v4.6<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | IIS 8.5    |
| **Windows Server 2012 R21 Server<br>Core with IIS 8.5 version 1.0.0**<br>_64bit Windows Server Core 2012 R2 v1.0.0 running IIS<br>8.5_ | .NET v4.6<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | IIS 8.5    |
| **Windows Server 20121 with IIS 8<br>version 1.0.0**<br>_64bit Windows Server 2012 v1.0.0 running IIS 8_                               | .NET v4.6<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | IIS 8      |
| **Windows Server 2008 R21 with<br>IIS 7.5 version 1.0.0**<br>_64bit Windows Server 2008 R2 v1.0.0 running IIS 7.5_                     | .NET v4.5<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | IIS 7.5    |
| **Windows Server 2012 R21 with<br>IIS 8.5**<br>_64bit Windows Server 2012 R2 running IIS 8.5_                                          | .NET v4.6<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | IIS 8.5    |
| **Windows Server 2012 R21 Server<br>Core with IIS 8.5**<br>_64bit Windows Server Core 2012 R2 running IIS 8.5_                         | .NET v4.6<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | IIS 8.5    |
| **Windows Server 20121 with IIS<br>8**<br>_64bit Windows Server 2012 running IIS 8_                                                    | .NET v4.6<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | IIS 8      |
| **Windows Server 2008 R21 with<br>IIS 7.5**<br>_64bit Windows Server 2008 R2 running IIS 7.5_                                          | .NET v4.5<br>Supports runtimes 4, 2.0, 1.1 and 1.0 | IIS 7.5    |

## September 14, 2015 – October 21, 2015

The following Elastic Beanstalk platform versions for .NET were current during this date range:

| Platform Version and _Solution Stack Name_                                                                     | Framework                                                  | Web Server |
| -------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ---------- |
| **Windows Server 2012 R21 with<br>IIS 8.5**<br>_64bit Windows Server 2012 R2 running IIS 8.5_                  | .NET v4.5<br>Also supports 4.0, 3.5, 3.0, 2.0, 1.1 and 1.0 | IIS 8.5    |
| **Windows Server 2012 R21 Server<br>Core with IIS 8.5**<br>_64bit Windows Server Core 2012 R2 running IIS 8.5_ | .NET v4.5<br>Also supports 4.0, 3.5, 3.0, 2.0, 1.1 and 1.0 | IIS 8.5    |
| **Windows Server 20121 with IIS<br>8**<br>_64bit Windows Server 2012 running IIS 8_                            | .NET v4.5<br>Also supports 4.0, 3.5, 3.0, 2.0, 1.1 and 1.0 | IIS 8      |
| **Windows Server 2008 R21 with<br>IIS 7.5**<br>_64bit Windows Server 2008 R2 running IIS 7.5_                  | .NET v4.5<br>Also supports 4.0, 3.5, 3.0, 2.0, 1.1 and 1.0 | IIS 7.5    |

1[Microsoft Security
Bulletin Summary for September 2015](https://technet.microsoft.com/en-us/library/security/ms15-sep.aspx "https://technet.microsoft.com/en-us/library/security/ms15-sep.aspx")

## August 20, 2015 – September 14, 2015

The following Elastic Beanstalk platform versions for .NET were current during this date range:

| Platform Version and _Solution Stack Name_                                                                     | Framework                                                  | Web Server |
| -------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ---------- |
| **Windows Server 2012 R21 with<br>IIS 8.5**<br>_64bit Windows Server 2012 R2 running IIS 8.5_                  | .NET v4.5<br>Also supports 4.0, 3.5, 3.0, 2.0, 1.1 and 1.0 | IIS 8.5    |
| **Windows Server 2012 R21 Server<br>Core with IIS 8.5**<br>_64bit Windows Server Core 2012 R2 running IIS 8.5_ | .NET v4.5<br>Also supports 4.0, 3.5, 3.0, 2.0, 1.1 and 1.0 | IIS 8.5    |
| **Windows Server 20121 with IIS<br>8**<br>_64bit Windows Server 2012 running IIS 8_                            | .NET v4.5<br>Also supports 4.0, 3.5, 3.0, 2.0, 1.1 and 1.0 | IIS 8      |
| **Windows Server 2008 R21 with<br>IIS 7.5**<br>_64bit Windows Server 2008 R2 running IIS 7.5_                  | .NET v4.5<br>Also supports 4.0, 3.5, 3.0, 2.0, 1.1 and 1.0 | IIS 7.5    |

1[Microsoft Security
Bulletin Summary for August 2015](https://technet.microsoft.com/en-us/library/security/ms15-aug.aspx "https://technet.microsoft.com/en-us/library/security/ms15-aug.aspx")

## July 21, 2015 – August 20, 2015

The following Elastic Beanstalk platform versions for .NET were current during this date range:

| Platform Version and _Solution Stack Name_                                                                     | Framework                                                  | Web Server |
| -------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ---------- |
| **Windows Server 2012 R21 with<br>IIS 8.5**<br>_64bit Windows Server 2012 R2 running IIS 8.5_                  | .NET v4.5<br>Also supports 4.0, 3.5, 3.0, 2.0, 1.1 and 1.0 | IIS 8.5    |
| **Windows Server 2012 R21 Server<br>Core with IIS 8.5**<br>_64bit Windows Server Core 2012 R2 running IIS 8.5_ | .NET v4.5<br>Also supports 4.0, 3.5, 3.0, 2.0, 1.1 and 1.0 | IIS 8.5    |
| **Windows Server 20121 with IIS<br>8**<br>_64bit Windows Server 2012 running IIS 8_                            | .NET v4.5<br>Also supports 4.0, 3.5, 3.0, 2.0, 1.1 and 1.0 | IIS 8      |
| **Windows Server 2008 R21 with<br>IIS 7.5**<br>_64bit Windows Server 2008 R2 running IIS 7.5_                  | .NET v4.5<br>Also supports 4.0, 3.5, 3.0, 2.0, 1.1 and 1.0 | IIS 7.5    |

1[Microsoft Security
Bulletin Summary for July 2015](https://technet.microsoft.com/en-us/library/security/ms15-jul.aspx "https://technet.microsoft.com/en-us/library/security/ms15-jul.aspx")

## June 12, 2015 – July 21, 2015

The following Elastic Beanstalk platform versions for .NET were current during this date range:

| Platform Version and _Solution Stack Name_                                                                     | Framework                                                  | Web Server |
| -------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ---------- |
| **Windows Server 2012 R21 with<br>IIS 8.5**<br>_64bit Windows Server 2012 R2 running IIS 8.5_                  | .NET v4.5<br>Also supports 4.0, 3.5, 3.0, 2.0, 1.1 and 1.0 | IIS 8.5    |
| **Windows Server 2012 R21 Server<br>Core with IIS 8.5**<br>_64bit Windows Server Core 2012 R2 running IIS 8.5_ | .NET v4.5<br>Also supports 4.0, 3.5, 3.0, 2.0, 1.1 and 1.0 | IIS 8.5    |
| **Windows Server 20121 with IIS<br>8**<br>_64bit Windows Server 2012 running IIS 8_                            | .NET v4.5<br>Also supports 4.0, 3.5, 3.0, 2.0, 1.1 and 1.0 | IIS 8      |
| **Windows Server 2008 R21 with<br>IIS 7.5**<br>_64bit Windows Server 2008 R2 running IIS 7.5_                  | .NET v4.5<br>Also supports 4.0, 3.5, 3.0, 2.0, 1.1 and 1.0 | IIS 7.5    |

1[Microsoft Security
Bulletin Summary for June 2015](https://technet.microsoft.com/en-us/library/security/ms15-jun.aspx "https://technet.microsoft.com/en-us/library/security/ms15-jun.aspx")

## April 16, 2015 – June 12, 2015

The following Elastic Beanstalk platform versions for .NET were current during this date range:

| **IIS Configurations**                                |
| ----------------------------------------------------- | ------- | ---------------------------------------------------------- | -------------- |
| **Name**                                              | **AMI** | **Language**                                               | **Web Server** |
| 64bit Windows Server 2012 R21 running IIS 8.5         | Custom  | .NET v4.5<br>Also supports 4.0, 3.5, 3.0, 2.0, 1.1 and 1.0 | IIS 8.5        |
| 64bit Windows Server Core 2012 R21 running IIS<br>8.5 | Custom  | .NET v4.5<br>Also supports 4.0, 3.5, 3.0, 2.0, 1.1 and 1.0 | IIS 8.5        |
| 64bit Windows Server 20121 running IIS 8              | Custom  | .NET v4.5<br>Also supports 4.0, 3.5, 3.0, 2.0, 1.1 and 1.0 | IIS 8          |
| 64bit Windows Server 2008 R21 running IIS 7.5         | Custom  | .NET v4.5<br>Also supports 4.0, 3.5, 3.0, 2.0, 1.1 and 1.0 | IIS 7.5        |

1[Microsoft Security
Bulletin Summary for May 2015](https://technet.microsoft.com/en-us/library/security/ms15-may.aspx "https://technet.microsoft.com/en-us/library/security/ms15-may.aspx")

## August 6, 2014 – April 16, 2015

The following Elastic Beanstalk platform versions for .NET were current during this date range:

| **IIS Configurations**                                |
| ----------------------------------------------------- | ------- | ---------------------------------------------------------- | -------------- |
| **Name**                                              | **AMI** | **Language**                                               | **Web Server** |
| 64bit Windows Server 2012 R21 running IIS 8.5         | Custom  | .NET v4.5<br>Also supports 4.0, 3.5, 3.0, 2.0, 1.1 and 1.0 | IIS 8.5        |
| 64bit Windows Server Core 2012 R21 running IIS<br>8.5 | Custom  | .NET v4.5<br>Also supports 4.0, 3.5, 3.0, 2.0, 1.1 and 1.0 | IIS 8.5        |
| 64bit Windows Server 20121 running IIS 8              | Custom  | .NET v4.5<br>Also supports 4.0, 3.5, 3.0, 2.0, 1.1 and 1.0 | IIS 8          |
| 64bit Windows Server 2008 R21 running IIS 7.5         | Custom  | .NET v4.5<br>Also supports 4.0, 3.5, 3.0, 2.0, 1.1 and 1.0 | IIS 7.5        |

1[Microsoft Security Bulletin
MS14-066 - Critical](https://technet.microsoft.com/library/security/ms14-066 "https://technet.microsoft.com/library/security/ms14-066")

## Prior to August 6, 2014

The following Elastic Beanstalk platform versions for .NET were current prior to August 6, 2014:

| **IIS Configurations**                        |
| --------------------------------------------- | ------- | ---------------------------------------------------------- | -------------- |
| **Name**                                      | **AMI** | **Language**                                               | **Web Server** |
| 64bit Windows Server 20121 running IIS 8      | Custom  | .NET v4.5<br>Also supports 4.0, 3.5, 3.0, 2.0, 1.1 and 1.0 | IIS 8          |
| 64bit Windows Server 2008 R21 running IIS 7.5 | Custom  | .NET v4.5<br>Also supports 4.0, 3.5, 3.0, 2.0, 1.1 and 1.0 | IIS 7.5        |

1[Microsoft Security Bulletin
MS14-066 - Critical](https://technet.microsoft.com/library/security/ms14-066 "https://technet.microsoft.com/library/security/ms14-066")
