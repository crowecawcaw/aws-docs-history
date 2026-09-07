

# Monitor your WorkSpaces using CloudWatch metrics
<a name="cloudwatch-metrics"></a>

WorkSpaces and Amazon CloudWatch are integrated, so you can gather and analyze performance metrics. You can monitor these metrics using the CloudWatch console, the CloudWatch command line interface, or programmatically using the CloudWatch API. CloudWatch also allows you to set alarms when you reach a specified threshold for a metric.

For more information about using CloudWatch and alarms, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/).

**Prerequisites**  
To get CloudWatch metrics, enable access on port 443 on the `AMAZON` subset in the `us-east-1` Region. For more information, see [IP address and port requirements for WorkSpaces Personal](workspaces-port-requirements.md).

**Topics**
+ [WorkSpaces metrics](#wsp-metrics)
+ [Dimensions for WorkSpaces metrics](#wsp-metric-dimensions)
+ [Monitoring example](#monitoring_example)

## WorkSpaces metrics
<a name="wsp-metrics"></a>

The `AWS/WorkSpaces` namespace includes the following metrics.


| Metric | Description | Dimensions | Statistics | Units | 
| --- | --- | --- | --- | --- | 
| `Available` | The number of WorkSpaces that are healthy. | `DirectoryId`<br />`WorkspaceId`<br />`RunningMode`<br />`Protocol`<br />`ComputeType`<br />`BundleId`<br />`UserName`<br />`ComputerName` | Average, Sum, Maximum, Minimum, Data Samples | Count | 
| `Unhealthy` | The number of WorkSpaces that are unhealthy. | `DirectoryId`<br />`WorkspaceId`<br />`RunningMode`<br />`Protocol`<br />`ComputeType`<br />`BundleId`<br />`UserName`<br />`ComputerName` | Average, Sum, Maximum, Minimum, Data Samples | Count | 
| `Stopped` | The number of WorkSpaces that are stopped. | `DirectoryId`<br />`WorkspaceId`<br />`RunningMode`<br />`Protocol`<br />`ComputeType`<br />`BundleId`<br />`UserName`<br />`ComputerName` | Average, Sum, Maximum, Minimum, Data Samples | Count | 
| `Maintenance` | The number of WorkSpaces that are under maintenance. | `DirectoryId`<br />`WorkspaceId`<br />`RunningMode`<br />`Protocol`<br />`ComputeType`<br />`BundleId`<br />`UserName`<br />`ComputerName` | Average, Sum, Maximum, Minimum, Data Samples | Count | 
| `ConnectionAttempt`1 | The number of connection attempts. | `DirectoryId`<br />`WorkspaceId`<br />`RunningMode`<br />`Protocol`<br />`ComputeType`<br />`BundleId`<br />`UserName`<br />`ComputerName` | Average, Sum, Maximum, Minimum, Data Samples | Count | 
| `ConnectionSuccess`1 | The number of successful connections. | `DirectoryId`<br />`WorkspaceId`<br />`RunningMode`<br />`Protocol`<br />`ComputeType`<br />`BundleId`<br />`UserName`<br />`ComputerName` | Average, Sum, Maximum, Minimum, Data Samples | Count | 
| `ConnectionFailure`1 | The number of failed connections. | `DirectoryId`<br />`WorkspaceId`<br />`RunningMode`<br />`Protocol`<br />`ComputeType`<br />`BundleId`<br />`UserName`<br />`ComputerName` | Average, Sum, Maximum, Minimum, Data Samples | Count | 
| `SessionLaunchTime`1 | The amount of time it takes to initiate a WorkSpaces session. | `DirectoryId`<br />`WorkspaceId`<br />`RunningMode`<br />`Protocol`<br />`ComputeType`<br />`BundleId`<br />`UserName`<br />`ComputerName` | Average, Maximum, Minimum, Data Samples | Seconds | 
| `SessionDisconnect` | The number of sessions that were disconnected. | `DirectoryId`<br />`WorkspaceId`<br />`RunningMode`<br />`Protocol`<br />`ComputeType`<br />`BundleId`<br />`UserName`<br />`ComputerName` | Average, Sum, Maximum, Minimum, Data Samples | Count | 
| `UserConnected` | The number of WorkSpaces that have a user connected. | `DirectoryId`<br />`WorkspaceId`<br />`RunningMode`<br />`Protocol`<br />`ComputeType`<br />`BundleId`<br />`UserName`<br />`ComputerName` | Average, Sum, Maximum, Minimum, Data Samples | Count | 
| `TrustedDeviceValidationAttempt`2 | The number of device authentication signature validation attempts. | `DirectoryId` | Average, Sum, Maximum, Minimum, Data Samples | Count | 
| `TrustedDeviceValidationSuccess`2 | The number of successful device authentication signature validations. | `DirectoryId` | Average, Sum, Maximum, Minimum, Data Samples | Count | 
| `TrustedDeviceValidationFailure`2 | The number of failed device authentication signature validations. | `DirectoryId` | Average, Sum, Maximum, Minimum, Data Samples | Count | 
| `TrustedDeviceCertificateDaysBeforeExpiration` | Days left before the root certificate associated with the directory is expired. | `CertificateId` | Average, Sum, Maximum, Minimum, Data Samples | Count | 
| `CPUUsage` | The percentage of the CPU resource used. | `DirectoryId`<br />`WorkspaceId`<br />`RunningMode`<br />`Protocol`<br />`ComputeType`<br />`BundleId`<br />`UserName`<br />`ComputerName` | Average, Maximum, Minimum | Percentage | 
| `MemoryUsage` | The percentage of the machine memory used. | `DirectoryId`<br />`WorkspaceId`<br />`RunningMode`<br />`Protocol`<br />`ComputeType`<br />`BundleId`<br />`UserName`<br />`ComputerName` | Average, Maximum, Minimum | Percentage | 
| `RootVolumeDiskUsage` | The percentage of the root disk volume used. | `DirectoryId`<br />`WorkspaceId`<br />`RunningMode`<br />`Protocol`<br />`ComputeType`<br />`BundleId`<br />`UserName`<br />`ComputerName` | Average, Maximum, Minimum | Percentage | 
| `UserVolumeDiskUsage` | The percentage of the user disk volume used. | `DirectoryId`<br />`WorkspaceId`<br />`RunningMode`<br />`Protocol`<br />`ComputeType`<br />`BundleId`<br />`UserName`<br />`ComputerName` | Average, Maximum, Minimum | Percentage | 
| `GPUUsage` | The percentage of the GPU resource used on the WorkSpace. | `DirectoryId`<br />`WorkspaceId`<br />`RunningMode`<br />`Protocol`<br />`ComputeType`<br />`BundleId`<br />`UserName`<br />`ComputerName` | Average, Maximum, Minimum | Percentage | 
| `CPUQueueLength` | The number of threads waiting for CPU time on the WorkSpace. | `DirectoryId`<br />`WorkspaceId`<br />`RunningMode`<br />`Protocol`<br />`ComputeType`<br />`BundleId`<br />`UserName`<br />`ComputerName` | Average, Maximum, Minimum | Count | 
| `RootVolumeDiskIOQueueLength` | The number of pending I/O requests waiting to be processed by the root volume disk on the WorkSpace. | `DirectoryId`<br />`WorkspaceId`<br />`RunningMode`<br />`Protocol`<br />`ComputeType`<br />`BundleId`<br />`UserName`<br />`ComputerName` | Average, Maximum, Minimum | Count | 
| `UserVolumeDiskIOQueueLength` | The number of pending I/O requests waiting to be processed by the user volume disk on the WorkSpace. | `DirectoryId`<br />`WorkspaceId`<br />`RunningMode`<br />`Protocol`<br />`ComputeType`<br />`BundleId`<br />`UserName`<br />`ComputerName` | Average, Maximum, Minimum | Count | 
| `MemoryPageHardFaults` | The rate of hard page faults on the WorkSpace. | `DirectoryId`<br />`WorkspaceId`<br />`RunningMode`<br />`Protocol`<br />`ComputeType`<br />`BundleId`<br />`UserName`<br />`ComputerName` | Average, Maximum, Minimum | Count/Second | 
| `PagingFileUsage` | The percentage of the paging file that is currently in use on the WorkSpace. | `DirectoryId`<br />`WorkspaceId`<br />`RunningMode`<br />`Protocol`<br />`ComputeType`<br />`BundleId`<br />`UserName`<br />`ComputerName` | Average, Maximum, Minimum | Percentage | 
| `UpTime` | The time since the last reboot of a WorkSpace. | `DirectoryId`<br />`WorkspaceId`<br />`RunningMode`<br />`Protocol`<br />`ComputeType`<br />`BundleId`<br />`UserName`<br />`ComputerName` | Average, Maximum, Minimum, Data Samples | Seconds | 
| `InSessionLatency` | The round trip time between the WorkSpaces client and the WorkSpace. | `DirectoryId`<br />`WorkspaceId`<br />`RunningMode`<br />`Protocol`<br />`ComputeType`<br />`BundleId`<br />`UserName`<br />`ComputerName` | Average, Maximum, Minimum, Data Samples | Milliseconds | 
| `UDPPacketLossRate`3 | The percentage of UDP packets lost in traffic between the gateway and the client. | `DirectoryId`<br />`WorkspaceId`<br />`RunningMode`<br />`Protocol`<br />`ComputeType`<br />`BundleId`<br />`UserName`<br />`ComputerName` | Average, Maximum, Minimum, Data Samples | Percentage | 
| `TCPRetransmissionRate`4 | The percentage of TCP segments that were retransmitted from the gateway to the client. | `DirectoryId`<br />`WorkspaceId`<br />`RunningMode`<br />`Protocol`<br />`ComputeType`<br />`BundleId`<br />`UserName`<br />`ComputerName` | Average, Maximum, Minimum, Data Samples | Percentage | 
| `Bandwidth`4 | The rate of data transferred from the gateway to the client (outbound). | `DirectoryId`<br />`WorkspaceId`<br />`RunningMode`<br />`Protocol`<br />`ComputeType`<br />`BundleId`<br />`UserName`<br />`ComputerName` | Average, Maximum, Minimum, Data Samples | Kilobits/Second | 
| `BandwidthInbound`4 | The rate of data transferred from the client to the gateway (inbound). | `DirectoryId`<br />`WorkspaceId`<br />`RunningMode`<br />`Protocol`<br />`ComputeType`<br />`BundleId`<br />`UserName`<br />`ComputerName` | Average, Maximum, Minimum, Data Samples | Kilobits/Second | 
| `CongestionWindow`4 | The size of the congestion window at the gateway for traffic flowing to the client. | `DirectoryId`<br />`WorkspaceId`<br />`RunningMode`<br />`Protocol`<br />`ComputeType`<br />`BundleId`<br />`UserName`<br />`ComputerName` | Average, Maximum, Minimum, Data Samples | Bytes | 
| `ConnectionDuration`4 | The duration of the streaming connection. | `DirectoryId`<br />`WorkspaceId`<br />`RunningMode`<br />`Protocol`<br />`ComputeType`<br />`BundleId`<br />`UserName`<br />`ComputerName` | Average, Maximum, Minimum, Data Samples | Seconds | 
| `FramesPerSecond`4 | The number of frames sent per second from the WorkSpace to the client. | `DirectoryId`<br />`WorkspaceId`<br />`RunningMode`<br />`Protocol`<br />`ComputeType`<br />`BundleId`<br />`UserName`<br />`ComputerName` | Average, Maximum, Minimum | Count/Second | 

1 WorkSpaces records metrics on connections made to each WorkSpace. These metrics are emitted after a user has successfully authenticated via the WorkSpaces client and the client then initiates a session connection.

2 If the trusted devices feature is enabled for the directory, Amazon WorkSpaces uses certificate-based authentication to determine whether a device is trusted. When users attempt to access their WorkSpaces, these metrics are emitted to indicate successful or failed trusted device authentication. These metrics are applicable to only Windows and macOS client applications.

3 Direction of measurement depends on the underlying protocol.
+ **On PCoIP**: Measures loss from the client to the gateway.
+ **On DCV**: Measures loss from the gateway to the client. 

4 Available only on DCV.

## Dimensions for WorkSpaces metrics
<a name="wsp-metric-dimensions"></a>

To filter the metric data, use the following dimensions.


| Dimension | Description | 
| --- | --- | 
| `DirectoryId` | Filters the metric data to the WorkSpaces in the specified directory. The form of the directory ID is `d-XXXXXXXXXX`. | 
| `WorkspaceId` | Filters the metric data to the specified WorkSpace. The form of the WorkSpace ID is `ws-XXXXXXXXXX`. | 
| `CertificateId` | Filters the metric data to the specified root certificate associated with the directory. The form of the certificate ID is `wsc-XXXXXXXXX`. | 
| `RunningMode` | Filters the metric data to the WorkSpaces by their running mode. The form of the running mode is AutoStop or AlwaysOn. | 
| `BundleId` | Filters the metric data to the WorkSpaces by the protocol. The form of the bundle is `wsb-XXXXXXXXXX`. | 
| `ComputeType` | Filters the metric data to the WorkSpaces by the compute type.  | 
| `Protocol` | Filters the metric data to the WorkSpaces by the protocol type. | 
| `UserName` | Filters the metric data to the WorkSpaces by the user's name. The `UserName` cannot consist of non-ASCII characters, such as the following:  Accented letters: é, à, ö, ñ, etc. Non-Latin alphabets Symbols: ©️, ®️, €, £, µ, ¥, etc.   | 
| `ComputerName` | Filters the metric data to the specified WorkSpace. See various formats for [WorkSpaces Computer Name]( https://docs.aws.amazon.com/workspaces/latest/adminguide/wsp-directory-identify-computer.html). | 

## Monitoring example
<a name="monitoring_example"></a>

The following example demonstrates how you can use the AWS CLI to respond to a CloudWatch alarm and determine which WorkSpaces in a directory have experienced connection failures.

**To respond to a CloudWatch alarm**

1. Determine which directory the alarm applies to using the [describe-alarms](https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/describe-alarms.html) command.

   ```
   aws cloudwatch describe-alarms --state-value "ALARM"
   
   {
     "MetricAlarms": [
       {
         ...
         "Dimensions": [
           {
             "Name": "DirectoryId",
             "Value": "{{directory_id}}"
           }
         ],
         ...
       }
     ]
   }
   ```

1. Get the list of WorkSpaces in the specified directory using the [describe-workspaces](https://docs.aws.amazon.com/cli/latest/reference/workspaces/describe-workspaces.html) command.

   ```
   aws workspaces describe-workspaces --directory-id {{directory_id}}
   
   {
     "Workspaces": [
       {
         ...
         "WorkspaceId": "{{workspace1_id}}",
         ...
       },
       {
         ...
         "WorkspaceId": "{{workspace2_id}}",
         ...
       },
       {
         ...
         "WorkspaceId": "{{workspace3_id}}",
         ...
       }
     ]
   }
   ```

1. Get the CloudWatch metrics for each WorkSpace in the directory using the [get-metric-statistics](https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/get-metric-statistics.html) command.

   ```
   aws cloudwatch get-metric-statistics \
   --namespace AWS/WorkSpaces \
   --metric-name ConnectionFailure \
   --start-time 2015-04-27T00:00:00Z \
   --end-time 2015-04-28T00:00:00Z \
   --period 3600 \
   --statistics Sum \
   --dimensions "Name=WorkspaceId,Value={{workspace_id}}"
   
   {
     "Datapoints" : [
       {
         "Timestamp": "2015-04-27T00:18:00Z",
         "Sum": 1.0,
         "Unit": "Count"
       },
       {
         "Timestamp": "2014-04-27T01:18:00Z",
         "Sum": 0.0,
         "Unit": "Count"
       }
     ],
     "Label" : "ConnectionFailure"
   }
   ```