AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Unlocking the Snowball Edge

This section describes unlocking the Snowball Edge device using the Snowball Edge Client. To unlock the device using AWS OpsHub, a graphical user interface (GUI) tool for Snowball Edge, see [Unlock a device](connect-unlock-device.md "connect-unlock-device.md").

Before using a Snowball Edge device to transfer data or perform edge compute tasks, you need to unlock the device. When unlocking the device, you authenticate your ability to access it by providing two forms of credentials: a 29-digit unlock code and a manifest file. After you unlock the device, you can further configure the device, move data to or from it, set up and use Amazon EC2-compatible instances, and more.

Before unlocking a device, the device must be plugged in to power and network, turned on, and an IP address assigned. See [Connecting a Snowball Edge to your local
network](getting-started.md#getting-started-connect "getting-started.md#getting-started-connect"). You will need the following information about the Snowball Edge device:

- Download and install the Snowball Edge client. For more information, see [Downloading and installing the Snowball Edge
  Client](using-client-commands.md#download-the-client "using-client-commands.md#download-the-client").
- Get the credentials from the AWS Snow Family Management Console. For one or more standalone devices, the unlock codes and manifest file for each Snowball Edge. For a cluster of Snowball Edge devices, the one unlock code and one manifest file for the cluster. For more information on downloading credentials, see [Getting credentials to access a Snowball Edge](getting-started.md#get-credentials "getting-started.md#get-credentials").
- Power on each device and connect it to your network. For more information, see [Connecting a Snowball Edge to your local
  network](getting-started.md#getting-started-connect "getting-started.md#getting-started-connect").

###### To unlock a standalone device with the Snowball Edge Client

1. Find the IP address for the AWS Snowball Edge device on the LCD display of the

AWS Snowball Edge device, under the **Connections** tab. Make a note of

that IP address. 2. Use the `unlock-device` command to authenticate
your access to the Snowball Edge with the IP address of the Snowball Edge and your
credentials, as follows.

```

  snowballEdge unlock-device --endpoint https://`ip-address-of-device` --manifest-file `/Path/to/manifest/file.bin` --unlock-code `29-character-unlock-code`
```

The device indicates it was unlocked successfully with the following message.

```

Your Snowball Edge device is unlocking. You may determine the unlock state of your device using the describe-device command. Your Snowball Edge device will be available for use when it is in the UNLOCKED state.

```

If the command returns `connection refused`, see [Troubleshooting unlocking a Snowball Edge](#troubleshooting-unlocking "#troubleshooting-unlocking").

###### Example of `unlock-device` command

In this example, the IP address for the device is `192.0.2.0`, the manifest file name is `JID2EXAMPLE-0c40-49a7-9f53-916aEXAMPLE81-manifest.bin`, and the
29-character unlock code is `12345-abcde-12345-ABCDE-12345`.

```

  snowballEdge unlock-device --endpoint https://192.0.2.0 --manifest-file /Downloads/JID2EXAMPLE-0c40-49a7-9f53-916aEXAMPLE81-manifest.bin /
    --unlock-code 12345-abcde-12345-ABCDE-12345
```

###### To unlock a cluster of Snowball Edge devices with the Snowball Edge client

1. Find the IP address of each of the devices in the cluster on the LCD display of each

AWS Snowball Edge device, under the **Connections** tab. Make a note of

the IP addresses. 2. Use the `snowballEdge unlock-cluster` command to authenticate

your access to the cluster of AWS Snowball Edge device devices with the IP address of one of the devices in the cluster, your

credentials, and the IP addresses of all devices in the cluster as follows.

```


snowballEdge unlock-cluster --endpoint https://`ip-address-of-device` --manifest-file `Path/to/manifest/file.bin` --unlock-code `29-character-unlock-code` --device-ip-addresses `ip-address-of-cluster-device-1` `ip-address-of-cluster-device-2` `ip-address-of-cluster-device-3`


```

The cluster of devices indicates it was unlocked successfully with the following message.

```


Your Snowball Edge Cluster is unlocking. You may determine the unlock state of your cluster using the describe-cluster command. Your Snowball Edge Cluster will be available for use when your Snowball Edge devices are in the UNLOCKED state.


```

If the command returns `connection refused`, see [Troubleshooting unlocking a Snowball Edge](#troubleshooting-unlocking "#troubleshooting-unlocking").

###### Example of `unlock-cluster` command

In this example for a cluster of five devices, the IP address for one of the devices in the cluster is `192.0.2.0`, the manifest file name is `JID2EXAMPLE-0c40-49a7-9f53-916aEXAMPLE81-manifest.bin`, and the

29-character unlock code is `12345-abcde-12345-ABCDE-12345`.

```


snowballEdge unlock-cluster --endpoint https://192.0.2.0 --manifest-file /Downloads/JID2EXAMPLE-0c40-49a7-9f53-916aEXAMPLE81-manifest.bin /

  --unlock-code 12345-abcde-12345-ABCDE-12345 --device-ip-addresses 192.0.2.0 192.0.2.1 192.0.2.2 192.0.2.3 192.0.2.4
```

## Troubleshooting unlocking a Snowball Edge

If the `unlock-device` command returns `connection refused`, you may have mistyped the command syntax or the configuration of your computer or network may be preventing the command from reaching the Snow device. Take these actions to resolve the situation:

1. Ensure the command was entered correctly.
   1. Use the LCD screen on the device to verify the IP addressed used in the command is correct.
   2. Ensure that the path to the manifest file used in the command is correct, including the file name.
   3. Use the [AWS Snowball Edge Management Console](https://console.aws.amazon.com/importexport/home?region=us-west-2 "https://console.aws.amazon.com/importexport/home?region=us-west-2") to verify the unlock code used in the command is correct.

2. Ensure the computer you are using is on the same network and subnet as the Snow device.
3. Ensure the computer you are using and the network are configured to allow access to the Snow device. Use the `ping` command for your operating system to determine if the computer can reach the Snow device over the network. Check the configurations of antivirus software, firewall configuration, virtual private network (VPN), or other configurations of your computer and network.

Now you can begin using the Snowball Edge.

**Next:**
[Setting up local users on a Snowball Edge](getting-started.md#setup-local-iam "getting-started.md#setup-local-iam")
