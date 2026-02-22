# Using a long-term support (LTS) release

Amazon DocumentDB designates certain versions as Long-Term Support (LTS) releases. Database clusters that use LTS can stay on the same version longer and undergo fewer upgrade cycles than clusters that use non-LTS releases. LTS versions will receive only critical stability and security patches without introducing new features.

## Current LTS Release

The current LTS release for Amazon DocumentDB is:

- Engine Version 5.0.0, Required Engine Patch Version 3.0.17983 or later

To determine the patch version your cluster is on, see [How to check if my existing engine version 5.0.0 cluster is on LTS](#docdb-lts-check-version "#docdb-lts-check-version").

For details about support timelines and release cycles for the LTS versions, see [Amazon DocumentDB engine version support dates](docdb-version-support-dates.md "docdb-version-support-dates.md"). Amazon DocumentDB will announce the next LTS version through standard communication channels.

## Who Should Use LTS

Amazon DocumentDB LTS releases are designed for clusters with limited upgrade windows. LTS is ideal for production environments where database availability directly impacts business operations.

**Consider LTS releases if:**

- Your application has strict uptime requirements that limit upgrade opportunities
- You have all required database engine features and enhancements your application needs

**Consider standard releases instead if:**

- Your application can handle minimal interruption
- You want the latest capabilities and enhancements as soon as they're released

## Understanding LTS Patch Versions

Amazon DocumentDB Long Term Support (LTS) has a designated minimum required patch version. Your cluster is considered to be on the LTS version if you are running either:

1. The designated LTS required patch version, or
2. Any later patch version (whether required or optional)

Optional patches remain the same as defined in [Maintaining Amazon DocumentDB](db-instance-maintain.md#user-initiated-updates "db-instance-maintain.md#user-initiated-updates").

**Required Patches vs. Optional Patches**

- **Required patches** contain critical updates and will be automatically applied during your cluster's upgrade window
- **Optional patches** contain non-critical improvements and have no automatic apply date

**How to Identify Patch Types**

To determine whether a pending patch is required or optional, connect to your cluster and run the CLI `describe-pending-maintenance-actions` command or call the `DescribePendingMaintenanceActions` API operation. For more details on managing patches, see [Maintaining Amazon DocumentDB](db-instance-maintain.md#user-initiated-updates "db-instance-maintain.md#user-initiated-updates").

- **Required patches** display specific dates for `CurrentApplyDate`, `ForcedApplyDate`, and `AutoAppliedAfterDate`
- **Optional patches** display null values for these date fields

###### Important

- Updates are **one-way operations** - you cannot downgrade after updating
- Your cluster will experience brief downtime during the update process

## How to create a new LTS cluster

To create an LTS cluster, follow these steps:

1. In the Management Console, create a new engine version 5.0.0 cluster
2. Verify you're on the required engine patch version after cluster creation or upgrade by connecting to your cluster and running the following command: `db.runCommand({getEngineVersion: 1})`

**Example**

```
{
    engineVersion: '3.0.17983',
    ok: 1,
    operationTime: Timestamp({ t: `timestamp_value`, i: 1 })
}
```

## How to upgrade from engine version 3.6.0 or 4.0.0 to a 5.0.0 LTS cluster

To upgrade to an LTS cluster, follow these steps:

1. In the Management Console, major version upgrade (MVU) your engine version 3.6.0 or 4.0.0 cluster to 5.0.0 following [Upgrading the Amazon DocumentDB engine version](docdb-mvu.md "docdb-mvu.md")
2. Verify you're on the required engine patch version after cluster creation or upgrade by connecting to your cluster and running the following command: `db.runCommand({getEngineVersion: 1})`

## How to check if my existing engine version 5.0.0 cluster is on LTS

To check if your engine version 5.0.0 cluster is running an LTS version:

1. Verify you're on engine version 5.0.0, **Required Engine Patch Version 3.0.17983 or later** by connecting to your cluster and running the following command: `db.runCommand({getEngineVersion: 1})`
2. If needed, update your existing engine version 5.0.0 cluster following [Performing a patch update to a cluster's engine version](db-cluster-version-upgrade.md "db-cluster-version-upgrade.md")
