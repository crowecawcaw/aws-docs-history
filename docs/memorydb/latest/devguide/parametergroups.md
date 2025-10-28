# Parameter management

Parameters are grouped together into named parameter groups for easier parameter management.
A parameter group represents a combination of specific values for the parameters that
are passed to the engine software during startup. These values determine how the engine
processes on each node behave at runtime. The parameter values on a specific parameter
group apply to all nodes that are associated with the group, regardless of which cluster
they belong to.

To fine-tune your cluster's performance, you can modify some parameter values or change the cluster's parameter group.

- You cannot modify or delete the default parameter groups.
  If you need custom parameter values, you must create a custom parameter group.
- The parameter group family and the cluster you're assigning it to must be compatible.
  For example, if your cluster is running Redis OSS version 6, you can only use parameter groups, default
  or custom, from the memorydb_redis6 family.
- When you change a cluster's parameters, the change is applied to the cluster
  immediately. This is true whether you change the
  cluster's parameter group itself or a parameter value within the cluster's
  parameter group.
