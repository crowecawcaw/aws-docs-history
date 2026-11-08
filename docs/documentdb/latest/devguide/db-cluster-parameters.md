

# Amazon DocumentDB cluster settings
<a name="db-cluster-parameters"></a>

When you create or modify a cluster, it is important to understand which parameters are immutable and which are modifiable after the cluster has been created. The following table lists all the settings, or parameters, that are specific to a cluster. As specified in the table, some are modifiable, others are not.

**Note**  
These settings should not be confused with Amazon DocumentDB cluster parameter groups and their parameters. For more information about cluster parameter groups, see [Managing Amazon DocumentDB cluster parameter groups](cluster_parameter_groups.md). 


| Parameter | Modifiable | Notes | 
| --- | --- | --- | 
| DBClusterIdentifier | Yes | Naming constraints:+  Length is [1—63] letters, numbers, or hyphens. <br />+  First character must be a letter. <br />+  Cannot end with a hyphen or contain two consecutive hyphens. <br />+  Must be unique for all clusters across Amazon RDS, Amazon Neptune, and Amazon DocumentDB per AWS account, per Region.  | 
| Engine | No | Must be docdb. | 
| BackupRetentionPeriod | Yes | Must be between [1-35] days. | 
| DBClusterParameterGroupName | Yes | Naming constraints:+  Length is [1—255] alphanumeric characters. <br />+  First character must be a letter. <br />+  Cannot end with a hyphen or contain two consecutive hyphens.  | 
| DBSubnetGroupName | No | After a cluster has been created, you cannot modify the cluster's subnet. | 
| EngineVersion | No |  +  If you omit `--engine-version` or specify `--engine-version 8.0`, Amazon DocumentDB uses the newest 8.0 minor version available in the AWS Region. This version advances as new 8.0 minor versions are released. <br />+  If you specify `--engine-version 5.0`, Amazon DocumentDB uses the 5.0 long-term support (LTS) minor version. This version changes only when Amazon DocumentDB declares a new 5.0 LTS minor version. <br />+  If you specify a fully-qualified version, such as `--engine-version 8.0.1` or `--engine-version 5.0.2`, Amazon DocumentDB uses exactly the version that you specify.   | 
| KmsKeyId | No | If you choose to encrypt your cluster, you cannot change the AWS KMS key that you used to encrypt your cluster. | 
| MasterUsername | No | After a cluster has been created, you cannot modify the `MasterUsername`.<br />Naming constraints:+  Length is [1—63] alphanumeric characters. <br />+  First character must be a letter. <br />+  Cannot be a word reserved by the database engine.  | 
| MasterUserPassword | Yes | Constraints:+  Length is [8—100] printable ASCII characters. <br />+  Can use any printable ASCII characters except for the following:   **/** (forward slash)   **"** (double quotation mark)   **@** (at symbol)    | 
| Port | Yes | The port number applies to all instances in the cluster. | 
| PreferredBackupWindow | Yes |  | 
| PreferredMaintenanceWindow | Yes |  | 
| StorageEncrypted | No | If you choose to encrypt your cluster, it cannot be unencrypted. | 
| StorageType | Yes | The storage type for the DB cluster: Standard (`standard`) or I/O-Optimized (`iopt1`).<br />Default: `standard`<br />This parameter can be configured with `CreateDBCluster` and `ModifyDBCluster`.<br />For more information, see [Amazon DocumentDB cluster storage configurations](db-cluster-storage-configs.md). | 
| Tags | Yes |  | 
| VpcSecurityGroupIds | No | After a cluster has been created, you cannot modify the VPC that the cluster resides in. | 