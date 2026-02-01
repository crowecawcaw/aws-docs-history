# OpenSearch Optimized Instances for Amazon OpenSearch Service domains

The OpenSearch optimized instance family for Amazon OpenSearch Service is a cost-effective solution for
storing large volumes of data. A domain with OpenSearch optimized instances use local storage as primary, with data copied synchronously to Amazon S3 as it arrives. This storage structure provides increased indexing throughput with high durability. OR1, OR2, OM2 uses uses Amazon Elastic Block Store (Amazon EBS) `gp3` or `io1` volumes locally whereas OI2 instances use local NVMe disks. The OpenSearch optimized instance family also supports
automatic data recovery in the event of failure. For information about OpenSearch optimized instance type
options, see [Current generation instance types](supported-instance-types.md#latest-gen "supported-instance-types.md#latest-gen").

If you're running indexing heavy operational analytics workloads such as log analytics,
observability, or security analytics, you can benefit from the improved performance and
compute efficiency of OpenSearch optimized instances. In addition, the automatic data recovery offered by OpenSearch optimized
instances improves the overall reliability of your domain.

OpenSearch Service sends storage-related OpenSearch optimized instance metrics to Amazon CloudWatch. For a list of available metrics, see
[OpenSearch Optimized Instances (OR1) metrics](managedomains-cloudwatchmetrics.md#managedomains-cloudwatchmetrics-or1 "managedomains-cloudwatchmetrics.md#managedomains-cloudwatchmetrics-or1").

OpenSearch optimized instances are available on-demand or with Reserved Instance pricing, with an hourly
rate for the instances and storage provisioned in Amazon EBS and Managed Storage Amazon S3.

###### Topics

- [Limitations](#or1-considerations "#or1-considerations")
- [Tuning for better ingestion throughput](#or1-ultrawarm-tuning "#or1-ultrawarm-tuning")
- [How OpenSearch optimized instances differ from
  other instances](#or1-optimized-instances "#or1-optimized-instances")
- [How OpenSearch optimized instances differ from UltraWarm
  instances](#or1-ultrawarm-differences "#or1-ultrawarm-differences")
- [Provisioning a domain with OpenSearch optimized instances](#or1-using "#or1-using")

## Limitations

Consider the following limitations when using OpenSearch optimized instances for your domain.

- Newly created domains must be running OpenSearch version 2.11 or
  higher.
- Exisiting domains must be running OpenSearch version 2.15 or higher.
- Your domain must have encryption at rest enabled. For more information, see
  [Encryption of data at rest for Amazon OpenSearch Service](encryption-at-rest.md "encryption-at-rest.md").
- If your domain uses dedicated master nodes, they must use Graviton instances.
  For more information about dedicated master nodes, see [Dedicated master nodes in
  Amazon OpenSearch Service](managedomains-dedicatedmasternodes.md "managedomains-dedicatedmasternodes.md").
- The refresh interval for indexes on OpenSearch optimized instances must be 10 seconds or
  higher. The default refresh interval for OpenSearch optimized instances is 10 seconds.
- If your domain has transitioned to using OpenSearch optimized instances, you can no longer transition back to regular instances.

## Tuning for better ingestion throughput

To get the best indexing throughput from your OpenSearch optimized instances, we recommend that you do
the following:

- Use large bulk sizes to improve buffer utilization. The recommended size is 10
  MB.
- Use multiple clients to improve parallel processing performance.
- Set your number of active primary shards to match the number of data nodes to
  maximize resource utilization.

## How OpenSearch optimized instances differ from

other instances

OpenSearch optimized instances differ from non-optimized instances in the following
ways:

- For OpenSearch optimized instances, indexing is only performed on primary
  shards.
- If OpenSearch optimized instances are configured with replicas, the indexing
  rate may appear lower than it actually is. For example, if there is one primary
  shard and one replica shard, the indexing rate might show a rate of 1000 when
  the actual indexing rate is 2000.
- OpenSearch optimized instances perform buffer operations prior to sending to
  a remote source. This results in higher ingestion latencies.

###### Note

The `IndexingLatency` metric is not affected, as it doesn’t
include time to sync translog.

- Replica shards can be a few seconds behind primary shards. You can monitor the
  lag using the `ReplicationLagMaxTime` Amazon CloudWatch metric

## How OpenSearch optimized instances differ from UltraWarm

instances

OpenSearch Service provides UltraWarm instances that are a cost-effective way to store large amounts
of read-only data. Both OpenSearch optimized and UltraWarm instances store data locally in Amazon EBS and
remotely in Amazon S3. However, OpenSearch optimized and UltraWarm instances differ in several important
ways:

- OpenSearch optimized instances keep a copy of data in _both_ your local and
  remote store. In UltraWarm instances, data is kept primarily in remote store to
  reduce storage costs. Depending on your usage patterns, data can be moved to
  local storage.
- OpenSearch optimized instances are active and can accept read and write operations, whereas the
  data on UltraWarm instances is read-only until you manually move it back to hot
  storage.
- UltraWarm relies on index snapshots for data durability. OpenSearch optimized instances, by
  comparison, perform replication and recovery behind the scenes. In the event of
  a red index, OpenSearch optimized instances will automatically restore missing shards from your
  remote storage in Amazon S3. The recovery time varies depending on the volume of data
  to be recovered.

For more information about UltraWarm storage, see [UltraWarm storage for Amazon OpenSearch Service](ultrawarm.md "ultrawarm.md").

## Provisioning a domain with OpenSearch optimized instances

You can select OpenSearch optimized instances for your data nodes when you create a new domain with the
AWS Management Console or the AWS Command Line Interface (AWS CLI). You can then index and query the data using your
existing tools.

1. Navigate to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/](https://console.aws.amazon.com/aos/ "https://console.aws.amazon.com/aos/").
2. In the left navigation pane, choose **Domains**.
3. Choose **Create domain**.
4. In the **Number of data nodes** section, expand the
   **Instance family** menu and choose
   **OpenSearch optimized**.
5. Choose the instance type and other storage settings.
6. In the **Encryption** section, make sure that
   **Enable encryption of data at rest** is
   selected.
7. Configure the rest of your domain and choose
   **Create**.
   To provision a domain that uses OpenSearch optimized storage using the AWS CLI, you must provide
   the value of the specific instance type size (such as OR1, OR2, OM2, or OI2) in the
   `InstanceType`.

The following example creates a domain with OR1 instances of size
`2xlarge` and enables encryption at rest.

```
aws opensearch create-domain \
  --domain-name `test-domain` \
  --engine-version OpenSearch_2.11 \
  --cluster-config "InstanceType=or1.2xlarge.search,InstanceCount=3,DedicatedMasterEnabled=true,DedicatedMasterType=r6g.large.search,DedicatedMasterCount=3" \
  --ebs-options "EBSEnabled=true,VolumeType=gp3,VolumeSize=200" \
  --encryption-at-rest-options Enabled=true \
  --advanced-security-options "Enabled=true,InternalUserDatabaseEnabled=true,MasterUserOptions={MasterUserName=`test-user`,MasterUserPassword=`test-password`}" \
  --node-to-node-encryption-options Enabled=true \
  --domain-endpoint-options EnforceHTTPS=true \
  --access-policies '{"Version": "2012-10-17",		 	 	 "Statement":[{"Effect":"Allow","Principal":{"AWS":"*"},"Action":"es:*","Resource":"arn:aws:es:`us-east-1`:`account-id`:domain/`test-domain`/*"}]}'
```

The following example creates a domain with OI2 instances of size
`large` and enables encryption at rest. Note that OI2 instances do not require EBS configuration as they use local NVMe storage.

```
aws opensearch create-domain \
  --domain-name `test-domain-oi2` \
  --engine-version OpenSearch_2.11 \
  --cluster-config "InstanceType=oi2.2xlarge.search,InstanceCount=3,DedicatedMasterEnabled=true,DedicatedMasterType=r6g.large.search,DedicatedMasterCount=3" \
  --encryption-at-rest-options Enabled=true \
  --advanced-security-options "Enabled=true,InternalUserDatabaseEnabled=true,MasterUserOptions={MasterUserName=`test-user`,MasterUserPassword=`test-password`}" \
  --node-to-node-encryption-options Enabled=true \
  --domain-endpoint-options EnforceHTTPS=true \
  --access-policies '{"Version": "2012-10-17",		 	 	 "Statement":[{"Effect":"Allow","Principal":{"AWS":"*"},"Action":"es:*","Resource":"arn:aws:es:`us-east-1`:`account-id`:domain/`test-domain-oi2`/*"}]}'
```
