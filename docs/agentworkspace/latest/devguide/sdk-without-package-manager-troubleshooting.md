

# Troubleshooting
<a name="sdk-without-package-manager-troubleshooting"></a>

This section describes common issues and resolutions when using the SDK without a package manager.

## Bundle is too large
<a name="sdk-without-package-manager-troubleshooting-size"></a>

If the bundle size is a concern, ensure you only import the packages you need. Each additional package increases bundle size.

## "AmazonConnectSDK is not defined" error
<a name="sdk-without-package-manager-troubleshooting-undefined"></a>

Verify that the bundle script tag appears before your application script in the HTML, and that the path to the bundle file is correct.

## Provider is undefined
<a name="sdk-without-package-manager-troubleshooting-provider"></a>

 **For StreamsJS:** Ensure you are accessing the provider after `connect.core.onInitialized()` fires.

 **For third-party apps:** Ensure you call ` AmazonConnectSDK.AmazonConnectApp.init()` and capture its return value.

## SDK methods not working
<a name="sdk-without-package-manager-troubleshooting-methods"></a>

Verify you passed the provider when creating the clients. The provider establishes the communication channel between your code and Amazon Connect.