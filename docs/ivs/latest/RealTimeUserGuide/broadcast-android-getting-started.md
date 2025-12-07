# Getting Started​ with the IVS

Android Broadcast SDK | Real-Time Streaming

This document takes you through the steps involved in getting started with the IVS
real-time streaming Android broadcast SDK.

## Install the Library

There are several ways to add the Amazon IVS Android broadcast library to your
Android development environment: use Gradle directly, use Gradle version catalogs,
or install the SDK manually.

**Use Gradle directly**: Add the library to your
module’s `build.gradle` file, as shown here (for the latest version of
the IVS broadcast SDK):

```
repositories {
    mavenCentral()
}

dependencies {
     implementation 'com.amazonaws:ivs-broadcast:1.37.0:stages@aar'
}
```

**Use Gradle version catalogs**: First include this
in your module’s `build.gradle` file:

```
implementation(libs.ivs){
   artifact {
      classifier = "stages"
      type = "aar"
   }
}
```

Then include the following in the `libs.version.toml` file (for the
latest version of the IVS broadcast SDK):

```
[versions]
ivs="1.37.0"

[libraries]
ivs = {module = "com.amazonaws:ivs-broadcast", version.ref = "ivs"}

```

**Install the SDK manually**: Download the latest
version from this location:

[https://search.maven.org/artifact/com.amazonaws/ivs-broadcast](https://search.maven.org/artifact/com.amazonaws/ivs-broadcast "https://search.maven.org/artifact/com.amazonaws/ivs-broadcast")

Be sure to download the `aar` with `-stages`
appended.

**Also allow SDK control over the speakerphone**:
Regardless of which installation method you choose, also add the following
permission to your manifest, to allow the SDK to enable and disable the
speakerphone:

```
<uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS"/>
```

## Using the SDK with Debug

Symbols

We also publish a version of the Android broadcast SDK which includes debug
symbols. You can use this version to improve the quality of debug reports (stack
traces) in Firebase Crashlytics, if you run into crashes in the IVS broadcast SDK;
i.e., `libbroadcastcore.so`. When you report these crashes to the IVS SDK
team, the higher quality stack traces make it easier to fix the issues.

To use this version of the SDK, put the following in your Gradle build
files:

```
implementation "com.amazonaws:ivs-broadcast:$version:stages-unstripped@aar"
```

Use the above line instead of this:

```
implementation "com.amazonaws:ivs-broadcast:$version:stages@aar"
```

### Uploading

Symbols to Firebase Crashlytics

Ensure that your Gradle build files are set up for Firebase Crashlytics.
Follow Google’s instructions here:

[https://firebase.google.com/docs/crashlytics/ndk-reports](https://firebase.google.com/docs/crashlytics/ndk-reports "https://firebase.google.com/docs/crashlytics/ndk-reports")

Be sure to include `com.google.firebase:firebase-crashlytics-ndk`
as a dependency.

When building your app for release, the Firebase Crashlytics plugin should
upload symbols automatically. To upload symbols manually, run either of the
following:

```
gradle uploadCrashlyticsSymbolFileRelease
```

```
./gradlew uploadCrashlyticsSymbolFileRelease
```

(It will not hurt if symbols are uploaded twice, both automatically and
manually.)

### Preventing your Release

.apk from Becoming Larger

Before packaging the release `.apk` file, the Android Gradle Plugin
automatically tries to strip debug information from shared libraries (including
the IVS broadcast SDK's `libbroadcastcore.so` library). However,
sometimes this does not happen. As a result, your `.apk` file could
become larger and you could get a warning message from the Android Gradle Plugin
that it’s unable to strip debug symbols and is packaging `.so` files
as is. If this happens, do the following:

- Install an Android NDK. Any recent version will work.
- Add `ndkVersion <your_installed_ndk_version_number>` to
  your application’s `build.gradle` file. Do this even if your
  application itself does not contain native code.

For more information, see this [issue
report](https://issuetracker.google.com/issues/353554169 "https://issuetracker.google.com/issues/353554169").

## Request Permissions

Your app must request permission to access the user’s camera and mic. (This is not
specific to Amazon IVS; it is required for any application that needs access to
cameras and microphones.)

Here, we check whether the user has already granted permissions and, if not, ask
for them:

```
final String[] requiredPermissions =
         { Manifest.permission.CAMERA, Manifest.permission.RECORD_AUDIO };

for (String permission : requiredPermissions) {
    if (ContextCompat.checkSelfPermission(this, permission)
                != PackageManager.PERMISSION_GRANTED) {
        // If any permissions are missing we want to just request them all.
        ActivityCompat.requestPermissions(this, requiredPermissions, 0x100);
        break;
    }
}
```

Here, we get the user’s response:

```
@Override
public void onRequestPermissionsResult(int requestCode,
                                      @NonNull String[] permissions,
                                      @NonNull int[] grantResults) {
    super.onRequestPermissionsResult(requestCode,
               permissions, grantResults);
    if (requestCode == 0x100) {
        for (int result : grantResults) {
            if (result == PackageManager.PERMISSION_DENIED) {
                return;
            }
        }
        setupBroadcastSession();
    }
}
```
