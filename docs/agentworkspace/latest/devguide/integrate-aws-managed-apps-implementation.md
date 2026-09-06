

# Implementation guide
<a name="integrate-aws-managed-apps-implementation"></a>

This section describes the steps to integrate AWS-managed applications using Streams and AppManager. The [ Worklist](https://docs.aws.amazon.com/connect/latest/adminguide/worklist-app.html) AWS-managed application is used for demonstration purposes.

## Prerequisites
<a name="integrate-aws-managed-apps-prerequisites"></a>

The following prerequisites are required:
+ A working web application integrated with [Amazon Connect Streams](https://github.com/amazon-connect/amazon-connect-streams) version 2.20 or above
+ Security Profile [permissions configured](https://docs.aws.amazon.com/connect/latest/adminguide/worklist-app.html) for the Worklist AWS-managed application

## Step 1: Install required packages
<a name="integrate-aws-managed-apps-step1"></a>

Choose the appropriate package based on your integration needs:
+ **For basic application management** — Install the `@amazon-connect/app-manager` package:

  ```
  npm install @amazon-connect/app-manager
  ```
+ **For contact-scoped applications** — If you need to manage applications that are tied to specific customer contacts, install the `@amazon-connect/app-manager-agent` package instead. This package includes all the functionality of `@amazon-connect/app-manager` plus contact-scoped application support. For more information, see [Contact-scoped applications](integrate-aws-managed-apps-contact-scoped.md).

  ```
  npm install @amazon-connect/app-manager-agent
  ```

**Note**  
 If you do not use NPM, refer to [Using Amazon Connect SDK without pacakage manager](https://docs.aws.amazon.com/agentworkspace/latest/devguide/sdk-without-package-manager.html) 

## Step 2: Add the AppManager plugin in CCP initialization
<a name="integrate-aws-managed-apps-step2"></a>

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

Use the code example that corresponds to the package you installed in [Step 1: Install required packages](#integrate-aws-managed-apps-step1). The two examples differ only in the side-effect import on the second line.

 **Option A — For basic application management (using `@amazon-connect/app-manager`):** 

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

 **Option B — For contact-scoped applications (using `@amazon-connect/app-manager-agent`):** 

```
import "@amzn/amazon-connect-streams";
import "@amazon-connect/app-manager-agent";
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

**Note**  
The AppManager plugin is backward compatible and does not affect existing CCP functionality.
Replace `<connect-instance-alias>` with your Amazon Connect instance alias.

## Step 3: Embed a page for AWS-managed application
<a name="integrate-aws-managed-apps-step3"></a>

Add an iframe element to the desired location for displaying the Worklist AWS-managed application:

```
<iframe id="aws-app-iframe" height="1080px" width="1920px"/>
```

**Important**  
AppManager configures the iframe source, do not manually set the `src` attribute in iframe.

## Step 4: Launch AWS-managed application
<a name="integrate-aws-managed-apps-step4"></a>

Launch the Worklist AWS-managed application using the AppManager `launchApp` API:

```
// Launch the Worklist AWS-managed application
const appHost = await provider.appManager.launchApp("Worklist");

// Retrieve the iframe element for displaying the Worklist AWS-managed application
const awsAppIframe = document.getElementById("aws-app-iframe");

// AppManager uses the iframe to render the AWS-managed application
appHost.setIFrame(awsAppIframe);
```

## Step 5: Build and deploy
<a name="integrate-aws-managed-apps-step5"></a>

After you build and deploy your web application, verify that the Worklist application is loaded in the iframe and available for usage.