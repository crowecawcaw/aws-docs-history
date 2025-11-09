# Auditing Amazon DocumentDB events

With Amazon DocumentDB (with MongoDB compatibility), you can audit events that were performed in your cluster. Examples of
logged events include successful and failed authentication attempts, dropping a collection in
a database, or creating an index. By default, auditing is disabled on Amazon DocumentDB and requires
that you opt in to use this feature.

When auditing is enabled, Amazon DocumentDB records Data Definition Language (DDL), Data Manipulation Language (DML),
authentication, authorization, and user management events to Amazon CloudWatch Logs. When
auditing is enabled, Amazon DocumentDB exports your cluster’s auditing records (JSON documents) to Amazon CloudWatch Logs. You can use Amazon CloudWatch Logs to analyze, monitor, and archive
your Amazon DocumentDB auditing events.

Although Amazon DocumentDB does not charge an additional cost to enable auditing, you are charged
standard rates for the usage of CloudWatch Logs. For information about CloudWatch Logs pricing, see [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

The Amazon DocumentDB auditing feature is distinctly different from the service resource usage that is
monitored with AWS CloudTrail. CloudTrail records operations that are performed with the AWS Command Line Interface (AWS CLI)
or AWS Management Console on resources like clusters, instances, parameter groups, and snapshots. Auditing of
resources with CloudTrail is on by default and cannot be disabled. The Amazon DocumentDB
auditing feature is an opt-in feature. It records operations that take place within your cluster
on objects, such as databases, collections, indexes, and users.

###### Topics

- [Supported events](#auditing-events "#auditing-events")
- [Enabling auditing](#event-auditing-enabling-auditing "#event-auditing-enabling-auditing")
- [Disabling auditing](#event-auditing-disabling-auditing "#event-auditing-disabling-auditing")
- [Accessing your audit events](#event-auditing-accessing "#event-auditing-accessing")
- [Filtering DML audit events](#filtering-dml-events "#filtering-dml-events")

## Supported events

Amazon DocumentDB auditing supports the following event categories:

- **Data Definition Language (DDL)** - includes
  database management operations, connections, user management, and authorization.
- **Data Manipulation Language read events (DML reads)** -
  includes `find()` and the various aggregation operators, arithmetic operators, boolean
  operators, and other read query operators.
- **Data Manipulation Language write events (DML writes)** - includes
  `insert(), update(), delete(),` and `bulkWrite()` operators

The event types are as follows.

| Event Type                                                     | Category               | Description                                                                                                             |
| -------------------------------------------------------------- | ---------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `authCheck`                                                    | Authorization          | Result code 0: Success                                                                                                  |
| Result code 13: Unauthorized attempts to perform an operation. |
| `authenticate`                                                 | Connection             | Successful or failed authentication attempts on a new connection.                                                       |
| `auditConfigure`                                               | DDL                    | Audit filter configuration.                                                                                             |
| `createDatabase`                                               | DDL                    | Creation of a new database.                                                                                             |
| `createCollection`                                             | DDL                    | Creation of a new collection within a database.                                                                         |
| `createIndex`                                                  | DDL                    | Creation of a new index within a collection.                                                                            |
| `dropCollection`                                               | DDL                    | Dropping of a collection within a database.                                                                             |
| `dropDatabase`                                                 | DDL                    | Dropping of a database.                                                                                                 |
| `dropIndex`                                                    | DDL                    | Dropping of an index within a collection.                                                                               |
| `modifyChangeStreams`                                          | DDL                    | Change stream was created.                                                                                              |
| `renameCollection`                                             | DDL                    | Renaming of a collection within a database.                                                                             |
| `createRole`                                                   | Role Management        | Creating a role.                                                                                                        |
| `dropAllRolesFromDatabase`                                     | Role Management        | Dropping all roles within a database.                                                                                   |
| `dropRole`                                                     | Role Management        | Dropping a role.                                                                                                        |
| `grantPrivilegesToRole`                                        | Role Management        | Granting privileges to a role.                                                                                          |
| `grantRolesToRole`                                             | Role Management        | Granting roles to a user-defined role.                                                                                  |
| `revokePrivilegesFromRole`                                     | Role Management        | Revoking privileges from a role.                                                                                        |
| `revokeRolesFromRole`                                          | Role Management        | Revoking roles from a user-defined role.                                                                                |
| `updateRole`                                                   | Role Management        | Updating a role.                                                                                                        |
| `createUser`                                                   | User Management        | Creation of a new user.                                                                                                 |
| `dropAllUsersFromDatabase`                                     | User Management        | Dropping of all users within a database.                                                                                |
| `dropUser`                                                     | User Management        | Dropping of an existing user.                                                                                           |
| `grantRolesToUser`                                             | User Management        | Granting roles to a user.                                                                                               |
| `revokeRolesFromUser`                                          | User Management        | Revoking roles from a user.                                                                                             |
| `updateUser`                                                   | UserManagement         | Updating of an existing user.                                                                                           |
| `insert`                                                       | DML write              | Inserts a document or documents into a collection.                                                                      |
| `delete`                                                       | DML write              | Deletes a document or documents from a collection.                                                                      |
| `update`                                                       | DML write              | Modifies an existing document or documents in a collection.                                                             |
| `bulkWrite`                                                    | DML write              | Performs multiple write operations with controls for order of execution.                                                |
| `setAuditConfig`                                               | DML write              | Set a new filter for DML auditing.                                                                                      |
| `count`                                                        | DML read               | Returns the count of documents that would match a find() query for the collection or view.                              |
| `countDocuments`                                               | DML read               | Returns the count of documents that match the query for a collection or view.                                           |
| `find`                                                         | DML read               | Selects documents in a collection or view and returns a cursor to the selected documents.                               |
| `getAuditConfig`                                               | DML read               | Retrieve the current filter for DML auditing.                                                                           |
| `findAndModify`                                                | DML read and DML write | Modifies and returns a single document.                                                                                 |
| `findOneAndDelete`                                             | DML read and DML write | Deletes a single document based on the filter and sort criteria, returning the deleted document.                        |
| `findOneAndReplace`                                            | DML read and DML write | Replaces a single document based on the specified filter.                                                               |
| `findOneAndUpdate`                                             | DML read and DML write | Updates a single document based on the filter and sort criteria.                                                        |
| `aggregate`                                                    | DML read and DML write | Supports APIs in the aggregation pipeline.                                                                              |
| `distinct`                                                     | DML read               | Finds the distinct values for a specified field across a single collection or view and returns the results in an array. |

###### Note

Values in the DML event document parameter field have a 1KB size limit.
Amazon DocumentDB truncates the value if it exceeds 1KB.

###### Note

TTL delete events are not audited at this time.

## Enabling auditing

Enabling auditing on a cluster is a two-step process. Ensure that both steps are completed, or audit logs will not be
sent to CloudWatch Logs.

### Step 1. Enable the audit_logs cluster parameter

To enable auditing, you need to modify the `audit_logs` parameter in the parameter group.
`audit_logs` is a comma-delimited list of events to log. Events must be specified in lowercase and there should be no white space
between the list elements.

You can set the following values for the parameter group:

| Value               | Description                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ddl`               | Setting this will enable auditing for DDL events such as createDatabase, dropDatabase,<br>createCollection, dropCollection, createIndex, dropIndex, authCheck, authenticate, createUser,<br>dropUser, grantRolesToUser, revokeRolesFromUser, updateUser, and dropAllUsersFromDatabase                                                                                                                                               |
| `dml_read`          | Setting this will enable auditing for DML read events such as find, sort count, distinct, group,<br>projecta, unwind, geoNear, geoIntersects, geoWithin and other MongoDB read query operators.                                                                                                                                                                                                                                     |
| `dml_write`         | Setting this will enable auditing for DML write events such as insert(), update(), delete(),<br>and bulkWrite()                                                                                                                                                                                                                                                                                                                     |
| `all`               | Setting this will enable auditing for your database events, such as read queries, write queries,<br>database actions and administrator actions.                                                                                                                                                                                                                                                                                     |
| `none`              | Setting this will disable auditing                                                                                                                                                                                                                                                                                                                                                                                                  |
| `enabled` (legacy)  | This is a legacy parameter setting that is equivalent to 'ddl'. Setting this will enable auditing<br>for DDL events such as createDatabase, dropDatabase, createCollection, dropCollection, createIndex,<br>dropIndex, authCheck, authenticate, createUser, dropUser, grantRolesToUser, revokeRolesFromUser,<br>updateUser, and dropAllUsersFromDatabase. We do not recommend using this setting because it is a<br>legacy setting. |
| `disabled` (legacy) | This is a legacy parameter setting that is equivalent to 'none'. We do not recommend using this setting<br>because it is a legacy setting.                                                                                                                                                                                                                                                                                          |

###### Note

The default value for the audit_logs cluster parameter is `none` (legacy "`disabled`").

You can also use the above mentioned values in combinations.

| Value                 | Description                                                           |
| --------------------- | --------------------------------------------------------------------- |
| `ddl, dml_read`       | Setting this will enable auditing for DDL events and DML read events. |
| `ddl, dml_write`      | Setting this will enable auditing for DDL events and DML write        |
| `dml_read, dml_write` | Setting this will enable auditing for all DML events                  |

###### Note

You cannot modify a default parameter group.

For more information, see the following:

- [Creating Amazon DocumentDB cluster parameter groups](cluster_parameter_groups-create.md "cluster_parameter_groups-create.md")

After creating a custom parameter group, modify it by changing the `audit_logs` parameter value to `all`.

- [Modifying Amazon DocumentDB cluster parameter groups](cluster_parameter_groups-modify.md "cluster_parameter_groups-modify.md")

### Step 2. Enable Amazon CloudWatch Logs export

When the value of the `audit_logs` cluster parameter is `enabled`, `ddl`, `dml_read`, or `dml_write`, you must also enable Amazon DocumentDB to export logs to Amazon CloudWatch.
If you omit either of these steps, audit logs will not be sent to CloudWatch.

When creating a cluster, performing a point-in-time-restore, or restoring a snapshot, you can enable CloudWatch Logs by following these steps.

Using the AWS Management Console
To enable Amazon DocumentDB exporting logs to CloudWatch using the console, see the following
topics:

- **When creating a cluster** — In [Creating a cluster and primary instance using the AWS Management Console](db-cluster-create.md#db-cluster-create-con "db-cluster-create.md#db-cluster-create-con"), see
  **Create a Cluster: Additional Configurations** (step 5,
  **Log exports**)
- **When modifying an existing cluster** —
  [Modifying an Amazon DocumentDB cluster](db-cluster-modify.md "db-cluster-modify.md")
- **When performing a cluster snapshot restore** — [Restoring from a cluster snapshot](backup_restore-restore_from_snapshot.md "backup_restore-restore_from_snapshot.md")
- **When performing a point-in-time restore** — [Restoring to a point in time](backup_restore-point_in_time_recovery.md "backup_restore-point_in_time_recovery.md")

Using the AWS CLI

###### To enable audit logs when creating a new cluster

The following code creates the cluster `sample-cluster` and enables CloudWatch audit logs.

For Linux, macOS, or Unix:

```
aws docdb create-db-cluster \
    --db-cluster-identifier `sample-cluster` \
    --port 27017 \
    --engine docdb \
    --master-username `master-username` \
    --master-user-password `password` \
    --db-subnet-group-name `default` \
    `--enable-cloudwatch-logs-exports audit`
```

For Windows:

```
aws docdb create-db-cluster ^
    --db-cluster-identifier `sample-cluster` ^
    --port 27017 ^
    --engine docdb ^
    --master-username `master-username` ^
    --master-user-password `password` ^
    --db-subnet-group-name `default` ^
    `--enable-cloudwatch-logs-exports audit`
```

###### To enable audit logs when modifying an existing cluster

The following code modifies the cluster `sample-cluster` and enables CloudWatch audit logs.

For Linux, macOS, or Unix:

```
aws docdb modify-db-cluster \
   --db-cluster-identifier `sample-cluster` \
   `--cloudwatch-logs-export-configuration '{"EnableLogTypes":["audit"]}'`
```

For Windows:

```
aws docdb modify-db-cluster ^
   --db-cluster-identifier `sample-cluster` ^
   `--cloudwatch-logs-export-configuration '{"EnableLogTypes":["audit"]}'`
```

Output from these operations looks something like the following (JSON format).

```
{
    "DBCluster": {
        "HostedZoneId": "ZNKXH85TT8WVW",
        "StorageEncrypted": false,
        "DBClusterParameterGroup": "default.docdb4.0",
        "MasterUsername": "<user-name>",
        "BackupRetentionPeriod": 1,
        "Port": 27017,
        "VpcSecurityGroups": [
            {
                "Status": "active",
                "VpcSecurityGroupId": "sg-77186e0d"
            }
        ],
        "DBClusterArn": "arn:aws:rds:us-east-1:900083794985:cluster:sample-cluster",
        "Status": "creating",
        "Engine": "docdb",
        "EngineVersion": "4.0.0",
        "MultiAZ": false,
        "AvailabilityZones": [
            "us-east-1a",
            "us-east-1c",
            "us-east-1f"
        ],
        "DBSubnetGroup": "default",
        "DBClusterMembers": [],
        "ReaderEndpoint": "sample-cluster.cluster-ro-corcjozrlsfc.us-east-1.docdb.amazonaws.com",
        `"EnabledCloudwatchLogsExports": [
 "audit"
 ]`,
        "PreferredMaintenanceWindow": "wed:03:08-wed:03:38",
        "AssociatedRoles": [],
        "ClusterCreateTime": "2019-02-13T16:35:04.756Z",
        "DbClusterResourceId": "cluster-YOS52CUXGDTNKDQ7DH72I4LED4",
        "Endpoint": "sample-cluster.cluster-corcjozrlsfc.us-east-1.docdb.amazonaws.com",
        "PreferredBackupWindow": "07:16-07:46",
        "DBClusterIdentifier": "sample-cluster"
    }
}
```

## Disabling auditing

You can disable auditing by disabling CloudWatch Logs export and disabling the
`audit_logs` parameter.

### Disabling CloudWatch Logs export

You can disable exporting audit logs using either the AWS Management Console or the AWS CLI.

Using the AWS Management Console
The following procedure uses the AWS Management Console to disable Amazon DocumentDB exporting logs to CloudWatch.

###### To disable audit logs

1. Sign in to the AWS Management Console, and open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb "https://console.aws.amazon.com/docdb").
2. In the navigation pane, choose **Clusters**. Then choose
   the button to the left of the name of the cluster for which you want to disable
   exporting logs.
3. Choose **Actions**, and then choose
   **Modify**.
4. Scroll down to the **Log exports** section and choose **Disabled**.
5. Choose **Continue**.
6. Review your changes, and then choose when you want this change applied to
   your cluster.
   - **Apply during the next scheduled maintenance window**
   - **Apply immediately**

7. Choose **Modify cluster**.

Using the AWS CLI
The following code modifies the cluster `sample-cluster` and disables CloudWatch audit logs.

For Linux, macOS, or Unix:

```
aws docdb modify-db-cluster \
   --db-cluster-identifier `sample-cluster` \
   --cloudwatch-logs-export-configuration '{"DisableLogTypes":["audit"]}'
```

For Windows:

```
aws docdb modify-db-cluster ^
   --db-cluster-identifier `sample-cluster` ^
   --cloudwatch-logs-export-configuration '{"DisableLogTypes":["audit"]}'
```

Output from this operation looks something like the following (JSON format).

```
{
    "DBCluster": {
        "DBClusterParameterGroup": "default.docdb4.0",
        "HostedZoneId": "ZNKXH85TT8WVW",
        "MasterUsername": "<user-name>",
        "Status": "available",
        "Engine": "docdb",
        "Port": 27017,
        "AvailabilityZones": [
            "us-east-1a",
            "us-east-1c",
            "us-east-1f"
        ],
        "EarliestRestorableTime": "2019-02-13T16:35:50.387Z",
        "DBSubnetGroup": "default",
        "LatestRestorableTime": "2019-02-13T16:35:50.387Z",
        "DBClusterArn": "arn:aws:rds:us-east-1:900083794985:cluster:sample-cluster2",
        "Endpoint": "sample-cluster2.cluster-corcjozrlsfc.us-east-1.docdb.amazonaws.com",
        "ReaderEndpoint": "sample-cluster2.cluster-ro-corcjozrlsfc.us-east-1.docdb.amazonaws.com",
        "BackupRetentionPeriod": 1,
        "EngineVersion": "4.0.0",
        "MultiAZ": false,
        "ClusterCreateTime": "2019-02-13T16:35:04.756Z",
        "DBClusterIdentifier": "sample-cluster2",
        "AssociatedRoles": [],
        "PreferredBackupWindow": "07:16-07:46",
        "DbClusterResourceId": "cluster-YOS52CUXGDTNKDQ7DH72I4LED4",
        "StorageEncrypted": false,
        "PreferredMaintenanceWindow": "wed:03:08-wed:03:38",
        "DBClusterMembers": [],
        "VpcSecurityGroups": [
            {
                "Status": "active",
                "VpcSecurityGroupId": "sg-77186e0d"
            }
        ]
    }
}
```

### Disabling the audit_logs parameter

To disable the `audit_logs` parameter for your cluster, you can modify the
cluster so that it uses a parameter group where the `audit_logs` parameter
value is `disabled`. Or you can modify the `audit_logs` parameter
value in the cluster's parameter group so that it is `disabled`.

For more information, see the following topics:

- [Modifying an Amazon DocumentDB cluster](db-cluster-modify.md "db-cluster-modify.md")
- [Modifying Amazon DocumentDB cluster parameter groups](cluster_parameter_groups-modify.md "cluster_parameter_groups-modify.md")

## Accessing your audit events

Use following steps to access your audit events on Amazon CloudWatch.

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. Make sure that you are in the same Region as your Amazon DocumentDB cluster.
3. In the navigation pane, choose **Logs**.
4. To find the audit logs for your cluster, from the list locate and choose
   `/aws/docdb/`yourClusterName`/audit`.

The auditing events for each of your instances are available under each of the respective instance names.

## Filtering DML audit events

### Getting started with DML audit filtering

DML audit events can be filtered before they are written to Amazon CloudWatch.
To utilize this feature, audit log and DML logging must be enabled. Amazon DocumentDB supports filtering on `atype`, `command`, `user`, `namespace`, and `auditAuthorizationSuccess`.

###### Note

DDL events are not filtered.

You can enable audit filtering at anytime by specifying the audit filter using the `setAuditConfig`, `filter`, and `auditAuthorizationSuccess` parameters in the `db.adminCommand( { command } )` operation:

```
db.admin.runCommand(
   {
      setAuditConfig: 1,
      filter:
         {
            //filter conditions
         },
      auditAuthorizationSuccess: true | false
   }
)
```

You can also retrieve the audit filter settings by running the following command:

```
db.admin.runCommand( { getAuditConfig: 1})
```

**Security requirements**

Only database users/roles with privileged action `auditConfigure` can execute the above commands against `admindb` when setting or listing DML audit filters.
You can either use one of the built-in roles from [`clusterAdmin`, `hostManager`, `root`] or create custom roles that have `auditConfigure` privileges.
The following is an example of using existing roles with the `auditConfigure` privilege and an example with custom roles.

User with built-in role:

```
use admin
db.createUser(
  {
    user: "myClusterAdmin",
    pwd: "password123",
    roles: [ { role: "clusterAdmin", db: "admin" } ]
  }
)
```

User with custom roles:

```
use admin
db.createRole(
   {
     role: "myRole",
     privileges: [
       { resource: { cluster: true }, actions: [ "auditConfigure" ] }
     ],
     roles: []
   }
)
db.createUser(
  {
    user: "myUser",
    pwd: "myPassword",
    roles: [ { role: "myRole", db: "admin" } ]
  }
)
```

#### Filtering use cases

**Example: filtering events by commands**

```
db.admin.runCommand(
   {
      setAuditConfig: 1,
      filter: {
        "$and": [
         {
            "param.command":
               {
                  $in: [ "find","count", "insert", "delete", "update", "findandmodify" ]
               }
         }
         ]
      },
      auditAuthorizationSuccess: true
   }
)
```

**Example: filtering events by user name**

In this example, only user "myUser" will be logged:

```
db.admin.runCommand(
   {
      setAuditConfig: 1,
      filter: {
      "$and": [
         {
            "param.user":
               {
                  $in: [ "myUser" ]
               }
         }
         ]},
      auditAuthorizationSuccess: true})
```

**Example: filtering by `atype`**

```
db.admin.runCommand(
   {
      setAuditConfig: 1,
      filter: {atype: "authCheck"},
      auditAuthorizationSuccess: true
   })
```

###### Note

All DML logs have `authCheck` as `atype`. Only DDL has a different `atype`.
If you put a value other than `authCheck` in the `filter`, it will not produce a DML log in CloudWatch.

**Example: filtering by using multiple filters joined by operators**

```
db.admin.runCommand(
   {
      setAuditConfig: 1,
      filter: {
      "$and": [
         {
            "param.command":
               {
                  $in: [ "find","count", "insert", "delete", "update", "findandmodify" ]
               }
         }
         ],
       "$nor": [
         {
            "param.command":
               {
                  $in: ["count", "insert", "delete", "update", "findandmodify" ]
               }
         }]
       },
      auditAuthorizationSuccess: true})
```

###### Note

At the top level, only `$and`, `$or`, and `$nor` are supported. Any other operators are not supported and will cause an error.

**Example: filtering by events by `auditAuthorizationSuccess`**

In this filter, all commands that have successfully passed authorization will not be logged:

```
db.admin.runCommand(
   {
      setAuditConfig: 1,
      filter: {},
      auditAuthorizationSuccess: false
   }
)
```

**Example: filtering with `$in` and `$nin` conditions**

When using both in `$in` and `$nin`, the command will not be logged as there will be an implicit "and" between the conditions.
In this example, regex will block the `find` command so nothing will be logged:

```
db.admin.runCommand(
   {
      setAuditConfig: 1,
      filter: {
      "$and": [
         {
            atype: "authCheck",
            "param.command":
               {
                  $in: [ "find", "insert", "delete", "update", "findandmodify" ],
                  $nin: ["count", "insert", "delete", "update", "findandmodify" ],
                  $not: /^^find.*/
               }
         },
         ],
       "$or": [
         {
            "param.command":
               {
                  $nin: ["count", "insert", "delete", "update", "findandmodify" ]
               }
         }]
       },
      auditAuthorizationSuccess: true})
```

**Example: filtering by `namespace`**

```
db.admin.runCommand(
   {
      setAuditConfig: 1,
      filter: {
      "$and": [
         {
            "param.ns":
               {
                  $in: [ "test.foo" ]
               }
         }
         ]},
      auditAuthorizationSuccess: true})
```

**Example: resetting to default filter**

Resetting to the default value means that every DML audit event will be logged. To reset filtering to the default value, run the following command:

```
db.admin.runCommand(
   {
      setAuditConfig: 1,
      filter: {},
      auditAuthorizationSuccess: true
   }
)
```
