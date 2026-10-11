

# The Companion App
<a name="the-companion-app"></a>

The companion app is a native iOS application built with SwiftUI. It is the driver-facing and customer-facing surface of the platform: where a fleet console shows an operator every vehicle in a fleet, the companion app shows one person the one vehicle that is theirs, plus the journey surfaces for acquiring the next one.

It is not deployed by a CloudFormation stack. It is built and installed as a mobile application, and it consumes APIs that the AVX stacks and the companion Connected Mobility (CMS) stacks already expose. The app uses only Apple frameworks — SwiftUI, AVFoundation, LocalAuthentication, CryptoKit — and carries no third-party package dependencies, so a clone builds without a package resolution step.

Two properties shape almost every design decision in the chapters below, and both come from the platform rather than from iOS:
+  **Voice runs on a hard latency budget.** Amazon Nova 2 Sonic expects a tool call to return in about one second, and closes an idle session after 55. The app is built around both numbers. See [the tool-completion window](ts-nova-tool-window.md).
+  **The app narrates decisions it does not make.** Triage classification, warranty verdicts, payment authorization and disclosure copy are decided server-side by deterministic components, and the app renders their output rather than re-deriving it. Where the app appears to make a judgement, it is deciding **when to ask**, never **what the answer is**.

![Sign-in screen](https://docs.aws.amazon.com/guidance/latest/agentic-vehicle-experience-on-aws/images/avx-ios-signin.png)


Sign-in. The email is pre-filled from build configuration in debug builds. The password field is **empty** here — its placeholder renders as dots — and **Sign In** stays disabled until a password is present, which is why it appears greyed. A demo password may be supplied through an untracked local configuration file for debug builds; it is never committed, and release builds carry no demo credential at all.

For the journey surfaces as a visual walkthrough — alerts, booking, the P0 card, and the Buy flow — see [The Customer Journey](the-customer-journey.md), which carries those screens rather than repeating them here.