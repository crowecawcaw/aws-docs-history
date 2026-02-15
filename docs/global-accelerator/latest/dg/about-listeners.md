# Add a standard listener

This section provides the steps to create a standard listener on the AWS Global Accelerator console. To complete
this task by using an API operation instead of the console, see [`CreateListener`](../api/API_CreateListener.md "../api/API_CreateListener.md"),
in the _AWS Global Accelerator API Reference_.

# To add a listener

1. Open the Global Accelerator console at [https://us-west-2.console.aws.amazon.com/globalaccelerator/home#GlobalAcceleratorHome:](https://us-west-2.console.aws.amazon.com/globalaccelerator/home#GlobalAcceleratorHome: "https://us-west-2.console.aws.amazon.com/globalaccelerator/home#GlobalAcceleratorHome:").
2. On the **accelerators** page, choose an accelerator.
3. Choose **Add listener**.
4. On the **Add listener** page, enter the ports or port ranges that you
   want to associate with the listener. Listeners support ports 1-65535.
5. Choose the protocol for the ports that you entered.
6. Optionally, choose to enable client affinity. Client affinity for a listener means
   that Global Accelerator ensures that connections from a specific source (client) IP address
   are always routed to the same endpoint. To enable this behavior, in the dropdown
   list, choose **Source IP**.

The default is **None**, which means that client affinity is not
enabled and Global Accelerator distributes traffic equally between the endpoints in the endpoint groups
for the listener.

For more information, see [How client affinity works in Global Accelerator](about-listeners-client-affinity.md "about-listeners-client-affinity.md"). 7. Choose **Add listener**.
