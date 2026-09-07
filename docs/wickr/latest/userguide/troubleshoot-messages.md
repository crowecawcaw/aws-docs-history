

This guide provides documentation for AWS Wickr. For Wickr Enterprise, which is the on-premises version of Wickr, see [Enterprise Administration Guide](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/what-is-wickr.html).

# Troubleshoot message delivery issues
<a name="troubleshoot-messages"></a>

This section helps you troubleshoot common message delivery issues with AWS Wickr, including unsent messages, missing messages, and delivery failures. If the steps below don't resolve your issue, contact your Wickr network administrator.

**Topics**
+ [Before you begin](#troubleshoot-messages-before)
+ [Common message issues](#troubleshoot-messages-common)
+ [Collect information for your administrator](#troubleshoot-messages-logs)

## Before you begin
<a name="troubleshoot-messages-before"></a>

Verify the following before troubleshooting:
+ You are using the correct Wickr product for your organization: **AWS Wickr**, **AWS WickrGov** (GovCloud), or **Wickr Enterprise** (self-hosted). Ask your administrator if you're not sure.
+ You are running a supported client version. To check, open Wickr and choose **Settings**, **About**. To update, see [Check for updates](https://docs.aws.amazon.com/wickr/latest/userguide/updates.html).
+ Your device meets [system requirements](https://docs.aws.amazon.com/wickr/latest/userguide/system-requirements.html).
+ Your internet connection is active.

## Common message issues
<a name="troubleshoot-messages-common"></a>

### Messages stuck as unsent
<a name="troubleshoot-messages-unsent"></a>

If a message shows as unsent (indicated by a warning icon or retry button), try the following steps in order.

1. **Manually retry the message.** Wickr does not automatically retry failed messages. Choose the retry button next to the unsent message.

1. **Check your internet connection.** Verify you have an active connection by opening a web page or another app.

1. **Test on a different network.** Switch to cellular data or a non-corporate network and retry the message.
+ **If messages send on cellular but not corporate WiFi** — Your corporate network is blocking Wickr traffic. Contact your network administrator and share the [ Wickr network requirements](https://docs.aws.amazon.com/wickr/latest/adminguide/network-requirements.html).
+ **If messages fail on all networks** — Try sending a message to a different contact. If that works, the issue may be with the recipient's account (see [Messages sent but not received by a specific contact](#troubleshoot-messages-recipient)).

### Messages sent but not received by a specific contact
<a name="troubleshoot-messages-recipient"></a>

If your messages appear sent but a specific contact does not receive them, consider the following causes:
+ **The contact blocked you.** If a contact blocks you, your messages appear to send successfully but are not delivered. This is expected behavior.
+ **The contact's account was deleted or suspended.** Contact your administrator to verify the recipient's account status.
+ **Federation settings.** If the contact is on a different Wickr network, federation must be enabled on both networks. Contact your administrator to verify federation settings.

### Missing messages
<a name="troubleshoot-messages-missing"></a>

If messages you previously received are no longer visible, the most common causes are message expiration and device sync limits.

Message expiration  
Wickr messages have an expiration time set by the sender. When the expiration time elapses, the message is automatically and permanently deleted. Additionally, messages with a burn-on-read timer are deleted after you view them and the timer completes. This is expected behavior and cannot be reversed.

Too many devices  
A Wickr account supports up to 10 devices, but sync issues can occur with more than 5 active devices. If messages appear on some devices but not others:  

1. Open **Settings**, then **Device Management**.

1. Remove devices you no longer use.

1. Keep 5 or fewer active devices for reliable sync.

Application reset  
If you recently reset the Wickr application or reset your password, all local message history is permanently deleted. This cannot be reversed. You may also become unverified, which can prevent you from receiving messages in rooms until a room moderator re-verifies you.

## Collect information for your administrator
<a name="troubleshoot-messages-logs"></a>

If the issue persists and is not explained by the causes above, collect the following information for your administrator or AWS Support:
+ Your email address (sender)
+ Date and time the message failed
+ Message type: 1:1, group, or room
+ Whether the issue affects all contacts or a specific contact
+ Whether the issue occurs on cellular data, corporate WiFi, or both
+ Your device model and operating system version
+ Wickr client version
+ Client logs (see [ Collect logs for your administrator](https://docs.aws.amazon.com/wickr/latest/userguide/troubleshoot-enduser.html#troubleshoot-enduser-logs))