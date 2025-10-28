# HTTP listeners for VPC Lattice services

A listener is a process that checks for connection requests. You can define a listener
when you create your VPC Lattice service. You can add listeners to your service at any time.

The information on this page helps you create an HTTP listener for your service.
For information about creating listeners that use other protocols, see [HTTPS listeners](https-listeners.md "https-listeners.md") and
[TLS listeners](tls-listeners.md "tls-listeners.md").

## Prerequisites

- To add a forward action to the default listener rule, you must specify an
  available VPC Lattice target group. For more information, see [Create a VPC Lattice target group](create-target-group.md "create-target-group.md").
- You can specify the same target group in multiple listeners, but these
  listeners must belong to the same service. To use a target group with a
  VPC Lattice service, you must verify that it is not used by a listener for
  any other VPC Lattice service.

## Add an HTTP listener

You can add listeners and rules to your service at any time. You configure a
listener with a protocol and a port for connections from clients to the service, and
a VPC Lattice target group for the default listener rule. For more information, see [Listener configuration](listeners.md#listener-configuration "listeners.md#listener-configuration").

###### To add an HTTP listener using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **VPC Lattice**, choose
   **Services**.
3. Select the name of the service to open its details page.
4. On the **Routing** tab, choose **Add listener**.
5. For **Listener name**, you can either provide a custom
   listener name, or use the protocol and port of your listener as the
   listener name. A custom name that you specify can have up to 63 characters,
   and it must be unique for every service in your account. The valid
   characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the
   first or last character, or immediately after another hyphen. You cannot
   change the name after you create it.
6. For **Protocol : port**, choose **HTTP**
   and enter a port number.
7. For **Default action**, choose the VPC Lattice target group
   to receive traffic and choose the weight to assign to this target group. The
   weight that you assign to a target group sets its priority to receive
   traffic. For example, if two target groups have the same weight, each target
   group receives half of the traffic. If you've specified only one target
   group, then 100 percent of the traffic is sent to the one target
   group.

You can optionally add another target group for the default action. Choose
**Add action** and then choose a target group and specify
its weight. 8. (Optional) To add another rule, choose **Add rule** and then
enter a name, a priority, a condition, and an action for the rule.

You can give each rule a priority number between 1 and 100. A listener
can't have multiple rules with the same priority. Rules are evaluated in
priority order, from the lowest value to the highest value. The default rule
is evaluated last. For more information, see [Listener rules](listener-rules.md "listener-rules.md"). 9. (Optional) To add tags, expand **Listener tags**, choose
**Add new tag**, and enter a tag key and tag value. 10. Review your configuration, and then choose **Add**.

###### To add an HTTP listener using the AWS CLI

Use the [create-listener](../../../cli/latest/reference/vpc-lattice/create-listener.md "../../../cli/latest/reference/vpc-lattice/create-listener.md")
command to create a listener with a default rule, and the [create-rule](../../../cli/latest/reference/vpc-lattice/create-rule.md "../../../cli/latest/reference/vpc-lattice/create-rule.md") command
to create additional listener rules.
