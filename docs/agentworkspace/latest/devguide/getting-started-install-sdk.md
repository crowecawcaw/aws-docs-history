

# Install the Amazon Connect SDK for developing applications for Connect Customer agent workspace
<a name="getting-started-install-sdk"></a>

To develop applications for the Connect Customer agent workspace you must first install the Connect Customer SDK. 

The [*Connect Customer Amazon Connect SDK*](https://github.com/amazon-connect/AmazonConnectSDK) can be installed from NPM. The Aamzon Connect SDK is made up of a set of modules that can be installed as separate packages, meaning that you should only pull in the packages that you need.

The *app* package provides core application features like logging, error handling, secure messaging, and lifecycle events, and must be installed by all applications at a minimum to integrate into the workspace.

 **Install from NPM** 

Install the app package from NPM by installing ** @amazon-connect/app**.

```
% npm install --save @amazon-connect/app
```

**Note**  
 If you do not use NPM, refer to [Using Amazon Connect SDK without pacakage manager](https://docs.aws.amazon.com/agentworkspace/latest/devguide/sdk-without-package-manager.html) 