# Amazon DocumentDB instance lifecycle

The lifecycle of an Amazon DocumentDB instance includes creating, modifying, maintaining and upgrading, performing backups and restores, rebooting, and deleting the instance. This section provides information about how to complete these processes.

###### Topics

- [Adding an instance](db-instance-add.md "db-instance-add.md")
- [Describing
  instances](db-instance-view-details.md "db-instance-view-details.md")
- [Modifying an
  instance](db-instance-modify.md "db-instance-modify.md")
- [Rebooting an instance](db-instance-reboot.md "db-instance-reboot.md")
- [Deleting an instance](db-instance-delete.md "db-instance-delete.md")
  You can create a new Amazon DocumentDB instance using the AWS Management Console or the AWS CLI. To add an instance to a cluster, the cluster must be in an _available_ state. You cannot add an instance to a cluster that is stopped. If the cluster is stopped, first start the cluster, wait for the cluster to become _available_, and then add an instance. For more information, see [Stopping and starting an
  Amazon DocumentDB cluster](db-cluster-stop-start.md "db-cluster-stop-start.md").

###### Note

If you create an Amazon DocumentDB cluster using the console, an
instance is automatically created for you at the same time.
If you want to create additional instances, use one of the
following procedures.
