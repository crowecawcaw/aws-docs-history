

# Amazon GameLift Servers AMI versions
<a name="reference-ec2-ami-version-history"></a>

The following table identifies the latest Amazon machine images (AMIs) that Amazon GameLift Servers uses for managed EC2 hosting. As described in [Configuration and vulnerability analysis in Amazon GameLift Servers](vulnerability-analysis-management.md), you must regularly create new Amazon GameLift Servers managed EC2 fleets to deploy the latest AMI version updates. 

**AMIs for use with server SDK for Amazon GameLift Servers 5\+**

Amazon GameLift Servers uses the following AMIs to host game servers that are integrated with server SDK for Amazon GameLift Servers version 5.


| Amazon GameLift Servers image | Architecture | Most recent patch | Base AWS image | 
| --- | --- | --- | --- | 
| Amazon Linux 2023<br />BASE\_AMI\_LINUX\_2023 | x86 | 2026-11-02 | Amazon Linux 2023 AMI 2023.12.20261102.0 x86\_64 HVM kernel-6.1 ([release notes](https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.12.20261102.html)) | 
| Amazon Linux 2<br />BASE\_AMI\_LINUX\_2\_SDK\_5 | x86 | 2026-11-02 | Amazon Linux 2 Kernel 5.10 AMI 2.0.20261102.0 x86\_64 HVM gp2 ([release notes](https://docs.aws.amazon.com/AL2/latest/relnotes/relnotes-20261102.html)) | 
| Windows 2016<br />BASE\_AMI\_WINDOWS\_2016\_SDK\_5 | x86 | 2026-10-28 | Windows\_Server-2016-English-Full-Base-2026.10.14 ([release notes](https://docs.aws.amazon.com/ec2/latest/windows-ami-reference/ec2-windows-ami-version-history.html#amis-2026)) | 
| Amazon Linux 2023<br />BASE\_AMI\_LINUX\_2023\_ARM | ARM64 | 2026-11-02 | Amazon Linux 2023 AMI 2023.12.20261102.0 arm64 HVM kernel-6.1 ([release notes](https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.12.20261102.html)) | 
| Amazon Linux 2<br />BASE\_AMI\_LINUX\_2\_ARM | ARM64 | 2026-11-02 | Amazon Linux 2 LTS Arm64 Kernel 5.10 AMI 2.0.20261102.0 arm64 HVM gp2 ([release notes](https://docs.aws.amazon.com/AL2/latest/relnotes/relnotes-20261102.html)) | 
| Windows 2022<br />BASE\_AMI\_WINDOWS\_2022 | x86 | 2026-10-28 | Windows\_Server-2022-English-Full-Base-2026.10.14 ([release notes](https://docs.aws.amazon.com/ec2/latest/windows-ami-reference/ec2-windows-ami-version-history.html#amis-2026)) | 

**AMIs for use with server SDK for Amazon GameLift Servers 4**

Amazon GameLift Servers uses the following AMIs to host game servers that are integrated with server SDK for Amazon GameLift Servers version 4 or earlier.


| Amazon GameLift Servers image | Architecture | Most recent patch | Base AWS image | 
| --- | --- | --- | --- | 
| Amazon Linux 2<br />BASE\_AMI\_LINUX\_2\_SDK\_4 | x86 | 2026-11-02 | Amazon Linux 2 AMI 2.0.20261102.0 x86\_64 HVM gp2 ([release notes](https://docs.aws.amazon.com/AL2/latest/relnotes/relnotes-20261102.html)) | 
| Amazon Linux 2023<br />BASE\_AMI\_LINUX\_2023\_SDK\_4<br />*Available in the China (Beijing) and China (Ningxia) Regions only.* | x86 | 2026-11-02 | Amazon Linux 2023 AMI 2023.12.20261102.0 x86\_64 HVM kernel-6.1 ([release notes](https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.12.20261102.html)) | 
| Windows 2016<br />BASE\_AMI\_WINDOWS\_2016\_SDK\_4 | x86 | 2026-10-28 | Windows\_Server-2016-English-Full-Base-2026.10.14 ([release notes](https://docs.aws.amazon.com/ec2/latest/windows-ami-reference/ec2-windows-ami-version-history.html#amis-2026)) | 

For more information, see the following resources: 
+ [ Amazon Linux 2023 release notes](https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes.html)
+ [ Amazon Linux 2 release notes](https://docs.aws.amazon.com/AL2/latest/relnotes/relnotes-al2.html)
+ [AWS Windows AMI version history](https://docs.aws.amazon.com/ec2/latest/windows-ami-reference/ec2-windows-ami-version-history.html)
+ [Description of Software Update Services and Windows Server Update Services changes in content for 2024](https://support.microsoft.com/en-us/help/894199/description-of-software-update-services-and-windows-server-update-serv-2024)