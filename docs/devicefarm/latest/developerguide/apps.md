

# Apps in AWS Device Farm
<a name="apps"></a>

The following sections contain information about app behaviors in Device Farm.

**Topics**
+ [Instrumenting apps](#test-runs-instrumenting)
+ [Re-signing apps](#test-runs-app-resigning)
+ [Obfuscated apps in runs](#test-runs-obfuscated-apps)

## Instrumenting apps
<a name="test-runs-instrumenting"></a>

You do not need to instrument your apps or provide Device Farm with the source code for your apps. Android apps can be submitted unmodified. iOS apps must be built with the **iOS Device** target instead of with the simulator.

## Re-signing apps
<a name="test-runs-app-resigning"></a>

For iOS apps, you do not need to add any Device Farm UUIDs to your provisioning profile. Device Farm replaces the embedded provisioning profile with a wildcard profile and then re-signs the app. If you provide auxiliary data, Device Farm adds it to the app's package before Device Farm installs it, so that the auxiliary exists in your app's sandbox. Re-signing the app removes entitlements such as App Group, Associated Domains, Game Center, HealthKit, HomeKit, Wireless Accessory Configuration, In-App Purchase, Inter-App Audio, Apple Pay, Push Notifications, and VPN Configuration & Control.

For Android apps, whether Device Farm re-signs the app in a test run depends on the test host and on whether you use public or private devices. For remote access sessions, see [Re-signing apps in sessions](sessions.md#session-resigning-apps). For more information about test hosts, see [Hosts for custom test environments](custom-test-environments-hosts.md). The following table shows the re-signing behavior for each test host.


**Android app re-signing by test host**  

| Test host | Public devices | Private devices | 
| --- | --- | --- | 
| amazon\_linux\_2023 | Not re-signed by default. You can opt in to re-signing. | Not re-signed by default. You can opt in to re-signing. | 
| amazon\_linux\_2 | Always re-signed. | Re-signed by default. You can skip re-signing. | 

To change the default for a test run, where the table shows a choice, select or clear **Skip app re-signing** under **Additional configuration**, or set `skipAppResign` to `true` or `false` in the `executionConfiguration` of your `ScheduleRun` request. For more information, see [Skipping app re-signing on private devices in AWS Device Farm](skip-app-re-signing-on-private-devices.md).

When Device Farm skips re-signing, it installs your app and test package exactly as you uploaded them. Sign them yourself before you upload. For instrumentation tests, sign both with the same certificate.

When Device Farm re-signs the app, any functionality that depends on the app's signature, such as the Google Maps Android API, might break. Re-signing might also trigger antipiracy or antitamper detection from products such as DexGuard.

## Obfuscated apps in runs
<a name="test-runs-obfuscated-apps"></a>

For Android apps, if the app is obfuscated, you can still test it with Device Farm if you use ProGuard. However, if you use DexGuard with antipiracy measures, Device Farm cannot re-sign and run tests against the app.