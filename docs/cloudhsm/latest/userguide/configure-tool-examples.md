# AWS CloudHSM Client SDK 3 configuration examples

These examples show how to use the **configure** tool for AWS CloudHSM Client SDK 3.

###### Example : Update the HSM data for the AWS CloudHSM client and key_mgmt_util

This example uses the `-a` parameter of **configure** to
update the HSM data for the AWS CloudHSM client and key_mgmt_util. To use the `-a` parameter,
you must have the IP address for one of the HSMs in your cluster. Use either the console or
the AWS CLI to get the IP address.

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

###### To update the HSM data

1. Before updating the `-a` parameter, stop the AWS CloudHSM client. This prevents
   conflicts that might occur while **configure** edits the client's
   configuration file. If the client is already stopped, this command has no effect, so you
   can use it in a script.

Amazon Linux

```
`$` `sudo stop cloudhsm-client`
```

Amazon Linux 2

```
`$` `sudo service cloudhsm-client stop`
```

CentOS 7

```
`$` `sudo service cloudhsm-client stop`
```

CentOS 8

```
`$` `sudo service cloudhsm-client stop`
```

RHEL 7

```
`$` `sudo service cloudhsm-client stop`
```

RHEL 8

```
`$` `sudo service cloudhsm-client stop`
```

Ubuntu 16.04 LTS

```
`$` `sudo service cloudhsm-client stop`
```

Ubuntu 18.04 LTS

```
`$` `sudo service cloudhsm-client stop`
```

Windows

    * For Windows client 1.1.2+:



    ```
    `C:\Program Files\Amazon\CloudHSM>``net.exe stop AWSCloudHSMClient`
    ```
    * For Windows clients 1.1.1 and older:


    Use **Ctrl**+**C** in the command window where you started the AWS CloudHSM client.

2. This step uses the `-a` parameter of **configure** to add
   the `10.0.0.9` ENI IP address to the configurations files.

Amazon Linux

```
`$` `sudo /opt/cloudhsm/bin/configure -a 10.0.0.9`
```

Amazon Linux 2

```
`$` `sudo /opt/cloudhsm/bin/configure -a 10.0.0.9`
```

CentOS 7

```
`$` `sudo /opt/cloudhsm/bin/configure -a 10.0.0.9`
```

CentOS 8

```
`$` `sudo /opt/cloudhsm/bin/configure -a 10.0.0.9`
```

RHEL 7

```
`$` `sudo /opt/cloudhsm/bin/configure -a 10.0.0.9`
```

RHEL 8

```
`$` `sudo /opt/cloudhsm/bin/configure -a 10.0.0.9`
```

Ubuntu 16.04 LTS

```
`$` `sudo /opt/cloudhsm/bin/configure -a 10.0.0.9`
```

Ubuntu 18.04 LTS

```
`$` `sudo /opt/cloudhsm/bin/configure -a 10.0.0.9`
```

Windows

```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\configure.exe" -a 10.0.0.9`
```

3. Next, restart the AWS CloudHSM client. When the client starts, it uses the ENI IP address
   in its configuration file to query the cluster. Then, it writes the ENI IP addresses of
   all HSMs in the cluster to the `cluster.info` file.

Amazon Linux

```
`$` `sudo start cloudhsm-client`
```

Amazon Linux 2

```
`$` `sudo service cloudhsm-client start`
```

CentOS 7

```
`$` `sudo service cloudhsm-client start`
```

CentOS 8

```
`$` `sudo service cloudhsm-client start`
```

RHEL 7

```
`$` `sudo service cloudhsm-client start`
```

RHEL 8

```
`$` `sudo service cloudhsm-client start`
```

Ubuntu 16.04 LTS

```
`$` `sudo service cloudhsm-client start`
```

Ubuntu 18.04 LTS

```
`$` `sudo service cloudhsm-client start`
```

Windows

    * For Windows client 1.1.2+:



    ```
    `C:\Program Files\Amazon\CloudHSM>``net.exe start AWSCloudHSMClient`
    ```
    * For Windows clients 1.1.1 and older:



    ```
    `C:\Program Files\Amazon\CloudHSM>``start "cloudhsm_client" cloudhsm_client.exe C:\ProgramData\Amazon\CloudHSM\data\cloudhsm_client.cfg`
    ```

When the command completes, the HSM data that the AWS CloudHSM client and key_mgmt_util use is
complete and accurate.

###### Example : Update the HSM Data for CMU from client SDK 3.2.1 and earlier

This example uses the `-m`
**configure** command to copy the updated HSM data from the
`cluster.info` file to the `cloudhsm_mgmt_util.cfg`
file that cloudhsm_mgmt_util uses. Use this with CMU that ships with Client SDK 3.2.1 and
earlier.

- Before running the `-m`, stop the AWS CloudHSM client, run the `-a`
  command, and then restart the AWS CloudHSM client, as shown in the previous example. This ensures that the data
  copied into the `cloudhsm_mgmt_util.cfg` file from the
  `cluster.info` file is complete and accurate.

Linux

```
`$` `sudo /opt/cloudhsm/bin/configure -m`
```

Windows

```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\configure.exe" -m`
```

###### Example : Update the HSM Data for CMU from client SDK 3.3.0 and later

This example uses the `--cmu` parameter of the **configure**
command to update HSM data for CMU. Use this with CMU that ships with Client SDK 3.3.0 and
later. For more information about using CMU, see [Using CloudHSM
Management Utility (CMU) to Manage Users](manage-hsm-users-cmu.md "manage-hsm-users-cmu.md") and [Using
CMU with Client SDK 3.2.1 and Earlier](understand-users.md#downlevel-cmu "understand-users.md#downlevel-cmu").

- Use the `--cmu` parameter to pass the IP address of an HSM in your
  cluster.

Linux

```
`$` `sudo /opt/cloudhsm/bin/configure --cmu `<IP address>``
```

Windows

```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\configure.exe" --cmu `<IP address>``
```
