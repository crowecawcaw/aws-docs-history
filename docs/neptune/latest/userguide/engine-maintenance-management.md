# Managing engine updates to your Neptune DB cluster

###### Note

Updates are applied to all instances in a DB cluster simultaneously.
An update requires a database restart on those instances, so you experience
downtime ranging from 20 or 30 seconds to several minutes, after which you can
resume using the DB cluster. On rare occasions a Multi-AZ failover might be
required for a maintenance update on an instance to complete.

For major version upgrades that can take longer to apply, you can use a
[blue-green deployment strategy](neptune-BG-deployments.md "neptune-BG-deployments.md")
to minimize downtime.

## Determining which engine version you are currently using

You can use the AWS CLI [get-engine-status](access-graph-status.md "access-graph-status.md")
command to check which engine release version your DB cluster is currently using:

```
aws neptunedata get-engine-status
```

The [JSON output](access-graph-status.md#access-graph-status-sample-output "access-graph-status.md#access-graph-status-sample-output") includes a
`"dbEngineVersion"` field like this:

```
  "dbEngineVersion": "1.3.0.0",
```

## Check to see what updates are pending and available

You can check pending updates to your DB cluster using the Neptune console.
Select **Databases** in the left column and then select your DB cluster
in the databases pane. Pending updates are listed in the **Maintenance**
column. If you select **Actions** and then **Maintenance**,
you have three choices about what to do:

- Upgrade now.
- Upgrade at next window.
- Defer upgrade.

You can list pending engine updates using the AWS CLI as follows:

```
aws neptune describe-pending-maintenance-actions \
  --resource-identifier `(ARN of your DB cluster)`
  --region `(your region)` \
  --engine neptune
```

You can also list available engine updates using the AWS CLI as follows:

```
aws neptune describe-db-engine-versions \
  --region `(your region)` \
  --engine neptune
```

The list of available engine releases includes only those releases that
have a version number higher than the current one and for which an upgrade path
is defined.

## Always test before you upgrade

When a new major or minor Neptune engine version is released, always test your
Neptune applications on it first before upgrading to it. A minor upgrade could
introduce new features or behavior that would affect your code even without any
breaking change.

Start by comparing the release notes pages from your current version to those
of the targeted version to see if there will be changes in query language versions
or other breaking changes.

The best way to test a new version before upgrading your production DB cluster is
to use the [Neptune Blue-Green deployment
solution](neptune-BG-deployments.md "neptune-BG-deployments.md"). That way you can run applications and queries on the new version
without affecting your production DB cluster.

## Always create a manual snapshot before you upgrade

Before performing an upgrade, we strongly recommend that you always create
a manual snapshot of your DB cluster. Having an automatic snapshot only offers
short-term protection, whereas a manual snapshot remains available until you
explicitly delete it.

In certain cases Neptune creates a manual snapshot for you as a part of the
upgrade process, but you should not rely on this, and should create your own manual
snapshot in any case.

When you are certain that you won't need to revert your DB cluster to its
pre-upgrade state, you can explicitly delete the manual snapshot that you created
yourself, as well as the manual snapshot that Neptune might have created. If Neptune
creates a manual snapshot, it will have a name that begins with `preupgrade`,
followed by the name of your DB cluster, the source engine version, the target engine
version, and the date.

## Neptune Maintenance Window

The weekly maintenance window is a 30-minute period during which scheduled engine
updates and other system changes are applied. Most maintenance events complete during the
30-minute window, although larger maintenance events might sometimes longer to complete.

Every DB cluster has a weekly 30-minute maintenance window. If you don't specify a
preferred time for it when you create the DB cluster, Neptune randomly picks a day of
the week and then randomly assigns a 30-minute period within it from an 8-hour block
of time that varies with the region.

Here, for example, are the 8-hour time blocks for maintence windows used in several AWS
regions:

| Region                         | Time Block      |
| ------------------------------ | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| US West (Oregon) Region        | 06:00–14:00 UTC |
| US West (N. California) Region | 06:00–14:00 UTC |
| US East (Ohio) Region          | 03:00–11:00 UTC |
| Europe (Ireland) Region        | 22:00–06:00 UTC | The maintenance window determines when pending operations start, and most maintenance operations complete within the window, but larger maintenance tasks can continue beyond the window's end time. ### Moving your DB cluster maintenance window Ideally, the your maintenance window should fall at a time when you cluster is at its lowest usage. If that isn't true of your current window, you can move it to a better time, like this: ###### To change your DB cluster maintenance window 1. Sign in to the AWS Management Console, and open the Amazon Neptune console at [https://console.aws.amazon.com/neptune/home](https://console.aws.amazon.com/neptune/home "https://console.aws.amazon.com/neptune/home"). 2. In the navigation pane, choose **databases**. 3. Choose the DB cluster for which you want to change the maintenance window. 4. Choose **Modify**. 5. Choose **Show more** at the bottom of the **Modify cluster** page. 6. In the **Preferred maintenance window** section, set the day, time and duration of the maintenance window as you prefer. 7. Choose **Next**. On the confirmation page, review your changes. 8. To apply the changes to the maintenance window immediately, select **Apply immediately**. 9. Choose **Submit** to apply your changes. To edit your changes, choose **Previous**, or to cancel your changes, choose **Cancel**. ## Using AutoMinorVersionUpgrade to control automatic minor version updates ###### Important `AutoMinorVersionUpgrade` is only effective for minor version upgrades above [engine release 1.3.0.0](engine-releases-1.3.0.md "engine-releases-1.3.0.md"). If you have the `AutoMinorVersionUpgrade` field set to `true` in the writer (primary) instance of your DB cluster, minor version updates are applied automatically to all instances in your DB cluster during the next maintenance window after they are released. If you have the `AutoMinorVersionUpgrade` field set to `false` in the writer instance of your DB cluster, they are applied only if you [explicitly install them](engine-updates-manually.md#engine-minor-updates-using-console "engine-updates-manually.md#engine-minor-updates-using-console"). ###### Note Patch releases (`*.*.*.1`, `*.*.*.2`, etc.) are always installed automatically during your next maintenance window, regardless of how the `AutoMinorVersionUpgrade` parameter is set. You can set `AutoMinorVersionUpgrade` using the AWS Management Console as follows: ###### To set `AutoMinorVersionUpgrade` using the Neptune console 1. Sign in to the AWS Management Console, and open the Amazon Neptune console at [https://console.aws.amazon.com/neptune/home](https://console.aws.amazon.com/neptune/home "https://console.aws.amazon.com/neptune/home"). 2. In the navigation pane, choose **Databases**. 3. Choose the primary (writer) instance of the DB cluster for which you want to set `AutoMinorVersionUpgrade`. 4. Choose **Modify**. 5. Choose **Show more** at the bottom of the **Modify cluster** page. 6. At the bottom of the expanded page, choose either **Turn on auto minor version upgrade** or **Turn off auto minor version upgrade**. 7. Choose **Next**. On the confirmation page, review your changes. 8. To apply the changes to auto minor version upgrade, select **Apply immediately**. 9. Choose **Submit** to apply your changes. To edit your changes, choose **Previous**, or to cancel your changes, choose **Cancel**. You can also use the AWS CLI to set the `AutoMinorVersionUpgrade` field. For example, to set it to `true`, you can use a command like this: ``aws neptune modify-db-instance \ --db-instance-identifier `(the ID of your cluster's writer instance)` \ --auto-minor-version-upgrade \ --apply-immediately`` Similarly, to set it to `false`, use a command like this: ``aws neptune modify-db-instance \ --db-instance-identifier `(the ID of your cluster's writer instance)` \ --no-auto-minor-version-upgrade \ --apply-immediately`` |
