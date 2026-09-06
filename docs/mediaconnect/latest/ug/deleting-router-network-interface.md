

# Deleting a router network interface in MediaConnect
<a name="deleting-router-network-interface"></a>

You can delete router network interfaces that are no longer needed for your workflow. This helps you to maintain a clean network configuration and reduce unused resources.

**Important**  
After you delete a network interface, you can't recover it. You'll need to create a new one if you need similar functionality later.

## Prerequisites
<a name="deleting-router-network-interface-prerequisites"></a>

Before you begin:
+ Make sure no router I/Os are currently using the router network interface you want to delete.
+ Consider documenting the router network interface's configuration in case you need to recreate it later.

## Procedure
<a name="deleting-router-network-interface-procedure"></a><a name="delete-router-network-interface-procedure"></a>

**To delete a router network interface**

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/).

1. In the navigation pane, choose **Router network interfaces**.

1. Choose the name of the router network interface that you want to delete.

1. Choose **Delete**.

1. To confirm, choose **Delete router network interface**.

**Note**  
The deleted interface might still appear in your list for about an hour, but it won't be functional.

## Next steps
<a name="deleting-router-network-interface-next-steps"></a>

After deleting a network interface, you can:
+ [Create a new network interface](creating-router-network-interfaces.md) with different settings if needed.
+ [Review your remaining network interfaces](viewing-router-network-interfaces.md) to ensure your network setup is complete.

## Additional resources
<a name="deleting-router-network-interface-additional-resources"></a>

To delete network interfacesprogrammatically, see the following page in the *MediaConnect API Reference*:
+ [DeleteRouterNetworkInterface](https://docs.aws.amazon.com/mediaconnect/latest/api/API_DeleteRouterNetworkInterface.html)

This includes information about how to use the `DeleteRouterNetworkInterface` operation and its parameters in one of the language-specific AWS SDKs.