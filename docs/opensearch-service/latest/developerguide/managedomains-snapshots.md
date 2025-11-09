# Creating index snapshots in Amazon OpenSearch Service

Snapshots in Amazon OpenSearch Service are backups of a cluster's indexes and state. _State_ includes cluster settings, node information, index
settings, and shard allocation.

OpenSearch Service snapshots come in the following forms:

- **Automated snapshots** are only for cluster
  recovery. You can use them to restore your domain in the event of red cluster status
  or data loss. For more information, see [Restoring snapshots](managedomains-snapshot-restore.md "managedomains-snapshot-restore.md") below. OpenSearch Service
  stores automated snapshots in a preconfigured Amazon S3 bucket at no additional
  charge.
- **Manual snapshots** are for cluster recovery
  _or_ for moving data from one cluster to
  another. You have to initiate manual snapshots. These snapshots are stored in your
  own Amazon S3 bucket and standard S3 charges apply. If you have a snapshot from a
  self-managed OpenSearch cluster, you can use that snapshot to migrate to an OpenSearch Service
  domain. For more information, see [Migrating to
  Amazon OpenSearch Service](migration.md "migration.md").
  All OpenSearch Service domains take automated snapshots, but the frequency differs in the following
  ways:

- For domains running OpenSearch or Elasticsearch 5.3 and later, OpenSearch Service takes hourly
  automated snapshots and retains up to 336 of them for 14 days. Hourly snapshots are
  less disruptive because of their incremental nature. They also provide a more recent
  recovery point in case of domain problems.
- For domains running Elasticsearch 5.1 and earlier, OpenSearch Service takes daily automated
  snapshots during the hour you specify, retains up to 14 of them, and doesn't retain
  any snapshot data for more than 30 days.
  If your cluster enters red status, all automated snapshots fail while the cluster status
  persists. If you don't correct the problem within two weeks, you can permanently lose the
  data in your cluster. For troubleshooting steps, see [Red cluster status](handling-errors.md#handling-errors-red-cluster-status "handling-errors.md#handling-errors-red-cluster-status").

## Prerequisites

To create snapshots manually, you need to work with IAM and Amazon S3. Make sure you meet
the following prerequisites before you attempt to take a snapshot:

| Prerequisite | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| S3 bucket    | Create an S3 bucket to store manual snapshots for your OpenSearch Service<br>domain. For instructions, see [Creating a general purpose bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md") in the _Amazon Simple Storage Service User Guide_.<br>Remember the name of the bucket to use it in the following<br>places:<br>• The `Resource` statement of the IAM policy<br>attached to your IAM role<br>• The Python client used to register a snapshot repository<br>(if you use this method)<br>ImportantDo not apply an Amazon Glacier lifecycle rule to this bucket. Manual<br>snapshots don't support the Amazon Glacier storage class.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| IAM role     | Create an IAM role to delegate permissions to OpenSearch Service. For<br>instructions, see [Creating an IAM role (console)](../../../IAM/latest/UserGuide/id_roles_create_for-user.md#roles-creatingrole-user-console "../../../IAM/latest/UserGuide/id_roles_create_for-user.md#roles-creatingrole-user-console") in the _IAM User Guide_. The rest of this<br>chapter refers to this role as `TheSnapshotRole`.<br>**Attach an IAM policy**<br>Attach the following policy to `TheSnapshotRole` to<br>allow access to the S3 bucket:<br>``<br>`{<br>"Version":"2012-10-17",<br>"Statement": [{<br>"Action": [<br>"s3:ListBucket"<br>],<br>"Effect": "Allow",<br>"Resource": [<br>"arn:aws:s3:::`amzn-s3-demo-bucket`"<br>]<br>},<br>{<br>"Action": [<br>"s3:GetObject",<br>"s3:PutObject",<br>"s3:DeleteObject"<br>],<br>"Effect": "Allow",<br>"Resource": [<br>"arn:aws:s3:::`amzn-s3-demo-bucket`/*"<br>]<br>}<br>]<br>}`<br>``<br>For instructions to attach a policy to a role, see [Adding IAM identity permissions (console)](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policies-console "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policies-console") in the<br>_IAM User Guide_.<br>**Edit the trust<br>relationship**<br>Edit the trust relationship of `TheSnapshotRole` to<br>specify OpenSearch Service in the `Principal` statement as shown in the<br>following example:<br>``<br>`{<br>"Version":"2012-10-17",<br>"Statement": [{<br>"Sid": "",<br>"Effect": "Allow",<br>"Principal": {<br>"Service": "es.amazonaws.com"<br>},<br>"Action": "sts:AssumeRole"<br>}]<br>}`<br>``<br>For instructions to edit the trust relationship, see [Update a role trust policy](../../../IAM/latest/UserGuide/id_roles_update-role-trust-policy.md "../../../IAM/latest/UserGuide/id_roles_update-role-trust-policy.md") in the _IAM User Guide_. |
| Permissions  | In order to register the snapshot repository, you need to be able<br>to pass `TheSnapshotRole` to OpenSearch Service. You also need access<br>to the `es:ESHttpPut` action. To grant both of these<br>permissions, attach the following policy to the IAM role whose<br>credentials are being used to sign the request:<br>``<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Effect": "Allow",<br>"Action": "iam:PassRole",<br>"Resource": "arn:aws:iam::`123456789012`:role/`TheSnapshotRole`"<br>},<br>{<br>"Effect": "Allow",<br>"Action": "es:ESHttpPut",<br>"Resource": "arn:aws:es:`us-east-1`:`123456789012`:domain/`domain-name`/*"<br>}<br>]<br>}`<br>``<br>If your user or role doesn't have `iam:PassRole`<br>permissions to pass `TheSnapshotRole`, you might<br>encounter the following common error when you try to register a<br>repository in the next step:<br>``<br>$ python register-repo.py<br>{"Message":"User: arn:aws:iam::`123456789012`:user/`MyUserAccount`<br>is not authorized to perform: iam:PassRole on resource:<br>arn:aws:iam::`123456789012`:role/`TheSnapshotRole`"}<br>``                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

## Deleting manual

snapshots

To delete a manual snapshot, run the following command:

```
DELETE _snapshot/`repository-name`/`snapshot-name`
```

## Automating snapshots with Index State

Management

You can use the Index State Management (ISM) [snapshot](https://opendistro.github.io/for-elasticsearch-docs/docs/im/ism/policies/#snapshot "https://opendistro.github.io/for-elasticsearch-docs/docs/im/ism/policies/#snapshot") operation to automatically trigger snapshots of indexes based on
changes in their age, size, or number of documents. ISM is best when you need one
snapshot per index. If you need to snapshot of a group of indices, see [Automating snapshots with Snapshot
Management](managedomains-snapshot-mgmt.md "managedomains-snapshot-mgmt.md").

To use SM in OpenSearch Service, you need to register your own Amazon S3 repository. For an example ISM
policy using the `snapshot` operation, see [Sample
Policies](ism.md#ism-example "ism.md#ism-example").

## Using Curator for snapshots

If ISM doesn't work for index and snapshot management, you can use Curator instead. It
offers advanced filtering functionality that can help simplify management tasks on
complex clusters. Use [pip](https://pip.pypa.io/en/stable/installing/ "https://pip.pypa.io/en/stable/installing/")
to install Curator:

```
pip install elasticsearch-curator
```

You can use Curator as a command line interface (CLI) or Python API. If you use the
Python API, you must use version 7.13.4 or earlier of the legacy [elasticsearch-py](https://elasticsearch-py.readthedocs.io/ "https://elasticsearch-py.readthedocs.io/") client. It
doesn't support the opensearch-py client.

If you use the CLI, export your credentials at the command line and configure
`curator.yml` as follows:

```
client:
  hosts: search-`my-domain`.`us-west-1`.es.amazonaws.com
  port: 443
  use_ssl: True
  aws_region: `us-west-1`
  aws_sign_request: True
  ssl_no_validate: False
  timeout: 60

logging:
  loglevel: INFO
```
