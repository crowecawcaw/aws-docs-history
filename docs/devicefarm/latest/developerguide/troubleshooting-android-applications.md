# Troubleshooting Android application tests in

AWS Device Farm

The following topic lists error messages that occur during the upload of Android application tests and
recommends workarounds to resolve each error.

###### Note

The instructions below are based on Linux x86_64 and Mac.

## ANDROID_APP_UNZIP_FAILED

If you see the following message, follow these steps to fix the issue.

###### Warning

We could not open your application. Please verify that the file is valid and try again.

Make sure that you can unzip the application package without errors. In the following example, the package's
name is **app-debug.apk**.

1. Copy your test package to your working directory, and then run the following command:

```
$ unzip app-debug.apk
```

2. After you successfully unzip the package, you can find the working directory tree structure by running the
   following command:

```
$ tree .
```

A valid Android application package should produce output like the following:

```
.
|-- AndroidManifest.xml
|-- classes.dex
|-- resources.arsc
|-- assets (directory)
|-- res (directory)
`-- META-INF (directory)
```

For more information, see [Android tests in AWS Device Farm](test-types-android-tests.md "test-types-android-tests.md").

## ANDROID_APP_AAPT_DEBUG_BADGING_FAILED

If you see the following message, follow these steps to fix the issue.

###### Warning

We could not extract information about your application. Please verify that the application is valid by
running the command `aapt debug badging `<path to your test
 package>``, and try again after the command does not print any error.

During the upload validation process, AWS Device Farm parses out information from the output of an `aapt debug
 badging `<path to your package>`` command.

Make sure that you can run this command on your Android application successfully. In the following example,
the package's name is **app-debug.apk**.

- Copy your application package to your working directory, and then run the command:

```
$ aapt debug badging app-debug.apk
```

A valid Android application package should produce output like the following:

```
package: name='com.amazon.aws.adf.android.referenceapp' versionCode='1' versionName='1.0' platformBuildVersionName='5.1.1-1819727'
sdkVersion:'9'
application-label:'ReferenceApp'
application: label='ReferenceApp' icon='res/mipmap-mdpi-v4/ic_launcher.png'
application-debuggable
launchable-activity: name='com.amazon.aws.adf.android.referenceapp.Activities.MainActivity'  label='ReferenceApp' icon=''
uses-feature: name='android.hardware.bluetooth'
uses-implied-feature: name='android.hardware.bluetooth' reason='requested android.permission.BLUETOOTH permission, and targetSdkVersion > 4'
main
supports-screens: 'small' 'normal' 'large' 'xlarge'
supports-any-density: 'true'
locales: '--_--'
densities: '160' '213' '240' '320' '480' '640'
```

For more information, see [Android tests in AWS Device Farm](test-types-android-tests.md "test-types-android-tests.md").

## ANDROID_APP_PACKAGE_NAME_VALUE_MISSING

If you see the following message, follow these steps to fix the issue.

###### Warning

We could not find the package name value in your application. Please verify that the application is valid by
running the command `aapt debug badging `<path to your test
 package>``, and try again after finding the package name value behind the keyword
"package: name."

During the upload validation process, AWS Device Farm parses out the package name value from the output of an
`aapt debug badging `<path to your package>`` command.

Make sure that you can run this command on your Android application and find the package name value
successfully. In the following example, the package's name is **app-debug.apk**.

- Copy your application package to your working directory, and then run the following command:

```
$ aapt debug badging app-debug.apk | grep "package: name="
```

A valid Android application package should produce output like the following:

```
package: name='com.amazon.aws.adf.android.referenceapp' versionCode='1' versionName='1.0' platformBuildVersionName='5.1.1-1819727'
```

For more information, see [Android tests in AWS Device Farm](test-types-android-tests.md "test-types-android-tests.md").

## ANDROID_APP_SDK_VERSION_VALUE_MISSING

If you see the following message, follow these steps to fix the issue.

###### Warning

We could not find the SDK version value in your application. Please verify that the application is valid by
running the command `aapt debug badging `<path to your test
 package>``, and try again after finding the SDK version value behind the keyword `sdkVersion`.

During the upload validation process, AWS Device Farm parses out the SDK version value from the output of an
`aapt debug badging `<path to your package>`` command.

Make sure that you can run this command on your Android application and find the package name value
successfully. In the following example, the package's name is **app-debug.apk**.

- Copy your application package to your working directory, and then run the following command:

```
$ aapt debug badging app-debug.apk | grep "sdkVersion"
```

A valid Android application package should produce output like the following:

```
sdkVersion:'9'
```

For more information, see [Android tests in AWS Device Farm](test-types-android-tests.md "test-types-android-tests.md").

## ANDROID_APP_AAPT_DUMP_XMLTREE_FAILED

If you see the following message, follow these steps to fix the issue.

###### Warning

We could not find the valid AndroidManifest.xml in your application. Please verify that the test package is
valid by running the command `aapt dump xmltree `<path to your test
 package>` AndroidManifest.xml`, and try again after the command does not print any
error.

During the upload validation process, AWS Device Farm parses out information from the XML parse tree for an XML file
contained within the package using the command `aapt dump xmltree `<path to your
 package>` AndroidManifest.xml`.

Make sure that you can run this command on your Android application successfully. In the following example,
the package's name is **app-debug.apk**.

- Copy your application package to your working directory, and then run the following command:

```
$ aapt dump xmltree app-debug.apk. AndroidManifest.xml
```

A valid Android application package should produce output like the following:

```
N: android=http://schemas.android.com/apk/res/android
  E: manifest (line=2)
    A: android:versionCode(0x0101021b)=(type 0x10)0x1
    A: android:versionName(0x0101021c)="1.0" (Raw: "1.0")
    A: package="com.amazon.aws.adf.android.referenceapp" (Raw: "com.amazon.aws.adf.android.referenceapp")
    A: platformBuildVersionCode=(type 0x10)0x16 (Raw: "22")
    A: platformBuildVersionName="5.1.1-1819727" (Raw: "5.1.1-1819727")
    E: uses-sdk (line=7)
      A: android:minSdkVersion(0x0101020c)=(type 0x10)0x9
      A: android:targetSdkVersion(0x01010270)=(type 0x10)0x16
    E: uses-permission (line=11)
      A: android:name(0x01010003)="android.permission.INTERNET" (Raw: "android.permission.INTERNET")
    E: uses-permission (line=12)
      A: android:name(0x01010003)="android.permission.CAMERA" (Raw: "android.permission.CAMERA")
```

For more information, see [Android tests in AWS Device Farm](test-types-android-tests.md "test-types-android-tests.md").

## ANDROID_APP_DEVICE_ADMIN_PERMISSIONS

If you see the following message, follow these steps to fix the issue.

###### Warning

We found that your application requires device admin permissions. Please verify that the permissions are not
required by run the command `aapt dump xmltree `<path to your test package>`
 AndroidManifest.xml`, and try again after making sure that output does not contain the keyword `android.permission.BIND_DEVICE_ADMIN`.

During the upload validation process, AWS Device Farm parses out permission information from the xml parse tree for
an xml file contained within the package using the command `aapt dump xmltree `<path to your
 package>` AndroidManifest.xml`.

Make sure that your application does not require device admin permission. In the following example, the
package's name is **app-debug.apk**.

- Copy your application package to your working directory, and then run the following command:

```
$ aapt dump xmltree app-debug.apk AndroidManifest.xml
```

You should find output like the following:

```
N: android=http://schemas.android.com/apk/res/android
  E: manifest (line=2)
    A: android:versionCode(0x0101021b)=(type 0x10)0x1
    A: android:versionName(0x0101021c)="1.0" (Raw: "1.0")
    A: package="com.amazonaws.devicefarm.android.referenceapp" (Raw: "com.amazonaws.devicefarm.android.referenceapp")
    A: platformBuildVersionCode=(type 0x10)0x16 (Raw: "22")
    A: platformBuildVersionName="5.1.1-1819727" (Raw: "5.1.1-1819727")
    E: uses-sdk (line=7)
      A: android:minSdkVersion(0x0101020c)=(type 0x10)0xa
      A: android:targetSdkVersion(0x01010270)=(type 0x10)0x16
    E: uses-permission (line=11)
      A: android:name(0x01010003)="android.permission.INTERNET" (Raw: "android.permission.INTERNET")
    E: uses-permission (line=12)
      A: android:name(0x01010003)="android.permission.CAMERA" (Raw: "android.permission.CAMERA")
        ……
```

If the Android application is valid, the output should not contain the following: `A:
 android:name(0x01010003)="android.permission.BIND_DEVICE_ADMIN" (Raw:
 "android.permission.BIND_DEVICE_ADMIN")`.

For more information, see [Android tests in AWS Device Farm](test-types-android-tests.md "test-types-android-tests.md").

## Certain windows in my Android application show a blank or black

screen

If you are testing an Android application and notice that certain windows in the application appear with a
black screen in Device Farm's video recording of your test, your application may be using Android's
`FLAG_SECURE` feature. This flag (as described in [Android's
official documentation](https://developer.android.com/reference/android/view/WindowManager.LayoutParams.html#FLAG_SECURE "https://developer.android.com/reference/android/view/WindowManager.LayoutParams.html#FLAG_SECURE")) is used to prevent certain windows of an application from being recorded by
screen recording tools. As a result, Device Farm's screen recording feature (for both automation and remote access
testing) may show a black screen in place of your application's window if the window uses this flag.

This flag is often used by developers for pages in their application that contain sensitive information such
as login pages. If you are seeing a black screen in place of your application's screen for certain pages like its
login page, work with your developer(s) to obtain a build of the application that doesn't use this flag for
testing.

Additionally, note that Device Farm can still interact with application windows that have this flag. So, if your
application's login page appears as a black screen, you may still be able to enter your credentials in order to
log in to the application (and thus view pages not blocked by the `FLAG_SECURE` flag).
