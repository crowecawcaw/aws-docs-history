# Getting Started with File Server Resource Manager

You can enable File Server Resource Manager (FSRM) when creating a new Amazon FSx for Windows File Server file system, or you can update your existing file system to enable FSRM.

FSRM is supported only on Amazon FSx for Windows File Server file systems with SSD storage and a throughput capacity of 128 MB/s or greater. You can update the storage type to SSD and modify the throughput capacity at any time after you create the file system. For more information, see [Updating the storage type of a FSx for Windows file system](updating-storage-type.md "updating-storage-type.md") and [Managing throughput capacity](managing-throughput-capacity.md "managing-throughput-capacity.md").

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/")
2. On the dashboard, choose **Create file system** to start the file system creation wizard.
3. Choose **Amazon FSx for Windows File Server** and then choose **Next**.
4. Select the **Standard Create** option
5. Provide the required information
6. Open the **File Server Resource Manager** block, choose **Enabled**.
7. For **Event log destination**, choose one of the following options:
   - **CloudWatch Logs** - Select a CloudWatch Logs log group to receive FSRM event logs. The name of the CloudWatch Logs log group must begin with the `'/aws/fsx/'` prefix.
   - **Kinesis Data Firehose** - Select a Kinesis Data Firehose delivery stream to receive FSRM event logs

8. Complete the remaining sections and choose **Create file system**.
   To enable FSRM when creating an FSx for Windows File Server file system, use the AWS CLI command `create-file-system`. Include the following FSRM configuration in the `--windows-configuration` parameter:

- `FsrmServiceEnabled` - Set to `true`
- `EventLogDestination` - The Amazon Resource Name (ARN) that specifies the destination of the FSRM event logs. Can be a CloudWatch Logs log group ARN or Kinesis Data Firehose delivery stream ARN.

```
aws fsx create-file-system \
        --file-system-type WINDOWS \
        --storage-capacity 300 \
        --storage-type SSD \
        --subnet-ids subnet-0123456789abcdef0 \
        --windows-configuration "ThroughputCapacity=128,WindowsFsrmConfiguration={FsrmServiceEnabled=true,EventLogDestination=arn:aws:logs:us-east-1:123456789012:log-group:/aws/fsx/fsrm}"
```

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. Navigate to **File systems** and choose the Windows file system that you want to modify.
3. Choose the **Administration** tab.
4. In the **File Server Resource Manager** section, choose **Manage**.
5. Make your required changes:
   - To change the event log destination, select a different CloudWatch Logs log group or Kinesis Data Firehose delivery stream
   - To enable FSRM, choose **Enabled**
   - To disable FSRM, choose **Disabled**

###### Important

Multi-AZ file systems will experience automatic failover and failback events during this process, while Single-AZ file systems will experience a brief period of unavailability. 6. Choose **Save**.
You can monitor the update progress on the File systems detail page, in the **Updates** tab.

To enable and disable FSRM on an existing FSx for Windows File Server file system, use the AWS CLI command `update-file-system`.

### Enabling FSRM

To enable FSRM, include the following FSRM configuration in the `--windows-configuration` parameter:

- `FsrmServiceEnabled` - Set to `true`
- `EventLogDestination` - The Amazon Resource Name (ARN) that specifies the destination of the FSRM event logs. Can be a CloudWatch Logs log group ARN or Kinesis Data Firehose delivery stream ARN.

```
aws fsx update-file-system \
    --file-system-id fs-0123456789abcdef0 \
    --windows-configuration FsrmConfiguration='{FsrmServiceEnabled=true,EventLogDestination=”arn:aws:logs:us-east-1:123456789012:log-group:/aws/fsx/fsrm”}'
```

### Disabling FSRM

To disable FSRM:

```
aws fsx update-file-system \
    --file-system-id fs-0123456789abcdef0 \
    --windows-configuration FsrmConfiguration='{FsrmServiceEnabled=false}'
```

###### Important

Multi-AZ file systems will experience automatic failover and failback events during this process, while Single-AZ file systems will experience a brief period of unavailability.

## FSx remote PowerShell

To configure and use FSRM features, you must use the Amazon FSx CLI for remote management on PowerShell. For information, see [Starting an Amazon FSx remote PowerShell session](start-remote-powershell-session.md "start-remote-powershell-session.md").
