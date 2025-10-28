# Apps in AWS Device Farm

The following sections contain information about app behaviors in Device Farm.

###### Topics

- [Instrumenting apps](#test-runs-instrumenting "#test-runs-instrumenting")
- [Re-signing apps in runs](#test-runs-app-resigning "#test-runs-app-resigning")
- [Obfuscated apps in runs](#test-runs-obfuscated-apps "#test-runs-obfuscated-apps")

## Instrumenting apps

You do not need to instrument your apps or provide Device Farm with the source code for your
apps. Android apps can be submitted unmodified. iOS apps must be built with the
**iOS Device** target instead of with the simulator.

## Re-signing apps in runs

For iOS apps, you do not need to add any Device Farm UUIDs to your provisioning profile.
Device Farm replaces the embedded provisioning profile with a wildcard profile and then
re-signs the app. If you provide auxiliary data, Device Farm adds it to the app's package
before Device Farm installs it, so that the auxiliary exists in your app's sandbox. Re-signing
the app removes entitlements such as App Group, Associated Domains, Game Center,
HealthKit, HomeKit, Wireless Accessory Configuration, In-App Purchase, Inter-App Audio,
Apple Pay, Push Notifications, and VPN Configuration & Control.

For Android apps, Device Farm re-signs the app. This might break any functionality that
depends on the app's signature, such as the Google Maps Android API, or it might trigger
antipiracy or antitamper detection from products such as DexGuard.

## Obfuscated apps in runs

For Android apps, if the app is obfuscated, you can still test it with Device Farm if you
use ProGuard. However, if you use DexGuard with antipiracy measures, Device Farm cannot
re-sign and run tests against the app.
