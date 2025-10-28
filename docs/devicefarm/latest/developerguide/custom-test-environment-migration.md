# Migrating tests from a standard to custom

test environment

You can switch from a standard test execution mode to a custom execution mode in AWS Device Farm. Migration
primarily involves two different forms of execution:

1. **Standard mode**: This test execution mode is primarily built to
   provide customers with granular reporting and a fully-managed environment.
2. **Custom mode**: This test execution mode is built for different use
   cases that require faster test runs, the ability to lift and shift and achieve parity with their
   local environment, and live video streaming.
   For more information about standard and custom modes in Device Farm, see [Test environments in AWS Device Farm](test-environments.md "test-environments.md") and [Custom test environments in AWS Device Farm](custom-test-environments.md "custom-test-environments.md").

## Considerations when migrating

This section lists some of the prominent use cases to consider when migrating to the custom
mode:

1. **Speed**: In the standard mode of execution, Device Farm parses the
   metadata of the tests that you have packaged and uploaded using the packaging instructions for
   your particular framework. Parsing detects the number of tests in your package. Thereafter,
   Device Farm runs each test separately and presents the logs, videos, and other result artifacts
   individually for each test. However, this steadily adds to the total end-to-end test execution
   time as there are the pre- and post-processing of tests and result artifacts on the service end.

By contrast, the custom mode of execution doesn't parse your test package; this means no
pre-processing and minimal post-processing for tests or result artifacts. This results in total
end-to-end execution times close to your local setup. The tests are executed in the same format
as they would be if they ran on your local machine(s). The results of the tests are the same as
what you get locally and are available for download at the end of the job execution. 2. **Customization or Flexibility**: The standard mode of execution
parses your test package to detect the number of tests and then runs each test separately. Note
that there is no guarantee that the tests will run in the order you specified. As a result,
tests requiring a particular sequence of execution may not work as expected. In addition, there
is no way to customize the host machine environment or pass config files that may be needed to
run your tests a certain way.

By contrast, custom mode lets you configure the host machine environment including the ability
to install additional software, pass filters to your tests, pass config files, and control the
test execution setup. It achieves this via a yaml file (also called the testspec file) that you
can modify by adding shell commands to it. This yaml file gets converted to a shell script which
gets executed on the test host machine. You can save multiple yaml files and choose one
dynamically as per your requirements when you schedule a run. 3. **Live video and logging**: Both standard and custom modes of
execution provide you with videos and logs for your tests. However, in standard mode, you get
the video and predefined logs of your tests only after your tests are completed.

By contrast, custom mode gives you a live stream of the video and client-side logs of your
tests. In addition, you are able to download the video and other artifacts at the end of the
test(s).

###### Tip

If your use case involves at least one of the factors above, we strongly recommend switching to
the custom mode of execution.

## Migration steps

To migrate from standard to custom mode, do the following:

1. Sign in to the AWS Management Console and open the Device Farm console at
   [https://console.aws.amazon.com/devicefarm/](https://console.aws.amazon.com/devicefarm/ "https://console.aws.amazon.com/devicefarm/").
2. Choose your project and then start a new automation run.
3. Upload your app (or select `web app`), choose your test framework type, upload your
   test package, then under the `Choose your execution environment` parameter, choose
   the option to `Run your test in a custom environment`.
4. By default, Device Farm's example test spec file will appear for you to view and edit. This example
   file can be used as a starting place to try your tests out in [custom environment mode](custom-test-environments.md "custom-test-environments.md"). Then, once you've verified that your tests are working
   properly from the console, you can then alter any of your API, CLI, and pipeline integrations
   with Device Farm to use this test spec file as a parameter when scheduling test runs. For information
   on how to add a test spec file as a parameter for your runs, see the `testSpecArn`
   parameter section for the `ScheduleRun` API in our [API
   guide](../APIReference/API_ScheduleRun.md "../APIReference/API_ScheduleRun.md").

## Appium framework

In a custom test environnment, Device Farm does not insert or override any Appium capabilities in your
Appium framework tests. You must specify your test's Appium capabilities in either the test spec YAML
file or your test code.

## Android instrumentation

You do not need to make changes to move your Android instrumentation tests to a custom test
environment.

## iOS XCUITest

You do not need to make changes to move your iOS XCUITest tests to a custom test environment.
