# AWS Site-to-Site VPN tunnel endpoint replacements

Your Site-to-Site VPN connection consists of two VPN tunnels for redundancy. Sometimes, one or both
of the VPN tunnel endpoints is replaced when AWS performs tunnel updates, or when you modify
your VPN connection. During a tunnel endpoint replacement, connectivity over the tunnel
might be interrupted while the new tunnel endpoint is provisioned.

###### Topics

- [Customer initiated endpoint replacements](#endpoint-replacements-for-vpn-modifications "#endpoint-replacements-for-vpn-modifications")
- [AWS managed endpoint replacements](#endpoint-replacements-for-aws-updates "#endpoint-replacements-for-aws-updates")
- [AWS Site-to-Site VPN tunnel endpoint lifecycle control](tunnel-endpoint-lifecycle.md "tunnel-endpoint-lifecycle.md")

## Customer initiated endpoint replacements

When you modify the following components of your VPN connection, one or both of your
tunnel endpoints is replaced.

| Modification                                                                                             | API action                                                                                                                                                                  | Tunnel impact                                                            |
| -------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Modify the target gateway for the VPN connection](modify-vpn-target.md "modify-vpn-target.md")          | [ModifyVpnConnection](../../../AWSEC2/latest/APIReference/API_ModifyVpnConnection.md "../../../AWSEC2/latest/APIReference/API_ModifyVpnConnection.md")                      | Both tunnels are unavailable while new tunnel endpoints are provisioned. |
| [Change the customer gateway for the VPN connection](change-vpn-cgw.md "change-vpn-cgw.md")              | [ModifyVpnConnection](../../../AWSEC2/latest/APIReference/API_ModifyVpnConnection.md "../../../AWSEC2/latest/APIReference/API_ModifyVpnConnection.md")                      | Both tunnels are unavailable while new tunnel endpoints are provisioned. |
| [Modify the VPN connection options](modify-vpn-connection-options.md "modify-vpn-connection-options.md") | [ModifyVpnConnectionOptions](../../../AWSEC2/latest/APIReference/API_ModifyVpnConnectionOptions.md "../../../AWSEC2/latest/APIReference/API_ModifyVpnConnectionOptions.md") | Both tunnels are unavailable while new tunnel endpoints are provisioned. |
| [Modify the VPN tunnel options](modify-vpn-tunnel-options.md "modify-vpn-tunnel-options.md")             | [ModifyVpnTunnelOptions](../../../AWSEC2/latest/APIReference/API_ModifyVpnTunnelOptions.md "../../../AWSEC2/latest/APIReference/API_ModifyVpnTunnelOptions.md")             | The modified tunnel is unavailable during the update.                    | ## AWS managed endpoint replacements AWS Site-to-Site VPN is a managed service, and periodically applies updates to your VPN tunnel endpoints. These updates happen for a variety of reasons, including the following: <br>• To apply general upgrades, such as patches, resiliency improvements, and other enhancements <br>• To retire underlying hardware <br>• When automated monitoring determines that a VPN tunnel endpoint is unhealthy AWS applies tunnel endpoint updates to one tunnel of your VPN connection at a time. During a tunnel endpoint update, your VPN connection might experience a brief loss of redundancy. It’s therefore important to configure both tunnels in your VPN connection for high availability. |
