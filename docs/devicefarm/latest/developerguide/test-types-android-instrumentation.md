# Instrumentation for Android and AWS Device Farm

Device Farm provides support for Instrumentation (JUnit, Espresso, Robotium, or any Instrumentation-based tests) for
Android.

Device Farm also provides a sample Android application and links to working tests in three Android automation
frameworks, including Instrumentation (Espresso). The [Device Farm sample app for Android](https://github.com/awslabs/aws-device-farm-sample-app-for-android "https://github.com/awslabs/aws-device-farm-sample-app-for-android") is
available for download on GitHub.

For more information about testing in Device Farm, see [Test frameworks and built-in tests in AWS Device Farm](test-types.md "test-types.md").

###### Topics

- [What is instrumentation?](#test-types-android-instrumentation-what-is "#test-types-android-instrumentation-what-is")
- [Considerations for Android instrumentation
  tests](#test-types-android-instrumentation-settings "#test-types-android-instrumentation-settings")
- [Standard mode test parsing](#test-types-android-standard-mode-test-parse "#test-types-android-standard-mode-test-parse")
- [Integrating Android Instrumentation with
  Device Farm](test-types-android-instrumentation-integrate.md "test-types-android-instrumentation-integrate.md")

## What is instrumentation?

Android instrumentation makes it possible for you to invoke callback methods in your test code so you can
run through the lifecycle of a component step by step, as if you were debugging the component. For more
information, see [Instrumented tests](https://developer.android.com/studio/test/test-in-android-studio#test_types_and_locations "https://developer.android.com/studio/test/test-in-android-studio#test_types_and_locations") in the _Test types and locations_ section
of the _Android Developer Tools_ documentation.

## Considerations for Android instrumentation

tests

When using Android instrumentation, consider the following recommendations and notes.

**Check Android OS Compatibility**

Check the [Android
documentation](https://developer.android.com/jetpack/androidx/releases/test#orchestrator-1.5.0 "https://developer.android.com/jetpack/androidx/releases/test#orchestrator-1.5.0") , to ensure Instrumentation is compatible with your Android OS version.

**Running from the Command Line**

To run Instrumentation tests from the command line, please follow the [Android
documentation.](https://developer.android.com/training/testing/instrumented-tests/androidx-test-libraries/runner#enable-command "https://developer.android.com/training/testing/instrumented-tests/androidx-test-libraries/runner#enable-command")

**System Animations**

Per the [Android
documentation for Espresso testing](https://developer.android.com/training/testing/espresso "https://developer.android.com/training/testing/espresso"), it is recommended that system animations are
turned off when testing on real devices. Device Farm automatically disables **Window Animation
Scale**, **Transition Animation Scale**, and **Animator
Duration Scale** settings when it executes with the [android.support.test.runner.AndroidJUnitRunner](http://developer.android.com/reference/android/support/test/runner/AndroidJUnitRunner.html "http://developer.android.com/reference/android/support/test/runner/AndroidJUnitRunner.html") instrumentation test runner.

**Test Recorders**

Device Farm supports frameworks, such as Robotium, that have record-and-playback scripting
tools.

## Standard mode test parsing

In the standard mode of a run, Device Farm parses your test suite and identifies the unique test classes and
methods that it will run. This is done through a tool called [Dex Test Parser](https://github.com/linkedin/dex-test-parser "https://github.com/linkedin/dex-test-parser").

When given an Android instrumentation .apk file as input, the parser returns the fully qualified method
names of the tests that match JUnit 3 and JUnit 4 conventions.

To test this in a local environment:

1. Download the [`dex-test-parser`](https://github.com/linkedin/dex-test-parser "https://github.com/linkedin/dex-test-parser") binary.
2. Run the following command to get the list of test methods that will run on Device Farm:

```
java -jar parser.jar path/to/apk path/for/output
```
