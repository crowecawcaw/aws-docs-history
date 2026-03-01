# Install the Amazon Connect SDK for developing applications for Amazon Connect Agent Workspace

To develop applications for the Amazon Connect agent workspace you must first install
the
Amazon Connect SDK.

The [_Amazon Connect Amazon Connect SDK_](https://github.com/amazon-connect/AmazonConnectSDK "https://github.com/amazon-connect/AmazonConnectSDK") can be
installed from NPM. The Aamzon Connect SDK is made up of a set of modules that can
be installed as separate packages, meaning that you should only pull in the packages
that you need.

The _app_ package provides core application features like
logging, error handling, secure messaging, and lifecycle events, and must be
installed by all applications at a minimum to integrate into the workspace.

**Install from NPM**

Install the app package from NPM by installing **@amazon-connect/app**.

```

% npm install --save @amazon-connect/app

```

###### Note

If you do not use NPM, refer to [Using
Amazon Connect SDK without pacakage manager](sdk-without-package-manager.md "sdk-without-package-manager.md")
