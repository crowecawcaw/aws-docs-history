

# Companion application
<a name="companion-app"></a>

The companion application is a native iOS app, built with SwiftUI, under `clients/ios/`. It is the driver’s surface. The Fleet Intelligence portal shows an operator every vehicle in a fleet; the companion app shows one driver the one vehicle assigned to them, with live state, alerts, remote controls, service booking, and a voice assistant.

The app is built and installed as a mobile application, not deployed by a CloudFormation stack. It calls APIs that the CMS stacks already expose, and the conversational and Findings APIs of the companion Agentic Vehicle Experience (AVX) accelerator. It uses only Apple frameworks (SwiftUI, AVFoundation, LocalAuthentication, and CryptoKit) and has no third-party package dependencies.