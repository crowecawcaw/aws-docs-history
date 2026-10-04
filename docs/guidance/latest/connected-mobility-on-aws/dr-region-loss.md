

# Recovering from a Region event
<a name="dr-region-loss"></a>

Nothing in this Guidance replicates across Regions. Recovery is a redeploy plus a data restore:

1. Deploy the stacks into the replacement Region. Follow [Deploy the Guidance](deploy-the-solution.md); the deployment is Region-agnostic.

1. Restore the DynamoDB tables from point-in-time recovery into the new Region’s tables.

1. Re-provision vehicle certificates in the new Region’s AWS IoT Core endpoint, and re-point vehicles at it.

1. Re-seed the signal catalog, decoder manifests and campaigns.

Two things do not recover, and are worth accepting deliberately rather than discovering:
+  **Telemetry in flight is lost.** Kafka retention is local to the cluster. Records not yet processed into DynamoDB at the time of the event do not survive.
+  **Live vehicle state is lost.** The Redis cache is not backed up. It rebuilds as soon as telemetry resumes, so the effect is that vehicles read as offline until their next transmission rather than a permanent loss.

Recovery time is dominated by the redeploy and by re-pointing vehicles, not by the data restore. The recovery point for stored data is the point-in-time recovery window; for in-flight telemetry it is the moment of the event.