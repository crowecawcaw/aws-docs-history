# Delete an AWS Site-to-Site VPN connection and gateway

If you no longer need an AWS Site-to-Site VPN connection, you can delete it. When you delete a Site-to-Site VPN
connection, we do not delete the customer gateway or virtual private gateway that was
associated with the Site-to-Site VPN connection. If you no longer need the customer gateway and virtual
private gateway, you can delete them.

###### Warning

If you delete your Site-to-Site VPN connection and then create a new one, you must download a
new configuration file and reconfigure the customer gateway device.

###### Tasks

- [Delete a VPN connection](delete-vpn-connection.md "delete-vpn-connection.md")
- [Delete a customer gateway](delete-cgw.md "delete-cgw.md")
- [Detach and delete a virtual private gateway](delete-vgw.md "delete-vgw.md")
