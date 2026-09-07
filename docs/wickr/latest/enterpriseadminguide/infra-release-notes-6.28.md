

This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html).

# Infrastructure 6.28 release
<a name="infra-release-notes-6.28"></a>

The following release notes include information for infrastructure release 6.28. For information on the release timeline, see [Change log](#infra-release-notes-6.28-change-log).

**Platform version**


|  |  | 
| --- | --- | 
| Infrastructure | 6.28.1 (1840) | 

**New features**:
+ Wickr Open Access (WOA) through deeplink: Wickr Open Access can now be enforced at client setup through deeplink. Force WOA must be enabled in the administrator dashboard for this feature to function.
+ Configuration naming: Administrators can now enter custom names to identify the Wickr Enterprise configurations they generate for client setup.

**Changes, enhancements, and resolved issues**:

The issue of not being able to save security group names has been resolved.

**Improvements**:
+ Device sync improvements: Users no longer require a camera for QR code scanning to sync conversation history. Users can input a code to sync as long as the original device is on hand.
+ Enhanced message failure UX: Users are more clearly alerted when a message fails to send and can easily cycle through failures. Retry logic has improved on the backend for better reliability.
+ Logging enhancements: UserID has been reintroduced to logs as a verbosity setting in the administrator dashboard. If an administrator wants UserID present in logs, it is now included in the header for easier analysis.
+ Upgraded to Node 18 for WickrServerDirectory, WickrServerReceipt, WickrServerCrond, WickrServerSchema, WickrServerAPI, and WickrServerFileProxy.

## Change log
<a name="infra-release-notes-6.28-change-log"></a>

**Change log for 6.28 release and release notes**


| Change | Description | Date | 
| --- | --- | --- | 
| Final release | Final notes with Replicated build number | December 20, 2023 | 
| Infrastructure update | Updates to address vulnerability scan results, new features, and patching. | December 19, 2023 | 
| Initial release | Initial release of December release notes | December 11, 2023 | 