This guide provides documentation for AWS Wickr. For Wickr
Enterprise, which is the on-premises version of Wickr, see [Enterprise Administration Guide](../enterpriseadminguide/what-is-wickr.md "../enterpriseadminguide/what-is-wickr.md").

# Troubleshoot voice and video call issues

This section helps you troubleshoot common voice and video call issues with
AWS Wickr. Most call quality and connectivity problems are caused by network
configuration. If the steps below don't resolve your issue, contact your Wickr
network administrator.

###### Topics

- [Before you begin](#troubleshoot-calls-before "#troubleshoot-calls-before")
- [Common call issues](#troubleshoot-calls-common "#troubleshoot-calls-common")
- [Collect information for your administrator](#troubleshoot-calls-logs "#troubleshoot-calls-logs")

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

## Common call issues

### Calls fail to connect

If calls fail to connect or drop immediately, the most common cause is
your network blocking the required traffic.

###### To determine if the issue is your network

1. Disconnect from your corporate WiFi or VPN.
2. Connect to cellular data (mobile) or a non-corporate network.
3. Try the call again.

- **If the call works on cellular data but not corporate
  WiFi** — Your corporate network is blocking Wickr traffic.
  Contact your network administrator and share the
  [Wickr network requirements](../adminguide/network-requirements.md "../adminguide/network-requirements.md").
- **If the call fails on all networks** —
  The issue may be with the Wickr service. Collect logs and contact your
  administrator. See [Collect information for your administrator](#troubleshoot-calls-logs "#troubleshoot-calls-logs").

### Test TCP calling (diagnostic)

Wickr uses UDP for voice and video calls by default. If UDP is blocked by
your network, you can test with TCP as a diagnostic step.

###### To enable TCP calling

1. Open Wickr and choose **Settings**.
2. Choose **Calling**.
3. Enable **TCP calling**.
4. Try the call again.

If the call succeeds with TCP enabled, UDP traffic is blocked by your
network firewall. Contact your network administrator to allowlist the UDP ports
listed in the [network requirements](../adminguide/network-requirements.md "../adminguide/network-requirements.md").

###### Note

TCP calling is a diagnostic tool, not a permanent solution. Call quality
is reduced when using TCP. Work with your network administrator to enable
UDP for optimal performance.

### Poor call quality (choppy audio, frozen video)

Poor call quality is typically caused by network bandwidth or latency
issues.

- **Test on a different network.** If quality
  improves on cellular data or a home network, the issue is your corporate
  network bandwidth or configuration.
- **Reduce participants.** Group calls with
  many participants require more bandwidth. Try a 1:1 call to isolate the
  issue.
- **Disable video.** If audio works but video
  is poor, your available bandwidth may be insufficient for video. Try an
  audio-only call.
- **Check your headset or microphone.** If
  others can hear you but you sound distorted, try a different audio device.
  Update your audio drivers if on desktop.

## Collect information for your administrator

If the issue persists after the steps above and occurs on all networks,
collect the following information for your administrator or AWS Support:

- Call type: 1:1, group, or room
- Number of participants
- Date and time of the failed call
- Your device model and operating system version
- Wickr client version
- Whether the issue occurs on cellular data, corporate WiFi, or both
- Client logs (see
  [Collect logs for your administrator](troubleshoot-enduser.md#troubleshoot-enduser-logs "troubleshoot-enduser.md#troubleshoot-enduser-logs"))
