# Configuring Amazon ECS Linux container instances to receive Spot Instance notices

Amazon EC2 terminates, stops, or hibernates your Spot Instance when the Spot price exceeds the
maximum price for your request or capacity is no longer available. Amazon EC2 provides a Spot Instance
two-minute interruption notice for terminate and stop actions. It does not provide the
two-minute notice for the hibernate action. If Amazon ECS Spot Instance draining is turned onon the
instance, Amazon ECS receives the Spot Instance interruption notice and places the instance in
`DRAINING` status.

###### Important

Amazon ECS does not receive a notice from Amazon EC2 when instances are removed by Auto
Scaling Capacity Rebalancing. For more information, see [Amazon EC2 Auto Scaling Capacity Rebalancing](../../../autoscaling/ec2/userguide/ec2-auto-scaling-capacity-rebalancing.md "../../../autoscaling/ec2/userguide/ec2-auto-scaling-capacity-rebalancing.md").

When a container instance is set to `DRAINING`, Amazon ECS prevents new
tasks from being scheduled for placement on the container instance. Service tasks on
the draining container instance that are in the `PENDING` state are
stopped immediately. If there are container instances in the cluster that are
available, replacement service tasks are started on them.

Spot Instance draining is turned off by default.

You can turn on Spot Instance draining when you launch an instance. Add the following script
into the **User data** field. Replace
`MyCluster` with the name of the cluster to register the
container instance to.

```
#!/bin/bash
cat <<'EOF' >> /etc/ecs/ecs.config
ECS_CLUSTER=`MyCluster`
ECS_ENABLE_SPOT_INSTANCE_DRAINING=true
EOF
```

For more information, see [Launching an Amazon ECS Linux container instance](launch_container_instance.md "launch_container_instance.md").

###### To turn on Spot Instance draining for an existing container instance

1. Connect to the Spot Instance over SSH.
2. Edit the `/etc/ecs/ecs.config` file and add the
   following:

```
ECS_ENABLE_SPOT_INSTANCE_DRAINING=true
```

3. Restart the `ecs` service.
   - For the Amazon ECS-optimized Amazon Linux 2 AMI:

   ```
   `sudo systemctl restart ecs`
   ```

4. (Optional) You can verify that the agent is running and see some
   information about your new container instance by querying the agent
   introspection API operation. For more information, see [Amazon ECS container introspection](ecs-agent-introspection.md "ecs-agent-introspection.md").

```
`curl http://localhost:51678/v1/metadata`
```
