This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Clients 6.26 release

The following release notes include information for clients release 6.26. For information on
the release timeline, see [Change log](#clients-release-notes-6.26-change-log "#clients-release-notes-6.26-change-log").

**Platform versions**

|                        |        |
| ---------------------- | ------ |
| Android                | 6.26.9 |
| iOS                    | 6.26.6 |
| Desktop (Mac, Windows) | 6.26.1 |
| Linux                  | 6.26.1 |

**Android**

New features: Guest user support

Changes, enhancements, and resolved issues:

Fixed regression causing keyboard to open behind file popup.

Improvements:

- Accessibility improvements
- German translation improvements
- Added analytics event for entering AWS Wickr from a registration deep link
- Updated RxJava
- Adjusted hostname passed into calling library
- Added guards against buffer overflow in calling library
- Added dialog when user has permissions permanently denied when trying to take
  picture/video
- Updated device sync UI to match AWS Wickr
  **iOS**

New features: Guest user support

Changes, enhancements, and resolved issues:

- Prevented automatically reading all messages in conversation
- Fixed a user being able to send a voice memo when the capability was turned off in the
  admin dashboard
  Improvements:

- Accessibility improvements
- Added “don't remind me again” option to WOA alert on file upload
  **Desktop**

New features: Guest user support

Changes, enhancements, and resolved issues:

- Fixed certain UI elements not translating when system language is in Spanish
- Fixed alignment of screenshare selector
- Fixed pinned file name clearing after pressing cancel
- Removed irrelevant error "File name must contain only valid characters" seen when user
  exceeds 260 characters while renaming a saved file using save file to room/save file to
  conversation
- Fixed Room A file name showing when a user edits the saved file name of Room B
- Fixed a crash when a user selects 'save as' when burn-on-read time is about to end on any
  file attachment
- Fixed continuous loading on the submit button when a Windows user enters wrong code for
  the second time during device verification
- Fixed wrong call duration showing in chat view when a user disconnects the call from
  Room/1:1/Group
- Fixed login failure with high CPU usage when certificate pinning was disabled
- Fixed and issue on Mac where uninstalling did not remove any data, just the
  application
- Fixed bot commands showing out of order in relation to output

## Change log

**Change log for 6.26 release and release notes**

| Change          | Description                               | Date              |
| --------------- | ----------------------------------------- | ----------------- |
| Clients update  | General availability of guest user access | November 16, 2023 |
| Initial release | Initial release of November release notes | November 8, 2023  |
