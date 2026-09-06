

# Migrate from Enhanced Container Insights (Classic) to OTel Container Insights
<a name="container-insights-eks-migrate-from-classic"></a>

Both Enhanced Container Insights (Classic) and OTel Container Insights use the same `amazon-cloudwatch-observability` Amazon EKS add-on. The migration is an in-place add-on version update that you can complete in 15–30 minutes.

**Warning**  
CloudWatch alarms configured with Classic metric names do not automatically work with OTel metrics. You must recreate alarms using PromQL-based alarm rules.

## Prerequisites
<a name="container-insights-eks-migrate-from-classic-prereqs"></a>

Before you begin the migration, verify that you meet the following requirements.
+ An Amazon EKS cluster running Kubernetes version 1.28 or later
+ The `amazon-cloudwatch-observability` add-on installed and in `ACTIVE` status
+ AWS CLI version 2.15.0 or later
+ `kubectl` configured to communicate with your target cluster
+ An IAM role with the `CloudWatchAgentServerPolicy` managed policy attached

## Breaking changes
<a name="container-insights-eks-migrate-from-classic-breaking"></a>

Review the following breaking changes before you begin the migration.

### Removed features
<a name="container-insights-eks-migrate-from-classic-removed"></a>

The following features are not available in OTel Container Insights:
+ **StatsD custom metrics** — Use the OTel StatsD receiver instead.
+ **collectd plugin** — Migrate to OTel-native instrumentation.

### Changed defaults
<a name="container-insights-eks-migrate-from-classic-defaults"></a>

The following table shows default values that change between Classic and OTel Container Insights.


| Setting | Classic default | OTel CI default | 
| --- | --- | --- | 
| Collection interval | 60 seconds | 60 seconds | 
| Enhanced Observability | Enabled | Enabled | 
| Agent CPU request | 200m | 100m | 
| Agent memory request | 200Mi | 128Mi | 

## Migration steps
<a name="container-insights-eks-migrate-from-classic-steps"></a>

This migration uses a phased approach to minimize monitoring gaps. You run both Classic and OTel metrics streams in parallel, validate the data, and then disable the Classic stream.

### Phase 1: Confirm current state (Classic only)
<a name="container-insights-eks-migrate-from-classic-phase1"></a>

Before you make changes, confirm your current add-on state and record the version for rollback.

**To confirm your current add-on configuration**

1. Run the following command to check the current add-on status.

   ```
   aws eks describe-addon \
     --cluster-name {{cluster-name}} \
     --addon-name amazon-cloudwatch-observability
   ```

1. Verify that the `status` field is `ACTIVE`.

1. Record the `addonVersion` value. You need this value if you must roll back.

### Phase 2: Enable dual publishing (Classic \+ OTel)
<a name="container-insights-eks-migrate-from-classic-phase2"></a>

Enable OTel Container Insights alongside Enhanced Container Insights (Classic). This publishes both metric streams simultaneously so that you can validate data equivalence.

**Important**  
Both metric streams incur charges during this phase. We recommend keeping the dual publishing window as short as possible to minimize costs.

**To enable dual publishing**

1. Run the following command to update the add-on with both streams enabled.

   ```
   aws eks update-addon \
     --cluster-name {{cluster-name}} \
     --addon-name amazon-cloudwatch-observability \
     --addon-version {{latest-version}} \
     --configuration-values '{"containerInsights":{"enabled":true},"otelContainerInsights":{"enabled":true}}' \
     --resolve-conflicts OVERWRITE
   ```

1. Wait for the add-on status to return to `ACTIVE`.

   ```
   aws eks describe-addon \
     --cluster-name {{cluster-name}} \
     --addon-name amazon-cloudwatch-observability \
     --query "addon.status"
   ```

1. Verify that OTel metrics appear in CloudWatch by querying a known metric with PromQL.

### Phase 3: Recreate alarms and update dashboards
<a name="container-insights-eks-migrate-from-classic-phase3"></a>

Build OTel replacements for your existing Classic alarms and dashboards. Keep Classic alarms active as a safety net during this phase.

**To recreate alarms for OTel metrics**

1. Identify all CloudWatch alarms that reference Classic Container Insights metric names.

1. Create equivalent alarms using PromQL-based metric math expressions that reference OTel metric names.

1. Verify that the new alarms enter `OK` state and produce equivalent threshold evaluations.

1. Update any CloudWatch dashboards to include widgets based on OTel metrics alongside the existing Classic widgets.

### Phase 4: Disable Classic (switch to OTel only)
<a name="container-insights-eks-migrate-from-classic-phase4"></a>

After you validate that OTel metrics, alarms, and dashboards work correctly, disable the Classic stream.

**To disable Classic and keep OTel only**

1. Run the following command to disable Classic metrics publishing.

   ```
   aws eks update-addon \
     --cluster-name {{cluster-name}} \
     --addon-name amazon-cloudwatch-observability \
     --configuration-values '{"containerInsights":{"enabled":false},"otelContainerInsights":{"enabled":true}}' \
     --resolve-conflicts OVERWRITE
   ```

1. Wait for the add-on status to return to `ACTIVE`.

1. Remove the Classic alarms that you replaced in Phase 3.

## Verification
<a name="container-insights-eks-migrate-from-classic-verify"></a>

After you complete the migration, verify that your observability stack is working correctly.
+ **Check metrics in Query Studio** — Use PromQL queries to confirm that metrics flow from the OTel pipeline.
+ **Compare with baseline values** — Verify that metric values are consistent with the Classic metrics you recorded during Phase 2.
+ **Verify Container Insights dashboards** — Confirm that the Container Insights console displays data for your cluster.
+ **Verify log delivery** — Check that container logs continue to appear in CloudWatch Logs.
+ **Verify alarms** — Confirm that no alarms are in `INSUFFICIENT_DATA` state.

## Rollback
<a name="container-insights-eks-migrate-from-classic-rollback"></a>

If you encounter issues after migration, you can restore the previous Classic configuration.

**To roll back to Enhanced Container Insights (Classic)**

1. Identify the previous add-on version that you recorded in Phase 1.

1. Run the following command to downgrade the add-on.

   ```
   aws eks update-addon \
     --cluster-name {{cluster-name}} \
     --addon-name amazon-cloudwatch-observability \
     --addon-version {{previous-version}} \
     --resolve-conflicts OVERWRITE
   ```

1. Wait for the add-on status to return to `ACTIVE`.

   ```
   aws eks describe-addon \
     --cluster-name {{cluster-name}} \
     --addon-name amazon-cloudwatch-observability \
     --query "addon.status"
   ```

1. Re-apply any custom configuration values that you used with the previous version.