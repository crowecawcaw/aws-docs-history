# Troubleshooting instrumentation tests in AWS Device Farm

The following topic lists error messages that occur during the upload of Instrumentation
tests and recommends workarounds to resolve each error.

###### Note

For important considerations when using Instrumentation tests in AWS Device Farm, see [Instrumentation for Android and AWS Device Farm](test-types-android-instrumentation.md "test-types-android-instrumentation.md").

## INSTRUMENTATION_TEST_PACKAGE_UNZIP_FAILED

If you see the following message, follow these steps to fix the issue.

```
`Warning: We could not open your test APK file. Please verify that the file is valid and
 try again.`
```

Make sure that you can unzip the test package without errors. In the following example,
the package's name is **app-debug-androidTest-unaligned.apk**.

1. Copy your test package to your working directory, and then run the
   following command:

```
$ unzip app-debug-androidTest-unaligned.apk
```

2. After you successfully unzip the package, you can find the working directory tree structure by
   running the following command:

```
$ tree .
```

A valid Instrumentation test package will produce output like the following:

```
.
|-- AndroidManifest.xml
|--  classes.dex
|-- resources.arsc
|-- LICENSE-junit.txt
|-- junit (directory)
`-- META-INF (directory)
```

For more information, see [Instrumentation for Android and AWS Device Farm](test-types-android-instrumentation.md "test-types-android-instrumentation.md").

## INSTRUMENTATION_TEST_PACKAGE_AAPT_DEBUG_BADGING_FAILED

If you see the following message, follow these steps to fix the issue.

```
`We could not extract information about your test package. Please verify that the
 test package is valid by running the command "aapt debug badging <path to your test
 package>", and try again after the command does not print any error.`
```

During the upload validation process, Device Farm parses out information from the output
of the `aapt debug badging <path to your package>` command.

Make sure that you can run this command on your Instrumentation test package successfully.

In the following example,
the package's name is **app-debug-androidTest-unaligned.apk**.

- Copy your test package to your working directory, and then run the
  following command:

```
$ aapt debug badging app-debug-androidTest-unaligned.apk
```

A valid Instrumentation test package will produce output like the following:

```
package: name='com.amazon.aws.adf.android.referenceapp.test' versionCode='' versionName='' platformBuildVersionName='5.1.1-1819727'
sdkVersion:'9'
targetSdkVersion:'22'
application-label:'Test-api'
application: label='Test-api' icon=''
application-debuggable
uses-library:'android.test.runner'
feature-group: label=''
uses-feature: name='android.hardware.touchscreen'
uses-implied-feature: name='android.hardware.touchscreen' reason='default feature for all apps'
supports-screens: 'small' 'normal' 'large' 'xlarge'
supports-any-density: 'true'
locales: '--_--'
densities: '160'
```

For more information, see [Instrumentation for Android and AWS Device Farm](test-types-android-instrumentation.md "test-types-android-instrumentation.md").

## INSTRUMENTATION_TEST_PACKAGE_INSTRUMENTATION_RUNNER_VALUE_MISSING

If you see the following message, follow these steps to fix the issue.

```
`We could not find the instrumentation runner value in the AndroidManifest.xml.
 Please verify the test package is valid by running the command "aapt dump xmltree <path to
 your test package> AndroidManifest.xml", and try again after finding the instrumentation
 runner value behind the keyword "instrumentation."`
```

During the upload validation process, Device Farm parses out the instrumentation runner value
from the XML parse tree for an XML file contained within the package. You can use the
following command: `aapt dump xmltree <path to your package>
 AndroidManifest.xml`.

Make sure that you can run this command on your Instrumentation test package and find the
instrumentation value successfully.

In the following example,
the package's name is **app-debug-androidTest-unaligned.apk**.

- Copy your test package to your working directory, and then run the
  following command:

```
$ aapt dump xmltree app-debug-androidTest-unaligned.apk AndroidManifest.xml | grep -A5 "instrumentation"
```

A valid Instrumentation test package will produce output like the following:

```
E: instrumentation (line=9)
      A: android:label(0x01010001)="Tests for com.amazon.aws.adf.android.referenceapp" (Raw: "Tests for com.amazon.aws.adf.android.referenceapp")
      A: android:name(0x01010003)="`android.support.test.runner.AndroidJUnitRunner`" (Raw: "android.support.test.runner.AndroidJUnitRunner")
      A: android:targetPackage(0x01010021)="com.amazon.aws.adf.android.referenceapp" (Raw: "com.amazon.aws.adf.android.referenceapp")
      A: android:handleProfiling(0x01010022)=(type 0x12)0x0
      A: android:functionalTest(0x01010023)=(type 0x12)0x0
```

For more information, see [Instrumentation for Android and AWS Device Farm](test-types-android-instrumentation.md "test-types-android-instrumentation.md").

## INSTRUMENTATION_TEST_PACKAGE_AAPT_DUMP_XMLTREE_FAILED

If you see the following message, follow these steps to fix the issue.

```
`We could not find the valid AndroidManifest.xml in your test package. Please
 verify that the test package is valid by running the command "aapt dump xmltree <path to
 your test package> AndroidManifest.xml", and try again after the command does not print any
 error.`
```

During the upload validation process, Device Farm parses out information from the XML parse tree
for an XML file contained within the package using the following
command: `aapt dump xmltree <path to your package> AndroidManifest.xml`.

Make sure that you can run this command on your instrumentation test package successfully.

In the following example,
the package's name is **app-debug-androidTest-unaligned.apk**.

- Copy your test package to your working directory, and then run the
  following command:

```
$ aapt dump xmltree app-debug-androidTest-unaligned.apk AndroidManifest.xml
```

A valid Instrumentation test package will produce output like the following:

```
N: android=http://schemas.android.com/apk/res/android
  E: manifest (line=2)
    A: package="com.amazon.aws.adf.android.referenceapp.test" (Raw: "com.amazon.aws.adf.android.referenceapp.test")
    A: platformBuildVersionCode=(type 0x10)0x16 (Raw: "22")
    A: platformBuildVersionName="5.1.1-1819727" (Raw: "5.1.1-1819727")
    E: uses-sdk (line=5)
      A: android:minSdkVersion(0x0101020c)=(type 0x10)0x9
      A: android:targetSdkVersion(0x01010270)=(type 0x10)0x16
    E: instrumentation (line=9)
      A: android:label(0x01010001)="Tests for com.amazon.aws.adf.android.referenceapp" (Raw: "Tests for com.amazon.aws.adf.android.referenceapp")
      A: android:name(0x01010003)="android.support.test.runner.AndroidJUnitRunner" (Raw: "android.support.test.runner.AndroidJUnitRunner")
      A: android:targetPackage(0x01010021)="com.amazon.aws.adf.android.referenceapp" (Raw: "com.amazon.aws.adf.android.referenceapp")
      A: android:handleProfiling(0x01010022)=(type 0x12)0x0
      A: android:functionalTest(0x01010023)=(type 0x12)0x0
    E: application (line=16)
      A: android:label(0x01010001)=@0x7f020000
      A: android:debuggable(0x0101000f)=(type 0x12)0xffffffff
      E: uses-library (line=17)
        A: android:name(0x01010003)="android.test.runner" (Raw: "android.test.runner")
```

For more information, see [Instrumentation for Android and AWS Device Farm](test-types-android-instrumentation.md "test-types-android-instrumentation.md").

## INSTRUMENTATION_TEST_PACKAGE_TEST_PACKAGE_NAME_VALUE_MISSING

If you see the following message, follow these steps to fix the issue.

```
`We could not find the package name in your test package. Please verify that the
 test package is valid by running the command "aapt debug badging <path to your test
 package>", and try again after finding the package name value behind the keyword "package:
 name."`
```

During the upload validation process, Device Farm parses out the package name value from the output
of the
following command: `aapt debug badging <path to your package>`.

Make sure that you can run this command on your Instrumentation test package and find the
package name value successfully.

In the following example,
the package's name is **app-debug-androidTest-unaligned.apk**.

- Copy your test package to your working directory, and then run the
  following command:

```
$ aapt debug badging app-debug-androidTest-unaligned.apk | grep "package: name="
```

A valid Instrumentation test package will produce output like the following:

```
package: name='com.amazon.aws.adf.android.referenceapp.test' versionCode='' versionName='' platformBuildVersionName='5.1.1-1819727'
```

For more information, see [Instrumentation for Android and AWS Device Farm](test-types-android-instrumentation.md "test-types-android-instrumentation.md").
