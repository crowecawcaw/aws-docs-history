#

Add a standard endpoint group

You work with endpoint groups on the AWS Global Accelerator console or by using an API operation. You
can add or remove endpoints from an endpoint group at any time.

This section explains how to add a standard endpoint groups on the AWS Global Accelerator console. If you
want to use API operations with Global Accelerator, see the [AWS Global Accelerator API Reference](../api/Welcome.md "../api/Welcome.md").

# To add a standard endpoint group

1. Open the Global Accelerator console at [https://us-west-2.console.aws.amazon.com/globalaccelerator/home#GlobalAcceleratorHome:](https://us-west-2.console.aws.amazon.com/globalaccelerator/home#GlobalAcceleratorHome: "https://us-west-2.console.aws.amazon.com/globalaccelerator/home#GlobalAcceleratorHome:").
2. On the **Accelerators** page, choose an accelerator.
3. In the **Listeners** section, for **Listener ID**,
   choose the ID of the listener that you want to add an endpoint group to.
4. Choose **Add endpoint group**.
5. In the section for a listener, specify a Region for the endpoint group by choosing one
   from the dropdown list.
6. Optionally, for **Traffic dial**, enter a number from 0 to 100 to set a
   percentage of traffic for this endpoint group. The percentage is applied only to
   the traffic that is already directed to this endpoint group, not all listener
   traffic. By default, the traffic dial is set to 100.
7. Optionally, to override the listener port used for routing traffic to endpoints and reroute
   traffic to specific ports on your endpoints, choose **Configure port overrides**.
   For more information, see [Override listener ports for restricted ports or connection collisions](about-endpoint-groups-port-override.md "about-endpoint-groups-port-override.md").
8. Optionally, to specify custom health check values to be applied to EC2 instance and
   Elastic IP address endpoints, choose **Configure health checks**. For more
   information, see [Ensure health check access for your accelerator](about-endpoint-groups-health-check-options.md "about-endpoint-groups-health-check-options.md").
9. Optionally, choose **Add endpoint group** to add additional endpoint groups for this listener
   or other listeners.
10. Choose **Add endpoint group**.
