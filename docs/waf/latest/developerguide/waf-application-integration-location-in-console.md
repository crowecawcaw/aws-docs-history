**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Accessing the AWS WAF client application integration APIs

This section explains where to find the application integration APIs in the AWS WAF console.

The JavaScript integration APIs are generally available, and you can use them for your browsers
and other devices that execute JavaScript.

AWS WAF offers custom intelligent threat integration SDKs for Android and iOS mobile apps.

- For Android mobile and TV apps, the SDKs work for Android API version 23 (Android version 6) and later. For information about Android
  versions, see [SDK Platform release notes](https://developer.android.com/tools/releases/platforms "https://developer.android.com/tools/releases/platforms").
- For iOS mobile apps, the SDKs work for iOS version 13 and later. For information about iOS
  versions, see [iOS & iPadOS Release Notes](https://developer.apple.com/documentation/ios-ipados-release-notes "https://developer.apple.com/documentation/ios-ipados-release-notes").
- For Apple TV apps, the SDKs work for tvOS version 14 or later. For information about tvOS
  versions, see [tvOS Release Notes](https://developer.apple.com/documentation/tvos-release-notes "https://developer.apple.com/documentation/tvos-release-notes").

###### To access the integration APIs through the console

1.  Sign in to the AWS Management Console and open the AWS WAF console at
    [https://console.aws.amazon.com/wafv2/homev2](https://console.aws.amazon.com/wafv2/homev2 "https://console.aws.amazon.com/wafv2/homev2").
2.  Choose **Application integration** in the navigation pane, and then
    choose the tab you're interested in.
    - **Intelligent threat integration** is available for JavaScript and mobile
      applications.

    The tab contains the following:

        + A list of the protection packs (web ACLs) that are enabled for intelligent threat application integration. The list
         includes each protection pack (web ACL) that uses the `AWSManagedRulesACFPRuleSet` managed rule group, the `AWSManagedRulesATPRuleSet` managed rule group, or
         the targeted protection level of the `AWSManagedRulesBotControlRuleSet` managed rule group.
         When you implement the intelligent threat APIs, you use the integration
         URL for the protection pack (web ACL) that you want to integrate with.
        + The APIs that you have access to. The JavaScript APIs are always available.
         For access to the mobile SDKs, contact support at [Contact AWS](https://aws.amazon.com/contact-us "https://aws.amazon.com/contact-us").

    - **CAPTCHA integration** is available for JavaScript applications.

    The tab contains the following:

        + The integration URL for use in your integration.
        + The API keys that you've created for your client application domains. Your use of
         the CAPTCHA API requires an encrypted API key that gives clients the right
         to access AWS WAF CAPTCHA from their domains. For each client that you
         integrate with, use an API key that contains the client's domain. For more
         information these requirements and about managing these keys, see [Managing API keys for the JS CAPTCHA API](waf-js-captcha-api-key.md "waf-js-captcha-api-key.md").
