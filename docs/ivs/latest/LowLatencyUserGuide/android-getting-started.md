# Getting Started with the IVS Android Player SDK

This document takes you through the steps involved in getting started with the Amazon IVS Android player SDK.

## Install the Library

To add the Amazon IVS Android player library to your Android development
environment, add the library to your module’s `build.gradle` file, as
shown here (for the latest version of the Amazon IVS player).

```
repositories {
    mavenCentral()
}

dependencies {
     implementation 'com.amazonaws:ivs-player:1.46.0'
}
```

Alternately, to install the SDK manually, download the latest version from this
location:

- [https://search.maven.org/artifact/com.amazonaws/ivs-player](https://search.maven.org/artifact/com.amazonaws/ivs-player "https://search.maven.org/artifact/com.amazonaws/ivs-player")

## Using the SDK with Debug Symbols

We also publish a version of the Android player SDK which includes debug symbols.
You can use this version to improve the quality of debug reports (stack traces) in
Firebase Crashlytics, if you run into crashes in the IVS player SDK; i.e.,
`libplayercore.so`. When you report these crashes to the IVS SDK team, the higher
quality stack traces make it easier to fix the issues.

To use this version of the SDK, in your Gradle build files, replace this
line:

```
implementation "com.amazonaws:ivs-player:$version@aar"
```

with this:

```
implementation "com.amazonaws:ivs-player:$version:unstripped@aar"
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

Before packaging the release `.apk` file, the Android Gradle Plugin
automatically tries to strip debug information from shared libraries (including
the IVS player SDK's `libplayercore.so` library). However, sometimes this does not
happen. In that case, your `.apk` file could become larger and you could get a
warning message from the Android Gradle Plugin that it’s unable to strip debug
symbols and is packaging `.so` files as is. If this happens, do the
following:

- Install an Android NDK. Any recent version will work.
- Add `ndkVersion <your_installed_ndk_version_number>` to
  your application’s `build.gradle` file. Do this even if
  your application itself does not contain native code.

For more information, see this [issue report](https://issuetracker.google.com/issues/353554169 "https://issuetracker.google.com/issues/353554169").

## Create the Player and Set Up Event

Listener

The player interface is `com.amazonaws.ivs.player.Player`. Initialize
it as shown below:

```
// Create a player instance
// <this> refers to the current Android Activity
player = Player.Factory.create(this);

// Set up to receive playback events and errors
player.addListener(this);
```

Alternately, initialize by using `PlayerView`:

```
// Create a player instance
// <this> refers to the current Android Activity
PlayerView playerView = new PlayerView(this);
Player player = playerView.getPlayer();
// Set up to receive playback events and errors
player.addListener(this);
```

**Note:** The listener callback methods are executed
in the main thread of your Android application.

## Set the Surface View for Video

If not using `PlayerView` add a `SurfaceView` to your
Android UI layout for displaying a video. This `Surface` must be
available before you can play any video streams. You can access the underlying
surface through the `SurfaceHolder` interface, which is retrieved by
calling `getHolder()`. (See [SurfaceView](https://developer.android.com/reference/android/view/SurfaceView.html "https://developer.android.com/reference/android/view/SurfaceView.html") in the Android developer reference). Use the
`SurfaceHolder.Callback` to receive events about surface changes (see
[SurfaceHolder.Callback](https://developer.android.com/reference/android/view/SurfaceHolder.Callback "https://developer.android.com/reference/android/view/SurfaceHolder.Callback")).

```
surfaceView = (SurfaceView) findViewById(R.id.surfaceView);
surfaceView.getHolder().addCallback(this);

@Override
public void surfaceCreated(SurfaceHolder holder) {
   this.surface = holder.getSurface();
   if (player != null) {
       player.setSurface(this.surface);
   }
}

@Override
public void surfaceDestroyed(SurfaceHolder holder) {
   this.surface = null;
   if (player != null) {
       player.setSurface(null);
   }
}
```

## Play a Stream

Because the stream is loaded asynchronously, the player must be in a
`READY` state before your application can call the `play`
method to begin playback. Use the `Player.Listener` interface to
determine when the player is in the correct state.

See the following sample code:

```
player.load(Uri.parse(url));

@Override
public void onStateChanged(Player.State state) {
    switch (state) {
        case BUFFERING:
            // player is buffering
            break;
        case READY:
            player.play();
            break;
        case IDLE:
            break;
        case PLAYING:
            // playback started
            break;
     }
}
```

## Release the Player

The `player.release()` method _must_
be called when the player is no longer in use, to free the resources used by the
library. Typically this is done in the `onDestroy` callback of the
Activity or Fragment containing the player.

```
@Override
protected void onDestroy() {
    super.onDestroy();
    player.removeListener(this);
    player.release();
}
```

After the `player.release()` method is called the player can no longer
be used.

## Permissions

The Android player SDK requires the following permission:

```
<uses-permission android:name="android.permission.INTERNET" />
```

In addition, these optional permissions can improve the playback experience:

```
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
```

## Thread Safety

The player API is not thread safe. All calls made to a player instance should be
from the same thread.

## SDK Size

The Amazon IVS player SDKs are designed to be as lightweight as possible. For current
information about SDK size, see the [Release
Notes](release-notes.md "release-notes.md").

**Important:** When evaluating size impact, the size of
the AAB/APK produced by Android Studio is not representative of the size of your app
downloaded to a user’s device. The Google Play Store performs optimizations to reduce
the size of your app. We recommend that you use [Android App Bundles](https://developer.android.com/guide/app-bundle "https://developer.android.com/guide/app-bundle") to
serve optimized apps for each device configuration.
