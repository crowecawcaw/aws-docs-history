# Deleting a router network interface in

MediaConnect

You can delete router network interfaces that are no longer needed for your workflow.
This helps you to maintain a clean network configuration and reduce unused resources.

###### Important

After you delete a network interface, you can't recover it. You'll need to create a
new one if you need similar functionality later.

## Prerequisites

Before you begin:

- Make sure no router I/Os are currently using the router network interface you want
  to delete.
- Consider documenting the router network interface's configuration in case you need
  to recreate it later.

## Procedure

###### To delete a router network interface

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/ "https://console.aws.amazon.com/mediaconnect/").
2. In the navigation pane, choose **Router network
   interfaces**.
3. Choose the name of the router network interface that you want to delete.
4. Choose **Delete**.
5. To confirm, choose **Delete router network interface**.

###### Note

The deleted interface might still appear in your list for about an hour, but it
won't be functional.

## Next steps

After deleting a network interface, you can:

- [Create a new network
  interface](creating-router-network-interfaces.md "creating-router-network-interfaces.md") with different settings if needed.
- [Review your remaining network
  interfaces](viewing-router-network-interfaces.md "viewing-router-network-interfaces.md") to ensure your network setup is complete.

## Additional

resources

To delete network interfacesprogrammatically, see the following page in the
_MediaConnect API Reference_:

- [DeleteRouterNetworkInterface](../api/API_DeleteRouterNetworkInterface.md "../api/API_DeleteRouterNetworkInterface.md")

This includes information about how to use the
`DeleteRouterNetworkInterface` operation and its parameters in one of the
language-specific AWS SDKs.
