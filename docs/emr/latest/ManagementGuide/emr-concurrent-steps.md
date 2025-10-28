# Considerations for running multiple steps in

parallel when you submit work to Amazon EMR

Running multiple steps in parallel when you submit work to Amazon EMR requires preliminary decisions about resource planning and
expectations regarding cluster behavior. These are covered in detail here.

- Steps running in parallel may complete in any order, but pending steps in
  queue transition to running state in the order they were submitted.
- When you select a step concurrency level for your cluster, you must consider
  whether or not the primary node instance type meets the memory requirements
  of user workloads. The main step executer process runs on the primary node
  for each step. Running multiple steps in parallel requires more memory and CPU
  utilization from the primary node than running one step at a time.
- To achieve complex scheduling and resource management of concurrent steps, you
  can use YARN scheduling features such as `FairScheduler` or
  `CapacityScheduler`. For example, you can use
  `FairScheduler` with a `queueMaxAppsDefault` set to
  prevent more than a certain number of jobs from running at a time.
- The step concurrency level is subject to the configurations of resource
  managers. For example, if YARN is configured with only a parallelism of
  `5`, then you can only have five YARN applications running in
  parallel even if the `StepConcurrencyLevel` is set to
  `10`. For more information about configuring resource managers, see
  [Configure
  applications](../ReleaseGuide/emr-configure-apps.md "../ReleaseGuide/emr-configure-apps.md") in the _Amazon EMR Release Guide_.
- You cannot add a step with an `ActionOnFailure` other than CONTINUE
  while the step concurrency level of the cluster is greater than 1.
- If the step concurrency level of a cluster is greater than one, step
  `ActionOnFailure` feature will not activate.
- If a cluster has step concurrency level `1` but has multiple
  running steps, `TERMINATE_CLUSTER ActionOnFailure` may activate, but
  `CANCEL_AND_WAIT ActionOnFailure` will not. This edge case arises
  when the cluster step concurrency level was greater than one, but lowered while
  multiple steps were running.
- You can use EMR automatic scaling to scale up and down based on the YARN
  resources to prevent resource contention. For more information, see [Using automatic
  scaling with a custom policy for instance groups](emr-automatic-scaling.md "emr-automatic-scaling.md") in the
  _Amazon EMR Management Guide_.
- When you decrease the step concurrent level, EMR allows any running steps to
  complete before reducing the number of steps. If the resources are exhausted
  because the cluster is running too many concurrent steps, we recommend manually
  canceling any running steps to free up resources.
