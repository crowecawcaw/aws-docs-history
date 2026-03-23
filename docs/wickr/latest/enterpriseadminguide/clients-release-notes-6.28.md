This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Clients 6.28 release

The following release notes include information for clients release 6.28. For information on
the release timeline, see [Change log](#clients-release-notes-6.28-change-log "#clients-release-notes-6.28-change-log").

**Platform versions**

|                        |        |
| ---------------------- | ------ |
| Android                | 6.28.9 |
| iOS                    | 6.28.8 |
| Desktop (Mac, Windows) | 6.28.1 |
| Linux                  | 6.28.1 |

**Android**

New features:

- Wickr Open Access (WOA) through deeplink
- Typing indicator: Users now see an indication within the conversation of someone
  typing
  Changes, enhancements, and resolved issues:

- Fixed logic around message error notifications
- Fixed not subscribing to user activity for a conversation that is focused
- Fixed failed message notification visibility logic
- Fixed the need to tap create room/direct message button twice
- Fixed crash when changing languages while on the support screen

###### Note

**Android version 6.28.9 Hotfix**

Fixed a crash caused by navigating between different dashboard elements

Improvements:

- Accessibility improvements
- Recreate crypto context on new device when re-sending notification during device
  sync
  **iOS**

New features:

- Wickr Open Access (WOA) through deeplink
- Typing indicator: Users now see an indication within the conversation of someone
  typing
  Changes, enhancements, and resolved issues:

- Fixed issue where users without email domain in username couldn't open files from desktop
  and Android clients
- Fixed incorrect burn-on-read value setting
- Fixed music not pausing for a Wickr call when using Apple CarPlay

###### Note

**iOS version 6.28.8 Hotfix**

Removed nonfunctional "performance" UI button

Improvements:

Accessibility improvements

**Desktop**

New features:

- Wickr Open Access (WOA) through deeplink

###### Note

The Wickr Enterprise Linux client does not support deeplink

- Typing indicator: Users now see an indication within the conversation of someone
  typing
  Changes, enhancements, and resolved issues:

- Fixed an issue with invalid call duration data in the retention bot logs
- Guard against AWSWickr OAuth server poisoning
- Fixed showing stale timestamps for unread messages
  Improvements:

- Guard against invalid MSN values
- Switch to allowlist for valid files to open as a preview

## Change log

**Change log for 6.28 release and release notes**

| Change                                                        | Description                                   | Date              |
| ------------------------------------------------------------- | --------------------------------------------- | ----------------- |
| Android version 6.28.8 > Android version 6.28.9 Hotfix update | Navigation update                             | January 12, 2024  |
| iOS version 6.28.6 > iOS version 6.28.8 Hotfix update         | UI setting update                             | January 5, 2024   |
| Clients update                                                | Updates to address vulnerability scan results | December 20, 2023 |
| Initial release                                               | Initial release of December release notes     | December 11, 2023 |
