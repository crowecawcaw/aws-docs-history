**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Installing the AWS WAF mobile SDK

This section provides instructions for installing the AWS WAF mobile SDK.

For access to the mobile SDKs, contact support at [Contact AWS](https://aws.amazon.com/contact-us "https://aws.amazon.com/contact-us").

Implement the mobile SDK first in a test environment, then in production.

###### To install the AWS WAF mobile SDK

1. Sign in to the AWS Management Console and open the AWS WAF console at
   [https://console.aws.amazon.com/wafv2/homev2](https://console.aws.amazon.com/wafv2/homev2 "https://console.aws.amazon.com/wafv2/homev2").
2. In the navigation pane, choose **Application integration**.
3. In the **Intelligent threat integrations** tab, do the following:
   1. In the pane **protection packs (web ACLs) that are enabled for application integration**, locate
      the protection pack (web ACL) that you're integrating with. Copy and save the protection pack (web ACL)
      integration URL for use in your implementation. You can also obtain
      this URL through the API call `GetWebACL`.
   2. Choose the mobile device type and version, then choose **Download**. You can
      choose any version you like, but we recommend using the latest
      version. AWS WAF downloads the `zip` file for your device
      to your standard download location.

4. In your app development environment, unzip the file to a work location of your choice.
   In the top-level directory of the zip file, locate and open the
   `README`. Follow the instructions in the `README`
   file to install the AWS WAF mobile SDK for use in your mobile app code.
5. Program your app according to the guidance in the following sections.
