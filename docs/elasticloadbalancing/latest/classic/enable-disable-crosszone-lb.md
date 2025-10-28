# Configure cross-zone load balancing for your Classic Load Balancer

With _cross-zone load balancing_, each load balancer node for your
Classic Load Balancer distributes requests evenly across the registered instances in all enabled
Availability Zones. If cross-zone load balancing is disabled, each load balancer node
distributes requests evenly across the registered instances in its Availability Zone
only. For more information, see [Cross-zone load balancing](../userguide/how-elastic-load-balancing-works.md#cross-zone-load-balancing "../userguide/how-elastic-load-balancing-works.md#cross-zone-load-balancing") in the
_Elastic Load Balancing User Guide_.

Cross-zone load balancing reduces the need to maintain equivalent numbers of instances
in each enabled Availability Zone, and improves your application's ability to handle the
loss of one or more instances. However, we still recommend that you maintain
approximately equivalent numbers of instances in each enabled Availability Zone for
higher fault tolerance.

For environments where clients cache DNS lookups, incoming requests might favor one of
the Availability Zones. Using cross-zone load balancing, this imbalance in the request
load is spread across all available instances in the Region, reducing the impact of
misbehaving clients.

When you create a Classic Load Balancer, the default for cross-zone load balancing depends on how you
create the load balancer. With the API or CLI, cross-zone load balancing is disabled by
default. With the AWS Management Console, the option to enable cross-zone load balancing is selected
by default. After you create a Classic Load Balancer, you can enable or disable cross-zone load
balancing at any time.

###### Contents

- [Enable cross-zone load balancing](#enable-cross-zone "#enable-cross-zone")
- [Disable cross-zone load balancing](#disable-cross-zone "#disable-cross-zone")

## Enable cross-zone load balancing

You can enable cross-zone load balancing for your Classic Load Balancer at any time.

###### To enable cross-zone load balancing using the console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**, choose
   **Load Balancers**.
3. Choose the name of the load balancer to open its detail page.
4. On the **Attributes** tab, choose **Edit**.
5. On the **Edit load balancer attributes** page, in the
   **Availability Zone routing configuration** section, enable
   **Cross-zone load balancing**.
6. Choose **Save changes**.

###### To enable cross-zone load balancing using the AWS CLI

1. Use the following [modify-load-balancer-attributes](../../../cli/latest/reference/elb/modify-load-balancer-attributes.md "../../../cli/latest/reference/elb/modify-load-balancer-attributes.md") command to set the
   `CrossZoneLoadBalancing` attribute of your load balancer to
   `true`:

```
`aws elb modify-load-balancer-attributes --load-balancer-name `my-loadbalancer` --load-balancer-attributes "{\"CrossZoneLoadBalancing\":{\"Enabled\":true}}"`
```

The following is an example response:

```
{
   "LoadBalancerAttributes": {
     "CrossZoneLoadBalancing": {
         "Enabled": true
       }
   },
   "LoadBalancerName": "my-loadbalancer"
 }

```

2. (Optional) Use the following [describe-load-balancer-attributes](../../../cli/latest/reference/elb/describe-load-balancer-attributes.md "../../../cli/latest/reference/elb/describe-load-balancer-attributes.md") command to verify that
   cross-zone load balancing is enabled for your load balancer:

```
`aws elb describe-load-balancer-attributes --load-balancer-name `my-loadbalancer``
```

The following is an example response:

```
{
    "LoadBalancerAttributes": {
        "ConnectionDraining": {
            "Enabled": false,
            "Timeout": 300
        },
        "CrossZoneLoadBalancing": {
            "Enabled": true
        },
        "ConnectionSettings": {
            "IdleTimeout": 60
        },
        "AccessLog": {
            "Enabled": false
        }
    }
}
```

## Disable cross-zone load balancing

You can disable the cross-zone load balancing option for your load balancer at any
time.

###### To disable cross-zone load balancing using the console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**, choose
   **Load Balancers**.
3. Choose the name of the load balancer to open its detail page.
4. On the **Attributes** tab, choose **Edit**.
5. On the **Edit load balancer attributes** page, in the
   **Availability Zone routing configuration** section, disable
   **Cross-zone load balancing**.
6. Choose **Save changes**.

To disable cross-zone load balancing, set the `CrossZoneLoadBalancing`
attribute of your load balancer to `false`.

###### To disable cross-zone load balancing using the AWS CLI

1. Use the following [modify-load-balancer-attributes](../../../cli/latest/reference/elb/modify-load-balancer-attributes.md "../../../cli/latest/reference/elb/modify-load-balancer-attributes.md") command:

```
`aws elb modify-load-balancer-attributes --load-balancer-name `my-loadbalancer` --load-balancer-attributes "{\"CrossZoneLoadBalancing\":{\"Enabled\":false}}"`
```

The following is an example response:

```
{
   "LoadBalancerAttributes": {
     "CrossZoneLoadBalancing": {
         "Enabled": false
       }
   },
   "LoadBalancerName": "my-loadbalancer"
 }
```

2. (Optional) Use the following [describe-load-balancer-attributes](../../../cli/latest/reference/elb/describe-load-balancer-attributes.md "../../../cli/latest/reference/elb/describe-load-balancer-attributes.md") command to verify that
   cross-zone load balancing is disabled for your load balancer:

```
`aws elb describe-load-balancer-attributes --load-balancer-name `my-loadbalancer``
```

The following is an example response:

```
{
    "LoadBalancerAttributes": {
        "ConnectionDraining": {
            "Enabled": false,
            "Timeout": 300
        },
        "CrossZoneLoadBalancing": {
            "Enabled": false
        },
        "ConnectionSettings": {
            "IdleTimeout": 60
        },
        "AccessLog": {
            "Enabled": false
        }
    }
}

```
