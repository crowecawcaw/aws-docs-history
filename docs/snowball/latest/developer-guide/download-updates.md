Effective November 7, 2025, AWS Snowball Edge will only be available to existing customers. If you would like to use AWS Snowball Edge,
sign up prior to that date. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Downloading updates to Snowball Edge devices

There are two ways that you can download an update for Snowball Edge:

- You can trigger manual updates at any time using specific Snowball Edge
  Client commands.
- You can programmatically determine a time to automatically update the
  device.
  The following procedure outlines the process of manually downloading updates. For
  information about automatically updating your Snowball Edge device, see
  `configure-auto-update-strategy` in [Updating a Snowball Edge](using-client-commands.md#update-client-commands "using-client-commands.md#update-client-commands").

###### Note

If your device has no access to the internet, you can download an update file
using the [GetSoftwareUpdates](../api-reference/API_GetSoftwareUpdates.md "../api-reference/API_GetSoftwareUpdates.md") API. Then point to a local file location when you
call `download-updates` using the `uri` parameter, as in the
following example.

```
snowballEdge download-updates --uri `file:///tmp/local-update`
```

For Windows operating systems, format the value of the `uri` parameter as follows:

```
snowballEdge download-updates --uri file:/`C:/path/to/local-update`
```

###### To check for and download Snowball Edge software updates for standalone devices

1. Open a terminal window, and ensure that the Snowball Edge device is unlocked
   using the `describe-device` command. If the device is
   locked, use the `unlock-device` command to unlock
   it. For more information, see [Unlocking the Snowball Edge](unlockdevice.md "unlockdevice.md").
2. When the device is unlocked, run the `snowballEdge
check-for-updates` command. This command returns the latest available
   version of the Snowball Edge software, and also the current version installed
   on the device.
3. If your device software is out of date, run the `snowballEdge
download-updates` command.

###### Note

If your device is not connected to the internet, first download an update
file using the [GetSoftwareUpdates](../api-reference/API_GetSoftwareUpdates.md "../api-reference/API_GetSoftwareUpdates.md") API. Then run the `snowballEdge
 download-updates` command using the `uri` parameter with
a local path to the file that you downloaded, as in the following
example.

```
snowballEdge download-updates --uri `file:///tmp/local-update`
```

For Windows operating systems, format the value of the `uri` parameter as follows:

```
snowballEdge download-updates --uri file:/`C:/path/to/local-update`
```

4. You can check the status of this download with the `snowballEdge
describe-device-software` command. While an update is downloading, you
   display the status using this command.

###### Example output of `describe-device-software` command

```

Install State: Downloading

```

###### To check for and download Snowball Edge software updates for clusters of devices

1. Open a terminal window, and ensure that all of the Snowball Edge devices in the cluster are unlocked
   using the `snowballEdge describe-device` command. If the devices are
   locked, use the `snowballEdge unlock-cluster` command to unlock
   it. For more information, see [Unlocking the Snowball Edge](unlockdevice.md "unlockdevice.md").
2. When all of the devices in the cluster are unlocked, for each device in the cluster, run the `check-for-updates` command. This command returns the latest available
   version of the Snowball Edge software, and also the current version installed
   on the device.

```

snowballEdge check-for-updates --unlock-code `29-character-unlock-code` --manifest-file `path/to/manifest/file.bin` --endpoint https://`ip-address-of-snow-device`

```

###### Note

The unlock code and manifest file are the same for all devices in the cluster.

###### Example of `check-for-updates` command

```

{
"InstalledVersion" : "118",
"LatestVersion" : "119"
}

```

If the value of the `LatestVersion` name is greater than the value of the `InstalledVersion` name, an update is available. 3. For each device in the cluster, use the `download-updates` command to download the update.

```

snowballEdge download-updates --uri `file:///tmp/local-update`
```

###### Note

For Windows operating systems, format the value of the `uri` parameter as follows:

```
snowballEdge download-updates --uri file:/`C:/path/to/local-update`
```

4. To check the status of this download for each device in the cluster, use the `describe-device-software` command.

```

snowballEdge describe-device-software --unlock-code `29-character-unlock-code` --manifest-file `path/to/manifest/file.bin` --endpoint https://`ip-address-of-snow-device`

```

###### Example of output of the `describe-device-software` command

```

{
"InstalledVersion" : "118",
"InstallingVersion" : "119",
"InstallState" : "DOWNLOADED",
"CertificateExpiry" : "Sat Mar 30 16:47:51 UTC 2024"
}

```

If the value of the `InstallState` name is `DOWNLOADED`, the update is done downloading and available to install.
