# Prerequisites for user management in AWS CloudHSM Management Utility

Before you use AWS CloudHSM Management Utility (CMU) to manage hardware security module (HSM) users in AWS CloudHSM, you must complete these prerequisites. The following topics describe getting started with the CMU.

###### Sections

- [Get the IP address of an HSM in AWS CloudHSM](#user-cmu-prereq-ip "#user-cmu-prereq-ip")
- [Using CMU with Client SDK 3.2.1 and earlier](#downlevel-cmu "#downlevel-cmu")
- [Download CloudHSM Management Utility](#get-cli-users-cmu "#get-cli-users-cmu")

## Get the IP address of an HSM in AWS CloudHSM

To use CMU, you must use the configure tool to update the local configuration. CMU
creates its own connection to the cluster and this connection is _not_ cluster aware. To track cluster information, CMU maintains a local
configuration file. This means that _each time_ you use
CMU, you should first update the configuration file by running the [configure](configure-tool.md "configure-tool.md") command line tool with the `--cmu`
parameter. If you are using Client SDK 3.2.1 or earlier, you must use a different parameter
than `--cmu`. For more information, see [Using CMU with Client SDK 3.2.1 and earlier](#downlevel-cmu "#downlevel-cmu").

The `--cmu` parameter requires you to add the IP address of an HSM in your
cluster. If you have multiple HSMs, you can use any IP address. This ensures CMU can
propagate any changes you make across the entire cluster. Remember that CMU uses its local
file to track cluster information. If the cluster has changed since the last time you used
CMU from a particular host, you must add those changes to the local configuration file
stored on that host. Never add or remove an HSM while you're using CMU.

###### To get an IP address for an HSM (console)

1. Open the AWS CloudHSM console at
   [https://console.aws.amazon.com/cloudhsm/home](https://console.aws.amazon.com/cloudhsm/home "https://console.aws.amazon.com/cloudhsm/home").
2. To change the AWS Region, use the Region selector in the upper-right corner of the
   page.
3. To open the cluster detail page, in the cluster table, choose the cluster ID.
4. To get the IP address, go to the HSMs tab. For IPv4 clusters, choose an address listed under **ENI IPv4 address**. For dual-stack clusters use either the ENI IPv4 or the **ENI IPv6 address**.

###### To get an IP address for an HSM (AWS CLI)

- Get the IP address of an HSM by using the **[describe-clusters](../../../cli/latest/reference/cloudhsmv2/describe-clusters.md "../../../cli/latest/reference/cloudhsmv2/describe-clusters.md")** command from the AWS CLI. In the output from the command,
  the IP address of the HSMs are the values of `EniIp` and `EniIpV6` (if it is a dual-stack cluster).

```
`$` `aws cloudhsmv2 describe-clusters`
`{
 "Clusters": [
 { ... }
 "Hsms": [
 {
...
 "EniIp": "10.0.0.9",
...
 },
 {
...
 "EniIp": "10.0.1.6",
 "EniIpV6": "2600:113f:404:be09:310e:ed34:3412:f733",
...`
```

## Using CMU with Client SDK 3.2.1 and earlier

With Client SDK 3.3.0, AWS CloudHSM added support for the `--cmu` parameter, which
simplifies the process of updating the configuration file for CMU. If you're using a
version of CMU from Client SDK 3.2.1 or earlier, you must continue to use the
`-a` and `-m` parameters to update the configuration file. For
more information about these parameters, see [Configure
Tool](configure-tool.md "configure-tool.md").

## Download CloudHSM Management Utility

The latest version of CMU is available for HSM user management tasks whether you are using Client SDK 5 and Client SDK 3.

###### To download and install CMU

- Download and install CMU.

Amazon Linux

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL6/cloudhsm-mgmt-util-latest.el6.x86_64.rpm`
```

```
`$` `sudo yum install ./cloudhsm-mgmt-util-latest.el6.x86_64.rpm`
```

Amazon Linux 2

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-mgmt-util-latest.el7.x86_64.rpm`
```

```
`$` `sudo yum install ./cloudhsm-mgmt-util-latest.el7.x86_64.rpm`
```

CentOS 7.8+

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-mgmt-util-latest.el7.x86_64.rpm`
```

```
`$` `sudo yum install ./cloudhsm-mgmt-util-latest.el7.x86_64.rpm`
```

CentOS 8.3+

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-mgmt-util-latest.el8.x86_64.rpm`
```

```
`$` `sudo yum install ./cloudhsm-mgmt-util-latest.el8.x86_64.rpm`
```

RHEL 7 (7.8+)

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-mgmt-util-latest.el7.x86_64.rpm`
```

```
`$` `sudo yum install ./cloudhsm-mgmt-util-latest.el7.x86_64.rpm`
```

RHEL 8 (8.3+)

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-mgmt-util-latest.el8.x86_64.rpm`
```

```
`$` `sudo yum install ./cloudhsm-mgmt-util-latest.el8.x86_64.rpm`
```

Ubuntu 16.04 LTS

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Xenial/cloudhsm-mgmt-util_latest_amd64.deb`
```

```
`$` `sudo apt install ./cloudhsm-mgmt-util_latest_amd64.deb`
```

Ubuntu 18.04 LTS

```
`$` `wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Bionic/cloudhsm-mgmt-util_latest_u18.04_amd64.deb`
```

```
`$` `sudo apt install ./cloudhsm-mgmt-util_latest_u18.04_amd64.deb`
```

Windows Server 2012

    1. Download [CloudHSM Management Utility](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMManagementUtil-latest.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMManagementUtil-latest.msi").
    2. Run the CMU installer (**AWSCloudHSMManagementUtil-latest.msi**) with Windows
     administrative privilege.

Windows Server 2012 R2

    1. Download [CloudHSM Management Utility](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMManagementUtil-latest.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMManagementUtil-latest.msi").
    2. Run the CMU installer (**AWSCloudHSMManagementUtil-latest.msi**) with Windows
     administrative privilege.

Windows Server 2016

    1. Download [CloudHSM Management Utility](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMManagementUtil-latest.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMManagementUtil-latest.msi").
    2. Run the CMU installer (**AWSCloudHSMManagementUtil-latest.msi**) with Windows
     administrative privilege.
