# Appium tests and AWS Device Farm

This section describes how to configure, package, and upload your Appium tests to Device Farm. Appium is an open source tool for automating native and mobile web applications.
For more information, see [Introduction to Appium](http://appium.io/docs/en/about-appium/intro/ "http://appium.io/docs/en/about-appium/intro/") on the Appium website.

For a sample app and links to working tests, see [Device Farm Sample App for Android](https://github.com/aws-samples/aws-device-farm-sample-app-for-android "https://github.com/aws-samples/aws-device-farm-sample-app-for-android") and [Device Farm Sample App for iOS](https://github.com/aws-samples/aws-device-farm-sample-app-for-ios "https://github.com/aws-samples/aws-device-farm-sample-app-for-ios") on GitHub.

For more information about testing in Device Farm, see [Test frameworks and built-in tests in AWS Device Farm](test-types.md "test-types.md").

## Version support

Support for various frameworks and programming languages depends on the language used.

Device Farm supports all Appium 1.x and 2.x server versions. For Android, you can choose any major Appium version with
`devicefarm-cli`. For example, to use Appium server version 2, add these commands to your test spec YAML
file:

```
phases:
  install:
    commands:
      # To install a newer version of Appium such as version 2:
      - export APPIUM_VERSION=2
      - devicefarm-cli use appium $APPIUM_VERSION
```

For iOS, you can choose specific Appium versions with the `avm` or `npm` commands. For
example, to use the `avm` command to set the Appium server version to 2.1.2, add these commands to your
test spec YAML file:

```
phases:
  install:
    commands:
      # To install a newer version of Appium such as version 2.1.2:
      - export APPIUM_VERSION=2.1.2
      - avm $APPIUM_VERSION
```

Using the `npm` command to use the latest version of Appium 2, add these commands to your test spec
YAML file:

```
phases:
  install:
    commands:
      - export APPIUM_VERSION=2
      - npm install -g appium@$APPIUM_VERSION
```

For more information about `devicefarm-cli` or any other CLI commands, see the [AWS CLI reference](../../../cli/latest/reference/devicefarm.md "../../../cli/latest/reference/devicefarm.md").

To use all the features of the framework, like annotations, choose a custom test environment, and use the AWS
CLI or the `Device Farm` console to upload a custom test spec.
