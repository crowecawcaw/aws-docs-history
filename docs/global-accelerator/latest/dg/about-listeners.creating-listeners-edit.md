

# Edit a standard listener
<a name="about-listeners.creating-listeners-edit"></a>

This section provides the steps to edit a standard listener on the AWS Global Accelerator console. To complete this task by using an API operation instead of the console, see [`UpdateListener`](https://docs.aws.amazon.com/global-accelerator/latest/api/API_UpdateListener.html) in the *AWS Global Accelerator API Reference*.

# To edit a standard listener


1. Open the Global Accelerator console at [ https://us-west-2.console.aws.amazon.com/globalaccelerator/home\#GlobalAcceleratorHome:](https://us-west-2.console.aws.amazon.com/globalaccelerator/home#GlobalAcceleratorHome:). 

1. On the **accelerators** page, choose an accelerator.

1. Choose a listener, and then choose **Edit listener**.

1. On the **Edit listener** page, change the ports, port ranges, or protocols that you want to associate with the listener.

1. Optionally, choose to enable client affinity. Client affinity for a listener means that Global Accelerator ensures that connections from a specific source (client) IP address are always routed to the same endpoint. To enable this behavior, in the dropdown list, choose **Source IP**.

   The default is **None**, which means that client affinity is not enabled and Global Accelerator distributes traffic equally between the endpoints in the endpoint groups for the listener.

   For more information, see [How client affinity works in Global Accelerator](about-listeners-client-affinity.md).

1. Choose **Save**.