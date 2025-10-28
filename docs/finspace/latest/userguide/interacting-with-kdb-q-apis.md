After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# FinSpace q API reference

FinSpace provides a set of q APIs that you can use to interact with resources in
your Managed kdb environment. These APIs reside in the _.aws Q_
namespace.

## Ingestion APIs

**Function**:
`.aws.create_changeset[db_name;change_requests]`

Creates a new changeset in the specified database.

Parameters

`db_name`

**Description** – The name of the FinSpace kdb database where you can create
Managed kdb Insights changesets. This must be the same database that you
used when you created the RDB cluster.

**Type** –
String

**Required** –
Yes

`change_requests`

**Description** – A
q table representing the list of change requests for the
Managed kdb Insights changesets. The table has 3 columns :

- `input_path` – The input path of the local file system directory or file to
  ingest as a Managed kdb changeset.
- `database_path` – The target database destination path of the Managed kdb
  changeset. This column maps to the `databasePath`
  field of the [CreateKxChangeset](../management-api/API_CreateKxChangeset.md "../management-api/API_CreateKxChangeset.md") API.
- `change_type` – The type of the Managed kdb changeset. It can be either
  `PUT` or `DELETE`. This column maps
  to the `changeType` field of the [CreateKxChangeset](../management-api/API_CreateKxChangeset.md "../management-api/API_CreateKxChangeset.md") API.

**Type** – Q
table

**Required** – Yes

Result
Returns the `changeset_id` of the created Managed kdb
changeset, along with its current status.

**Function**:
`.aws.get_changeset[db_name;changeset_id]`

Retrieves information about a specific changeset.

Parameters

`db_name`

**Description** – The name of the FinSpace kdb database where you can create Managed
kdb changesets. This must be the same database that you used when
you created the RDB cluster.

**Type** –
String

**Required** –
Yes

`changeset_id`

**Description** – The identifier of the Managed kdb changeset.

**Type** – string

**Required** – Yes

Result
Returns the `changeset_id` and the status of the Managed kdb
changeset.

**Function**:
`.aws.get_latest_sym_file[db_name;destination_path]`

Retrieves the latest sym file from the specified database.

Parameters

`db_name`

**Description** – The name of the FinSpace kdb database where you can create Managed
kdb changesets. This must be the same database that you used when
you created the RDB cluster.

**Type** –
String

**Required** –
Yes

`destination_path`

**Description** – The directory in the local filesystem scratch location where you want to download the symfile.

**Type** – String

**Required** – Yes

Result
Returns the destination path where the sym file was copied to.

**Function**:
`.aws.s3.get_object[source_s3_path;destination_disk_path]`

Copies Amazon S3 object from your S3 bucket account into a local disk location in a kdb cluster.

Permissions
For this function, the `executionRole` of the cluster
must have the `s3:GetObject` permission to access the
object and `kms:Decrypt` permission for the key that you
use to encrypt the S3 bucket.

Parameters

`source_s3_path`

**Description** – The
source path in the customer account from where you want to
copy an S3 object. This can be S3 object ARN or S3 URI
path.

**Type** –
String

**Required** –
Yes

`destination_disk_path`

**Description** – The local disk location to copy the S3 object to.

**Type** –
String

**Required** –
Yes

Example
The following code is an example request to copy S3 object to a
local disk.

```
 q) .aws.s3.get_object["s3://customer-bucket/reference_data.csv"; "/opt/kx/app/shared/VolumeName/common/"]
```

Result
Returns a table of S3 object path and local directory disk
location.

Sample response

```
s3ObjectPath                                containerFileDestinationPath
--------------------------------------------------------------------------
s3://data-bucket/data.csv                   "/opt/kx/app/shared/test/common/data.csv"
```

Sample response for retrieving multiple files

```
.aws.copy_database_files["DATABASE_NAME"; "DESTINATION_PATH"; "PARTITION_NAME/*"; ""]
database_name| "DATABASE_NAME"
changeset_id | "CHANGESET_ID"
result_paths | ("DESTINATION_PATH/PARTITION_NAME/file1"; "DESTINATION_PATH/PARTITION_NAME/file2"...)
```

**Function**:
`.aws.copy_database_files[database_name, destination_path, db_path,
 changeset_id]`

Retrieves a specific file from a specific version of the database. The
`changeset_id` provides the version of the database from where
you want to retrieve the file.

Parameters

`database_name`

**Description** – The name of the FinSpace kdb database where you can create Managed
kdb changesets. This must be the same database that you used when
you created the RDB cluster.

**Type** –
String

**Required** –
Yes

`destination_path`

**Description** – The
directory in the local filesystem scratch location where you
want to download one or more files.

**Type** – String

**Required** – Yes

`db_path`

**Description** – The
path within the database directory of the file you want to
retrieve. This can be a single file or a path ending with the
wildcard "\*” to retrieve multiple files. Following are a few
example values for `db_path`.

- `sym` retrieves the file named **sym** located in the root
  directory of the database.
- `sym*` retrieves all files starting with
  **sym** for a database.
  For example, **sym1** and
  **sym2**.
- `2022.01.02/*` retrieves all files within
  the directory **2022.01.02**. For example, **2022.01.02/col1**, **2022.01.02/col2**, etc.
  Alternatively, you can use `2022.01.02/` to
  achieve the same result.
- `2022.05.*` retrieves all files from May
  2022 within a date-partitioned database. For example, all files from **2022.05.01**, **2022.05.02**, etc.

**Type** – String

**Required** – Yes

`changeset_id`

**Description** – The
identifier of the Managed kdb changeset. You can specify an
empty string `""` to use the latest
changeset.

**Type** – String

**Required** – Yes

Result
Returns the destination path where the files were copied to, along
with the `database_name` and `changeset_id`
used.

Sample response for retrieving a file

```
.aws.copy_database_files["DATABASE_NAME"; "DESTINATION_PATH"; "DB_FILE_PATH"; ""]
database_name| "DATABASE_NAME"
changeset_id | "CHANGESET_ID"
result_paths | ,"DESTINATION_PATH/DB_FILE_PATH"
```

Sample response for retrieving multiple files

```
.aws.copy_database_files["DATABASE_NAME"; "DESTINATION_PATH"; "PARTITION_NAME/*"; ""]
database_name| "DATABASE_NAME"
changeset_id | "CHANGESET_ID"
result_paths | ("DESTINATION_PATH/PARTITION_NAME/file1"; "DESTINATION_PATH/PARTITION_NAME/file2"...)
```

**Function**:
`.aws.get_kx_dataview[db_name;dataview_name]`

Retrieves information about a specific dataview. This operation is helpful
especially when you update a dataview with `update_kx_dataview`, as
it retrieves the latest status and reflects the updated
`changeset_id`, `segment_configurations`, and
`active_versions`.

Permissions
For this function, the `executionRole` must have the
`finspace:GetKxDataview` permission.

Parameters

`db_name`

**Description** – The
name of the FinSpace kdb database where the specified dataview
exists. This must be same as the database you used when you
created a cluster.

**Type** –
String

**Required** –
Yes

`dataview_name`

**Description** – The
name of the Managed kdb dataview you want to retrieve.

**Type** –
String

**Required** –
Yes

Result
Returns the details of specified dataview, including its status,
changeset id, and segment configurations.

```
dataview_name          | "example-dataview-name"
database_name          | "example-db"
status                 | "ACTIVE"
changeset_id           | "example-changeset-id"
segment_configurations | +`db_paths`volume_name!(,,"/*";,"example-volume")
availability_zone_id   | "use1-az2"
az_mode                | "SINGLE"
auto_update            | 0b
read_write             | 0b
active_versions        | +`changeset_id`segment_configurations`attached_clusters`created_timestamp`version_id!(("example-changeset-id";"prior-changeset-id");(+`db_paths`volume_name!(,,"/*";,"example-volume");+`db_paths`volume_name!(,,"/*";,"example-volume"));(();,"example-cluster");1.717532e+09 1.716324e+09;("kMfybotBQNQl5LBLhDnAEA";"XMfOcGisErAFO9i1XRTdYQ"))
create_timestamp       | 1.716324e+09
last_modified_timestamp| 1.717779e+09
```

**Function**: `.aws.update_kx_dataview[db_name;dataview_name;changeset_id;segment_configurations]`

Updates the changeset id and/or segment configurations of the specified dataview. Each update of the dataview creates a new version, with its own changeset details and cache configurations. If a dataview is created with auto-update set to false, when new changesets are ingested, this operation must be run to update the dataview with the latest changeset. This operation can also be used to update the segment configurations, which define which database paths are placed on each selected volume.

Permissions
For this function, the `executionRole` must have the
`finspace:UpdateKxDataview` permission.

Parameters

`db_name`

**Description** – The
name of the Managed kdb database where the specified dataview
exists. This must be the same database that you used when you
created a cluster.

**Type** –
String

**Required** –
Yes

`dataview_name`

**Description** – The
name of the Managed kdb dataview you want to update.

**Type** –
String

**Required** –
Yes

`changeset_id`

**Description** – The
identifier of the Managed kdb changeset that the dataview
should use.

**Type** –
String

**Required** –
Yes

`segment_configurations`

**Description** – The
output of the `.aws.sgmtcfgs` function.

**Required** –
Yes

Example
The following code is an example request to update the
dataview.

```
.aws.update_kx_dataview["example-db"; "example-dataview-name"; "example-changeset-id"; .aws.sgmtcfgs[.aws.sgmtcfg[("/*");"example-volume"]]]
```

Result
This function does not return any value.

**Function**: `.aws.sgmtcfgs[segment_configurations]`

This is a helper function to construct arguments for
.`aws.update_kx_dataview`, defining the list of segment
configurations for the dataview.

Parameters

`segment_configurations`

**Description** –
Either a single output of `.aws.sgmtcfg` or a list
of .`aws.sgmtcfg` outputs.

**Required** –
Yes

Example
The following example shows how this function can take a single
segment configuration.

```
.aws.sgmtcfgs[.aws.sgmtcfg[("/*");"example-volume"]]
```

Alternatively, you can use this function with multiple segment
configurations as following.

```
.aws.sgmtcfgs[(.aws.sgmtcfg[("/2020.02.01/*");"example-volume-1"];.aws.sgmtcfg[("/2020.02.02/*");"example-volume-2"])]
```

Result
The output of this function is used as input for
`.aws.update_kx_dataview`.

**Function**: `.aws.sgmtcfg[db_paths;volume_name]`

This is a helper function to construct arguments for
`.aws.sgmtcfgs`, defining a single segment configuration, the
database path of the data that you want to place on each selected volume. Each
segment must have a unique database path for each volume.

Parameters

`db_paths`

**Description** – The
database path of the data you want to place on each selected
volume for the segment. Each segment must have a unique
database path for each volume.

**Type** – Array of
strings

**Required** –
Yes

`volume_name`

**Description** – The
name of the Managed kdb volume where you would like to add
data.

**Type** –
String

**Required** –
Yes

Example
The following example shows how this function can take a single db
path.

```
.aws.sgmtcfg[("/*");"example-volume"]
```

Alternatively, you can use this function with multiple db paths as following.

```
.aws.sgmtcfg[("/2020.01.06/*";"/2020.01.02/*");"example-volume"]
```

Result
The output of this function is used as input for
`.aws.sgmtcfgs`.

## Discovery APIs

**Function**:
`.aws.list_kx_clusters()`

Returns a table of clusters in non-deleted state.

Parameters
N/A

Result
Returns a table of Managed kdb clusters that are in a non-deleted
state. This table consists of the following fields –
`cluster_name`, `status`,
`cluster_type`, and `description`.

**Function**:
`.aws.list_kx_cluster_nodes[cluster_name]`

Retrieves a list of nodes within a cluster.

Parameters

`cluster_name`

**Description** – The name of the Managed kdb cluster that you specified when
creating a kdb cluster. You can also get this by using the
`.aws.list_kx_clusters()` function.

**Type** –
String

**Required** –
Yes

Result
Returns a table of nodes in the Managed kdb cluster that consists of
`node_id`, `az_id`, and
`launch_time`.

## Authorization APIs

###### Note

You must create clusters with the IAM `executionRole` field to use the q auth APIs. Clusters will assume this role when calling the auth APIs, so the role should have `GetKxConnectionString` and `ConnectKxCluster` permissions.

**Function**:
`.aws.get_kx_node_connection_string[cluster_name;node_id]`

Retrieves the connection string for a given kdb cluster node.

Parameters

`cluster_name`

**Description** – The name of the destination Managed kdb cluster for the
connection string.

**Type** –
String

**Pattern** – `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`

**Length** –
3-63

**Required** –
Yes

`node_id`

**Description** – The node identifier of the target cluster.

**Type** –
String

**Length** – 1-40

**Required** –
Yes

Result
Returns the connection string.

**Function**:
`.aws.get_kx_connection_string[cluster_name]`

Retrieves the connection string for a given kdb cluster.

Parameters

`cluster_name`

**Description** – The name of the destination cluster for the connection string.

**Type** –
String

**Pattern** – `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`

**Length** –
3-63

**Required** –
Yes

Result
Returns the connection string.

## Cluster management APIs

###### Note

You must create clusters with the IAM `executionRole` field to use the cluster management APIs.

**Function**: `.aws.stop_current_kx_cluster_creation[message]`

Stops the current cluster creation and puts the cluster in the
`CREATE_FAILED` state. You can only call this function from an
initialization script.

Parameters

`message`

**Description** – A message to display in the `statusReason` field of the cluster after the cluster reaches the `CREATE_FAILED` state.

**Type** –
String

**Pattern** – `^[a-zA-Z0-9\_\-\.\s]*$`

**Length** – 0-50

**Required** –
Yes

Example
The following code is an example request to stop creation of current cluster with a message.

```
.aws.stop_current_kx_cluster_creation[""]
```

Result
This function does not return any value.

**Function**: `.aws.delete_kx_cluster[clusterName]`

Deletes the specified cluster. If `clusterName` is an empty
string, this function deletes the current cluster.

Permissions
For this function, the `executionRole` must have the
following permissions to delete the cluster:

- `ec2:DescribeTags`
- `ec2:DeleteVpcEndpoints`
- `finspace:DeleteKxCluster`

Parameters

`clusterName`

**Description** – The name of the cluster that you want to delete.

**Type** –
String

**Pattern** – `^[a-zA-Z0-9-_]*$`

**Length** – 1-63

**Required** –
Yes

Example
The following example deletes the _samplecst_ cluster.

```
.aws.delete_kx_cluster["samplecst"]
```

The following example deletes the current cluster.

```
.aws.delete_kx_cluster[""]
```

Result
This function does not return any value.

**Function**: `.aws.get_kx_cluster[clusterName]`

Retrieves information about the specified cluster.

Permissions
For this function, the `executionRole` must have the `finspace:GetKxCluster` permission.

Parameters

`clusterName`

**Description** – The name of the target cluster.

**Type** –
String

**Pattern** – `^[a-zA-Z0-9-_]*$`

**Length** – 1-63

**Required** –
Yes

Result

```
status               | "RUNNING"
>>>>>>> mainline
clusterName          | "`example-cluster-name`"
clusterType          | "HDB"
capacityConfiguration| `nodeType`nodeCount!("kx.s.xlarge";1f)
releaseLabel         | "1.0"
vpcConfiguration     | `vpcId`securityGroupIds`subnetIds`ipAddressType!("vpcId";,"securityGroupId";,"subnetId";"IP_V4")
executionRole        | "arn:aws:iam::`111111111111`:role/exampleRole"
lastModifiedTimestamp| 1.695064e+09
azMode               | "SINGLE"
availabilityZoneId   | "use1-az1"
createdTimestamp     | 1.695063e+09
```

**Function**: `.aws.update_kx_cluster_databases[clusterName;databases;properties]`

Updates the database of the specified kdb cluster.

Permissions

- For this function, the `executionRole` must have the `finspace:UpdateKxClusterDatabases` permission.
- You must have `finspace:GetKXCluster` permission for the `clusterName`.

Parameters

`clusterName`

**Description** – The name of the target cluster.

**Type** –
String

**Pattern** – `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`

**Length** – 3-63

**Required** –
Yes

`databases`

**Description** – The
output of the `.aws.sdbs` function.

**Required** –
Yes

`properties`

**Description** – The
output of the `.aws.sdep` function.

**Required** –
Yes

Example
The following code is an example request to update the cluster database.

```
.aws.update_kx_cluster_databases["`HDB_TAQ_2021H1`";
    .aws.sdbs[
        .aws.db["`TAQ_2021H1`";"`osSoXB58eSXuDXLZFTCHyg`";
            .aws.cache["CACHE_1000";"/"];
            ""
            ]
        ];
    .aws.sdep["`ROLLING`"]]
```

Result
This function does not return any value.

**Function**: `.aws.sdbs[databases]`

This is a helper function to construct arguments for
`.aws.update_kx_cluster_databases`.

Parameters

databases
**Description** – It is either a single output of
`.aws.db` or a list of `.aws.db`
outputs.

**Required** –
Yes

ExampleHere is an example of how you can use this function.

```
.aws.sdbs[
    .aws.db["TAQ_2021H1";"osSoXB58eSXuDXLZFTCHyg";
        .aws.cache["CACHE_1000";"/"];
         ""
        ]
    ];
```

Result The output of this function is used as input for `.aws.update_kx_cluster_databases` function.

**Function**:
`.aws.db[databaseName;changesetId;caches;dataviewName]`

This is a helper function to construct arguments for
`.aws.sdbs`.

Parameters

databaseName

**Description** – The name of the target database.

**Type** –
String

**Pattern** – `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`

**Length** – 3-63

**Required** –
Yes

changesetId

**Description** – A
unique identifier of the changeset. If you pass empty string “”
for this parameter, the latest changeset of the database will be
used.

**Type** –
String

**Length** – 1-26

**Required** –
No

caches

**Description** – It is
either a single output of `.aws.cache` or a list of
.`aws.cache` outputs. If there is no cache
associated to the cluster, this list must be empty.

**Required** –
No

dataviewName

**Description** – The
name of the dataview.

**Type** –
String

**Pattern** – `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`

**Length** – 3-63

**Required** –
No

Example You can use this function to specify the changeset that you want to update, as
following:

```
.aws.db["example-db";"example-changeset-id"; .aws.cache["CACHE_1000";"/"];""]
```

Alternatively, if the cluster is attached to a dataview, you can use
this function to update the cluster to the latest version of the
dataview with the specified `dataviewName`, as
following:

```
.aws.db["example-db";""; .aws.cache["CACHE_1000";"/"];"example-dataview-name"]
```

Result The output of this function is used as input for `.aws.sdbs` function.

**Function**: `.aws.cache[cacheType;dbPaths]`

This is a helper function to construct arguments for
`.aws.db`.

Parameters

cacheType

**Description** – The type of disk cache. This parameter is used to map the database path to cache storage.

**Type** –
String

**Length** – 8-10

**Required** –
Yes

dbPaths

**Description** – The portions of database that will be loaded into the cache for access.

**Type** –
Array of strings

**Pattern** – `^\/([^\/]+\/){0,2}[^\/]*$`

**Length** – 1-1025

**Required** – Yes

Example The following two examples show how you can send different requests by using this function.

```
.aws.cache["CACHE_1000";"/"]
```

```
.aws.cache["CACHE_1000";("path1";"path2")]
```

Result The output of this function is used as input for `.aws.db` function.

**Function**: `.aws.sdbs[deploymentStrategy]`

This is a helper function to construct arguments for
`.aws.update_kx_cluster_databases`.

Parameters

deploymentStrategy

**Description** – The type of deployment that you want on a cluster. The following types are available.

- `ROLLING` – This options loads the updated database by stopping the exiting q process and starting a new q process with updated configuration.
- `NO_RESTART` – This option loads the updated database on the running q process without stopping it. This option is quicker as it reduces the turn around time to update a kdb database changeset configuration on a cluster.

**Type** –
String

**Required** –
Yes

Result The output of this function is used as input for `.aws.update_kx_cluster_databases` function.

## Pub/Sub APIs

**Function**:
`.aws.sub[table;sym_list]`

Initializes the publish and subscribe function.

Parameters

`table`

**Description** – The symbol of the table that you want to subscribe to. The symbol ``` subscribes to all tables.

**Type** –
Symbol

**Required** –
Yes

`sym_list`

**Description** – The list of symbols to filter published records. Defaults to ``` if no filter is applied.

**Type** –
Symbol list

**Required** –
Yes

Result
Returns table schema or table schemas list.

**Example 1: Subscribes to ``tab` table
 and filtering ``AAPL`MSFT`**.

```
target_instance_connection_handle ".aws.sub[`tab;`AAPL`MSFT]"
```

**Result**

```
`tab
+`sym`sales`prices!(`g#`symbol$();`long$();`long$())
```

**Example 2: Subscribes to all tables with no
filtering**.

```
target_instance_connection_handle ".aws.sub[`;`]"
```

**Result**

```
`tab  +`sym`sales`prices!(`g#`symbol$();`long$();`long$())
`tab1 +`sym`sales`prices!(`g#`symbol$();`long$();`long$())
`tab2 +`sym`sales`prices!(`g#`symbol$();`long$();`long$())
`tab3 +`sym`sales`prices!(`g#`symbol$();`long$();`long$())
```

**Function**:
`.aws.pub[table;table_records]`

Publishes table records to table subscribers by calling
`upd[table;table_records]` within the subscriber connection
handle.

Parameters

`table`

**Description** – Publishes the records to the table subscribers.

**Type** –
Symbol

**Required** –
Yes

`table_records`

**Description** – The table records that you want to publish.

**Type** – Table

**Required** –
Yes

Example
This example publishes ``tab` table and values to the subscribers.

```
.aws.pub[`tab;value `tab]
```

Result
This function does not return any value.

## Database maintenance APIs

**Function**:
`.aws.commit_kx_database[database_name]`

Commits the database changes after performing database maintenance.

Parameters

`database_name`

**Description** – The
name of the database where you performed database maintenance
operations and whose changes you want to commit.

**Type** –
String

**Required** –
Yes

Example

```
.aws.commit_kx_database["welcomedb"]
```

Result
Returns the `id` and `status` of the
changeset that the API creates.
