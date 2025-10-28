# Enhanced AWS Site-to-Site VPN security features using Secrets Manager

AWS Site-to-Site VPN's Security Rebase feature provides enhanced security capabilities
that gives you greater control and visibility over your VPN connections. A key improvement is
the ability to store pre-shared keys (PSKs) in AWS Secrets Manager rather than directly in the Site-to-Site VPN
service, allowing for better secret management and compliance with security best practices.
The feature also includes a `GetActiveVpnTunnelStatus` API that provides real-time
visibility into the security parameters being used in active VPN tunnels, including encryption
algorithms, integrity algorithms, and Diffie-Hellman groups for both IKE phases. Additionally,
you can now generate recommended security configurations that enforce the use of modern
protocols by excluding legacy options such as IKEv1. These enhancements are particularly
valuable if your organization needs to maintain strict security standards, require detailed
audit trails of your VPN configurations, or want to ensure your VPN connections are using the
most secure protocols available.

###### Contents

- [Change the Secrets Manager pre-shared
  key](enhanced-security-tunnel.md "enhanced-security-tunnel.md")
- [Change the pre-shared key storage
  mode](enhanced-security-storage.md "enhanced-security-storage.md")
