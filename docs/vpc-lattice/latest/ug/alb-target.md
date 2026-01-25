# Application Load Balancers as targets in VPC Lattice

You can create a VPC Lattice target group, register a single internal Application Load Balancer as the
target, and configure your VPC Lattice service to forward traffic to this target group. In
this scenario, the Application Load Balancer takes over the routing decision as soon as traffic reaches it.
This configuration allows you to use the layer 7 request-based routing feature of the
Application Load Balancer in combination with features that VPC Lattice supports, such as IAM authentication
and authorization, and connectivity across VPCs and accounts.

###### Limitations

- You can register a single internal Application Load Balancer as the target in a VPC Lattice
  target group of type `ALB`.
- You can register an Application Load Balancer as a target of up to two VPC Lattice target groups,
  used by two different VPC Lattice services.
- VPC Lattice does not provide health checks for an `ALB` type target group.
  However, you can configure health checks independently at the load balancer
  level for the targets in Elastic Load Balancing. For more information, see [Target group health checks](../../../elasticloadbalancing/latest/application/target-group-health-checks.md "../../../elasticloadbalancing/latest/application/target-group-health-checks.md") in the _User Guide for Application Load Balancers_

## Prerequisites

Create an Application Load Balancer to register as a target with your VPC Lattice target group. The
load balancer must meet the following criteria:

- The load balancer scheme is **Internal**.
- The Application Load Balancer must be in the same account as the VPC Lattice target group, and must
  be in the **Active** state.
- The Application Load Balancer must be in the same VPC as the VPC Lattice target group.
- You can use HTTPS listeners on the Application Load Balancer to terminate TLS, but only if the
  VPC Lattice service uses the same SSL/TLS certificate as the load balancer.
- To preserve the client IP of the VPC Lattice service in the
  `X-Forwarded-For` request header, you must set the attribute for
  the Application Load Balancer `routing.http.xff_header_processing.mode` to
  `Preserve`. If the value is `Preserve`, the load
  balancer preserves the `X-Forwarded-For` header in the HTTP request,
  and sends it to targets without any change.

For more information, see [Create an Application Load Balancer](../../../elasticloadbalancing/latest/application/create-application-load-balancer.md "../../../elasticloadbalancing/latest/application/create-application-load-balancer.md") in the _User Guide for Application Load Balancers_.

## Step 1: Create a target group of type ALB

Use the following procedure to create the target group. Note that VPC Lattice does not
support health checks for `ALB` target groups. However, you can configure health checks
for the target groups for your Application Load Balancer. For more information, see [Target group health checks](../../../elasticloadbalancing/latest/application/target-group-health-checks.md "../../../elasticloadbalancing/latest/application/target-group-health-checks.md") in the _User Guide for Application Load Balancers_.

###### To create the target group

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the navigation pane, under **VPC Lattice**, choose
   **Target groups**.
3. Choose **Create target group**.
4. On the **Specify target group details** page,
   under **Basic configuration**, choose **Application Load Balancer**
   as the target type.
5. For **Target group name**, enter a name for
   the target group.
6. For **Protocol**, choose `HTTP`,
   `HTTPS`, or `TCP`. The target
   group protocol must match the protocol of the listener for your internal
   Application Load Balancer.
7. For **Port**, specify the port for your target group. This port must match
   the port of the listener for your internal Application Load Balancer. You can alternatively add a
   listener port on the internal Application Load Balancer to match the target group port that you
   specify here.
8. For **VPC**, select the same virtual private
   cloud (VPC) that you selected when you created the internal Application Load Balancer.
   This should be the VPC that contains your VPC Lattice resources.
9. For **Protocol version**, choose the protocol version
   that your Application Load Balancer supports.
10. (Optional) Add any required tags.
11. Choose **Next**.

## Step 2: Register the Application Load Balancer as a target

You can either register the load balancer as a target now or later on.

###### To register an Application Load Balancer as a target

1. Choose **Register now**.
2. For **Application Load Balancer**, choose your internal Application Load Balancer.
3. For **Port**, keep the default or specify a different port
   as needed. This port must match an existing listener port on your Application Load Balancer. If you
   continue without a matching port, traffic won't reach your Application Load Balancer.
4. Choose **Create target group**.
