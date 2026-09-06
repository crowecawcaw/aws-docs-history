

# Using the SDK in a 3P app
<a name="sdk-without-package-manager-3p-app"></a>

This section explains how to use the prebuilt bundle in a third-party application that runs within the Connect Customer agent workspace.

## Prerequisites
<a name="sdk-without-package-manager-3p-prerequisites"></a>

The following prerequisites are required:
+ Your application is registered as a third-party app in Amazon Connect
+ The `connect-sdk-app.bundle.js` file from the building section

## HTML setup
<a name="sdk-without-package-manager-3p-html"></a>

```
<!DOCTYPE html>
<html>
  <head>
    <title>Connect Third-Party App</title>
  </head>
  <body>
    <div id="app-container"></div>

    <!-- Load the SDK bundle -->
    <script src="/assets/vendor/connect-sdk-app.bundle.js"></script>

    <!-- Your application code -->
    <script src="/app.js"></script>
  </body>
</html>
```

## JavaScript implementation
<a name="sdk-without-package-manager-3p-js"></a>

In your `app.js` file:

```
// Initialize the third-party app - this must be called first
var initResult = AmazonConnectSDK.AmazonConnectApp.init({
  // Optional lifecycle callbacks
  onCreate: function (event) {
    console.log("App created");
  },
  onDestroy: function (event) {
    console.log("App destroyed");
  },
});

// Get the provider from the init result
var provider = initResult.provider;

// Create the SDK clients using the provider
var contactClient = new AmazonConnectSDK.ContactClient(provider);
var emailClient = new AmazonConnectSDK.EmailClient(provider);

// Example: Subscribe to contact lifecycle events
contactClient.onIncoming(function (event) {
  console.log("Incoming contact:", event.contactId);
});

contactClient.onConnected(function (event) {
  console.log("Contact connected:", event.contactId);
});

contactClient.onCleared(function (event) {
  console.log("Contact cleared:", event.contactId);
});
```

## Key points for third-party apps
<a name="sdk-without-package-manager-3p-key-points"></a>

1. Call `AmazonConnectSDK.AmazonConnectApp.init()` before using any SDK functionality

1. The `init()` function returns an object containing the ` provider`

1. Instantiate SDK clients with `new AmazonConnectSDK.ContactClient(provider)`

1. Lifecycle callbacks (`onCreate`, `onDestroy`) are optional but useful for managing app state