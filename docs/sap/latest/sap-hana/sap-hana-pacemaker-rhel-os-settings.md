# Operating System Requirements

This section outlines the required operating system configurations for Red Hat Enterprise Linux for SAP (RHEL for SAP) cluster nodes. Note that this is not a comprehensive list of configuration requirements for running SAP HANA on AWS, but rather focuses specifically on cluster management prerequisites.

Consider using configuration management tools or automated deployment scripts to ensure accurate and repeatable setup across your cluster infrastructure.

###### Topics

- [Root Access](#_root_access "#_root_access")
- [Install Missing Operating System Packages](#packages "#packages")
- [Update and Check Operating System Versions](#_update_and_check_operating_system_versions "#_update_and_check_operating_system_versions")
- [System Logging](#_system_logging "#_system_logging")
- [Disable NetworkManager Cloud Services](#_disable_networkmanager_cloud_services "#_disable_networkmanager_cloud_services")
- [Time Synchronization Services](#_time_synchronization_services "#_time_synchronization_services")
- [AWS CLI Profile](#shared_aws_cli_profile "#shared_aws_cli_profile")
- [Pacemaker Proxy Settings (Optional)](#_pacemaker_proxy_settings_optional "#_pacemaker_proxy_settings_optional")
- [Add Overlay IP for Initial Database Access](#_add_overlay_ip_for_initial_database_access "#_add_overlay_ip_for_initial_database_access")
- [Hostname Resolution](#_hostname_resolution "#_hostname_resolution")

###### Important

The following configurations must be performed on all cluster nodes. Ensure consistency across nodes to prevent cluster issues.

## Root Access

Verify root access on both cluster nodes. The majority of the setup commands in this document are performed with the root user. Assume that commands should be run as root unless there is an explicit call out to choose otherwise.

## Install Missing Operating System Packages

This is applicable to all cluster nodes. You must install any missing operating system packages.

The following packages and their dependencies are required for the pacemaker setup. Depending on your baseline image, for example, RHEL for SAP, these packages may already be installed.

| Package                           | Description                                     | Category       | Required    | Configuration Pattern                           |
| --------------------------------- | ----------------------------------------------- | -------------- | ----------- | ----------------------------------------------- |
| chrony                            | Time Synchronization                            | System Support | Mandatory   | All                                             |
| pacemaker                         | Cluster Resource Manager                        | Core Cluster   | Mandatory   | All                                             |
| corosync                          | Cluster Communication Engine                    | Core Cluster   | Mandatory   | All                                             |
| pcs                               | Cluster Management CLI                          | Core Cluster   | Mandatory   | All                                             |
| resource-agents                   | Basic Resource Agents                           | Core Cluster   | Mandatory   | All                                             |
| resource-agents-cloud             | Cloud Resource agents including aws-vpc-move-ip | Core Cluster   | Mandatory   | All                                             |
| fence-agents-aws                  | Fencing Capabilities                            | Core Cluster   | Mandatory   | All                                             |
| sap-hana-ha                       | New Generation HANA System Replication Agent    | SAP HANA HA    | Mandatory\* | SAPHANAScaleUp-SAPANGI, SAPHANAScaleOut-SAPANGI |
| resource-agents-sap-hana          | SAP HANA Resource Agents                        | SAP HANA HA    | Mandatory\* | SAPHANAScaleUp-Classic                          |
| resource-agents-sap-hana-scaleout | SAP HANA Resource Agents                        | SAP HANA HA    | Mandatory\* | SAPHANAScaleOut-Classic                         |
| sos                               | System Information Gathering                    | Support Tools  | Mandatory   | All                                             |
| sysstat                           | Performance Monitoring Tools                    | Support Tools  | Mandatory   | All                                             |
| pcp-system-tools                  | Performance Co-Pilot Tools                      | Monitoring     | Recommended | All                                             |

###### Note

Refer to [Vendor Support of Deployment Types](sap-hana-pacemaker-rhel-references.md#deployments-rhel "sap-hana-pacemaker-rhel-references.md#deployments-rhel") for more information on Configuration Patterns. `Mandatory*` indicates that this package is mandatory based on the Configuration Pattern.

```
 #!/bin/bash

# Mandatory core packages for SAP HANA HA on AWS
mandatory_packages="pacemaker corosync pcs chrony resource-agents resource-agents-sap-hana resource-agents-cloud fence-agents-aws"

# HANA SR packages - Previous Generation (still in common use)
hanaSR_scaleup="resource-agents-sap-hana"  # For scale-up deployments
hanaSR_scaleout="resource-agents-sap-hana-scaleout"  # For scale-out deployment

# HANA SR packages - New Generation
hanaSR_angi="sap-hana-ha"  # New generation package for both scale-up and scale-out

# Recommended monitoring and support packages
support_packages="pcp-system-tools sos sysstat"

# Note: Choose hanaSR_scaleup/hanaSR_scaleout or hanaSR_angi
# Uncomment the appropriate line based on your deployment:
packages="${mandatory_packages} ${hanaSR_scaleup} ${support_packages}"
#packages="${mandatory_packages} ${hanaSR_scaleout} ${support_packages}"
#packages="${mandatory_packages} ${hanaSR_angi} ${support_packages}"

missingpackages=""

for package in ${packages}; do
    echo "Checking if ${package} is installed..."
    if ! rpm -q ${package} &>/dev/null; then
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
```

If you encounter issues installing high availability packages, verify repository access:

```
 $ sudo dnf repolist
```

For BYOL (Bring Your Own License) systems, also verify subscription status using subscription-manager.

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

For more information, see [Set the time for your Linux instance](../../../AWSEC2/latest/UserGuide/set-time.md "../../../AWSEC2/latest/UserGuide/set-time.md").

## AWS CLI Profile

The AWS cluster resource agents use AWS Command Line Interface (AWS CLI). You need to create an AWS CLI profile for the root account.

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

## Add Overlay IP for Initial Database Access

This step is optional and only needed if you require client connectivity to the SAP HANA database before cluster setup. The Overlay IP will later be managed automatically by the cluster resources.

To enable initial database access, manually add the Overlay IP to the primary instance (where the SAP HANA database is currently running):

```
 # ip addr add <hana_overlayip>/32 dev eth0
```

- This configuration is temporary and will be lost after instance reboot
- Only configure this on the current primary instance
- The cluster will take over management of this IP once configured

## Hostname Resolution

You must ensure that all instances can resolve all hostnames in use. Add the hostnames for cluster nodes to `/etc/hosts` file on all cluster nodes. This ensures that hostnames for cluster nodes can be resolved even in case of DNS issues. See the following example for a two-node cluster:

```
 # cat /etc/hosts
10.2.10.1 hanahost01.example.com hanahost01
10.2.20.1 hanahost02.example.com hanahost02
172.16.52.1 hanahdb.example.com hanahdb
```

In this example, the secondary IPs used for the second cluster ring are not mentioned. They are only used in the cluster configuration. You can allocate virtual hostnames for administration and identification purposes.

###### Important

The Overlay IP is out of VPC range, and cannot be reached from locations not associated with the route table, including on-premises.
