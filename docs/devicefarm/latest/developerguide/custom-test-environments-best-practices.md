# Best practices for custom test

environment execution

The following topics cover recommended best practices for using custom test execution with
Device Farm.

###### Run configuration

- Rely on Device Farm managed software and API features for run configuration

wherever possible, as opposed to applying similar configurations via shell commands in the
test spec file. This includes the configuration of the test host and the device, as this
will be more sustainable and consistent across test hosts and devices.

While Device Farm encourages you to customize your test spec file as greatly as you need in
order to run your tests, the test spec file can become difficult to maintain over time as
more customized commands are added to it. Using Device Farm managed software (through tools like `devicefarm-cli` and the default available tools in the `$PATH`), and using
managed features (like the [`deviceProxy`](../APIReference/API_ScheduleRunConfiguration.md#devicefarm-Type-ScheduleRunConfiguration-deviceProxy "../APIReference/API_ScheduleRunConfiguration.md#devicefarm-Type-ScheduleRunConfiguration-deviceProxy") request parameter) to simplify the test spec file
by shifting the responsibility of maintenance to Device Farm itself.

###### Test spec and test package code

- Do not use absolute paths or rely on specific minor versions
  in your test spec file or test package code. Device Farm applies routine updates to the selected
  test host and its included software versions. Using specific or absolute paths (such as `/usr/local/bin/python` instead of `python`) or requiring
  specific minor versions (such as Node.js `20.3.1` instead of just `20`) may lead to your tests failing to locate the required executable / file.

As part of the custom test execution, Device Farm sets up various environment variables and
the `$PATH` variable to ensure tests to have a consistent experience within our
dynamic environments. See [Environment variables for custom test
environments](custom-test-environment-variables.md "custom-test-environment-variables.md") and [Supported software within custom test
environments](custom-test-environments-hosts-software.md "custom-test-environments-hosts-software.md") for more information.

- Save generated or copied files within the temp directory during
  the test run. Today, we make sure that the temp directory (`/tmp`)
  will be accessible to the user during the test execution (besides managed directories, such
  as the `$DEVICEFARM_LOG_DIR`). Other directories that the user has access to may
  change over time due to the needs of the service or the operating system in use.
- Save your test execution logs to `$DEVICEFARM_LOG_DIR`.
  This is the default artifact directory provided for your execution to add execution logs /
  artifacts into. The [example test
  specs](custom-test-environment-test-spec.md#custom-test-environment-test-spec-example "custom-test-environment-test-spec.md#custom-test-environment-test-spec-example") we provide each uses this directory for artifacts by default.
- Ensure your commands return a non-zero code on failure during
  the `test` phase of your test spec. We determine if your execution failed by
  checking for a non-zero exit code of each shell command invoked during the `test`
  phase. You should ensure your logic or test framework will return a non-zero exit code for
  all desired scenarios, which may require additional configuration.

For example, certain test frameworks (such as JUnit5) do not consider zero tests run to
be a failure, which will cause your tests to be detected to have run successfully even if
nothing was executed. Using JUnit5 as the example, you would need to specify the command
line option `--fail-if-no-tests` to ensure this scenario exits with a non-zero
exit code.

- Review the compatibility of software with the device OS
  version and test host version you will be using for the test run. As an example, there are
  certain features in testing software frameworks (ie: Appium) that may not work as intended
  on all OS versions of the device being tested.

###### Security

- Avoid storing or logging sensitive variables (like AWS keys) in your test spec file.

Test spec files, the test spec generated scripts, and the test spec script's logs are all
provided as downloadable artifacts at the end of the test execution. This may lead to the
unintended exposure of secrets for other users in your account with read access to your test
run.
