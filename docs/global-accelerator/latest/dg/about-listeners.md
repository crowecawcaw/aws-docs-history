# Edit a standard listener

This section provides the steps to edit a standard listener on the AWS Global Accelerator console. To complete
this task by using an API operation instead of the console, see [`UpdateListener`](../api/API_UpdateListener.md "../api/API_UpdateListener.md") in the _AWS Global Accelerator API Reference_.

# To edit a standard listener

1. Open the Global Accelerator console at [https://us-west-2.console.aws.amazon.com/globalaccelerator/home#GlobalAcceleratorHome:](https://us-west-2.console.aws.amazon.com/globalaccelerator/home#GlobalAcceleratorHome: "https://us-west-2.console.aws.amazon.com/globalaccelerator/home#GlobalAcceleratorHome:").
2. On the **accelerators** page, choose an accelerator.
3. Choose a listener, and then choose **Edit listener**.
4. On the **Edit listener** page, change the ports, port ranges, or
   protocols that you want to associate with the listener.
5. Optionally, choose to enable client affinity. Client affinity for a listener means
   that Global Accelerator ensures that connections from a specific source (client) IP address
   are always routed to the same endpoint. To enable this behavior, in the dropdown
   list, choose **Source IP**.

The default is **None**, which means that client affinity is not
enabled and Global Accelerator distributes traffic equally between the endpoints in the endpoint groups
for the listener.

For more information, see [How client affinity works in Global Accelerator](about-listeners-client-affinity.md "about-listeners-client-affinity.md"). 6. Choose **Save**.
