

# AWS User Experience Customization (UXC)
<a name="uxc"></a>

AWS User Experience Customization (UXC) is a utility that lets account administrators customize the visual appearance of the AWS Management Console and manage these settings at the account level.

With UXC, you can customize the following settings:
+ **Account color** – You can set a color for your accounts to visually distinguish between them. For example, you can use green for development accounts, yellow for test accounts, and red for production accounts.
+ **Service visibility** – You can control which AWS services appear in the console navigation. Service visibility simplifies the AWS Management Console to show only the AWS services that are relevant to your account.
+ **Region visibility** – You can control which AWS Regions appear in the Region selector. Region visibility simplifies the AWS Management Console to show only the Regions that are relevant to your account.

If you have not configured a setting, then the default behavior applies: all services and Regions are visible, and no account color is set. You can reset account color to its default by setting the value to `"none"`. You can reset visible services and Regions to their defaults by setting their values to `null`.

**Note**  
The `visibleServices` and `visibleRegions` settings control only the appearance of services and Regions in the AWS Management Console. They do not restrict access through the AWS Command Line Interface, SDKs, or other APIs.

**Topics**
+ [Getting started with AWS User Experience Customization](getting-started-uxc.md)
+ [UXC API Reference](uxc-api-reference.md)
+ [Logging AWS User Experience Customization API calls using AWS CloudTrail](log-using-cloudtrail.md)
+ [Security in AWS User Experience Customization](security.md)