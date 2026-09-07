

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Release notes
<a name="release-notes"></a>

To help you keep track of the ongoing updates and improvements to Wickr, we publish release notices that describe recent changes.

## August 2026
<a name="august-2026-updates"></a>
+ **Non-SSO device sync** - Users with password-based (non-SSO) accounts can now transfer their account and message history when signing in on a new device. The sync flow supports QR code scanning and manual code entry across desktop and mobile platforms. Previously, device sync was only available for SSO-configured accounts.
+ **Need Help link** - A help link is now available on the sign-in and registration screens across all platforms, making it easier for users to access support resources during onboarding.

## June 2026
<a name="june-2026-updates"></a>
+ **Session Timeout** - Admins can now configure an inactivity timeout that automatically locks the Wickr client after a specified period. Users are prompted to re-authenticate to resume their session.
+ **Consent Banner** - Admins can now configure a consent banner that displays to users upon login. Users must acknowledge the banner before accessing the application.

## March 2026
<a name="march-2026-updates"></a>
+ Accessibility has been improved throughout the admin console, including updates to ATAK help panels, SSO configuration, and network creation flows.

## December 2025
<a name="december-2025-updates"></a>
+ Device suspend and unsuspend actions have been removed from the admin console. Administrators can continue to reset user devices.

## November 2025
<a name="november-2025-updates"></a>
+ Improved UI and UX for network and security group tables, along with console metrics for page load and API call monitoring.

## August 2025
<a name="august-2025-updates"></a>
+ Email templates for AWS Wickr and AWS WickrGov have been updated to improve the user onboarding experience. The sender email address has changed from `donotreply@wickr.email` to `no-reply@amazonaws.com`.

## May 2025
<a name="may-2025-updates"></a>
+ File preview is now available. When file downloads are disabled by the admin in the admin console for a security group, users will only be able to view a list of supported files in Messaging and Files tabs.

## March 2025
<a name="march-2025-updates"></a>
+ Redesigned Wickr administrator console is now available.

## October 2024
<a name="october-2024-updates"></a>
+ Wickr now supports delete network. For more information, see [Delete network in AWS Wickr](https://docs.aws.amazon.com/wickr/latest/adminguide/delete-network.html).

## September 2024
<a name="september-2024-updates"></a>
+  Administrators can now configure AWS Wickr with Microsoft Entra (Azure AD) single sign-on. For more information, see [Configure AWS Wickr with Microsoft Entra (Azure AD) single sign-on](https://docs.aws.amazon.com/wickr/latest/adminguide/entra-ad-sso.html).

## August 2024
<a name="august-2024-updates"></a>
+ Enhancements
  + Wickr is now available in the Europe (Zurich) AWS Region.

## June 2024
<a name="june-2024-updates"></a>
+  Cross Boundary classification and federation is now available for GovCloud users. For more information, see [GovCloud cross boundary classification and federation](https://docs.aws.amazon.com/wickr/latest/adminguide/govcloud-cross-boundary.html).

## April 2024
<a name="april-2024-updates"></a>
+  Wickr now supports read receipts. For more information, see [Read receipts](https://docs.aws.amazon.com/wickr/latest/adminguide/read-receipts.html).

## March 2024
<a name="march-2024-updates"></a>
+  Global Federation now supports restricted federation, where global federation can be enabled only for selected networks that are added under restricted federation. This works for Wickr networks in other AWS Regions. For more information, see [Security groups](https://docs.aws.amazon.com/wickr/latest/adminguide/security-groups.html).
+ Administrators can now view their usage analytics on the Analytics dashboard in the Admin Console. For more information, see [Analytics dashboard](https://docs.aws.amazon.com/wickr/latest/adminguide/dashboard.html).

## February 2024
<a name="february-2024-updates"></a>
+  AWS Wickr is now offering a three-month free trial of its Premium plan for up to 30 users. Changes and limitations include:
  + All Standard and Premium plan features such as unlimited admin controls and data retention are now available in the Premium free trial. The guest user feature is not available during the Premium free trial.
  + The previous Free trial is no longer available. You can upgrade your existing Free trial or Standard plan to a Premium free trial if you haven't already used the Premium free trial. For more information, see [Manage plan](https://docs.aws.amazon.com/wickr/latest/adminguide/manage-plan.html).

## November 2023
<a name="november-2023-updates"></a>
+  Guest users feature is now generally available. Changes and additions include:
  + Ability to report abuse by other Wickr users.
  + Administrators can view a list of guest users a network has interacted with, and monthly usage counts.
  + Administrators can block guest users from communicating with their network.
  + Add-on pricing for guest users.
+ Admin control enhancements
  + Ability to bulk delete/suspend users.
  + Additional SSO setting to configure a grace period for token refresh.

## October 2023
<a name="october-2023-updates"></a>
+ Enhancements
  + Wickr is now available in the Europe (Frankfurt) AWS Region.

## September 2023
<a name="september-2023-updates"></a>
+ Enhancements
  + Wickr networks now have the ability to federate across AWS Regions. For more information, see [Security groups](https://docs.aws.amazon.com/wickr/latest/adminguide/security-groups.html).

## August 2023
<a name="august-2023-updates"></a>
+ Enhancements
  + Wickr is now available in the Europe (London) AWS Region.

## July 2023
<a name="july-2023-updates"></a>
+ Enhancements
  + Wickr is now available in the Canada (Central) AWS Region.

## May 2023
<a name="may-2023-updates"></a>
+ Enhancements
  + Added support for guest users. For more information, see [Guest users in AWS Wickr network](guest-users.md).

## March 2023
<a name="march-2023-updates"></a>
+ Wickr is now integrated with AWS CloudTrail. For more information, see [Logging AWS Wickr API calls using AWS CloudTrail](logging-using-cloudtrail.md).
+ Wickr is now available in AWS GovCloud (US-West) as WickrGov. For more information, see [AWS WickrGov](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-wickr.html) in the *AWS GovCloud (US) User Guide*.
+ Wickr now supports tagging. For more information, see [Network tags for AWS Wickr](network-tags.md). Multiple networks can now be created in Wickr. For more information, see [Step 1: Create a network](getting-started-step1.md).

## February 2023
<a name="february-2023-updates"></a>
+ Wickr now supports the Android Tactical Assault Kit (ATAK). For more information, see [Enable ATAK in the Wickr Network Dashboard](what-is-atak.md#atak).

## January 2023
<a name="january-2023-updates"></a>
+ Single sign-on (SSO) can now be configured on all plans, including Free Trial and Standard.