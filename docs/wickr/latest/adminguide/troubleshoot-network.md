

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Troubleshoot network and connectivity issues
<a name="troubleshoot-network"></a>

This section helps administrators troubleshoot network and connectivity issues with AWS Wickr. Most connectivity problems reported by end users are caused by corporate network configuration (firewalls, proxies, VPNs) blocking required Wickr traffic. If the steps in this section don't resolve your issue, open a case in the [AWS Support Center](https://console.aws.amazon.com/support/home).

**Topics**
+ [Before you begin](#troubleshoot-network-before)
+ [Common network issues](#troubleshoot-network-common)
+ [Determine the scope of the issue](#troubleshoot-network-scope)
+ [Additional resources](#troubleshoot-network-resources)

## Before you begin
<a name="troubleshoot-network-before"></a>

Verify the following before troubleshooting:
+ You have access to your organization's network configuration (firewall rules, proxy settings, VPN configuration).
+ You have reviewed the [Wickr network requirements](https://docs.aws.amazon.com/wickr/latest/adminguide/allow-list-ports-domains.html) (required domains and ports).
+ You have confirmed whether the issue affects all users, specific users, or specific locations.
+ You have confirmed whether affected users can connect on a non-corporate network (cellular data or home WiFi).

**Important**  
If users can connect on cellular data or home WiFi but not on your corporate network, the issue is your network configuration — not the Wickr service.

## Common network issues
<a name="troubleshoot-network-common"></a>

### Firewall blocking Wickr traffic
<a name="troubleshoot-network-firewall"></a>

This is the most common cause of connectivity failures. Wickr requires access to specific domains and ports.

Symptoms  
Users cannot connect on corporate WiFi but can connect on cellular data. Multiple users in the same location are affected. Wickr worked previously but stopped after a network change.

Resolution  

1. Review the full list of required domains and ports in [Network requirements for Wickr](https://docs.aws.amazon.com/wickr/latest/adminguide/allow-list-ports-domains.html).

1. Allowlist all required domains in your firewall. Wickr requires HTTPS (TCP 443) for messaging and signaling, and UDP ports for voice and video calling.

1. Verify DNS resolution for required domains from within your corporate network. Use `nslookup` or `dig` to confirm domains resolve.

1. Test connectivity after making changes. Have affected users restart Wickr and attempt to connect.

**Note**  
If only voice and video calls fail but messaging works, UDP traffic is likely blocked. Wickr uses UDP for calls by default. See [UDP blocked (calls fail, messaging works)](#troubleshoot-network-udp).

### Proxy server interference
<a name="troubleshoot-network-proxy"></a>

Corporate proxy servers can interfere with Wickr connections, particularly if they do not support WebSocket connections.

Symptoms  
Connection issues only when proxy is configured. Wickr works when proxy is bypassed. Intermittent disconnects.

Resolution  

1. Verify your proxy supports WebSocket connections (required for Wickr messaging).

1. Configure a proxy bypass (PAC file exception or direct connection rule) for Wickr domains listed in the [network requirements](https://docs.aws.amazon.com/wickr/latest/adminguide/allow-list-ports-domains.html).

1. Review proxy logs for blocked or failed connections to Wickr domains.

1. If your proxy requires authentication, verify that Wickr traffic is not being rejected due to missing credentials. Wickr does not support proxy authentication on SaaS deployments.

### SSL/TLS inspection breaking connections
<a name="troubleshoot-network-ssl"></a>

Corporate SSL inspection (also called HTTPS inspection or TLS interception) breaks the certificate chain that Wickr expects, causing connection failures.

Symptoms  
Certificate errors in Wickr. "Secure connection failed" errors. Wickr works on networks without SSL inspection.

Resolution  

1. **Preferred:** Bypass SSL inspection for Wickr domains. Configure your SSL inspection appliance to exclude the domains listed in the [network requirements](https://docs.aws.amazon.com/wickr/latest/adminguide/allow-list-ports-domains.html). This maintains Wickr's end-to-end encryption.

1. **Alternative:** Install your organization's root CA certificate on user devices. This allows Wickr to trust the intercepted certificate chain. Contact your IT security team for the certificate and installation instructions.

To verify whether SSL inspection is the cause, run the following command from an affected device and compare the certificate issuer to the expected AWS certificate:

```
openssl s_client -showcerts -connect ingress-prod-calling.wickr.us-east-1.amazonaws.com:443
```

If the certificate issuer shows your organization's CA instead of an AWS or Amazon certificate, SSL inspection is active for Wickr traffic.

### VPN blocking Wickr
<a name="troubleshoot-network-vpn"></a>

VPN configurations commonly block Wickr traffic, particularly UDP ports required for calling.

Symptoms  
Wickr works without VPN but not with VPN connected. Connection drops when VPN connects. Calls fail but messaging works over VPN.

Resolution  

1. Configure split tunneling to route Wickr traffic directly (bypassing the VPN tunnel) for the domains listed in the [network requirements](https://docs.aws.amazon.com/wickr/latest/adminguide/allow-list-ports-domains.html).

1. If split tunneling is not permitted, ensure the VPN allows both TCP 443 and the UDP ports listed in the network requirements.

1. If only calls fail over VPN, the VPN likely blocks UDP. See [UDP blocked (calls fail, messaging works)](#troubleshoot-network-udp).

### UDP blocked (calls fail, messaging works)
<a name="troubleshoot-network-udp"></a>

Wickr uses UDP for voice and video calls by default and falls back to TCP. If your network blocks UDP, calls will fail to connect right away and will fall back to TCP with potentially degraded performance, while messaging continues to work normally. You can enable (force) TCP calling within the Wickr Network Security Group to skip UDP entirely, forcing all calls to TCP.

Diagnostic  
Ask the affected user to enable TCP calling as a test (or administratively enable/force TCP through the console for all users): **Settings**, **Calling**, enable **TCP calling**. If calls succeed with TCP enabled, UDP is blocked.

Resolution  
Allowlist the UDP ports listed in the [network requirements](https://docs.aws.amazon.com/wickr/latest/adminguide/allow-list-ports-domains.html) in your firewall and VPN configuration.  
TCP calling is a diagnostic tool, not a permanent solution. Call quality is reduced when using TCP.

### DNS resolution failures
<a name="troubleshoot-network-dns"></a>

If your DNS servers cannot resolve Wickr domains, the client cannot connect.

Diagnostic  
From a device on the affected network, verify DNS resolution for a required Wickr domain:  

```
nslookup gw-pro-prod.wickr.com
```
If the domain does not resolve, the issue is DNS configuration.

Resolution  

1. Verify your DNS servers can resolve the domains listed in the [network requirements](https://docs.aws.amazon.com/wickr/latest/adminguide/allow-list-ports-domains.html).

1. If using DNS filtering or a DNS firewall, add exceptions for Wickr domains.

1. Test with an alternative DNS server (such as `8.8.8.8`) to confirm whether the issue is your internal DNS.

## Determine the scope of the issue
<a name="troubleshoot-network-scope"></a>

Use the following questions to narrow down the cause:
+ **Does Wickr work on cellular data or home WiFi?** If yes, the issue is your corporate network configuration.
+ **Are all users affected, or only specific users?** If all users at a location are affected, the issue is network-wide. If only specific users, check their device or VPN configuration.
+ **Did this start after a network change?** Firewall rule updates, proxy changes, or VPN configuration changes commonly break Wickr connectivity.
+ **Does messaging work but calls fail?** This indicates UDP is blocked. See [UDP blocked (calls fail, messaging works)](#troubleshoot-network-udp).
+ **Do users see certificate errors?** This indicates SSL inspection is intercepting Wickr traffic. See [SSL/TLS inspection breaking connections](#troubleshoot-network-ssl).

## Additional resources
<a name="troubleshoot-network-resources"></a>
+ [Network requirements for AWS Wickr](https://docs.aws.amazon.com/wickr/latest/adminguide/allow-list-ports-domains.html) (required domains and ports)
+ [End-user network troubleshooting](https://docs.aws.amazon.com/wickr/latest/userguide/troubleshoot-network.html) (share with affected users)