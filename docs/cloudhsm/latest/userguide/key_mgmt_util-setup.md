# Set up AWS CloudHSM key_mgmt_util

Complete the following setup before you use AWS CloudHSM key_mgmt_util (KMU).

###### Topics

- [Step 1. Start the AWS CloudHSM client](#key_mgmt_util-start-cloudhsm-client "#key_mgmt_util-start-cloudhsm-client")
- [Step 2. Start key_mgmt_util](#key_mgmt_util-start "#key_mgmt_util-start")

## Step 1. Start the AWS CloudHSM client

Before you use key_mgmt_util, you must start the AWS CloudHSM client. The client is a daemon that
establishes end-to-end encrypted communication with the HSMs in your cluster. The key_mgmt_util
tool uses the client connection to communicate with the HSMs in your cluster. Without it,
key_mgmt_util doesn't work.

###### To start the AWS CloudHSM client

Use the following command to start the AWS CloudHSM client.

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

- For Windows client 1.1.2+:

```
`C:\Program Files\Amazon\CloudHSM>``net.exe start AWSCloudHSMClient`
```

- For Windows clients 1.1.1 and older:

```
`C:\Program Files\Amazon\CloudHSM>``start "cloudhsm_client" cloudhsm_client.exe C:\ProgramData\Amazon\CloudHSM\data\cloudhsm_client.cfg`
```

## Step 2. Start key_mgmt_util

After you start the AWS CloudHSM client, use the following command to start key_mgmt_util.

Amazon Linux

```
`$` `/opt/cloudhsm/bin/key_mgmt_util`
```

Amazon Linux 2

```
`$` `/opt/cloudhsm/bin/key_mgmt_util`
```

CentOS 7

```
`$` `/opt/cloudhsm/bin/key_mgmt_util`
```

CentOS 8

```
`$` `/opt/cloudhsm/bin/key_mgmt_util`
```

RHEL 7

```
`$` `/opt/cloudhsm/bin/key_mgmt_util`
```

RHEL 8

```
`$` `/opt/cloudhsm/bin/key_mgmt_util`
```

Ubuntu 16.04 LTS

```
`$` `/opt/cloudhsm/bin/key_mgmt_util`
```

Ubuntu 18.04 LTS

```
`$` `/opt/cloudhsm/bin/key_mgmt_util`
```

Windows

```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\key_mgmt_util.exe"`
```

The prompt changes to `Command:` when key_mgmt_util is running.

If the command fails, such as returning a `Daemon socket connection error` message, try
[updating your configuration file](troubleshooting-lost-connection.md "troubleshooting-lost-connection.md").
