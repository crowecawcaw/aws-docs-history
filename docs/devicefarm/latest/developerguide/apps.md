

# Apps in AWS Device Farm

The following sections contain information about app behaviors in Device Farm.

**Topics**
+ [Instrumenting apps](#test-runs-instrumenting)
+ [Packaging an iOS app](#test-runs-ios-app-packaging)
+ [Preparing an Android app for emulators](#test-runs-android-emulator-app)
+ [Re-signing apps](#test-runs-app-resigning)
+ [Obfuscated apps in runs](#test-runs-obfuscated-apps)

## Instrumenting apps
<a name="test-runs-instrumenting"></a>

You do not need to instrument your apps or provide Device Farm with the source code for your apps. Android apps can be submitted unmodified, on physical devices and emulators alike. For more information, see [Preparing an Android app for emulators](#test-runs-android-emulator-app). Build iOS apps for the type of device that you test on. For more information, see [Packaging an iOS app](#test-runs-ios-app-packaging).

## Packaging an iOS app
<a name="test-runs-ios-app-packaging"></a>

Build an iOS app for the type of device that you test on. A physical device runs a device build, and an iOS simulator runs a simulator build. Neither build runs on the other type of device. You build and package both the same way. The steps differ only in the build destination that you choose and the folder that Xcode writes the build to.

You need a Mac with Xcode installed.

### Build your app
<a name="test-runs-ios-app-build"></a>

Follow the steps for the type of device that you test on. You can build in Xcode or with the **xcodebuild** command, which comes with Xcode.

#### Physical devices
<a name="test-runs-ios-app-build-device"></a>

**To build your app for physical devices in Xcode**

1. Open your app project in Xcode.

1. In the scheme menu on the Xcode toolbar, choose **Generic iOS Device** as the destination.

1. On the **Product** menu, choose **Build For**, and then choose **Testing**.

1. In the project navigator, under **Products**, open the contextual menu for the file named `{{app-project-name}}.app`, and then choose **Show in Finder**. Finder opens the `Debug-iphoneos` folder, which contains your `.app` file.

Alternatively, build from the command line. The following command uses the signing settings of your project and writes the app to `build/Build/Products/Debug-iphoneos/{{MyApp}}.app`. Run it from the directory that contains your project file:

```bash
xcodebuild build-for-testing -project {{MyApp}}.xcodeproj -scheme {{MyApp}} -configuration Debug \
    -sdk iphoneos -destination "generic/platform=iOS" -derivedDataPath build
```

#### Simulators
<a name="test-runs-ios-app-build-simulator"></a>

**To build your app for simulators in Xcode**

1. Open your app project in Xcode.

1. In the scheme menu on the Xcode toolbar, choose an iOS Simulator destination.

1. On the **Product** menu, choose **Build For**, and then choose **Testing**.

1. In the project navigator, under **Products**, open the contextual menu for the file named `{{app-project-name}}.app`, and then choose **Show in Finder**. Finder opens the `Debug-iphonesimulator` folder, which contains your `.app` file.

Alternatively, build from the command line. A simulator build does not need code signing, so the following command skips it. The command writes the app to `build/Build/Products/Debug-iphonesimulator/{{MyApp}}.app`. Run it from the directory that contains your project file:

```bash
xcodebuild build-for-testing -project {{MyApp}}.xcodeproj -scheme {{MyApp}} -configuration Debug \
    -sdk iphonesimulator -destination "generic/platform=iOS Simulator" \
    -derivedDataPath build CODE_SIGNING_ALLOWED=NO
```

Device Farm runs iOS simulators on Mac computers with Apple silicon, so the build must include the `arm64` architecture. The generic destination in these steps includes it. The same build runs on any simulator device that Device Farm offers whose iOS version is at or above your app's minimum iOS version.

### Package your app
<a name="test-runs-ios-app-package"></a>

Package the `.app` bundle from your build output folder as an `.ipa` file. The following table shows the layouts that Device Farm accepts for an iOS app upload. For more information about rejected layouts, see [Troubleshooting iOS application tests in AWS Device Farm](troubleshooting-packaging.md#troubleshooting-ios-applications).


| Build | File | Layout | 
| --- | --- | --- | 
| Device | .ipa | Payload/{{name}}.app | 
| Simulator | .ipa | Payload/{{name}}.app. This is the recommended layout. | 
| Simulator | .zip | {{name}}.app at the root of the archive | 

#### Physical devices
<a name="test-runs-ios-app-package-device"></a>

**To package a device build as an .ipa file**

1. In the `Debug-iphoneos` folder, create a new folder, and name it `Payload`.

1. Copy the `{{app-project-name}}.app` file into the `Payload` folder.

1. Open the contextual menu for the `Payload` folder and choose **Compress "Payload"**. Finder creates a file named `Payload.zip`.

1. Change the file name and extension of `Payload.zip` to `{{app-project-name}}.ipa`. This file is your app package.

#### Simulators
<a name="test-runs-ios-app-package-simulator"></a>

**To package a simulator build as an .ipa file**

1. In the `Debug-iphonesimulator` folder, create a new folder, and name it `Payload`.

1. Copy the `{{app-project-name}}.app` file into the `Payload` folder.

1. Open the contextual menu for the `Payload` folder and choose **Compress "Payload"**. Finder creates a file named `Payload.zip`.

1. Change the file name and extension of `Payload.zip` to `{{app-project-name}}.ipa`. This file is your app package.

Device Farm also accepts a simulator build as a `.zip` file with the `.app` bundle at the root of the archive. The **ditto** command, which is part of macOS, creates that layout. To create the `.zip` file, run the following command in the `Debug-iphonesimulator` folder:

```bash
ditto -c -k --sequesterRsrc --keepParent {{MyApp}}.app {{MyApp}}.zip
```

## Preparing an Android app for emulators
<a name="test-runs-android-emulator-app"></a>

An Android emulator runs the same `.apk` file that you upload for physical Android devices.

Emulators run Android 15, 16, and 17. These versions refuse to install an app whose `targetSdk` is lower than 24. The emulator is a 64 bit `x86_64` device. If your app includes native libraries, include an `x86_64` build of them.

## Re-signing apps
<a name="test-runs-app-resigning"></a>

### Physical devices
<a name="test-runs-app-resigning-physical"></a>

For iOS device builds, you do not need to add any Device Farm UUIDs to your provisioning profile. Device Farm replaces the embedded provisioning profile with a wildcard profile and then re-signs the app. If you provide auxiliary data, Device Farm adds it to the app's package before Device Farm installs it, so that the auxiliary exists in your app's sandbox. Re-signing the app removes entitlements such as App Group, Associated Domains, Game Center, HealthKit, HomeKit, Wireless Accessory Configuration, In-App Purchase, Inter-App Audio, Apple Pay, Push Notifications, and VPN Configuration & Control.

For Android apps, whether Device Farm re-signs the app in a test run depends on the test host and on whether you use public or private devices. For remote access sessions, see [Re-signing apps in sessions](sessions.md#session-resigning-apps). For more information about test hosts, see [Hosts for custom test environments](custom-test-environments-hosts.md). The following table shows the re-signing behavior for each test host.


**Android app re-signing by test host**  

| Test host | Public devices | Private devices | 
| --- | --- | --- | 
| amazon\_linux\_2023 | Not re-signed by default. You can opt in to re-signing. | Not re-signed by default. You can opt in to re-signing. | 
| amazon\_linux\_2 | Always re-signed. | Re-signed by default. You can skip re-signing. | 

To change the default for a test run, where the table shows a choice, select or clear **Skip app re-signing** under **Additional configuration**, or set `skipAppResign` to `true` or `false` in the `executionConfiguration` of your `ScheduleRun` request. For more information, see [Skipping app re-signing on private devices in AWS Device Farm](skip-app-re-signing-on-private-devices.md).

When Device Farm skips re-signing, it installs your app and test package exactly as you uploaded them. Sign them yourself before you upload. For instrumentation tests, sign both with the same certificate.

When Device Farm re-signs the app, any functionality that depends on the app's signature, such as the Google Maps Android API, might break. Re-signing might also trigger antipiracy or antitamper detection from products such as DexGuard.

### Simulators and emulators
<a name="test-runs-app-resigning-simulators-emulators"></a>

Device Farm does not re-sign iOS simulator builds. If you omit `skipAppResign` for a run on simulators, Device Farm treats it as `true`. A request that sets `skipAppResign` to `false` for a run on simulators is rejected.

Android emulators run on the amazon\_linux\_2023 test host, so its row in the table applies to them: Device Farm does not re-sign the app by default, and you can opt in to re-signing.

## Obfuscated apps in runs
<a name="test-runs-obfuscated-apps"></a>

For Android apps, if the app is obfuscated, you can still test it with Device Farm if you use ProGuard. However, if you use DexGuard with antipiracy measures, Device Farm cannot re-sign and run tests against the app.