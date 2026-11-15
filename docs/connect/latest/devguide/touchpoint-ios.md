

# Touchpoint SDK for iOS
<a name="touchpoint-ios"></a>

The Touchpoint SDK for iOS is the native Swift counterpart of the [Touchpoint](touchpoint.md) web SDK. It brings the same capabilities to iOS apps — chat, voice, and **Live Sync**, the native technology that keeps a voice or chat conversation in sync with your on-screen interface — as SwiftUI views and Swift APIs.

The SDK is distributed through Swift Package Manager. The following `Package.swift` excerpt adds the package and its products to your app. Replace {{REPLACE\_WITH\_VERSION}} with the SDK version that you want to use.

```
// Package.swift
dependencies: [
    .package(url: "https://github.com/amazon-connect/touchpoint-ios", from: "REPLACE_WITH_VERSION"),
],
targets: [
    .target(
        name: "MyApp",
        dependencies: [
            .product(name: "TouchpointChat", package: "touchpoint-ios"),
            .product(name: "TouchpointVoice", package: "touchpoint-ios"),
            .product(name: "TouchpointLiveSync", package: "touchpoint-ios"),
        ]
    ),
]
```

In Xcode, you can instead choose **File**, **Add Package Dependencies**, enter the repository URL, and select the products your app needs.

**Important**  
The Touchpoint SDK for iOS is open source. For the source code, see the [touchpoint-ios repository](https://github.com/amazon-connect/touchpoint-ios) on the GitHub website. The repository contains the full source, the API documentation for every public type, and a sample banking app that shows a complete integration.

**Topics**
+ [What the Touchpoint SDK for iOS provides](#touchpoint-ios-what-provides)
+ [Requirements](#touchpoint-ios-requirements)
+ [Prerequisites](#touchpoint-ios-prerequisites)
+ [Permissions and app configuration](#touchpoint-ios-permissions)
+ [Examples](#touchpoint-ios-examples)
+ [Theming and localization](#touchpoint-ios-customization)
+ [API reference](#touchpoint-ios-api-reference)
+ [License](#touchpoint-ios-license)

## What the Touchpoint SDK for iOS provides
<a name="touchpoint-ios-what-provides"></a>

Unlike the web SDK, which exposes a single `create()` function and an `input` option, the iOS SDK is split into separately linkable Swift Package Manager products. Your app links only the products it uses, so a chat-only app never includes the voice media stack.

The following table lists the products and what each one provides.


| Product | What it provides | Web equivalent | 
| --- | --- | --- | 
| TouchpointCore | The session, the credential and backend protocols, conversation storage, and theme tokens. Every other product depends on it, so you don't add it directly. | Not applicable | 
| TouchpointChat | Chat with an Amazon Connect Customer contact, including the transcript UI and chat push notifications. Connects through your StartChatContact backend. | input: "text" | 
| TouchpointVoice | Outbound in-app calling with CallKit integration, a full-screen call view, and a compact in-app call control. Connects through your StartWebRTCContact backend. | input: "voice" and input: "voiceMini" | 
| TouchpointLiveSync | A Live Sync client with no UI of its own, plus a declarative API for advertising actions from your SwiftUI views. You can bind it to a chat or voice contact that your app starts, or to any other live contact, such as a phone call. | liveSync and input: "external" | 

Live Sync is native Amazon Connect Customer technology that synchronizes a conversation with a digital, on-screen interface. Only Live Sync requires an Agentic CX Designer (ACXD) application; plain chat and voice don't need it. For more information about ACXD, see the [Amazon CX Designer SDK](acxd-sdk.md) chapter in this guide and [Agentic CX designer (ACXD)](https://docs.aws.amazon.com/connect/latest/adminguide/acxd.html) in the *Amazon Connect Administrator Guide*.

## Requirements
<a name="touchpoint-ios-requirements"></a>
+ iOS 17.0 or later
+ Swift 6 (Swift tools version 6.0)
+ Xcode 16 or later
+ SwiftUI. The chat and voice views are SwiftUI views. A UIKit app can host them in a `UIHostingController`.

## Prerequisites
<a name="touchpoint-ios-prerequisites"></a>

To run Touchpoint for iOS you need an Amazon Connect Customer instance with a contact flow, plus a backend that your app can call to create contacts. Gather the following before you build a session.


| What you need | Where it comes from | 
| --- | --- | 
| StartChatContact backend (chat) | An authenticated endpoint that calls Amazon Connect's StartChatContact and returns participant credentials. You can start from the [StartChatContact API sample](https://github.com/amazon-connect/amazon-connect-chat-ui-examples/tree/master/cloudformationTemplates/startChatContactAPI) on the GitHub website. Your app calls it from TouchpointBackend.startChatContact(\_:). Required for TouchpointChat. | 
| StartWebRTCContact backend (voice) | An authenticated endpoint that calls StartWebRTCContact and returns the Amazon Chime SDK connection data. You can start from the [StartWebRTCContact sample](https://github.com/amazon-connect/amazon-connect-in-app-calling-examples/tree/main/Backend/AmazonConnectNetraApiSample) on the GitHub website. Your app calls it from TouchpointBackend.startVoiceContact(\_:). Required for TouchpointVoice. | 
| Instance ID and Contact Flow ID | The Amazon Connect Customer instance (UUID) and contact flow (UUID) that handle the contact. Your backend adds them to its StartChatContact and StartWebRTCContact requests; the app doesn't need to hold them. | 
| Region | AWS Region of your instance, for example us-west-2. Passed to the chat transport and to LiveSyncConfiguration. | 

### Implementing the backend protocol
<a name="touchpoint-ios-backend"></a>

The web SDK takes endpoint URLs in its configuration. The iOS SDK instead asks your app to implement the `TouchpointBackend` protocol. Anything compiled into an app binary is public. For this reason, the SDK has no production API that accepts AWS credentials or a Live Sync API key directly. Your implementation calls your own authenticated backend, which holds the AWS credentials and calls Amazon Connect on the server.

```
import TouchpointCore

struct MyBackend: TouchpointBackend {
    // Calls your backend, which calls StartChatContact.
    func startChatContact(_ request: ChatContactRequest) async throws -> ChatContactCredentials {
        let reply = try await MyAPI.startChat(displayName: request.displayName,
                                              attributes: request.attributes)
        return ChatContactCredentials(contactID: reply.contactId,
                                      participantID: reply.participantId,
                                      participantToken: reply.participantToken,
                                      expiresAt: reply.expiresAt)
    }

    // Calls your backend, which calls StartWebRTCContact.
    func startVoiceContact(_ request: VoiceContactRequest) async throws -> VoiceContactCredentials {
        let reply: [String: Any] = try await MyAPI.startWebRTCContact(request)
        return try VoiceContactCredentials(fromBackendReply: reply)
    }

    // Returns the ACXD deployment key and API key, only if you use Live Sync.
    func liveSyncCredentials() async throws -> LiveSyncCredentials {
        let keys = try await MyAPI.liveSyncKeys()
        return LiveSyncCredentials(deploymentKey: keys.deploymentKey,
                                   apiKey: keys.apiKey,
                                   expiresAt: nil)
    }
}
```

Don't put secrets in `ChatContactRequest.attributes`; the SDK forwards attributes to `StartChatContact` as contact attributes.

### Setting up Amazon Connect Customer
<a name="touchpoint-ios-setup-connect"></a>

1. **Create a contact flow** in your Amazon Connect Customer instance that handles the contact; note the **instance ID** and **contact flow ID**.

1. **Stand up the backend endpoints** that your `TouchpointBackend` calls — the `StartChatContact` (chat) and `StartWebRTCContact` (voice) endpoints listed in [Prerequisites](#touchpoint-ios-prerequisites). Authenticate calls to them the way your app authenticates its other API calls.

### Adding Live Sync (optional)
<a name="touchpoint-ios-setup-livesync"></a>

Live Sync requires an ACXD application. Build and publish it, and route your contact flow into it, as described in [Adding Live Sync (optional)](touchpoint.md#touchpoint-setup-livesync) for the web SDK. Then return the application's **deployment key** and **API key** from your backend's `liveSyncCredentials()` implementation instead of embedding them in the app.

## Permissions and app configuration
<a name="touchpoint-ios-permissions"></a>

The SDK never requests a permission unless your app opts in, and it reports a denied permission as a state in the UI rather than as a crash. Configure your app target as follows.


| Setting | When it's required | 
| --- | --- | 
| NSMicrophoneUsageDescription (Info.plist) | Voice. Explain why your app uses the microphone. If the customer denies access, the call view offers a link to Settings. | 
| UIBackgroundModes with audio (Info.plist) | Voice, so a call keeps its audio when the app moves to the background. If the mode is missing, the call reports an invalidConfiguration error. | 
| Push Notifications capability | Optional. Chat push notifications while the app is in the background. Register for remote notifications in your app delegate and forward the device token to your backend through the PushTokenRegistering protocol. | 

Calls are outbound only and use CallKit, so they appear in the system call UI. Each SDK product includes its own privacy manifest (`PrivacyInfo.xcprivacy`). The Amazon Connect chat SDK that `TouchpointChat` links also includes a privacy manifest; review it when you answer the App Store privacy questions for your app.

## Examples
<a name="touchpoint-ios-examples"></a>

Every example starts from a `TouchpointSession`. A session coordinates one active contact. It uses a `CredentialBroker` that wraps your backend, a `ConversationStore` that keeps the transcript on the device, and one transport for each modality.

### Chat
<a name="touchpoint-ios-example-chat"></a>

The following example builds a session with the chat transport, starts a chat contact, and presents the chat view as a sheet. Replace {{REPLACE\_WITH\_CUSTOMER\_NAME}} with the customer's display name, which the agent sees.

```
import SwiftUI
import TouchpointCore
import TouchpointChat

let keychain = SecurityFrameworkKeychainStore(service: "com.example.myapp")
let storeURL = try FileManager.default
    .url(for: .applicationSupportDirectory, in: .userDomainMask, appropriateFor: nil, create: true)
    .appending(path: "Touchpoint", directoryHint: .isDirectory)
let store = try await ConversationStore(containerURL: storeURL, keychain: keychain)

let broker = CredentialBroker(backend: MyBackend(), keychain: keychain)
let chat = try ConnectChatTransport.live(regionName: "us-east-1")
let session = TouchpointSession(broker: broker, store: store, transports: [.chat: chat])

try await session.startChat(ChatContactRequest(displayName: "REPLACE_WITH_CUSTOMER_NAME",
                                               attributes: [:]))

// In your view:
struct SupportButton: View {
    let session: TouchpointSession
    @State private var showChat = false

    var body: some View {
        Button("Chat with us") { showChat = true }
            .touchpointChat(session: session, isPresented: $showChat)
    }
}
```

To place the chat in your own container instead of a sheet, use `TouchpointChatView(session:)`. To present it in a floating window similar to the web widget, use the `.touchpointChatWindow(isPresented:mode:panel:)` modifier. It supports full, half, and mini sizes. You can customize bubbles, participant names, the assistant name and icon, and the welcome screen with `TouchpointChatOptions`.

### Voice
<a name="touchpoint-ios-example-voice"></a>

Voice uses a separate session with the voice transport. Create a `TouchpointVoiceCall` and show it in `TouchpointVoiceView`, the full-screen call experience. When the view appears, it starts the call. It asks for the microphone if the call's permission policy allows it.

In the following example, replace {{REPLACE\_WITH\_YOUR\_APP\_NAME}} with your app's name, which appears in the system call UI.

```
import SwiftUI
import TouchpointCore
import TouchpointVoice

let voice = VoiceTransport()
let voiceSession = TouchpointSession(broker: broker, store: store, transports: [.voice: voice])

let call = TouchpointVoiceCall(session: voiceSession,
                               transport: voice,
                               displayName: "REPLACE_WITH_YOUR_APP_NAME",   // shown in the system call UI
                               permissionPolicy: PermissionPolicy(mayRequest: [.microphone]))

// In your view:
.fullScreenCover(isPresented: $showCall) {
    TouchpointVoiceView(call: call, onClose: { showCall = false })
}
```

For a compact control that stays on screen while the customer keeps using your app, the `TouchpointVoice` product also includes `TouchpointVoiceMiniRail`. You can start the call yourself with `call.start()` and observe it with `call.onStateChange`.

### Live Sync
<a name="touchpoint-ios-example-livesync"></a>

Live Sync is native Amazon Connect Customer technology that synchronizes a voice or chat conversation with a digital, on-screen interface. As on the web, the AI agent drives your app through **custom actions**: you advertise a named action with a JSON Schema, the agent resolves what the customer said into typed arguments, and your handler applies them to the screen.

Create a `LiveSyncClient` for the contact you want to mirror. Its `conversationId` is the Amazon Connect contact ID — for example, `session.contactID` after a chat starts. The client gets the Live Sync keys from your backend through the credential broker. The following example creates a client, handles an action, and advertises it to the AI agent.

```
import TouchpointLiveSync

let client = LiveSyncClient(
    configuration: try LiveSyncConfiguration(
        region: "us-east-1",
        conversationId: contactID,                    // the contact to sync with
        channel: try LiveSyncChannel(locale: .current)
    ),
    credentials: broker,       // fetches the deployment key and API key from MyBackend
    consent: .held,            // nothing is sent until the customer grants consent
    autoConnect: false
)

client.onAction = { invocation in
    switch invocation.action {
    case "set_cabin_class":
        let choice = try invocation.decode(CabinChoice.self)
        setCabinClass(choice.cabin)
    default:
        break
    }
}
client.connect()

// Advertise the actions the AI agent may take. Each call replaces the previous set.
try await client.sendContext(actions: [
    LiveSyncAction("set_cabin_class",
                   description: "Choose the cabin class",
                   schema: ["type": "object",
                            "properties": ["cabin": ["type": "string",
                                                     "enum": ["economy", "business", "first"]]],
                            "required": ["cabin"]])
])
```

Instead of maintaining the action list by hand, you can declare actions on the SwiftUI views that handle them. An action is advertised while its view is on screen and withdrawn when the view goes away, so the context always matches what the customer sees. The following example declares an action on a SwiftUI view.

```
import SwiftUI
import TouchpointLiveSync

struct DisputeDetails: TouchpointActionPayload {
    var reason: String?
    var amount: Double?
    static let schema: JSONValue = .object(["type": "object", "properties": [
        "reason": ["type": "string"],
        "amount": ["type": "number"],
    ]])
}

let aggregator = TouchpointActionAggregator(post: { try await client.sendContext($0) })
client.onAction = { try aggregator.route($0) }

// Once, at the root of the views that declare actions:
RootView()
    .touchpointLiveSync(aggregator)

// On any view below it:
DisputeForm(model: model)
    .touchpointScope("dispute")
    .touchpointAction("set_dispute_details",
                      description: "Fill in the dispute form with what the customer said") {
        (details: DisputeDetails) in model.apply(details)
    }
```

Make every payload field optional; the agent sends only what the customer said. Actions can also be configured in [Agentic CX designer (ACXD)](https://docs.aws.amazon.com/connect/latest/adminguide/acxd.html) on the Live Sync node; defining them in the app is useful for rapid prototyping.

When a human agent joins the contact, the client can suspend action delivery; observe this with `client.onDispatchStateChange`.

#### Live Sync consent
<a name="touchpoint-ios-example-consent"></a>

Live Sync shares what is on the customer's screen with the AI agent. The client starts with consent `.held` and sends no context until the customer grants it. Use `LiveSyncConsentController` to store the decision for each deployment, and show the SDK's `LiveSyncConsentSheet` – or your own view — when the controller needs an answer. In the following example, replace {{REPLACE\_WITH\_DEPLOYMENT\_ID}} with an identifier for your ACXD deployment, and {{REPLACE\_WITH\_YOUR\_COMPANY}} with your company name as customers know it.

```
let consent = LiveSyncConsentController(
      client: client,
      store: ConsentStore(keychain: keychain, deploymentID: "REPLACE_WITH_DEPLOYMENT_ID"),
      prompt: ConsentPrompt(
          dataDescription: "which screen you're on and what you can do there",
          recipient: "REPLACE_WITH_YOUR_COMPANY's assistant",
          privacyPolicyURL: URL(string: "https://example.com/privacy")))

  // In your view:
  .sheet(isPresented: .constant(consent.needsPrompt)) {
      LiveSyncConsentSheet(controller: consent)
  }
```

To give customers a way to stop sharing at any time, add `LiveSyncConsentRevokeButton(controller:)` to a settings screen or to your support UI. Revoking consent closes the Live Sync connection and clears the advertised context immediately; chat and voice continue.

#### Live Sync without chat or voice
<a name="touchpoint-ios-example-external"></a>

The equivalent of the web SDK's `input: "external"` mode is to link only `TouchpointLiveSync` and create a `LiveSyncClient` for a contact that your app didn't start. A common case is a **phone call**: the caller talks to the agent while your app updates alongside them. No chat or voice backend is needed — only the Live Sync credentials and the contact ID.

Your app needs a way to learn the contact ID. The SDK defines a `TouchpointContactIDResolver` protocol and includes a deep-link resolver as a reference. For production, resolve the contact ID through your authenticated backend. Anyone who has an unauthenticated link can bind to the conversation.

## Theming and localization
<a name="touchpoint-ios-customization"></a>

The SDK's theme tokens have the same shape as the web SDK's, so a brand configured once looks the same on both. Pass a `TouchpointTheme` with the `.touchpointTheme(_:)` modifier, or to the `theme` parameter of a chat view. The theme is propagated through the SwiftUI environment only, so it never restyles the rest of your app.
+ **Dark Mode** – every color token has a light and a dark value and follows the system appearance.
+ **Dynamic Type** – text and spacing scale with the customer's text size. A custom `fontFamily` changes the typeface only.
+ **Accessibility** – the views support VoiceOver and honor Reduce Motion.
+ **Localization** – the SDK's strings are in a String Catalog that includes the web SDK's translations. Live Sync maps the session locale to a Live Sync channel, so make sure the channel you pass to `LiveSyncChannel` matches a language that your ACXD application supports.

## API reference
<a name="touchpoint-ios-api-reference"></a>

Every public type is documented in source, and the [touchpoint-ios repository](https://github.com/amazon-connect/touchpoint-ios) on the GitHub website contains the full API documentation and a sample banking app. The following list describes common entry points.
+ `TouchpointBackend` – the protocol your app implements to create contacts and vend Live Sync credentials.
+ `TouchpointSession` – coordinates one contact; `startChat(_:)`, `startVoice(_:)`, `end()`, and resume after a relaunch.
+ `TouchpointChatView`, `.touchpointChat(session:isPresented:)`, and `TouchpointChatOptions` – the chat UI and its options.
+ `TouchpointVoiceCall` and `TouchpointVoiceView` – the call and its full-screen UI.
+ `LiveSyncClient`, `LiveSyncConfiguration`, `.touchpointAction`, and `LiveSyncConsentController` – the Live Sync connection, declarative actions, and consent.
+ `TouchpointError` and `LiveSyncError` – the errors the SDK throws or reports. For example, `LiveSyncError.contactMayBeStale` indicates that the Live Sync connection is open but the contact ID likely no longer refers to a live contact.

## License
<a name="touchpoint-ios-license"></a>

The Touchpoint SDK for iOS is open source. For license terms, see the [LICENSE file](https://github.com/amazon-connect/touchpoint-ios/blob/main/LICENSE) in the touchpoint-ios repository on the GitHub website.