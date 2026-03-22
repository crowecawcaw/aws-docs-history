# Viewing storage volume details for your DB instance

You can view your storage volume configuration from the AWS Management Console or AWS
CLI. This includes details about both your primary storage volume and any additional storage
volumes attached to your DB instance.

The `StorageVolumeStatus` field indicates whether the volume is currently in
use by your database. A status of `Not-in-use` means the volume is attached but
it's not in use by the database engine or an RDS feature.
