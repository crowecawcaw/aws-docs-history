# Updating a router network interface in

MediaConnect

After creating a router network interface in MediaConnect, you can modify its configuration to
adapt to changing network requirements. This enables you to update the properties of your
public and VPC interfaces, ensuring that your network setup remains flexible and
up-to-date.

## Prerequisites

- The following procedure assumes that you’ve already created a router network
  interface.
- For VPC interfaces only: If you plan to change your VPC or security group
  settings, make sure that the VPC interface you're updating isn't currently associated
  with any router inputs or outputs.

## Procedure

###### To update a router network interface

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/ "https://console.aws.amazon.com/mediaconnect/").
2. In the navigation pane, choose **Router network
   interfaces**.
3. Select the router network interface that you want to update.
4. Choose **Edit**.
5. Update any of the following settings:
   - For public interfaces: You can edit the interface name, the inbound
     connections setting, and the allowed CIDR blocks.
   - For VPC interfaces: You can edit the subnet and the security groups
     selections.

6. Choose **Save changes**.
7. Check the outcome:
   1. If successful: The router network interface will be updated with your
      changes.
   2. If unsuccessful: You'll see an error message explaining what went
      wrong.

## Next steps

After you update a network interface, you can [review the updated network interface](viewing-router-network-interfaces.md "viewing-router-network-interfaces.md")
to verify that your updates were successful.

## Additional

resources

To update a router network interface programmatically, see the following page in the
_MediaConnect API Reference_:

- [UpdateRouterNetworkInterface](../api/API_UpdateRouterNetworkInterface.md "../api/API_UpdateRouterNetworkInterface.md")

This includes information about how to use this operation and parameters in one of the
language-specific AWS SDKs.
