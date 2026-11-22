

# Troubleshooting test and application packaging for use in AWS Device Farm

The following sections list error messages that can occur when you upload applications and test packages to Device Farm, grouped by application platform and test type.

**Topics**
+ [Troubleshooting Android application tests in AWS Device Farm](#troubleshooting-android-applications)
+ [Troubleshooting iOS application tests in AWS Device Farm](#troubleshooting-ios-applications)
+ [Troubleshooting Appium Java JUnit tests in AWS Device Farm](#troubleshooting-appium-java-junit)
+ [Troubleshooting Appium Java JUnit web application tests in AWS Device Farm](#troubleshooting-appium-web-java-junit-tests)
+ [Troubleshooting Appium Java TestNG tests in AWS Device Farm](#troubleshooting-appium-java-testng)
+ [Troubleshooting Appium Java TestNG web applications in AWS Device Farm](#troubleshooting-appium-web-java-testng)
+ [Troubleshooting Appium Python tests in AWS Device Farm](#troubleshooting-appium-python)
+ [Troubleshooting Appium Python web application tests in AWS Device Farm](#troubleshooting-appium-web-python)
+ [Troubleshooting instrumentation tests in AWS Device Farm](#troubleshooting-instrumentation-tests)
+ [Troubleshooting XCTest tests in AWS Device Farm](#troubleshooting-xctest)
+ [Troubleshooting XCTest UI tests in AWS Device Farm](#troubleshooting-xctest-ui)

## Troubleshooting Android application tests in AWS Device Farm
<a name="troubleshooting-android-applications"></a>

The following topic lists error messages that occur during the upload of Android application tests and recommends workarounds to resolve each error.

### ANDROID\_APP\_UNZIP\_FAILED
<a name="ANDROID_APP_UNZIP_FAILED"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not open your application. Please verify that the file is valid and try again.

Make sure that you can unzip the application package without errors. In the following example, the package's name is **app-debug.apk**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip app-debug.apk
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

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

   For more information, see [Android tests in AWS Device Farm](test-types-android-tests.md).

### ANDROID\_APP\_AAPT\_DEBUG\_BADGING\_FAILED
<a name="ANDROID_APP_AAPT_DEBUG_BADGING_FAILED"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not extract information about your application. Please verify that the application is valid by running the command `aapt debug badging {{<path to your test package>}}`, and try again after the command does not print any error. 

During the upload validation process, AWS Device Farm parses out information from the output of an `aapt debug badging {{<path to your package>}}` command. 

Make sure that you can run this command on your Android application successfully. In the following example, the package's name is **app-debug.apk**.
+ Copy your application package to your working directory, and then run the command:

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

  For more information, see [Android tests in AWS Device Farm](test-types-android-tests.md).

### ANDROID\_APP\_PACKAGE\_NAME\_VALUE\_MISSING
<a name="ANDROID_APP_PACKAGE_NAME_VALUE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find the package name value in your application. Please verify that the application is valid by running the command `aapt debug badging {{<path to your test package>}}`, and try again after finding the package name value behind the keyword "package: name."

During the upload validation process, AWS Device Farm parses out the package name value from the output of an `aapt debug badging {{<path to your package>}}` command.

Make sure that you can run this command on your Android application and find the package name value successfully. In the following example, the package's name is **app-debug.apk**.
+ Copy your application package to your working directory, and then run the following command:

  ```
  $ aapt debug badging app-debug.apk | grep "package: name="
  ```

  A valid Android application package should produce output like the following:

  ```
  package: name='com.amazon.aws.adf.android.referenceapp' versionCode='1' versionName='1.0' platformBuildVersionName='5.1.1-1819727'
  ```

  For more information, see [Android tests in AWS Device Farm](test-types-android-tests.md).

### ANDROID\_APP\_SDK\_VERSION\_VALUE\_MISSING
<a name="ANDROID_APP_SDK_VERSION_VALUE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find the SDK version value in your application. Please verify that the application is valid by running the command `aapt debug badging {{<path to your test package>}}`, and try again after finding the SDK version value behind the keyword `sdkVersion`.

During the upload validation process, AWS Device Farm parses out the SDK version value from the output of an `aapt debug badging {{<path to your package>}}` command.

Make sure that you can run this command on your Android application and find the package name value successfully. In the following example, the package's name is **app-debug.apk**.
+ Copy your application package to your working directory, and then run the following command:

  ```
  $ aapt debug badging app-debug.apk | grep "sdkVersion"
  ```

  A valid Android application package should produce output like the following:

  ```
  sdkVersion:'9'
  ```

  For more information, see [Android tests in AWS Device Farm](test-types-android-tests.md).

### ANDROID\_APP\_AAPT\_DUMP\_XMLTREE\_FAILED
<a name="ANDROID_APP_AAPT_DUMP_XMLTREE_FAILED"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find the valid AndroidManifest.xml in your application. Please verify that the test package is valid by running the command `aapt dump xmltree {{<path to your test package>}} AndroidManifest.xml`, and try again after the command does not print any error.

During the upload validation process, AWS Device Farm parses out information from the XML parse tree for an XML file contained within the package using the command `aapt dump xmltree {{<path to your package>}} AndroidManifest.xml`.

Make sure that you can run this command on your Android application successfully. In the following example, the package's name is **app-debug.apk**.
+ Copy your application package to your working directory, and then run the following command:

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

  For more information, see [Android tests in AWS Device Farm](test-types-android-tests.md).

### ANDROID\_APP\_DEVICE\_ADMIN\_PERMISSIONS
<a name="ANDROID_APP_DEVICE_ADMIN_PERMISSIONS"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We found that your application requires device admin permissions. Please verify that the permissions are not required by run the command `aapt dump xmltree {{<path to your test package>}} AndroidManifest.xml`, and try again after making sure that output does not contain the keyword `android.permission.BIND_DEVICE_ADMIN`.

During the upload validation process, AWS Device Farm parses out permission information from the xml parse tree for an xml file contained within the package using the command `aapt dump xmltree {{<path to your package>}} AndroidManifest.xml`.

Make sure that your application does not require device admin permission. In the following example, the package's name is **app-debug.apk**.
+ Copy your application package to your working directory, and then run the following command:

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

  If the Android application is valid, the output should not contain the following: `A: android:name(0x01010003)="android.permission.BIND_DEVICE_ADMIN" (Raw: "android.permission.BIND_DEVICE_ADMIN")`. 

  For more information, see [Android tests in AWS Device Farm](test-types-android-tests.md).

## Troubleshooting iOS application tests in AWS Device Farm
<a name="troubleshooting-ios-applications"></a>

The following topic lists error messages that occur during the upload of iOS application tests and recommends workarounds to resolve each error.

### IOS\_APP\_UNZIP\_FAILED
<a name="IOS_APP_UNZIP_FAILED"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not open your application. Please verify that the file is valid and try again.

Make sure that you can unzip the application package without errors. In the following example, the package's name is **AWSDeviceFarmiOSReferenceApp.ipa**.

1. Copy your application package to your working directory, and then run the following command:

   ```
   $ unzip AWSDeviceFarmiOSReferenceApp.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   A valid iOS application package should produce output like the following:

   ```
   .
   `-- Payload (directory)
           `-- AWSDeviceFarmiOSReferenceApp.app (directory)
                         |-- Info.plist
                         `-- (any other files)
   ```

   For more information, see [iOS tests in AWS Device Farm](test-types-ios-tests.md).

### IOS\_APP\_PAYLOAD\_DIR\_MISSING
<a name="IOS_APP_PAYLOAD_DIR_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find the Payload directory in your IOS application package. Please unzip your application package, verify that the Payload directory is inside the package, and try again. If your application is built for a simulator, upload either an .ipa file with the .app directory inside a Payload directory at the root of the archive, or a .zip file with the .app directory at the root of the archive.

Device Farm rejects a simulator build with this error when the {{.app}} directory is nested inside another folder. For more information about the simulator build and packaging steps, see [Packaging an iOS app](apps.md#test-runs-ios-app-packaging).

In the following example, the package's name is **AWSDeviceFarmiOSReferenceApp.ipa**.

1. Copy your application package to your working directory, and then run the following command:

   ```
   $ unzip AWSDeviceFarmiOSReferenceApp.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the iOS application package is a valid `.ipa` file, the `Payload` directory is inside the working directory.

   ```
   .
   `-- {{Payload}} (directory)
           `-- AWSDeviceFarmiOSReferenceApp.app (directory)
                         |-- Info.plist
                         `-- (any other files)
   ```

   For more information, see [iOS tests in AWS Device Farm](test-types-ios-tests.md).

### IOS\_APP\_APP\_DIR\_MISSING
<a name="IOS_APP_APP_DIR_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find the .app directory inside the Payload directory. Please unzip your application and then open the Payload directory, verify that the .app directory is inside the directory, and try again.

In the following example, the package's name is **AWSDeviceFarmiOSReferenceApp.ipa**.

1. Copy your application package to your working directory, and then run the following command:

   ```
   $ unzip AWSDeviceFarmiOSReferenceApp.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the iOS application package is valid, you will find an {{.app}} directory like {{AWSDeviceFarmiOSReferenceApp.app}} in our example inside the `Payload` directory.

   ```
   .
   `-- Payload (directory)
           `-- {{AWSDeviceFarmiOSReferenceApp.app}} (directory)
                         |-- Info.plist
                         `-- (any other files)
   ```

   For more information, see [iOS tests in AWS Device Farm](test-types-ios-tests.md).

### IOS\_APP\_MULTIPLE\_APP\_DIRS
<a name="IOS_APP_MULTIPLE_APP_DIRS"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We found multiple .app directories inside your IOS application package. Please unzip your application package, verify that only a single .app directory is present inside the package, then try again.

In the following example, the package's name is **AWSDeviceFarmiOSReferenceApp.ipa**.

1. Copy your application package to your working directory, and then run the following command:

   ```
   $ unzip AWSDeviceFarmiOSReferenceApp.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the iOS application package is valid, it contains a single {{.app}} directory like {{AWSDeviceFarmiOSReferenceApp.app}} in this example.

   ```
   .
   `-- Payload (directory)
           `-- {{AWSDeviceFarmiOSReferenceApp.app}} (directory)
                         |-- Info.plist
                         `-- (any other files)
   ```

   For the layouts that Device Farm accepts, including the `.zip` layout for a simulator build, see [Packaging an iOS app](apps.md#test-runs-ios-app-packaging).

   For more information, see [iOS tests in AWS Device Farm](test-types-ios-tests.md).

### IOS\_APP\_PLIST\_FILE\_MISSING
<a name="IOS_APP_PLIST_FILE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find the Info.plist file inside the .app directory. Please unzip your application and then open the .app directory, verify that the Info.plist file is inside the directory, and try again.

In the following example, the package's name is **AWSDeviceFarmiOSReferenceApp.ipa**.

1. Copy your application package to your working directory, and then run the following command:

   ```
   $ unzip AWSDeviceFarmiOSReferenceApp.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the iOS application package is valid, you will find the {{Info.plist}} file inside the {{.app}} directory like {{AWSDeviceFarmiOSReferenceApp.app}} in our example.

   ```
   .
   `-- Payload (directory)
           `-- AWSDeviceFarmiOSReferenceApp.app (directory)
                         |-- {{Info.plist}}
                         `-- (any other files)
   ```

   For more information, see [iOS tests in AWS Device Farm](test-types-ios-tests.md).

### IOS\_APP\_CPU\_ARCHITECTURE\_VALUE\_MISSING
<a name="IOS_APP_CPU_ARCHITECTURE_VALUE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find the CPU architecture value in the Info.plist file. Please unzip your application and then open Info.plist file inside the .app directory, verify that the key "UIRequiredDeviceCapabilities" is specified, and try again.

In the following example, the package's name is **AWSDeviceFarmiOSReferenceApp.ipa**.

1. Copy your application package to your working directory, and then run the following command:

   ```
   $ unzip AWSDeviceFarmiOSReferenceApp.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find the {{Info.plist}} file inside an {{.app}} directory like {{AWSDeviceFarmiOSReferenceApp.app}} in our example:

   ```
   .
   `-- Payload (directory)
           `-- AWSDeviceFarmiOSReferenceApp.app (directory)
                         |-- {{Info.plist}}
                         `-- (any other files)
   ```

1. To find the CPU architecture value, you can open Info.plist using Xcode or Python.

   For Python, you can install the biplist module by running the following command:

   ```
   $ pip install biplist
   ```

1. Next, open Python and run the following command:

   ```
   import biplist
   info_plist = biplist.readPlist('Payload/AWSDeviceFarmiOSReferenceApp-cal.app/Info.plist')
   print info_plist['UIRequiredDeviceCapabilities']
   ```

   A valid iOS application package should produce output like the following:

   ```
   ['armv7']
   ```

   For more information, see [iOS tests in AWS Device Farm](test-types-ios-tests.md).

### IOS\_APP\_PLATFORM\_VALUE\_MISSING
<a name="IOS_APP_PLATFORM_VALUE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find the platform value in the Info.plist file. Please unzip your application and then open Info.plist file inside the .app directory, verify that the key "CFBundleSupportedPlatforms" is specified, and try again.

In the following example, the package's name is **AWSDeviceFarmiOSReferenceApp.ipa**.

1. Copy your application package to your working directory, and then run the following command:

   ```
   $ unzip AWSDeviceFarmiOSReferenceApp.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find the {{Info.plist}} file inside an {{.app}} directory like {{AWSDeviceFarmiOSReferenceApp.app}} in our example:

   ```
   .
   `-- Payload (directory)
           `-- AWSDeviceFarmiOSReferenceApp.app (directory)
                         |-- {{Info.plist}}
                         `-- (any other files)
   ```

1. To find the platform value, you can open Info.plist using Xcode or Python.

   For Python, you can install the biplist module by running the following command:

   ```
   $ pip install biplist
   ```

1. Next, open Python and run the following command:

   ```
   import biplist
   info_plist = biplist.readPlist('Payload/AWSDeviceFarmiOSReferenceApp-cal.app/Info.plist')
   print info_plist['CFBundleSupportedPlatforms']
   ```

   A valid iOS application package should produce output like the following:

   ```
   ['iPhoneOS']
   ```

   For more information, see [iOS tests in AWS Device Farm](test-types-ios-tests.md).

### IOS\_APP\_WRONG\_PLATFORM\_DEVICE\_VALUE
<a name="IOS_APP_WRONG_PLATFORM_DEVICE_VALUE"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not match the platform value in the Info.plist file to your IOS application package. Please unzip your IOS application package and then open Info.plist file inside the .app directory, verify that the value of the key "CFBundleSupportedPlatforms" names the platform your application was built for, and try again.

Device Farm tells a device build from a simulator build by the `CFBundleSupportedPlatforms` key, not the file name. For more information, see [Packaging an iOS app](apps.md#test-runs-ios-app-packaging).

In the following example, the package's name is **AWSDeviceFarmiOSReferenceApp.ipa**.

1. Copy your application package to your working directory, and then run the following command:

   ```
   $ unzip AWSDeviceFarmiOSReferenceApp.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find the {{Info.plist}} file inside an {{.app}} directory like {{AWSDeviceFarmiOSReferenceApp.app}} in our example:

   ```
   .
   `-- Payload (directory)
           `-- AWSDeviceFarmiOSReferenceApp.app (directory)
                         |-- {{Info.plist}}
                         `-- (any other files)
   ```

1. To find the platform value, you can open Info.plist using Xcode or Python.

   For Python, you can install the biplist module by running the following command:

   ```
   $ pip install biplist
   ```

1. Next, open Python and run the following command:

   ```
   import biplist
   info_plist = biplist.readPlist('Payload/AWSDeviceFarmiOSReferenceApp-cal.app/Info.plist')
   print info_plist['CFBundleSupportedPlatforms']
   ```

   A device build produces the following output:

   ```
   ['iPhoneOS']
   ```

   A simulator build produces the following output:

   ```
   ['iPhoneSimulator']
   ```

   For more information, see [iOS tests in AWS Device Farm](test-types-ios-tests.md).

### IOS\_APP\_WRONG\_PLATFORM\_SIMULATOR\_VALUE
<a name="IOS_APP_WRONG_PLATFORM_SIMULATOR_VALUE"></a>

If you see the following message, a device build has the {{.app}} directory at the root of the archive.

**Warning**  
We found the platform simulator value was wrong in the Info.plist file. A .app directory at the root of your IOS application package is treated as a simulator build. Please unzip your IOS application package and then open Info.plist file inside the .app directory, verify that the value of the key "CFBundleSupportedPlatforms" contains the keyword "simulator", and try again. If this is a device build, place the .app directory inside a Payload directory instead.

Package a device build as an `.ipa` file with the {{.app}} directory inside a `Payload` directory. For the layouts that Device Farm accepts, see [Packaging an iOS app](apps.md#test-runs-ios-app-packaging).

To confirm the platform that your application was built for, check the `CFBundleSupportedPlatforms` value as described in [IOS\_APP\_WRONG\_PLATFORM\_DEVICE\_VALUE](#IOS_APP_WRONG_PLATFORM_DEVICE_VALUE).

### IOS\_APP\_PLATFORM\_NAME\_MISMATCH
<a name="IOS_APP_PLATFORM_NAME_MISMATCH"></a>

If you see the following message, your upload succeeded with a warning.

**Warning**  
We found that the value of the key "DTPlatformName" in the Info.plist file does not name a simulator platform, although the key "CFBundleSupportedPlatforms" indicates a simulator build. This may cause some of your tests to not be executed correctly.

To check the value, open the `Info.plist` file inside the {{.app}} directory with Xcode or the biplist module, as described in [IOS\_APP\_WRONG\_PLATFORM\_DEVICE\_VALUE](#IOS_APP_WRONG_PLATFORM_DEVICE_VALUE). In a simulator build, the value of the key `DTPlatformName` is `iphonesimulator`.

### IOS\_APP\_FORM\_FACTOR\_VALUE\_MISSING
<a name="IOS_APP_FORM_FACTOR_VALUE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find the form factor value in the Info.plist file. Please unzip your application and then open Info.plist file inside the .app directory, verify that the key "UIDeviceFamily" is specified, and try again.

In the following example, the package's name is **AWSDeviceFarmiOSReferenceApp.ipa**.

1. Copy your application package to your working directory, and then run the following command:

   ```
   $ unzip AWSDeviceFarmiOSReferenceApp.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find the {{Info.plist}} file inside an {{.app}} directory like {{AWSDeviceFarmiOSReferenceApp.app}} in our example:

   ```
   .
   `-- Payload (directory)
           `-- AWSDeviceFarmiOSReferenceApp.app (directory)
                         |-- {{Info.plist}}
                         `-- (any other files)
   ```

1. To find the form factor value, you can open Info.plist using Xcode or Python.

   For Python, you can install the biplist module by running the following command:

   ```
   $ pip install biplist
   ```

1. Next, open Python and run the following command:

   ```
   import biplist
   info_plist = biplist.readPlist('Payload/AWSDeviceFarmiOSReferenceApp-cal.app/Info.plist')
   print info_plist['UIDeviceFamily']
   ```

   A valid iOS application package should produce output like the following:

   ```
   [1, 2]
   ```

   For more information, see [iOS tests in AWS Device Farm](test-types-ios-tests.md).

### IOS\_APP\_PACKAGE\_NAME\_VALUE\_MISSING
<a name="IOS_APP_PACKAGE_NAME_VALUE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find the package name value in the Info.plist file. Please unzip your application and then open Info.plist file inside the .app directory, verify that the key "CFBundleIdentifier" is specified, and try again.

In the following example, the package's name is **AWSDeviceFarmiOSReferenceApp.ipa**.

1. Copy your application package to your working directory, and then run the following command:

   ```
   $ unzip AWSDeviceFarmiOSReferenceApp.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find the {{Info.plist}} file inside an {{.app}} directory like {{AWSDeviceFarmiOSReferenceApp.app}} in our example:

   ```
   .
   `-- Payload (directory)
           `-- AWSDeviceFarmiOSReferenceApp.app (directory)
                         |-- {{Info.plist}}
                         `-- (any other files)
   ```

1. To find the package name value, you can open Info.plist using Xcode or Python.

   For Python, you can install the biplist module by running the following command:

   ```
   $ pip install biplist
   ```

1. Next, open Python and run the following command:

   ```
   import biplist
   info_plist = biplist.readPlist('Payload/AWSDeviceFarmiOSReferenceApp-cal.app/Info.plist')
   print info_plist['CFBundleIdentifier']
   ```

   A valid iOS application package should produce output like the following:

   ```
   Amazon.AWSDeviceFarmiOSReferenceApp
   ```

   For more information, see [iOS tests in AWS Device Farm](test-types-ios-tests.md).

### IOS\_APP\_EXECUTABLE\_VALUE\_MISSING
<a name="IOS_APP_EXECUTABLE_VALUE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find the executable value in the Info.plist file. Please unzip your application and then open Info.plist file inside the .app directory, verify that the key "CFBundleExecutable" is specified, and try again.

In the following example, the package's name is **AWSDeviceFarmiOSReferenceApp.ipa**.

1. Copy your application package to your working directory, and then run the following command:

   ```
   $ unzip AWSDeviceFarmiOSReferenceApp.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find the {{Info.plist}} file inside an {{.app}} directory like {{AWSDeviceFarmiOSReferenceApp.app}} in our example:

   ```
   .
   `-- Payload (directory)
           `-- AWSDeviceFarmiOSReferenceApp.app (directory)
                         |-- {{Info.plist}}
                         `-- (any other files)
   ```

1. To find the executable value, you can open Info.plist using Xcode or Python.

   For Python, you can install the biplist module by running the following command:

   ```
   $ pip install biplist
   ```

1. Next, open Python and run the following command:

   ```
   import biplist
   info_plist = biplist.readPlist('Payload/AWSDeviceFarmiOSReferenceApp-cal.app/Info.plist')
   print info_plist['CFBundleExecutable']
   ```

   A valid iOS application package should produce output like the following:

   ```
   AWSDeviceFarmiOSReferenceApp
   ```

   For more information, see [iOS tests in AWS Device Farm](test-types-ios-tests.md).

## Troubleshooting Appium Java JUnit tests in AWS Device Farm
<a name="troubleshooting-appium-java-junit"></a>

The following topic lists error messages that occur during the upload of Appium Java JUnit tests and recommends workarounds to resolve each error.

### APPIUM\_JAVA\_JUNIT\_TEST\_PACKAGE\_UNZIP\_FAILED
<a name="APPIUM_JAVA_JUNIT_TEST_PACKAGE_UNZIP_FAILED"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not open your test ZIP file. Please verify that the file is valid and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   A valid Appium Java JUnit package should produce output like the following:

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md).

### APPIUM\_JAVA\_JUNIT\_TEST\_PACKAGE\_DEPENDENCY\_DIR\_MISSING
<a name="APPIUM_JAVA_JUNIT_TEST_PACKAGE_DEPENDENCY_DIR_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find the dependency-jars directory inside your test package. Please unzip your test package, verify that the dependency-jars directory is inside the package, and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Java JUnit package is valid, you will find the {{dependency-jars}} directory inside the working directory:

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— {{dependency-jars}}  (this is the directory that contains all of your dependencies, built as JAR files)
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md).

### APPIUM\_JAVA\_JUNIT\_TEST\_PACKAGE\_JAR\_MISSING\_IN\_DEPENDENCY\_DIR
<a name="APPIUM_JAVA_JUNIT_TEST_PACKAGE_JAR_MISSING_IN_DEPENDENCY_DIR"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find a JAR file in the dependency-jars directory tree. Please unzip your test package and then open the dependency-jars directory, verify that at least one JAR file is in the directory, and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Java JUnit package is valid, you will find at least one {{jar}} file inside the {{dependency-jars}} directory:

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— {{com.some-dependency.bar-4.1.jar}}
         |— {{com.another-dependency.thing-1.0.jar}}
         |— {{joda-time-2.7.jar}}
         `— {{log4j-1.2.14.jar}}
   ```

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md).

### APPIUM\_JAVA\_JUNIT\_TEST\_PACKAGE\_TESTS\_JAR\_FILE\_MISSING
<a name="APPIUM_JAVA_JUNIT_TEST_PACKAGE_TESTS_JAR_FILE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find a \*-tests.jar file in your test package. Please unzip your test package, verify that at least one \*-tests.jar file is in the package, and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Java JUnit package is valid, you will find at least one {{jar}} file like {{acme-android-appium-1.0-SNAPSHOT-tests.jar}} in our example. The file's name may be different, but it should end with {{–tests.jar}}.

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— {{acme-android-appium-1.0-SNAPSHOT-tests.jar}} (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md).

### APPIUM\_JAVA\_JUNIT\_TEST\_PACKAGE\_CLASS\_FILE\_MISSING\_IN\_TESTS\_JAR
<a name="APPIUM_JAVA_JUNIT_TEST_PACKAGE_CLASS_FILE_MISSING_IN_TESTS_JAR"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find a class file within the tests JAR file. Please unzip your test package and then unjar the tests JAR file, verify that at least one class file is within the JAR file, and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find at least one jar file like {{acme-android-appium-1.0-SNAPSHOT-tests.jar}} in our example. The file's name may be different, but it should end with {{–tests.jar}}.

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— {{acme-android-appium-1.0-SNAPSHOT-tests.jar}} (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

1. After you successfully extract the files, you should find at least one class in the working directory tree by running the command: 

   ```
   $ tree .
   ```

   You should see output like this:

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing 
   everything built from the ./src/test directory)
   |- {{one-class-file.class}}
   |- folder
   |    `-{{another-class-file.class}}
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md).

### APPIUM\_JAVA\_JUNIT\_TEST\_PACKAGE\_JUNIT\_VERSION\_VALUE\_UNKNOWN
<a name="APPIUM_JAVA_JUNIT_TEST_PACKAGE_JUNIT_VERSION_VALUE_UNKNOWN"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find a JUnit version value. Please unzip your test package and open the dependency-jars directory, verify that the JUnit JAR file is inside the directory, and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working-directory tree structure by running the following command:

   ```
   tree .
   ```

   The output should look like this:

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
       |— {{junit-4.10.jar}}
       |— com.some-dependency.bar-4.1.jar
       |— com.another-dependency.thing-1.0.jar
       |— joda-time-2.7.jar
       `— log4j-1.2.14.jar
   ```

   If the Appium Java JUnit package is valid, you will find the JUnit dependency file that is similar to the jar file {{junit-4.10.jar}} in our example. The name should consist of the keyword {{junit}} and its version number, which in this example is 4.10.

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md).

### APPIUM\_JAVA\_JUNIT\_TEST\_PACKAGE\_INVALID\_JUNIT\_VERSION
<a name="APPIUM_JAVA_JUNIT_TEST_PACKAGE_INVALID_JUNIT_VERSION"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We found the JUnit version was lower than the minimum version 4.10 we support. Please change the JUnit version and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find a JUnit dependency file like {{junit-4.10.jar}} in our example and its version number, which in our example is 4.10:

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars (this is the directory that contains all of your dependencies, built as JAR files)
         |— {{junit-4.10.jar}}
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```
**Note**  
Your tests may not execute correctly if the JUnit version specified in your test package is lower than the minimum version 4.10 we support.

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md).

## Troubleshooting Appium Java JUnit web application tests in AWS Device Farm
<a name="troubleshooting-appium-web-java-junit-tests"></a>

The following topic lists error messages that can occur for Appium Java JUnit Web application tests and recommends workarounds to resolve each error. For more information on using Appium with Device Farm, see [Automatically run Appium tests in Device Farm](test-types-appium.md).

### APPIUM\_WEB\_JAVA\_JUNIT\_TEST\_PACKAGE\_UNZIP\_FAILED
<a name="APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE_UNZIP_FAILED"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not open your test ZIP file. Please verify that the file is valid and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   A valid Appium Java JUnit package should produce output like the following:

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

### APPIUM\_WEB\_JAVA\_JUNIT\_TEST\_PACKAGE\_DEPENDENCY\_DIR\_MISSING
<a name="APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE_DEPENDENCY_DIR_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find the dependency-jars directory inside your test package. Please unzip your test package, verify that the dependency-jars directory is inside the package, and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Java JUnit package is valid, you will find the {{dependency-jars}} directory inside the working directory:

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— {{dependency-jars}}  (this is the directory that contains all of your dependencies, built as JAR files)
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

### APPIUM\_WEB\_JAVA\_JUNIT\_TEST\_PACKAGE\_JAR\_MISSING\_IN\_DEPENDENCY\_DIR
<a name="APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE_JAR_MISSING_IN_DEPENDENCY_DIR"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find a JAR file in the dependency-jars directory tree. Please unzip your test package and then open the dependency-jars directory, verify that at least one JAR file is in the directory, and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Java JUnit package is valid, you will find at least one {{jar}} file inside the {{dependency-jars}} directory:

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— {{com.some-dependency.bar-4.1.jar}}
         |— {{com.another-dependency.thing-1.0.jar}}
         |— {{joda-time-2.7.jar}}
         `— {{log4j-1.2.14.jar}}
   ```

### APPIUM\_WEB\_JAVA\_JUNIT\_TEST\_PACKAGE\_TESTS\_JAR\_FILE\_MISSING
<a name="APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE_TESTS_JAR_FILE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find a \*-tests.jar file in your test package. Please unzip your test package, verify that at least one \*-tests.jar file is in the package, and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Java JUnit package is valid, you will find at least one {{jar}} file like {{acme-android-appium-1.0-SNAPSHOT-tests.jar}} in our example. The file's name may be different, but it should end with {{–tests.jar}}.

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— {{acme-android-appium-1.0-SNAPSHOT-tests.jar}} (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

### APPIUM\_WEB\_JAVA\_JUNIT\_TEST\_PACKAGE\_CLASS\_FILE\_MISSING\_IN\_TESTS\_JAR
<a name="APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE_CLASS_FILE_MISSING_IN_TESTS_JAR"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find a class file within the tests JAR file. Please unzip your test package and then unjar the tests JAR file, verify that at least one class file is within the JAR file, and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find at least one jar file like {{acme-android-appium-1.0-SNAPSHOT-tests.jar}} in our example. The file's name may be different, but it should end with {{–tests.jar}}.

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— {{acme-android-appium-1.0-SNAPSHOT-tests.jar}} (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

1. After you successfully extract the files, you should find at least one class in the working directory tree by running the command: 

   ```
   $ tree .
   ```

   You should see output like this:

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing 
   everything built from the ./src/test directory)
   |- {{one-class-file.class}}
   |- folder
   |    `-{{another-class-file.class}}
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

### APPIUM\_WEB\_JAVA\_JUNIT\_TEST\_PACKAGE\_JUNIT\_VERSION\_VALUE\_UNKNOWN
<a name="APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE_JUNIT_VERSION_VALUE_UNKNOWN"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find a JUnit version value. Please unzip your test package and open the dependency-jars directory, verify that the JUnit JAR file is inside the directory, and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working-directory tree structure by running the following command:

   ```
   tree .
   ```

   The output should look like this:

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— {{junit-4.10.jar}}
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

   If the Appium Java JUnit package is valid, you will find the JUnit dependency file that is similar to the jar file {{junit-4.10.jar}} in our example. The name should consist of the keyword {{junit}} and its version number, which in this example is 4.10.

### APPIUM\_WEB\_JAVA\_JUNIT\_TEST\_PACKAGE\_INVALID\_JUNIT\_VERSION
<a name="APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE_INVALID_JUNIT_VERSION"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We found the JUnit version was lower than the minimum version 4.10 we support. Please change the JUnit version and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find a JUnit dependency file like {{junit-4.10.jar}} in our example and its version number, which in our example is 4.10:

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars (this is the directory that contains all of your dependencies, built as JAR files)
         |— {{junit-4.10.jar}}
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```
**Note**  
Your tests may not execute correctly if the JUnit version specified in your test package is lower than the minimum version 4.10 we support.

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md).

## Troubleshooting Appium Java TestNG tests in AWS Device Farm
<a name="troubleshooting-appium-java-testng"></a>

The following topic lists error messages that occur during the upload of Appium Java TestNG tests and recommends workarounds to resolve each error.

### Upload errors
<a name="troubleshooting-appium-java-testng-upload"></a>

The following errors can occur when you upload your Appium Java TestNG tests.

#### APPIUM\_JAVA\_TESTNG\_TEST\_PACKAGE\_UNZIP\_FAILED
<a name="APPIUM_JAVA_TESTNG_TEST_PACKAGE_UNZIP_FAILED"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not open your test ZIP file. Please verify that the file is valid and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   A valid Appium Java JUnit package should produce output like the following:

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md).

#### APPIUM\_JAVA\_TESTNG\_TEST\_PACKAGE\_DEPENDENCY\_DIR\_MISSING
<a name="APPIUM_JAVA_TESTNG_TEST_PACKAGE_DEPENDENCY_DIR_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find the `dependency-jars` directory inside your test package. Please unzip your test package, verify that the `dependency-jars` directory is inside the package, and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Java JUnit package is valid, you will find the {{dependency-jars}} directory inside the working directory.

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— {{dependency-jars}}  (this is the directory that contains all of your dependencies, built as JAR files)
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md).

#### APPIUM\_JAVA\_TESTNG\_TEST\_PACKAGE\_JAR\_MISSING\_IN\_DEPENDENCY\_DIR
<a name="APPIUM_JAVA_TESTNG_TEST_PACKAGE_JAR_MISSING_IN_DEPENDENCY_DIR"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find a JAR file in the dependency-jars directory tree. Please unzip your test package and then open the dependency-jars directory, verify that at least one JAR file is in the directory, and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Java JUnit package is valid, you will find at least one {{jar}} file inside the {{dependency-jars}} directory. 

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— {{com.some-dependency.bar-4.1.jar}}
         |— {{com.another-dependency.thing-1.0.jar}}
         |— {{joda-time-2.7.jar}}
         `— {{log4j-1.2.14.jar}}
   ```

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md).

#### APPIUM\_JAVA\_TESTNG\_TEST\_PACKAGE\_TESTS\_JAR\_FILE\_MISSING
<a name="APPIUM_JAVA_TESTNG_TEST_PACKAGE_TESTS_JAR_FILE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find a \*-tests.jar file in your test package. Please unzip your test package, verify that at least one \*-tests.jar file is in the package, and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Java JUnit package is valid, you will find at least one {{jar}} file like {{acme-android-appium-1.0-SNAPSHOT-tests.jar}} in our example. The file's name may be different, but it should end with {{–tests.jar}}.

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— {{acme-android-appium-1.0-SNAPSHOT-tests.jar}} (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md).

#### APPIUM\_JAVA\_TESTNG\_TEST\_PACKAGE\_CLASS\_FILE\_MISSING\_IN\_TESTS\_JAR
<a name="APPIUM_JAVA_TESTNG_TEST_PACKAGE_CLASS_FILE_MISSING_IN_TESTS_JAR"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find a class file within the tests JAR file. Please unzip your test package and then unjar the tests JAR file, verify that at least one class file is within the JAR file, and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find at least one jar file like {{acme-android-appium-1.0-SNAPSHOT-tests.jar}} in our example. The file's name may be different, but it should end with {{–tests.jar}}.

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— {{acme-android-appium-1.0-SNAPSHOT-tests.jar}} (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

1. To extract files from the jar file, you can run the following command: 

   ```
   $ jar xf acme-android-appium-1.0-SNAPSHOT-tests.jar
   ```

1. After you successfully extract the files, run the following command:

   ```
   $ tree .
   ```

   You should find at least one class in the working directory tree:

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing 
   everything built from the ./src/test directory)
   |- {{one-class-file.class}}
   |- folder
   |    `— {{another-class-file.class}}
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md).

## Troubleshooting Appium Java TestNG web applications in AWS Device Farm
<a name="troubleshooting-appium-web-java-testng"></a>

The following topic lists error messages that can occur for Appium Java TestNG Web application tests and recommends workarounds to resolve each error.

### APPIUM\_WEB\_JAVA\_TESTNG\_TEST\_PACKAGE\_UNZIP\_FAILED
<a name="APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE_UNZIP_FAILED"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not open your test ZIP file. Please verify that the file is valid and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   A valid Appium Java JUnit package should produce output like the following:

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md).

### APPIUM\_WEB\_JAVA\_TESTNG\_TEST\_PACKAGE\_DEPENDENCY\_DIR\_MISSING
<a name="APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE_DEPENDENCY_DIR_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find the dependency-jars directory inside your test package. Please unzip your test package, verify that the dependency-jars directory is inside the package, and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Java JUnit package is valid, you will find the {{dependency-jars}} directory inside the working directory.

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— {{dependency-jars}}  (this is the directory that contains all of your dependencies, built as JAR files)
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md).

### APPIUM\_WEB\_JAVA\_TESTNG\_TEST\_PACKAGE\_JAR\_MISSING\_IN\_DEPENDENCY\_DIR
<a name="APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE_JAR_MISSING_IN_DEPENDENCY_DIR"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find a JAR file in the dependency-jars directory tree. Please unzip your test package and then open the dependency-jars directory, verify that at least one JAR file is in the directory, and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Java JUnit package is valid, you will find at least one {{jar}} file inside the {{dependency-jars}} directory. 

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— {{com.some-dependency.bar-4.1.jar}}
         |— {{com.another-dependency.thing-1.0.jar}}
         |— {{joda-time-2.7.jar}}
         `— {{log4j-1.2.14.jar}}
   ```

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md).

### APPIUM\_WEB\_JAVA\_TESTNG\_TEST\_PACKAGE\_TESTS\_JAR\_FILE\_MISSING
<a name="APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE_TESTS_JAR_FILE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find a \*-tests.jar file in your test package. Please unzip your test package, verify that at least one \*-tests.jar file is in the package, and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Java JUnit package is valid, you will find at least one {{jar}} file like {{acme-android-appium-1.0-SNAPSHOT-tests.jar}} in our example. The file's name may be different, but it should end with {{–tests.jar}}.

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— {{acme-android-appium-1.0-SNAPSHOT-tests.jar}} (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md).

### APPIUM\_WEB\_JAVA\_TESTNG\_TEST\_PACKAGE\_CLASS\_FILE\_MISSING\_IN\_TESTS\_JAR
<a name="APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE_CLASS_FILE_MISSING_IN_TESTS_JAR"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find a class file within the tests JAR file. Please unzip your test package and then unjar the tests JAR file, verify that at least one class file is within the JAR file, and try again.

In the following example, the package's name is **zip-with-dependencies.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip zip-with-dependencies.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find at least one jar file like {{acme-android-appium-1.0-SNAPSHOT-tests.jar}} in our example. The file's name may be different, but it should end with {{–tests.jar}}.

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— {{acme-android-appium-1.0-SNAPSHOT-tests.jar}} (this is the JAR containing everything built from the ./src/test directory)
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

1. To extract files from the jar file, you can run the following command: 

   ```
   $ jar xf acme-android-appium-1.0-SNAPSHOT-tests.jar
   ```

1. After you successfully extract the files, run the following command:

   ```
   $ tree .
   ```

   You should find at least one class in the working directory tree:

   ```
   .
   |— acme-android-appium-1.0-SNAPSHOT.jar (this is the JAR containing everything built from the ./src/main directory)
   |— acme-android-appium-1.0-SNAPSHOT-tests.jar (this is the JAR containing 
   everything built from the ./src/test directory)
   |- {{one-class-file.class}}
   |- folder
   |    `— {{another-class-file.class}}
   |— zip-with-dependencies.zip (this .zip file contains all of the items)
   `— dependency-jars  (this is the directory that contains all of your dependencies, built as JAR files)
         |— com.some-dependency.bar-4.1.jar
         |— com.another-dependency.thing-1.0.jar
         |— joda-time-2.7.jar
         `— log4j-1.2.14.jar
   ```

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md).

## Troubleshooting Appium Python tests in AWS Device Farm
<a name="troubleshooting-appium-python"></a>

The following topic lists error messages that occur during the upload of Appium Python tests and recommends workarounds to resolve each error.

### APPIUM\_PYTHON\_TEST\_PACKAGE\_UNZIP\_FAILED
<a name="APPIUM_PYTHON_TEST_PACKAGE_UNZIP_FAILED"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not open your Appium test ZIP file. Please verify that the file is valid and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   A valid Appium Python package should produce output like the following:

   ```
   .
   |-- requirements.txt
   |-- test_bundle.zip
   |-- tests (directory)
   |      `-- test_unittest.py
   `-- wheelhouse (directory)
          |-- Appium_Python_Client-0.20-cp27-none-any.whl
          |-- py-1.4.31-py2.py3-none-any.whl
          |-- pytest-2.9.0-py2.py3-none-any.whl
          |-- selenium-2.52.0-cp27-none-any.whl
          `-- wheel-0.26.0-py2.py3-none-any.whl
   ```

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md). 

### APPIUM\_PYTHON\_TEST\_PACKAGE\_DEPENDENCY\_WHEEL\_MISSING
<a name="APPIUM_PYTHON_TEST_PACKAGE_DEPENDENCY_WHEEL_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find a dependency wheel file in the wheelhouse directory tree. Please unzip your test package and then open the wheelhouse directory, verify that at least one wheel file is in the directory, and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Python package is valid, you will find at least one {{.whl}} dependent file like the highlighted files inside the {{wheelhouse}} directory.

   ```
   .
   |-- requirements.txt
   |-- test_bundle.zip
   |-- tests (directory)
   |      `-- test_unittest.py
   `-- wheelhouse (directory)
          |-- {{Appium_Python_Client-0.20-cp27-none-any.whl}}
          |-- {{py-1.4.31-py2.py3-none-any.whl}}
          |-- {{pytest-2.9.0-py2.py3-none-any.whl}}
          |-- {{selenium-2.52.0-cp27-none-any.whl}}
          `-- {{wheel-0.26.0-py2.py3-none-any.whl}}
   ```

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md). 

### APPIUM\_PYTHON\_TEST\_PACKAGE\_INVALID\_PLATFORM
<a name="APPIUM_PYTHON_TEST_PACKAGE_INVALID_PLATFORM"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We found at least one wheel file specified a platform that we do not support. Please unzip your test package and then open the wheelhouse directory, verify that names of wheel files end with -any.whl or -linux\_x86\_64.whl, and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Python package is valid, you will find at least one {{.whl}} dependent file like the highlighted files inside the {{wheelhouse}} directory. The file's name may be different, but it should end with {{-any.whl}} or {{-linux\_x86\_64.whl}}, which specifies the platform. Any other platforms like `windows` are not supported.

   ```
   .
   |-- requirements.txt
   |-- test_bundle.zip
   |-- tests (directory)
   |      `-- test_unittest.py
   `-- wheelhouse (directory)
          |-- {{Appium_Python_Client-0.20-cp27-none-any.whl}}
          |-- {{py-1.4.31-py2.py3-none-any.whl}}
          |-- {{pytest-2.9.0-py2.py3-none-any.whl}}
          |-- {{selenium-2.52.0-cp27-none-any.whl}}
          `-- {{wheel-0.26.0-py2.py3-none-any.whl}}
   ```

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md). 

### APPIUM\_PYTHON\_TEST\_PACKAGE\_TEST\_DIR\_MISSING
<a name="APPIUM_PYTHON_TEST_PACKAGE_TEST_DIR_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find the tests directory inside your test package. Please unzip your test package, verify that the tests directory is inside the package, and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Python package is valid, you will find the {{tests}} directory inside the working directory.

   ```
   .
   |-- requirements.txt
   |-- test_bundle.zip
   |-- {{tests}} (directory)
   |      `-- test_unittest.py
   `-- wheelhouse (directory)
          |-- Appium_Python_Client-0.20-cp27-none-any.whl
          |-- py-1.4.31-py2.py3-none-any.whl
          |-- pytest-2.9.0-py2.py3-none-any.whl
          |-- selenium-2.52.0-cp27-none-any.whl
          `-- wheel-0.26.0-py2.py3-none-any.whl
   ```

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md). 

### APPIUM\_PYTHON\_TEST\_PACKAGE\_INVALID\_TEST\_FILE\_NAME
<a name="APPIUM_PYTHON_TEST_PACKAGE_INVALID_TEST_FILE_NAME"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find a valid test file in the tests directory tree. Please unzip your test package and then open the tests directory, verify that at least one file's name starts or ends with the keyword "test", and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Python package is valid, you will find the {{tests}} directory inside the working directory. The file's name may be different, but it should start with {{test\_}} or end with {{\_test.py}}.

   ```
   .
   |-- requirements.txt
   |-- test_bundle.zip
   |-- tests (directory)
   |      `-- {{test_unittest.py}}
   `-- wheelhouse (directory)
          |-- Appium_Python_Client-0.20-cp27-none-any.whl
          |-- py-1.4.31-py2.py3-none-any.whl
          |-- pytest-2.9.0-py2.py3-none-any.whl
          |-- selenium-2.52.0-cp27-none-any.whl
          `-- wheel-0.26.0-py2.py3-none-any.whl
   ```

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md). 

### APPIUM\_PYTHON\_TEST\_PACKAGE\_REQUIREMENTS\_TXT\_FILE\_MISSING
<a name="APPIUM_PYTHON_TEST_PACKAGE_REQUIREMENTS_TXT_FILE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find the requirements.txt file inside your test package. Please unzip your test package, verify that the requirements.txt file is inside the package, and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Python package is valid, you will find the {{requirements.txt}} file inside the working directory.

   ```
   .
   |-- {{requirements.txt}}
   |-- test_bundle.zip
   |-- tests (directory)
   |      `-- test_unittest.py
   `-- wheelhouse (directory)
          |-- Appium_Python_Client-0.20-cp27-none-any.whl
          |-- py-1.4.31-py2.py3-none-any.whl
          |-- pytest-2.9.0-py2.py3-none-any.whl
          |-- selenium-2.52.0-cp27-none-any.whl
          `-- wheel-0.26.0-py2.py3-none-any.whl
   ```

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md). 

### APPIUM\_PYTHON\_TEST\_PACKAGE\_INVALID\_PYTEST\_VERSION
<a name="APPIUM_PYTHON_TEST_PACKAGE_INVALID_PYTEST_VERSION"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We found the pytest version was lower than the minimum version 2.8.0 we support. Please change the pytest version inside the requirements.txt file, and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find the {{requirements.txt}} file inside the working directory.

   ```
   .
   |-- {{requirements.txt}}
   |-- test_bundle.zip
   |-- tests (directory)
   |      `--test_unittest.py
   `-- wheelhouse (directory)
          |-- Appium_Python_Client-0.20-cp27-none-any.whl
          |-- py-1.4.31-py2.py3-none-any.whl
          |-- pytest-2.9.0-py2.py3-none-any.whl
          |-- selenium-2.52.0-cp27-none-any.whl
          `-- wheel-0.26.0-py2.py3-none-any.whl
   ```

1. To get the pytest version, you can run the following command:

   ```
   $ grep "pytest" requirements.txt
   ```

   You should find output like the following:

   ```
   pytest==2.9.0
   ```

   It shows the pytest version, which in this example is 2.9.0. If the Appium Python package is valid, the pytest version should be larger than or equal to 2.8.0. 

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md). 

### APPIUM\_PYTHON\_TEST\_PACKAGE\_INSTALL\_DEPENDENCY\_WHEELS\_FAILED
<a name="APPIUM_PYTHON_TEST_PACKAGE_INSTALL_DEPENDENCY_WHEELS_FAILED"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We failed to install the dependency wheels. Please unzip your test package and then open the requirements.txt file and the wheelhouse directory, verify that the dependency wheels specified in the requirements.txt file exactly match the dependency wheels inside the wheelhouse directory, and try again.

We strongly recommend that you set up [Python virtualenv](https://pypi.python.org/pypi/virtualenv) for packaging tests. Here is an example flow of creating a virtual environment using Python virtualenv and then activating it:

```
$ virtualenv workspace
$ cd workspace 
$ source bin/activate
```

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. To test installing wheel files, you can run the following command:

   ```
   $ pip install --use-wheel --no-index --find-links=./wheelhouse --requirement=./requirements.txt
   ```

   A valid Appium Python package should produce output like the following:

   ```
   Ignoring indexes: https://pypi.python.org/simple
   Collecting Appium-Python-Client==0.20 (from -r ./requirements.txt (line 1))
   Collecting py==1.4.31 (from -r ./requirements.txt (line 2))
   Collecting pytest==2.9.0 (from -r ./requirements.txt (line 3))
   Collecting selenium==2.52.0 (from -r ./requirements.txt (line 4))
   Collecting wheel==0.26.0 (from -r ./requirements.txt (line 5))
   Installing collected packages: selenium, Appium-Python-Client, py, pytest, wheel
     Found existing installation: wheel 0.29.0
       Uninstalling wheel-0.29.0:
         Successfully uninstalled wheel-0.29.0
   Successfully installed Appium-Python-Client-0.20 py-1.4.31 pytest-2.9.0 selenium-2.52.0 wheel-0.26.0
   ```

1. To deactivate the virtual environment, you can run the following command:

   ```
   $ deactivate
   ```

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md). 

### APPIUM\_PYTHON\_TEST\_PACKAGE\_PYTEST\_COLLECT\_FAILED
<a name="APPIUM_PYTHON_TEST_PACKAGE_PYTEST_COLLECT_FAILED"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We failed to collect tests in the tests directory. Please unzip your test package, very that the test package is valid by running the command `py.test --collect-only <path to your tests directory>`, and try again after the command does not print any error. 

We strongly recommend that you set up [Python virtualenv](https://pypi.python.org/pypi/virtualenv) for packaging tests. Here is an example flow of creating a virtual environment using Python virtualenv and then activating it:

```
$ virtualenv workspace
$ cd workspace 
$ source bin/activate
```

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. To install wheel files, you can run the following command:

   ```
   $ pip install --use-wheel --no-index --find-links=./wheelhouse --requirement=./requirements.txt
   ```

1. To collect tests, you can run the following command:

   ```
   $ py.test --collect-only tests
   ```

   A valid Appium Python package should produce output like the following:

   ```
   ==================== test session starts ====================
   platform darwin -- Python 2.7.11, pytest-2.9.0, py-1.4.31, pluggy-0.3.1
   rootdir: /Users/zhena/Desktop/Ios/tests, inifile:
   collected 1 items
   <Module 'test_unittest.py'>
     <UnitTestCase 'DeviceFarmAppiumWebTests'>
       <TestCaseFunction 'test_devicefarm'>
   
   ==================== no tests ran in 0.11 seconds ====================
   ```

1. To deactivate the virtual environment, you can run the following command:

   ```
   $ deactivate
   ```

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md). 

### APPIUM\_PYTHON\_TEST\_PACKAGE\_DEPENDENCY\_WHEELS\_INSUFFICIENT
<a name="APPIUM_PYTHON_TEST_PACKAGE_DEPENDENCY_WHEELS_INSUFFICIENT"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find enough wheel dependencies in the wheelhouse directory. Please unzip your test package, and then open the wheelhouse directory. Verify that you have all the wheel dependencies specified in the requirements.txt file.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. Check the length of the {{requirements.txt}} file as well as the number of {{.whl}} dependent files in the wheelhouse directory:

   ```
   $ cat requirements.txt | egrep "." |wc -l
   ﻿    12
   $ ls wheelhouse/ | egrep ".+\.whl" | wc -l
       11
   ```

   If the number of {{.whl}} dependent files is less than the number of non-empty rows in your {{requirements.txt}} file, then you need to ensure the following: 
   + There is a {{.whl}} dependent file corresponding to each row in the {{requirements.txt}} file.
   + There are no other lines in the {{requirements.txt}} file that contain information other than the dependency package names.
   + No dependency names are duplicated in multiple lines in the {{requirements.txt}} file such that two lines in the file may correspond to one {{.whl}} dependent file.

   AWS Device Farm doesn't support lines in the {{requirements.txt}} file that don't directly correspond to dependency packages, such as lines that specify global options for the `pip install` command. See [Requirements file format](https://pip.pypa.io/en/stable/reference/requirements-file-format/#global-options) for a list of global options.

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md). 

## Troubleshooting Appium Python web application tests in AWS Device Farm
<a name="troubleshooting-appium-web-python"></a>

The following topic lists error messages that can occur for Appium Python Web application tests and recommends workarounds to resolve each error.

### APPIUM\_WEB\_PYTHON\_TEST\_PACKAGE\_UNZIP\_FAILED
<a name="APPIUM_WEB_PYTHON_TEST_PACKAGE_UNZIP_FAILED"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not open your Appium test ZIP file. Please verify that the file is valid and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   A valid Appium Python package should produce output like the following:

   ```
   .
   |-- requirements.txt
   |-- test_bundle.zip
   |-- tests (directory)
   |      `-- test_unittest.py
   `-- wheelhouse (directory)
          |-- Appium_Python_Client-0.20-cp27-none-any.whl
          |-- py-1.4.31-py2.py3-none-any.whl
          |-- pytest-2.9.0-py2.py3-none-any.whl
          |-- selenium-2.52.0-cp27-none-any.whl
          `-- wheel-0.26.0-py2.py3-none-any.whl
   ```

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md). 

### APPIUM\_WEB\_PYTHON\_TEST\_PACKAGE\_DEPENDENCY\_WHEEL\_MISSING
<a name="APPIUM_WEB_PYTHON_TEST_PACKAGE_DEPENDENCY_WHEEL_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find a dependency wheel file in the wheelhouse directory tree. Please unzip your test package and then open the wheelhouse directory, verify that at least one wheel file is in the directory, and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Python package is valid, you will find at least one {{.whl}} dependent file like the highlighted files inside the {{wheelhouse}} directory.

   ```
   .
   |-- requirements.txt
   |-- test_bundle.zip
   |-- tests (directory)
   |      `-- test_unittest.py
   `-- wheelhouse (directory)
          |-- {{Appium_Python_Client-0.20-cp27-none-any.whl}}
          |-- {{py-1.4.31-py2.py3-none-any.whl}}
          |-- {{pytest-2.9.0-py2.py3-none-any.whl}}
          |-- {{selenium-2.52.0-cp27-none-any.whl}}
          `-- {{wheel-0.26.0-py2.py3-none-any.whl}}
   ```

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md). 

### APPIUM\_WEB\_PYTHON\_TEST\_PACKAGE\_INVALID\_PLATFORM
<a name="APPIUM_WEB_PYTHON_TEST_PACKAGE_INVALID_PLATFORM"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We found at least one wheel file specified a platform that we do not support. Please unzip your test package and then open the wheelhouse directory, verify that names of wheel files end with -any.whl or -linux\_x86\_64.whl, and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Python package is valid, you will find at least one {{.whl}} dependent file like the highlighted files inside the {{wheelhouse}} directory. The file's name may be different, but it should end with {{-any.whl}} or {{-linux\_x86\_64.whl}}, which specifies the platform. Any other platforms like `windows` are not supported.

   ```
   .
   |-- requirements.txt
   |-- test_bundle.zip
   |-- tests (directory)
   |      `-- test_unittest.py
   `-- wheelhouse (directory)
          |-- {{Appium_Python_Client-0.20-cp27-none-any.whl}}
          |-- {{py-1.4.31-py2.py3-none-any.whl}}
          |-- {{pytest-2.9.0-py2.py3-none-any.whl}}
          |-- {{selenium-2.52.0-cp27-none-any.whl}}
          `-- {{wheel-0.26.0-py2.py3-none-any.whl}}
   ```

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md). 

### APPIUM\_WEB\_PYTHON\_TEST\_PACKAGE\_TEST\_DIR\_MISSING
<a name="APPIUM_WEB_PYTHON_TEST_PACKAGE_TEST_DIR_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find the tests directory inside your test package. Please unzip your test package, verify that the tests directory is inside the package, and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Python package is valid, you will find the {{tests}} directory inside the working directory.

   ```
   .
   |-- requirements.txt
   |-- test_bundle.zip
   |-- {{tests}} (directory)
   |      `-- test_unittest.py
   `-- wheelhouse (directory)
          |-- Appium_Python_Client-0.20-cp27-none-any.whl
          |-- py-1.4.31-py2.py3-none-any.whl
          |-- pytest-2.9.0-py2.py3-none-any.whl
          |-- selenium-2.52.0-cp27-none-any.whl
          `-- wheel-0.26.0-py2.py3-none-any.whl
   ```

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md). 

### APPIUM\_WEB\_PYTHON\_TEST\_PACKAGE\_INVALID\_TEST\_FILE\_NAME
<a name="APPIUM_WEB_PYTHON_TEST_PACKAGE_INVALID_TEST_FILE_NAME"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find a valid test file in the tests directory tree. Please unzip your test package and then open the tests directory, verify that at least one file's name starts or ends with the keyword "test", and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Python package is valid, you will find the {{tests}} directory inside the working directory. The file's name may be different, but it should start with {{test\_}} or end with {{\_test.py}}.

   ```
   .
   |-- requirements.txt
   |-- test_bundle.zip
   |-- tests (directory)
   |      `-- {{test_unittest.py}}
   `-- wheelhouse (directory)
          |-- Appium_Python_Client-0.20-cp27-none-any.whl
          |-- py-1.4.31-py2.py3-none-any.whl
          |-- pytest-2.9.0-py2.py3-none-any.whl
          |-- selenium-2.52.0-cp27-none-any.whl
          `-- wheel-0.26.0-py2.py3-none-any.whl
   ```

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md). 

### APPIUM\_WEB\_PYTHON\_TEST\_PACKAGE\_REQUIREMENTS\_TXT\_FILE\_MISSING
<a name="APPIUM_WEB_PYTHON_TEST_PACKAGE_REQUIREMENTS_TXT_FILE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find the requirements.txt file inside your test package. Please unzip your test package, verify that the requirements.txt file is inside the package, and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the Appium Python package is valid, you will find the {{requirements.txt}} file inside the working directory.

   ```
   .
   |-- {{requirements.txt}}
   |-- test_bundle.zip
   |-- tests (directory)
   |      `-- test_unittest.py
   `-- wheelhouse (directory)
          |-- Appium_Python_Client-0.20-cp27-none-any.whl
          |-- py-1.4.31-py2.py3-none-any.whl
          |-- pytest-2.9.0-py2.py3-none-any.whl
          |-- selenium-2.52.0-cp27-none-any.whl
          `-- wheel-0.26.0-py2.py3-none-any.whl
   ```

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md). 

### APPIUM\_WEB\_PYTHON\_TEST\_PACKAGE\_INVALID\_PYTEST\_VERSION
<a name="APPIUM_WEB_PYTHON_TEST_PACKAGE_INVALID_PYTEST_VERSION"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We found the pytest version was lower than the minimum version 2.8.0 we support. Please change the pytest version inside the requirements.txt file, and try again.

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find the {{requirement.txt}} file inside the working directory.

   ```
   .
   |-- {{requirements.txt}}
   |-- test_bundle.zip
   |-- tests (directory)
   |      `--test_unittest.py
   `-- wheelhouse (directory)
          |-- Appium_Python_Client-0.20-cp27-none-any.whl
          |-- py-1.4.31-py2.py3-none-any.whl
          |-- pytest-2.9.0-py2.py3-none-any.whl
          |-- selenium-2.52.0-cp27-none-any.whl
          `-- wheel-0.26.0-py2.py3-none-any.whl
   ```

1. To get the pytest version, you can run the following command:

   ```
   $ grep "pytest" requirements.txt
   ```

   You should find output like the following:

   ```
   pytest==2.9.0
   ```

   It shows the pytest version, which in this example is 2.9.0. If the Appium Python package is valid, the pytest version should be larger than or equal to 2.8.0. 

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md). 

### APPIUM\_WEB\_PYTHON\_TEST\_PACKAGE\_INSTALL\_DEPENDENCY\_WHEELS\_FAILED
<a name="APPIUM_WEB_PYTHON_TEST_PACKAGE_INSTALL_DEPENDENCY_WHEELS_FAILED"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We failed to install the dependency wheels. Please unzip your test package and then open the requirements.txt file and the wheelhouse directory, verify that the dependency wheels specified in the requirements.txt file exactly match the dependency wheels inside the wheelhouse directory, and try again.

We strongly recommend that you set up [Python virtualenv](https://pypi.python.org/pypi/virtualenv) for packaging tests. Here is an example flow of creating a virtual environment using Python virtualenv and then activating it:

```
$ virtualenv workspace
$ cd workspace 
$ source bin/activate
```

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. To test installing wheel files, you can run the following command:

   ```
   $ pip install --use-wheel --no-index --find-links=./wheelhouse --requirement=./requirements.txt
   ```

   A valid Appium Python package should produce output like the following:

   ```
   Ignoring indexes: https://pypi.python.org/simple
   Collecting Appium-Python-Client==0.20 (from -r ./requirements.txt (line 1))
   Collecting py==1.4.31 (from -r ./requirements.txt (line 2))
   Collecting pytest==2.9.0 (from -r ./requirements.txt (line 3))
   Collecting selenium==2.52.0 (from -r ./requirements.txt (line 4))
   Collecting wheel==0.26.0 (from -r ./requirements.txt (line 5))
   Installing collected packages: selenium, Appium-Python-Client, py, pytest, wheel
     Found existing installation: wheel 0.29.0
       Uninstalling wheel-0.29.0:
         Successfully uninstalled wheel-0.29.0
   Successfully installed Appium-Python-Client-0.20 py-1.4.31 pytest-2.9.0 selenium-2.52.0 wheel-0.26.0
   ```

1. To deactivate the virtual environment, you can run the following command:

   ```
   $ deactivate
   ```

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md). 

### APPIUM\_WEB\_PYTHON\_TEST\_PACKAGE\_PYTEST\_COLLECT\_FAILED
<a name="APPIUM_WEB_PYTHON_TEST_PACKAGE_PYTEST_COLLECT_FAILED"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We failed to collect tests in the tests directory. Please unzip your test package, very that the test package is valid by running the command "py.test --collect-only <path to your tests directory>", and try again after the command does not print any error. 

We strongly recommend that you set up [Python virtualenv](https://pypi.python.org/pypi/virtualenv) for packaging tests. Here is an example flow of creating a virtual environment using Python virtualenv and then activating it:

```
$ virtualenv workspace
$ cd workspace 
$ source bin/activate
```

Make sure that you can unzip the test package without errors. In the following example, the package's name is **test\_bundle.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip test_bundle.zip
   ```

1. To install wheel files, you can run the following command:

   ```
   $ pip install --use-wheel --no-index --find-links=./wheelhouse --requirement=./requirements.txt
   ```

1. To collect tests, you can run the following command:

   ```
   $ py.test --collect-only tests
   ```

   A valid Appium Python package should produce output like the following:

   ```
   ==================== test session starts ====================
   platform darwin -- Python 2.7.11, pytest-2.9.0, py-1.4.31, pluggy-0.3.1
   rootdir: /Users/zhena/Desktop/Ios/tests, inifile:
   collected 1 items
   <Module 'test_unittest.py'>
     <UnitTestCase 'DeviceFarmAppiumWebTests'>
       <TestCaseFunction 'test_devicefarm'>
   
   ==================== no tests ran in 0.11 seconds ====================
   ```

1. To deactivate the virtual environment, you can run the following command:

   ```
   $ deactivate
   ```

   For more information, see [Automatically run Appium tests in Device Farm](test-types-appium.md). 

## Troubleshooting instrumentation tests in AWS Device Farm
<a name="troubleshooting-instrumentation-tests"></a>

The following topic lists error messages that occur during the upload of Instrumentation tests and recommends workarounds to resolve each error.

**Note**  
For important considerations when using Instrumentation tests in AWS Device Farm, see [Instrumentation for Android and AWS Device Farm](test-types-android-instrumentation.md). 

### Upload errors
<a name="troubleshooting-instrumentation-tests-upload"></a>

The following errors can occur when you upload your Instrumentation tests.

#### INSTRUMENTATION\_TEST\_PACKAGE\_UNZIP\_FAILED
<a name="INSTRUMENTATION_TEST_PACKAGE_UNZIP_FAILED"></a>

If you see the following message, follow these steps to fix the issue.

```
Warning: We could not open your test APK file. Please verify that the file is valid and
    try again.
```

Make sure that you can unzip the test package without errors. In the following example, the package's name is **app-debug-androidTest-unaligned.apk**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip app-debug-androidTest-unaligned.apk
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

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

   For more information, see [Instrumentation for Android and AWS Device Farm](test-types-android-instrumentation.md). 

#### INSTRUMENTATION\_TEST\_PACKAGE\_AAPT\_DEBUG\_BADGING\_FAILED
<a name="INSTRUMENTATION_TEST_PACKAGE_AAPT_DEBUG_BADGING_FAILED"></a>

If you see the following message, follow these steps to fix the issue.

```
We could not extract information about your test package. Please verify that the
      test package is valid by running the command "aapt debug badging <path to your test
      package>", and try again after the command does not print any error.
```

During the upload validation process, Device Farm parses out information from the output of the `aapt debug badging <path to your package>` command.

Make sure that you can run this command on your Instrumentation test package successfully.

In the following example, the package's name is **app-debug-androidTest-unaligned.apk**.
+ Copy your test package to your working directory, and then run the following command:

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

  For more information, see [Instrumentation for Android and AWS Device Farm](test-types-android-instrumentation.md). 

#### INSTRUMENTATION\_TEST\_PACKAGE\_INSTRUMENTATION\_RUNNER\_VALUE\_MISSING
<a name="INSTRUMENTATION_TEST_PACKAGE_INSTRUMENTATION_RUNNER_VALUE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

```
We could not find the instrumentation runner value in the AndroidManifest.xml.
      Please verify the test package is valid by running the command "aapt dump xmltree <path to
      your test package> AndroidManifest.xml", and try again after finding the instrumentation
      runner value behind the keyword "instrumentation."
```

During the upload validation process, Device Farm parses out the instrumentation runner value from the XML parse tree for an XML file contained within the package. You can use the following command: `aapt dump xmltree <path to your package> AndroidManifest.xml`.

Make sure that you can run this command on your Instrumentation test package and find the instrumentation value successfully.

In the following example, the package's name is **app-debug-androidTest-unaligned.apk**.
+ Copy your test package to your working directory, and then run the following command:

  ```
  $ aapt dump xmltree app-debug-androidTest-unaligned.apk AndroidManifest.xml | grep -A5 "instrumentation"
  ```

  A valid Instrumentation test package will produce output like the following:

  ```
  E: instrumentation (line=9)
        A: android:label(0x01010001)="Tests for com.amazon.aws.adf.android.referenceapp" (Raw: "Tests for com.amazon.aws.adf.android.referenceapp")
        A: android:name(0x01010003)="{{android.support.test.runner.AndroidJUnitRunner}}" (Raw: "android.support.test.runner.AndroidJUnitRunner")
        A: android:targetPackage(0x01010021)="com.amazon.aws.adf.android.referenceapp" (Raw: "com.amazon.aws.adf.android.referenceapp")
        A: android:handleProfiling(0x01010022)=(type 0x12)0x0
        A: android:functionalTest(0x01010023)=(type 0x12)0x0
  ```

  For more information, see [Instrumentation for Android and AWS Device Farm](test-types-android-instrumentation.md). 

#### INSTRUMENTATION\_TEST\_PACKAGE\_AAPT\_DUMP\_XMLTREE\_FAILED
<a name="INSTRUMENTATION_TEST_PACKAGE_AAPT_DUMP_XMLTREE_FAILED"></a>

If you see the following message, follow these steps to fix the issue.

```
We could not find the valid AndroidManifest.xml in your test package. Please
      verify that the test package is valid by running the command "aapt dump xmltree <path to
      your test package> AndroidManifest.xml", and try again after the command does not print any
      error.
```

During the upload validation process, Device Farm parses out information from the XML parse tree for an XML file contained within the package using the following command: `aapt dump xmltree <path to your package> AndroidManifest.xml`.

Make sure that you can run this command on your instrumentation test package successfully.

In the following example, the package's name is **app-debug-androidTest-unaligned.apk**.
+ Copy your test package to your working directory, and then run the following command:

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

  For more information, see [Instrumentation for Android and AWS Device Farm](test-types-android-instrumentation.md). 

#### INSTRUMENTATION\_TEST\_PACKAGE\_TEST\_PACKAGE\_NAME\_VALUE\_MISSING
<a name="INSTRUMENTATION_TEST_PACKAGE_TEST_PACKAGE_NAME_VALUE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

```
We could not find the package name in your test package. Please verify that the
      test package is valid by running the command "aapt debug badging <path to your test
      package>", and try again after finding the package name value behind the keyword "package:
      name."
```

During the upload validation process, Device Farm parses out the package name value from the output of the following command: `aapt debug badging <path to your package>`.

Make sure that you can run this command on your Instrumentation test package and find the package name value successfully.

In the following example, the package's name is **app-debug-androidTest-unaligned.apk**.
+ Copy your test package to your working directory, and then run the following command:

  ```
  $ aapt debug badging app-debug-androidTest-unaligned.apk | grep "package: name="
  ```

  A valid Instrumentation test package will produce output like the following:

  ```
  package: name='com.amazon.aws.adf.android.referenceapp.test' versionCode='' versionName='' platformBuildVersionName='5.1.1-1819727'
  ```

  For more information, see [Instrumentation for Android and AWS Device Farm](test-types-android-instrumentation.md). 

## Troubleshooting XCTest tests in AWS Device Farm
<a name="troubleshooting-xctest"></a>

The following topic lists error messages that occur during the upload of XCTest tests and recommends workarounds to resolve each error.

**Note**  
The instructions below assume you are using MacOS.

### XCTEST\_TEST\_PACKAGE\_UNZIP\_FAILED
<a name="XCTEST_TEST_PACKAGE_UNZIP_FAILED"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not open your test ZIP file. Please verify that the file is valid and try again.

Make sure that you can unzip the application package without errors. In the following example, the package's name is **swiftExampleTests.xctest-1.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swiftExampleTests.xctest-1.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   A valid XCTest package should produce output like the following:

   ```
   .
   `-- swiftExampleTests.xctest (directory)
                 |-- Info.plist
                 `-- (any other files)
   ```

   For more information, see [Integrating Device Farm with XCTest for iOS](test-types-ios-xctest.md).

### XCTEST\_TEST\_PACKAGE\_XCTEST\_DIR\_MISSING
<a name="XCTEST_TEST_PACKAGE_XCTEST_DIR_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find the .xctest directory inside your test package. Please unzip your test package, verify that the .xctest directory is inside the package, and try again. 

In the following example, the package's name is **swiftExampleTests.xctest-1.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swiftExampleTests.xctest-1.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the XCTest package is valid, you will find a directory with a name similar to {{swiftExampleTests.xctest}} inside the working directory. The name should end with {{.xctest}}.

   ```
   .
   `-- {{swiftExampleTests.xctest}} (directory)
                 |-- Info.plist
                 `-- (any other files)
   ```

   For more information, see [Integrating Device Farm with XCTest for iOS](test-types-ios-xctest.md).

### XCTEST\_TEST\_PACKAGE\_PLIST\_FILE\_MISSING
<a name="XCTEST_TEST_PACKAGE_PLIST_FILE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find the Info.plist file inside the .xctest directory. Please unzip your test package and then open the .xctest directory, verify that the Info.plist file is inside the directory, and try again.

In the following example, the package's name is **swiftExampleTests.xctest-1.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swiftExampleTests.xctest-1.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the XCTest package is valid, you will find the {{Info.plist}} file inside the {{.xctest}} directory. In our example below, the directory is called {{swiftExampleTests.xctest}}.

   ```
   .
   `-- swiftExampleTests.xctest (directory)
                 |-- {{Info.plist}}
                 `-- (any other files)
   ```

   For more information, see [Integrating Device Farm with XCTest for iOS](test-types-ios-xctest.md).

### XCTEST\_TEST\_PACKAGE\_PACKAGE\_NAME\_VALUE\_MISSING
<a name="XCTEST_TEST_PACKAGE_PACKAGE_NAME_VALUE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find the package name value in the Info.plist file. Please unzip your test package and then open Info.plist file, verify that the key "CFBundleIdentifier" is specified, and try again.

In the following example, the package's name is **swiftExampleTests.xctest-1.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swiftExampleTests.xctest-1.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find the {{Info.plist}} file inside an {{.xctest}} directory like {{swiftExampleTests.xctest}} in our example:

   ```
   .
   `-- swiftExampleTests.xctest (directory)
                 |-- {{Info.plist}}
                 `-- (any other files)
   ```

1. To find the package name value, you can open Info.plist using Xcode or Python.

   For Python, you can install the biplist module by running the following command:

   ```
   $ pip install biplist
   ```

1. Next, open Python and run the following command:

   ```
   import biplist
   info_plist = biplist.readPlist('swiftExampleTests.xctest/Info.plist')
   print info_plist['CFBundleIdentifier']
   ```

   A valid XCtest application package should produce output like the following:

   ```
   com.amazon.kanapka.swiftExampleTests
   ```

   For more information, see [Integrating Device Farm with XCTest for iOS](test-types-ios-xctest.md).

### XCTEST\_TEST\_PACKAGE\_EXECUTABLE\_VALUE\_MISSING
<a name="XCTEST_TEST_PACKAGE_EXECUTABLE_VALUE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

**Warning**  
We could not find the executable value in the Info.plist file. Please unzip your test package and then open Info.plist file, verify that the key "CFBundleExecutable" is specified, and try again.

In the following example, the package's name is **swiftExampleTests.xctest-1.zip**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swiftExampleTests.xctest-1.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find the {{Info.plist}} file inside an {{.xctest}} directory like {{swiftExampleTests.xctest}} in our example:

   ```
   .
   `-- swiftExampleTests.xctest (directory)
                 |-- {{Info.plist}}
                 `-- (any other files)
   ```

1. To find the package name value, you can open Info.plist using Xcode or Python.

   For Python, you can install the biplist module by running the following command:

   ```
   $ pip install biplist
   ```

1. Next, open Python and run the following command:

   ```
   import biplist
   info_plist = biplist.readPlist('swiftExampleTests.xctest/Info.plist')
   print info_plist['CFBundleExecutable']
   ```

   A valid XCtest application package should produce output like the following:

   ```
   swiftExampleTests
   ```

   For more information, see [Integrating Device Farm with XCTest for iOS](test-types-ios-xctest.md).

## Troubleshooting XCTest UI tests in AWS Device Farm
<a name="troubleshooting-xctest-ui"></a>

The following topic lists error messages that occur during the upload of XCTest UI tests and recommends workarounds to resolve each error.

### Upload errors
<a name="troubleshooting-xctest-ui-upload"></a>

The following errors can occur when you upload your XCTest UI tests.

#### XCTEST\_UI\_TEST\_PACKAGE\_UNZIP\_FAILED
<a name="XCTEST_UI_TEST_PACKAGE_UNZIP_FAILED"></a>

If you see the following message, follow these steps to fix the issue.

`We could not open your test IPA file. Please verify that the file is valid and try again.`

Make sure that you can unzip the application package without errors. In the following example, the package's name is **swift-sample-UI.ipa**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swift-sample-UI.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   A valid iOS application package should produce output like the following:

   ```
   .
   `-- Payload (directory)
           `-- swift-sampleUITests-Runner.app (directory)
                         |-- Info.plist
                         |-- Plugins (directory)
                         |       `swift-sampleUITests.xctest (directory)
                         |                       |-- Info.plist
                         |                       `-- (any other files)
                         `-- (any other files)
   ```

   For more information, see [Integrating XCTest UI for iOS with Device Farm](test-types-ios-xctest-ui.md).

#### XCTEST\_UI\_TEST\_PACKAGE\_PAYLOAD\_DIR\_MISSING
<a name="XCTEST_UI_TEST_PACKAGE_PAYLOAD_DIR_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

`We could not find the Payload directory inside your test package. Please unzip your test package, verify that the Payload directory is inside the package, and try again. `

A test runner built for a simulator can instead be a `.zip` file with the runner {{.app}} directory at the root of the archive. For the simulator build and packaging steps, see [Option 2: Creating an XCTest UI .zip package](test-types-ios-xctest-ui.md#how-to-use-create-XCTestUI-zip-package).

In the following example, the package's name is **swift-sample-UI.ipa**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swift-sample-UI.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the XCTest UI package is a valid `.ipa` file, the `Payload` directory is inside the working directory.

   ```
   .
   `-- {{Payload}} (directory)
           `-- swift-sampleUITests-Runner.app (directory)
                         |-- Info.plist
                         |-- Plugins (directory)
                         |       `swift-sampleUITests.xctest (directory)
                         |                       |-- Info.plist
                         |                       `-- (any other files)
                         `-- (any other files)
   ```

   For more information, see [Integrating XCTest UI for iOS with Device Farm](test-types-ios-xctest-ui.md).

#### XCTEST\_UI\_TEST\_PACKAGE\_APP\_DIR\_MISSING
<a name="XCTEST_UI_TEST_PACKAGE_APP_DIR_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

`We could not find the .app directory inside the Payload directory. Please unzip your test package and then open the Payload directory, verify that the .app directory is inside the directory, and try again.`

In the following example, the package's name is **swift-sample-UI.ipa**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swift-sample-UI.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the XCTest UI package is valid, you will find an {{.app}} directory like {{swift-sampleUITests-Runner.app}} in our example inside the `Payload` directory.

   ```
   .
   `-- Payload (directory)
           `-- {{swift-sampleUITests-Runner.app}} (directory)
                         |-- Info.plist
                         |-- Plugins (directory)
                         |       `swift-sampleUITests.xctest (directory)
                         |                       |-- Info.plist
                         |                       `-- (any other files)
                         `-- (any other files)
   ```

   For more information, see [Integrating XCTest UI for iOS with Device Farm](test-types-ios-xctest-ui.md).

#### XCTEST\_UI\_TEST\_PACKAGE\_PLUGINS\_DIR\_MISSING
<a name="XCTEST_UI_TEST_PACKAGE_PLUGINS_DIR_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

`We could not find the Plugins directory inside the .app directory. Please unzip your test package and then open the .app directory, verify that the Plugins directory is inside the directory, and try again.`

In the following example, the package's name is **swift-sample-UI.ipa**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swift-sample-UI.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the XCTest UI package is valid, you will find the {{Plugins}} directory inside an {{.app}} directory. In our example, the directory is called {{swift-sampleUITests-Runner.app}}.

   ```
   .
   `-- Payload (directory)
           `-- swift-sampleUITests-Runner.app (directory)
                         |-- Info.plist
                         |-- {{Plugins}} (directory)
                         |       `swift-sampleUITests.xctest (directory)
                         |                       |-- Info.plist
                         |                       `-- (any other files)
                         `-- (any other files)
   ```

   For more information, see [Integrating XCTest UI for iOS with Device Farm](test-types-ios-xctest-ui.md).

#### XCTEST\_UI\_TEST\_PACKAGE\_XCTEST\_DIR\_MISSING\_IN\_PLUGINS\_DIR
<a name="XCTEST_UI_TEST_PACKAGE_XCTEST_DIR_MISSING_IN_PLUGINS_DIR"></a>

If you see the following message, follow these steps to fix the issue.

`We could not find the .xctest directory inside the plugins directory. Please unzip your test package and then open the plugins directory, verify that the .xctest directory is inside the directory, and try again.`

In the following example, the package's name is **swift-sample-UI.ipa**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swift-sample-UI.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the XCTest UI package is valid, you will find an {{.xctest}} directory inside the {{Plugins}} directory. In our example, the directory is called {{swift-sampleUITests.xctest}}.

   ```
   .
   `-- Payload (directory)
           `-- swift-sampleUITests-Runner.app (directory)
                         |-- Info.plist
                         |-- Plugins (directory)
                         |       `{{swift-sampleUITests.xctest}} (directory)
                         |                       |-- Info.plist
                         |                       `-- (any other files)
                         `-- (any other files)
   ```

   For more information, see [Integrating XCTest UI for iOS with Device Farm](test-types-ios-xctest-ui.md).

#### XCTEST\_UI\_TEST\_PACKAGE\_PLIST\_FILE\_MISSING
<a name="XCTEST_UI_TEST_PACKAGE_PLIST_FILE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

`We could not find the Info.plist file inside the .app directory. Please unzip your test package and then open the .app directory, verify that the Info.plist file is inside the directory, and try again.`

In the following example, the package's name is **swift-sample-UI.ipa**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swift-sample-UI.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the XCTest UI package is valid, you will find the {{Info.plist}} file inside the {{.app}} directory. In our example below, the directory is called {{swift-sampleUITests-Runner.app}}.

   ```
   .
   `-- Payload (directory)
           `-- swift-sampleUITests-Runner.app (directory)
                         |-- {{Info.plist}}
                         |-- Plugins (directory)
                         |       `swift-sampleUITests.xctest (directory)
                         |                       |-- Info.plist
                         |                       `-- (any other files)
                         `-- (any other files)
   ```

   For more information, see [Integrating XCTest UI for iOS with Device Farm](test-types-ios-xctest-ui.md).

#### XCTEST\_UI\_TEST\_PACKAGE\_PLIST\_FILE\_MISSING\_IN\_XCTEST\_DIR
<a name="XCTEST_UI_TEST_PACKAGE_PLIST_FILE_MISSING_IN_XCTEST_DIR"></a>

If you see the following message, follow these steps to fix the issue.

`We could not find the Info.plist file inside the .xctest directory. Please unzip your test package and then open the .xctest directory, verify that the Info.plist file is inside the directory, and try again.`

In the following example, the package's name is **swift-sample-UI.ipa**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swift-sample-UI.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the XCTest UI package is valid, you will find the {{Info.plist}} file inside the {{.xctest}} directory. In our example below, the directory is called {{swift-sampleUITests.xctest}}.

   ```
   .
   `-- Payload (directory)
           `-- swift-sampleUITests-Runner.app (directory)
                         |-- Info.plist
                         |-- Plugins (directory)
                         |       `swift-sampleUITests.xctest (directory)
                         |                       |-- {{Info.plist}}
                         |                       `-- (any other files)
                         `-- (any other files)
   ```

   For more information, see [Integrating XCTest UI for iOS with Device Farm](test-types-ios-xctest-ui.md).

#### XCTEST\_UI\_TEST\_PACKAGE\_CPU\_ARCHITECTURE\_VALUE\_MISSING
<a name="XCTEST_UI_TEST_PACKAGE_CPU_ARCHITECTURE_VALUE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

`We could not the CPU architecture value in the Info.plist file. Please unzip your test package and then open the Info.plist file inside the .app directory, verify that the key "UIRequiredDeviceCapabilities" is specified, and try again.`

In the following example, the package's name is **swift-sample-UI.ipa**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swift-sample-UI.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find the {{Info.plist}} file inside an {{.app}} directory like {{swift-sampleUITests-Runner.app}} in our example:

   ```
   .
   `-- Payload (directory)
           `-- swift-sampleUITests-Runner.app (directory)
                         |-- {{Info.plist}}
                         |-- Plugins (directory)
                         |       `swift-sampleUITests.xctest (directory)
                         |                       |-- Info.plist
                         |                       `-- (any other files)
                         `-- (any other files)
   ```

1. To find the CPU architecture value, you can open Info.plist using Xcode or Python.

   For Python, you can install the biplist module by running the following command:

   ```
   $ pip install biplist
   ```

1. Next, open Python and run the following command:

   ```
   import biplist
   info_plist = biplist.readPlist('Payload/swift-sampleUITests-Runner.app/Info.plist') 
   print info_plist['UIRequiredDeviceCapabilities']
   ```

   A valid XCtest UI package should produce output like the following:

   ```
   ['armv7']
   ```

   For more information, see [Integrating XCTest UI for iOS with Device Farm](test-types-ios-xctest-ui.md).

#### XCTEST\_UI\_TEST\_PACKAGE\_PLATFORM\_VALUE\_MISSING
<a name="XCTEST_UI_TEST_PACKAGE_PLATFORM_VALUE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

`We could not find the platform value in the Info.plist. Please unzip your test package and then open the Info.plist file inside the .app directory, verify that the key "CFBundleSupportedPlatforms" is specified, and try again.`

In the following example, the package's name is **swift-sample-UI.ipa**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swift-sample-UI.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find the {{Info.plist}} file inside an {{.app}} directory like {{swift-sampleUITests-Runner.app}} in our example:

   ```
   .
   `-- Payload (directory)
           `-- swift-sampleUITests-Runner.app (directory)
                         |-- {{Info.plist}}
                         |-- Plugins (directory)
                         |       `swift-sampleUITests.xctest (directory)
                         |                       |-- Info.plist
                         |                       `-- (any other files)
                         `-- (any other files)
   ```

1. To find the platform value, you can open Info.plist using Xcode or Python.

   For Python, you can install the biplist module by running the following command:

   ```
   $ pip install biplist
   ```

1. Next, open Python and run the following command:

   ```
   import biplist
   info_plist = biplist.readPlist('Payload/swift-sampleUITests-Runner.app/Info.plist')
   print info_plist['CFBundleSupportedPlatforms']
   ```

   A valid XCtest UI package should produce output like the following:

   ```
   ['iPhoneOS']
   ```

   For more information, see [Integrating XCTest UI for iOS with Device Farm](test-types-ios-xctest-ui.md).

#### XCTEST\_UI\_TEST\_PACKAGE\_WRONG\_PLATFORM\_DEVICE\_VALUE
<a name="XCTEST_UI_TEST_PACKAGE_WRONG_PLATFORM_DEVICE_VALUE"></a>

If you see the following message, follow these steps to fix the issue.

`We could not match the platform value in the Info.plist file to your test package. Please unzip your test package and then open the Info.plist file inside the .app directory, verify that the value of the key "CFBundleSupportedPlatforms" names the platform your test runner was built for, and try again.`

Device Farm tells a device build from a simulator build by the `CFBundleSupportedPlatforms` key, not the file name. For more information, see [Packaging an iOS app](apps.md#test-runs-ios-app-packaging).

In the following example, the package's name is **swift-sample-UI.ipa**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swift-sample-UI.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find the {{Info.plist}} file inside an {{.app}} directory like {{swift-sampleUITests-Runner.app}} in our example:

   ```
   .
   `-- Payload (directory)
           `-- swift-sampleUITests-Runner.app (directory)
                         |-- {{Info.plist}}
                         |-- Plugins (directory)
                         |       `swift-sampleUITests.xctest (directory)
                         |                       |-- Info.plist
                         |                       `-- (any other files)
                         `-- (any other files)
   ```

1. To find the platform value, you can open Info.plist using Xcode or Python.

   For Python, you can install the biplist module by running the following command:

   ```
   $ pip install biplist
   ```

1. Next, open Python and run the following command:

   ```
   import biplist
   info_plist = biplist.readPlist('Payload/swift-sampleUITests-Runner.app/Info.plist')
   print info_plist['CFBundleSupportedPlatforms']
   ```

   A device build produces the following output:

   ```
   ['iPhoneOS']
   ```

   A simulator build produces the following output:

   ```
   ['iPhoneSimulator']
   ```

   For more information, see [Integrating XCTest UI for iOS with Device Farm](test-types-ios-xctest-ui.md).

#### XCTEST\_UI\_TEST\_PACKAGE\_SIMULATOR\_RUNNER\_NOT\_AT\_ZIP\_ROOT
<a name="XCTEST_UI_TEST_PACKAGE_SIMULATOR_RUNNER_NOT_AT_ZIP_ROOT"></a>

If you see the following message, the runner {{.app}} directory of a simulator build is inside another folder, or inside an `.ipa` file inside the `.zip` file.

`We found that your XCTest UI runner is built for a simulator but is not packaged where a simulator can install it. Please upload either a .zip file with the runner .app directory at the root of the archive or an .ipa file with the runner .app directory inside its Payload directory, and try again. If this runner is built for a physical device, verify that the value of the key "CFBundleSupportedPlatforms" in its Info.plist file does not contain the keyword "simulator".`

Zip the runner {{.app}} directory itself so that it is at the root of the archive, or package it as an `.ipa` file with the runner inside a `Payload` directory. For the simulator build and packaging steps, see [Option 2: Creating an XCTest UI .zip package](test-types-ios-xctest-ui.md#how-to-use-create-XCTestUI-zip-package).

If your runner is built for a physical device, confirm the `CFBundleSupportedPlatforms` value as described in [XCTEST\_UI\_TEST\_PACKAGE\_WRONG\_PLATFORM\_DEVICE\_VALUE](#XCTEST_UI_TEST_PACKAGE_WRONG_PLATFORM_DEVICE_VALUE).

#### XCTEST\_UI\_TEST\_PACKAGE\_PLATFORM\_NAME\_MISMATCH
<a name="XCTEST_UI_TEST_PACKAGE_PLATFORM_NAME_MISMATCH"></a>

If you see the following message, your upload succeeded with a warning.

`We found that the value of the key "DTPlatformName" in the Info.plist file does not name a simulator platform, although the key "CFBundleSupportedPlatforms" indicates a simulator build. This may cause some of your tests to not be executed correctly.`

To check the value, open the `Info.plist` file inside the runner {{.app}} directory with Xcode or the biplist module, as described in [XCTEST\_UI\_TEST\_PACKAGE\_WRONG\_PLATFORM\_DEVICE\_VALUE](#XCTEST_UI_TEST_PACKAGE_WRONG_PLATFORM_DEVICE_VALUE). In a simulator build, the value of the key `DTPlatformName` is `iphonesimulator`.

#### XCTEST\_UI\_TEST\_PACKAGE\_FORM\_FACTOR\_VALUE\_MISSING
<a name="XCTEST_UI_TEST_PACKAGE_FORM_FACTOR_VALUE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

`We could not the form factor value in the Info.plist. Please unzip your test package and then open the Info.plist file inside the .app directory, verify that the key "UIDeviceFamily" is specified, and try again.`

In the following example, the package's name is **swift-sample-UI.ipa**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swift-sample-UI.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find the {{Info.plist}} file inside an {{.app}} directory like {{swift-sampleUITests-Runner.app}} in our example:

   ```
   .
   `-- Payload (directory)
           `-- swift-sampleUITests-Runner.app (directory)
                         |-- {{Info.plist}}
                         |-- Plugins (directory)
                         |       `swift-sampleUITests.xctest (directory)
                         |                       |-- Info.plist
                         |                       `-- (any other files)
                         `-- (any other files)
   ```

1. To find the form factor value, you can open Info.plist using Xcode or Python.

   For Python, you can install the biplist module by running the following command:

   ```
   $ pip install biplist
   ```

1. Next, open Python and run the following command:

   ```
   import biplist
   info_plist = biplist.readPlist('Payload/swift-sampleUITests-Runner.app/Info.plist')
   print info_plist['UIDeviceFamily']
   ```

   A valid XCtest UI package should produce output like the following:

   ```
   [1, 2]
   ```

   For more information, see [Integrating XCTest UI for iOS with Device Farm](test-types-ios-xctest-ui.md).

#### XCTEST\_UI\_TEST\_PACKAGE\_PACKAGE\_NAME\_VALUE\_MISSING
<a name="XCTEST_UI_TEST_PACKAGE_PACKAGE_NAME_VALUE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

`We could not find the package name value in the Info.plist file. Please unzip your test package and then open the Info.plist file inside the .app directory, verify that the key "CFBundleIdentifier" is specified, and try again.`

In the following example, the package's name is **swift-sample-UI.ipa**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swift-sample-UI.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find the {{Info.plist}} file inside an {{.app}} directory like {{swift-sampleUITests-Runner.app}} in our example:

   ```
   .
   `-- Payload (directory)
           `-- swift-sampleUITests-Runner.app (directory)
                         |-- {{Info.plist}}
                         |-- Plugins (directory)
                         |       `swift-sampleUITests.xctest (directory)
                         |                       |-- Info.plist
                         |                       `-- (any other files)
                         `-- (any other files)
   ```

1. To find the package name value, you can open Info.plist using Xcode or Python.

   For Python, you can install the biplist module by running the following command:

   ```
   $ pip install biplist
   ```

1. Next, open Python and run the following command:

   ```
   import biplist
   info_plist = biplist.readPlist('Payload/swift-sampleUITests-Runner.app/Info.plist')
   print info_plist['CFBundleIdentifier']
   ```

   A valid XCtest UI package should produce output like the following:

   ```
   com.apple.test.swift-sampleUITests-Runner
   ```

   For more information, see [Integrating XCTest UI for iOS with Device Farm](test-types-ios-xctest-ui.md).

#### XCTEST\_UI\_TEST\_PACKAGE\_EXECUTABLE\_VALUE\_MISSING
<a name="XCTEST_UI_TEST_PACKAGE_EXECUTABLE_VALUE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

`We could not find the executable value in the Info.plist file. Please unzip your test package and then open the Info.plist file inside the .app directory, verify that the key "CFBundleExecutable" is specified, and try again.`

In the following example, the package's name is **swift-sample-UI.ipa**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swift-sample-UI.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find the {{Info.plist}} file inside an {{.app}} directory like {{swift-sampleUITests-Runner.app}} in our example:

   ```
   .
   `-- Payload (directory)
           `-- swift-sampleUITests-Runner.app (directory)
                         |-- {{Info.plist}}
                         |-- Plugins (directory)
                         |       `swift-sampleUITests.xctest (directory)
                         |                       |-- Info.plist
                         |                       `-- (any other files)
                         `-- (any other files)
   ```

1. To find the executable value, you can open Info.plist using Xcode or Python.

   For Python, you can install the biplist module by running the following command:

   ```
   $ pip install biplist
   ```

1. Next, open Python and run the following command:

   ```
   import biplist
   info_plist = biplist.readPlist('Payload/swift-sampleUITests-Runner.app/Info.plist')
   print info_plist['CFBundleExecutable']
   ```

   A valid XCtest UI package should produce output like the following:

   ```
   XCTRunner
   ```

   For more information, see [Integrating XCTest UI for iOS with Device Farm](test-types-ios-xctest-ui.md).

#### XCTEST\_UI\_TEST\_PACKAGE\_TEST\_PACKAGE\_NAME\_VALUE\_MISSING
<a name="XCTEST_UI_TEST_PACKAGE_TEST_PACKAGE_NAME_VALUE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

`We could not find the package name value in the Info.plist file inside the .xctest directory. Please unzip your test package and then open the Info.plist file inside the .xctest directory, verify that the key "CFBundleIdentifier" is specified, and try again.`

In the following example, the package's name is **swift-sample-UI.ipa**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swift-sample-UI.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find the {{Info.plist}} file inside an {{.app}} directory like {{swift-sampleUITests-Runner.app}} in our example:

   ```
   .
   `-- Payload (directory)
           `-- swift-sampleUITests-Runner.app (directory)
                         |-- {{Info.plist}}
                         |-- Plugins (directory)
                         |       `swift-sampleUITests.xctest (directory)
                         |                       |-- Info.plist
                         |                       `-- (any other files)
                         `-- (any other files)
   ```

1. To find the package name value, you can open Info.plist using Xcode or Python.

   For Python, you can install the biplist module by running the following command:

   ```
   $ pip install biplist
   ```

1. Next, open Python and run the following command:

   ```
   import biplist
   info_plist = biplist.readPlist('Payload/swift-sampleUITests-Runner.app/Plugins/swift-sampleUITests.xctest/Info.plist')
   print info_plist['CFBundleIdentifier']
   ```

   A valid XCtest UI package should produce output like the following:

   ```
   com.amazon.swift-sampleUITests
   ```

   For more information, see [Integrating XCTest UI for iOS with Device Farm](test-types-ios-xctest-ui.md).

#### XCTEST\_UI\_TEST\_PACKAGE\_TEST\_EXECUTABLE\_VALUE\_MISSING
<a name="XCTEST_UI_TEST_PACKAGE_TEST_EXECUTABLE_VALUE_MISSING"></a>

If you see the following message, follow these steps to fix the issue.

`We could not find the executable value in the Info.plist file inside the .xctest directory. Please unzip your test package and then open the Info.plist file inside the .xctest directory, verify that the key "CFBundleExecutable" is specified, and try again.`

In the following example, the package's name is **swift-sample-UI.ipa**.

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swift-sample-UI.ipa
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   You should find the {{Info.plist}} file inside an {{.app}} directory like {{swift-sampleUITests-Runner.app}} in our example:

   ```
   .
   `-- Payload (directory)
           `-- swift-sampleUITests-Runner.app (directory)
                         |-- {{Info.plist}}
                         |-- Plugins (directory)
                         |       `swift-sampleUITests.xctest (directory)
                         |                       |-- Info.plist
                         |                       `-- (any other files)
                         `-- (any other files)
   ```

1. To find the executable value, you can open Info.plist using Xcode or Python.

   For Python, you can install the biplist module by running the following command:

   ```
   $ pip install biplist
   ```

1. Next, open Python and run the following command:

   ```
   import biplist
   info_plist = biplist.readPlist('Payload/swift-sampleUITests-Runner.app/Plugins/swift-sampleUITests.xctest/Info.plist')
   print info_plist['CFBundleExecutable']
   ```

   A valid XCtest UI package should produce output like the following:

   ```
   swift-sampleUITests
   ```

   For more information, see [Integrating XCTest UI for iOS with Device Farm](test-types-ios-xctest-ui.md).

#### XCTEST\_UI\_TEST\_PACKAGE\_MULTIPLE\_APP\_DIRS
<a name="XCTEST_UI_TEST_PACKAGE_MULTIPLE_APP_DIRS"></a>

If you see the following message, follow these steps to fix the issue.

`We found multiple .app directories inside your test package. Please unzip your test package, verify that only a single .app directory is present inside the package, then try again.`

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swift-sample-UI.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the XCTest UI package is valid, you should find only single `.app` directory like `swift-sampleUITests-Runner.app` in our example inside the .zip test package. 

   ```
   .
   `--swift-sample-UI.zip--(directory)
       `-- {{swift-sampleUITests-Runner.app}} (directory)
               |-- Info.plist
               |-- Plugins (directory)
               |       `swift-sampleUITests.xctest (directory)
              |            |-- Info.plist
              |            `-- (any other files)
               `-- (any other files)
       `-- (any other files)
   ```

   For more information, see [Integrating XCTest UI for iOS with Device Farm](test-types-ios-xctest-ui.md).

#### XCTEST\_UI\_TEST\_PACKAGE\_MULTIPLE\_IPA\_DIRS
<a name="XCTEST_UI_TEST_PACKAGE_MULTIPLE_IPA_DIRS"></a>

If you see the following message, follow these steps to fix the issue.

`We found multiple .ipa directories inside your test package. Please unzip your test package, verify that only a single .ipa directory is present inside the package, then try again.`

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swift-sample-UI.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the XCTest UI package is valid, you should find only single `.ipa` directory like `sampleUITests.ipa` in our example inside the .zip test package. 

   ```
   .
   `--swift-sample-UI.zip--(directory)
       `-- {{sampleUITests.ipa}} (directory)
               `-- Payload (directory)
                   `-- swift-sampleUITests-Runner.app (directory)
       `-- (any other files)
   ```

   For more information, see [Integrating XCTest UI for iOS with Device Farm](test-types-ios-xctest-ui.md).

#### XCTEST\_UI\_TEST\_PACKAGE\_BOTH\_APP\_AND\_IPA\_DIR\_PRESENT
<a name="XCTEST_UI_TEST_PACKAGE_BOTH_APP_AND_IPA_DIR_PRESENT"></a>

If you see the following message, follow these steps to fix the issue.

`We found both .app and .ipa files inside your test package. Please unzip your test package, verify that only a single .app or .ipa file is present inside the package, then try again.`

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swift-sample-UI.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the XCTest UI package is valid, you should find either `.ipa` directory like `sampleUITests.ipa` or `.app` directory like `swift-sampleUITests-Runner.app` in our example inside the .zip test package. You can refer to an example of valid XCTEST\_UI Test package in our documentation on [Integrating XCTest UI for iOS with Device Farm](test-types-ios-xctest-ui.md). 

   ```
   .
   `--swift-sample-UI.zip--(directory)
       `-- {{sampleUITests.ipa}} (directory)
               `-- Payload (directory)
                   `-- swift-sampleUITests-Runner.app (directory)
      `-- (any other files)
   ```

    or 

   ```
   .
   `--swift-sample-UI.zip--(directory)
       `-- {{swift-sampleUITests-Runner.app}} (directory)
               |-- Info.plist
               |-- Plugins (directory)
               `-- (any other files)
      `-- (any other files)
   ```

   For more information, see [Integrating XCTest UI for iOS with Device Farm](test-types-ios-xctest-ui.md).

#### XCTEST\_UI\_TEST\_PACKAGE\_PAYLOAD\_DIR\_PRESENT\_IN\_ZIP
<a name="XCTEST_UI_TEST_PACKAGE_PAYLOAD_DIR_PRESENT_IN_ZIP"></a>

If you see the following message, follow these steps to fix the issue.

`We found a Payload directory inside your .zip test package. Please unzip your test package, ensure that a Payload directory is not present in the package, then try again.`

1. Copy your test package to your working directory, and then run the following command:

   ```
   $ unzip swift-sample-UI.zip
   ```

1. After you successfully unzip the package, you can find the working directory tree structure by running the following command:

   ```
   $ tree .
   ```

   If the XCTest UI package is valid, you should not find a Payload Directory inside your test package.

   ```
   .
   `--swift-sample-UI.zip--(directory)
       `-- swift-sampleUITests-Runner.app (directory)
               |-- Info.plist
               |-- Plugins (directory)
               `-- (any other files)
      `-- {{Payload (directory) [This directory should not be present]}}
               |-- (any other files)
      `-- (any other files)
   ```

   For more information, see [Integrating XCTest UI for iOS with Device Farm](test-types-ios-xctest-ui.md).