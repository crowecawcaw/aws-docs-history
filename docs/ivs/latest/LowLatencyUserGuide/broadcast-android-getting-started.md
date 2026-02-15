#

Getting Started​ with the IVS Android Broadcast SDK | Low-Latency Streaming

This document takes you through the steps involved in getting started with the Amazon IVS low-latency
streaming Android broadcast SDK.

## Install the Library

To add the Amazon IVS Android broadcast library to your Android development
environment, add the library to your module’s `build.gradle` file, as
shown here (for the latest version of the Amazon IVS broadcast SDK):

```
repositories {
    mavenCentral()
}
dependencies {
     implementation 'com.amazonaws:ivs-broadcast:1.39.0'
}
```

Alternately, to install the SDK manually, download the latest version from this
location:

- [https://search.maven.org/artifact/com.amazonaws/ivs-broadcast](https://search.maven.org/artifact/com.amazonaws/ivs-broadcast "https://search.maven.org/artifact/com.amazonaws/ivs-broadcast")

## Using the SDK with Debug Symbols

We also publish a version of the Android broadcast SDK which includes debug symbols. You can use this version to improve the quality of debug reports (stack traces) in Firebase Crashlytics, if you run into crashes in the IVS broadcast SDK; i.e., `libbroadcastcore.so`. When you report these crashes to the IVS SDK team, the higher quality stack traces make it easier to fix the issues.

To use this version of the SDK, put the following in your Gradle build files:

```
implementation "com.amazonaws:ivs-broadcast:$version:unstripped@aar"
```

Use the above line instead of this:

```
implementation "com.amazonaws:ivs-broadcast:$version@aar"
```

### Uploading Symbols to Firebase Crashlytics

Ensure that your Gradle build files are set up for Firebase Crashlytics. Follow Google’s instructions here:

[https://firebase.google.com/docs/crashlytics/ndk-reports](https://firebase.google.com/docs/crashlytics/ndk-reports "https://firebase.google.com/docs/crashlytics/ndk-reports")

Be sure to include `com.google.firebase:firebase-crashlytics-ndk` as a dependency.

When building your app for release, the Firebase Crashlytics plugin should upload symbols automatically. To upload symbols manually, run either of the following:

```
gradle uploadCrashlyticsSymbolFileRelease
```

```
./gradlew uploadCrashlyticsSymbolFileRelease
```

(It will not hurt if symbols are uploaded twice, both automatically and manually.)

### Preventing your Release .apk from Becoming Larger

Before packaging the release `.apk` file, the Android Gradle Plugin automatically tries to strip debug information from shared libraries (including the IVS broadcast SDK's `libbroadcastcore.so` library). However, sometimes this does not happen. As a result, your `.apk` file could become larger and you could get a warning message from the Android Gradle Plugin that it’s unable to strip debug symbols and is packaging `.so` files as is. If this happens, do the following:

- Install an Android NDK. Any recent version will work.
- Add `ndkVersion <your_installed_ndk_version_number>` to
  your application’s `build.gradle` file. Do this even if
  your application itself does not contain native code.

For more information, see this [issue report](https://issuetracker.google.com/issues/353554169 "https://issuetracker.google.com/issues/353554169").

## Create the Event

Listener

Setting up an event listener allows you to receive state updates, device-change
notifications, errors, and session-audio information.

```
BroadcastSession.Listener broadcastListener =
          new BroadcastSession.Listener() {
    @Override
    public void onStateChanged(@NonNull BroadcastSession.State state) {
        Log.d(TAG, "State=" + state);
    }

    @Override
    public void onError(@NonNull BroadcastException exception) {
        Log.e(TAG, "Exception: " + exception);
    }
};
```

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

## Create the Broadcast

Session

The broadcast interface is
`com.amazonaws.ivs.broadcast.BroadcastSession`. Initialize it with a
preset, as shown below. If there are any errors during initialization (such as a
failure to configure a codec) your `BroadcastListener` will get an error
message and `broadcastSession.isReady` will be `false`.

**Important:** All calls to the Amazon IVS Broadcast
SDK for Android _must_ be made on the thread on
which the SDK is instantiated. _A call from a different
thread will cause the SDK to throw a fatal error and stop
broadcasting_.

```
// Create a broadcast-session instance and sign up to receive broadcast
// events and errors.
Context ctx = getApplicationContext();
broadcastSession = new BroadcastSession(ctx,
                       broadcastListener,
                       Presets.Configuration.STANDARD_PORTRAIT,
                       Presets.Devices.FRONT_CAMERA(ctx));
```

Also see [Create the Broadcast
Session (Advanced Version)](broadcast-android-use-cases.md#broadcast-android-create-session-advanced "broadcast-android-use-cases.md#broadcast-android-create-session-advanced") .

## Set the ImagePreviewView

for Preview

If you want to display a preview for an active camera device, add a preview
`ImagePreviewView` for the device to your view hierarchy.

```
// awaitDeviceChanges will fire on the main thread after all pending devices
// attachments have been completed
broadcastSession.awaitDeviceChanges(() -> {
    for(Device device: session.listAttachedDevices()) {
        // Find the camera we attached earlier
        if(device.getDescriptor().type == Device.Descriptor.DeviceType.CAMERA) {
            LinearLayout previewHolder = findViewById(R.id.previewHolder);
            ImagePreviewView preview = ((ImageDevice)device).getPreviewView();
            preview.setLayoutParams(new LinearLayout.LayoutParams(
                    LinearLayout.LayoutParams.MATCH_PARENT,
                    LinearLayout.LayoutParams.MATCH_PARENT));
            previewHolder.addView(preview);
        }
    }
});
```

## Start a Broadcast

The hostname that you receive in the `ingestEndpoint` response field of
the `GetChannel` operation needs to have `rtmps://` prepended
and `/app` appended. The complete URL should be in this format:
`rtmps://{{ ingestEndpoint }}/app`

```
broadcastSession.start(IVS_RTMPS_URL, IVS_STREAMKEY);
```

The Android broadcast SDK supports only RTMPS ingest (not insecure RTMP
ingest).

## Stop a Broadcast

```
broadcastSession.stop();
```

## Release the Broadcast

Session

You _must call_ the
`broadcastSession.release()` method when the broadcast session is no
longer in use, to free the resources used by the library.

```
@Override
protected void onDestroy() {
    super.onDestroy();
    previewHolder.removeAllViews();
    broadcastSession.release();
}
```
