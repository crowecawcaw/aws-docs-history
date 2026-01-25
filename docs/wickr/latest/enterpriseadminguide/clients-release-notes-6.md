This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Clients 6.34 release

The following release notes include information for clients release 6.34. For information on
the release timeline, see [Change log](#clients-release-notes-6.34-change-log "#clients-release-notes-6.34-change-log").

**Platform versions**

|                        |         |
| ---------------------- | ------- |
| Android                | 6.34.6  |
| iOS                    | 6.34.12 |
| Desktop (Mac, Windows) | 6.34.13 |
| Linux                  | 6.34.11 |

**Android**

Changes, enhancements, and resolved issues:

Fixed issue where conversations would not show as read when toggling between dashboard and
chat view.

Improvements:

- Accessibility improvements
- Added login hint to SSO. The IDP authentication page will now prepopulate email after a
  user’s initial entry.
  **iOS**

Changes and resolved issues:

- Fixed issue where HEIF images would not preview when sent from iOS.
- Fixed issue where sending live location would result in message send failure
  notification.
  Improvements:

- Accessibility improvements
- Added login hint to SSO. The IDP authentication page will now prepopulate email after a
  user’s initial entry.
  **Desktop**

Changes, enhancements, and resolved issues:

Added defensive logic to prevent corruption of User state information associated with
WickrUser alias

###### Note

**Desktop version 6.34.13 Hotfix**

Fixed an issue where using New User Experience with Wickr Open Access enabled resulted in
an infinite loading loop.

Improvements:

- Accessibility improvements
- Added .mov and .log filetypes to preview allowlist.
- Added login hint to SSO. The IDP authentication page will now prepopulate email after a
  user’s initial entry.

## Change log

**Change log for 6.34 release and release notes**

| Change                                            | Description                                                        | Date           |
| ------------------------------------------------- | ------------------------------------------------------------------ | -------------- |
| Desktop version 6.34.11 > Desktop version 6.34.13 | New User Experience update.                                        | April 2, 2024  |
| Clients update                                    | Updates to address vulnerability scan results and bug fix updates. | March 28, 2024 |
| Initial release                                   | Initial release of March release notes                             | March 20, 2024 |
