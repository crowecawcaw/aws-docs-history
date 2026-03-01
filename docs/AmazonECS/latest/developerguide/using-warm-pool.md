# Configuring pre-initialized instances for your Amazon ECS Auto Scaling group

Amazon ECS supports Amazon EC2 Auto Scaling warm pools. A warm pool is a group of pre-initialized Amazon EC2 instances
ready to be placed into service. Whenever your application needs to scale out, Amazon EC2 Auto Scaling uses
the pre-initialized instances from the warm pool rather than launching cold instances, allows
for any final initialization process to run, and then places the instance into service.

To learn more about warm pools and how to add a warm pool to your Auto Scaling group, see [Warm
pools for Amazon EC2 Auto Scaling](../../../autoscaling/ec2/userguide/ec2-auto-scaling-warm-pools.md "../../../autoscaling/ec2/userguide/ec2-auto-scaling-warm-pools.md")
_in the Amazon EC2 Auto Scaling User Guide_.

When you create or update a warm pool for an Auto Scaling group for Amazon ECS , you cannot set the option
that returns instances to the warm pool on scale in (`ReuseOnScaleIn`). For more
information, see [put-warm-pool](../../../cli/latest/reference/autoscaling/put-warm-pool.md "../../../cli/latest/reference/autoscaling/put-warm-pool.md") in the
_AWS Command Line Interface Reference_.

To use warm pools with your Amazon ECS cluster, set the `ECS_WARM_POOLS_CHECK` agent
configuration variable to `true` in the **User
data** field of your Amazon EC2 Auto Scaling group launch template.

The following shows an example of how the agent configuration variable can be specified in
the **User data** field of an Amazon EC2 launch template. Replace
`MyCluster` with the name our your cluster.

```
`#!/bin/bash
cat <<'EOF' >> /etc/ecs/ecs.config
ECS_CLUSTER=`MyCluster`
ECS_WARM_POOLS_CHECK=true
EOF`
```

The `ECS_WARM_POOLS_CHECK` variable is only supported on agent versions
`1.59.0` and later. For more information about the variable, see [Amazon ECS container agent configuration](ecs-agent-config.md "ecs-agent-config.md").
