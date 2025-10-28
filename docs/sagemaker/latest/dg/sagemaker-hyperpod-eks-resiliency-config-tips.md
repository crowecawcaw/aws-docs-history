# Suggested resilience

configurations

When the deep health checks are enabled, whenever a new instance is added to the
HyperPod cluster (either during create-cluster or through automatic node
replacement), the new instance goes through the deep health check process (instance
level stress tests) for about a couple of hours. The following are suggested resilience
config combinations depending on possible cases.

1. **Case**: When you have additional spare nodes
   within a cluster as back-up resources (not using the full capacity), or if you
   can wait for about 2 hours for the deep health check process to get the less
   error-prone instances.

**Recommendation**: Enable the deep health check
config throughout the cluster lifecycle. Node auto-recovery config is enabled by
default. 2. **Case**: When you don't have additional backup
nodes (capacity is fully used for some training load). You want to get the
replacement nodes as soon as possible to resume the training job.

**Recommendation**: Enable the deep health check
during cluster creation, then turn-off the deep health check config after the
cluster is created. Node auto recovery config is enabled by default. 3. **Case**: When you don't have additional backup
nodes, and you don't want to wait for the ~2 hour deep health check process
(small clusters).

**Recommendation**: disable the deep health check
config throughout the cluster life cycle. Node auto recovery config is enabled
by default.
If you want to resume the training job from a failure immediately, make sure that you
have additional spare nodes as backup resources in the cluster.
