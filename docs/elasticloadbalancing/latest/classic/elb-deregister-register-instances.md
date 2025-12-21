# Register instances with your Classic Load Balancer

Registering an EC2 instance adds it to your load balancer. The load balancer continuously
monitors the health of registered instances in its enabled Availability Zones, and routes
requests to the instances that are healthy. If demand on your instances increases, you can
register additional instances with the load balancer to handle the demand.

Deregistering an EC2 instance removes it from your load balancer. The load balancer stops
routing requests to an instance as soon as it is deregistered.
If demand decreases, or you need to service your instances, you can deregister instances from the load balancer.
An instance that is deregistered remains running, but no longer receives traffic from the load balancer,
and you can register it with the load balancer again when you are ready.

When you deregister an instance, ELB waits until in-flight requests have completed if
connection draining is enabled. For more information, see [Configure connection draining for your Classic Load Balancer](config-conn-drain.md "config-conn-drain.md").

If your load balancer is attached to an Auto Scaling group, instances in the group are
automatically registered with the load balancer. If you detach a load balancer from
your Auto Scaling group, the instances in the group are deregistered.

ELB registers your EC2 instance with your load balancer using its IP address.

[EC2-VPC] When you register an instance with an elastic network interface (ENI)
attached, the load balancer routes requests to the primary IP address of the
primary interface (eth0) of the instance.

###### Contents

- [Register an instance](#elb-register-instances "#elb-register-instances")
- [View the instances registered with a load balancer](#elb-describe-load-balancer-instances "#elb-describe-load-balancer-instances")
- [Determine the load balancer for a registered instance](#elb-describe-instance-load-balancer "#elb-describe-instance-load-balancer")
- [Deregister an instance](#elb-deregister-instances "#elb-deregister-instances")

## Register an instance

When you are ready, register your instance with your load balancer. If the
instance is an in Availability Zone that is enabled for the load balancer,
the instance is ready to receive traffic from the load balancer as soon as it
passes the required number of health checks.

###### To register your instances using the console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**, choose
   **Load Balancers**.
3. Choose the name of the load balancer to open its detail page.
4. On the **Target instances** tab, select **Manage instances**.
5. On the **Manage instances** page, within the **Available instances** table, select the instances to register with your load balancer.
6. Ensure the instances needing to be registered are populated within the **Review selected instances** table.
7. Choose **Save changes**.

###### To register your instances using the AWS CLI

Use the following [register-instances-with-load-balancer](../../../cli/latest/reference/elb/register-instances-with-load-balancer.md "../../../cli/latest/reference/elb/register-instances-with-load-balancer.md") command:

```
`aws elb register-instances-with-load-balancer --load-balancer-name `my-loadbalancer` --instances `i-4e05f721``
```

The following is an example response that lists the instances registered
with the load balancer:

```
{
    "Instances": [
        {
            "InstanceId": "i-315b7e51"
        },
        {
            "InstanceId": "i-4e05f721"
        }
    ]
}
```

## View the instances registered with a load balancer

Use the following [describe-load-balancers](../../../cli/latest/reference/elb/describe-load-balancers.md "../../../cli/latest/reference/elb/describe-load-balancers.md") command to list the instances registered
with the specified load balancer:

```
`aws elb describe-load-balancers --load-balancer-names `my-load-balancer` --output text --query "LoadBalancerDescriptions[*].Instances[*].InstanceId"`
```

The following is example output:

```
i-e905622e
i-315b7e51
i-4e05f721
```

## Determine the load balancer for a registered instance

Use the following [describe-load-balancers](../../../cli/latest/reference/elb/describe-load-balancers.md "../../../cli/latest/reference/elb/describe-load-balancers.md") command to get the name of the load balancer to
which the specified instance is registered:

```
`aws elb describe-load-balancers --output text --query "LoadBalancerDescriptions[?Instances[?InstanceId=='`i-e905622e`']].[LoadBalancerName]"`
```

The following is example output:

```
my-load-balancer
```

## Deregister an instance

You can deregister an instance from your load balancer if you
no longer need the capacity or if you need to service the instance.

If your load balancer is attached to an Auto Scaling group, detaching the instance
from the group also deregisters it from the load balancer. For more
information, see [Detach
EC2 instances from your Auto Scaling group](../../../autoscaling/ec2/userguide/ec2-auto-scaling-detach-attach-instances.md "../../../autoscaling/ec2/userguide/ec2-auto-scaling-detach-attach-instances.md") in the _Amazon EC2 Auto Scaling User Guide_.

###### To deregister your instances using the console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**, choose
   **Load Balancers**.
3. Choose the name of the load balancer to open its detail page.
4. On the **Target instances** tab, select **Manage instances**.
5. On the **Manage instances** page, within the **Available instances** table, deselect the instances to deregister from your load balancer.
6. Ensure the instances needing to be deregistered are not populated within the **Review selected instances** table.
7. Choose **Save changes**.

###### To deregister your instances using the AWS CLI

Use the following [deregister-instances-from-load-balancer](../../../cli/latest/reference/elb/deregister-instances-from-load-balancer.md "../../../cli/latest/reference/elb/deregister-instances-from-load-balancer.md") command:

```
`aws elb deregister-instances-from-load-balancer --load-balancer-name `my-loadbalancer` --instances `i-4e05f721``
```

The following is an example response that lists the remaining instances
registered with the load balancer:

```
{
    "Instances": [
        {
            "InstanceId": "i-315b7e51"
        }
    ]
}
```
