# View the Application Load Balancer resource map

The Application Load Balancer resource map provides an interactive display of your load balancer's
architecture, including its associated listeners, rules, target groups, and
targets. The resource map also highlights the relationships and routing paths
between all resources, producing a visual representation of your load balancer's
configuration.

###### To view the resource map for your Application Load Balancer

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, choose **Load Balancers**.
3. Select the load balancer.
4. Choose the **Resource map** tab to display the load balancer's
   resource map.

## Resource map components

###### Map views

There are two views available in the Application Load Balancer resource map: **Overview**, and **Unhealthy
Target Map**. **Overview** is selected by default and displays
all of your load balancer's resources. Selecting the **Unhealthy Target Map**
view will only display the unhealthy targets and the resources associated to them.

The **Unhealthy Target Map** view can be used to troubleshoot targets that are
failing health checks. For more information, see
[Troubleshoot unhealthy targets using the resource map](load-balancer-troubleshooting.md#troubleshoot-with-resourcemap "load-balancer-troubleshooting.md#troubleshoot-with-resourcemap").

###### Resource groups

The Application Load Balancer resource map contains four resource groups, one for each resource type. The resource
groups are **Listeners**, **Rules**,
**Target groups**, and **Targets**.

###### Resource tiles

Each resource within a group has its own tile, which displays details about
that specific resource.

- Hovering over a resource tile highlights the
  relationships between it and other resources.
- Selecting a resource tile highlights the
  relationships between it and other resources,
  and displays additional details about that resource.
  - **rule conditions:** The conditions for each rule.
  - **target group health summary:** The number of registered targets for each health status.
  - **target health status** The targets current health status and description.

###### Note

You can turn off **Show resource details** to hide additional
details within the resource map.

- Each resource tile contains a link that, when selected, navigates to
  that resource's details page.
  - **Listeners** ‐ Select the listeners protocol:port. For example, `HTTP:80`
  - **Rules** ‐ Select the rules action. For example, `Forward to target group`
  - **Target groups** ‐ Select the target group name. For example, `my-target-group`
  - **Targets** ‐ Select the targets ID. For example, `i-1234567890abcdef0`

###### Export the resource map

Selecting **Export** gives you the option of exporting the current
view of your Application Load Balancer's resource map as a PDF.
