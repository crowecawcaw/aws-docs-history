# Tear Down the High Availability Deployment

To tear down the deployment, you submit the Delete Stack CT against the HA Two-Tier stack, and the S3 bucket, and
you can request that RDS snapshots be deleted (they are deleted automatically after ten days, but they do cost a small amount while there).
Gather the stack IDs for the HA stack and the S3 bucket and then follow these steps. See
[Stack | Delete](../ctref/management-standard-stack-delete.md "../ctref/management-standard-stack-delete.md").
