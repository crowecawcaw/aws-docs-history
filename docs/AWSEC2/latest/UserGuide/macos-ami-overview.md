

# Amazon EC2 macOS AMIs release notes
<a name="macos-ami-overview"></a>

The following information provides details about the packages included by default in the EC2 macOS AMIs and summarizes the changes for each EC2 macOS AMI release.

For information about how to subscribe to macOS AMI notifications, see [Subscribe to macOS AMI notifications](macos-subscribe-notifications.md).

Mac instances can run one of the following operating systems:
+ macOS Mojave (version 10.14) (x86 Mac instances only)
+ macOS Catalina (version 10.15) (x86 Mac instances only)
+ macOS Big Sur (version 11) (x86 and M1 Mac instances)
+ macOS Monterey (version 12) (x86 and M1 Mac instances)
+ macOS Ventura (version 13) (all Mac instances, M2 and M2 Pro Mac instances support macOS Ventura version 13.2 or later)
+ macOS Sonoma (version 14) (all Mac instances)
+ macOS Sequoia (version 15) (all Mac instances)
**Note**  
M4 and M4 Pro Mac instances support macOS Sequoia version 15.6 or later.

## Approve Local Network Privacy policies for macOS Sequoia
<a name="macos-sequoia-lnp"></a>

macOS Sequoia (version 15) has a new Local Network Privacy feature that impacts users of local IP-based services, including Amazon EC2 Instance Metadata Service (IMDS).

**Important**  
To make sure that you have uninterrupted access to local IP-based services, use the following steps to approve the Local Network Privacy policies.

**To approve Local Network Privacy policies**

1. [Connect to your instance's graphical user interface (GUI)](connect-to-mac-instance.md#mac-instance-vnc).

1. Follow the prompts on the screen to approve the Local Network Privacy policies.

1. After you have approved the policies, create an AMI of your EC2 Mac instance. For more information, see [Create an Amazon EBS-backed AMI](creating-an-ami-ebs.md). 

Any EC2 Mac instances that are launched from the newly created AMI will retain the Local Network Privacy permissions.

## Default packages included in Amazon EC2 macOS AMIs
<a name="macos-ami-default-packages"></a>

The following table describes packages that are included by default in the EC2 macOS AMIs.


| Packages | Release notes | 
| --- | --- | 
| EC2 macOS Init | [https://github.com/aws/ec2-macos-init/tags](https://github.com/aws/ec2-macos-init/tags) | 
| EC2 macOS Utils | [https://github.com/aws/ec2-macos-utils/tags](https://github.com/aws/ec2-macos-utils/tags) | 
| Amazon SSM Agent | [https://github.com/aws/amazon-ssm-agent/releases](https://github.com/aws/amazon-ssm-agent/releases) | 
| AWS Command Line Interface (AWS CLI) version 2 | [https://raw.githubusercontent.com/aws/aws-cli/v2/CHANGELOG.rst](https://raw.githubusercontent.com/aws/aws-cli/v2/CHANGELOG.rst) | 
| Command Line Tools for Xcode | [https://developer.apple.com/documentation/xcode-release-notes](https://developer.apple.com/documentation/xcode-release-notes) | 
| Homebrew | [https://github.com/Homebrew/brew/releases](https://github.com/Homebrew/brew/releases) | 
| EC2 Instance Connect | [https://github.com/aws/aws-ec2-instance-connect-config/releases](https://github.com/aws/aws-ec2-instance-connect-config/releases) | 
| Safari | [https://developer.apple.com/documentation/safari-release-notes](https://developer.apple.com/documentation/safari-release-notes) | 

## Amazon EC2 macOS AMI updates
<a name="macos-ami-change-log"></a>

The following table describes changes included in the EC2 macOS AMI releases. Note that some changes apply to all EC2 macOS AMIs, whereas others apply to only a subset of these AMIs.

### EC2 macOS AMI updates
<a name="monthly-ami-updates"></a>


| Release | Changes | 
| --- | --- | 
| 2026.09.02 |  +  Updated `awscli` to 2.36.36 <br />+  Updated Homebrew to 6.0.20  +  [Security content of macOS Sonoma 14.8.9](https://support.apple.com/en-us/148172) <br />+  Updated Safari to 26.6.1   [Security content of Safari 26.6.1](https://support.apple.com/en-us/148286)    +  [Security content of macOS Tahoe 26.6.2](https://support.apple.com/en-us/148281)   | 
| 2026.08.26 |  +  Updated `awscli` to 2.36.27 <br />+  Updated Homebrew to 6.0.18  +  [Security content of macOS Sonoma 14.8.9](https://support.apple.com/en-us/148172) <br />+  Updated Safari to 26.6.1   [Security content of Safari 26.6.1](https://support.apple.com/en-us/148286)    +  [Security content of macOS Sequoia 15.7.9](https://support.apple.com/en-us/148171) <br />+  Updated Safari to 26.6.1   [Security content of Safari 26.6.1](https://support.apple.com/en-us/148286)    +  [Security content of macOS Tahoe 26.6.1](https://support.apple.com/en-us/148170)   | 
| 2026.08.13 |  +  Updated `awscli` to 2.36.12 <br />+  Updated Homebrew to 6.0.13  +  [Security content of macOS Sonoma 14.8.8](https://support.apple.com/en-us/128072) <br />+  Updated Safari to 26.6   [Security content of Safari 26.6](https://support.apple.com/en-us/128073)    +  [Security content of macOS Sequoia 15.7.8](https://support.apple.com/en-us/128071) <br />+  Updated Safari to 26.6   [Security content of Safari 26.6](https://support.apple.com/en-us/128073)    +  [Security content of macOS Tahoe 26.6](https://support.apple.com/en-us/128067) <br />+  Updated Command Line Tools to 26.6   | 
| 2026.07.29 |  +  [Security content of macOS Tahoe 26.5.2](https://support.apple.com/en-us/127595) <br />+  Updated `awscli` to 2.36.1 <br />+  Updated Homebrew to 6.0.11   | 
| 2026.05.19 |  +  Updated `awscli` to 2.34.46 <br />+  Updated Homebrew to 5.1.11  +  [Security content of macOS Sonoma 14.8.7](https://support.apple.com/en-us/127117) <br />+  Updated Safari to 26.5   [Security content of Safari 26.5](https://support.apple.com/en-us/127121)    +  [Security content of macOS Sequoia 15.7.7](https://support.apple.com/en-us/127116) <br />+  Updated Safari to 26.5   [Security content of Safari 26.5](https://support.apple.com/en-us/127121)    +  [Security content of macOS Tahoe 26.5](https://support.apple.com/en-us/127115) <br />+  Updated Command Line Tools to 26.5   | 
| 2026.04.20 |  +  [Security content of macOS Tahoe 26.4.1](https://support.apple.com/en-us/100100) <br />+  Updated Command Line Tools to 26.4.1 <br />+  Updated `awscli` to 2.34.32 <br />+  Updated Homebrew to 5.1.7   | 
| 2026.04.16 |  +  Updated `awscli` to 2.34.27 <br />+  Updated `ec2-macos-init` to 1.5.15 <br />+  Updated Homebrew to 5.1.5  +  [Security content of macOS Sonoma 14.8.5](https://support.apple.com/en-us/126796) <br />+  Updated Safari to 26.4   [Security content of Safari 26.4](https://support.apple.com/en-us/126800)    +  [Security content of macOS Sequoia 15.7.5](https://support.apple.com/en-us/126795) <br />+  Updated Safari to 26.4   [Security content of Safari 26.4](https://support.apple.com/en-us/126800)    +  [Security content of macOS Tahoe 26.4](https://support.apple.com/en-us/126794) <br />+  Updated Command Line Tools to 26.4   | 
| 2026.03.17 |  +  [What's new in the updates for macOS Tahoe 26](https://support.apple.com/en-us/122868) <br />+  Updated Command Line Tools to 26.3 <br />+  Updated `awscli` to 2.34.10 <br />+  Updated Homebrew to 5.1.0   | 
| 2026.03.03 |  +  Updated `awscli` to 2.33.31 <br />+  Updated Homebrew to 5.0.15  +  [Security content of macOS Sonoma 14.8.4](https://support.apple.com/en-us/126350) <br />+  Updated Safari to 26.3   [Security content of Safari 26.3](https://support.apple.com/en-us/126354)    +  [Security content of macOS Sequoia 15.7.4](https://support.apple.com/en-us/126349) <br />+  Updated Safari to 26.3   [Security content of Safari 26.3](https://support.apple.com/en-us/126354)    +  [Security content of macOS Tahoe 26.3](https://support.apple.com/en-us/126348)   | 
| 2025.12.26 |  +  Updated `awscli` to 2.32.19 <br />+  Updated `amazon-ssm-agent` to 3.3.3270.0 <br />+  Updated Homebrew to 5.0.6  +  [Security content of macOS Sonoma 14.8.3]( https://support.apple.com/en-us/125888) <br />+  Updated Safari to 26.2   [Security content of Safari 26.2](https://support.apple.com/en-us/125892)    +  [Security content of macOS Sequoia 15.7.3](https://support.apple.com/en-us/125887) <br />+  Updated Safari to 26.2   [Security content of Safari 26.2](https://support.apple.com/en-us/125892)   <br />+  Updated Command Line Tools to 26.2  +  [Security content of macOS Tahoe 26.2](https://support.apple.com/en-us/125886) <br />+  Updated Command Line Tools to 26.2   | 
| 2025.12.17 |  +  Updated `awscli` to 2.32.16 <br />+  Updated Homebrew to 5.0.5  +  [Security content of macOS Sonoma 14.8.2](https://support.apple.com/en-us/125636) <br />+  Updated Safari to 26.1   [Security content of Safari 26.1](https://support.apple.com/en-us/125640)    +  [Security content of macOS Sequoia 15.7.2](https://support.apple.com/en-us/125635) <br />+  Updated Safari to 26.1   [Security content of Safari 26.1](https://support.apple.com/en-us/125640)   <br />+  Updated Command Line Tools to 26.1  +  [Security content of macOS Tahoe 26.1](https://support.apple.com/en-us/125634) <br />+  Updated Command Line Tools to 26.1   | 
| 2025.11.18 |  +  Updated `awscli` to 2.31.35 <br />+  Updated `ec2-macos-init` to 1.5.13 <br />+  Updated `ec2-macos-utils` to 1.0.7 <br />+  Updated Homebrew to 5.0.1  +  [Security content of macOS Sonoma 14.8.1](https://support.apple.com/en-us/125330) <br />+  Updated Safari to 26.0.1   [Security content of Safari 26.0.1](https://support.apple.com/en-us/125113)    +  [Security content of macOS Sequoia 15.7.1](https://support.apple.com/en-us/125329) <br />+  Updated Safari to 26.0.1   [Security content of Safari 18.6](https://support.apple.com/en-us/125113)   <br />+  Updated Command Line Tools to 26.0  +  [Security content of macOS Tahoe 26.0.1](https://support.apple.com/en-us/125328) <br />+  Updated Command Line Tools to 26.0   | 
| 2025.09.04 |  +  Updated `awscli` to 2.28.19 <br />+  Updated `ec2-instance-connect` to 2.0.0-5 <br />+  Updated Homebrew to 4.6.7  +  [Security content of macOS Ventura 13.7.8](https://support.apple.com/en-us/124929)  +  [Security content of macOS Sonoma 14.7.8](https://support.apple.com/en-us/124928)  +  [Security content of macOS Sequoia 15.6.1](https://support.apple.com/en-us/124927)   | 
| 2025.08.05 |  +  Updated `awscli` to 2.28.0 <br />+  Updated Homebrew to 4.5.13  +  [Security content of macOS Ventura 13.7.7](https://support.apple.com/en-us/124151) <br />+  Updated Safari to 18.6   [Security content of Safari 18.6](https://support.apple.com/en-us/124152)    +  [Security content of macOS Sonoma 14.7.7](https://support.apple.com/en-us/124150) <br />+  Updated Safari to 18.6   [Security content of Safari 18.6](https://support.apple.com/en-us/124152)    +  [Security content of macOS Sequoia 15.6](https://support.apple.com/en-us/124149) <br />+  Updated AWS ENA Ethernet to 2.0.0   | 
| 2025.06.27 |  +  Updated `awscli` to 2.27.40 <br />+  Updated Homebrew to 4.5.7 <br />+  Migrated x86\_64 images to AWS ENA Ethernet dext  +  [Security content of macOS Ventura 13.7.6](https://support.apple.com/en-us/122718) <br />+  Updated Safari to 18.5   [Security content of Safari 18.5](https://support.apple.com/en-us/122719)    +  [Security content of macOS Sonoma 14.7.6](https://support.apple.com/en-us/122717) <br />+  Updated Safari to 18.5   [ Security content of Safari 18.5](https://support.apple.com/en-us/122719)    +  [Security content of macOS Sequoia 15.5](https://support.apple.com/en-us/122716) <br />+  Updated Command Line Tools to 16.4 <br />+  Updated AWS ENA Ethernet to 1.0.9   | 
| 2025.05.21 |  +  Updated `awscli` to 2.27.7 <br />+  Updated `ec2-macos-init` to 1.5.11 <br />+  Updated `ec2-macos-utils` to 1.0.5 <br />+  Updated Homebrew to 4.5.1  +  [Security content of macOS Ventura 13.7.5](https://support.apple.com/en-us/122375) <br />+  Updated Safari to 18.4   [ Security content of Safari 18.4](https://support.apple.com/en-us/122379)    +  [Security content of macOS Sonoma 14.7.5](https://support.apple.com/en-us/122374) <br />+  Updated Safari to 18.4   [ Security content of Safari 18.4 ](https://support.apple.com/en-us/122379)    +  [Security content of macOS Sequoia 15.4.1](https://support.apple.com/en-us/122400) <br />+  Updated Command Line Tools to 16.3   | 
| 2025.05.05 |  +  Updated `awscli` to 2.27.1 <br />+  Updated `ec2-macos-init` to 1.5.11 <br />+  Updated `ec2-macos-system-monitor` to 1.3.1 <br />+  Updated `ec2-macos-utils` to 1.0.5 <br />+  Updated Homebrew to 4.4.32  +  [Security content of macOS Ventura 13.7.5](https://support.apple.com/en-us/122375) <br />+  Updated Safari to 18.4   [ Security content of Safari 18.4](https://support.apple.com/en-us/122379)    +  [Security content of macOS Sonoma 14.7.5](https://support.apple.com/en-us/122374) <br />+  Updated Safari to 18.4   [ Security content of Safari 18.4 ](https://support.apple.com/en-us/122379)    +  [Security content of macOS Sequoia 15.4.1](https://support.apple.com/en-us/122400)   | 
| 2025.03.18 |  +  Updated `awscli` to 2.24.2 <br />+  Updated Homebrew to 4.4.20  +  [Security content of macOS Sequoia 15.3.1](https://support.apple.com/en-us/120283)  +  [Security content of macOS Sonoma 14.7.4](https://support.apple.com/en-us/109035) <br />+  Updated Safari to 18.3  +  [Security content of macOS Ventura 13.7.4](https://support.apple.com/en-us/106337) <br />+  Updated Safari to 18.3   | 
| 2025.01.24 |  +  Updated `awscli` to 2.22.33 <br />+  Updated Homebrew to 4.4.15  +  [Security content of macOS Sequoia 15.2](https://support.apple.com/en-us/121839) <br />+  Updated Command Line Tools to 16.2  +  [Security content of macOS Sonoma 14.7.2](https://support.apple.com/en-us/121840) <br />+  Updated Safari to 18.2 <br />+  Updated Command Line Tools to 16.2  +  [Security content of macOS Ventura 13.7.2](https://support.apple.com/en-us/121842) <br />+  Updated Safari to 18.2   | 
| 2024.12.20 |  +  Updated Homebrew to 4.4.8 <br />+  Updated `aws-cli` to 2.22.5 <br />+  Updated `amazon-ssm-agent` to 3.3.987.0  +  [Security content of macOS Sequoia 15.1.1](https://support.apple.com/en-us/121753)  +  [Security content of macOS Sonoma 14.7.1](https://support.apple.com/en-us/121570) <br />+  Updated Safari to 18.1.1  +  [Security content of macOS Ventura 13.7.1](https://support.apple.com/en-us/121568) <br />+  Updated Safari to 18.1.1   | 
| 2024.10.28 |  +  Updated Homebrew to 4.4.2 <br />+  Updated `aws-cli` to 2.18.13 <br />+  Updated `amazon-ssm-agent` to 3.3.987.0 <br />+  Updated `ec2-macos-init` to 1.5.10 <br />+  Updated `ec2-macos-utils` to 1.0.4  +  [Security content of macOS Sequoia 15](https://support.apple.com/en-us/121238)  +  [Security content of macOS Sonoma 14.7](https://support.apple.com/en-us/121247). <br />+  Updated Command Line Tools to 16.0 <br />+  Updated Safari to 18.0.1   [Security content of Safari 18](https://support.apple.com/en-us/121241)    +  [Security content of macOS Ventura 13.7](https://support.apple.com/en-us/121234) <br />+  Updated Safari to 18.0.1   [Security content of Safari 18](https://support.apple.com/en-us/121241)     | 
| 2024.08.20 |  +  Updated Homebrew to 4.3.14 <br />+  Updated `aws-cli` to 2.17.29  +  No published CVE entries.  +  No published CVE entries. <br />+  Updated Safari to 17.6   [Security content of Safari 17.6](https://support.apple.com/en-us/120913)    +  [Security content of macOS Monterey 12.7.6](https://support.apple.com/en-us/120910) <br />+  Updated Safari to 17.6   [Security content of Safari 17.6](https://support.apple.com/en-us/120913)     | 
| 2024.06.07 |  +  Updated Homebrew to 4.3.1-1 <br />+  Updated `aws-cli` to 2.15.56 <br />+  Updated `amazon-ssm-agent` to 3.3.380.0-1  +  [Security content of macOS Sonoma 14.5](https://support.apple.com/en-us/120903)  +  [Security content of macOS Ventura 13.6.7](https://support.apple.com/en-us/120900) <br />+  Updated Safari to 17.5   [Security content of Safari 17.5](https://support.apple.com/en-us/120896)    +  [Security content of macOS Monterey 12.7.5](https://support.apple.com/en-us/120896) <br />+  Updated Safari to 17.5   [Security content of Safari 17.5](https://support.apple.com/en-us/120896)     | 
| 2024.04.12 |  +  Updated Homebrew to 4.2.16-1 <br />+  Updated `aws-cli` to 2.15.36  +  [Security content of macOS Sonoma 14.4.1](https://support.apple.com/en-us/120889)  +  [Security content of macOS Ventura 13.6.6](https://support.apple.com/en-us/120891) <br />+  Updated Safari to 17.4.1   [Security content of Safari 17.4.1](https://support.apple.com/en-us/120888)    +  Updated Safari to 17.4.1   [Security content of Safari 17.4.1](https://support.apple.com/en-us/120888)     | 