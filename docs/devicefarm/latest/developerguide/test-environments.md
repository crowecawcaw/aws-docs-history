# Test environments in AWS Device Farm

AWS Device Farm provides both custom and standard test environments for running your automated
tests. You can choose a custom test environment for complete control over your automated tests.
Or, you can choose the Device Farm default standard test environment, which offers granular reporting
of each test in your automated test suite.

###### Topics

- [Standard test environment](#test-environments-standard "#test-environments-standard")
- [Custom test environment](#custom-test-environment "#custom-test-environment")

## Standard test environment

When you run a test in the standard environment, Device Farm provides detailed logs and
reporting for every case in your test suite. You can view performance data, videos,
screenshots, and logs for each test to pinpoint and fix issues in your app.

###### Note

Because Device Farm provides granular reporting in the standard environment, test execution
times can be longer than when you run your tests locally. If you want faster execution
times, run your tests in a custom test environment.

## Custom test environment

When you customize the test environment, you can specify the commands Device Farm should run to
execute your tests. This ensures that tests on Device Farm run in a way that is similar to tests run
on your local machine. Running your tests in this mode also enables live log and video
streaming of your tests. When you run tests in a customized test environment, you do not get
granular reports for each test case. For more information, see [Custom test environments in AWS Device Farm](custom-test-environments.md "custom-test-environments.md").

You have the option to use a custom test environment when you use the Device Farm console,
AWS CLI, or Device Farm API to create a test run.

For more information, see [Uploading a Custom Test Spec Using the AWS CLI](how-to-create-test-run.md#how-to-create-test-run-cli-step5 "how-to-create-test-run.md#how-to-create-test-run-cli-step5")
and [Creating a test run in Device Farm](how-to-create-test-run.md "how-to-create-test-run.md").
