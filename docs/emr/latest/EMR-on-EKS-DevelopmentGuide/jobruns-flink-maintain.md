# Maintaining Flink applications

###### Topics

- [Upgrade modes](#jobruns-flink-upgrademode "#jobruns-flink-upgrademode")
  Flink applications are typically designed to run for long periods of time such as
  weeks, months, or even years. As with all long-running services, Flink streaming
  applications need to be maintained. This includes bug fixes, improvements, and migration
  to a Flink cluster of a later version.

When the spec changes for `FlinkDeployment` and
`FlinkSessionJob` resources, you need to upgrade the running application.
To do this, the operator stops the running job (unless already suspended) and redeploys
it with the latest spec and, for stateful applications, the state from the previous
run.

Users control how to manage the state when stateful applications stop and restore with
the `upgradeMode` setting of the `JobSpec`.

## Upgrade modes

Optional introduction

**Stateless**

Stateless application upgrades from empty state.

**Last state**

Quick upgrades in any application state (even for failing jobs), does
not require a healthy job as it always uses the latest successful
checkpoint. Manual recovery may be necessary if HA metadata is lost. To
limit the time the job may fall back when picking up the latest
checkpoint you can configure
`kubernetes.operator.job.upgrade.last-state.max.allowed.checkpoint.age`.
If the checkpoint is older than the configured value, a savepoint will
be taken instead for healthy jobs. This is not supported in Session
mode.

**Savepoint**

Use savepoint for upgrade, providing maximal safety and possibility to
serve as backup/fork point. The savepoint will be created during the
upgrade process. Note that the Flink job needs to be running to allow
the savepoint to get created. If the job is in an unhealthy state, the
last checkpoint will be used (unless
kubernetes.operator.job.upgrade.last-state-fallback.enabled is set to
false). If the last checkpoint is not available, the job upgrade will
fail.
