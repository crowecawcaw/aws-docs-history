**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# AWS WAF mobile application integration

This section introduces the topic of using the AWS WAF mobile SDKs to implement AWS WAF intelligent
threat integration SDKs for Android and iOS mobile and TV apps. For TV apps, the SDKs are
compatible with major smart TV platforms, including Android TV and Apple TV.

- For Android mobile and TV apps, the SDKs work for Android API version 23 (Android version 6) and later. For information about Android
  versions, see [SDK Platform release notes](https://developer.android.com/tools/releases/platforms "https://developer.android.com/tools/releases/platforms").
- For iOS mobile apps, the SDKs work for iOS version 13 and later. For information about iOS
  versions, see [iOS & iPadOS Release Notes](https://developer.apple.com/documentation/ios-ipados-release-notes "https://developer.apple.com/documentation/ios-ipados-release-notes").
- For Apple TV apps, the SDKs work for tvOS version 14 or later. For information about tvOS
  versions, see [tvOS Release Notes](https://developer.apple.com/documentation/tvos-release-notes "https://developer.apple.com/documentation/tvos-release-notes").
  With the mobile AWS WAF SDK, you can manage token authorization,
  and include the tokens in the requests that you send to your protected resources. By
  using the SDKs, you ensure that these remote procedure calls by your client contain a
  valid token. Additionally, when this integration is in place on your application's
  pages, you can implement mitigating rules in your protection pack (web ACL), such as blocking requests
  that don't contain a valid token.

For access to the mobile SDKs, contact support at [Contact AWS](https://aws.amazon.com/contact-us "https://aws.amazon.com/contact-us").

###### Note

The AWS WAF mobile SDKs aren't available for CAPTCHA customization.

The basic approach for using the SDK is to create a token provider using a configuration
object, then to use the token provider to retrieve tokens from AWS WAF.
By default, the token provider includes the retrieved tokens in your web requests to
your protected resource.

The following is a partial listing of an SDK implementation, which shows the main
components. For more detailed examples, see [Code examples for the AWS WAF mobile SDK](waf-mobile-sdk-coding-examples.md "waf-mobile-sdk-coding-examples.md").

iOS

```
let url: URL = URL(string: "`protection pack (web ACL) integration URL`")!
	let configuration = WAFConfiguration(applicationIntegrationUrl: url, domainName: "`Domain name`")
	let tokenProvider = WAFTokenProvider(configuration)
	let token = tokenProvider.getToken()

```

Android

```
URL applicationIntegrationURL = new URL("`protection pack (web ACL) integration URL`");
	String domainName = "`Domain name`";
	WAFConfiguration configuration = WAFConfiguration.builder().applicationIntegrationURL(applicationIntegrationURL).domainName(domainName).build();
	WAFTokenProvider tokenProvider = new WAFTokenProvider(`Application context`, configuration);
	WAFToken token = tokenProvider.getToken();

```
