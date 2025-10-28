# Sessions in AWS Device Farm

You can use Device Farm to perform interactive testing of Android and iOS apps through remote
access sessions in a web browser. This kind of interactive testing helps support engineers
on a customer call to walk through, step by step, the customer's issue. Developers can
reproduce a problem on a specific device to isolate possible sources of the problem. You can
use remote sessions to conduct usability tests with your target customers.

###### Topics

- [Supported devices for remote access](#session-devices-supported "#session-devices-supported")
- [Session files retention](#session-files-retention "#session-files-retention")
- [Instrumenting apps](#session-instrumenting "#session-instrumenting")
- [Re-signing apps in sessions](#session-resigning-apps "#session-resigning-apps")
- [Obfuscated apps in sessions](#session-obfuscated-apps "#session-obfuscated-apps")

## Supported devices for remote access

Device Farm provides support for a number of unique, popular Android and iOS devices. The
list of available devices grows as new devices enter the market. The Device Farm console
displays the current list of Android and iOS devices available for remote access. For
more information, see [Device support in AWS Device Farm](devices.md "devices.md").

## Session files retention

Device Farm stores your apps and files for 30 days and then deletes them from its system.
You can delete your files at any time, however.

Device Farm stores your session logs and captured video for 400 days and then deletes them
from its system.

## Instrumenting apps

You do not need to instrument your apps or provide Device Farm with the source code for your
apps. Android and iOS apps can be submitted unmodified.

## Re-signing apps in sessions

Device Farm re-signs Android and iOS apps. This can break functionality that depends on
the app's signature. For example, the Google Maps API for Android depends on your app's
signature. App re-signing can also trigger antipiracy or antitamper detection from
products such as DexGuard for Android devices.

## Obfuscated apps in sessions

For Android apps, if the app is obfuscated, you can still test it with Device Farm if you
use ProGuard. However, if you use DexGuard with antipiracy measures, Device Farm cannot
re-sign the app.
