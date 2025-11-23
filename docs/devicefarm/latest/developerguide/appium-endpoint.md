# Appium testing in AWS Device Farm

During a remote access session, you can run Appium tests from your local environment,
targeting the session's device using a managed Appium endpoint. With an Appium endpoint, you're
able to develop, test, and execute Appium code with fast feedback and rapid iteration.
This **client-side** approach to testing offers the flexibility to
connect to a Device Farm device from any Appium client environment of your choice.

To complement client-side testing, Device Farm also supports running tests on
infrastructure managed by the service, called **server-side** execution.
In this approach, you can upload your app and tests to the service,
then executes the tests in parallel on multiple devices using service-managed
[test hosts](custom-test-environments-hosts.md "custom-test-environments-hosts.md").
This approach scales well for testing on many
devices independently, as well as testing from the context of a CI/CD pipeline.

To learn more about server-side execution, please see [Test frameworks and built-in tests in AWS Device Farm](test-types.md "test-types.md").

###### Topics

- [What is an Appium endpoint?](#appium-endpoint-what-is "#appium-endpoint-what-is")
- [Getting started with Appium testing](appium-endpoint-getting-started.md "appium-endpoint-getting-started.md")
- [Interacting with the device using Appium](appium-endpoint-interaction.md "appium-endpoint-interaction.md")
- [Reviewing your Appium server logs](appium-endpoint-server-logs.md "appium-endpoint-server-logs.md")
- [Supported Appium capabilities and commands](appium-endpoint-supported-caps-and-commands.md "appium-endpoint-supported-caps-and-commands.md")

## What is an Appium endpoint?

[Appium](https://appium.io/ "https://appium.io/") is a popular open-source software testing framework for testing native, hybrid, and mobile web applications on different devices, including mobile phones and tablets, for both iOS and Android. It allows developers and QA (Quality Assurance) engineers to write scripts that can remotely control a device, simulate user interactions, and verify that the application under test is behaving as expected. Appium interacts with apps from the perspective of an end-user, enabling testers to develop tests that simulate how real users will use the app for their tests.

Appium is built on the client-server model, where a local client requests a (local or remote) Appium server to command a device on their behalf. The Appium server manages a driver for communicating with the device, such as the [UIAutomator2 driver](https://github.com/appium/appium-uiautomator2-driver/ "https://github.com/appium/appium-uiautomator2-driver/") for Android or the [XCUITest driver](https://appium.github.io/appium-xcuitest-driver/9.10/ "https://appium.github.io/appium-xcuitest-driver/9.10/") for iOS. All commands follow the [W3C WebDriver](https://www.w3.org/TR/webdriver2/ "https://www.w3.org/TR/webdriver2/") standards for how to control a device.

Device Farm's Appium endpoint exposes an Appium server URL for the device in your remote access session. The Appium endpoint URL will be specific to that device in that session, and remain valid for the duration of the session, allowing you to iterate on the same device without additional setup time. For more information about Remote Access, please see [Remote access in AWS Device Farm](remote-access.md "remote-access.md").
