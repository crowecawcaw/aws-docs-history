# Test spec reference and syntax

The test spec (test specification) is a file that you use to define custom test environments
in Device Farm.

## Test spec workflow

The Device Farm test spec executes phases and their commands in a pre-determined order, letting
you customize the way your environment is prepared and executed. When each phase is
executed, its commands are run in the order listed within the test spec file. Phases are
executed in the following sequence

1. `install` - This is where actions like downloading, installing, and setting
   up tooling should be defined.
2. `pre_test` - This is where pre-test actions like starting background
   processes should be defined.
3. `test` - This is where the command that invokes your test should be
   defined.
4. `post_test` - This is where any final tasks that need to be run after your
   test concludes should be defined, such as test report generation and artifact file
   aggregation.

## Test spec syntax

The following is the YAML schema for a test spec file

```
version: 0.1

android_test_host: "string"
ios_test_host: "string"

phases:
  install:
    commands:
      - "string"
      - "string"
  pre_test:
    commands:
      - "string"
      - "string"
  test:
    commands:
      - "string"
      - "string"
  post_test:
    commands:
      - "string"
      - "string"

artifacts:
    - "string"
    - "string"
```

**`version`**

_(Required, number)_

Reflects the Device Farm supported test spec version. The current version number is `0.1`.

**`android_test_host`**

_(Optional, string)_

The test host that will be selected for test runs performed on Android devices.
This field is required for test runs on Android devices. For more information, see [Available test hosts for custom
test environments](custom-test-environments-hosts.md#custom-test-environments-hosts-available "custom-test-environments-hosts.md#custom-test-environments-hosts-available").

**`ios_test_host`**

_(Optional, string)_

The test host that will be selected for test runs performed on iOS devices. This
field is required for test runs on iOS devices with a major version greater than 26. For
more information, see [Available test hosts for custom
test environments](custom-test-environments-hosts.md#custom-test-environments-hosts-available "custom-test-environments-hosts.md#custom-test-environments-hosts-available").

**`phases`**

This section contains groups of commands executed during a test run, where each
phase is optional The allowed test phase names are: `install`, `pre_test`
, `test`, and `post_test`.

- `install` - Default dependencies for testing frameworks supported by
  Device Farm are already installed. This phase contains additional commands, if any,
  that Device Farm runs during installation.
- `pre_test` - The commands, if any, executed before your automated
  test.
- `test` - The commands executed during your automated test run. If any
  command in the test phase fails (meaning it returns a non-zero exit code), the test
  is marked as failed
- `post_test` - The commands, if any, executed after your automated
  test run. This will be executed whether or not your test in the `test`
  phase succeeds or fails.

**`commands`**

_(Optional, List[string])_

A list of strings to execute as a shell command during the phase.

**`artifacts`**

_(Optional, List[string])_

Device Farm gathers artifacts such as custom reports, log files, and images from a location
specified here. Wildcard characters are not supported as part of an artifact location,
so you must specify a valid path for each location.

These test artifacts are available for each device in your test run. For information
about retrieving your test artifacts, see [Downloading artifacts in a custom test
environment](using-artifacts-custom.md "using-artifacts-custom.md").

###### Important

A test spec must be formatted as a valid YAML file. If the indenting or spacing in your
test spec are invalid, your test run can fail. Tabs are not allowed in YAML files. You can
use a YAML validator to test whether your test spec is a valid YAML file. For more
information, see the [YAML website](http://yaml.org/spec/1.2/spec.html "http://yaml.org/spec/1.2/spec.html").

## Test spec examples

The following examples show test specs that can be executed on Device Farm.

Simple Demo
The following is an example test spec file that simply logs `Hello world!`
as a test run artifact.

```
version: 0.1

android_test_host: `amazon_linux_2`
ios_test_host: `macos_sequoia`

phases:
  install:
    commands:
      # Setup your environment by installing and/or validating software
      - devicefarm-cli use python 3.11
      - python --version

  pre_test:
    commands:
      # Setup your tests by starting background tasks or setting up
      # additional environment variables.
      - OUTPUT_FILE="/tmp/hello.log"

  test:
    commands:
      # Run your tests within this phase.
      - python -c 'print("Hello world!")' &> $OUTPUT_FILE

  post_test:
    commands:
      # Perform any remaining tasks within this phase, such as copying
      # artifacts to the DEVICEFARM_LOG_DIR for upload
      - cp $OUTPUT_FILE $DEVICEFARM_LOG_DIR

artifacts:
  # By default, Device Farm will collect your artifacts from the $DEVICEFARM_LOG_DIR directory.
  - $DEVICEFARM_LOG_DIR
```

Appium Android

The following is an example test spec file that configures an Appium Java TestNG
test run on Android..

```
version: 0.1

# The following fields(s) allow you to select which Device Farm test host is used for your test run.
android_test_host: `amazon_linux_2`

phases:

  # The install phase contains commands for installing dependencies to run your tests.
  # Certain frequently used dependencies are preinstalled on the test host to accelerate and
  # simplify your test setup. To find these dependencies, versions supported and additional
  # software installation please see:
  # https://docs.aws.amazon.com/devicefarm/latest/developerguide/custom-test-environments-hosts-software.html
  install:
    commands:
      # The Appium server is written using Node.js. In order to run your desired version of Appium,
      # you first need to set up a Node.js environment that is compatible with your version of Appium.
      - devicefarm-cli use node 20
      - node --version

      # Use the devicefarm-cli to select a preinstalled major version of Appium.
      - devicefarm-cli use appium 2
      - appium --version

      # The Device Farm service periodically updates the preinstalled Appium versions over time to
      # incorporate the latest minor and patch versions for each major version. If you wish to
      # select a specific version of Appium, you can use NPM to install it.
      # - npm install -g appium@2.19.0

      # When running Android tests with Appium version 2, the uiautomator2 driver is preinstalled using driver
      # version 2.44.1 for Appium 2.5.1  If you want to install a different version of the driver,
      # you can use the Appium extension CLI to uninstall the existing uiautomator2 driver
      # and install your desired version:
      # - |-
      #   if [ $DEVICEFARM_DEVICE_PLATFORM_NAME = "Android" ];
      #   then
      #     appium driver uninstall uiautomator2;
      #     appium driver install uiautomator2@2.34.0;
      #   fi;

      # Based on Appium framework's recommendation, we recommend setting the Appium server's
      # base path explicitly for accepting commands. If you prefer the legacy base path of /wd/hub,
      # please set it here.
      - export APPIUM_BASE_PATH=

      # Use the devicefarm-cli to setup a Java environment, with which you can run your test suite.
      - devicefarm-cli use java 17
      - java -version

  # The pre-test phase contains commands for setting up your test environment.
  pre_test:
    commands:
      # Setup the CLASSPATH so that Java knows where to find your test classes.
      - export CLASSPATH=$CLASSPATH:$DEVICEFARM_TEST_PACKAGE_PATH/*
      - export CLASSPATH=$CLASSPATH:$DEVICEFARM_TEST_PACKAGE_PATH/dependency-jars/*

      # We recommend starting the Appium server process in the background using the command below.
      # The Appium server log will be written to the $DEVICEFARM_LOG_DIR directory.
      # The environment variables passed as capabilities to the server will be automatically assigned
      # during your test run based on your test's specific device.
      # For more information about which environment variables are set and how they're set, please see
      # https://docs.aws.amazon.com/devicefarm/latest/developerguide/custom-test-environment-variables.html
      - |-
        appium --base-path=$APPIUM_BASE_PATH --log-timestamp \
          --log-no-colors --relaxed-security --default-capabilities \
          "{\"appium:deviceName\": \"$DEVICEFARM_DEVICE_NAME\", \
          \"platformName\": \"$DEVICEFARM_DEVICE_PLATFORM_NAME\", \
          \"appium:udid\":\"$DEVICEFARM_DEVICE_UDID\", \
          \"appium:platformVersion\": \"$DEVICEFARM_DEVICE_OS_VERSION\", \
          \"appium:chromedriverExecutableDir\": \"$DEVICEFARM_CHROMEDRIVER_EXECUTABLE_DIR\", \
          \"appium:automationName\": \"UiAutomator2\"}" \
          >> $DEVICEFARM_LOG_DIR/appium.log 2>&1 &;

      # This code snippet is to wait until the Appium server starts.
      - |-
        appium_initialization_time=0;
        until curl --silent --fail "http://0.0.0.0:4723${APPIUM_BASE_PATH}/status"; do
          if [[ $appium_initialization_time -gt 30 ]]; then
            echo "Appium did not start within 30 seconds. Exiting...";
            exit 1;
          fi;
          appium_initialization_time=$((appium_initialization_time + 1));
          echo "Waiting for Appium to start on port 4723...";
          sleep 1;
        done;

  # The test phase contains commands for running your tests.
  test:
    commands:
      # Your test package is downloaded and unpackaged into the $DEVICEFARM_TEST_PACKAGE_PATH directory.
      - echo "Navigate to test package directory"
      - cd $DEVICEFARM_TEST_PACKAGE_PATH
      - echo "Starting the Appium TestNG test"

      # The following command runs your Appium Java TestNG test.
      # For more information, please see TestNG's documentation here:
      # https://testng.org/#_running_testng
      - |-
        java -Dappium.screenshots.dir=$DEVICEFARM_SCREENSHOT_PATH org.testng.TestNG -testjar *-tests.jar \
          -d $DEVICEFARM_LOG_DIR/test-output -verbose 10

      # To run your tests with a testng.xml file that is a part of your test package,
      # use the following commands instead:

      # - echo "Unzipping the tests JAR file"
      # - unzip *-tests.jar
      # - |-
      #   java -Dappium.screenshots.dir=$DEVICEFARM_SCREENSHOT_PATH org.testng.TestNG -testjar *-tests.jar \
      #     testng.xml -d $DEVICEFARM_LOG_DIR/test-output -verbose 10

  # The post-test phase contains commands that are run after your tests have completed.
  # If you need to run any commands to generating logs and reports on how your test performed,
  # we recommend adding them to this section.
  post_test:
    commands:

# Artifacts are a list of paths on the filesystem where you can store test output and reports.
# All files in these paths will be collected by Device Farm, with certain limits (see limit details
# here: https://docs.aws.amazon.com/devicefarm/latest/developerguide/limits.html#file-limits).
# These files will be available through the ListArtifacts API as your "Customer Artifacts".
artifacts:
  # By default, Device Farm will collect your artifacts from the $DEVICEFARM_LOG_DIR directory.
  - $DEVICEFARM_LOG_DIR
```

Appium iOS

The following is an example test spec file that configures an Appium Java TestNG test
run on iOS.

```
version: 0.1

# The following fields(s) allow you to select which Device Farm test host is used for your test run.
ios_test_host: `macos_sequoia`

phases:

  # The install phase contains commands for installing dependencies to run your tests.
  # Certain frequently used dependencies are preinstalled on the test host to accelerate and
  # simplify your test setup. To find these dependencies, versions supported and additional
  # software installation please see:
  # https://docs.aws.amazon.com/devicefarm/latest/developerguide/custom-test-environments-hosts-software.html
  install:
    commands:
      # The Appium server is written using Node.js. In order to run your desired version of Appium,
      # you first need to set up a Node.js environment that is compatible with your version of Appium.
      - devicefarm-cli use node 20
      - node --version

      # Use the devicefarm-cli to select a preinstalled major version of Appium.
      - devicefarm-cli use appium 2
      - appium --version

      # The Device Farm service periodically updates the preinstalled Appium versions over time to
      # incorporate the latest minor and patch versions for each major version. If you wish to
      # select a specific version of Appium, you can use NPM to install it.
      # - npm install -g appium@2.19.0

      # When running iOS tests with Appium version 2, the XCUITest driver is preinstalled using driver
      # version 9.10.5 for Appium 2.5.4. If you want to install a different version of the driver,
      # you can use the Appium extension CLI to uninstall the existing XCUITest driver
      # and install your desired version:
      # - |-
      #   if [ $DEVICEFARM_DEVICE_PLATFORM_NAME = "iOS" ];
      #   then
      #     appium driver uninstall xcuitest;
      #     appium driver install xcuitest@10.0.0;
      #   fi;

      # Based on Appium framework's recommendation, we recommend setting the Appium server's
      # base path explicitly for accepting commands. If you prefer the legacy base path of /wd/hub,
      # please set it here.
      - export APPIUM_BASE_PATH=

      # Use the devicefarm-cli to setup a Java environment, with which you can run your test suite.
      - devicefarm-cli use java 17
      - java -version

  # The pre-test phase contains commands for setting up your test environment.
  pre_test:
    commands:
      # Setup the CLASSPATH so that Java knows where to find your test classes.
      - export CLASSPATH=$CLASSPATH:$DEVICEFARM_TEST_PACKAGE_PATH/*
      - export CLASSPATH=$CLASSPATH:$DEVICEFARM_TEST_PACKAGE_PATH/dependency-jars/*

      # Device Farm provides multiple pre-built versions of WebDriverAgent (WDA), a required
      # Appium dependency for iOS, where each version corresponds to the XCUITest driver version selected.
      # If Device Farm cannot find a corresponding version of WDA for your XCUITest driver,
      # the latest available version is selected by default.
      - |-
        APPIUM_DRIVER_VERSION=$(appium driver list --installed --json | jq -r ".xcuitest.version" | cut -d "." -f 1);
        CORRESPONDING_APPIUM_WDA=$(env | grep "DEVICEFARM_APPIUM_WDA_DERIVED_DATA_PATH_V${APPIUM_DRIVER_VERSION}")
        if [[ ! -z "$APPIUM_DRIVER_VERSION" ]] && [[ ! -z "$CORRESPONDING_APPIUM_WDA" ]]; then
          echo "Using Device Farm's prebuilt WDA version ${APPIUM_DRIVER_VERSION}.x, which corresponds with your driver";
          DEVICEFARM_APPIUM_WDA_DERIVED_DATA_PATH=$(echo $CORRESPONDING_APPIUM_WDA | cut -d "=" -f2)
        else
          LATEST_SUPPORTED_WDA_VERSION=$(env | grep "DEVICEFARM_APPIUM_WDA_DERIVED_DATA_PATH_V" | sort -V -r | head -n 1)
          echo "Unknown driver version $APPIUM_DRIVER_VERSION; falling back to the Device Farm default version of $LATEST_SUPPORTED_WDA_VERSION";
          DEVICEFARM_APPIUM_WDA_DERIVED_DATA_PATH=$(echo $LATEST_SUPPORTED_WDA_VERSION | cut -d "=" -f2)
        fi;

      # For iOS versions 16 and below only, the device unique identifier (UDID) needs to modified for Appium tests
      # on Device Farm to remove the hypens.
      - |-
        if [ $DEVICEFARM_DEVICE_PLATFORM_NAME = "iOS" ]; then
          DEVICEFARM_DEVICE_UDID_FOR_APPIUM=$DEVICEFARM_DEVICE_UDID;
          if [ $(echo $DEVICEFARM_DEVICE_OS_VERSION | cut -d "." -f 1) -le 16 ]; then
            DEVICEFARM_DEVICE_UDID_FOR_APPIUM=$(echo $DEVICEFARM_DEVICE_UDID | tr -d "-");
          fi;
        fi;

      # We recommend starting the Appium server process in the background using the command below.
      # The Appium server log will be written to the $DEVICEFARM_LOG_DIR directory.
      # The environment variables passed as capabilities to the server will be automatically assigned
      # during your test run based on your test's specific device.
      # For more information about which environment variables are set and how they're set, please see
      # https://docs.aws.amazon.com/devicefarm/latest/developerguide/custom-test-environment-variables.html
      - |-
        appium --base-path=$APPIUM_BASE_PATH --log-timestamp \
          --log-no-colors --relaxed-security --default-capabilities \
          "{\"appium:deviceName\": \"$DEVICEFARM_DEVICE_NAME\", \
          \"platformName\": \"$DEVICEFARM_DEVICE_PLATFORM_NAME\", \
          \"appium:app\": \"$DEVICEFARM_APP_PATH\", \
          \"appium:udid\":\"$DEVICEFARM_DEVICE_UDID_FOR_APPIUM\", \
          \"appium:platformVersion\": \"$DEVICEFARM_DEVICE_OS_VERSION\", \
          \"appium:derivedDataPath\": \"$DEVICEFARM_APPIUM_WDA_DERIVED_DATA_PATH\", \
          \"appium:usePrebuiltWDA\": true, \
          \"appium:automationName\": \"XCUITest\"}" \
          >> $DEVICEFARM_LOG_DIR/appium.log 2>&1 &

      # This code snippet is to wait until the Appium server starts.
      - |-
        appium_initialization_time=0;
        until curl --silent --fail "http://0.0.0.0:4723${APPIUM_BASE_PATH}/status"; do
          if [[ $appium_initialization_time -gt 30 ]]; then
            echo "Appium did not start within 30 seconds. Exiting...";
            exit 1;
          fi;
          appium_initialization_time=$((appium_initialization_time + 1));
          echo "Waiting for Appium to start on port 4723...";
          sleep 1;
        done;

  # The test phase contains commands for running your tests.
  test:
    commands:
      # Your test package is downloaded and unpackaged into the $DEVICEFARM_TEST_PACKAGE_PATH directory.
      - echo "Navigate to test package directory"
      - cd $DEVICEFARM_TEST_PACKAGE_PATH
      - echo "Starting the Appium TestNG test"

      # The following command runs your Appium Java TestNG test.
      # For more information, please see TestNG's documentation here:
      # https://testng.org/#_running_testng
      - |-
        java -Dappium.screenshots.dir=$DEVICEFARM_SCREENSHOT_PATH org.testng.TestNG -testjar *-tests.jar \
          -d $DEVICEFARM_LOG_DIR/test-output -verbose 10

      # To run your tests with a testng.xml file that is a part of your test package,
      # use the following commands instead:

      # - echo "Unzipping the tests JAR file"
      # - unzip *-tests.jar
      # - |-
      #   java -Dappium.screenshots.dir=$DEVICEFARM_SCREENSHOT_PATH org.testng.TestNG -testjar *-tests.jar \
      #     testng.xml -d $DEVICEFARM_LOG_DIR/test-output -verbose 10

  # The post-test phase contains commands that are run after your tests have completed.
  # If you need to run any commands to generating logs and reports on how your test performed,
  # we recommend adding them to this section.
  post_test:
    commands:

# Artifacts are a list of paths on the filesystem where you can store test output and reports.
# All files in these paths will be collected by Device Farm, with certain limits (see limit details
# here: https://docs.aws.amazon.com/devicefarm/latest/developerguide/limits.html#file-limits).
# These files will be available through the ListArtifacts API as your "Customer Artifacts".
artifacts:
  # By default, Device Farm will collect your artifacts from the $DEVICEFARM_LOG_DIR directory.
  - $DEVICEFARM_LOG_DIR
```

Appium (Both Platforms)

The following is an example test spec file that configures an Appium Java TestNG test
run on both Android and iOS.

```
version: 0.1

# The following fields(s) allow you to select which Device Farm test host is used for your test run.
android_test_host: `amazon_linux_2`
ios_test_host: `macos_sequoia`

phases:

  # The install phase contains commands for installing dependencies to run your tests.
  # Certain frequently used dependencies are preinstalled on the test host to accelerate and
  # simplify your test setup. To find these dependencies, versions supported and additional
  # software installation please see:
  # https://docs.aws.amazon.com/devicefarm/latest/developerguide/custom-test-environments-hosts-software.html
  install:
    commands:
      # The Appium server is written using Node.js. In order to run your desired version of Appium,
      # you first need to set up a Node.js environment that is compatible with your version of Appium.
      - devicefarm-cli use node 20
      - node --version

      # Use the devicefarm-cli to select a preinstalled major version of Appium.
      - devicefarm-cli use appium 2
      - appium --version

      # The Device Farm service periodically updates the preinstalled Appium versions over time to
      # incorporate the latest minor and patch versions for each major version. If you wish to
      # select a specific version of Appium, you can use NPM to install it.
      # - npm install -g appium@2.19.0

      # When running Android tests with Appium version 2, the uiautomator2 driver is preinstalled using driver
      # version 2.44.1 for Appium 2.5.1  If you want to install a different version of the driver,
      # you can use the Appium extension CLI to uninstall the existing uiautomator2 driver
      # and install your desired version:
      # - |-
      #   if [ $DEVICEFARM_DEVICE_PLATFORM_NAME = "Android" ];
      #   then
      #     appium driver uninstall uiautomator2;
      #     appium driver install uiautomator2@2.34.0;
      #   fi;

      # When running iOS tests with Appium version 2, the XCUITest driver is preinstalled using driver
      # version 9.10.5 for Appium 2.5.4. If you want to install a different version of the driver,
      # you can use the Appium extension CLI to uninstall the existing XCUITest driver
      # and install your desired version:
      # - |-
      #   if [ $DEVICEFARM_DEVICE_PLATFORM_NAME = "iOS" ];
      #   then
      #     appium driver uninstall xcuitest;
      #     appium driver install xcuitest@10.0.0;
      #   fi;

      # Based on Appium framework's recommendation, we recommend setting the Appium server's
      # base path explicitly for accepting commands. If you prefer the legacy base path of /wd/hub,
      # please set it here.
      - export APPIUM_BASE_PATH=

      # Use the devicefarm-cli to setup a Java environment, with which you can run your test suite.
      - devicefarm-cli use java 17
      - java -version

  # The pre-test phase contains commands for setting up your test environment.
  pre_test:
    commands:
      # Setup the CLASSPATH so that Java knows where to find your test classes.
      - export CLASSPATH=$CLASSPATH:$DEVICEFARM_TEST_PACKAGE_PATH/*
      - export CLASSPATH=$CLASSPATH:$DEVICEFARM_TEST_PACKAGE_PATH/dependency-jars/*

      # Device Farm provides multiple pre-built versions of WebDriverAgent (WDA), a required
      # Appium dependency for iOS, where each version corresponds to the XCUITest driver version selected.
      # If Device Farm cannot find a corresponding version of WDA for your XCUITest driver,
      # the latest available version is selected by default.
      - |-
        if [ $DEVICEFARM_DEVICE_PLATFORM_NAME = "iOS" ]; then
          APPIUM_DRIVER_VERSION=$(appium driver list --installed --json | jq -r ".xcuitest.version" | cut -d "." -f 1);
          CORRESPONDING_APPIUM_WDA=$(env | grep "DEVICEFARM_APPIUM_WDA_DERIVED_DATA_PATH_V${APPIUM_DRIVER_VERSION}")
          if [[ ! -z "$APPIUM_DRIVER_VERSION" ]] && [[ ! -z "$CORRESPONDING_APPIUM_WDA" ]]; then
            echo "Using Device Farm's prebuilt WDA version ${APPIUM_DRIVER_VERSION}.x, which corresponds with your driver";
            DEVICEFARM_APPIUM_WDA_DERIVED_DATA_PATH=$(echo $CORRESPONDING_APPIUM_WDA | cut -d "=" -f2)
          else
            LATEST_SUPPORTED_WDA_VERSION=$(env | grep "DEVICEFARM_APPIUM_WDA_DERIVED_DATA_PATH_V" | sort -V -r | head -n 1)
            echo "Unknown driver version $APPIUM_DRIVER_VERSION; falling back to the Device Farm default version of $LATEST_SUPPORTED_WDA_VERSION";
            DEVICEFARM_APPIUM_WDA_DERIVED_DATA_PATH=$(echo $LATEST_SUPPORTED_WDA_VERSION | cut -d "=" -f2)
          fi;
        fi;

      # For iOS versions 16 and below only, the device unique identifier (UDID) needs to modified for Appium tests
      # on Device Farm to remove the hypens.
      - |-
        if [ $DEVICEFARM_DEVICE_PLATFORM_NAME = "iOS" ]; then
          DEVICEFARM_DEVICE_UDID_FOR_APPIUM=$DEVICEFARM_DEVICE_UDID;
          if [ $(echo $DEVICEFARM_DEVICE_OS_VERSION | cut -d "." -f 1) -le 16 ]; then
            DEVICEFARM_DEVICE_UDID_FOR_APPIUM=$(echo $DEVICEFARM_DEVICE_UDID | tr -d "-");
          fi;
        fi;

      # We recommend starting the Appium server process in the background using the command below.
      # The Appium server log will be written to the $DEVICEFARM_LOG_DIR directory.
      # The environment variables passed as capabilities to the server will be automatically assigned
      # during your test run based on your test's specific device.
      # For more information about which environment variables are set and how they're set, please see
      # https://docs.aws.amazon.com/devicefarm/latest/developerguide/custom-test-environment-variables.html
      - |-
        if [ $DEVICEFARM_DEVICE_PLATFORM_NAME = "Android" ]; then
          appium --base-path=$APPIUM_BASE_PATH --log-timestamp \
            --log-no-colors --relaxed-security --default-capabilities \
            "{\"appium:deviceName\": \"$DEVICEFARM_DEVICE_NAME\", \
            \"platformName\": \"$DEVICEFARM_DEVICE_PLATFORM_NAME\", \
            \"appium:udid\":\"$DEVICEFARM_DEVICE_UDID\", \
            \"appium:platformVersion\": \"$DEVICEFARM_DEVICE_OS_VERSION\", \
            \"appium:chromedriverExecutableDir\": \"$DEVICEFARM_CHROMEDRIVER_EXECUTABLE_DIR\", \
            \"appium:automationName\": \"UiAutomator2\"}" \
            >> $DEVICEFARM_LOG_DIR/appium.log 2>&1 &
        else
          appium --base-path=$APPIUM_BASE_PATH --log-timestamp \
            --log-no-colors --relaxed-security --default-capabilities \
            "{\"appium:deviceName\": \"$DEVICEFARM_DEVICE_NAME\", \
            \"platformName\": \"$DEVICEFARM_DEVICE_PLATFORM_NAME\", \
            \"appium:udid\":\"$DEVICEFARM_DEVICE_UDID_FOR_APPIUM\", \
            \"appium:platformVersion\": \"$DEVICEFARM_DEVICE_OS_VERSION\", \
            \"appium:derivedDataPath\": \"$DEVICEFARM_WDA_DERIVED_DATA_PATH\", \
            \"appium:usePrebuiltWDA\": true, \
            \"appium:automationName\": \"XCUITest\"}" \
            >> $DEVICEFARM_LOG_DIR/appium.log 2>&1 &
        fi;

      # This code snippet is to wait until the Appium server starts.
      - |-
        appium_initialization_time=0;
        until curl --silent --fail "http://0.0.0.0:4723${APPIUM_BASE_PATH}/status"; do
          if [[ $appium_initialization_time -gt 30 ]]; then
            echo "Appium did not start within 30 seconds. Exiting...";
            exit 1;
          fi;
          appium_initialization_time=$((appium_initialization_time + 1));
          echo "Waiting for Appium to start on port 4723...";
          sleep 1;
        done;

  # The test phase contains commands for running your tests.
  test:
    commands:
      # Your test package is downloaded and unpackaged into the $DEVICEFARM_TEST_PACKAGE_PATH directory.
      - echo "Navigate to test package directory"
      - cd $DEVICEFARM_TEST_PACKAGE_PATH
      - echo "Starting the Appium TestNG test"

      # The following command runs your Appium Java TestNG test.
      # For more information, please see TestNG's documentation here:
      # https://testng.org/#_running_testng
      - |-
        java -Dappium.screenshots.dir=$DEVICEFARM_SCREENSHOT_PATH org.testng.TestNG -testjar *-tests.jar \
          -d $DEVICEFARM_LOG_DIR/test-output -verbose 10

      # To run your tests with a testng.xml file that is a part of your test package,
      # use the following commands instead:

      # - echo "Unzipping the tests JAR file"
      # - unzip *-tests.jar
      # - |-
      #   java -Dappium.screenshots.dir=$DEVICEFARM_SCREENSHOT_PATH org.testng.TestNG -testjar *-tests.jar \
      #     testng.xml -d $DEVICEFARM_LOG_DIR/test-output -verbose 10

  # The post-test phase contains commands that are run after your tests have completed.
  # If you need to run any commands to generating logs and reports on how your test performed,
  # we recommend adding them to this section.
  post_test:
    commands:

# Artifacts are a list of paths on the filesystem where you can store test output and reports.
# All files in these paths will be collected by Device Farm, with certain limits (see limit details
# here: https://docs.aws.amazon.com/devicefarm/latest/developerguide/limits.html#file-limits).
# These files will be available through the ListArtifacts API as your "Customer Artifacts".
artifacts:
  # By default, Device Farm will collect your artifacts from the $DEVICEFARM_LOG_DIR directory.
  - $DEVICEFARM_LOG_DIR
```
