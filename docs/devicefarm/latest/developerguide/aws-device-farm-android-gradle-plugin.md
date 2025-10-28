# Integrating Device Farm with a Gradle build system

The Device Farm Gradle plugin provides AWS Device Farm integration with the Gradle build system in Android Studio. For more information,
see [Gradle](https://gradle.org "https://gradle.org").

###### Note

To download the Gradle plugin, go to [GitHub](https://github.com/awslabs/aws-device-farm-gradle-plugin "https://github.com/awslabs/aws-device-farm-gradle-plugin") and follow the instructions in [Building the Device Farm Gradle plugin](#aws-device-farm-gradle-plugin-building "#aws-device-farm-gradle-plugin-building").

The Device Farm Gradle Plugin provides Device Farm functionality from your Android Studio environment. You can kick off
tests on real Android phones and tablets hosted by Device Farm.

This section contains a series of procedures to set up and use the Device Farm Gradle Plugin.

###### Topics

- [Dependencies](#aws-device-farm-gradle-plugin-dependencies "#aws-device-farm-gradle-plugin-dependencies")
- [Step 1: Building the AWS Device Farm Gradle plugin](#aws-device-farm-gradle-plugin-building "#aws-device-farm-gradle-plugin-building")
- [Step 2: Setting up the AWS Device Farm Gradle
  plugin](#aws-device-farm-gradle-plugin-setting-up "#aws-device-farm-gradle-plugin-setting-up")
- [Step 3: Generating an IAM user in the Device Farm Gradle plugin](#aws-device-farm-gradle-plugin-generating-iam-user "#aws-device-farm-gradle-plugin-generating-iam-user")
- [Step 4: Configuring test types](#aws-device-farm-gradle-plugin-configuring-test-types "#aws-device-farm-gradle-plugin-configuring-test-types")

## Dependencies

**Runtime**

- The Device Farm Gradle Plugin requires the AWS Mobile SDK 1.10.15 or later. For more information and to
  install the SDK, see [AWS Mobile SDK](https://aws.amazon.com/mobile/sdk/ "https://aws.amazon.com/mobile/sdk/").
- Android tools builder test api 0.5.2
- Apache Commons Lang3 3.3.4

**For Unit Tests**

- Testng 6.8.8
- Jmockit 1.19
- Android gradle tools 1.3.0

## Step 1: Building the AWS Device Farm Gradle plugin

This plugin provides AWS Device Farm integration with the Gradle build system in Android Studio. For more
information, see [Gradle](https://gradle.org "https://gradle.org").

###### Note

Building the plugin is optional. The plugin is published through Maven
Central. If you wish to allow Gradle to download the plugin directly, skip this step
and jump to [Step 2: Setting up the AWS Device Farm Gradle
plugin](#aws-device-farm-gradle-plugin-setting-up "#aws-device-farm-gradle-plugin-setting-up").

###### To build the plugin

1. Go to [GitHub](https://github.com/awslabs/aws-device-farm-gradle-plugin "https://github.com/awslabs/aws-device-farm-gradle-plugin") and clone the
   repository.
2. Build the plugin using `gradle install`.

The plugin is installed to your local maven repository.

Next step: [Step 2: Setting up the AWS Device Farm Gradle
plugin](#aws-device-farm-gradle-plugin-setting-up "#aws-device-farm-gradle-plugin-setting-up")

## Step 2: Setting up the AWS Device Farm Gradle

plugin

If you haven't done so already, clone the repository and install the plugin using the procedure here: [Building the Device Farm Gradle plugin](#aws-device-farm-gradle-plugin-building "#aws-device-farm-gradle-plugin-building").

###### To configure the AWS Device Farm Gradle Plugin

1. Add the plugin artifact to your dependency list in `build.gradle`.

```
    buildscript {

        repositories {
            mavenLocal()
            mavenCentral()
        }

        dependencies {
            classpath 'com.android.tools.build:gradle:1.3.0'
            classpath 'com.amazonaws:aws-devicefarm-gradle-plugin:1.0'
        }
    }
```

2. Configure the plugin in your `build.gradle` file. The following test specific
   configuration should serve as your guide:

```
apply plugin: 'devicefarm'

devicefarm {

    // Required. The project must already exist. You can create a project in the AWS Device Farm console.
    projectName "My Project" // required: Must already exist.

    // Optional. Defaults to "Top Devices"
    // devicePool "My Device Pool Name"

    // Optional. Default is 150 minutes
    // executionTimeoutMinutes 150

    // Optional. Set to "off" if you want to disable device video recording during a run. Default is "on"
    // videoRecording "on"

    // Optional. Set to "off" if you want to disable device performance monitoring during a run. Default is "on"
    // performanceMonitoring "on"

    // Optional. Add this if you have a subscription and want to use your unmetered slots
    // useUnmeteredDevices()

    // Required. You must specify either accessKey and secretKey OR roleArn. roleArn takes precedence.
    authentication {
        accessKey "AKIAIOSFODNN7EXAMPLE"
        secretKey "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

        // OR

        roleArn "arn:aws:iam::111122223333:role/DeviceFarmRole"
    }

    // Optionally, you can
    // - enable or disable Wi-Fi, Bluetooth, GPS, NFC radios
    // - set the GPS coordinates
    // - specify files and applications that must be on the device when your test runs
    devicestate {
        // Extra files to include on the device.
        // extraDataZipFile file("path/to/zip")

        // Other applications that must be installed in addition to yours.
        // auxiliaryApps files(file("path/to/app"), file("path/to/app2"))

        // By default, Wi-Fi, Bluetooth, GPS, and NFC are turned on.
        // wifi "off"
        // bluetooth "off"
        // gps "off"
        // nfc "off"

        // You can specify GPS location. By default, this location is 47.6204, -122.3491
        // latitude 44.97005
        // longitude -93.28872
    }

    // By default, the Instrumentation test is used.
    // If you want to use a different test type, configure it here.
    // You can set only one test type (for example, Calabash, Fuzz, and so on)

    // Fuzz
    // fuzz { }

    // Calabash
    // calabash { tests file("path-to-features.zip") }

}

```

3. Run your Device Farm test using the following task: `gradle devicefarmUpload`.

The build output will print out a link to the Device Farm console where you can monitor your test
execution.

Next step: [Generating an IAM user in the Device Farm Gradle
plugin](#aws-device-farm-gradle-plugin-generating-iam-user "#aws-device-farm-gradle-plugin-generating-iam-user")

## Step 3: Generating an IAM user in the Device Farm Gradle plugin

AWS Identity and Access Management (IAM) helps you manage permissions and policies for working with AWS resources. This
topic walks you through generating an IAM user with permissions to access AWS Device Farm resources.

If you haven't done so already, complete steps 1 and 2 before generating an IAM
user.

We recommend that you do not use your AWS root account to access Device Farm. Instead,
create a new IAM user (or use an existing IAM user) in your AWS
account, and then access Device Farm with that IAM user.

###### Note

The AWS root account or IAM user that you use to complete the following steps
must have permission to create the following IAM policy and attach it to the IAM
user. For more information, see [Working with
Policies](../../../IAM/latest/UserGuide/policies_manage.md "../../../IAM/latest/UserGuide/policies_manage.md").

###### To create a new user with the proper access policy in IAM

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Choose **Users**.
3. Choose **Create New Users**.
4. Enter the user name of your choice.

For example, `GradleUser`. 5. Choose **Create**. 6. Choose **Download Credentials** and save them in a location where you
can easily retrieve them later. 7. Choose **Close**. 8. Choose the user name in the list. 9. Under **Permissions**, expand the **Inline Policies**
header by clicking the down arrow on the right. 10. Choose **Click here** where it says, **There are no inline
policies to show. To create one, click here**. 11. On the **Set Permissions** screen, choose **Custom Policy**. 12. Choose **Select**. 13. Give your policy a name, such as `AWSDeviceFarmGradlePolicy`. 14. Paste the following policy into **Policy Document**.

JSON

```
 `{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DeviceFarmAll",
 "Effect": "Allow",
 "Action": [ "devicefarm:*" ],
 "Resource": [ "*" ]
 }
 ]
 }`

```

15. Choose **Apply Policy**.

Next step: [Configuring test types](#aws-device-farm-gradle-plugin-configuring-test-types "#aws-device-farm-gradle-plugin-configuring-test-types").

For more information, see [Creating an
IAM User (AWS Management Console)](../../../IAM/latest/UserGuide/Using_SettingUpUser.md#Using_CreateUser_console "../../../IAM/latest/UserGuide/Using_SettingUpUser.md#Using_CreateUser_console") or [Setting up](setting-up.md "setting-up.md").

## Step 4: Configuring test types

By default, the AWS Device Farm Gradle plugin runs the [Instrumentation for Android and AWS Device Farm](test-types-android-instrumentation.md "test-types-android-instrumentation.md") test. If you want to run your own tests
or specify additional parameters, you can choose to configure a test type. This topic provides
information about each available test type and what you need to do in Android Studio to
configure it for use. For more information about the available test types in Device Farm, see [Test frameworks and built-in tests in AWS Device Farm](test-types.md "test-types.md").

If you haven't done so already, complete steps 1 – 3 before configuring test
types.

###### Note

If
you are using [device slots](how-to-purchase-device-slots.md "how-to-purchase-device-slots.md"), the device
slots feature is disabled by default.

### Appium

Device Farm provides support for Appium Java JUnit and TestNG for Android.

- [Appium (under Java (JUnit))](test-types-appium.md "test-types-appium.md")
- [Appium (under Java (TestNG))](test-types-appium.md "test-types-appium.md")

You can choose `useTestNG()` or `useJUnit()`. `JUnit` is the default and does not need to be explicitly specified.

```
    appium {
        tests file("path to zip file") // required
        useTestNG() // or useJUnit()
    }
```

### Built-in: fuzz

Device Farm provides a built-in fuzz test type, which randomly sends user interface events to
devices and then reports the results.

```
    fuzz {

       eventThrottle 50 // optional default
       eventCount 6000  // optional default
       randomizerSeed 1234 // optional default blank

     }
```

For more information, see [Running Device Farm's built-in fuzz test (Android and iOS)](test-types-built-in-fuzz.md "test-types-built-in-fuzz.md").

### Instrumentation

Device Farm provides support for instrumentation (JUnit, Espresso, Robotium, or any
instrumentation-based tests) for Android. For more information, see [Instrumentation for Android and AWS Device Farm](test-types-android-instrumentation.md "test-types-android-instrumentation.md").

When running an instrumentation test in Gradle, Device Farm uses the `.apk` file
generated from your **androidTest** directory as the source of your tests.

```
    instrumentation {

        filter "test filter per developer docs" // optional

    }
```
