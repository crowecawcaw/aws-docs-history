# Migrating your custom test environments to the new iOS test

hosts

To migrate existing tests from the legacy host to the new macOS test host, you will need to
develop new test spec files based on your pre-existing ones.

The recommended approach is to start with the example test spec file for your desired test
types, then migrate relevant commands from your old test spec file to the new one. This lets you
leverage new features and optimizations of the example test spec for the new host while reusing
snippets your existing code.

###### Topics

- [Tutorial: Migrating iOS test spec files
  with the console](#ios-host-migration-console-tutorial "#ios-host-migration-console-tutorial")
- [Differences between the new and legacy test
  hosts](#ios-host-migration-differences "#ios-host-migration-differences")

## Tutorial: Migrating iOS test spec files

with the console

In this example, the Device Farm console will be used to onboard an existing iOS device test spec to
use the new test host.

###

Step 1: Creating a new test spec files with the console

1. Sign in to the [AWS Device Farm console](https://console.aws.amazon.com/devicefarm "https://console.aws.amazon.com/devicefarm").
2. Navigate to the Device Farm project containing your automation tests.
3. Download a copy of the existing test spec your wish to onboard with.
   1. Click the "Project Settings" option and navigate to the **Uploads**
      tab.
   2. Navigate to the test spec file that you wish to onboard with.
   3. Click the **Download** button to make a local copy of this
      file.

4. Navigate back to the Project page and click **Create run**.
5. Fill in the options on the wizard as if you were to start a new run, but stop at the **Select
   test spec** option.
6. Using the iOS test spec selected by default, click the **Create a test spec**
   button.
7. Modify the test specification that was selected by _default_ in
   the text editor.
   1. If not already present, modify the test spec file to select the new host using:

   ```
   ios_test_host: macos_sequoia
   ```

   2. From the copy of your test spec downloaded in a prior step, review each `phase`.
   3. Copy commands from the old test spec's phases into each respective phase in the
      new test spec, ignoring commands related to installing or selecting Java, Python,
      Node.js, Ruby, Appium, or Xcode.

8. Enter a new file name in the **Save as** text box.
9. Click the **Save as new** button to save your changes.

For an example of a test spec file you can use as a reference, see the example provided
in [Test spec examples](custom-test-environment-test-spec.md#custom-test-environment-test-spec-example "custom-test-environment-test-spec.md#custom-test-environment-test-spec-example").

### Step 2: Selecting software

pre-installed software

In the new test host, pre-installed software versions are selected using a new
standardized version management tool called `devicefarm-cli`. This tooling is now
the recommended approach for using the various software we provide on the test hosts.

As an example, you would add the following line to use a different JDK 17 your test
environment:

```
- devicefarm-cli use java 17
```

For more information on the software supported available, please review: [Supported software within custom test
environments](custom-test-environments-hosts-software.md "custom-test-environments-hosts-software.md").

###

Step 3: Using Appium and its dependencies via the software selection tooling

The new test host only supports Appium 2.x and above. Please explicitly select the
Appium version using the `devicefarm-cli`, while removing legacy tooling such as `avm`. For example:

```
# This line using 'avm' should be removed
# - avm 2.3.1

# And the following lines should be added
- devicefarm-cli use appium 2 # Selects the version
- appium --version            # Prints the version
```

The Appium version selected with `devicefarm-cli` comes preinstalled with a
compatible version of the XCUITest driver for iOS.

Additionally, you will need to update your test spec to use `DEVICEFARM_APPIUM_WDA_DERIVED_DATA_PATH_V9` instead of `DEVICEFARM_WDA_DERIVED_DATA_PATH`. The new environment variable points to a pre-built
version of WebDriverAgent 9.x, which is the latest supported version for Appium 2 tests.

For more information, review [Selecting a WebDriverAgent version for iOS tests](test-types-appium.md#test-types-appium-select-wda "test-types-appium.md#test-types-appium-select-wda") and [Environment variables for Appium
tests](custom-test-environment-variables.md#custom-test-environment-variables-appium "custom-test-environment-variables.md#custom-test-environment-variables-appium").

## Differences between the new and legacy test

hosts

When you're editing your test spec file to use the new iOS test host and transitioning your
tests from the legacy test host, be aware of these key environment differences:

- Xcode versions:
  In the legacy test host environment, the
  Xcode version available was based on the iOS version of the device used for testing. For
  example, tests on iOS 18 devices used Xcode 16 in the legacy host, whereas tests on iOS 17
  used Xcode 15. In the new host environment, all devices can access the same versions of
  Xcode, allowing a consistent environment for tests on devices with different versions. For
  a list of currently available Xcode versions, see [Supported software](custom-test-environments-hosts-software.md "custom-test-environments-hosts-software.md").
- Selecting software versions:
  In many instances, the
  default software versions have changed, so if you weren't explicitly selecting your
  software version in the legacy test host before, you may want to specify it now in the new
  test host using [devicefarm-cli](custom-test-environments-hosts-software-cli.md "custom-test-environments-hosts-software-cli.md"). In the vast majority of use cases, we
  recommend that customers explicitly select the versions of software they use. By selecting
  a software version with `devicefarm-cli` you'll have a predictable and
  consistent experience with it and receive ample amounts of warnings if Device Farm plans
  to remove that version from the test host.

Moreover, software selection tools like `nvm`, `pyenv`, `avm`, and `rvm` have been removed in favor of the new `devicefarm-cli` software selection system.

- Available software versions:
  Many versions of previously
  pre-installed software have been removed, and many new versions have been added. So,
  ensure that when using the `devicefarm-cli` to select your software versions,
  you select versions which are in the [supported version list](custom-test-environments-hosts-software.md "custom-test-environments-hosts-software.md").
- The `libimobiledevice` suite of tools have been removed
  in favor of newer / first party tooling to track current iOS device testing and industry
  standards. For iOS 17 and above, you can migrate most commands to use similar Xcode
  tooling, called `devicectl`. For information on `devicectl`, you
  can run `xcrun devicectl help` from a machine with Xcode installed.
- File paths that are hard-coded
  in your legacy host test
  spec file as absolute paths will most likely not work as expected in the new test host,
  and they're generally not recommended for test spec file use. We recommend that you use
  relative paths and environment variables for all test spec file code. For more
  information, review the topic on [Best practices for custom test
  environment execution](custom-test-environments-best-practices.md "custom-test-environments-best-practices.md").
- Operating system version and architecture:
  The legacy
  test hosts were using a variety of macOS versions and CPU architectures based on the
  assigned device. As a result, users may notice some differences in the available system
  libraries available in the environment. For more information on the previous host OS
  version, review [Legacy iOS test host](custom-test-environments-hosts-ios.md#legacy-ios-host "custom-test-environments-hosts-ios.md#legacy-ios-host").
- For Appium users, the way to select the WebDriverAgent has
  changed to a use environment variable prefix `DEVICEFARM_APPIUM_WDA_DERIVED_DATA_PATH_V` instead of the old `DEVICEFARM_WDA_DERIVED_DATA_PATH_V` prefix. For more information on the updated
  variable, review [Environment variables for Appium
  tests](custom-test-environment-variables.md#custom-test-environment-variables-appium "custom-test-environment-variables.md#custom-test-environment-variables-appium").
- For Appium Java users, the new test host does not contain
  any pre-installed JAR files in its class path, whereas the previous host contained one for
  the TestNG framework (via an environment variable `$DEVICEFARM_TESTNG_JAR`). We
  recommend that customers package the necessary JAR files for their test frameworks inside
  their test package and remove instances of the `$DEVICEFARM_TESTNG_JAR`
  variable from their test spec files.

We recommend reaching out to the service team through a support case if you have any feedback
or questions about the differences between the test hosts from a software perspective.
