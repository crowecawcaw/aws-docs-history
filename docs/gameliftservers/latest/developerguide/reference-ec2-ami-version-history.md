# Amazon GameLift Servers AMI versions

The following table identifies the latest Amazon machine images (AMIs) that Amazon GameLift Servers uses for
managed EC2 hosting. As described in [Configuration and vulnerability analysis
in Amazon GameLift Servers](vulnerability-analysis-management.md "vulnerability-analysis-management.md"), you must regularly create new Amazon GameLift Servers
managed EC2 fleets to deploy the latest AMI version updates.

**AMIs for use with server SDK for Amazon GameLift Servers 5+**

Amazon GameLift Servers uses the following AMIs to host game servers that are integrated with server SDK for
Amazon GameLift Servers version 5.

| Amazon GameLift Servers image                | Architecture | Most recent patch | Base AWS image                                                                                                                                                                                                                                      |
| -------------------------------------------- | ------------ | ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Amazon Linux 2023<br>BASE_AMI_LINUX_2023     | x86          | 2025-06-12        | Amazon Linux 2023 AMI 2023.7.20250609.0 x86_64 HVM kernel-6.1 ([release notes](../../../linux/al2023/release-notes/relnotes-2023.7.md "../../../linux/al2023/release-notes/relnotes-2023.7.md"))                                                    |
| Amazon Linux 2<br>BASE_AMI_LINUX_2_SDK_5     | x86          | 2025-06-12        | Amazon Linux 2 Kernel 5.10 AMI 2.0.20250603.0 x86_64 HVM gp2 ([release notes](../../../AL2/latest/relnotes/relnotes-20250603.md "../../../AL2/latest/relnotes/relnotes-20250603.md"))                                                               |
| Windows 2016<br>BASE_AMI_WINDOWS_2016_SDK_5  | x86          | 2025-06-12        | Windows_Server-2016-English-Full-Base-2025.06.12 ([release notes](../../../ec2/latest/windows-ami-reference/ec2-windows-ami-version-history.md#amis-2025 "../../../ec2/latest/windows-ami-reference/ec2-windows-ami-version-history.md#amis-2025")) |
| Amazon Linux 2023<br>BASE_AMI_LINUX_2023_ARM | ARM64        | 2025-06-12        | Amazon Linux 2023 AMI 2023.7.20250609.0 arm64 HVM kernel-6.1 ([release notes](../../../linux/al2023/release-notes/relnotes-2023.7.md "../../../linux/al2023/release-notes/relnotes-2023.7.md"))                                                     |
| Amazon Linux 2<br>BASE_AMI_LINUX_2_ARM       | ARM64        | 2025-06-12        | Amazon Linux 2 LTS Arm64 Kernel 5.10 AMI 2.0.20250603.0 arm64 HVM gp2 ([release notes](../../../AL2/latest/relnotes/relnotes-20250603.md "../../../AL2/latest/relnotes/relnotes-20250603.md"))                                                      |
| Windows 2022<br>BASE_AMI_WINDOWS_2022        | x86          | 2025-10-27        | Windows_Server-2022-English-Full-Base-2025.10.15 ([release notes](../../../ec2/latest/windows-ami-reference/ec2-windows-ami-version-history.md#amis-2025 "../../../ec2/latest/windows-ami-reference/ec2-windows-ami-version-history.md#amis-2025")) |

**AMIs for use with server SDK for Amazon GameLift Servers 4**

Amazon GameLift Servers uses the following AMIs to host game servers that are integrated with server SDK for
Amazon GameLift Servers version 4 or earlier.

| Amazon GameLift Servers image                  | Architecture | Most recent patch | Base AWS image                                                                                                                                                                                                                                      |
| ---------------------------------------------- | ------------ | ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Amazon Linux 2<br>BASE_AMI_LINUX_2_SDK_4       | x86          | 2025-06-12        | Amazon Linux 2 AMI 2.0.20250605.0 x86_64 HVM gp2 ([release notes](../../../AL2/latest/relnotes/relnotes-20250605.md "../../../AL2/latest/relnotes/relnotes-20250605.md"))                                                                           |
| Amazon Linux 2023<br>BASE_AMI_LINUX_2023_SDK_4 | x86          | 2025-10-30        | Amazon Linux 2023 AMI 2023.9.20251027.0 x86_64 HVM kernel-6.1 ([release notes](../../../linux/al2023/release-notes/relnotes-2023.9.md "../../../linux/al2023/release-notes/relnotes-2023.9.md"))                                                    |
| Windows 2016<br>BASE_AMI_WINDOWS_2016_SDK_4    | x86          | 2025-06-12        | Windows_Server-2016-English-Full-Base-2025.06.12 ([release notes](../../../ec2/latest/windows-ami-reference/ec2-windows-ami-version-history.md#amis-2025 "../../../ec2/latest/windows-ami-reference/ec2-windows-ami-version-history.md#amis-2025")) |

For more information, see the following resources:

- [Amazon Linux 2023 release notes](../../../linux/al2023/release-notes/relnotes.md "../../../linux/al2023/release-notes/relnotes.md")
- [Amazon Linux 2 release notes](../../../AL2/latest/relnotes/relnotes-al2.md "../../../AL2/latest/relnotes/relnotes-al2.md")
- [AWS Windows AMI version history](../../../ec2/latest/windows-ami-reference/ec2-windows-ami-version-history.md "../../../ec2/latest/windows-ami-reference/ec2-windows-ami-version-history.md")
- [Description of Software Update Services and Windows Server Update Services
  changes in content for 2024](https://support.microsoft.com/en-us/help/894199/description-of-software-update-services-and-windows-server-update-serv-2024 "https://support.microsoft.com/en-us/help/894199/description-of-software-update-services-and-windows-server-update-serv-2024")
