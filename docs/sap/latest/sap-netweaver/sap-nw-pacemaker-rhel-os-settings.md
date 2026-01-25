# Operating System Requirements

This section outlines the required operating system configurations for Red Hat Enterprise Linux for SAP (RHEL for SAP) cluster nodes. Note that this is not a comprehensive list of configuration requirements for running SAP on AWS, but rather focuses specifically on cluster management prerequisites.

Consider using configuration management tools or automated deployment scripts to ensure accurate and repeatable setup across your cluster infrastructure.

###### Topics

- [Root Access](#_root_access "#_root_access")
- [Install Missing Operating System Packages](#packages-nw-rhel "#packages-nw-rhel")
- [Update and Check Operating System Versions](#_update_and_check_operating_system_versions "#_update_and_check_operating_system_versions")
- [System Logging](#_system_logging "#_system_logging")
- [Disable NetworkManager Cloud Services](#_disable_networkmanager_cloud_services "#_disable_networkmanager_cloud_services")
- [Disable kdump](#_disable_kdump "#_disable_kdump")
- [Time Synchronization Services](#_time_synchronization_services "#_time_synchronization_services")
- [Install AWS CLI and Configure Profiles](#install_shared_aws_cli_and_configure_profiles "#install_shared_aws_cli_and_configure_profiles")
- [Pacemaker Proxy Settings (Optional)](#_pacemaker_proxy_settings_optional "#_pacemaker_proxy_settings_optional")

###### Important

The following configurations must be performed on all cluster nodes. Ensure consistency across nodes to prevent cluster issues.

## Root Access

Verify root access on both cluster nodes. The majority of the setup commands in this document are performed with the root user. Assume that commands should be run as root unless there is an explicit call out to choose otherwise.

## Install Missing Operating System Packages

This is applicable to all cluster nodes. You must install any missing operating system packages.

The following packages and their dependencies are required for the pacemaker setup. Depending on your baseline image, for example, RHEL for SAP, these packages may already be installed.

| Package               | Description                                     | Category        | Required    | Configuration Pattern                               |
| --------------------- | ----------------------------------------------- | --------------- | ----------- | --------------------------------------------------- |
| chrony                | Time Synchronization                            | System Support  | Mandatory   | All                                                 |
| rsyslog               | System Logging                                  | System Support  | Mandatory   | All                                                 |
| pacemaker             | Cluster Resource Manager                        | Core Cluster    | Mandatory   | All                                                 |
| corosync              | Cluster Communication Engine                    | Core Cluster    | Mandatory   | All                                                 |
| resource-agents       | Resource Agents including SAPInstance           | Core Cluster    | Mandatory   | All                                                 |
| resource-agents-cloud | Cloud Resource agents including aws-vpc-move-ip | Core Cluster    | Mandatory   | RHEL 9 and above                                    |
| fence-agents-aws      | AWS Fencing Capabilities                        | Core Cluster    | Mandatory   | All                                                 |
| resource-agents-sap   | SAP Resource Agents                             | SAP Integration | Mandatory   | resource-agents-sap-4.15.1 required for SimpleMount |
| sap-cluster-connector | SAP HA-Script Connector                         | SAP Integration | Mandatory   | All                                                 |
| pcs                   | Pacemaker Configuration System                  | Core Cluster    | Mandatory   | All                                                 |
| sysstat               | Performance Monitoring Tools                    | Support Tools   | Recommended | All                                                 |
| dstat                 | System Resource Statistics                      | Monitoring      | Recommended | All                                                 |
| iotop                 | I/O Monitoring                                  | Monitoring      | Recommended | All                                                 |

###### Note

Refer to [Vendor Support of Deployment Types](sap-nw-pacemaker-rhel-references.md#deployments-rhel "sap-nw-pacemaker-rhel-references.md#deployments-rhel") for more information on Configuration Patterns. `Mandatory*` indicates that this package is mandatory based on the Configuration Pattern.

You can use the following script to check for missing packages and optionally install them:

```
#!/bin/bash
# Mandatory core packages for SAP NetWeaver HA on AWS
mandatory_packages="corosync pacemaker resource-agents resource-agents-cloud fence-agents-aws rsyslog chrony sap-cluster-connector pcs resource-agents-sap"

# Recommended monitoring and support packages
support_packages="sysstat dstat iotop"

# Default to checking all packages
packages="${mandatory_packages} ${support_packages}"

missingpackages=""

echo "Checking SAP NetWeaver HA package requirements..."

for package in ${packages}; do
    echo "Checking if ${package} is installed..."
    if ! rpm -q ${package} --quiet; then
        echo " ${package} is missing and needs to be installed"
        missingpackages="${missingpackages} ${package}"
    fi
done

if [ -z "$missingpackages" ]; then
    echo "All packages are installed."
else
    echo "Missing mandatory packages: $(echo ${missingpackages} | tr ' ' '\n' | grep -E "^($(echo ${mandatory_packages} | tr ' ' '|'))$")"
    echo "Missing support packages: $(echo ${missingpackages} | tr ' ' '\n' | grep -E "^($(echo ${support_packages} | tr ' ' '|'))$")"

    echo -n "Do you want to install the missing packages (y/n)? "
    read response
    if [ "$response" = "y" ]; then
        dnf install -y $missingpackages
    fi
fi

# Check sap-cluster-connector version if installed
if rpm -q sap-cluster-connector --quiet; then
    version=$(rpm -q sap-cluster-connector --qf '%{VERSION}')
    echo "sap-cluster-connector version: $version"
    if [[ $(echo "$version" | cut -d. -f1) -ge 3 ]] && [[ $(echo "$version" | cut -d. -f2) -ge 1 ]] && [[ $(echo "$version" | cut -d. -f3) -ge 1 ]]; then
        echo "sap-cluster-connector version is suitable for SimpleMount architecture"
    else
        echo "WARNING: SimpleMount architecture requires sap-cluster-connector version 3.1.1 or higher"
    fi
fi
```

If a package is not installed, and you are unable to install it using dnf, it may be because Red Hat Enterprise Linux High Availability Add-On is not available as a repository in your chosen image. You can verify the availability of the add-on using the following command:

```
$ sudo dnf repolist
```

To install or update a package or packages with confirmation, use the following command:

```
$ sudo dnf install <package_name(s)>
```

## Update and Check Operating System Versions

You must update and confirm versions across nodes. Apply all the latest patches to your operating system versions. This ensures that bugs are addressed and new features are available.

You can update the patches individually or update all system patches using the `dnf update` command. A clean reboot is recommended prior to setting up a cluster.

```
$ sudo dnf update
$ sudo reboot
```

Compare the operating system package versions on the two cluster nodes and ensure that the versions match on both nodes.

## System Logging

Both systemd-journald and rsyslog are suggested for comprehensive logging. Systemd-journald (enabled by default) provides structured, indexed logging with immediate access to events, while rsyslog is maintained for backward compatibility and traditional file-based logging. This dual approach ensures both modern logging capabilities and compatibility with existing log management tools and practices.

**1. Enable and start rsyslog:**

```
# systemctl enable --now rsyslog
```

###### 2. (Optional) Configure persistent logging for systemd-journald:

If you are not using a logging agent (like the AWS CloudWatch Unified Agent or Vector) to ship logs to a centralized location, you may want to configure persistent logging to retain logs after system reboots.

```
# mkdir -p /etc/systemd/journald.conf.d
```

Create `/etc/systemd/journald.conf.d/99-logstorage.conf` with:

```
[Journal]
Storage=persistent
```

Persistent logging requires careful storage management. Configure appropriate retention and rotation settings in `journald.conf` to prevent logs from consuming excessive disk space. Review `man journald.conf` for available options such as SystemMaxUse, RuntimeMaxUse, and MaxRetentionSec.

To apply the changes, restart journald:

```
# systemctl restart systemd-journald
```

After enabling persistent storage, only new logs will be stored persistently. Existing logs from the current boot session will remain in volatile storage until the next reboot.

**3. Verify services are running:**

```
# systemctl status systemd-journald
# systemctl status rsyslog
```

## Disable NetworkManager Cloud Services

When using Red Hat Enterprise Linux 8.6 or later, the NetworkManager cloud setup services must be disabled to maintain cluster stability. These services can interfere with cluster operations by automatically removing the overlay IP address from network interfaces.

Run these commands on each cluster node:

```
# systemctl disable --now nm-cloud-setup.timer
# systemctl disable --now nm-cloud-setup
```

Verify the services are disabled and stopped:

```
# systemctl status nm-cloud-setup.timer
# systemctl status nm-cloud-setup
```

The status commands should show both services as "disabled" and "inactive (dead)".

## Disable kdump

The kernel crash dump facility (kdump) should be disabled with the following commands on each cluster node:

```
# systemctl stop kdump
# systemctl disable kdump
```

When kdump triggers an immediate system reboot during a kernel panic, it bypasses Pacemaker’s controlled failover process, potentially leaving cluster resources in an inconsistent state.

## Time Synchronization Services

Time synchronization is important for cluster operation. Ensure that chrony rpm is installed, and configure appropriate time servers in the configuration file.

You can use Amazon Time Sync Service that is available on any instance running in a VPC. It does not require internet access. To ensure consistency in the handling of leap seconds, don’t mix Amazon Time Sync Service with any other ntp time sync servers or pools.

Create or check the `/etc/chrony.d/ec2.conf` file to define the server:

```
# Amazon EC2 time source config
server 169.254.169.123 prefer iburst minpoll 4 maxpoll 4
```

Start the chronyd.service, using the following command:

```
# systemctl enable --now chronyd.service
# systemctl status chronyd
```

Verify time synchronization is working:

```
# chronyc tracking
```

Ensure the output shows `Reference ID : A9FEA97B (169.254.169.123)` confirming synchronization with Amazon Time Sync Service.

For more information, see [Set the time for your Linux instance](../../../AWSEC2/latest/UserGuide/set-time.md "../../../AWSEC2/latest/UserGuide/set-time.md").

## Install AWS CLI and Configure Profiles

The AWS cluster resource agents require AWS Command Line Interface (AWS CLI). Check if AWS CLI is already installed, and install it if necessary.

Check if AWS CLI is installed:

```
# aws --version
```

If the command is not found, install AWS CLI v2 using the following commands:

```
# cd /tmp
# curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
# dnf install -y unzip
# unzip awscliv2.zip
# sudo ./aws/install --update
```

Create symlinks to ensure AWS CLI is in the system PATH:

```
# sudo ln -sf /usr/local/bin/aws /usr/bin/aws
```

Verify the installation:

```
# aws --version
```

The installation creates a symbolic link at `/usr/local/bin/aws` which is typically in the system PATH by default.

For more information, see [Installing or updating to the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").

After installing AWS CLI, you need to create an AWS CLI profile for the root account.

You can either edit the config file at `/root/.aws` manually or by using the `aws configure`
AWS CLI command.

You should skip providing the information for the access and secret access keys. The permissions are provided through IAM roles attached to Amazon EC2 instances.

```
# aws configure
AWS Access Key ID [None]:
AWS Secret Access Key [None]:
Default region name [None]: <region>
Default output format [None]:
```

The profile name is `default` unless configured. If you choose to use a different name you can specify `--profile`. The name chosen in this example is cluster. It is used in the AWS resource agent definition for pacemaker. The AWS Region must be the default AWS Region of the instance.

```
# aws configure --profile cluster
AWS Access Key ID [None]:
AWS Secret Access Key [None]:
Default region name [None]: <region>
Default output format [None]:
```

On the hosts, you can verify the available profiles using the following command:

```
# aws configure list-profiles
```

And review that an assumed role is associated by querying the caller identity:

```
# aws sts get-caller-identity --profile=<profile_name>
```

## Pacemaker Proxy Settings (Optional)

If your Amazon EC2 instance has been configured to access the internet and/or AWS Cloud through proxy servers, then you need to replicate the settings in the pacemaker configuration. For more information, see [Using an HTTP Proxy](../../../cli/latest/userguide/cli-configure-proxy.md "../../../cli/latest/userguide/cli-configure-proxy.md").

Add the following lines to `/etc/sysconfig/pacemaker`:

```
http_proxy=http://<proxyhost>:<proxyport>
https_proxy=http://<proxyhost>:<proxyport>
no_proxy=127.0.0.1,localhost,169.254.169.254,fd00:ec2::254
```

- Modify proxyhost and proxyport to match your settings.
- Ensure that you exempt the address used to access the instance metadata.
- Configure no_proxy to include the IP address of the instance metadata service – 169.254.169.254 (IPV4) and fd00:ec2::254 (IPV6). This address does not vary.
