

This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html).

# Clients 6.22 release
<a name="clients-release-notes-6.22"></a>

The following release notes include information for clients release 6.22. For information on the release timeline, see [Change log](#clients-release-notes-6.22-change-log).

**Platform versions**


|  |  | 
| --- | --- | 
| Android | 6.22.3 | 
| iOS | 6.22.2 | 
| Desktop (Mac, Windows) | 6.22.1 | 
| Linux | 6.22.1 | 

**Android**

New features:

Support for multi-region federation. Enterprise customers can now federate with AWS Wickr customers in AWS Canada (Central) and London regions in addition to Northern Virginia.

Changes, enhancements, and resolved issues:
+ Added error message for SSO provider exceptions (crash fix)
+ Fixed threading crash when accessing conversation membership
+ Fixed issue where guest users would get an error when registering mid-registration
+ Fixed message edit and reply layouts overlapping
+ Fixed FAQ link in guest user restricted user interface (UI)
+ Fixed not showing guest user restricted user interface (UI) as soon as the last licensed user leaves the conversation
+ Added missing create password CTA analytics
+ 6.22.3 - Addressed calling compatibility with Android 13, September 2023 security update

Improvements:
+ Accessibility improvements
+ Registration loading buttons announce the loading action
+ Fallback to user domain if file domain is blank when downloading files
+ Refresh user domain if user domain is blank when downloading files

**iOS**

New features:

Support for multi-region federation. Enterprise customers can now federate with AWS Wickr customers in AWS Canada (Central) and London regions in addition to Northern Virginia.

Changes, enhancements, and resolved issues:
+ Fixed issue where users could not create a room without adding other members first
+ Fixed issue where users could not download an image when certificate pinning was enabled

Improvements:
+ Background file upload/download support
+ Accessibility improvements for account deletion
+ Reduced menu latency in listing members to add to a room

**Desktop**

New features:

Support for multi-region federation. Enterprise customers can now federate with AWS Wickr customers in AWS Canada (Central) and London regions in addition to Northern Virginia.

Changes, enhancements, and resolved issues:
+ Implemented retry logic on getUserInfo error handling in case network issues occur. The new logic will improve room recovery.
+ (Security) Updated bot buttons to escape HTML prior to displaying.

Improvements: German translation updates

## Change log
<a name="clients-release-notes-6.22-change-log"></a>

**Change log for 6.22 release and release notes**


| Change | Description | Date | 
| --- | --- | --- | 
| Android version 6.22.1 > version 6.22.3 update | Android 13, September 2023 security update | October 4, 2023 | 
| Clients update | Multi-region updates | September 28, 2023 | 
| Initial release | Initial release of September release notes | September 28, 2023 | 