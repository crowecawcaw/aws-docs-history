# Using `neptune-export`

You can use the open-source
[`neptune-export`](https://github.com/aws/neptune-export "https://github.com/aws/neptune-export")
tool in two different ways:

- **As the [Neptune-Export
  service](export-service.md "export-service.md")**.   When you export data from Neptune using the Neptune-Export
  service, you trigger and monitor export jobs through a REST API.
- **As the [neptune-export
  Java command-line utility](export-utility.md "export-utility.md")**.   To use this command-line
  tool to export Neptune data, you have to run it in an environment where your
  Neptune DB cluster is accessible.
  Both the Neptune-Export service and the `neptune-export`
  command line tool publish data to Amazon Simple Storage Service (Amazon S3), encrypted using Amazon S3
  server-side encryption (`SSE-S3`).

###### Note

It is a best practice to [enable
access logging](../../../AmazonS3/latest/userguide/enable-server-access-logging.md "../../../AmazonS3/latest/userguide/enable-server-access-logging.md") on all Amazon S3 buckets, to let you audit all access
to those buckets.

If you try to export data from a Neptune DB cluster whose data is changing
while the export is happening, the consistency of the exported data is not
guaranteed. That is, if your cluster is servicing write traffic while an
export job is in progress, there may be inconsistencies in the exported data.
This is true whether you export from the primary instance in the cluster or
from one or more read replicas.

To guarantee that exported data is consistent, it is best to export from
a [clone of your DB cluster](manage-console-cloning.md "manage-console-cloning.md").
This both provides the export tool with a static version of your data and
ensures that the export job doesn't slow down queries in your original DB
cluster.

To make this easier, you can indicate that you want to clone the source
DB cluster when you trigger an export job. If you do, the export process
automatically creates the clone, uses it for the export, and then deletes
it when the export is finished.
