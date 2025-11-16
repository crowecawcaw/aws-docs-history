AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Configuring and using the Snowball Edge Client

The Snowball Edge Client is a command-line interface (CLI) tool from AWS that you can use to work with a Snowball Edge or a cluster of Snowball Edge. You can use the client to unlock a Snowball Edge or cluster of devices, set up Snowball Edge, start and stop services on devices, and transfer data to or from devices. The Snowball Edge client is compatible with computers running on Linux, macOS, and Windows operating systems.

###### Topics

- [Downloading and installing the Snowball Edge
  Client](#download-the-client "#download-the-client")
- [Configuring a profile for the Snowball Edge
  Client](#client-configuration "#client-configuration")
- [Finding Snowball Edge client version](#cli-version "#cli-version")
- [Getting credentials for a Snowball Edge](#client-credentials "#client-credentials")
- [Starting a service on a Snowball Edge](#edge-start-service "#edge-start-service")
- [Stopping a service on a Snowball Edge](#edge-stop-service "#edge-stop-service")
- [Viewing and downloading logs from Snowball Edge](#logs "#logs")
- [Viewing status of a Snowball Edge](#client-status "#client-status")
- [Vieiwing status of services running on Snowball Edge](#client-service-status "#client-service-status")
- [Viewing status of features of Snowball Edge](#snowball-edge-describe-features "#snowball-edge-describe-features")
- [Setting time servers for Snowball Edge](#client-set-ntp "#client-set-ntp")
- [Getting a QR code to validate Snowball Edge NFC tags](#client-qr-code "#client-qr-code")
- [Updating MTU size](#update-mtu-size "#update-mtu-size")

## Downloading and installing the Snowball Edge

Client

You can download the Snowball Edge Client from
[AWS Snowball Edge Resources](http://aws.amazon.com/snowball/resources/ "http://aws.amazon.com/snowball/resources/"). On that page, you can find the installation
package for your operating system.

Install and configure the client according to the instructions below.

Linux

###### Note

The Snowball Edge client is only supported on 64-bit Linux
distributions.

1. Extract the `snowball-client-linux.tar.gz` file. It creates the `/snowball-client-linux-build_number/bin` folder structure and extracts the files there.
2. Run the following commands to configure the folders.

```

  chmod u+x `snowball-client-linux-build_number`/bin/snowballEdge

```

```

  chmod u+x `snowball-client-linux-build_number`/jre/bin/java

```

3. Add `/`snowball-client-linux-build_number`/bin` to your operating system's $PATH environment variable to run Snowball Edge Client commands from any directory. For more information, see the documentation for your device's operating system or your shell.

macOS

1. Extract the `snowball-client-mac.tar.gz` file. It creates the `/snowball-client-linux-build_number/bin` folder structure and extracts the files there.
2. Run the following commands to configure the folders.

```

  chmod u+x `snowball-client-mac-build_number`/bin/snowballEdge

```

```

  chmod u+x `snowball-client-mac-build_number`/jre/bin/java

```

3. Add `/`snowball-client-mac-build_number`/bin` to your operating system's $PATH environment variable to run Snowball Edge Client commands from any directory. For more information, see the documentation for your device's operating system or your shell.

Windows
The client is packaged as Microsoft Software Installer (MSI) file. Open the file and follow the prompts in the installation wizard. When the client has
been installed, you can run it from any directory without any additional preparation.

## Configuring a profile for the Snowball Edge

Client

Every time you run a command for the Snowball Edge Client, you provide your
manifest file, unlock code, and the IP address of the Snowball Edge. Instead of providing these each time you run a command, you can use the `configure` command to
store the path to the manifest file, the 29-character unlock code, and the endpoint (the IP address of the Snowball Edge) as a
profile. After configuration, you can use Snowball Edge Client commands
without having to manually enter these values for each command by including the profile name with the command. After you
configure the Snowball Edge Client, the information is saved in a plaintext JSON
format to ``home
 directory`/.aws/snowball/config/snowball-edge.config`. Make sure your environment is configured to allow you to create this file.

###### Important

Anyone who can access the configuration file can access the data on your
Snowball Edge devices or clusters. Managing local access control for this file
is one of your administrative responsibilities.

You can also use AWS OpsHub to create a profile. Profiles created in AWS OpsHub are available to use with the Snowball Edge Client and profiles created in AWS OpsHub are available to use with the Snowball Edge Client. For more information, see [Managing profiles](manage-device.md#manage-profile "manage-device.md#manage-profile").

###### To create a profile

1. Enter the command in the command line interface for your operating system. The value of the `profile-name` parameter is the name of the profile. You will provide it in the future when running Snowball Edge Client commands.

```

snowballEdge configure --profile `profile-name`
```

2. The Snowball Edge Client will prompt you for each parameter. When prompted, enter the information for your environment and the Snowball Edge.

###### Note

The value of the `endpoint` parameter is the IP address of the Snowball Edge, prefaced by `https://`. You can
locate the IP address for the Snowball Edge device on the LCD screen on the front of the device.

###### Example output of `configure` command

```

Configuration will stored at home directory\.aws\snowball\config\snowball-edge.config
Snowball Edge Manifest Path: `/Path/to/manifest/file`
Unlock Code: `29 character unlock code`
Default Endpoint: `https://192.0.2.0`
```

The Snowball Edge Client will check that the unlock code is correct for the manifest file. If they do not match, the command stops and does not create the profile. Check the unlock code and manifest file and run the command again.

To use the profile, include `--profile profile-name` after the command syntax.

If you are using multiple, standalone Snowball Edge, you can create a profile for each. To create another profile, run the `configure` command again, provide a different value for the `--profile` prameter, and provide the information for another device.

###### Example `snowball-edge.config` file

This example shows a profile file containing three
profiles—`SnowDevice1profile`,
`SnowDevice2profile`, and `SnowDevice3profile`.

```

{"version":1,"profiles":
    {
    "SnowDevice1profile":
        {
            "name":"SnowDevice1profile",
            "jobId":"JID12345678-136f-45b4-b5c2-847db8adc749",
            "unlockCode":"db223-12345-dbe46-44557-c7cc2",
            "manifestPath":"C:\\Users\\Administrator\\.aws\\ops-hub\\manifest\\JID12345678-136f-45b4-b5c2-847db8adc749_manifest-1670622989203.bin",
            "defaultEndpoint":"https://10.16.0.1",
            "isCluster":false,
            "deviceIps":[]
        },
    },
    "SnowDevice2profile":
    {
        "name":"SnowDevice2profile",
        "jobId":"JID12345678-fdb2-436a-a4ff-7c510dec1bae",
        "unlockCode":"b893b-54321-0f65c-6c5e1-7f748",
        "manifestPath":"C:\\Users\\Administrator\\.aws\\ops-hub\\manifest\\JID12345678-fdb2-436a-a4ff-7c510dec1bae_manifest-1670623746908.bin",
        "defaultEndpoint":"https://10.16.0.2",
        "isCluster":false,
        "deviceIps":[]
    },
    "SnowDevice3profile":
    {
        "name":"SnowDevice3profile",
        "jobId":"JID12345678-c384-4a5e-becd-ab5f38888463",
        "unlockCode":"64c89-13524-4d054-13d93-c1b80",
        "manifestPath":"C:\\Users\\Administrator\\.aws\\ops-hub\\manifest\\JID12345678-c384-4a5e-becd-ab5f38888463_manifest-1670623999136.bin",
        "defaultEndpoint":"https://10.16.0.3",
        "isCluster":false,
        "deviceIps":[]
    }
}

```

To edit or delete profiles, edit the profile file in a text editor.

###### To edit a profile

1. In a text editor, open `snowball-edge.config` from
   ``home directory`\.aws\snowball\config`.

###### Note

Make sure your environment is configured to allow you to access to read and write this file. 2. Edit the file as necessary. For example, to change the IP address of the Snowball Edge
associated with the profile, change the `defaultEndpoint` entry. 3. Save and close the file.

###### To delete a profile

1. Using a text editor, open `snowball-edge.config` from
   ``home directory`\.aws\snowball\config`.

###### Note

Make sure your environment is configured to allow you to access to read and write this file. 2. Delete the line that contains the profile name, the curly brackets
`{`
`}`that follow the profile name, and the contents within the
those brackets. 3. Save and close the file.

## Finding Snowball Edge client version

Use the `version` command to see the version of the Snowball Edge command line interface (CLI) client.

**Usage**

```

    snowballEdge version

```

**Example output**

```

    Snowball Edge client version: 1.2.0  Build 661

```

## Getting credentials for a Snowball Edge

Using the `snowballEdge list-access-keys` and `snowballEdge
 get-secret-access-key` commands, you can get the credentials of the admin
user of your AWS account on Snowball Edge. You can use these credentials to
create AWS Identity and Access Management (IAM users) and roles, and to authenticate your requests when
using the AWS CLI or with an AWS SDK. These credentials are only associated with an
individual job for Snowball Edge, and you can use them only on the device or
cluster of devices. The device or devices don't have any IAM permissions in the
AWS Cloud.

###### Note

If you're using the AWS CLI with the Snowball Edge, you must use these
credentials when you configure the CLI. For information about configuring
credentials for the AWS CLI, see [Configuring the AWS CLI](../../../cli/latest/userguide/cli-chap-getting-started.md#cli-quick-configuration "../../../cli/latest/userguide/cli-chap-getting-started.md#cli-quick-configuration") in the
_AWS Command Line Interface User Guide_.

**Usage (configured Snowball Edge client)**

```
snowballEdge list-access-keys
```

###### Example Output

```
{
  "AccessKeyIds" : [ "AKIAIOSFODNN7EXAMPLE" ]
}

```

**Usage (configured Snowball Edge client)**

```
snowballEdge get-secret-access-key --access-key-id `Access Key`
```

###### Example Output

```
[snowballEdge]
aws_access_key_id = AKIAIOSFODNN7EXAMPLE
aws_secret_access_key = wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY


```

## Starting a service on a Snowball Edge

Snowball Edge devices support multiple services. These
include compute instances, the Network File System (NFS) interface, Snowball Edge Device Management, and AWS IoT Greengrass. The Amazon S3 adapter service, Amazon EC2, AWS STS, and IAM are started by
default and can't be stopped or restarted. However,
the NFS interface, Snowball Edge Device Management, and AWS IoT Greengrass can be started by using its service ID with the `start-service`
command. To get the service ID for each service, you can use the `list-services` command.

Before you run this command, create a single virtual network interface to bind to
the service that you're starting. For more information, see [Creating a Virtual Network Interface on a Snowball Edge](using-ec2-edge-client.md#ec2-edge-create-vnic "using-ec2-edge-client.md#ec2-edge-create-vnic").

```

snowballEdge start-service --service-id `service_id` --virtual-network-interface-arns `virtual-network-interface-arn` --profile `profile-name`
```

###### Example output of `start-service` command

```
Starting the AWS service on your Snowball Edge. You can determine the status of the AWS service using the describe-service command.
```

## Stopping a service on a Snowball Edge

To stop a service running on a Snowball Edge, you can use the
`stop-service` command.

The Amazon S3 adapter, Amazon EC2, AWS STS, and IAM services cannot be stopped.

###### Warning

Data loss can occur if the Network File System (NFS) service is stopped before remaining buffered data is
written to the device. For more information on using the NFS service, see [Managing the NFS interface on Snowball Edge](shared-using-nfs.md "shared-using-nfs.md").

###### Note

Stopping the Amazon S3 compatible storage on Snowball Edge service disables access to the data stored in your S3 buckets on the device or cluster. Access is restored when the Amazon S3 compatible storage on Snowball Edge is started again. For devices enabled with Amazon S3 compatible storage on Snowball Edge, it is recommended to start the service after the Snowball Edge device is powered up. See [Setting up Snowball Edge](s3compatible-on-snow.md#setting-up-s3-on-snow-cluster "s3compatible-on-snow.md#setting-up-s3-on-snow-cluster") in this guide.

```

snowballEdge stop-service --service-id `service_id` --profile `profile-name`
```

###### Example output of `stop-service` command

```
Stopping the AWS service on your Snowball Edge. You can determine the status of the AWS service using the describe-service command.
```

##

Viewing and downloading logs from Snowball Edge

When you transfer data between your on-premises data center and a Snowball Edge,
logs are automatically generated. If you encounter unexpected errors during data
transfer to the device, you can use the following commands to save a copy of the
logs to your local server.

There are three commands related to logs:

- `list-logs` – Returns a list of logs in JSON format. This
  list reports the size of the logs in bytes, the ARN for the logs, the
  service ID for the logs, and the type of logs.

**Usage**

```
snowballEdge list-logs --profile `profile-name`
```

###### Example output of the `list-logs` command

```
{
  "Logs" : [ {
    "LogArn" : "arn:aws:snowball-device:::log/s3-storage-JIEXAMPLE2f-1234-4953-a7c4-dfEXAMPLE709",
    "LogType" : "SUPPORT",
    "ServiceId" : "s3",
    "EstimatedSizeBytes" : 53132614
  }, {
    "LogArn" : "arn:aws:snowball-device:::log/fileinterface-JIDEXAMPLEf-1234-4953-a7c4-dfEXAMPLE709",
    "LogType" : "CUSTOMER",
    "ServiceId" : "fileinterface",
    "EstimatedSizeBytes" : 4446
  }]
}


```

- `get-log` – Downloads a copy of a specific log from the
  Snowball Edge to your device at a specified path. `CUSTOMER`
  logs are saved in the `.zip` format, and you can extract this
  type of log to view its contents. `SUPPORT` logs are encrypted
  and can only be read by AWS Support. You have the option of
  specifying a name and a path for the log.

**Usage**

```
snowballEdge get-log --log-arn arn:aws:snowball-device:::log/fileinterface-JIDEXAMPLEf-1234-4953-a7c4-dfEXAMPLE709 --profile `profile-name`
```

###### Example output of `get-log` command

```
Logs are being saved to download/path/snowball-edge-logs-1515EXAMPLE88.bin

```

- `get-support-logs` – Downloads a copy of all the
  `SUPPORT` type of logs from the Snowball Edge to your
  service at a specified path.

**Usage**

```
snowballEdge get-support-logs --profile `profile-name`
```

###### Example output of `get-support-logs` command

```
Logs are being saved to download/path/snowball-edge-logs-1515716135711.bin
```

###### Important

`CUSTOMER` type might contain sensitive information about your own
data. To protect this potentially sensitive information, we strongly suggest
that you delete these logs once you're done with them.

## Viewing status of a Snowball Edge

You can determine the status and general health of Snowball Edge
with the `describe-device` command.

```
snowballEdge describe-device --profile `profile-name`
```

###### Example output of `describe-device` command

```

                            {
  "DeviceId": "JID-EXAMPLE12345-123-456-7-890",
  "UnlockStatus": {
    "State": "UNLOCKED"
  },
  "ActiveNetworkInterface": {
    "IpAddress": "192.0.2.0"
  },
  "PhysicalNetworkInterfaces": [
    {
      "PhysicalNetworkInterfaceId": "s.ni-EXAMPLEd9ecbf03e3",
      "PhysicalConnectorType": "RJ45",
      "IpAddressAssignment": "STATIC",
      "IpAddress": "0.0.0.0",
      "Netmask": "0.0.0.0",
      "DefaultGateway": "192.0.2.1",
      "MacAddress": "EX:AM:PL:E0:12:34"
    },
    {
      "PhysicalNetworkInterfaceId": "s.ni-EXAMPLE4c3840068f",
      "PhysicalConnectorType": "QSFP",
      "IpAddressAssignment": "STATIC",
      "IpAddress": "0.0.0.0",
      "Netmask": "0.0.0.0",
      "DefaultGateway": "192.0.2.2",
      "MacAddress": "EX:AM:PL:E0:56:78"
    },
    {
      "PhysicalNetworkInterfaceId": "s.ni-EXAMPLE0a3a6499fd",
      "PhysicalConnectorType": "SFP_PLUS",
      "IpAddressAssignment": "DHCP",
      "IpAddress": "192.168.1.231",
      "Netmask": "255.255.255.0",
      "DefaultGateway": "192.0.2.3",
      "MacAddress": "EX:AM:PL:E0:90:12"
    }
  ]
}

```

## Vieiwing status of services running on Snowball Edge

You can determine the status and general health of the services running on
Snowball Edge devices with the `describe-service` command. You can
first run the `list-services` command to see what services are
running.

- `list-services`

**Usage**

```
snowballEdge list-services --profile `profile-name`
```

###### Example output of `list-services` command

```
{
  "ServiceIds" : [ "greengrass", "fileinterface", "s3", "ec2", "s3-snow" ]
}

```

- `describe-service`

This command returns a status value for a service. It also includes state
information that might be helpful in resolving issues you encounter with the
service. Those states are as follows.

    + `ACTIVE` – The service is running and available
     for use.
    + `ACTIVATING` – The service is starting up, but it
     is not yet available for use.
    + `DEACTIVATING` – The service is in the process of
     shutting down.
    + `DEGRADED` – For Amazon S3 compatible storage on Snowball Edge, this status indicates one or more disks or devices in cluster is down. The Amazon S3 compatible storage on Snowball Edge service is running uninterrupted, but you should recover or replace the affected device before the cluster quorum is lost to minimize the risk of lost data. See [Clustering overview](ClusterOverview.md "ClusterOverview.md") in this guide.
    + `INACTIVE` – The service is not running and is
     not available for use.

**Usage**

```
snowballEdge describe-service --service-id `service-id` --profile `profile-name`
```

###### Example output of `describe-service` command

```

{
  "ServiceId": "s3",
  "Status": {
    "State": "ACTIVE"
  },
  "Storage": {
    "TotalSpaceBytes": 99608745492480,
    "FreeSpaceBytes": 99608744468480
  },
  "Endpoints": [
    {
      "Protocol": "http",
      "Port": 8080,
      "Host": "192.0.2.0"
    },
    {
      "Protocol": "https",
      "Port": 8443,
      "Host": "192.0.2.0",
      "CertificateAssociation": {
        "CertificateArn": "arn:aws:snowball-device:::certificate/6d955EXAMPLEdb71798146EXAMPLE3f0"
      }
    }
  ]
}

```

###### Example Amazon S3 compatible storage on Snowball Edge service output

The `describe-service` command provides the following output for the `s3-snow` value of the `service-id` parameter.

```

{
  "ServiceId" : "s3-snow",
  "Autostart" : false,
  "Status" : {
    "State" : "ACTIVE"
  },
  "ServiceCapacities" : [ {
    "Name" : "S3 Storage",
    "Unit" : "Byte",
    "Used" : 640303104,
    "Available" : 219571981512
  } ],
  "Endpoints" : [ {
    "Protocol" : "https",
    "Port" : 443,
    "Host" : "10.0.2.123",
    "CertificateAssociation" : {
      "CertificateArn" : "arn:aws:snowball-device:::certificate/a65ba817f2c5ac9683fc3bc1ae123456"
    },
    "Description" : "s3-snow bucket API endpoint",
    "DeviceId" : "JID6ebd4c50-c3a1-4b16-b32c-b254f9b7f2dc",
    "Status" : {
      "State" : "ACTIVE"
    }
  }, {
    "Protocol" : "https",
    "Port" : 443,
    "Host" : "10.0.3.202",
    "CertificateAssociation" : {
      "CertificateArn" : "arn:aws:snowball-device:::certificate/a65ba817f2c5ac9683fc3bc1ae123456"
    },
    "Description" : "s3-snow object API endpoint",
    "DeviceId" : "JID6ebd4c50-c3a1-4b16-b32c-b254f9b7f2dc",
    "Status" : {
      "State" : "ACTIVE"
    }
  }, {
    "Protocol" : "https",
    "Port" : 443,
    "Host" : "10.0.3.63",
    "CertificateAssociation" : {
      "CertificateArn" : "arn:aws:snowball-device:::certificate/a65ba817f2c5ac9683fc3bc1ae123456"
    },
    "Description" : "s3-snow bucket API endpoint",
    "DeviceId" : "JID2a1e0deb-38b1-41f8-b904-a396c62da70d",
    "Status" : {
      "State" : "ACTIVE"
    }
  }, {
    "Protocol" : "https",
    "Port" : 443,
    "Host" : "10.0.2.243",
    "CertificateAssociation" : {
      "CertificateArn" : "arn:aws:snowball-device:::certificate/a65ba817f2c5ac9683fc3bc1ae123456"
    },
    "Description" : "s3-snow object API endpoint",
    "DeviceId" : "JID2a1e0deb-38b1-41f8-b904-a396c62da70d",
    "Status" : {
      "State" : "ACTIVE"
    }
  }, {
    "Protocol" : "https",
    "Port" : 443,
    "Host" : "10.0.2.220",
    "CertificateAssociation" : {
      "CertificateArn" : "arn:aws:snowball-device:::certificate/a65ba817f2c5ac9683fc3bc1ae123456"
    },
    "Description" : "s3-snow bucket API endpoint",
    "DeviceId" : "JIDcc45fa8f-b994-4ada-a821-581bc35d8645",
    "Status" : {
      "State" : "ACTIVE"
    }
  }, {
    "Protocol" : "https",
    "Port" : 443,
    "Host" : "10.0.2.55",
    "CertificateAssociation" : {
      "CertificateArn" : "arn:aws:snowball-device:::certificate/a65ba817f2c5ac9683fc3bc1ae123456"
    },
    "Description" : "s3-snow object API endpoint",
    "DeviceId" : "JIDcc45fa8f-b994-4ada-a821-581bc35d8645",
    "Status" : {
      "State" : "ACTIVE"
    }
  }, {
    "Protocol" : "https",
    "Port" : 443,
    "Host" : "10.0.3.213",
    "CertificateAssociation" : {
      "CertificateArn" : "arn:aws:snowball-device:::certificate/a65ba817f2c5ac9683fc3bc1ae123456"
    },
    "Description" : "s3-snow bucket API endpoint",
    "DeviceId" : "JID4ec68543-d974-465f-b81d-89832dd502db",
    "Status" : {
      "State" : "ACTIVE"
    }
  }, {
    "Protocol" : "https",
    "Port" : 443,
    "Host" : "10.0.3.144",
    "CertificateAssociation" : {
      "CertificateArn" : "arn:aws:snowball-device:::certificate/a65ba817f2c5ac9683fc3bc1ae123456"
    },
    "Description" : "s3-snow object API endpoint",
    "DeviceId" : "JID4ec68543-d974-465f-b81d-89832dd502db",
    "Status" : {
      "State" : "ACTIVE"
    }
  }, {
    "Protocol" : "https",
    "Port" : 443,
    "Host" : "10.0.2.143",
    "CertificateAssociation" : {
      "CertificateArn" : "arn:aws:snowball-device:::certificate/a65ba817f2c5ac9683fc3bc1ae123456"
    },
    "Description" : "s3-snow bucket API endpoint",
    "DeviceId" : "JID6331b8b5-6c63-4e01-b3ca-eab48b5628d2",
    "Status" : {
      "State" : "ACTIVE"
    }
  }, {
    "Protocol" : "https",
    "Port" : 443,
    "Host" : "10.0.3.224",
    "CertificateAssociation" : {
      "CertificateArn" : "arn:aws:snowball-device:::certificate/a65ba817f2c5ac9683fc3bc1ae123456"
    },
    "Description" : "s3-snow object API endpoint",
    "DeviceId" : "JID6331b8b5-6c63-4e01-b3ca-eab48b5628d2",
    "Status" : {
      "State" : "ACTIVE"
    }
  } ]
}

```

## Viewing status of features of Snowball Edge

To list the status of features available on a Snowball Edge use
the `describe-features` command.

`RemoteManagementState` indicates the status of Snowball Edge Device Management and returns one
of the following states:

- `INSTALLED_ONLY` – The feature is installed but not enabled.
- `INSTALLED_AUTOSTART` – The feature is enabled and the device will attempt
  to connect to its AWS Region when it is powered on.
- `NOT_INSTALLED` – The device does not support the feature or was already in
  the field before its launch.

**Usage**

```

snowballEdge describe-features --profile `profile-name`
```

###### Example output of `describe-features` command

```

{
  "RemoteManagementState" : String
}

```

## Setting time servers for Snowball Edge

You can use Snowball Edge Client commands to view the current Network Time Protocol (NTP) configuration and choose a server or peer to provide time. You can use the Snowball Edge Client
commands when the device is in both locked and unlocked states.

It is your responsibility to provide a secure NTP time server. To set which NTP time
servers the device connects to, use the `update-time-servers` command.

### Checking time sources of Snowball Edge

To see which NTP time sources the device are currently connected to, use
the `describe-time-sources` command.

```
snowballEdge describe-time-sources --profile `profile-name`
```

###### Example output of `describe-time-sources` command

```
{
  "Sources" : [ {
    "Address" : "172.31.2.71",
    "State" : "LOST",
    "Type" : "PEER",
    "Stratum" : 10
  }, {
    "Address" : "172.31.3.203",
    "State" : "LOST",
    "Type" : "PEER",
    "Stratum" : 10
  }, {
    "Address" : "172.31.0.178",
    "State" : "LOST",
    "Type" : "PEER",
    "Stratum" : 10
  }, {
    "Address" : "172.31.3.178",
    "State" : "LOST",
    "Type" : "PEER",
    "Stratum" : 10
  }, {
    "Address" : "216.239.35.12",
    "State" : "CURRENT",
    "Type" : "SERVER",
    "Stratum" : 1
  } ]
}
```

The `describe-time-sources` command returns a list of time source states.
Each time source state contains the `Address`, `State`, `Type`,
and `Stratum` fields. Following are the meanings of these fields.

- `Address` – The DNS name / IP address of the time source.
- `State` – The current connection status between the device and
  that time source. There are five possible states:.
  - `CURRENT` – The time source is currently being used to
    synchronize time.
  - `COMBINED` – The time source is combined with the
    current source.
  - `EXCLUDED` – The time source is excluded by the
    combining algorithm.
  - `LOST` – The connection with the time source
    has been lost.
  - `UNACCEPTABLE` – An invalid time source where
    the combining algorithm has deemed to be either a falseticker or
    has too much variability.

- `Type` – An NTP time source can be either a server or a peer.
  Servers can be set by the `update-time-servers` command. Peers can only
  be other Snowball Edge Edge devices in the cluster and are automatically set up when
  the cluster is associated.
- `Stratum` – This field shows the stratum of the source.
  Stratum 1 indicates a source with a locally attached reference clock. A source
  that is synchronized to a stratum 1 source is at stratum 2. A source that is
  synchronized to a stratum 2 source is at stratum 3, and so on..

An NTP time source can either be a server or a peer. A server can be set by the user
with the `update-time-servers` command, whereas a peer could only be other
Snowball Edge Edge devices in the cluster. In the example output, `describe-time-sources`
is called on a Snowball Edge Edge that is in a cluster of 5. The output contains 4 peers
and 1 server. The peers have a stratum of 10 while the server has a stratum of 1;
therefore, the server is selected to be the current time source.

### Updating time servers

Use the `update-time-servers` command and the time server address to configure the Snowball Edge to use an NTP server or peer for NTP.

```
snowballEdge update-time-servers `time-server-address` --profile `profile-name`
```

###### Note

The `update-time-servers` command will override the previous
NTP time servers settings.

###### Example output of `update-time-servers` command

```
Updating time servers now.
```

## Getting a QR code to validate Snowball Edge NFC tags

You can use this command to generate a device-specific QR code for use with the
AWS Snowball Edge Verification App. For more information about NFC validation, see [Validating NFC Tags](data-protection.md#nfc-validation "data-protection.md#nfc-validation").

**Usage**

```
snowballEdge get-app-qr-code --output-file `~/downloads/snowball-qr-code.png` --profile `profile-name`
```

###### Example Output

```
QR code is saved to `~/downloads/snowball-qr-code.png`

```

## Updating MTU size

Use the `update-mtu-size` command to modify the size in bytes of the maximum transmission unit (MTU) of a physical interface of a Snowball Edge device. All virtual network interfaces and direct network interface associated with this physical network interface will be configured with the same MTU size.

###### Note

The minimum MTU size is 1500 bytes and the maximum size is 9216 bytes.

You can use the `describe-device` command to retrieve the physical network interface IDs and current MTU sizes of those interfaces. For more information, see [Viewing status of a Snowball Edge](#client-status "#client-status").

You can use the `descibe-direct-network-interface` and `describe-virtual-network-interface` commands to retrieve the current MTU sizes of those interfaces.

**Usage**

```
snowballEdge update-mtu-size --physical-network-interface-id `physical-network-interface-id` --mtu-size `size-in-bytes` --profile `profile-name`
```

###### Example of `update-mtu-size` output

```

{
    "PhysicalNetworkInterface": {
        "PhysicalNetworkInterfaceId": "s.ni-8c1f891d7f5b87cfe",
        "PhysicalConnectorType": "SFP_PLUS",
        "IpAddressAssignment": "DHCP",
        "IpAddress": "192.0.2.0",
        "Netmask": "255.255.255.0",
        "DefaultGateway": "192.0.2.255",
        "MacAddress": "8A:2r:5G:9p:6Q:4s",
        "MtuSize": "5743"
    }
}

```
