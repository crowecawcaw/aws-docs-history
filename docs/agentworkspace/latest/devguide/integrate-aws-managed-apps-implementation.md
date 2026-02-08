# Implementation guide

This section describes the steps to integrate AWS-managed applications using Streams
and AppManager. The [Worklist](../../../connect/latest/adminguide/worklist-app.md "../../../connect/latest/adminguide/worklist-app.md") AWS-managed application is used for demonstration purposes.

## Prerequisites

The following prerequisites are required:

- A working web application integrated with [Amazon
  Connect Streams](https://github.com/amazon-connect/amazon-connect-streams "https://github.com/amazon-connect/amazon-connect-streams") version 2.20 or above
- Security Profile [permissions
  configured](../../../connect/latest/adminguide/worklist-app.md "../../../connect/latest/adminguide/worklist-app.md") for the Worklist AWS-managed application

## Step 1: Install required packages

Install the Amazon Connect AppManager package from npm into your web application:

```

npm install @amazon-connect/app-manager
```

###### Note

If you do not use NPM, refer to [Using
Amazon Connect SDK without pacakage manager](sdk-without-package-manager.md "sdk-without-package-manager.md")

## Step 2: Add the AppManager plugin

in CCP initialization

Update the existing CCP initialization code to include the AppManager plugin.

**Before:**

```

import "@amzn/amazon-connect-streams";

const containerElement = document.getElementById("ccp-container");
connect.core.initCCP(containerElement, {
    ccpUrl: "https://<connect-instance-alias>.my.connect.aws/ccp-v2/",
    // Other initialization parameters
});
```

**After:**

```

import "@amzn/amazon-connect-streams";
import "@amazon-connect/app-manager";
import { AppManagerPlugin } from "@amazon-connect/app-manager";

const containerElement = document.getElementById("ccp-container");
connect.core.initCCP(containerElement, {
    ccpUrl: "https://<connect-instance-alias>.my.connect.aws/ccp-v2/",
    // Other initialization parameters

    plugins: [AppManagerPlugin], // Enables AppManager
});

// Retrieve the provider for accessing AppManager
const provider = connect.core.getSDKClientConfig().provider;
```

###### Note

- The AppManager plugin is backward compatible and does not affect
  existing CCP functionality.
- Replace `<connect-instance-alias>` with your Amazon
  Connect instance alias.

## Step 3: Embed a page for

AWS-managed application

Add an iframe element to the desired location for displaying the Worklist
AWS-managed application:

```

<iframe id="aws-app-iframe" height="1080px" width="1920px"/>
```

###### Important

AppManager configures the iframe source, do not manually set the `src`
attribute in iframe.

## Step 4: Launch AWS-managed

application

Launch the Worklist AWS-managed application using the AppManager `launchApp`
API:

```

// Launch the Worklist AWS-managed application
const appHost = await provider.appManager.launchApp("Worklist");

// Retrieve the iframe element for displaying the Worklist AWS-managed application
const awsAppIframe = document.getElementById("aws-app-iframe");

// AppManager uses the iframe to render the AWS-managed application
appHost.setIFrame(awsAppIframe);
```

## Step 5: Build and deploy

After you build and deploy your web application, verify that the Worklist
application is loaded in the iframe and available for usage.
