

# Setting up managed disaster recovery in Amazon OpenSearch Service
<a name="disaster-recovery"></a>

Amazon OpenSearch Service managed disaster recovery (DR) replicates data from a primary domain in one AWS Region to a secondary domain in another Region. The service manages the connection between the domains and encrypts replicated data in transit, so you don't need to configure network connectivity, such as VPC peering, between the domains.

When you set up DR, the service copies each existing index from the primary domain to the secondary domain. After this initial copy, the service asynchronously replicates new changes from the primary domain, and the secondary domain indexes them.

**Important**  
DR is supported only when both the primary and secondary domains run OpenSearch 3.7 or later. To upgrade a domain, see [Upgrading Amazon OpenSearch Service domains](version-migration.md).

DR uses an active-passive model. Both domains are available for read operations, but only the primary domain accepts write operations. If the primary domain becomes unavailable, you can manually fail over to the secondary domain. You can also perform a planned switchover to exchange the primary and secondary roles without data loss.

Use [Multi-AZ](managedomains-multiaz.md) to protect a domain from Availability Zone failures within one AWS Region. Use DR when your recovery plan requires a domain in another Region.

**Topics**
+ [Requirements and limitations](#disaster-recovery-requirements)
+ [Data and resources that DR replicates](#disaster-recovery-replication-scope)
+ [Closed indexes](#disaster-recovery-closed-indexes)
+ [Set up disaster recovery](#disaster-recovery-setup)
+ [Check replication status](#disaster-recovery-status)
+ [Remove the replication relationship](#disaster-recovery-remove)
+ [Disaster recovery API operations](#disaster-recovery-operations)
+ [CloudWatch metrics](#disaster-recovery-cloudwatch-metrics)
+ [Perform a planned switchover](#disaster-recovery-switchover)
+ [Perform an unplanned failover](#disaster-recovery-failover)
+ [Fail back after a failover](#disaster-recovery-failback)
+ [Recover from a long secondary-domain outage](#disaster-recovery-replication-interruption)
+ [Upgrade domains that use DR](#disaster-recovery-upgrade)
+ [Operational guidance](#disaster-recovery-operational-guidance)
+ [Pricing](#disaster-recovery-pricing)

## Requirements and limitations
<a name="disaster-recovery-requirements"></a>

Before you set up DR, review the following requirements and limitations:
+ Both domains must run the same OpenSearch version, 3.7 or later. If the versions differ later, for example during an upgrade, you can't perform a switchover until both domains run the same version. For more information, see [Upgrade domains that use DR](#disaster-recovery-upgrade).
+ Both domains must be in the same AWS account and in different AWS Regions. A domain can have only one replication peer.
+ Both domains must have [fine-grained access control](fgac.md) and [node-to-node encryption](ntn.md) enabled.
+ The secondary domain must be empty. It can't contain any indexes other than system indexes, because DR copies all indexes from the primary domain to the secondary domain.
+ Both domains index all of the data, and each index has the same number of primary shards and replicas on both domains. For consistent performance after a switchover or failover, configure the domains with similar CPU, memory, and storage capacity.
+ The secondary domain must have at least as much total storage as the primary domain, and enough free storage for the primary domain's current index data. DR checks storage only when you set up the replication relationship.
+ Warm and cold storage aren't supported. Neither domain can use [UltraWarm](ultrawarm.md), [cold storage](cold-storage.md), or the writable warm tier of [multi-tier storage](multi-tier-storage.md).
+ Domains that use the [Optimized engine for log analytics](optimized-log-analytics.md) aren't supported.
+ [Automatic semantic enrichment](opensearch-semantic-enrichment.md) isn't supported on domains that use DR replication. You can't pair domains when either domain contains an index that has automatic semantic enrichment enabled. Delete these indexes before you create the replication relationship.

  While the relationship exists, you can't enable automatic semantic enrichment for a new or existing index on either domain. To use automatic semantic enrichment again, first remove the replication relationship.
+ Failover is manual. OpenSearch Service doesn't determine when to fail over or automatically promote the secondary domain. To automate failover, build your own automation that calls `FailoverReplication`, for example in response to CloudWatch alarms.
+ DR doesn't redirect your applications after a switchover or failover. Update your applications to send writes to the new primary domain.

## Data and resources that DR replicates
<a name="disaster-recovery-replication-scope"></a>

DR replicates the following data and resources from the primary domain:
+ Indexes and documents
+ Index settings
+ Aliases
+ Data streams

DR doesn't replicate the following resources:
+ Index templates, including composable index templates
+ Ingest pipelines
+ Index State Management (ISM) policies
+ Roles
+ Cluster settings

**Important**  
Before a switchover or failover, create the same index templates, ingest pipelines, ISM policies, and roles on the secondary domain. Without the required resources on the new primary, data stream rollover can fail, new indexes don't inherit the expected settings and mappings, and writes that use an ingest pipeline fail.

Use infrastructure as code to keep the domain configurations and non-replicated resources consistent. You can use the `CompareDomainConfiguration` API to identify differences in key configuration categories between the domains.

## Closed indexes
<a name="disaster-recovery-closed-indexes"></a>

A closed index isn't protected by DR replication. When you close an index on the primary domain, DR removes its copy from the secondary domain. If you fail over while the index is closed, the index isn't available on the secondary domain.

When you reopen the index, DR copies the entire index to the secondary domain again. The index is protected after this copy finishes. Copying a large index can take a long time.

## Set up disaster recovery
<a name="disaster-recovery-setup"></a>

Create and configure both domains before you establish the replication relationship. We recommend that you use infrastructure as code so that you can apply consistent domain configurations and non-replicated resources in both Regions.

------
#### [ Console ]

**To set up disaster recovery**

1. Open the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home).

1. In the navigation pane, choose **Domains**, and then choose the domain that will be the primary domain.

1. In the **General information** section, for **Disaster recovery**, choose **Set up**.

1. For **Secondary domain ARN**, enter the ARN of the secondary domain.

1. Choose **Validate prerequisites**. If the domains are compatible, the console confirms that they can be paired for disaster recovery. Otherwise, the console describes each issue that prevents pairing. Fix the issues, and then validate again. For the requirements, see [Requirements and limitations](#disaster-recovery-requirements).

1. Choose **Create and enable disaster recovery**. Creating the replication relationship can take several minutes.

------
#### [ AWS CLI ]

Call `AddReplicationPeer` in the Region of the primary domain. The following AWS CLI command adds the secondary domain as a replication peer:

```
aws opensearch add-replication-peer \
  --domain-name {{primary-domain-name}} \
  --peer-domain-arn arn:aws:es:{{secondary-region}}:{{account-id}}:domain/{{secondary-domain-name}} \
  --region {{primary-region}}
```

To validate the domains without creating the replication relationship, add the `--dry-run` option. OpenSearch Service creates the relationship asynchronously. To check when replication is active, see [Check replication status](#disaster-recovery-status).

------

## Check replication status
<a name="disaster-recovery-status"></a>

After you set up DR, and after each switchover or failover, check the role of each domain and the status of the replication relationship.

------
#### [ Console ]

**To check replication status**

1. Open the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home).

1. In the navigation pane, choose **Domains**, and then choose either domain.

1. In the **General information** section, for **Disaster recovery**, choose **Manage**. The **Disaster recovery** page shows the primary domain, the secondary domain, and the replication status.

------
#### [ AWS CLI ]

The following AWS CLI command calls `DescribeDomainReplication` for either domain. Run the command in that domain's Region:

```
aws opensearch describe-domain-replication \
  --domain-name {{domain-name}} \
  --region {{region}}
```

The response includes the role of the domain that you specify and, for its peer, the peer's role and the status of the relationship. The status is `ACTIVE` when replication is running.

```
{
  "DomainArn": "arn:aws:es:{{primary-region}}:{{account-id}}:domain/{{primary-domain-name}}",
  "Role": "PRIMARY",
  "Peers": [
    {
      "PeerDomainArn": "arn:aws:es:{{secondary-region}}:{{account-id}}:domain/{{secondary-domain-name}}",
      "PeerRole": "SECONDARY",
      "Status": "ACTIVE"
    }
  ]
}
```

------

## Remove the replication relationship
<a name="disaster-recovery-remove"></a>

When you remove the replication relationship, replication stops for both domains. Both domains become standalone domains and keep their data. To protect a domain again, set up DR with an empty secondary domain.

------
#### [ Console ]

**To remove the replication relationship**

1. Open the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home).

1. In the navigation pane, choose **Domains**, and then choose either domain.

1. In the **General information** section, for **Disaster recovery**, choose **Manage**.

1. Choose **Actions**, and then choose **Remove replication peer**.

1. Enter **remove**.

1. Choose **Remove peer**.

------
#### [ AWS CLI ]

The following AWS CLI command calls `RemoveReplicationPeer`. Run the command in the Region of the domain that you specify, and specify the other domain as the peer:

```
aws opensearch remove-replication-peer \
  --domain-name {{domain-name}} \
  --peer-domain-arn arn:aws:es:{{peer-region}}:{{account-id}}:domain/{{peer-domain-name}} \
  --region {{region}}
```

The status is `PENDING_REMOVAL` while replication is being stopped. After the removal finishes, the relationship no longer appears in the `DescribeDomainReplication` response.

------

## Disaster recovery API operations
<a name="disaster-recovery-operations"></a>

The Amazon OpenSearch Service configuration API provides the following operations for managing DR:

`AddReplicationPeer`  
Adds a secondary domain as a replication peer.

`RemoveReplicationPeer`  
Removes the replication relationship. Each domain retains its data.

`SwitchoverReplication`  
Performs a planned switchover without data loss and exchanges the primary and secondary roles. Call this operation on the secondary domain that you want to promote.

`FailoverReplication`  
Unilaterally promotes a secondary domain to primary. Call this operation on the secondary domain that you want to promote.

`DescribeDomainReplication`  
Describes the relationship, including the role and replication status of each domain.

`CompareDomainConfiguration`  
Compares key configuration categories between two domains and reports the differences.

For API syntax and response details, see the [Amazon OpenSearch Service API Reference](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/Welcome.html).

## CloudWatch metrics
<a name="disaster-recovery-cloudwatch-metrics"></a>

The secondary domain publishes the following DR metrics to Amazon CloudWatch every minute. The primary domain doesn't publish these metrics. We recommend that you create CloudWatch alarms for these metrics. For information about viewing metrics, see [Monitoring OpenSearch cluster metrics with Amazon CloudWatch](managedomains-cloudwatchmetrics.md).


**Disaster recovery metrics**  

| Metric | Description | Unit | 
| --- | --- | --- | 
| DisasterRecoveryReplicationLagTime | The approximate amount of time that the secondary domain is behind the primary domain. This metric can report values up to 10 seconds even when the secondary domain is fully caught up. | Milliseconds | 
| DisasterRecoveryReplicationLagOps | The number of changes that the secondary domain hasn't applied. A value of 0 means that the secondary domain is caught up. When the primary domain is receiving writes, this value is usually greater than 0, and its typical value depends on your write rate. | Count | 
| DisasterRecoveryBootstrappingIndices | The number of indexes performing their first full copy from the primary domain. This value can be greater than 0 immediately after setup or after you create a new index. It should return to 0 after the copy finishes. | Count | 
| DisasterRecoveryDegradedIndices | The number of indexes that are replicating but aren't fully healthy. This value should be 0. | Count | 
| DisasterRecoveryFailedIndices | The number of indexes where replication stopped because of an error. These indexes no longer receive changes from the primary domain. This value should be 0. | Count | 

## Perform a planned switchover
<a name="disaster-recovery-switchover"></a>

Use a planned switchover when both domains are available and you want to move your workload to the secondary Region, for example to rehearse your recovery procedure or to perform maintenance. Before the switchover, verify that both domains run the same engine version, compare the domain configurations, and verify that the secondary domain contains the required non-replicated resources.

OpenSearch Service coordinates with the current primary domain, replicates any pending changes, and exchanges the primary and secondary roles without data loss. During the switchover, neither domain accepts writes for a short time, so configure your applications to retry failed writes. After the switchover, the former primary domain becomes the secondary domain, and replication continues in the reverse direction.

------
#### [ Console ]

**To perform a planned switchover**

1. Open the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home).

1. In the navigation pane, choose **Domains**, and then choose the secondary domain.

1. In the **General information** section, for **Disaster recovery**, choose **Manage**.

1. Choose **Switchover**.

1. Enter **confirm**.

1. Choose **Start switchover**.

------
#### [ AWS CLI ]

The following AWS CLI command calls `SwitchoverReplication` in the Region of the secondary domain that you want to promote. For the peer, specify the current primary domain:

```
aws opensearch switchover-replication \
  --domain-name {{secondary-domain-name}} \
  --peer-domain-arn arn:aws:es:{{primary-region}}:{{account-id}}:domain/{{primary-domain-name}} \
  --region {{secondary-region}}
```

The status is `SWITCHING_OVER` while the switchover is in progress. To confirm the new roles, see [Check replication status](#disaster-recovery-status).

------

**Important**  
After the switchover, redirect application writes to the new primary domain. Amazon OpenSearch Service doesn't update your application configuration or endpoints.

## Perform an unplanned failover
<a name="disaster-recovery-failover"></a>

Use an unplanned failover when the primary domain is unavailable and you decide to promote the secondary domain. OpenSearch Service promotes the secondary domain without coordinating with the primary domain.

**Warning**  
An unplanned failover can cause data loss. Writes that the old primary domain accepted but didn't replicate before the failover are lost, and the replication lag at the time of the failover limits this loss. If clients keep writing to the old primary domain after the failover, those writes also aren't replicated to the new primary domain.

------
#### [ Console ]

**To perform an unplanned failover**

1. Open the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home).

1. In the navigation pane, choose **Domains**, and then choose the secondary domain.

1. In the **General information** section, for **Disaster recovery**, choose **Manage**.

1. Choose **Failover**.

1. Select the check box to acknowledge that data might be lost.

1. Enter **failover**.

1. Choose **Fail over**.

------
#### [ AWS CLI ]

The following AWS CLI command calls `FailoverReplication` in the Region of the secondary domain that you want to promote. For the peer, specify the current primary domain. Because a failover can lose data, you must include the `--allow-data-loss` option:

```
aws opensearch failover-replication \
  --domain-name {{secondary-domain-name}} \
  --peer-domain-arn arn:aws:es:{{primary-region}}:{{account-id}}:domain/{{primary-domain-name}} \
  --allow-data-loss \
  --region {{secondary-region}}
```

The status is `FAILING_OVER` while the failover is in progress. To confirm the new roles, see [Check replication status](#disaster-recovery-status).

------

After the failover, redirect application writes to the new primary domain, and stop clients from writing to the former primary domain. Review the per-index replication status before you rely on the new primary for recovery.

The former primary domain doesn't rejoin replication automatically. Its replication status is `EJECTED`, and DR doesn't protect the new primary domain until you pair it with a secondary domain again. When OpenSearch Service can reach the former primary domain again, the domain becomes read-only. If the former primary domain kept running during the failure, for example during a network partition, clients that could still reach it might have written to it after the failover. Those writes aren't replicated to the new primary domain. For information about saving those writes before you fail back, see [Fail back after a failover](#disaster-recovery-failback).

## Fail back after a failover
<a name="disaster-recovery-failback"></a>

After a failover, DR doesn't resynchronize the former primary domain. To protect the new primary domain, pair it with an empty secondary domain, and DR copies all indexes to that domain. To return the primary role to the original Region, use a domain in the original Region as the new secondary domain, and then perform a planned switchover after the copy finishes.

**To fail back after a failover**

1. When the original Region is available, remove the replication relationship from the former primary domain. In the console, start from the former primary domain. With the AWS CLI, specify the former primary domain as the domain and the new primary domain as the peer. For instructions, see [Remove the replication relationship](#disaster-recovery-remove).

1. Delete all indexes except system indexes from the former primary domain, or create a new domain in the original Region. The secondary domain must be empty when you set up DR.
**Important**  
The former primary domain might contain writes that the new primary domain doesn't have. These include writes that weren't replicated before the failover and, if the former primary domain kept running, writes that clients made to it after the failover. Before you delete its indexes, save any data that you need, for example by taking a [manual snapshot](managedomains-snapshots.md).

1. Set up DR with the new primary domain as the primary domain and the empty domain in the original Region as the secondary domain. For instructions, see [Set up disaster recovery](#disaster-recovery-setup).

1. Wait for the initial copy to finish. The `DisasterRecoveryBootstrappingIndices` metric returns to 0 after all indexes are copied. Copying a large amount of data can take several hours.

1. (Optional) To make the domain in the original Region the primary domain again, perform a planned switchover. For instructions, see [Perform a planned switchover](#disaster-recovery-switchover).

## Recover from a long secondary-domain outage
<a name="disaster-recovery-replication-interruption"></a>

The primary domain keeps a limited history of index operations so that the secondary domain can replay changes after an interruption. If the secondary domain is unavailable for longer than this history is retained, DR can't catch up the affected indexes.

The affected indexes on the secondary domain remain searchable, but their results are stale. For example, a search can return an older version of an updated document or a document that was deleted from the primary domain. The overall domain replication status can still be `ACTIVE` while the per-index replication status identifies the affected indexes as failed.

To recover an affected index, initiate a new full copy, or re-bootstrap, from the secondary domain. The index is protected again after the copy finishes.

## Upgrade domains that use DR
<a name="disaster-recovery-upgrade"></a>

When you upgrade the engine version of domains that use DR, upgrade the secondary domain first, and then upgrade the primary domain. You can't perform a switchover while the domains run different versions. The steps depend on the upgrade method that you use. For information about upgrade methods, see [Choose an upgrade method](version-migration.md#upgrade-methods).

### In-place upgrades
<a name="disaster-recovery-upgrade-blue-green"></a>

An in-place upgrade upgrades the existing cluster of a domain and runs as a blue/green deployment. In-place upgrades work while DR is active, so you don't need to remove the replication relationship.

**To upgrade domains with an in-place upgrade**

1. Upgrade the secondary domain to the new version.

1. Validate your workload on the secondary domain. For example, test your read requests against the secondary domain, and check the DR metrics to confirm that replication is healthy.

1. Upgrade the primary domain to the same version.

Upgrade the primary domain as soon as you validate the secondary domain. Don't run the domains on different versions longer than necessary.

### Clone-based upgrades
<a name="disaster-recovery-upgrade-clone"></a>

A [clone-based upgrade](version-migration.md#how-clone-based-works) creates a cloned cluster of the domain on the new version. After cutover, OpenSearch Service keeps the original cluster, which the upgrade documentation calls the primary cluster, for the retention period that you set. If you don't set a retention period, OpenSearch Service deletes the original cluster immediately after cutover.

If you use a clone-based upgrade, remove the replication relationship before you upgrade either domain. Set up DR again only after both upgrades finish and the original clusters of both domains are deleted. Until a domain's original cluster is deleted, you can roll the domain back to it, which returns the domain to the earlier version. DR doesn't protect the primary domain until you set up DR again and the initial copy finishes.

**To upgrade domains with a clone-based upgrade**

1. Remove the replication relationship. Both domains become standalone domains and keep their data. For instructions, see [Remove the replication relationship](#disaster-recovery-remove).

1. Upgrade the secondary domain, and validate your workload on it.

1. Upgrade the primary domain to the same version.

1. Wait until the original clusters of both domains are deleted. OpenSearch Service deletes each original cluster when its retention period ends. To delete an original cluster sooner, see [Delete the primary cluster early](starting-upgrades.md#console-clone-delete).

1. Delete all indexes except system indexes from the secondary domain, or create a new secondary domain that runs the new version. The secondary domain must be empty when you set up DR.

1. Set up DR again. For instructions, see [Set up disaster recovery](#disaster-recovery-setup). DR copies all indexes from the primary domain to the secondary domain. The `DisasterRecoveryBootstrappingIndices` metric returns to 0 after the copy finishes. Copying a large amount of data can take several hours.

## Operational guidance
<a name="disaster-recovery-operational-guidance"></a>
+ Rehearse Region moves regularly with a planned switchover, including how your applications discover and connect to the current primary domain. A failover ends the replication relationship and requires a full copy to protect the new primary domain again, so test your failover procedure on non-production domains.
+ Keep the domain configurations and non-replicated resources synchronized with infrastructure as code. Use `CompareDomainConfiguration` to detect differences between the domains.
+ When you upgrade the engine version, upgrade the secondary domain first and the primary domain last. If you use a clone-based upgrade, remove the replication relationship first. For more information, see [Upgrade domains that use DR](#disaster-recovery-upgrade).
+ Use `DescribeDomainReplication` and per-index replication status to verify that the secondary domain is current before a planned switchover.

## Pricing
<a name="disaster-recovery-pricing"></a>

There is no additional charge for managed disaster recovery. You pay for both domains at standard Amazon OpenSearch Service rates, and standard AWS data transfer charges apply to the data that DR replicates across Regions. For more information, see [Amazon OpenSearch Service pricing](https://aws.amazon.com/opensearch-service/pricing/) on the AWS website.