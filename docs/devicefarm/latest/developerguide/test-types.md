

# Test frameworks and built-in tests in AWS Device Farm
<a name="test-types"></a>

This section describes Device Farm support for testing frameworks and built-in test types.

Device Farm runs automated tests by having you upload your app and tests to a secure Amazon S3 bucket managed by the service. Once uploaded, it spins up the underlying infrastructure, including service-managed [test hosts](custom-test-environments-hosts.md), and executes the tests in parallel on multiple devices. The test results are stored in a service managed S3 bucket. This architecture is called **service-side execution**, and is a fast and efficient way to run tests on hosts that are physically close to the device, without needing to manage the test host infrastructure yourself. This approach scales well for testing on many devices independently, as well as testing from the context of a CI/CD pipeline.

For more information about how Device Farm runs tests, see [Test environments in AWS Device Farm](test-environments.md).

**Note**  
For Appium testers, you may prefer to run your Appium tests from your local environment. With a [remote access session](remote-access.md), you can run **client-side** Appium tests. For more information, please see [client-side Appium testing](appium-endpoint.md).

## Testing frameworks
<a name="test-types-framework"></a>

Device Farm supports these mobile automation testing frameworks:

### Android application testing frameworks
<a name="test-types-framework-android-list"></a>
+ [Automatic Appium tests](test-types-appium.md)
+ [Instrumentation](test-types-android-instrumentation.md)

### iOS application testing frameworks
<a name="test-types-framework-ios-list"></a>
+ [Automatic Appium tests](test-types-appium.md)
+ [XCTest](test-types-ios-xctest.md)
+ [XCTest UI](test-types-ios-xctest-ui.md)

### Web application testing frameworks
<a name="test-types-framework-web-app-list"></a>

Web applications are supported using Appium. For more information on bringing your tests to Appium, see [Automatically run Appium tests in Device Farm](test-types-appium.md).

### Frameworks in a custom test environment
<a name="test-types-framework-custom-support"></a>

Device Farm does not provide support for customizing the test environment for the XCTest framework. For more information, see [Custom test environments in AWS Device Farm](custom-test-environments.md).

### Appium version support
<a name="test-types-framework-appium"></a>

For tests running in a custom environment, Device Farm supports Appium version 1. For more information, see [Test environments in AWS Device Farm](test-environments.md).

## Built-in test types
<a name="test-types-built-in"></a>

With built-in tests, you can test your application on multiple devices without having to write and maintain test automation scripts. Device Farm offers one built-in test type:
+ [Built-in: fuzz (Android and iOS)](test-types-built-in-fuzz.md)