# Amazon ECS-optimized Windows AMI

versions

View the current and previous versions of the Amazon ECS-optimized AMIs and their
corresponding versions of the Amazon ECS container agent, Docker, and the
`ecs-init` package.

The Amazon ECS-optimized AMI metadata, including the AMI ID, for each variant can be
retrieved programmatically. For more information, see [Retrieving Amazon ECS-optimized Windows
AMI metadata](retrieve-ecs-optimized_windows_AMI.md "retrieve-ecs-optimized_windows_AMI.md").

The following tabs display a list of Windows Amazon ECS-optimized AMIs versions. For
details on referencing the Systems Manager Parameter Store parameter in an AWS CloudFormation template, see
[Using the latest
recommended Amazon ECS-optimized AMI in an AWS CloudFormation template](retrieve-ecs-optimized_AMI.md#ecs-optimized-ami-parameter-examples-5 "retrieve-ecs-optimized_AMI.md#ecs-optimized-ami-parameter-examples-5").

###### Important

To ensure that customers have the latest security updates by
default, Amazon ECS maintains at least the last three Windows
Amazon ECS-optimized AMIs. After releasing new Windows
Amazon ECS-optimized AMIs, Amazon ECS makes the Windows Amazon ECS-optimized
AMIs that are older private. If there is a private AMI that
you need access to, let us know by filing a ticket with Cloud
Support.

Windows Server 2016 does not support the latest Docker version, for example 25.x.x. Therefore the Windows Server 2016 Full AMIs will
not receive security or bug patches to the Docker runtime. We recommend that you move to one
of the following Windows platforms:

- Windows Server 2022 Full
- Windows Server 2022 Core
- Windows Server 2019 Full
- Windows Server 2019 Core

###### Note

gMSA plugin logging has been migrated from file-based logging
`(C:\ProgramData\Amazon\gmsa)` to Windows Event logging with the August 2025 AMI
release. The public log collector script will collect all gMSA logs. For more information, see [Collecting container logs with Amazon ECS logs collector](ecs-logs-collector.md "ecs-logs-collector.md") .

Windows Server 2025 Full AMI versions
The table below lists the current and previous versions of the
Amazon ECS-optimized Windows Server 2025 Full AMI and their corresponding versions of the Amazon ECS
container agent and Docker.

| Amazon ECS-optimized Windows Server 2025 Full AMI             | Amazon ECS container agent version | Docker version       | Visibility |
| ------------------------------------------------------------- | ---------------------------------- | -------------------- | ---------- |
| **Windows_Server-2025-English-Full-ECS_Optimized-2025.09.13** | `1.99.0`                           | `25.0.6 (Docker CE)` | Public     |
| **Windows_Server-2025-English-Full-ECS_Optimized-2025.08.24** | `1.98.0`                           | `25.0.6 (Docker CE)` | Public     |
| **Windows_Server-2025-English-Full-ECS_Optimized-2025.08.16** | `1.97.1`                           | `25.0.6 (Docker CE)` | Public     |
| **Windows_Server-2025-English-Full-ECS_Optimized-2025.07.16** | `1.96.0`                           | `25.0.6 (Docker CE)` | Public     |
| **Windows_Server-2025-English-Full-ECS_Optimized-2025.06.13** | `1.94.0`                           | `25.0.6 (Docker CE)` | Public     |

Use the following AWS CLI command to retrieve the current
Amazon ECS-optimized Windows Server 2025 Full AMI.

```
`aws ssm get-parameters --names /aws/service/ami-windows-latest/Windows_Server-2025-English-Full-ECS_Optimized`
```

Windows Server 2025 Core AMI versions
The table below lists the current and previous versions of the
Amazon ECS-optimized Windows Server 2025 Core AMI and their corresponding versions of the
Amazon ECS container agent and Docker.

| Amazon ECS-optimized Windows Server 2025 Core AMI             | Amazon ECS container agent version | Docker version       | Visibility |
| ------------------------------------------------------------- | ---------------------------------- | -------------------- | ---------- |
| **Windows_Server-2025-English-Core-ECS_Optimized-2025.09.13** | `1.99.0`                           | `25.0.6 (Docker CE)` | Public     |
| **Windows_Server-2025-English-Core-ECS_Optimized-2025.08.24** | `1.98.0`                           | `25.0.6 (Docker CE)` | Public     |
| **Windows_Server-2025-English-Core-ECS_Optimized-2025.08.16** | `1.97.1`                           | `25.0.6 (Docker CE)` | Public     |
| **Windows_Server-2025-English-Core-ECS_Optimized-2025.07.16** | `1.96.0`                           | `25.0.6 (Docker CE)` | Public     |
| **Windows_Server-2025-English-Core-ECS_Optimized-2025.06.13** | `1.94.0`                           | `25.0.6 (Docker CE)` | Public     |

Use the following AWS CLI command to retrieve the current
Amazon ECS-optimized Windows Server 2025 Core AMI.

```
`aws ssm get-parameters --names /aws/service/ami-windows-latest/Windows_Server-2025-English-Core-ECS_Optimized`
```

Windows Server 2022 Full AMI versions
The table below lists the current and previous versions of the
Amazon ECS-optimized Windows Server 2022 Full AMI and their corresponding versions of the Amazon ECS
container agent and Docker.

| Amazon ECS-optimized Windows Server 2022 Full AMI             | Amazon ECS container agent version | Docker version       | Visibility |
| ------------------------------------------------------------- | ---------------------------------- | -------------------- | ---------- |
| **Windows_Server-2022-English-Full-ECS_Optimized-2025.09.13** | `1.99.0`                           | `25.0.6 (Docker CE)` | Public     |
| **Windows_Server-2022-English-Full-ECS_Optimized-2025.08.24** | `1.98.0`                           | `25.0.6 (Docker CE)` | Public     |
| **Windows_Server-2022-English-Full-ECS_Optimized-2025.08.16** | `1.97.1`                           | `25.0.6 (Docker CE)` | Public     |
| **Windows_Server-2022-English-Full-ECS_Optimized-2025.07.16** | `1.95.0`                           | `25.0.6 (Docker CE)` | Public     |

Use the following AWS CLI command to retrieve the current
Amazon ECS-optimized Windows Server 2022 Full AMI.

```
`aws ssm get-parameters --names /aws/service/ami-windows-latest/Windows_Server-2022-English-Full-ECS_Optimized`
```

Windows Server 2022 Core AMI versions
The table below lists the current and previous versions of the
Amazon ECS-optimized Windows Server 2022 Core AMI and their corresponding versions of the
Amazon ECS container agent and Docker.

| Amazon ECS-optimized Windows Server 2022 Core AMI             | Amazon ECS container agent version | Docker version       | Visibility |
| ------------------------------------------------------------- | ---------------------------------- | -------------------- | ---------- |
| **Windows_Server-2022-English-Core-ECS_Optimized-2025.09.13** | `1.99.0`                           | `25.0.6 (Docker CE)` | Public     |
| **Windows_Server-2022-English-Core-ECS_Optimized-2025.08.24** | `1.98.0`                           | `25.0.6 (Docker CE)` | Public     |
| **Windows_Server-2022-English-Core-ECS_Optimized-2025.08.16** | `1.97.1`                           | `25.0.6 (Docker CE)` | Public     |
| **Windows_Server-2022-English-Core-ECS_Optimized-2025.07.16** | `1.95.0`                           | `25.0.6 (Docker CE)` | Public     |

Use the following AWS CLI command to retrieve the current
Amazon ECS-optimized Windows Server 2022 Full AMI.

```
`aws ssm get-parameters --names /aws/service/ami-windows-latest/Windows_Server-2022-English-Core-ECS_Optimized`
```

Windows Server 2019 Full AMI versions
The table below lists the current and previous versions of the
Amazon ECS-optimized Windows Server 2019 Full AMI and their corresponding versions of the Amazon ECS
container agent and Docker.

| Amazon ECS-optimized Windows Server 2019 Full AMI             | Amazon ECS container agent version | Docker version       | Visibility |
| ------------------------------------------------------------- | ---------------------------------- | -------------------- | ---------- |
| **Windows_Server-2019-English-Full-ECS_Optimized-2025.09.13** | `1.99.0`                           | `25.0.6 (Docker CE)` | Public     |
| **Windows_Server-2019-English-Full-ECS_Optimized-2025.08.24** | `1.98.0`                           | `25.0.6 (Docker CE)` | Public     |
| **Windows_Server-2019-English-Full-ECS_Optimized-2025.08.16** | `1.97.1`                           | `25.0.6 (Docker CE)` | Public     |
| **Windows_Server-2019-English-Full-ECS_Optimized-2025.07.16** | `1.95.0`                           | `25.0.6 (Docker CE)` | Public     |

Use the following AWS CLI command to retrieve the current
Amazon ECS-optimized Windows Server 2019 Full AMI.

```
`aws ssm get-parameters --names /aws/service/ami-windows-latest/Windows_Server-2019-English-Full-ECS_Optimized`
```

Windows Server 2019 Core AMI versions
The table below lists the current and previous versions of the
Amazon ECS-optimized Windows Server 2019 Core AMI and their corresponding versions of the
Amazon ECS container agent and Docker.

| Amazon ECS-optimized Windows Server 2019 Core AMI             | Amazon ECS container agent version | Docker version       | Visibility |
| ------------------------------------------------------------- | ---------------------------------- | -------------------- | ---------- |
| **Windows_Server-2019-English-Core-ECS_Optimized-2025.09.13** | `1.99.0`                           | `25.0.6 (Docker CE)` | Public     |
| **Windows_Server-2019-English-Core-ECS_Optimized-2025.08.24** | `1.98.0`                           | `25.0.6 (Docker CE)` | Public     |
| **Windows_Server-2019-English-Core-ECS_Optimized-2025.08.16** | `1.97.1`                           | `25.0.6 (Docker CE)` | Public     |
| **Windows_Server-2019-English-Core-ECS_Optimized-2025.07.16** | `1.95.0`                           | `25.0.6 (Docker CE)` | Public     |

Use the following AWS CLI command to retrieve the current
Amazon ECS-optimized Windows Server 2019 Full AMI.

```
`aws ssm get-parameters --names /aws/service/ami-windows-latest/Windows_Server-2019-English-Core-ECS_Optimized`
```

Windows Server 2016 Full AMI versions

###### Important

Windows Server 2016 does not support the latest Docker version, for example 25.x.x. Therefore the Windows Server 2016 Full AMIs will
not receive security or bug patches to the Docker runtime. We recommend that you move to one
of the following Windows platforms:

- Windows Server 2022 Full
- Windows Server 2022 Core
- Windows Server 2019 Full
- Windows Server 2019 Core

The table below lists the current and previous versions of the
Amazon ECS-optimized Windows Server 2016 Full AMI and their corresponding versions of the Amazon ECS
container agent and Docker.

| Amazon ECS-optimized Windows Server 2016 Full AMI             | Amazon ECS container agent version | Docker version         | Visibility |
| ------------------------------------------------------------- | ---------------------------------- | ---------------------- | ---------- |
| **Windows_Server-2016-English-Full-ECS_Optimized-2025.09.13** | `1.99.0`                           | `20.10.23 (Docker CE)` | Public     |
| **Windows_Server-2016-English-Full-ECS_Optimized-2025.08.16** | `1.97.1`                           | `20.10.23 (Docker CE)` | Public     |
| **Windows_Server-2016-English-Full-ECS_Optimized-2025.07.16** | `1.95.0`                           | `20.10.23 (Docker CE)` | Public     |
| **Windows_Server-2016-English-Full-ECS_Optimized-2025.06.13** | `1.94.0`                           | `20.10.23 (Docker CE)` | Public     |

Use the following AWS CLI Amazon ECS-optimized Windows Server 2016 Full AMI.

```
`aws ssm get-parameters --names /aws/service/ami-windows-latest/Windows_Server-2016-English-Full-ECS_Optimized`
```
