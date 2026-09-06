

# Updating a router network interface in MediaConnect
<a name="editing-router-network-interface"></a>

After creating a router network interface in MediaConnect, you can modify its configuration to adapt to changing network requirements. This enables you to update the properties of your public and VPC interfaces, ensuring that your network setup remains flexible and up-to-date.

## Prerequisites
<a name="editing-router-network-interface-prerequisites"></a>
+ The following procedure assumes that you’ve already created a router network interface.
+ For VPC interfaces only: If you plan to change your VPC or security group settings, make sure that the VPC interface you're updating isn't currently associated with any router inputs or outputs. 

## Procedure
<a name="editing-router-network-interface-procedure"></a><a name="edit-router-network-interface-procedure"></a>

**To update a router network interface**

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/).

1. In the navigation pane, choose **Router network interfaces**.

1. Select the router network interface that you want to update.

1. Choose **Edit**.

1. Update any of the following settings: 
   + For public interfaces: You can edit the interface name, the inbound connections setting, and the allowed CIDR blocks.
   + For VPC interfaces: You can edit the subnet and the security groups selections.

1. Choose **Save changes**.

1. Check the outcome:

   1. If successful: The router network interface will be updated with your changes.

   1. If unsuccessful: You'll see an error message explaining what went wrong.

## Next steps
<a name="editing-router-network-interface-next-steps"></a>

After you update a network interface, you can [review the updated network interface](viewing-router-network-interfaces.md) to verify that your updates were successful.

## Additional resources
<a name="editing-router-network-interface-additional-resources"></a>

To update a router network interface programmatically, see the following page in the *MediaConnect API Reference*:
+ [UpdateRouterNetworkInterface](https://docs.aws.amazon.com/mediaconnect/latest/api/API_UpdateRouterNetworkInterface.html)

This includes information about how to use this operation and parameters in one of the language-specific AWS SDKs. 