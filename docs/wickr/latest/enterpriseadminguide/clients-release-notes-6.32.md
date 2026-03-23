This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Clients 6.32 release

The following release notes include information for clients release 6.32. For information on
the release timeline, see [Change log](#clients-release-notes-6.32-change-log "#clients-release-notes-6.32-change-log").

**Platform versions**

|                        |        |
| ---------------------- | ------ |
| Android                | 6.32.3 |
| iOS                    | 6.32.9 |
| Desktop (Mac, Windows) | 6.32.5 |
| Linux                  | 6.32.5 |

**Android**

New features:

- Added a floating action button (FAB) that allows users to cycle through messages in chat
  that failed to send.
- Added media upload options under a new "Performance" settings menu to control image
  compression when uploading media depending on your internet connection.
  Changes, enhancements, and resolved issues:

Fixed crash caused by mutable typing indicator fields

Improvements:

- Video media preview are now in line with messages and can be played from the
  preview
- Added a preview for new rich text formatting options, which can be found under Settings >
  Appearance
  **iOS**

New features:

- Added a floating action button (FAB) that allows users to cycle through messages in chat
  that failed to send
- Added media upload options under a new "Performance" settings menu to control image
  compression when uploading media depending on your internet connection.
  Changes, enhancements, and resolved issues:

Fixed bug where sent attachments or locations would not display in a chat, but would still
be received

Improvements:

- Video media preview are now in line with messages and can be played from the
  preview
- Added a preview for new rich text formatting options, which can be found under Settings >
  Appearance
  **Desktop**

New features:

Added a floating action button (FAB) that allows users to cycle through messages in chat
that failed to send

Changes, enhancements, and resolved issues:

Mitigate potential OAuth server poisoning

Improvements:

- Added a preview for new messaging UI, including rich text formatting options, which can be
  found under Settings > Appearance
- Filetype allowlist introduced for in-client previews. All filetypes are still allowed to
  download.

## Change log

**Change log for 6.32 release and release notes**

| Change          | Description                                                    | Date              |
| --------------- | -------------------------------------------------------------- | ----------------- |
| Clients update  | Updates to address vulnerability scan results and new features | February 13, 2024 |
| Initial release | Initial release of February release notes                      | February 5, 2024  |
