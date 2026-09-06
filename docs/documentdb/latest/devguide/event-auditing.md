

# Auditing Amazon DocumentDB events
<a name="event-auditing"></a>

With Amazon DocumentDB (with MongoDB compatibility), you can audit events that were performed in your cluster. Examples of logged events include successful and failed authentication attempts, dropping a collection in a database, or creating an index. By default, auditing is disabled on Amazon DocumentDB and requires that you opt in to use this feature.

When auditing is enabled, Amazon DocumentDB records Data Definition Language (DDL), Data Manipulation Language (DML), authentication, authorization, and user management events to Amazon CloudWatch Logs. When auditing is enabled, Amazon DocumentDB exports your cluster’s auditing records (JSON documents) to Amazon CloudWatch Logs. You can use Amazon CloudWatch Logs to analyze, monitor, and archive your Amazon DocumentDB auditing events.

Although Amazon DocumentDB does not charge an additional cost to enable auditing, you are charged standard rates for the usage of CloudWatch Logs. For information about CloudWatch Logs pricing, see [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/).

The Amazon DocumentDB auditing feature is distinctly different from the service resource usage that is monitored with AWS CloudTrail. CloudTrail records operations that are performed with the AWS Command Line Interface (AWS CLI) or AWS Management Console on resources like clusters, instances, parameter groups, and snapshots. Auditing of resources with CloudTrail is on by default and cannot be disabled. The Amazon DocumentDB auditing feature is an opt-in feature. It records operations that take place within your cluster on objects, such as databases, collections, indexes, and users.

**Topics**
+ [Supported events](#auditing-events)
+ [Enabling auditing](#event-auditing-enabling-auditing)
+ [Disabling auditing](#event-auditing-disabling-auditing)
+ [Accessing your audit events](#event-auditing-accessing)
+ [Filtering DML audit events](#filtering-dml-events)

## Supported events
<a name="auditing-events"></a>

Amazon DocumentDB auditing supports the following event categories:
+ **Data Definition Language (DDL)** - includes database management operations, connections, user management, and authorization. 
+ **Data Manipulation Language read events (DML reads) ** - includes `find()` and the various aggregation operators, arithmetic operators, boolean operators, and other read query operators. 
+ **Data Manipulation Language write events (DML writes) ** - includes `insert(), update(), delete(),` and `bulkWrite()` operators 

The event types are as follows.



- **`authCheck`**
  - **Category:** Authorization
  - **Description:**
    - Result code 0: Success
    - Result code 13: Unauthorized attempts to perform an operation.

- **`authenticate`**
  - **Category:** Connection
  - **Description:** Successful or failed authentication attempts on a new connection.

- **`auditConfigure`**
  - **Category:** DDL
  - **Description:** Audit filter configuration.

- **`createDatabase`**
  - **Category:** DDL
  - **Description:** Creation of a new database.

- **`createCollection`**
  - **Category:** DDL
  - **Description:** Creation of a new collection within a database.

- **`createIndex`**
  - **Category:** DDL
  - **Description:** Creation of a new index within a collection.

- **`dropCollection`**
  - **Category:** DDL
  - **Description:** Dropping of a collection within a database.

- **`dropDatabase`**
  - **Category:** DDL
  - **Description:** Dropping of a database.

- **`dropIndex`**
  - **Category:** DDL
  - **Description:** Dropping of an index within a collection.

- **`modifyChangeStreams`**
  - **Category:** DDL
  - **Description:** Change stream was created.

- **`renameCollection`**
  - **Category:** DDL
  - **Description:** Renaming of a collection within a database.

- **`createRole`**
  - **Category:** Role Management
  - **Description:** Creating a role.

- **`dropAllRolesFromDatabase`**
  - **Category:** Role Management
  - **Description:** Dropping all roles within a database.

- **`dropRole`**
  - **Category:** Role Management
  - **Description:** Dropping a role.

- **`grantPrivilegesToRole`**
  - **Category:** Role Management
  - **Description:** Granting privileges to a role.

- **`grantRolesToRole`**
  - **Category:** Role Management
  - **Description:** Granting roles to a user-defined role.

- **`revokePrivilegesFromRole`**
  - **Category:** Role Management
  - **Description:** Revoking privileges from a role.

- **`revokeRolesFromRole`**
  - **Category:** Role Management
  - **Description:** Revoking roles from a user-defined role.

- **`updateRole`**
  - **Category:** Role Management
  - **Description:** Updating a role.

- **`createUser`**
  - **Category:** User Management
  - **Description:** Creation of a new user.

- **`dropAllUsersFromDatabase`**
  - **Category:** User Management
  - **Description:** Dropping of all users within a database.

- **`dropUser`**
  - **Category:** User Management
  - **Description:** Dropping of an existing user.

- **`grantRolesToUser`**
  - **Category:** User Management
  - **Description:** Granting roles to a user.

- **`revokeRolesFromUser`**
  - **Category:** User Management
  - **Description:** Revoking roles from a user.

- **`updateUser`**
  - **Category:** UserManagement
  - **Description:** Updating of an existing user.

- **`insert`**
  - **Category:** DML write
  - **Description:** Inserts a document or documents into a collection.

- **`delete`**
  - **Category:** DML write
  - **Description:** Deletes a document or documents from a collection.

- **`update`**
  - **Category:** DML write
  - **Description:** Modifies an existing document or documents in a collection.

- **`bulkWrite`**
  - **Category:** DML write
  - **Description:** Performs multiple write operations with controls for order of execution.

- **`setAuditConfig`**
  - **Category:** DML write
  - **Description:** Set a new filter for DML auditing.

- **`count`**
  - **Category:** DML read
  - **Description:** Returns the count of documents that would match a find() query for the collection or view.

- **`countDocuments`**
  - **Category:** DML read
  - **Description:** Returns the count of documents that match the query for a collection or view.

- **`find`**
  - **Category:** DML read
  - **Description:** Selects documents in a collection or view and returns a cursor to the selected documents.

- **`getAuditConfig`**
  - **Category:** DML read
  - **Description:** Retrieve the current filter for DML auditing.

- **`findAndModify`**
  - **Category:** DML read and DML write
  - **Description:** Modifies and returns a single document.

- **`findOneAndDelete`**
  - **Category:** DML read and DML write
  - **Description:** Deletes a single document based on the filter and sort criteria, returning the deleted document.

- **`findOneAndReplace`**
  - **Category:** DML read and DML write
  - **Description:** Replaces a single document based on the specified filter.

- **`findOneAndUpdate`**
  - **Category:** DML read and DML write
  - **Description:** Updates a single document based on the filter and sort criteria.

- **`aggregate`**
  - **Category:** DML read and DML write
  - **Description:** Supports APIs in the aggregation pipeline.

- **`distinct`**
  - **Category:** DML read
  - **Description:** Finds the distinct values for a specified field across a single collection or view and returns the results in an array.



**Note**  
Values in the DML event document parameter field have a 1KB size limit. Amazon DocumentDB truncates the value if it exceeds 1KB.

**Note**  
TTL delete events are not audited at this time.

## Enabling auditing
<a name="event-auditing-enabling-auditing"></a>

Enabling auditing on a cluster is a two-step process. Ensure that both steps are completed, or audit logs will not be sent to CloudWatch Logs.

### Step 1. Enable the audit\_logs cluster parameter
<a name="event-auditing-enable-audit_logs"></a>

To enable auditing, you need to modify the `audit_logs` parameter in the parameter group. `audit_logs` is a comma-delimited list of events to log. Events must be specified in lowercase and there should be no white space between the list elements. 

You can set the following values for the parameter group:


| Value | Description | 
| --- | --- | 
| ddl | Setting this will enable auditing for DDL events such as createDatabase, dropDatabase, createCollection, dropCollection, createIndex, dropIndex, authCheck, authenticate, createUser, dropUser, grantRolesToUser, revokeRolesFromUser, updateUser, and dropAllUsersFromDatabase | 
| dml\_read | Setting this will enable auditing for DML read events such as find, sort count, distinct, group, projecta, unwind, geoNear, geoIntersects, geoWithin and other MongoDB read query operators. | 
| dml\_write | Setting this will enable auditing for DML write events such as insert(), update(), delete(), and bulkWrite() | 
| all | Setting this will enable auditing for your database events, such as read queries, write queries, database actions and administrator actions. | 
| none | Setting this will disable auditing | 
| enabled (legacy) | This is a legacy parameter setting that is equivalent to 'ddl'. Setting this will enable auditing for DDL events such as createDatabase, dropDatabase, createCollection, dropCollection, createIndex, dropIndex, authCheck, authenticate, createUser, dropUser, grantRolesToUser, revokeRolesFromUser, updateUser, and dropAllUsersFromDatabase. We do not recommend using this setting because it is a legacy setting. | 
| disabled (legacy) | This is a legacy parameter setting that is equivalent to 'none'. We do not recommend using this setting because it is a legacy setting.  | 

**Note**  
The default value for the audit\_logs cluster parameter is `none` (legacy "`disabled`").

You can also use the above mentioned values in combinations. 


| Value | Description | 
| --- | --- | 
| ddl, dml\_read | Setting this will enable auditing for DDL events and DML read events. | 
| ddl, dml\_write | Setting this will enable auditing for DDL events and DML write | 
| dml\_read, dml\_write | Setting this will enable auditing for all DML events | 

**Note**  
You cannot modify a default parameter group.

For more information, see the following:
+ [Creating Amazon DocumentDB cluster parameter groups](cluster_parameter_groups-create.md)

  After creating a custom parameter group, modify it by changing the `audit_logs` parameter value to `all`.
+ [Modifying Amazon DocumentDB cluster parameter groups](cluster_parameter_groups-modify.md)

  

### Step 2. Enable Amazon CloudWatch Logs export
<a name="event-auditing-enable-export"></a>

When the value of the `audit_logs` cluster parameter is `enabled`, `ddl`, `dml_read`, or `dml_write`, you must also enable Amazon DocumentDB to export logs to Amazon CloudWatch. If you omit either of these steps, audit logs will not be sent to CloudWatch.

When creating a cluster, performing a point-in-time-restore, or restoring a snapshot, you can enable CloudWatch Logs by following these steps.

------
#### [ Using the AWS Management Console ]

To enable Amazon DocumentDB exporting logs to CloudWatch using the console, see the following topics:
+ **When creating a cluster** — In [Creating a cluster and primary instance using the AWS Management Console](db-cluster-create.md#db-cluster-create-con), see **Create a Cluster: Additional Configurations** (step 5, **Log exports**)
+ **When modifying an existing cluster** — [Modifying an Amazon DocumentDB cluster](db-cluster-modify.md)
+ **When performing a cluster snapshot restore** — [Restoring from a cluster snapshot](backup_restore-restore_from_snapshot.md)
+ **When performing a point-in-time restore** — [Restoring to a point in time](backup_restore-point_in_time_recovery.md)

------
#### [ Using the AWS CLI ]

**To enable audit logs when creating a new cluster**  
The following code creates the cluster `sample-cluster` and enables CloudWatch audit logs.

**Example**  
For Linux, macOS, or Unix:  

```
aws docdb create-db-cluster \
    --db-cluster-identifier {{sample-cluster}} \
    --port 27017 \
    --engine docdb \
    --master-username {{master-username}} \
    --master-user-password {{password}} \
    --db-subnet-group-name {{default}} \
    --enable-cloudwatch-logs-exports audit
```
For Windows:  

```
aws docdb create-db-cluster ^
    --db-cluster-identifier {{sample-cluster}} ^
    --port 27017 ^
    --engine docdb ^
    --master-username {{master-username}} ^
    --master-user-password {{password}} ^
    --db-subnet-group-name {{default}} ^
    --enable-cloudwatch-logs-exports audit
```

**To enable audit logs when modifying an existing cluster**  
The following code modifies the cluster `sample-cluster` and enables CloudWatch audit logs.

**Example**  
For Linux, macOS, or Unix:  

```
aws docdb modify-db-cluster \
   --db-cluster-identifier {{sample-cluster}} \
   --cloudwatch-logs-export-configuration '{"EnableLogTypes":["audit"]}'
```
For Windows:  

```
aws docdb modify-db-cluster ^
   --db-cluster-identifier {{sample-cluster}} ^
   --cloudwatch-logs-export-configuration '{"EnableLogTypes":["audit"]}'
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
        "EnabledCloudwatchLogsExports": [
            "audit"
        ],
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

------

## Disabling auditing
<a name="event-auditing-disabling-auditing"></a>

You can disable auditing by disabling CloudWatch Logs export and disabling the `audit_logs` parameter.

### Disabling CloudWatch Logs export
<a name="event-auditing-disabling-logs-export"></a>

You can disable exporting audit logs using either the AWS Management Console or the AWS CLI.

------
#### [ Using the AWS Management Console ]

The following procedure uses the AWS Management Console to disable Amazon DocumentDB exporting logs to CloudWatch.

**To disable audit logs**

1. Sign in to the AWS Management Console, and open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb).

1. In the navigation pane, choose **Clusters**. Then choose the button to the left of the name of the cluster for which you want to disable exporting logs.

1. Choose **Actions**, and then choose **Modify**.

1. Scroll down to the **Log exports** section and choose **Disabled**.

1. Choose **Continue**.

1. Review your changes, and then choose when you want this change applied to your cluster.
   + **Apply during the next scheduled maintenance window**
   + **Apply immediately**

1. Choose **Modify cluster**.

------
#### [ Using the AWS CLI ]

The following code modifies the cluster `sample-cluster` and disables CloudWatch audit logs.

**Example**  
For Linux, macOS, or Unix:  

```
aws docdb modify-db-cluster \
   --db-cluster-identifier {{sample-cluster}} \
   --cloudwatch-logs-export-configuration '{"DisableLogTypes":["audit"]}'
```
For Windows:  

```
aws docdb modify-db-cluster ^
   --db-cluster-identifier {{sample-cluster}} ^
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

------

### Disabling the audit\_logs parameter
<a name="event-auditing-disabling-audit-parameter"></a>

To disable the `audit_logs` parameter for your cluster, you can modify the cluster so that it uses a parameter group where the `audit_logs` parameter value is `disabled`. Or you can modify the `audit_logs` parameter value in the cluster's parameter group so that it is `disabled`.

For more information, see the following topics:
+ [Modifying an Amazon DocumentDB cluster](db-cluster-modify.md)
+ [Modifying Amazon DocumentDB cluster parameter groups](cluster_parameter_groups-modify.md)

## Accessing your audit events
<a name="event-auditing-accessing"></a>

Use following steps to access your audit events on Amazon CloudWatch.

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. Make sure that you are in the same Region as your Amazon DocumentDB cluster.

1. In the navigation pane, choose **Logs**.

1. To find the audit logs for your cluster, from the list locate and choose **/aws/docdb/{{yourClusterName}}/audit**.

   The auditing events for each of your instances are available under each of the respective instance names.

## Filtering DML audit events
<a name="filtering-dml-events"></a>

### Getting started with DML audit filtering
<a name="w2aac39c57c21b3"></a>

DML audit events can be filtered before they are written to Amazon CloudWatch. To utilize this feature, audit log and DML logging must be enabled. Amazon DocumentDB supports filtering on `atype`, `command`, `user`, `namespace`, and `auditAuthorizationSuccess`.

**Note**  
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

Only database users/roles with privileged action `auditConfigure` can execute the above commands against `admindb` when setting or listing DML audit filters. You can either use one of the built-in roles from [`clusterAdmin`, `hostManager`, `root`] or create custom roles that have `auditConfigure` privileges. The following is an example of using existing roles with the `auditConfigure` privilege and an example with custom roles.

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
<a name="filtering-use-cases"></a>

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

**Note**  
All DML logs have `authCheck` as `atype`. Only DDL has a different `atype`. If you put a value other than `authCheck` in the `filter`, it will not produce a DML log in CloudWatch.

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

**Note**  
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

When using both in `$in` and `$nin`, the command will not be logged as there will be an implicit "and" between the conditions. In this example, regex will block the `find` command so nothing will be logged:

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