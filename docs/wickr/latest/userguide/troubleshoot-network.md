This guide provides documentation for AWS Wickr. For Wickr
Enterprise, which is the on-premises version of Wickr, see [Enterprise Administration Guide](../enterpriseadminguide/what-is-wickr.md "../enterpriseadminguide/what-is-wickr.md").

# Troubleshoot network and connectivity issues

This section helps you troubleshoot network and connectivity issues with
AWS Wickr. Most connectivity problems are caused by your network configuration,
not the Wickr service. If the steps below don't resolve your issue, contact
your Wickr network administrator.

###### Topics

- [Before you begin](#troubleshoot-network-before "#troubleshoot-network-before")
- [Common connectivity issues](#troubleshoot-network-common "#troubleshoot-network-common")
- [Collect information for your administrator](#troubleshoot-network-logs "#troubleshoot-network-logs")

## Before you begin

Verify the following before troubleshooting:

- You are using the correct Wickr product for your organization:
  **AWS Wickr**,
  **AWS WickrGov** (GovCloud), or
  **Wickr Enterprise** (self-hosted).
  Ask your administrator if you're not sure.
- You are running a supported client version. To check, open Wickr
  and choose **Settings**,
  **About**. To update, see
  [Check for
  updates](updates.md "updates.md").
- Your device meets
  [system
  requirements](system-requirements.md "system-requirements.md").
- Your internet connection is active.

## Common connectivity issues

### Cannot connect to Wickr

If Wickr displays "Unable to connect," is stuck on a loading screen,
or times out, the most common cause is your network blocking Wickr
traffic.

###### To determine if the issue is your network

1. Verify your internet connection is working by opening a web page
   or using another app.
2. Disconnect from your corporate WiFi or VPN.
3. Connect to a different network — cellular data (mobile) or
   a non-corporate WiFi network.
4. Open Wickr and try to connect.

- **If Wickr connects on the other
  network** — Your corporate network is blocking
  Wickr traffic. Contact your network administrator and let them
  know that Wickr works on other networks but not on your
  organization's network.
- **If Wickr fails on all
  networks** — Restart your device and try again.
  If the issue persists, collect logs and contact your administrator.
  See [Collect information for your administrator](#troubleshoot-network-logs "#troubleshoot-network-logs").

###### Note

If your device is managed by your organization, you may not be able
to connect to a different network. In this case, contact your network
administrator directly and describe the error you see.

### Intermittent connectivity (frequent disconnects)

If Wickr frequently shows "Reconnecting" or drops your connection,
try the following:

1. **Test on a different network.**
   Switch to cellular data or a different WiFi network. If the issue
   stops, your original network is unstable or interfering with
   Wickr.
2. **Disconnect from VPN.** If you are
   on a VPN, disconnect temporarily and test. Some VPN configurations
   cause intermittent connectivity with Wickr.
3. **Restart Wickr.** Close the
   application completely and reopen it.
4. **Restart your device.** A full
   restart clears network state that can cause connection issues.

If the issue persists only on your organization's network, contact your
network administrator.

### Wickr not working over VPN

If Wickr works without VPN but not with VPN connected:

1. Confirm the issue by disconnecting VPN and testing Wickr.
2. Contact your network administrator and let them know that Wickr
   works without VPN but fails when VPN is connected. Your administrator
   may need to configure split tunneling or allowlist Wickr domains
   on the VPN.

###### Note

VPN issues are managed by your organization's IT team. Wickr
requires access to specific domains and ports that your VPN may be
blocking. Your administrator can find the full list in the
[network requirements](../adminguide/network-requirements.md "../adminguide/network-requirements.md") documentation.

## Collect information for your administrator

If the issue persists after the steps above, collect the following
information for your administrator:

- The exact error message or behavior you see
- Whether Wickr works on cellular data or other networks
- Whether you are connected to a VPN
- Your device model and operating system version
- Wickr client version
- Client logs (see
  [Collect logs for your administrator](troubleshoot-enduser.md#troubleshoot-enduser-logs "troubleshoot-enduser.md#troubleshoot-enduser-logs"))
