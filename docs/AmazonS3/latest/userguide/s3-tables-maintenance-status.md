# S3 Tables maintenance job status

S3 Tables maintenance jobs run periodically for your S3 tables or table buckets. You
can query the status of these jobs with the `GetTableMaintenanceJobStatus`
API.

**To get the status of your maintenance jobs by using the AWS CLI**

The following example will get the statuses of maintenance jobs using the
`GetTableMaintenanceJobStatus` API.

```
aws s3tables get-table-maintenance-job-status \
   --table-bucket-arn="arn:aws:s3tables:arn:aws::111122223333:bucket/`amzn-s3-demo-bucket1`" \
   --namespace="`mynamespace`" \
   --name="`testtable`"
```

For more information, see [get-table-maintenance-job-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3tables/get-table-maintenance-job-status.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3tables/get-table-maintenance-job-status.html") in the
_AWS CLI Command Reference_.

S3 Tables maintenance jobs can transition between four possible statuses:

- `Successful`
- `Failed`
- `Disabled`
- `Not_Yet_Run`
  Jobs with a failed status will include a failure message. The following list
  describes possible failure messages.

- Encountered Iceberg validation exception when trying to read table. Ensure that your table is readable, adheres to the Iceberg specification, and contains only S3 paths that begin with your S3 Table alias.
- Iceberg Snapshot management does not currently support user defined tags or references.
- Iceberg table maintenance configuration is incompatible with 'history.expire.max-snapshot-age-ms' and 'history.expire.min-snapshots-to-keep' table properties.
- Iceberg snapshot management and unreferenced file removal is not supported when the 'gc.enabled' table property is false. Ensure that this property is unset or explicitly set to true.
- Failed to commit because of out of date metadata. Maintenance will be retried at the next available opportunity.
- Insufficient access to perform table maintenance. Ensure that the key used to encrypt the table is active, exists, and has a resource policy granting access to the S3 service principal `maintenance.s3tables.amazonaws.com`.

###### Note

For more information on AWS KMS permissions for S3 Tables, see [Permission requirements for S3 Tables SSE-KMS encryption](s3-tables-kms-permissions.md "s3-tables-kms-permissions.md").

- Internal error
