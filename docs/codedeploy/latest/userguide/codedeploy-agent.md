

# Working with the CodeDeploy agent
<a name="codedeploy-agent"></a>

**Version 2.0.x rollout status**  
Version 2.0.x of the CodeDeploy agent is being rolled out across AWS Regions and might not be available in all Regions yet. Version 2.0.0 is an opt-in upgrade. In order to upgrade to version 2.0.x from any older revisions, see [Install the CodeDeploy agent](codedeploy-agent-operations-install.md).

 The AWS CodeDeploy agent is a software package that, when installed and configured on an instance, makes it possible for that instance to be used in CodeDeploy deployments.

AWS actively supports the latest minor version of the CodeDeploy agent. For the latest released version, see [Version history of the CodeDeploy agent](#codedeploy-agent-version-history).

**Note**  
 The CodeDeploy agent is required only if you deploy to an EC2/On-Premises compute platform. The agent is not required for deployments that use the Amazon ECS or AWS Lambda compute platform. 

A configuration file is placed on the instance when the agent is installed. This file is used to specify how the agent works. This configuration file specifies directory paths and other settings for AWS CodeDeploy to use as it interacts with the instance. You can change some of the configuration options in the file. For information about working with the CodeDeploy agent configuration file, see [CodeDeploy agent configuration reference](reference-agent-configuration.md).

For more information about working with the CodeDeploy agent, such as steps for installing, updating, and verifying versions, see [Managing CodeDeploy agent operations](codedeploy-agent-operations.md).

**Topics**
+ [Operating systems supported by the CodeDeploy agent](#codedeploy-agent-supported-operating-systems)
+ [Communication protocol and port for the CodeDeploy agent](#codedeploy-agent-outbound-port)
+ [Version history of the CodeDeploy agent](#codedeploy-agent-version-history)
+ [Managing the CodeDeploy process](#codedeploy-agent-processes)
+ [Application revision and log file cleanup](#codedeploy-agent-revisions-logs-cleanup)
+ [Files installed by the CodeDeploy agent](#codedeploy-agent-install-files)
+ [Managing CodeDeploy agent operations](codedeploy-agent-operations.md)

## Operating systems supported by the CodeDeploy agent
<a name="codedeploy-agent-supported-operating-systems"></a>

### Supported Amazon EC2 AMI operating systems
<a name="codedeploy-agent-supported-operating-systems-ec2"></a>

The CodeDeploy agent has been tested on the following Amazon EC2 AMI operating systems:
+ Amazon Linux 2023 (x86\_64, aarch64)
+ Amazon Linux 2 (x86\_64, aarch64)
+ Red Hat Enterprise Linux (RHEL) 8, 9, 10 (x86\_64, aarch64)
+ Oracle Linux 8, 9, 10 (x86\_64, aarch64)
+ Rocky Linux 9, 10 (x86\_64, aarch64)
+ CentOS Stream 9, 10 (x86\_64, aarch64)
+ SLES 15 (x86\_64, aarch64)
+ Debian 11, 12, 13 (x86\_64, aarch64)
+ Ubuntu Server 16.04 LTS, 18.04 LTS, 20.04 LTS, 22.04 LTS, 24.04 LTS, 25.04, 26.04 LTS (x86\_64, aarch64)
+ Windows Server 2016, 2019, 2022, 2025 (x86\_64)

**Note**  
The following platforms have been tested on the CodeDeploy agent version 2.0.x and later only: Windows Server 2025, RHEL 10, Oracle Linux 8, 9, 10, Rocky Linux 9, 10, CentOS Stream 9, 10, SLES 15, Debian 11, 12, 13, and Ubuntu Server 24.04, 25.04, 26.04.

The CodeDeploy agent is available as open source for you to adapt to your needs. It can be used with other Amazon EC2 AMI operating systems. For more information, go to the [CodeDeploy agent](https://github.com/aws/aws-codedeploy-agent) repository in GitHub.

### Supported on-premises operating systems
<a name="codedeploy-agent-supported-operating-systems-on-premises"></a>

The CodeDeploy agent has been tested on the following on-premises operating systems:
+ Windows Server 2016, 2019, 2022, 2025 (x86\_64)
+ Red Hat Enterprise Linux (RHEL) 8, 9, 10 (x86\_64, aarch64)
+ Oracle Linux 8, 9, 10 (x86\_64, aarch64)
+ Rocky Linux 9, 10 (x86\_64, aarch64)
+ CentOS Stream 9, 10 (x86\_64, aarch64)
+ SLES 15 (x86\_64, aarch64)
+ Debian 11, 12, 13 (x86\_64, aarch64)
+ Ubuntu Server 16.04 LTS, 18.04 LTS, 20.04 LTS, 22.04 LTS, 24.04 LTS, 25.04, 26.04 LTS (x86\_64, aarch64)

**Note**  
The following platforms have been tested on the CodeDeploy agent version 2.0.x and later only: Windows Server 2025, RHEL 10, Oracle Linux 8, 9, 10, Rocky Linux 9, 10, CentOS Stream 9, 10, SLES 15, Debian 11, 12, 13, and Ubuntu Server 24.04, 25.04, 26.04.

The CodeDeploy agent is available as open source for you to adapt to your needs. It can be used with other on-premises instance operating systems. For more information, go to the [CodeDeploy agent](https://github.com/aws/aws-codedeploy-agent) repository in GitHub.

## Communication protocol and port for the CodeDeploy agent
<a name="codedeploy-agent-outbound-port"></a>

The CodeDeploy agent communicates outbound using HTTPS over port 443.

When the CodeDeploy agent runs on an EC2 instance, it will use the [EC2 metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html) endpoint to retrieve instance related information. Find out more about [limiting and granting instance metadata service access](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html#instance-metadata-limiting-access).

## Version history of the CodeDeploy agent
<a name="codedeploy-agent-version-history"></a>

Your instances must be running a supported version of the CodeDeploy agent. The current minimum supported version is 1.8.x.

**Note**  
We recommend using the latest version of the CodeDeploy agent. If you're having issues, update to the latest version before contacting AWS Support. For upgrade information, see [Update the CodeDeploy agent](codedeploy-agent-operations-update.md).

**Version 2.0.x rollout status**  
Version 2.0.x of the CodeDeploy agent is being rolled out across AWS Regions and might not be available in all Regions yet. Version 2.0.0 is an opt-in upgrade. In order to upgrade to version 2.0.x from any older revisions, see [Install the CodeDeploy agent](codedeploy-agent-operations-install.md).

The following table lists all releases of the CodeDeploy agent and the features and enhancements included with each version.


| Version | Release date | Details | 
| --- | --- | --- | 
| 2.0.1 | August 24, 2026 | **Fixed**: On Windows, AppSpec file paths that begin with a backslash (`\`) or with more than one separator (for example, `//my-folder`) are now resolved inside the revision, not at the root of the drive.<br />For examples of supported `source` values, see [AppSpec 'files' section (EC2/On-Premises deployments only)](reference-appspec-file-structure-files.md). | 
| 2.0.0 | July 15, 2026 | **Changed**: The CodeDeploy agent is now Rust-based and ships as a single self-contained native binary. The Ruby runtime dependency has been dropped. Ruby is no longer required to install or run the agent. The agent is behavior-compatible with version 1.8.x by default; existing configuration files, AppSpec handling, lifecycle-hook semantics, on-disk layout, and deployment outcomes are unchanged unless noted below.<br />**Added**: Expanded operating-system support, including Windows Server 2025, RHEL 10, and Ubuntu Server 26.04, as well as additional Linux distributions and ARM (aarch64) variants. For the full list of platforms tested with this version, see [Operating systems supported by the CodeDeploy agent](#codedeploy-agent-supported-operating-systems).<br />**Added**: A `codedeploy-agent update` command for on-demand agent self-update.<br />**Added**: A local command port. This is an optional TCP management interface that listens only on the loopback address (127.0.0.1) for querying agent status and injecting commands locally. It is disabled by default and is enabled with `enable_command_port`.<br />**Changed**: The local deployment command is now `codedeploy-agent deploy-local`. The `codedeploy-local` command remains available for backward compatibility. All command options are preserved, and local paths, Amazon S3 (`s3://`), and GitHub bundle sources are still supported.<br />**Changed**: On Linux, the agent is managed by a native systemd unit (`codedeploy-agent.service`); the SysV init.d script is no longer installed. Use `systemctl` to manage the agent.<br />**Changed (security)**: TLS certificate verification is always enabled, and core dumps are disabled by default.<br />**Added**: Optional hardening settings that you can enable to meet your own security requirements. Each setting is turned off by default, and you enable the ones you want individually. You can reject bundles that contain symbolic links, path traversal, or unsafe permissions; restrict the environment of lifecycle event hooks; and restrict the permissions of agent directories and log files. For the full list, see [CodeDeploy agent configuration reference](reference-agent-configuration.md).<br />**Changed**: The command-line install script is now written in Bash (previously Ruby). It requires either `curl` or `wget`.<br />**Changed**: The install script for version 2.0.x is published under the `latestv2/` prefix in the regional `aws-codedeploy-{{region-identifier}}` buckets. The `latest/` prefix continues to serve the version 1.8.x install script.<br />**Changed**: AWS now publishes version 2.0.x as the `AWSCodeDeployAgentV2` Systems Manager Distributor package. The `AWSCodeDeployAgent` package continues to serve version 1.8.x.<br />**Removed**: The `ssl_verify_peer` configuration setting and the Ruby ProcessManager configuration keys.<br />**Important**: No automatic update path currently exists from version 1.8.x to 2.0.0. To upgrade to 2.0.0, install it with the `AWSCodeDeployAgentV2` Systems Manager Distributor package or run the regional `latestv2/install` script manually. For instructions, see [Install the CodeDeploy agent](codedeploy-agent-operations-install.md). | 
| 1.8.1 | February 3, 2026 | **Fixed**: S3 endpoint bugfix.<br />**Added**: Sectigo CA certificate to Windows CA list. | 
| 1.8.0 | July 31, 2025 | **Changed**: Upgraded the bundled Ruby to 3.2 in the CodeDeploy agent for Windows. | 
| 1.7.1 | November 14, 2024 | **Changed**: Updated dependencies for security patches. | 
| 1.7.0 | March 6, 2024 | **Added**: A `:disable_imds_v1:` configuration setting to the CodeDeploy agent configuration file. Use this setting to disable the fallback to IMDSv1 when IMDSv2 errors occur. Defaults to `false` (enable the fallback). For more information, see [CodeDeploy agent configuration reference](https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-agent-configuration.html).<br />**Added**: Support for the Red Hat Enterprise Linux 9 (RHEL 9) operating system.<br />**Added**: Support for Ruby versions 3.1 and 3.2 on Ubuntu Server.<br />**Fixed**: The CodeDeploy agent now generates a user-friendly error if the CodeDeploy agent configuration file fails to load.<br />**Changed**: Upgraded Ruby to 2.7.8-1 in the CodeDeploy agent for Windows. | 
| 1.6.0 | March 30, 2023 | **Added**: Support for Ruby 3.1, 3.2.<br />**Added**: Support for Amazon Linux 2023.<br />**Added**: Support for Windows Server 2022.<br />**Changed**: The default setting of `verbose` is now `false` for Windows Server instances. To continue to print debug messages in log files on Windows, you must set `verbose` to `true`.<br />**Removed**: Support for Windows Server 2016 and Windows Server 2012 R2.<br />**Removed**: Support for Amazon Linux 2018.03.x. | 
| 1.5.0 | March 3, 2023 | **Added**: Support for Ruby 3.<br />**Added**: Support for Ubuntu 22.04.<br />**Fixed**: An issue where restarting the CodeDeploy agent soon after startup would lead to the agent hanging.<br />**Changed**: The CodeDeploy agent now fails a host deployment on agent startup if the agent service restarts unexpectedly while running a hook script. This fix lets you avoid waiting for the 70-minute timeout period before retrying a deployment.<br />**Deprecation notice**: CodeDeploy agent 1.5.0 is the last release to support Windows Server 2016 and Windows Server 2012 R2.<br />**Removed:** Support for the CodeDeploy agent on Ubuntu 14.04 LTS, Windows Server 2008 R2, and Windows Server 2008 R2 32-bit. | 
| 1.4.1 | December 6, 2022 | **Fixed**: Security vulnerability related to logging.<br />**Enhancement**: Improved logging when polling for the host command. | 
| 1.4.0 | August 31, 2022 | **Added**: Support for Red Hat Enterprise Linux 8. <br />**Added**: Support for long file paths on the CodeDeploy agent for Windows. To enable long file paths, you'll need to set the appropriate Windows registry key and then restart your agent. For more information, see [Long file paths cause "No such file or directory" errors](troubleshooting-deployments.md#troubleshooting-long-file-paths).<br />**Fixed**: An issue with the unzip operation when the disk was full. The CodeDeploy agent now detects the unzip's [exit code 50](https://linux.die.net/man/1/unzip) indicating a full disk, removes partially extracted files, and raises an exception to post a failure to the CodeDeploy server. The error message is visible as a lifecycle event error message, and the host-level deployment will stop without being stuck or timing-out.<br />**Fixed**: An issue that would cause the agent to fail.<br />**Fixed**: An issue where hooks would time out during an edge-case race condition. Hooks with no scripts will now continue and no longer cause failures or timeouts. <br />**Changed**: The `update` script from the CodeDeploy agent's `bin` directory was removed because it is no longer used.<br />**Changed**: The CodeDeploy agent for Windows Server now bundles Ruby 2.7.<br />**Changed**: New environment variables were added, to be used by hook scripts depending on the source of the deployment bundle (Amazon S3 or GitHub). <br />For more information, see [Environment variable availability for hooks](reference-appspec-file-structure-hooks.md#reference-appspec-file-structure-environment-variable-availability). **Deprecation notice**: CodeDeploy agent 1.4.0 is the last release that will include installers for 32-bit Windows Server. <br />**Deprecation notice**: CodeDeploy agent 1.4.0 is the last release that will support Windows Server 2008 R2. <br />**Removed**: Support for the CodeDeploy agent on the following Amazon EC2 AMIs: Amazon Linux 2014.09, 2016.03, 2016.09, and 2017.03.  | 
| 1.3.2 | May 6, 2021 |  CodeDeploy agent 1.3.2 addresses [CVE-2018-1000201](https://nvd.nist.gov/vuln/detail/CVE-2018-1000201) which affects Windows hosts running the agent. The CVE cites ruby-ffi, which is a dependency of the CodeDeploy agent. If your agent was installed with Amazon EC2 Systems Manager (SSM) and is set to update automatically, no action is required. Otherwise, action is required to manually update the agent. To upgrade the agent follow the instructions in [Update the CodeDeploy agent on Windows Server](https://docs.aws.amazon.com/codedeploy/latest/userguide/codedeploy-agent-operations-update-windows.html). <br />**Fixed**: An issue when installing the CodeDeploy agent on Ubuntu 20.04 and later.<br />**Fixed**: An intermittent issue that occurred when extracting compressed files because relative paths weren't being handled correctly.<br />**Added**: Support for [AWS PrivateLink and VPC endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/endpoint-services-overview.html) for Windows instances.<br />**Added**: AppSpec file improvements, as described below.+  You can now specify a custom filename for the AppSpec file when creating a local deployment. For more information, see [Create a local deployment](deployments-local.md#deployments-local-deploy). <br />+  The AppSpec file can now have a `.yaml` file extension. <br />+  You can now overwrite deployed files using a new, optional `file_exists_behavior` setting in the AppSpec file. For more information, see [AppSpec 'files' section (EC2/On-Premises deployments only)](reference-appspec-file-structure-files.md). <br />**Upgraded**: CodeDeploy now uses the AWS SDK for Ruby 3.0. | 
| 1.3.1 | December 22, 2020 | **Fixed**: 1.3.0 issue that prevented on-premises instances from starting. | 
| 1.3.0 | November 10, 2020 |  This version is deprecated. **Fixed**: Removed an expired certificate that was no longer used.<br />**Fixed**: Removed the prompt message from the agent uninstall script used by AWS Systems Manager, making it easier to downgrade a host or fleet to a previous version of the agent. | 
| 1.2.1 | September 23, 2020 | **Changed**: Upgraded AWS SDK for Ruby dependency from v2 to v3.<br />**Added**: Support for IMDSv2. Includes a silent fallback to IMDSv1 if IMDSv2 http requests fail.<br />**Changed**: Updated Rake and Rubyzip dependencies for security patches.<br />**Fixed**: Ensure that an empty PID file will return a status of `No CodeDeploy Agent Running` and clean up the PID file on agent start. | 
| 1.1.2 | August 4, 2020 | **Added**: Support for Ubuntu Server 19.10 and 20.04.<br />**Note**: : Version 19.10 reached its end-of-life date and is no longer supported by Ubuntu or CodeDeploy.<br />**Added**: Memory efficiency improvements for Linux and Ubuntu to release reserved memory more timely.<br />**Added**: Compatibility with Windows Server "silent-cleanup" which was causing the agent to be unresponsive in some cases.<br />**Added**: Ignore non-empty directories during cleanup to avoid failures on deployment.<br />**Added**: Support for AWS Local Zone in Los Angeles (LA).<br />**Added**: Extract AZ from instance metadata to provide compatibility for AWS Local Zones.<br />**Added**: Users can now provide their archive in subdirectories and aren't required to store it in the root directory.<br />**Added**: Detected an issue with Rubyzip that could result in memory leaks. Updated the unzip command to first attempt to use a system-installed unzip utility before using Rubyzip.<br />**Added**: `:enable_auth_policy:` as an agent configuration setting.<br />**Changed**: Unzip warnings are now ignored so deployments will continue. | 
| 1.1.0 | June 30, 2020 | **Changed**: Versioning of the CodeDeploy agent now follows the Ruby standard versioning convention.<br />**Added**: New parameter to the install and update command to allow installation of specific agent version from the command line.<br />**Removed**: Removed the CodeDeploy agent Auto Updater for Linux and Ubuntu. To configure automatic updates of the CodeDeploy agent, see [Install the CodeDeploy agent using AWS Systems Manager](https://docs.aws.amazon.com/codedeploy/latest/userguide/codedeploy-agent-operations-install-ssm.html). | 
| 1.0.1.1597 | November 15, 2018 | **Enhancement**: CodeDeploy supports Ubuntu 18.04.<br />**Enhancement**: CodeDeploy supports Ruby 2.5.<br />**Enhancement**: CodeDeploy supports FIPS endpoints. For more information about FIPS endpoints, see [FIPS 140-2 overview](https://aws.amazon.com/compliance/fips/). For endpoints that can be used with CodeBuild, see [CodeDeploy Regions and endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#codedeploy_region). | 
| 1.0.1.1518 | June 12, 2018 | **Enhancement**: Fixed an issue that caused an error when the CodeDeploy agent is closed while it is accepting poll requests.<br />**Enhancement**: Added a deployment tracking feature that prevents the CodeDeploy agent from being closed when a deployment is in progress.<br />**Enhancement**: Improved performance when deleting files. | 
| 1.0.1.1458 | March 6, 2018 | **Note**: This version is no longer supported. If you use this version, your deployments might fail.<br />**Enhancement**: Improved certificate validations to support more trusted authorities.<br />**Enhancement**: Fixed an issue that caused the local CLI to fail during a deployment that includes a BeforeInstall lifecycle event.<br />**Enhancement**: Fixed an issue that might cause an active deployment to fail when the CodeDeploy agent is updated. | 
| 1.0.1.1352 | November 16, 2017 | **Note**: This version is no longer supported. If you use this version, your deployments might fail.<br />**Feature**: Introduced a new feature for testing and debugging an EC2/On-Premises deployment on a local machine or instance where the CodeDeploy agent is installed. | 
| 1.0.1.1106 | May 16, 2017 | **Note**: This version is no longer supported. If you use this version, your deployments might fail.<br />**Feature**: Introduced new support for handling content in a target location that wasn't part of the application revision from the most recent successful deployment. Deployments options for existing content now include retaining the content, overwriting the content, or failing the deployment. <br />**Enhancement**: Made the CodeDeploy agent compatible with version 2.9.2 of the AWS SDK for Ruby (aws-sdk-core 2.9.2). | 
| 1.0.1.1095 | March 29, 2017 | **Note**: This version is no longer supported. If you use this version, your deployments might fail.<br />**Enhancement**: Introduced support for the CodeDeploy agent in the China (Beijing) Region.<br />**Enhancement**: Enabled Puppet to run on Windows Server instances when invoked by a lifecycle event hook.<br />**Enhancement**: Improved the handling of `untar` operations. | 
| 1.0.1.1067 | January 6, 2017 | **Note**: This version is no longer supported. If you use this version, your deployments might fail.<br />**Enhancement**: Revised many error messages to include more specific causes for deployment failures.<br />**Enhancement**: Fixed an issue that prevented the CodeDeploy agent from identifying the correct application revision to deploy during some deployments.<br />**Enhancement**: Reverted the usage of `pushd` and `popd` before and after the `untar` operation. | 
| 1.0.1.1045 | November 21, 2016 | **Note**: This version is no longer supported. If you use this version, your deployments might fail.<br />**Enhancement**: Made the CodeDeploy agent compatible with version 2.6.11 of the AWS SDK for Ruby (aws-sdk-core 2.6.11).  | 
| 1.0.1.1037 | October 19, 2016 | **Note**: This version is no longer supported. If you use this version, your deployments might fail.<br />The CodeDeploy agent for Amazon Linux, RHEL, and Ubuntu Server instances has been updated with the following change. For Windows Server instances, the latest version remains 1.0.1.998.<br />**Enhancement**: The agent can now determine which version of Ruby is installed on an instance so it can invoke the `codedeploy-agent` script using that version. | 
| 1.0.1.1011.1 | August 17, 2016 | **Note**: This version is no longer supported. If you use this version, your deployments might fail.<br />**Enhancement**: Removed the changes introduced by version 1.0.1.1011 due to issues with shell support. This version of the agent is functionally equivalent to version 1.0.1.998 released on July 11, 2016. | 
| 1.0.1.1011 | August 15, 2016 | **Note**: This version is no longer supported. If you use this version, your deployments might fail.<br />The CodeDeploy agent for Amazon Linux, RHEL, and Ubuntu Server instances has been updated with the following changes. For Windows Server instances, the latest version remains 1.0.1.998.<br />**Feature**: Added support for invoking the CodeDeploy agent using the bash shell on operating systems where the systemd init system is in use.Enhancement: Enabled support for all versions of Ruby 2.x in the CodeDeploy agent and the CodeDeploy agent updater. Updated CodeDeploy agents are no longer dependent on Ruby 2.0 only. (Ruby 2.0 is still required for deb and rpm versions of the CodeDeploy agent installer.) | 
| 1.0.1.998 | July 11, 2016 | **Note**: This version is no longer supported. If you use this version, your deployments might fail.<br />**Enhancement**: Fixed support for running the CodeDeploy agent with user profiles other than *root*. The variable named `USER` is replaced by `CODEDEPLOY_USER` to avoid conflicts with environmental variables. | 
| 1.0.1.966 | June 16, 2016 | **Note**: This version is no longer supported. If you use this version, your deployments might fail.<br />**Feature**: Introduced support for running the CodeDeploy agent with user profiles other than *root*.<br />**Enhancement**: Fixed support for specifying the number of application revisions you want the CodeDeploy agent to archive for a deployment group.<br />**Enhancement**: Made the CodeDeploy agent compatible with version 2.3 of the AWS SDK for Ruby (aws-sdk-core 2.3). <br />**Enhancement**: Fixed issues with UTF-8 encoding during deployments.<br />**Enhancement**: Improved accuracy when identifying process names. | 
| 1.0.1.950 | March 24, 2016 | **Note**: This version is no longer supported. If you use this version, your deployments might fail.<br />**Feature**: Added installation proxy support.<br />**Enhancement**: Updated the installation script to not download the CodeDeploy agent if the latest version is already installed. | 
| 1.0.1.934 | February 11, 2016 | **Note**: This version is no longer supported. If you use this version, your deployments might fail.<br />**Feature**: Introduced support for specifying the number of application revisions you want the CodeDeploy agent to archive for a deployment group.  | 
| 1.0.1.880 | January 11, 2016 | **Note**: This version is no longer supported and might cause deployments to fail.<br />**Enhancement**: Made the CodeDeploy agent compatible with version 2.2 of the AWS SDK for Ruby (aws-sdk-core 2.2). Version 2.1.2 is still supported. | 
| 1.0.1.854 | November 17, 2015 | **Note**: This version is no longer supported. If you use this version, your deployments might fail.<br />**Feature**: Introduced support for the SHA-256 hash algorithm. <br />**Feature**: Introduced version tracking support in `.version` files.<br />**Feature**: Made the deployment group ID available through the use of an environment variable.<br />**Enhancement**: Added support for monitoring CodeDeploy agent logs using [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatchLogs.html). | 

For related information, see the following:
+ [Determine the version of the CodeDeploy agent](codedeploy-agent-operations-version.md)
+ [Install the CodeDeploy agent](codedeploy-agent-operations-install.md)

For a history of CodeDeploy agent versions, see the [Release repository on GitHub](https://github.com/aws/aws-codedeploy-agent/releases).

## Managing the CodeDeploy process
<a name="codedeploy-agent-processes"></a>

The CodeDeploy agent uses [systemd](https://systemd.io/) to manage the agent process on all supported Linux distributions.

For version 2.0.x and later, the agent ships a native systemd unit (`codedeploy-agent.service`) only. There is no `/etc/init.d/codedeploy-agent` script. Use `systemctl` to manage the agent, or invoke the binary directly with `start`, `stop`, `restart`, or `status` subcommands.

For version 1.8.x and earlier, both the rpm and deb distributions ship with startup scripts at `/etc/init.d/codedeploy-agent`. On systems that support systemd, using the `service` command may inadvertently run the init.d scripts instead of allowing systemd to manage the process. Use `systemctl` for agent operations to avoid this issue.

To manage the CodeDeploy agent, use the `systemctl` utility:

```
sudo systemctl start codedeploy-agent
sudo systemctl stop codedeploy-agent
sudo systemctl restart codedeploy-agent
sudo systemctl status codedeploy-agent
```

## Application revision and log file cleanup
<a name="codedeploy-agent-revisions-logs-cleanup"></a>

The CodeDeploy agent archives revisions and log files on instances. The CodeDeploy agent cleans up these artifacts to conserve disk space.

**Application revision deployment logs**: You can use the **:max\_revisions:** option in the agent configuration file to specify the number of application revisions to archive by entering any positive integer. CodeDeploy also archives the log files for those revisions. All others are deleted, with the exception of the log file of the last successful deployment. That log file is always retained, even if the number of failed deployments exceeds the number of retained revisions. If no value is specified, CodeDeploy retains the five most recent revisions in addition to the currently deployed revision. 

**CodeDeploy logs**: For Amazon Linux, Ubuntu Server, and RHEL instances, the CodeDeploy agent rotates the log files under the `/var/log/aws/codedeploy-agent` folder. The log file is rotated at 00:00:00 (instance time) daily, or when the file reaches 64 MB, whichever comes first. If a second rotation occurs on the same day, the agent appends a numeric suffix (for example, `codedeploy-agent.20260715.1.log`). The agent deletes log files after seven days. The naming pattern for rotated log files is `codedeploy-agent.{{YYYYMMDD}}.log`.

## Files installed by the CodeDeploy agent
<a name="codedeploy-agent-install-files"></a>

The CodeDeploy agent stores revisions, deployment history, and deployment scripts in its root directory on an instance. The default name and location of this directory is:

`'/opt/codedeploy-agent/deployment-root'` for Amazon Linux, Ubuntu Server, and RHEL instances.

`'C:\ProgramData\Amazon\CodeDeploy'` for Windows Server instances. 

You can use the **root\_dir** setting in the CodeDeploy agent configuration file to configure the directory's name and location. For more information, see [CodeDeploy agent configuration reference](reference-agent-configuration.md).

The following is an example of the file and directory structure under the root directory. The structure assumes there are N number of deployment groups, and each deployment group contains N number of deployments. 

```
|--deployment-root/
|-- deployment group 1 ID 
|    |-- deployment 1 ID 
|    |    |-- Contents and logs of the deployment's revision
|    |-- deployment 2 ID
|    |    |-- Contents and logs of the deployment's revision
|    |-- deployment N ID
|    |    |-- Contents and logs of the deployment's revision
|-- deployment group 2 ID
|    |-- deployment 1 ID
|    |    |-- bundle.tar
|    |    |-- deployment-archive
|    |    |    | -- contents of the deployment's revision
|    |    |-- logs
|    |    |    | -- scripts.log     
|    |-- deployment 2 ID
|    |    |-- bundle.tar
|    |    |-- deployment-archive
|    |    |    | -- contents of the deployment's revision
|    |    |-- logs
|    |    |    | -- scripts.log     
|    |-- deployment N ID
|    |    |-- bundle.tar
|    |    |-- deployment-archive
|    |    |    | -- contents of the deployment's revision
|    |    |-- logs
|    |    |    | -- scripts.log     
|-- deployment group N ID
|    |-- deployment 1 ID
|    |    |-- Contents and logs of the deployment's revision
|    |-- deployment 2 ID
|    |    |-- Contents and logs of the deployment's revision
|    |-- deployment N ID
|    |    |-- Contents and logs of the deployment's revision
|-- deployment-instructions
|    |-- [deployment group 1 ID]_cleanup
|    |-- [deployment group 2 ID]_cleanup
|    |-- [deployment group N ID]_cleanup
|    |-- [deployment group 1 ID]_install.json
|    |-- [deployment group 2 ID]_install.json
|    |-- [deployment group N ID]_install.json
|    |-- [deployment group 1 ID]_last_successful_install
|    |-- [deployment group 2 ID]_last_successful_install
|    |-- [deployment group N ID]_last_successful_install
|    |-- [deployment group 1 ID]_most_recent_install
|    |-- [deployment group 2 ID]_most_recent_install
|    |-- [deployment group N ID]_most_recent_install
|-- deployment-logs
|    |-- codedeploy-agent-deployments.log
```


+  **Deployment Group ID** folders represent each of your deployment groups. A deployment group directory's name is its ID (for example, `acde1916-9099-7caf-fd21-012345abcdef`). Each deployment group directory contains one subdirectory for each attempted deployment in that deployment group. 

   You can use the [batch-get-deployments](https://docs.aws.amazon.com/cli/latest/reference/deploy/batch-get-deployments.html) command to find a deployment group ID.
+  **Deployment ID** folders represent each deployment in a deployment group. Each deployment directory's name is its ID. Each folder contains:
  +  **bundle.tar**, a compressed file with the contents of the deployment's revision. Use a zip decompression utility if you want to view the revision.
  +  **deployment-archive**, a directory that contains the contents of the deployment's revision. 
  +  **logs**, a directory that contains a `scripts.log` file. This file lists the output of all scripts specified in the deployment's AppSpec file. 

   If you want to find the folder for a deployment but don't know its deployment ID or deployment group ID, you can use the [AWS CodeDeploy console](https://console.aws.amazon.com/codedeploy) or the AWS CLI to find them. For more information, see [View CodeDeploy deployment details](deployments-view-details.md). 

   The default maximum number of deployments that can be archived in a deployment group is five. When that number is reached, future deployments are archived and the oldest archive is deleted. You can use the **max\_revisions** setting in the CodeDeploy agent configuration file to change the default. For more information, see [CodeDeploy agent configuration reference](reference-agent-configuration.md). 
**Note**  
 If you want to recover hard disk space used by archived deployments, update the **max\_revisions** setting to a low number, such as 1 or 2. The next deployment deletes archived deployments so that the number is equal to the number you specified. 
+  **deployment-instructions** contains four text files for each deployment group: 
  + **[Deployment Group ID]-cleanup**, a text file with an undo version of each command that is run during a deployment. An example file name is `acde1916-9099-7caf-fd21-012345abcdef-cleanup`. 
  + **[Deployment Group ID]-install.json**, a JSON file created during the most recent deployment. It contains the commands run during the deployment. An example file name is `acde1916-9099-7caf-fd21-012345abcdef-install.json`.
  + **[Deployment Group ID]\_last\_successful\_install**, a text file that lists the archive directory of the last successful deployment. This file is created when the CodeDeploy agent has copied all files in the deployment application to the instance. It is used by the CodeDeploy agent during the next deployment to determine which `ApplicationStop` and `BeforeInstall` scripts to run. An example file name is `acde1916-9099-7caf-fd21-012345abcdef_last_successful_install`.
  + **[Deployment Group ID]\_most\_recent\_install**, a text file that lists the name of the archive directory of the most recent deployment. This file is created when the files in the deployment are successfully downloaded. The [deployment group ID]\_last\_successful\_install file is created after this file, when the downloaded files are copied to their final destination. An example file name is `acde1916-9099-7caf-fd21-012345abcdef_most_recent_install`.
+  **deployment-logs** contains the following log files: 
  +  **codedeploy-agent.yyyymmdd.log** files are created for each day there is a deployment. Each log file contains information about the day's deployments. These log files might be useful for debugging problems like a permissions issue. The log file is initially named `codedeploy-agent.log`. The next day, the date of its deployments is inserted into the file name. For example, if today is January 3, 2018, you can see information about all of today's deployments in `codedeploy-agent.log`. Tomorrow, on January 4, 2018, the log file is renamed `codedeploy-agent.20180103.log`. 
  +  **codedeploy-agent-deployments.log** compiles the contents of `scripts.log` files for each deployment. The `scripts.log` files are located in the `logs` subfolder under each `Deployment ID` folder. The entries in this file are preceded by a deployment ID. For example, "`[d-ABCDEF123]LifecycleEvent - BeforeInstall`" might be written during a deployment with an ID of `d-ABCDEF123`. When `codedeploy-agent-deployments.log` reaches its maximum size, the CodeDeploy agent continues to write to it while deleting old content. 