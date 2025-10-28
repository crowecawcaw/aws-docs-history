Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Standard datashares

With standard datashares, you can share data across provisioned clusters, serverless
workgroups, Availability Zones, AWS accounts, and AWS Regions. You can share between
cluster types as well as between provisioned clusters and Amazon Redshift Serverless.

To share data, note the following provisioned cluster, serverless namespace, and
AWS account identifiers:

- Provisioned namespaces are identifiers that identify Amazon Redshift provisioned
  clusters. A namespace globally unique identifier (GUID) is automatically created
  during provisioned cluster creation and attached to the cluster. A namespace
  Amazon Resource Name (ARN) is in the
  arn:{partition}:redshift:{region}:{account-id}:namespace:{namespace-guid} format.
  You can see the namespace of a provisioned cluster on the cluster details page on
  the Amazon Redshift console.

In the data sharing workflow, the namespace GUID value and the namespace ARN
are used to share data with clusters in the AWS account. You can also find the
namespace for the current cluster by using the `current_namespace`
function.

- Serverless namespaces are identifiers that identify Amazon Redshift Serverless. A
  namespace globally unique identifier (GUID) is automatically created during
  Amazon Redshift Serverless creation and attached to the instance. A serverless namespace
  ARN is in the
  arn:{partition}:redshift-serverless:{region}:{account-id}:namespace/{namespace-guid}
  format.
- AWS accounts can be consumers for datashares and are each represented by a
  12-digit AWS account ID.
  For _standard datashares_, consider the
  following:

- When a producer cluster is deleted, Amazon Redshift deletes the datashares created by
  the producer cluster. When a producer cluster is backed up and restored, the
  created datashares still persist on the restored cluster. However, datashare
  permissions granted to other clusters are no longer valid on the restored cluster.
  Re-grant usage permissions of datashares to desired consumer clusters. The
  consumer database on the consumer cluster points to the datashare from the
  original cluster where the snapshot is taken. To query the shared data from the
  restored cluster, the consumer administrator creates a different database. Or the
  administrator can drop and recreate an existing consumer database to use the
  datashare from the newly restored cluster.
- When a consumer cluster is deleted and restored from a snapshot, the previous
  access shared to this cluster would no longer be valid and visible. If access to
  datashares is still required on the restored consumer cluster, the producer
  administrator must grant usage of datashares to the restored consumer cluster
  again. The consumer administrator must drop any stale consumer databases created
  from the inactive datashares. Then the administrator must recreate the consumer
  database from the datashare, after the producer re-granted the permissions. As the
  namespace GUID is different on a restored cluster from the original cluster,
  re-grant datashare permissions when the consumer or producer cluster is restored
  from backup.
