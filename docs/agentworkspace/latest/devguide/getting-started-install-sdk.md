

# Install the Connect Customer SDK for developing applications for Connect Customer agent workspace
<a name="getting-started-install-sdk"></a>

To develop applications for the Connect Customer agent workspace you must first install the Connect Customer SDK. 

The [*Connect Customer SDK*](https://github.com/amazon-connect/AmazonConnectSDK) can be installed from npm. The Connect Customer SDK is made up of modules that you can install as separate packages. Install only the packages that you need.

The *app* package provides core application features like logging, error handling, secure messaging, and lifecycle events, and must be installed by all applications at a minimum to integrate into the workspace.

 **Install from NPM** 

Install the app package from NPM by installing ** @amazon-connect/app**.

```
% npm install --save @amazon-connect/app
```

**Note**  
 If you do not use NPM, refer to [Using Connect Customer SDK without pacakage manager](https://docs.aws.amazon.com/agentworkspace/latest/devguide/sdk-without-package-manager.html) 