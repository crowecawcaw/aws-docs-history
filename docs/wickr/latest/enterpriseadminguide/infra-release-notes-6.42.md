This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Infrastructure 6.42 release

The following release notes include information for infrastructure release 6.42. For
information on the release timeline, see [Change log](#infra-release-notes-6.42-change-log "#infra-release-notes-6.42-change-log").

**Platform version**

|                |                                                                        |
| -------------- | ---------------------------------------------------------------------- |
| Infrastructure | 6.42.2<br>Replicated Native Scheduler (2046)<br>Replicated KOTS (1762) |

**Improvements**:

Addressed an issue affecting single sign-on (SSO) networks, where users may miss
notifications for initiating a device sync on the Wickr Android app when it is sent to the
background. This also leads to Switchboard restarting.

The problem occurs only when all of the following conditions are met during a device
sync:

1. The network is SSO-enabled.
2. The primary device is an Android.
3. The Wickr app is running in the background.
4. No recent messages have been received by the Wickr app.
   **Platform version**

|                |                                                                              |
| -------------- | ---------------------------------------------------------------------------- |
| Infrastructure | 6.42.1 Patch<br>Replicated Native Scheduler (2039)<br>Replicated KOTS (1759) |

**Improvements**:

Migrated to the new Google Firebase Cloud Messaging (FCM) v1 API for Android
notifications.

**Platform version**

|                |                                                                        |
| -------------- | ---------------------------------------------------------------------- |
| Infrastructure | 6.42.1<br>Replicated Native Scheduler (2027)<br>Replicated KOTS (1690) |

**Improvements**:

Allow Switchboard to handle empty header requests without restarting. This should mitigate
intermittent connection banners and failed messages in specific scenarios.

## Change log

**Change log for 6.42 release and release notes**

| Change                                                             | Description                                                    | Date               |
| ------------------------------------------------------------------ | -------------------------------------------------------------- | ------------------ |
| Infrastructure version 6.42.1> Infrastructure version 6.42.2       | SSO improvement                                                | September 25, 2024 |
| Infrastructure version 6.42.1> Infrastructure version 6.42.1 Patch | Migration                                                      | September 17, 2024 |
| Final release                                                      | Final notes with Replicated build number                       | August 27, 2024    |
| Infrastructure update                                              | Updates to address vulnerability scan results and improvements | August 26, 2024    |
