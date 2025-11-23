# Migrate from a virtual private

gateway to an Direct Connect gateway

You can migrate a virtual private gateway attached to a virtual interface to a Direct Connect
gateway.

If you're using Direct Connect with VPCs that currently bypass a parent Availability Zone you
won't be able to migrate your Direct Connect connections or virtual interfaces.

The following steps describe the steps you need to take to migrate a virtual private
gateway to a Direct Connect gateway.

###### To migrate to a Direct Connect gateway

1. Create a Direct Connect gateway.

If the Direct Connect gateway does not yet exist, you'll need to create it. For the
steps to create a Direct Connect gateway, see [Create a Direct Connect gateway](create-direct-connect-gateway.md "create-direct-connect-gateway.md"). 2. Create a virtual interface for the Direct Connect gateway.

A virtual interface is required for migration. If the interface does not exist,
you'll need to create it. For the steps to create the virtual interface, see [Virtual interfaces](create-vif.md "create-vif.md"). 3. Associate the virtual private gateway with the Direct Connect gateway.

Both the Direct Connect gateway and a virtual private gateway need to be associated.
For the steps to create the association, see [Associate or disassociate virtual private gateways](associate-vgw-with-direct-connect-gateway.md "associate-vgw-with-direct-connect-gateway.md"). 4. Delete the virtual interface that was associated with the virtual private
gateway. For more information, see [Delete a virtual interface](deletevif.md "deletevif.md").
