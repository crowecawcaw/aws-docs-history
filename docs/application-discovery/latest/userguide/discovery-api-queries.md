AWS Application Discovery Service is no longer open to new customers. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](application-discovery-service-availability-change.md "application-discovery-service-availability-change.md").

# Using the Application Discovery Service API to query discovered configuration

items

A _configuration item_ is an IT asset that was discovered
in your data center by an agent or by an import. When you use
AWS Application Discovery Service (Application Discovery Service), you use the API to specify filters and query specific configuration
items for server, application, process, and connection assets. For information about the API,
see [Application Discovery Service API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

The tables in the following sections list the available input filters and output sorting
options for two Application Discovery Service actions:

- `DescribeConfigurations`
- `ListConfigurations`
  The filtering and sorting options are organized by the type of asset to which apply (server,
  application, process, or connection).

###### Important

Results returned by `DescribeConfigurations`, `ListConfigurations`,
and `StartExportTask` might not contain recent updates. For more information, see
[Eventual consistency in the AWS Application Discovery Service API](#eventual-consistency "#eventual-consistency").

## Using the `DescribeConfigurations`

action

The `DescribeConfigurations`action retrieves attributes for a list of
configuration IDs. All the supplied IDs must be for the same asset type (server, application,
process, or connection). Output fields are specific to the asset type selected. For example,
the output for a server configuration item includes a list of attributes about the server,
such as host name, operating system, and number of network cards. For more information about
command syntax, see [DescribeConfigurations](../APIReference/API_DescribeConfigurations.md "../APIReference/API_DescribeConfigurations.md").

The `DescribeConfigurations`action does not support filtering.

###### Output fields for `DescribeConfigurations`

The following tables, organized by asset type, list the supported output fields of the
`DescribeConfigurations`action. The ones marked as mandatory are always present
in the output.

**Server assets**

| Field                                              | Mandatory |
| -------------------------------------------------- | --------- |
| `server.agentId`                                   |           |
| `server.applications`                              |           |
| `server.applications.hasMoreValues`                |           |
| `server.configurationId`                           | x         |
| `server.cpuType`                                   |           |
| `server.hostName`                                  |           |
| `server.hypervisor`                                |           |
| `server.networkInterfaceInfo`                      |           |
| `server.networkInterfaceInfo.hasMoreValues`        |           |
| `server.osName`                                    |           |
| `server.osVersion`                                 |           |
| `server.tags`                                      |           |
| `server.tags.hasMoreValues`                        |           |
| `server.timeOfCreation`                            | x         |
| `server.type`                                      |           |
| `server.performance.avgCpuUsagePct`                |           |
| `server.performance.avgDiskReadIOPS`               |           |
| `server.performance.avgDiskReadsPerSecondInKB`     |           |
| `server.performance.avgDiskWriteIOPS`              |           |
| `server.performance.avgDiskWritesPerSecondInKB`    |           |
| `server.performance.avgFreeRAMInKB`                |           |
| `server.performance.avgNetworkReadsPerSecondInKB`  |           |
| `server.performance.avgNetworkWritesPerSecondInKB` |           |
| `server.performance.maxCpuUsagePct`                |           |
| `server.performance.maxDiskReadIOPS`               |           |
| `server.performance.maxDiskReadsPerSecondInKB`     |           |
| `server.performance.maxDiskWriteIOPS`              |           |
| `server.performance.maxDiskWritesPerSecondInKB`    |           |
| `server.performance.maxNetworkReadsPerSecondInKB`  |           |
| `server.performance.maxNetworkWritesPerSecondInKB` |           |
| `server.performance.minFreeRAMInKB`                |           |
| `server.performance.numCores`                      |           |
| `server.performance.numCpus`                       |           |
| `server.performance.numDisks`                      |           |
| `server.performance.numNetworkCards`               |           |
| `server.performance.totalRAMInKB`                  |           |

**Process assets**

| Field                     | Mandatory |
| ------------------------- | --------- |
| `process.commandLine`     |           |
| `process.configurationId` | x         |
| `process.name`            |           |
| `process.path`            |           |
| `process.timeOfCreation`  | x         |

**Application assets**

| Field                          | Mandatory |
| ------------------------------ | --------- |
| `application.configurationId`  | x         |
| `application.description`      |           |
| `application.lastModifiedTime` | x         |
| `application.name`             | x         |
| `application.serverCount`      | x         |
| `application.timeOfCreation`   | x         |

## Using the `ListConfigurations` action

The `ListConfigurations`action retrieves a list of configuration items
according to the criteria that you specify in a filter. For more information about command
syntax, see [ListConfigurations](../APIReference/API_ListConfigurations.md "../APIReference/API_ListConfigurations.md").

###### Output fields for

`ListConfigurations`

The following tables, organized by asset type, list the supported output fields of the
`ListConfigurations`action. The ones marked as mandatory are always present in
the output.

**Server assets**

| Field                    | Mandatory |
| ------------------------ | --------- |
| `server.configurationId` | x         |
| `server.agentId`         |           |
| `server.hostName`        |           |
| `server.osName`          |           |
| `server.osVersion`       |           |
| `server.timeOfCreation`  | x         |
| `server.type`            |           |

**Process assets**

| Field                     | Mandatory |
| ------------------------- | --------- |
| `process.commandLine`     |           |
| `process.configurationId` | x         |
| `process.name`            |           |
| `process.path`            |           |
| `process.timeOfCreation`  | x         |
| `server.agentId`          |           |
| `server.configurationId`  | x         |

**Application assets**

| Field                          | Mandatory |
| ------------------------------ | --------- |
| `application.configurationId`  | x         |
| `application.description`      |           |
| `application.name`             | x         |
| `application.serverCount`      | x         |
| `application.timeOfCreation`   | x         |
| `application.lastModifiedTime` | x         |

**Connection assets**

| Field                                | Mandatory |
| ------------------------------------ | --------- |
| `connection.destinationIp`           | x         |
| `connection.destinationPort`         | x         |
| `connection.ipVersion`               | x         |
| `connection.latestTimestamp`         | x         |
| `connection.occurrence`              | x         |
| `connection.sourceIp`                | x         |
| `connection.transportProtocol`       |           |
| `destinationProcess.configurationId` |           |
| `destinationProcess.name`            |           |
| `destinationServer.configurationId`  |           |
| `destinationServer.hostName`         |           |
| `sourceProcess.configurationId`      |           |
| `sourceProcess.name`                 |           |
| `sourceServer.configurationId`       |           |
| `sourceServer.hostName`              |           |

###### Supported filters for

`ListConfigurations`

The following tables, organized by asset type, list the supported filters for the
`ListConfigurations`action. Filters and values are in a key/value relationship
defined by one of the supported logical conditions. You can sort the output of the indicated
filters.

**Server assets**

| Filter                                          | Supported conditions                                                     | Supported values                                                                                                     | Supported sorting |
| ----------------------------------------------- | ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------- | ----------------- |
| `server.configurationId`                        | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE                                 | • Any valid server configuration ID                                                                                  | None              |
| `server.hostName`                               | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE<br>• CONTAINS<br>• NOT_CONTAINS | • String                                                                                                             | • ASC<br>• DESC   |
| `server.osName`                                 | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE<br>• CONTAINS<br>• NOT_CONTAINS | • String                                                                                                             | • ASC<br>• DESC   |
| `server.osVersion`                              | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE<br>• CONTAINS<br>• NOT_CONTAINS | • String                                                                                                             | • ASC<br>• DESC   |
| `server.agentId`                                | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE                                 | • String                                                                                                             | None              |
| `server.connectorId`                            | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE                                 | • String                                                                                                             | None              |
| `server.type`                                   | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE                                 | String with one of the following values:<br>• EC2<br>• OTHER<br>• VMWARE_VM<br>• VMWARE_HOST<br>• VMWARE_VM_TEMPLATE | None              |
| `server.vmWareInfo.morefId`                     | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE<br>• CONTAINS<br>• NOT_CONTAINS | • String                                                                                                             | None              |
| `server.vmWareInfo.vcenterId`                   | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE<br>• CONTAINS<br>• NOT_CONTAINS | • String                                                                                                             | None              |
| `server.vmWareInfo.hostId`                      | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE<br>• CONTAINS<br>• NOT_CONTAINS | • String                                                                                                             | None              |
| `server.networkInterfaceInfo.portGroupId`       | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE<br>• CONTAINS<br>• NOT_CONTAINS | • String                                                                                                             | None              |
| `server.networkInterfaceInfo.portGroupName`     | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE<br>• CONTAINS<br>• NOT_CONTAINS | • String                                                                                                             | None              |
| `server.networkInterfaceInfo.virtualSwitchName` | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE<br>• CONTAINS<br>• NOT_CONTAINS | • String                                                                                                             | None              |
| `server.networkInterfaceInfo.ipAddress`         | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE<br>• CONTAINS<br>• NOT_CONTAINS | • String                                                                                                             | None              |
| `server.networkInterfaceInfo.macAddress`        | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE<br>• CONTAINS<br>• NOT_CONTAINS | • String                                                                                                             | None              |
| `server.performance.avgCpuUsagePct`             | • GE<br>• LE<br>• GT<br>• LT                                             | • Percentage                                                                                                         | None              |
| `server.performance.totalDiskFreeSizeInKB`      | • GE<br>• LE<br>• GT<br>• LT                                             | • Double                                                                                                             | None              |
| `server.performance.avgFreeRAMInKB`             | • GE<br>• LE<br>• GT<br>• LT                                             | • Double                                                                                                             | None              |
| `server.tag.value`                              | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE<br>• CONTAINS<br>• NOT_CONTAINS | • String                                                                                                             | None              |
| `server.tag.key`                                | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE<br>• CONTAINS<br>• NOT_CONTAINS | • String                                                                                                             | None              |
| `server.application.name`                       | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE<br>• CONTAINS<br>• NOT_CONTAINS | • String                                                                                                             | None              |
| `server.application.description`                | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE<br>• CONTAINS<br>• NOT_CONTAINS | • String                                                                                                             | None              |
| `server.application.configurationId`            | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE                                 | • Any valid application configuration ID                                                                             | None              |
| `server.process.configurationId`                | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE                                 | • ProcessId                                                                                                          | None              |
| `server.process.name`                           | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE<br>• CONTAINS<br>• NOT_CONTAINS | • String                                                                                                             | None              |
| `server.process.commandLine`                    | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE<br>• CONTAINS<br>• NOT_CONTAINS | • String                                                                                                             | None              |

**Application assets**

| Filter                         | Supported conditions                                                     | Supported values         | Supported sorting |
| ------------------------------ | ------------------------------------------------------------------------ | ------------------------ | ----------------- |
| `application.configurationId`  | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE                                 | • ApplicationId          | None              |
| `application.name`             | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE<br>• CONTAINS<br>• NOT_CONTAINS | • String                 | • ASC<br>• DESC   |
| `application.description`      | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE<br>• CONTAINS<br>• NOT_CONTAINS | • String                 | • ASC<br>• DESC   |
| `application.serverCount`      | Filtering not supported.                                                 | Filtering not supported. | • ASC<br>• DESC   |
| `application.timeOfCreation`   | Filtering not supported.                                                 | Filtering not supported. | • ASC<br>• DESC   |
| `application.lastModifiedTime` | Filtering not supported.                                                 | Filtering not supported. | • ASC<br>• DESC   |
| `server.configurationId`       | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE                                 | • ServerId               | None              |

**Process assets**

| Filter                    | Supported conditions                                                     | Supported values | Supported sorting |
| ------------------------- | ------------------------------------------------------------------------ | ---------------- | ----------------- |
| `process.configurationId` | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE                                 | • ProcessId      |                   |
| `process.name`            | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE<br>• CONTAINS<br>• NOT_CONTAINS | • String         | • ASC<br>• DESC   |
| `process.commandLine`     | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE<br>• CONTAINS<br>• NOT_CONTAINS | • String         | • ASC<br>• DESC   |
| `server.configurationId`  | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE                                 | • ServerId       |                   |
| `server.hostName`         | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE<br>• CONTAINS<br>• NOT_CONTAINS | • String         | • ASC<br>• DESC   |
| `server.osName`           | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE<br>• CONTAINS<br>• NOT_CONTAINS | • String         | • ASC<br>• DESC   |
| `server.osVersion`        | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE<br>• CONTAINS<br>• NOT_CONTAINS | • String         | • ASC<br>• DESC   |
| `server.agentId`          | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE<br>• CONTAINS<br>• NOT_CONTAINS | • String         |                   |

**Connection assets**

| Filter                               | Supported conditions                                                     | Supported values | Supported sorting |
| ------------------------------------ | ------------------------------------------------------------------------ | ---------------- | ----------------- |
| `connection.sourceIp`                | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE<br>• CONTAINS<br>• NOT_CONTAINS | • IP             | • ASC<br>• DESC   |
| `connection.destinationIp`           | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE<br>• CONTAINS<br>• NOT_CONTAINS | • IP             | • ASC<br>• DESC   |
| `connection.destinationPort`         | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE                                 | • Integer        | • ASC<br>• DESC   |
| `sourceServer.configurationId`       | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE                                 | • ServerId       |                   |
| `sourceServer.hostName`              | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE<br>• CONTAINS<br>• NOT_CONTAINS | • String         | • ASC<br>• DESC   |
| `destinationServer.osName`           | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE<br>• CONTAINS<br>• NOT_CONTAINS | • String         | • ASC<br>• DESC   |
| `destinationServer.osVersion`        | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE<br>• CONTAINS<br>• NOT_CONTAINS | • String         | • ASC<br>• DESC   |
| `destinationServer.agentId`          | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE<br>• CONTAINS<br>• NOT_CONTAINS | • String         |                   |
| `sourceProcess.configurationId`      | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE                                 | • ProcessId      |                   |
| `sourceProcess.name`                 | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE<br>• CONTAINS<br>• NOT_CONTAINS | • String         | • ASC<br>• DESC   |
| `sourceProcess.commandLine`          | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE<br>• CONTAINS<br>• NOT_CONTAINS | • String         | • ASC<br>• DESC   |
| `destinationProcess.configurationId` | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE                                 | • ProcessId      |                   |
| `destinationProcess.name`            | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE<br>• CONTAINS<br>• NOT_CONTAINS | • String         | • ASC<br>• DESC   |
| `destinationprocess.commandLine`     | • EQUALS<br>• NOT_EQUALS<br>• EQ<br>• NE<br>• CONTAINS<br>• NOT_CONTAINS | • String         | • ASC<br>• DESC   |

## Eventual consistency in the AWS Application Discovery Service API

The following update operations are eventually consistent. Updates might not be
immediately visible to the read operations [StartExportTask](../APIReference/API_StartExportTask.md "../APIReference/API_StartExportTask.md"), [DescribeConfigurations](../APIReference/API_DescribeConfigurations.md "../APIReference/API_DescribeConfigurations.md"), and [ListConfigurations](../APIReference/API_ListConfigurations.md "../APIReference/API_ListConfigurations.md").

- [AssociateConfigurationItemsToApplication](../APIReference/API_AssociateConfigurationItemsToApplication.md "../APIReference/API_AssociateConfigurationItemsToApplication.md")
- [CreateTags](../APIReference/API_CreateTags.md "../APIReference/API_CreateTags.md")
- [DeleteApplications](../APIReference/API_DeleteApplications.md "../APIReference/API_DeleteApplications.md")
- [DeleteTags](../APIReference/API_DeleteTags.md "../APIReference/API_DeleteTags.md")
- [DescribeBatchDeleteConfigurationTask](../APIReference/API_DescribeBatchDeleteConfigurationTask.md "../APIReference/API_DescribeBatchDeleteConfigurationTask.md")
- [DescribeImportTasks](../APIReference/API_DescribeImportTasks.md "../APIReference/API_DescribeImportTasks.md")
- [DisassociateConfigurationItemsFromApplication](../APIReference/API_DisassociateConfigurationItemsFromApplication.md "../APIReference/API_DisassociateConfigurationItemsFromApplication.md")
- [UpdateApplication](../APIReference/API_UpdateApplication.md "../APIReference/API_UpdateApplication.md")

Suggestions for managing eventual consistency:

- When you invoke the read operations [StartExportTask](../APIReference/API_StartExportTask.md "../APIReference/API_StartExportTask.md"), [DescribeConfigurations](../APIReference/API_DescribeConfigurations.md "../APIReference/API_DescribeConfigurations.md"), or [ListConfigurations](../APIReference/API_ListConfigurations.md "../APIReference/API_ListConfigurations.md") (or their corresponding AWS CLI commands), use an
  exponential backoff algorithm to allow enough time for any previous update operation to
  propagate through the system. To do this, run the read operation repeatedly, starting
  with a two-second wait time, and increasing gradually up to five minutes of wait
  time.
- Add wait time between subsequent operations, even if an update operation returns a
  200 - OK response. Apply an exponential backoff algorithm starting with a couple of
  seconds of wait time, and increase gradually up to about five minutes of wait
  time.
