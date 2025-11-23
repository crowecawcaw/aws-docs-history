# Custom test environments in AWS Device Farm

AWS Device Farm enables configuring a custom environment for automated testing (custom mode), which is the
recommended approach for all Device Farm users. To learn more about environments in Device Farm, see [Test
environments](test-environments.md "test-environments.md").

Benefits of the Custom Mode as opposed to the Standard Mode include:

- **Faster end-to-end test execution**: The test package isn't parsed to
  detect every test in the suite, avoiding preprocessing/postprocessing overhead.
- **Live log and video streaming**: Your client-side test logs and video
  are live streamed when using Custom Mode. This feature isn't available in the standard mode.
- **Captures all artifacts**: On the host and device, Custom Mode allows
  you to capture all test artifacts. This may not be possible in the standard mode.
- **More consistent and replicable local environment**: When in Standard
  Mode, artifacts will be provided for each individual test separately, which can be beneficial under
  certain circumstances. However, your local test environment may deviate from the original configuration
  as Device Farm handles each executed test differently.

In contrast, Custom Mode enables you to make your Device Farm test execution environment consistently in
line with with your local test environment.

Custom environments are configured using a YAML-formatted test specification (test spec) file. Device Farm
provides a default test spec file for each supported test type that can be used as is or customized;
customizations like test filters or config files can be added to the test spec. Edited test specs can be saved
for future test runs.

For more information, see [Uploading a Custom Test Spec Using the AWS CLI](how-to-create-test-run.md#how-to-create-test-run-cli-step5 "how-to-create-test-run.md#how-to-create-test-run-cli-step5")
and [Creating a test run in Device Farm](how-to-create-test-run.md "how-to-create-test-run.md").

###### Topics

- [Test spec reference and syntax](custom-test-environment-test-spec.md "custom-test-environment-test-spec.md")
- [Hosts for custom test environments](custom-test-environments-hosts.md "custom-test-environments-hosts.md")
- [Access AWS resources using an IAM Execution Role](custom-test-environments-iam-roles.md "custom-test-environments-iam-roles.md")
- [Environment variables for custom test
  environments](custom-test-environment-variables.md "custom-test-environment-variables.md")
- [Best practices for custom test
  environment execution](custom-test-environments-best-practices.md "custom-test-environments-best-practices.md")
- [Migrating tests from a standard to custom
  test environment](custom-test-environment-migration.md "custom-test-environment-migration.md")
- [Extending custom test environments in Device Farm](custom-test-environments-extending.md "custom-test-environments-extending.md")
