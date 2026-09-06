

# Configuring visible Regions and services in the AWS Management Console
<a name="visible-regions-services"></a>

Account administrators can control which AWS Regions and AWS services are visible in the AWS Management Console navigation. These account-level settings are available on the **Account settings** tab of the Unified Settings page. When you hide a Region, it is removed from the Region selector for all users in the account. When you hide a service, it appears as unavailable in a separate section of the Services menu for all users in the account. Hidden services are also grayed out in Unified Search results and in the Recently Visited and Favorites widgets on Console Home.

If a user navigates directly to a hidden Region or service through a URL, they see an overlay that informs them the Region or service is hidden at the account level.

**Note**  
Navigation to the Unified Settings page is always available, so administrators can't lock themselves out of these settings. If a user doesn't have the required permissions, or if the AWS User Experience Customization service is unavailable, all Regions and services are visible by default.

**Topics**
+ [Prerequisites for configuring visible Regions and services](visible-regions-services-prereqs.md)
+ [Configuring visible Regions in the AWS Management Console](configure-visible-regions.md)
+ [Configuring visible services in the AWS Management Console](configure-visible-services.md)