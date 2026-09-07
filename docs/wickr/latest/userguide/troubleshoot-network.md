

This guide provides documentation for AWS Wickr. For Wickr Enterprise, which is the on-premises version of Wickr, see [Enterprise Administration Guide](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/what-is-wickr.html).

# Troubleshoot network and connectivity issues
<a name="troubleshoot-network"></a>

This section helps you troubleshoot network and connectivity issues with AWS Wickr. Most connectivity problems are caused by your network configuration, not the Wickr service. If the steps below don't resolve your issue, contact your Wickr network administrator.

**Topics**
+ [Before you begin](#troubleshoot-network-before)
+ [Common connectivity issues](#troubleshoot-network-common)
+ [Collect information for your administrator](#troubleshoot-network-logs)

## Before you begin
<a name="troubleshoot-network-before"></a>

Verify the following before troubleshooting:
+ You are using the correct Wickr product for your organization: **AWS Wickr**, **AWS WickrGov** (GovCloud), or **Wickr Enterprise** (self-hosted). Ask your administrator if you're not sure.
+ You are running a supported client version. To check, open Wickr and choose **Settings**, **About**. To update, see [Check for updates](https://docs.aws.amazon.com/wickr/latest/userguide/updates.html).
+ Your device meets [system requirements](https://docs.aws.amazon.com/wickr/latest/userguide/system-requirements.html).
+ Your internet connection is active.

## Common connectivity issues
<a name="troubleshoot-network-common"></a>

### Cannot connect to Wickr
<a name="troubleshoot-network-cannot-connect"></a>

If Wickr displays "Unable to connect," is stuck on a loading screen, or times out, the most common cause is your network blocking Wickr traffic.

**To determine if the issue is your network**

1. Verify your internet connection is working by opening a web page or using another app.

1. Disconnect from your corporate WiFi or VPN.

1. Connect to a different network — cellular data (mobile) or a non-corporate WiFi network.

1. Open Wickr and try to connect.
+ **If Wickr connects on the other network** — Your corporate network is blocking Wickr traffic. Contact your network administrator and let them know that Wickr works on other networks but not on your organization's network.
+ **If Wickr fails on all networks** — Restart your device and try again. If the issue persists, collect logs and contact your administrator. See [Collect information for your administrator](#troubleshoot-network-logs).

**Note**  
If your device is managed by your organization, you may not be able to connect to a different network. In this case, contact your network administrator directly and describe the error you see.

### Intermittent connectivity (frequent disconnects)
<a name="troubleshoot-network-intermittent"></a>

If Wickr frequently shows "Reconnecting" or drops your connection, try the following:

1. **Test on a different network.** Switch to cellular data or a different WiFi network. If the issue stops, your original network is unstable or interfering with Wickr.

1. **Disconnect from VPN.** If you are on a VPN, disconnect temporarily and test. Some VPN configurations cause intermittent connectivity with Wickr.

1. **Restart Wickr.** Close the application completely and reopen it.

1. **Restart your device.** A full restart clears network state that can cause connection issues.

If the issue persists only on your organization's network, contact your network administrator.

### Wickr not working over VPN
<a name="troubleshoot-network-vpn"></a>

If Wickr works without VPN but not with VPN connected:

1. Confirm the issue by disconnecting VPN and testing Wickr.

1. Contact your network administrator and let them know that Wickr works without VPN but fails when VPN is connected. Your administrator may need to configure split tunneling or allowlist Wickr domains on the VPN.

**Note**  
VPN issues are managed by your organization's IT team. Wickr requires access to specific domains and ports that your VPN may be blocking. Your administrator can find the full list in the [ network requirements](https://docs.aws.amazon.com/wickr/latest/adminguide/network-requirements.html) documentation.

## Collect information for your administrator
<a name="troubleshoot-network-logs"></a>

If the issue persists after the steps above, collect the following information for your administrator:
+ The exact error message or behavior you see
+ Whether Wickr works on cellular data or other networks
+ Whether you are connected to a VPN
+ Your device model and operating system version
+ Wickr client version
+ Client logs (see [ Collect logs for your administrator](https://docs.aws.amazon.com/wickr/latest/userguide/troubleshoot-enduser.html#troubleshoot-enduser-logs))