# Using the SDK with StreamsJS

This section explains how to use the prebuilt bundle in a solution that uses Amazon
Connect Streams (StreamsJS).

## Prerequisites

The following prerequisites are required:

- The Amazon Connect Streams library loaded on your page
- The `connect-sdk-streams.bundle.js` file from the building
  section

## HTML setup

```

<!DOCTYPE html>
<html>
  <head>
    <title>Connect StreamsJS with SDK</title>
  </head>
  <body>
    <div id="ccp-container" style="width: 400px; height: 600px;"></div>

    <!-- Load Amazon Connect Streams first -->
    <script src="https://your-domain.com/amazon-connect-streams.min.js"></script>

    <!-- Load the SDK bundle -->
    <script src="/assets/vendor/connect-sdk-streams.bundle.js"></script>

    <!-- Your application code -->
    <script src="/app.js"></script>
  </body>
</html>
```

## JavaScript implementation

In your `app.js` file:

```

// Initialize the CCP
var ccpContainer = document.getElementById("ccp-container");

connect.core.initCCP(ccpContainer, {
  ccpUrl: "https://your-instance.my.connect.aws/ccp-v2/",
  loginPopup: true,
  loginPopupAutoClose: true,
});

// Get the SDK provider from Streams after CCP initializes
connect.core.onInitialized(function () {
  // Retrieve the provider from the Streams SDK client config
  var sdkConfig = connect.core.getSDKClientConfig();
  var provider = sdkConfig.provider;

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
});
```

## Hosting Connect

first-party apps (optional)

If you want to host Connect first-party apps like Cases or Step-by-Step Guides
alongside your CCP, include the `@amazon-connect/app-manager` package in
your bundle and apply the plugin during CCP initialization:

```

connect.core.initCCP(ccpContainer, {
  ccpUrl: "https://your-instance.my.connect.aws/ccp-v2/",
  loginPopup: true,
  loginPopupAutoClose: true,
  // Apply the plugin to enable 1P app hosting
  plugins: AmazonConnectSDK.AppManagerPlugin,
});
```

## Key points for

StreamsJS integration

1. Load the Streams library before the SDK bundle
2. Retrieve the provider using `connect.core.getSDKClientConfig().provider` after CCP initializes
3. Instantiate SDK clients with `new
AmazonConnectSDK.ContactClient(provider)`
4. The `AppManagerPlugin` is only required if hosting Connect
   first-party apps
