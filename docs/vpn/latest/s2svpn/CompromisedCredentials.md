# Replace compromised credentials for an AWS Site-to-Site VPN connection

If you believe that the tunnel credentials for your Site-to-Site VPN connection have been
compromised, you can change the IKE pre-shared key or change the ACM certificate. The
method you use depends on the authentication option you used for your VPN tunnels. For more
information, see [AWS Site-to-Site VPN tunnel authentication options](vpn-tunnel-authentication-options.md "vpn-tunnel-authentication-options.md").

###### To change the IKE pre-shared key

You can modify the tunnel options for the VPN connection and specify a new
IKE pre-shared key for each tunnel. For more information, see [Modify AWS Site-to-Site VPN tunnel options](modify-vpn-tunnel-options.md "modify-vpn-tunnel-options.md").

Alternatively, you can delete the VPN connection. For more information,
see [Delete a VPN connection and gateway](delete-vpn.md "delete-vpn.md"). You don't need to delete the
VPC or the virtual private gateway. Then, create a new VPN connection using the same
virtual private gateway, and configure the new keys on your customer gateway device. You can
specify your own pre-shared keys for the tunnels or let AWS generate new pre-shared keys
for you. For more information, see [Create a VPN connection](SetUpVPNConnections.md#vpn-create-vpn-connection "SetUpVPNConnections.md#vpn-create-vpn-connection").
The tunnel's inside and outside addresses might change when you recreate the VPN connection.

###### To change the certificate for the AWS side of the tunnel endpoint

Rotate the certificate. For more information, see [Rotate VPN tunnel endpoint certificates](rotate-vpn-certificate.md "rotate-vpn-certificate.md").

###### To change the certificate on the customer gateway device

1. Create a new certificate. For information, see
   [Issuing and managing certificates](../../../acm/latest/userguide/gs.md "../../../acm/latest/userguide/gs.md") in the
   _AWS Certificate Manager User Guide_.
2. Add the certificate to the customer gateway device.
