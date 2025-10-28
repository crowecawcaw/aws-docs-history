# Automatic node

recovery

During cluster creation or update, cluster admin users can select the node (instance)
recovery option between `Automatic` (Recommended) and `None` at
the cluster level. If set to `Automatic`, SageMaker HyperPod reboots or replaces
faulty nodes automatically.

###### Important

We recommend setting the `Automatic` option.

Automatic node recovery runs when issues are found from health-monitoring agent, basic
health checks, and deep health checks. If set to `None`, the health
monitoring agent will label the instances when a fault is detected, but it will not
automatically initiate any repair or recovery actions on the affected nodes. This option
is not recommended.
