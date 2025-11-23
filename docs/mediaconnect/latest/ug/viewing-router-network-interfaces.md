# Viewing router network interfaces in

MediaConnect

You can view your router network interfaces in the MediaConnect console. For each interface,
you can see the configuration details, status, and associated resources.

## Prerequisites

The following procedure assumes you have at least one router network interface in your
AWS account.

## Procedure

Follow these steps to view the network interfaces that are available in your
AWS account.

###### To view your router network interfaces

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/ "https://console.aws.amazon.com/mediaconnect/").
2. In the navigation pane, choose **Router network
   interfaces**.
3. Review the list of your router network interfaces.
4. Select a router network interface and choose **View
   resource**.
5. On the details page, use the following tabs to find specific information:

| Router network interface details tabs | Tab                                                                                     | Description |
| ------------------------------------- | --------------------------------------------------------------------------------------- | ----------- |
| Inputs                                | View the router inputs that are using this network interface.                           |
| Outputs                               | View the router outputs that are using this network interface.                          |
| Configuration                         | View the basic configuration information and current state of the<br>network interface. |
| Tags                                  | View the tags that are applied to this network interface.                               |

## Next steps

After reviewing your network interfaces, you can:

- [Update your router network
  interface settings if needed](editing-router-network-interface.md "editing-router-network-interface.md")
- [Create additional
  router network interfaces](creating-router-network-interfaces.md#create-router-network-interfaces-procedure "creating-router-network-interfaces.md#create-router-network-interfaces-procedure")
- [Delete unused router network
  interfaces](deleting-router-network-interface.md "deleting-router-network-interface.md")

## Additional

resources

To view network interfaces programmatically, see the following pages in the _MediaConnect API Reference_:

- [ListRouterNetworkInterfaces](../api/API_ListRouterNetworkInterfaces.md "../api/API_ListRouterNetworkInterfaces.md")
- [GetRouterNetworkInterface](../api/API_GetRouterNetworkInterface.md "../api/API_GetRouterNetworkInterface.md")
- [BatchGetRouterNetworkInterface](../api/API_BatchGetRouterNetworkInterface.md "../api/API_BatchGetRouterNetworkInterface.md")

This includes information about how to use these operations and parameters in one of
the language-specific AWS SDKs.
