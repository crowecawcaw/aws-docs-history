This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Clients 6.70 release

The following release notes include information for clients release 6.70. For information on
the release timeline, see [Change log](#clients-release-notes-6.70-change-log "#clients-release-notes-6.70-change-log").

**Platform versions**

|                               |        |
| ----------------------------- | ------ |
| Android                       | 6.70.2 |
| iOS                           | 6.70.4 |
| Desktop (Mac, Windows, Linux) | 6.70.4 |

**Android**

New features:

- Theme setting added to Appearance settings
- Password complexity requirements displayed during account creation and password changes
- Directory contacts limited to 100 with search prompt for larger directories
- Forgot password flow includes back button navigation
- New bot UI enabled for all builds
  Changes, enhancements, and resolved issues:

- Fixed emoji picker tab crash
- Fixed recent files search scoping to active conversation
- Fixed registration deeplinks for WickrGov Gamma
- Fixed media permission handling for newer Android SDK versions
  **iOS**

New features:

- Dark mode settings with theme switching
- Password complexity requirements displayed during account creation
- Directory contacts limited to 100 with search prompt for larger directories
  Changes, enhancements, and resolved issues:

- Fixed dark/light mode theme switching
- Fixed guided tour pop up delay
- Fixed iOS 26 search bar styling and cancel button
- Fixed app reset notification handling during sign-in flow
- Fixed region manager for Gamma builds
- Fixed markdown rendering for messages containing # characters
  **Desktop**

New features:

- Wickr Edge database migration support
- MLS protocol updated to SDK v0.29.5
  Changes, enhancements, and resolved issues:

- Fixed crash on launch when no internet connection
- Fixed crash in getConversationDetails
- Fixed message forwarding search deduplication
- Fixed call timer to start only when call is answered
- Fixed password requirements not clearing on environment reset
- Fixed Edit Group Details panel Save/Discard button behavior
- Fixed cancel file download button
- Fixed saved links panel overflow
- Fixed "More Unread" button visibility
- Fixed web sign-in regression
- Data retention indicator restored to desktop web UI
- Manage Users panel updates correctly on user actions
- Directory limited to first 100 users with search prompt

## Change log

**Change log for 6.70 release and release notes**

| Change          | Description                     | Date          |
| --------------- | ------------------------------- | ------------- |
| Initial release | Initial release of April update | April 9, 2026 |
