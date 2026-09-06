

# Restore testing inferred metadata
<a name="restore-testing-inferred-metadata"></a>

Restoring a recovery point requires restore metadata. To perform restore tests, AWS Backup automatically infers metadata that is likely to result in a successful restore. The command `get-restore-testing-inferred-metadata` can be used to preview what AWS Backup will infer. The command `get-restore-job-metadata` returns the set of metadata inferred by AWS Backup. Note that for some resource types (Amazon FSx), AWS Backup is not able to infer a complete set of metadata.

*Inferred restore metadata* is determined during the restore testing process. You can override certain restore metadata keys by including the parameter `RestoreMetadataOverrides` in the body of `RestoreTestingSelection`. Some metadata overrides are not available in the AWS Backup console.

Each supported resource has both inferred restore metadata keys and values, and overridable restore metadata keys. Only `RestoreMetadataOverrides` key value pairs or nested key value pairs marked with {{required for successful restore}} are necessary to include; the others are optional. Note that key values are not case sensitive.

**Important**  
AWS Backup can infer that a resource should be restored to the default setting, such as an Amazon EC2 instance or Amazon RDS cluster restored to the default VPC. However, if the default is not present, for example the default VPC or subnet has been deleted and no metadata override has been input, the restore will not be successful.


| Resource type | Inferred restore metadata keys and values | Overridable metadata | 
| --- | --- | --- | 
| **DynamoDB** | `deletionProtection`, where value is set to `false`<br />`encryptionType` is set to `Default`<br />`targetTableName`, where value is set to random value starting with `awsbackup-restore-test-` | `encryptionType`<br />`kmsMasterKeyArn` | 
| **Amazon EBS** | `availabilityZone`, whose value is set to a random availability zone<br />`encrypted`, whose value is set to `true` | `availabilityZone`<br />`iops`<br />`kmsKeyId`<br />`throughput`<br />`volumesize`<br />`volumetype` | 
| **Amazon EC2** | `disableApiTermination` value is set to `false`<br />`instanceType` value is set to the instanceType of the recovery point being restored<br />`requiredImdsV2` value is set to `true` | `iamInstanceProfileName` (null or `UseBackedUpValue`)<br />`instanceType`<br />`requireImdsV2`<br />`securityGroupIds`<br />`subnetId` | 
| **Amazon EFS** | `encrypted` value is set to `true`<br />`file-system-id` value is set to the file system ID of the recovery point being restored<br />`kmsKeyId value` is set to `alias/aws/elasticfilesystem`<br />`newFileSystem` value is set to `true`<br />`performanceMode` value is set to `generalPurpose` | `kmsKeyId`<br />`performanceMode` | 
| **Amazon FSx for Lustre** | `lustreConfiguration` has nested keys. One nested key is `automaticBackupRetentionDays`, the value of which is set to `0` | `kmsKeyId`<br />`lustreConfiguration` has nested key `logConfiguration`<br />`securityGroupIds`<br />`subnetIds`, {{required for successful restore}} | 
| **Amazon FSx for NetApp ONTAP** | `name` is set to a random value starting with `awsbackup_restore_test_`<br />`ontapConfiguration` has nested keys, including:+  `junctionPath` where `/name` is the name of the volume being restored <br />+  `sizeInMegabytes`, the value of which is set to the size in megabytes of the recovery point being restored <br />+  `snapshotPolicy` where the value is set to `none`  For FSx for ONTAP resources, the Storage Virtual Machine (SVM) that you specify in `storageVirtualMachineId` determines the subnet and Availability Zone of the restored volume. If you specify the `SubnetIds` parameter in the console, AWS Backup accepts but ignores it during the restore operation. <br />To restore to a different file system or Availability Zone, specify an SVM that belongs to the target file system in your `RestoreMetadataOverrides`. If you specify an SVM in the same file system, the volume is restored to that file system regardless of any subnet configuration that you specify in the console.  | `ontapConfiguration` has specific overrideable nested keys, including:+  `junctionPath` <br />+  `ontapVolumeType` <br />+  `securityStyle` <br />+  `sizeInMegabytes` <br />+  `storageEfficiencyEnabled` <br />+  `storageVirtualMachineId`, {{required for successful restore}} <br />+  `tieringPolicy`  | 
| **Amazon FSx for OpenZFS** | `openZfzConfiguration`, which has nested keys, including:+  `automaticBackupRetentionDays` with value set to `0` <br />+  `deploymentType` with value set to the deployment type of the recovery point being restored <br />+  `throughputCapacity`, whose value is based on the `deploymentType`. If `deploymentType` is `SINGLE_AZ_1`, the value is set to `64`; if the `deploymentType` is `SINGLE_AZ_2 or MULTI_AZ_1`, the value is set to `160`  | `kmsKeyId`<br />`openZfsConfiguration` has specific overridable nested keys, including:+  `deploymentType` <br />+  `throughputCapacity` <br />+  `diskiopsConfiguration` <br />`securityGroupIds`<br />`subnetIds` | 
| **Amazon FSx for Windows File Server** | `windowsConfiguration`, which has nested keys including:+  `automaticBackupRetentionDays` with value set to `0` <br />+  `deploymentType` with value set to the deployment type of the recovery point being restored <br />+  `throughputCapacity` with value set to `8`  | `kmsKeyId`<br />`securityGroupIds`<br />`subnetIds` {{required for successful restore}}<br />`windowsConfiguration`, with specific overridable nested keys+  `throughputCapacity` <br />+  `activeDirectoryId` {{required for successful restore}} <br />+  `preferredSubnetId`  | 
| **Amazon RDS, Aurora, Amazon DocumentDB, Amazon Neptune clusters** | `availabilityZones` with value set to a list of up to three random availability zones<br />`dbClusterIdentifier` with a random value starting with `awsbackup-restore-test`<br />`engine` with value set to the engine of the recovery point being restored | `availabilityZones`<br />`databaseName`<br />`dbClusterParameterGroupName`<br />`dbSubnetGroupName`<br />`enableCloudwatchLogsExports`<br />`enableIamDatabaseAuthentication`<br />`engine`<br />`engineMode`<br />`engineVersion`<br />`kmskeyId`<br />`port`<br />`optionGroupName`<br />`scalingConfiguration`<br />`vpcSecurityGroupIds` | 
| **Amazon RDS instances** | `dbInstanceIdentifier` with a random value starting with `awsbackup-restore-test-`<br />`deletionProtection` with value set to `false`<br />`multiAz` with value set to `false`<br />`publiclyAccessible` with value set to false | `allocatedStorage`<br />`availabilityZones`<br />`dbInstanceClass`<br />`dbName`<br />`dbParameterGroupName`<br />`dbSubnetGroupName`<br />`domain`<br />`domainIamRoleName`<br />`enableCloudwatchLogsExports`<br />`enableIamDatabaseAuthentication`<br />`iops`<br />`licensemodel`<br />`multiAz`<br />`optionGroupName`<br />`port`<br />`processorFeatures`<br />`publiclyAccessible`<br />`storageType`<br />`vpcSecurityGroupIds` | 
| **Amazon Simple Storage Service (Amazon S3)** | `destinationBucketName` with a random value starting with `awsbackup-restore-test-`<br />`encrypted ` with value set to `true`<br />`encryptionType` with value set to `SSE-S3`<br />`newBucket` with value set to `true`<br />`restoreACLs` specifies whether to restore ACLs. The value is `false` when you created the backup with `BackupACLs` disabled. Otherwise, the value is `true`. | `encryptionType`<br />`kmsKey`<br />`restoreACLs` | 

## Format for list-typed override values
<a name="restore-testing-inferred-metadata-list-format"></a>

Because `RestoreMetadataOverrides` is a map of string key-value pairs, override values that represent lists (such as `vpcSecurityGroupIds`, `availabilityZones`, `enableCloudwatchLogsExports`, `securityGroupIds`, and `subnetIds`) must be specified as JSON-array-encoded strings.

For example, to specify a single security group:

```
"vpcSecurityGroupIds": "[\"sg-012d52c68c6e88f00\"]"
```

To specify multiple security groups:

```
"vpcSecurityGroupIds": "[\"sg-012d52c68c6e88f00\",\"sg-abcdef01234567890\"]"
```

In AWS CloudFormation templates, you can use the `!Sub` intrinsic function to reference resource attributes within the JSON-array string:

```
RestoreMetadataOverrides:
  vpcSecurityGroupIds: !Sub '["${DBSecurityGroup.GroupId}"]'
```

For multiple values in CloudFormation:

```
RestoreMetadataOverrides:
  vpcSecurityGroupIds: !Sub '["${DBSecurityGroup.GroupId}","${AnotherSecurityGroup.GroupId}"]'
```

This JSON-array-string format applies to all list-typed overrides in the preceding table. For more examples of this format, see [Restore an RDS database](restoring-rds.md).