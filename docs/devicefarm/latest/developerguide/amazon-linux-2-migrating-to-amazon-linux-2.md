# Migrating to the Amazon Linux 2 Test Host in

AWS Device Farm

###### Warning

The legacy Android Test Host will no longer be available on October 21, 2024. Note that the process
for deprecation is split across several dates:

- On April 22, 2024, jobs from any new account will be directed to the upgraded test host.
- On September 2, 2024, all new or modified test spec files must target the upgraded test host.
- On October 21, 2024, jobs will no longer be able to run on the legacy test host.

Set your test spec files to the `amazon_linux_2` host to prevent compatibility issues.

To migrate existing tests from the legacy host to the new Amazon Linux 2 host, develop new test spec files
based on your pre-existing ones. The recommended approach is to start with the new default test spec files
for your test types. Then, migrate relevant commands from your old test spec file to the new one, saving the
old file as a backup. This lets you leverage the optimized default spec for the new host while reusing your
existing code. It ensures you get the full benefits of the new host configured optimally for your tests,
while retaining your legacy test spec for reference as you adapt commands to the new environment.

The following steps can be used to create a new Amazon Linux 2 test spec file while reusing commands from
your old test spec file:

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm "https://console.aws.amazon.com/devicefarm").
2. Navigate to the Device Farm project containing your automation tests.
3. Choose **Create run** in the project.
4. Choose a previously used app and test package for your test framework.
5. Choose **Run your test in a custom environment**.
6. Choose the test spec file you are currently using for tests on the legacy test host from the test
   spec drop-down menu.
7. Copy the contents of this file and paste them locally in a text editor for reference later
   on.
8. In the test spec drop-down menu, change your test spec selection to the most recent _default_ test spec file.
9. Choose **Edit**, and you will enter the test spec editing interface.
   You will notice that, in the first few lines of the test spec file, it has already opted in to the
   new test host:

```
android_test_host: amazon_linux_2
```

10. Review the syntax for selecting test hosts [here](amazon-linux-2-android-test-selection.md "amazon-linux-2-android-test-selection.md")
    and the key differences between the test hosts [here](amazon-linux-2-migrating-to-amazon-linux-2.md#amazon-linux-2-differences-between-hosts "amazon-linux-2-migrating-to-amazon-linux-2.md#amazon-linux-2-differences-between-hosts").
11. Selectively add and edit commands from your locally-saved test spec file from step 6 into the new
    default test spec file. Then, choose **Save as** to save the new spec
    file. You can now schedule test runs on the Amazon Linux 2 test host.

## Differences between the new and legacy test

hosts

When you're editing your test spec file to use the Amazon Linux 2 test host and transitioning your
tests from the legacy test host, be aware of these key environment differences:

- **Selecting software versions**: In many instances, the default
  software versions have changed, so if you weren’t explicitly selecting your software version in
  the Legacy test host before, you may want to specify it now in the Amazon Linux 2 test host
  using [`devicefarm-cli`](amazon-linux-2-devicefarm-cli.md "amazon-linux-2-devicefarm-cli.md"). In the vast majority of use cases, we recommend
  that customers explicitly select the versions of software they use. By selecting a software
  version with `devicefarm-cli`, you’ll have a predictable and consistent experience
  with it and receive ample amounts of warnings if Device Farm plans to remove that version from
  the test host.

Moreover, software selection tools like `nvm`, `pyenv`,
`avm`, and `rvm` have been removed in favor of the new
`devicefarm-cli` software selection system.

- **Available software versions**: Many versions of previously
  pre-installed software have been removed, and many new versions have been added. So, ensure that
  when using the `devicefarm-cli` to select your software versions, you select versions
  which are in the [supported
  version list](amazon-linux-2-supported-software.md "amazon-linux-2-supported-software.md").
- Any **file paths that are hard-coded** in your Legacy host test
  spec file as absolute paths will most likely not work as expected in the Amazon Linux 2 test
  host; they're generally not recommended for test spec file use. We recommend that you use
  relative paths and environment variables for all test spec file code. Moreover, note that most
  binaries you need for your test can be found in the PATH of the host so that they are
  immediately runnable from the spec file using just their name (such as appium).
- **Performance data** collection isn’t supported on the new test
  host at this time.
- **Operating System version**: The legacy test host was based on
  the Ubuntu operating system, whereas the new one is based on Amazon Linux 2. As a result, users
  may notice some differences in the available system libraries and system library
  versions.
- For **Appium Java** users, the new test host does not contain any
  pre-installed JAR files in its class path, whereas the previous host contained one for the
  TestNG framework (via an environment variable `$DEVICEFARM_TESTNG_JAR`). We recommend
  that customers package the necessary JAR files for their test frameworks inside their test
  package and remove instances of the `$DEVICEFARM_TESTNG_JAR` variable from their test
  spec files. For more information, see [Working with Appium and AWS
  Device Farm](test-types-appium.md "test-types-appium.md").
- For **Appium** users, the
  `$DEVICEFARM_CHROMEDRIVER_EXECUTABLE` environment variable has been removed in
  favor of a new approach to enabling customers to access Chromedriver for Android. See our [Default
  test spec file](amazon-linux-2-test-spec-file-example.md "amazon-linux-2-test-spec-file-example.md") for an example, which uses a new environment variable
  `$DEVICEFARM_CHROMEDRIVER_EXECUTABLE_DIR`.

###### Note

We strongly recommend keeping the existing Appium server command from the default test spec file
as is.

We recommend reaching out to the service team through a support case if you have any feedback or
questions about the differences between the test hosts from a software perspective.
