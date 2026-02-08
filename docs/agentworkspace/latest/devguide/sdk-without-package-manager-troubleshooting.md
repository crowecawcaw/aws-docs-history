# Troubleshooting

This section describes common issues and resolutions when using the SDK without a
package manager.

## Bundle is too

large

If the bundle size is a concern, ensure you only import the packages you need.
Each additional package increases bundle size.

## "AmazonConnectSDK

is not defined" error

Verify that the bundle script tag appears before your application script in the
HTML, and that the path to the bundle file is correct.

## Provider is

undefined

**For StreamsJS:** Ensure you are accessing the
provider after `connect.core.onInitialized()` fires.

**For third-party apps:** Ensure you call `AmazonConnectSDK.AmazonConnectApp.init()` and capture its return value.

## SDK methods

not working

Verify you passed the provider when creating the clients. The provider
establishes the communication channel between your code and Amazon Connect.
