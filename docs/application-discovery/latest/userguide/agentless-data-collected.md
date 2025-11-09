AWS Application Discovery Service is no longer open to new customers. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](application-discovery-service-availability-change.md "application-discovery-service-availability-change.md").

# Collecting data with the Discovery Connector

###### Important

We recommend that customers who are currently using Discovery Connector transition to the new
Agentless Collector. Starting November 17, 2025, AWS Application Discovery Service will stop
accepting new data from Discovery Connectors. For more information, see [Discovery Connector](appendix.md "appendix.md").

The Discovery Connector collects information about your VMware vCenter Server hosts and VMs.
However, you can capture this data only if VMware vCenter Server tools are installed. To
make sure the AWS account you are using has the required permission for this task, see
[AWS managed policies for AWS Application Discovery Service](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

Following, you can find an inventory of the information collected by the
Discovery Connector.

###### Table legend for Discovery Connector collected data:

- Collected data is in measurements of kilobytes (KB) unless stated
  otherwise.
- Equivalent data in the Migration Hub console is reported in megabytes (MB).
- Data fields denoted with an asterisk (\*) are only available in the .csv files
  that are produced from the connector's API export function.
- The polling period is in intervals of approximately 60 minutes.
- Data fields denoted with a double asterisk (\*\*) currently return a _null_ value.

| Data field                      | Description                                                                                                                                                                   |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| applicationConfigurationId\*    | ID of the migration application the VM is grouped under                                                                                                                       |
| avgCpuUsagePct                  | Average percentage of CPU usage over polling period                                                                                                                           |
| avgDiskBytesReadPerSecond       | Average number of bytes read from disk over polling period                                                                                                                    |
| avgDiskBytesWrittenPerSecond    | Average number of bytes written to disk over polling period                                                                                                                   |
| avgDiskReadOpsPerSecond\*\*     | Average number of read I/O operations per second null                                                                                                                         |
| avgDiskWriteOpsPerSecond\*\*    | Average number of write I/O operations per second                                                                                                                             |
| avgFreeRAM                      | Average free RAM expressed in MB                                                                                                                                              |
| avgNetworkBytesReadPerSecond    | Average amount of throughput of bytes read per second                                                                                                                         |
| avgNetworkBytesWrittenPerSecond | Average amount of throughput of bytes written per second                                                                                                                      |
| configId                        | Application Discovery Service assigned ID to the discovered VM                                                                                                                |
| configType                      | Type of resource discovered                                                                                                                                                   |
| connectorId                     | ID of the Discovery Connector virtual appliance                                                                                                                               |
| cpuType                         | vCPU for a VM, actual model for a host                                                                                                                                        |
| datacenterId                    | ID of the vCenter                                                                                                                                                             |
| hostId\*                        | ID of the VM host                                                                                                                                                             |
| hostName                        | Name of host running the virtualization software                                                                                                                              |
| hypervisor                      | Type of hypervisor                                                                                                                                                            |
| id                              | ID of server                                                                                                                                                                  |
| lastModifiedTimeStamp\*         | Latest date and time of data collection before data export                                                                                                                    |
| macAddress                      | MAC address of the VM                                                                                                                                                         |
| manufacturer                    | Maker of the virtualization software                                                                                                                                          |
| maxCpuUsagePct                  | Max. percentage of CPU usage during polling period                                                                                                                            |
| maxDiskBytesReadPerSecond       | Max. number of bytes read from disk over polling period                                                                                                                       |
| maxDiskBytesWrittenPerSecond    | Max. number of bytes written to disk over polling period                                                                                                                      |
| maxDiskReadOpsPerSecond\*\*     | Max. number of read I/O operations per second                                                                                                                                 |
| maxDiskWriteOpsPerSecond\*\*    | Max. number of write I/O operations per second                                                                                                                                |
| maxNetworkBytesReadPerSecond    | Max. amount of throughput of bytes read per second                                                                                                                            |
| maxNetworkBytesWrittenPerSecond | Max. amount of throughput of bytes written per second                                                                                                                         |
| memoryReservation\*             | Limit to avoid overcommitment of memory on VM                                                                                                                                 |
| moRefId                         | Unique vCenter Managed Object Reference ID                                                                                                                                    |
| name\*                          | Name of VM or network (user specified)                                                                                                                                        |
| numCores                        | Number of independent processing units within CPU                                                                                                                             |
| numCpus                         | Number of central processing units on VM                                                                                                                                      |
| numDisks\*\*                    | Number of disks on VM                                                                                                                                                         |
| numNetworkCards\*\*             | Number of network cards on VM                                                                                                                                                 |
| osName                          | Operating system name on VM                                                                                                                                                   |
| osVersion                       | Operating system version on VM                                                                                                                                                |
| portGroupId\*                   | ID of group of member ports of VLAN                                                                                                                                           |
| portGroupName\*                 | Name of group of member ports of VLAN                                                                                                                                         |
| powerState\*                    | Status of power                                                                                                                                                               |
| serverId                        | Application Discovery Service assigned ID to the discovered VM                                                                                                                |
| smBiosId\*                      | ID/version of the system management BIOS                                                                                                                                      |
| state\*                         | Status of the Discovery Connector virtual appliance                                                                                                                           |
| toolsStatus                     | Operational state of VMware tools (See [Sorting data collectors in the AWS Migration Hub<br>console](sort-data-collectors.md "sort-data-collectors.md") for a complete list.) |
| totalDiskSize                   | Total capacity of disk expressed in MB                                                                                                                                        |
| totalRAM                        | Total amount of RAM available on VM in MB                                                                                                                                     |
| type                            | Type of host                                                                                                                                                                  |
| vCenterId                       | Unique ID number of a VM                                                                                                                                                      |
| vCenterName\*                   | Name of the vCenter host                                                                                                                                                      |
| virtualSwitchName\*             | Name of the virtual switch                                                                                                                                                    |
| vmFolderPath                    | Directory path of VM files                                                                                                                                                    |
| vmName                          | Name of the virtual machine                                                                                                                                                   |

## Collect Discovery Connector data

After you deploy and configure the Discovery Connector in your VMware environment, you can
restart data collections if it stops. You can start or stop data collection through
the console or by making API calls through the AWS CLI. Both of these methods are
described in the following procedures.

Using the Migration Hub Console
The following procedure shows how to start or stop the Discovery Connector data
collection process, on the **Data Collectors** page of
the Migration Hub console.

###### To start or stop data collection

1. In the navigation pane, choose **Data
   Collectors**.
2. Choose the **Connectors** tab.
3. Select the check box of the connector you want to start or
   stop.
4. Choose **Start data collection** or
   **Stop data collection**.

###### Note

If you don’t see inventory information after starting data
collection with the connector, confirm that you have registered the
connector with your vCenter Server.

Using the AWS CLI
To start the Discovery Connector data collection process from the AWS CLI, the
AWS CLI must first be installed in your environment, and then you must set
the CLI to use your selected [Migration Hub home
Region](../../../migrationhub/latest/ug/home-region.md "../../../migrationhub/latest/ug/home-region.md").

###### To install the AWS CLI and start data collection

1. Install the AWS CLI for your operating system (Linux, macOS, or
   Windows). See the [AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md") for instructions.
2. Open the Command prompt (Windows) or Terminal (Linux or
   macOS).
   1. Type `aws configure` and press
      Enter.
   2. Enter your AWS Access Key ID and AWS Secret Access
      Key.
   3. Enter your home Region for the Default Region Name.
      For example, `us-west-2`.
   4. Enter `text` for Default Output
      Format.

3. To find the ID of the connector you want to start or stop data
   collection for, type the following command to see the
   connector's ID:

```
aws discovery describe-agents --filters condition=EQUALS,name=hostName,values=connector
```

4. To start data collection by the connector, type the following
   command:

```
aws discovery start-data-collection-by-agent-ids --agent-ids `<connector ID>`
```

###### Note

If you don’t see inventory information after starting data
collection with the connector, confirm that you have
registered the connector with your vCenter Server.

To stop data collection by the connector, type the following
command:

```
aws discovery stop-data-collection-by-agent-ids --agent-ids `<connector ID>`
```
