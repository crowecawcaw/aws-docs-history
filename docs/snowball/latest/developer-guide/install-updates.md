Effective November 7, 2025, AWS Snowball Edge will only be available to existing customers. If you would like to use AWS Snowball Edge,
sign up prior to that date. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Installing updates to Snowball Edge devices

After downloading updates, you must install them and restart your device for the
updates to take effect. The following procedure guides you through manually installing
updates.

For clusters of Snowball Edge devices, the update must be downloaded to and installed for each device in the cluster.

###### Note

Suspend all activity on the device before you install software updates. Installing updates stops running instances and interrupts any
writes to Amazon S3 buckets on the device. This can result in lost data

###### To install software updates that were already downloaded to standalone Snowball Edge

1. Open a terminal window, and ensure that the Snowball Edge device is unlocked
   using the `describe-device` command. If the device is
   locked, use the `unlock-device` command to unlock
   it. For more information, see [Unlocking the Snowball Edge](unlockdevice.md "unlockdevice.md").
2. Run the `list-services` command to see the services available on the device. The command returns the service IDs of each service available on the device.

```

snowballEdge list-services

```

###### Example of output of `list-services` command

```

{
  "ServiceIds" : [ "greengrass", "fileinterface", "s3", "ec2", "s3-snow" ]
}

```

3. For each service ID identified by the `list-services` command, run the `describe-service` command to see the status. Use this information to identify services to stop.

```

snowballEdge describe-service --service-id `service-id`

```

###### Example of output of `describe-service` command

```

{
"ServiceId" : "s3",
  "Status" : {
    "State" : "ACTIVE"
  },
"Storage" : {
"TotalSpaceBytes" : 99608745492480,
"FreeSpaceBytes" : 99608744468480
},
"Endpoints" : [ {
"Protocol" : "http",
"Port" : 8080,
"Host" : "192.0.2.0"
}, {
"Protocol" : "https",
"Port" : 8443,
"Host" : "192.0.2.0",
"CertificateAssociation" : {
"CertificateArn" : "arn:aws:snowball-device:::certificate/6d955EXAMPLEdb71798146EXAMPLE3f0"
  }
 } ]
}

```

This output shows that the `s3` service is active and must be stopped using the `stop-service` command. 4. Use the
`stop-service` command to stop each service where the value of the `State` name is `ACTIVE` in the output of the `list-services` command. If more than one service is running, stop each one before continuing.

###### Note

The Amazon S3 adapter, Amazon EC2, AWS STS, and IAM services cannot be stopped. If Amazon S3 compatible storage on Snowball Edge is running, stop it before installing updates. Amazon S3 compatible storage on Snowball Edge has `s3-snow` as the `serviceId`.

```

snowballEdge stop-service --service-id `service-id` --device-ip-addresses `snow-device-1-ip-address` `snow-device-device-2-ip-address` `snow-device-3-ip-address` --manifest-file `path/to/manifest/file.bin` --unlock-code `29-character-unlock-code` --endpoint https://`snow-device-ip-address`

```

###### Example of output of the `stop-service` command

```

Stopping the AWS service on your Snowball Edge. You can determine the status of the AWS service using the describe-service command.

```

5. Run the `snowballEdge install-updates` command.
6. You can check the status of this installation with the `snowballEdge
describe-device-software` command. While an update is installing, you
   display the status with this command.

###### Example output

`Install State: Installing //Possible values[NA, Installing, Requires
 Reboot]`

You’ve successfully installed a software update for your Snowball Edge
device. Installing an update does not automatically apply the update to the
device. To finish installing the update, the device must be restarted.

###### Warning

Restarting your Snowball Edge device without stopping all activity on the
device can result in lost data. 7. When all the services on the device have stopped, reboot the device, unlock the device, and reboot it again. This completes installation of the downloaded software updates. For more information about rebooting the device, see [Rebooting the Snowball Edge](reboot.md "reboot.md"). For more information about unlocking the device, see [Unlocking the Snowball Edge](unlockdevice.md "unlockdevice.md"). 8. When the device powers on after the second reboot, unlock the device. 9. Run the `check-for-updates` command. This command
returns the latest available version of the Snowball Edge software, and also the
current version that is installed on the device.

###### To install software updates that were already downloaded to a cluster of Snowball Edge devices

1. For each device in the cluster, run the `describe-device` command to determine if the devices are unlocked. If the devices are
   locked, use the `unlock-cluster` command to unlock
   it. For more information, see [Unlocking the Snowball Edge](unlockdevice.md "unlockdevice.md").
2. For each device in the cluster, run the `list-services` command to see the services available on the device. The command returns the service IDs of each service available on the device.

```

snowballEdge list-services

```

###### Example of output of `list-services` command

```

{
  "ServiceIds" : [ "greengrass", "fileinterface", "s3", "ec2", "s3-snow" ]
}

```

3. For each service ID identified by the `list-services` command, run the `describe-service` command to see the status. Use this information to identify services to stop.

```

snowballEdge describe-service --service-id `service-id`

```

###### Example of output of `describe-service` command

```

{
"ServiceId" : "s3",
  "Status" : {
    "State" : "ACTIVE"
  },
"Storage" : {
"TotalSpaceBytes" : 99608745492480,
"FreeSpaceBytes" : 99608744468480
},
"Endpoints" : [ {
"Protocol" : "http",
"Port" : 8080,
"Host" : "192.0.2.0"
}, {
"Protocol" : "https",
"Port" : 8443,
"Host" : "192.0.2.0",
"CertificateAssociation" : {
"CertificateArn" : "arn:aws:snowball-device:::certificate/6d955EXAMPLEdb71798146EXAMPLE3f0"
  }
 } ]
}

```

This output shows that the `s3` service is active and must be stopped using the `stop-service` command. 4. For each device in the cluster, use the
`stop-service` command to stop each service where the value of the `State` name is `ACTIVE` in the output of the `list-services` command. If more than one service is running, stop each one before continuing.

###### Note

The Amazon S3 adapter, Amazon EC2, AWS STS, and IAM services cannot be stopped. If Amazon S3 compatible storage on Snowball Edge is running, stop it before installing updates. Amazon S3 compatible storage on Snowball Edge has `s3-snow` as the `serviceId`.

```

snowballEdge stop-service --service-id `service-id` --device-ip-addresses `snow-device-1-ip-address` `snow-device-device-2-ip-address` `snow-device-3-ip-address` --manifest-file `path/to/manifest/file.bin` --unlock-code `29-character-unlock-code` --endpoint https://`snow-device-ip-address`

```

###### Example of output of the `stop-service` command

```

Stopping the AWS service on your Snowball Edge. You can determine the status of the AWS service using the describe-service command.

```

5. For each device in the cluster, run the `install-updates` command.

```

snowballEdge install-updates

```

6. You can check the status of this installation with the `describe-device-software` command.

```

snowballEdge describe-device-software

```

###### Example of output of the `describe-device-service` command

```

Install State: Installing //Possible values[NA, Installing, Requires Reboot]
```

When the `Install State` is `Requires Reboot`, you've successfully installed the software update for your Snowball Edge
device. Installing an update does not automatically apply the update to the
device. To finish installing the update, the device must be restarted.

###### Warning

Restarting the Snowball Edge device without stopping all activity on the
device can result in lost data. 7. Reboot all devices in the cluster, unlock the cluster, and reboot all devices in the cluster again. This completes installation of the downloaded software updates. For more information about rebooting the devices, see [Rebooting the Snowball Edge](reboot.md "reboot.md"). For more information about unlocking the cluster of devices, see [Unlocking the Snowball Edge](unlockdevice.md "unlockdevice.md"). 8. After each device in the cluster has rebooted twice, unlock the cluster then use the `check-for-updates` command to verify the device was updated. This command
returns the latest available version of the Snowball Edge software, and also the current version that is installed on the device. If the current version and the latest available version are the same, the device was updated successfully.
You have now successfully updated the Snowball Edge or cluster of devices and confirmed that the update to the latest Snowball Edge software.
