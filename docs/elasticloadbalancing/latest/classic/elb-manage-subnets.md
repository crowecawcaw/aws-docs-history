# Configure subnets for your Classic Load Balancer

When you add a subnet to your load balancer, ELB creates a load balancer node in the
Availability Zone. Load balancer nodes accept traffic from clients and forward requests to the
healthy registered instances in one or more Availability Zones. We recommend that
you add one subnet per Availability Zone
for at least two Availability Zones. This improves the availability of your load balancer.
Note that you can modify the subnets for your load balancer at any time.

Select subnets from the same Availability Zones as your instances. If your load balancer is
an internet-facing load balancer, you must select public subnets in order for your
back-end instances to receive traffic from the load balancer (even if the back-end
instances are in private subnets). If your load balancer is an internal load balancer,
we recommend that you select private subnets. For more information about subnets for
your load balancer, see [Recommendations for your VPC](elb-backend-instances.md#set-up-ec2 "elb-backend-instances.md#set-up-ec2").

To add a subnet, register the instances in the Availability Zone with the load balancer,
then attach a subnet from that Availability Zone to the load balancer. For more information,
see [Register instances with your Classic Load Balancer](elb-deregister-register-instances.md "elb-deregister-register-instances.md").

After you add a subnet, the load balancer starts routing requests to the registered
instances in the corresponding Availability Zone. By default, the load balancer routes
requests evenly across the Availability Zones for its subnets. To route
requests evenly across the registered instances in the Availability Zones for its
subnets, enable cross-zone load balancing. For more information, see [Configure cross-zone load balancing for your Classic Load Balancer](enable-disable-crosszone-lb.md "enable-disable-crosszone-lb.md").

You might want to remove a subnet from your load balancer temporarily when its Availability
Zone has no healthy registered instances, or when you want to troubleshoot or update the
registered instances. After you've removed a subnet, the load balancer stops routing
requests to the registered instances in its Availability Zone, but continues to route
requests to the registered instances in the Availability Zones for the remaining
subnets. Note that after you remove a subnet, the instances in that subnet remain registered
with the load balancer, but you can deregister them if you choose. For more information, see
[Register instances with your Classic Load Balancer](elb-deregister-register-instances.md "elb-deregister-register-instances.md").

###### Contents

- [Requirements](#elb-subnet-requirements "#elb-subnet-requirements")
- [Configure subnets using the console](#add-remove-subnets-console "#add-remove-subnets-console")
- [Configure subnets using the CLI](#add-remove-subnets-cli "#add-remove-subnets-cli")

## Requirements

When you update the subnets for your load balancer, you must meet the following requirements:

- The load balancer must have at least one subnet at all times.
- You can add at most one subnet per Availability Zone.
- You cannot add a Local Zone subnet.

Because there are separate APIs to add and remove subnets from a load balancer,
you must consider the order of operations carefully when swapping the current
subnets for new subnets in order to meet these requirements. Also, you must
temporarily add a subnet from another Availability Zone if you need to swap all
subnets for your load balancer. For example, if your load balancer has a
single Availability Zone and you need to swap its subnet for another subnet, you
must first add a subnet from a second Availability Zone. Then you can remove the
subnet from the original Availability Zone (without going below one subnet),
add a new subnet from the original Availability Zone (without exceeding
one subnet per Availability Zone), and then remove the subnet from the second
Availability Zone (if it is only needed to perform the swap).

## Configure subnets using the console

Use the following procedure to add or remove subnets using the console.

###### To configure subnets using the console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**, choose
   **Load Balancers**.
3. Choose the name of the load balancer to open its detail page.
4. On the **Network mapping** tab, choose **Edit subnets**.
5. On the **Edit subnets** page, in the **Network mapping** section,
   add and remove subnets as needed..
6. When you are finished, choose **Save changes**.

## Configure subnets using the CLI

Use the following examples to add or remove subnets using the AWS CLI.

###### To add a subnet to your load balancer using the CLI

Use the following [attach-load-balancer-to-subnets](../../../cli/latest/reference/elb/attach-load-balancer-to-subnets.md "../../../cli/latest/reference/elb/attach-load-balancer-to-subnets.md") command to add two subnets to
your load balancer:

```
`aws elb attach-load-balancer-to-subnets --load-balancer-name `my-load-balancer` --subnets `subnet-dea770a9 subnet-fb14f6a2``
```

The response lists all subnets for the load balancer. For example:

```
{
    "Subnets": [
        "subnet-5c11033e",
        "subnet-dea770a9",
        "subnet-fb14f6a2"
    ]
}
```

###### To remove a subnet using the AWS CLI

Use the following [detach-load-balancer-from-subnets](../../../cli/latest/reference/elb/detach-load-balancer-from-subnets.md "../../../cli/latest/reference/elb/detach-load-balancer-from-subnets.md") command to remove the specified subnets
from the specified load balancer:

```
`aws elb detach-load-balancer-from-subnets --load-balancer-name `my-loadbalancer` --subnets `subnet-450f5127``
```

The response lists the remaining subnets for the load balancer. For example:

```
{
    "Subnets": [
        "subnet-15aaab61"
    ]
}
```
