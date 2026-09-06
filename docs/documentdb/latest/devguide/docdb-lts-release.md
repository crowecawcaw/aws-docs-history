

# Using a long-term support (LTS) release
<a name="docdb-lts-release"></a>

Amazon DocumentDB designates certain versions as Long-Term Support (LTS) releases. Database clusters that use LTS can stay on the same version longer and undergo fewer upgrade cycles than clusters that use non-LTS releases. LTS versions will be patched only in the event of critical stability and security patches without introducing new features. Additional optional patches may be released such as metrics to debug critical failures. These will be cumulatively applied with required patches.

## Current LTS Release
<a name="docdb-lts-current-release"></a>

The current LTS release for Amazon DocumentDB is:
+ Minor Version 5.0.0

To determine the version your cluster is on, see [How to check if my existing engine version 5.0.0 cluster is on LTS](#docdb-lts-check-version).

For more information about support timelines and release cycles for the LTS versions, see [Amazon DocumentDB engine version support dates](docdb-version-support-dates.md). Amazon DocumentDB will announce the next LTS version through standard communication channels.

**Note**  
An LTS release for Amazon DocumentDB 8.0 has not yet been designated. If you require LTS, use engine version 5.0.0 with Patch Version 3.0.17983 or later.

## Who should use LTS
<a name="docdb-lts-who-should-use"></a>

Amazon DocumentDB LTS releases are designed for clusters with limited upgrade windows. LTS is ideal for production environments where database availability directly impacts business operations.

**Consider LTS releases if:**
+ Your application has strict uptime requirements that limit upgrade opportunities
+ You have all required database engine features and enhancements your application needs

**Consider standard releases instead if:**
+ Your application can handle minimal interruption
+ You want the latest capabilities and enhancements as soon as they're released

**Important**  
Upgrades are **one-way operations** - you cannot downgrade after upgrading
Your cluster will experience brief downtime during the upgrade process

## How to create a new LTS cluster
<a name="docdb-lts-create-cluster"></a>

To create an LTS cluster, follow these steps:

1. In the Management Console, create a new engine version 5.0.0 cluster

1. Verify you're on engine version 5.0.0 after cluster creation using the AWS CLI:

```
aws docdb describe-db-clusters \
    --db-cluster-identifier {{mydocdbcluster}} \
    --query 'DBClusters[0].EngineVersion'
```

Output from this operation looks something like the following:

```
"5.0.0"
```

## How to upgrade from engine version 3.6.0 or 4.0.0 to a 5.0.0 LTS cluster
<a name="docdb-lts-upgrade-cluster"></a>

To upgrade to an LTS cluster, follow these steps:

1. In the Management Console, major version upgrade (MVU) your engine version 3.6.0 or 4.0.0 cluster to 5.0.0. For instructions on performing an MVU, see [Amazon DocumentDB in-place major version upgrade](docdb-mvu.md).

1. Verify you're on engine version 5.0.0 after upgrade using the AWS CLI:

```
aws docdb describe-db-clusters \
    --db-cluster-identifier {{mydocdbcluster}} \
    --query 'DBClusters[0].EngineVersion'
```

## How to check if my existing engine version 5.0.0 cluster is on LTS
<a name="docdb-lts-check-version"></a>

To check if your engine version 5.0.0 cluster is running an LTS version:

1. Verify you're on engine version 5.0.0 using the AWS CLI:

   ```
   aws docdb describe-db-clusters \
       --db-cluster-identifier {{mydocdbcluster}} \
       --query 'DBClusters[0].EngineVersion'
   ```

1. If needed, upgrade your existing engine version 5.0.0 cluster. For instructions on performing a patch update, see [Performing a patch update to a cluster's engine version](db-cluster-version-upgrade.md).