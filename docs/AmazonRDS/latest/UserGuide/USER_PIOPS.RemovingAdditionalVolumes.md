

# Removing additional storage volumes
<a name="USER_PIOPS.RemovingAdditionalVolumes"></a>

You can remove additional storage volumes from RDS for Oracle and RDS for SQL Server DB instances when they are no longer needed. Before removing a volume, make sure that you have moved all database files off the volume and that no database objects are referencing it. Verify that the volume status is `Not-in-use`.

**Important**  
You can't remove the primary storage volume. You can only remove additional storage volumes.

## Console
<a name="USER_PIOPS.RemovingAdditionalVolumes.console"></a>

**To remove an additional storage volume from a DB instance**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**.

1. Choose the DB instance that includes the volume that you want to remove.

1. Choose **Modify**.

1. In the **Storage** section, locate the additional storage volume that you want to remove.

1. Choose **Remove volume** for the volume you want to delete.
**Note**  
You can only remove volumes with a status of `Not-in-use`. If the volume is still in use, move all database files off the volume.

1. Choose **Continue**.

1. When the settings are as you want them, choose **Modify DB instance**.

## AWS CLI
<a name="USER_PIOPS.RemovingAdditionalVolumes.cli"></a>

To remove an additional storage volume from a DB instance, use the AWS CLI command [`modify-db-instance`](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-instance.html). Set the following parameter:
+ `--additional-storage-volumes` – JSON array specifying the remaining additional storage volumes. Omit the volume you want to remove from this array.

The following example removes the additional storage volume named `rdsdbdata3` from `mydbinstance` by specifying only the remaining volumes and applies the change immediately.

```
aws rds modify-db-instance \
	--db-instance-identifier mydbinstance \
	--additional-storage-volumes '[{ \
		"VolumeName": "rdsdbdata3", \
		"SetForDelete": true
	}]'
```

## RDS API
<a name="USER_PIOPS.RemovingAdditionalVolumes.api"></a>

To remove an additional storage volume from a DB instance, use the Amazon RDS API operation [`ModifyDBInstance`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBInstance.html). Set the following parameters:
+ `AdditionalStorageVolumes` – Array of additional storage volume specifications for the volumes you want to keep. Omit the volume you want to remove from this array.
+ `ApplyImmediately` – Set this option to `True` to apply the storage changes immediately. Set this option to `False` (the default) to apply the changes during the next maintenance window.