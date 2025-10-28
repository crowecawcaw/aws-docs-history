# View the Network Load Balancer resource map

The Network Load Balancer resource map provides an interactive display of your Network Load Balancers
architecture, including its associated listeners, target groups, and
targets. The resource map also highlights the relationships and routing paths
between all resources, producing a visual representation of your Network Load Balancers
configuration.

###### To view the resource map for your load balancer

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, choose **Load Balancers**.
3. Select the Network Load Balancer.
4. Choose the **Resource map** tab.

## Resource map components

###### Map views

There are two views available in the Network Load Balancer resource map: **Overview**, and **Unhealthy
Target Map**. **Overview** is selected by default and displays
all of your Network Load Balancer's resources. Selecting the **Unhealthy Target Map**
view will only display the unhealthy targets and the resources associated to them.

The **Unhealthy Target Map** view can be used to troubleshoot targets that are
failing health checks. For more information, see
[Troubleshoot unhealthy targets using the resource map](load-balancer-troubleshooting.md#troubleshoot-with-resourcemap "load-balancer-troubleshooting.md#troubleshoot-with-resourcemap").

###### Resource columns

The Network Load Balancer resource map contains three resource columns, one for each resource type. The resource
groups are **Listeners**,
**Target groups**, and **Targets**.

###### Resource tiles

Each resource within a column has its own tile, which displays details about
that specific resource.

- Hovering over a resource tile highlights the
  relationships between it and other resources.
- Selecting a resource tile highlights the
  relationships between it and other resources,
  and displays additional details about that resource.
  - **target group health summary:** The number of registered targets for each health status.
  - **target health status:** The target's current health status and description.

###### Note

You can turn off **Show resource details** to hide additional
details within the resource map.

- Each resource tile contains a link that, when selected, navigates to
  that resource's details page.
  - **Listeners** ‐ Select the listeners protocol:port. For example, `TCP:80`
  - **Target groups** ‐ Select the target group name. For example, `my-target-group`
  - **Targets** ‐ Select the targets ID. For example, `i-1234567890abcdef0`

###### Export the resource map

Selecting **Export** gives you the option of exporting the current
view of your Network Load Balancer's resource map as a PDF.
