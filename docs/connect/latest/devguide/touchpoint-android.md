

# Touchpoint SDK for Android
<a name="touchpoint-android"></a>

The Touchpoint SDK for Android is the native Kotlin counterpart of the [Touchpoint](touchpoint.md) web SDK. It brings the same capabilities to Android apps — chat, voice, and **Live Sync**, the native technology that keeps a voice or chat conversation in sync with your on-screen interface — as Jetpack Compose UI and Kotlin coroutine APIs.

The SDK is published to Maven Central as separate modules. The following Gradle Kotlin DSL excerpt adds the modules your app needs to its `build.gradle.kts` file. Replace {{REPLACE\_WITH\_VERSION}} with the SDK version that you want to use.

```
dependencies {
    val touchpointVersion = "REPLACE_WITH_VERSION"
    implementation("software.aws.connect:touchpoint-chat:$touchpointVersion")
    implementation("software.aws.connect:touchpoint-voice:$touchpointVersion")
    implementation("software.aws.connect:touchpoint-livesync:$touchpointVersion")
}
```

**Important**  
The Touchpoint SDK for Android is open source. For the source code, see the [touchpoint-android repository](https://github.com/amazon-connect/touchpoint-android) on the GitHub website. The repository contains the full source, the API documentation for every public type, and a sample banking app that shows a complete integration.

**Topics**
+ [What the Touchpoint SDK for Android provides](#touchpoint-android-what-provides)
+ [Requirements](#touchpoint-android-requirements)
+ [Prerequisites](#touchpoint-android-prerequisites)
+ [Permissions and manifest](#touchpoint-android-permissions)
+ [Examples](#touchpoint-android-examples)
+ [Theming and localization](#touchpoint-android-customization)
+ [API reference](#touchpoint-android-api-reference)
+ [License](#touchpoint-android-license)

## What the Touchpoint SDK for Android provides
<a name="touchpoint-android-what-provides"></a>

Unlike the web SDK, which exposes a single `create()` function and an `input` option, the Android SDK is split into separately linkable Gradle modules. Your app includes only the modules it uses, so a chat-only app never includes the voice media stack.

The following table lists the modules and what each one provides.


| Module | What it provides | Web equivalent | 
| --- | --- | --- | 
| touchpoint-core, touchpoint-core-android, touchpoint-ui | The session, the credential and backend interfaces, secure on-device storage, and the shared Compose theme and controls. Other modules bring these in, so you don't add them directly. | Not applicable | 
| touchpoint-chat | Chat with an Amazon Connect Customer contact, including the transcript UI and chat push notifications. Connects through your StartChatContact backend. | input: "text" | 
| touchpoint-voice | Outbound in-app calling, a full-screen call view, and a compact floating call widget. Connects through your StartWebRTCContact backend. | input: "voice" and input: "voiceMini" | 
| touchpoint-voice-telecom (optional) | Keeps an in-app call running in the background, with a system call notification, through Jetpack core-telecom and a phone-call foreground service. | Not applicable | 
| touchpoint-livesync | A Live Sync client with no UI of its own, plus composables for advertising actions from your screens. You can bind it to a chat or voice contact that your app starts, or to any other live contact, such as a phone call. | liveSync and input: "external" | 

Live Sync is native Amazon Connect Customer technology that synchronizes a conversation with a digital, on-screen interface. Only Live Sync requires an Agentic CX Designer (ACXD) application; plain chat and voice don't need it. For more information about ACXD, see the [Amazon CX Designer SDK](acxd-sdk.md) chapter in this guide and [Agentic CX designer (ACXD)](https://docs.aws.amazon.com/connect/latest/adminguide/acxd.html) in the *Amazon Connect Administrator Guide*.

## Requirements
<a name="touchpoint-android-requirements"></a>
+ Android 12 (API level 31) or later (`minSdk 31`)
+ `compileSdk 36` or later
+ Kotlin 2.1 or later
+ Java 17 bytecode target (JDK 17 or later to build)
+ Jetpack Compose 1.11 or later for the chat and voice UI

The public API uses Kotlin suspend functions and flows, so it's designed for Kotlin callers.

## Prerequisites
<a name="touchpoint-android-prerequisites"></a>

To run Touchpoint for Android you need an Amazon Connect Customer instance with a contact flow, plus a backend that your app can call to create contacts. Gather the following before you build a session.


| What you need | Where it comes from | 
| --- | --- | 
| StartChatContact backend (chat) | An authenticated endpoint that calls Amazon Connect's StartChatContact and returns participant credentials. You can start from the [StartChatContact API sample](https://github.com/amazon-connect/amazon-connect-chat-ui-examples/tree/master/cloudformationTemplates/startChatContactAPI) on the GitHub website. Your app calls it from TouchpointBackend.startChatContact. Required for touchpoint-chat. | 
| StartWebRTCContact backend (voice) | An authenticated endpoint that calls StartWebRTCContact and returns the Amazon Chime SDK meeting and attendee data. You can start from the [StartWebRTCContact sample](https://github.com/amazon-connect/amazon-connect-in-app-calling-examples/tree/main/Backend/AmazonConnectNetraApiSample) on the GitHub website. Your app calls it from TouchpointBackend.startVoiceContact. Required for touchpoint-voice. | 
| Instance ID and Contact Flow ID | The Amazon Connect Customer instance (UUID) and contact flow (UUID) that handle the contact. Your backend adds them to its StartChatContact and StartWebRTCContact requests; the app doesn't hold them. | 
| Region | AWS Region of your instance, for example us-west-2. Passed to the chat transport and to LiveSyncConfiguration. | 

### Implementing the backend interface
<a name="touchpoint-android-backend"></a>

The web SDK takes endpoint URLs in its configuration. The Android SDK instead asks your app to implement the `TouchpointBackend` interface. Anything packaged in an APK is public. For this reason, the SDK has no production API that accepts AWS credentials or a Live Sync API key directly. Your implementation calls your own authenticated backend, which holds the AWS credentials and calls Amazon Connect on the server.

```
import com.amazon.connect.touchpoint.core.ChatContactCredentials
import com.amazon.connect.touchpoint.core.ChatContactRequest
import com.amazon.connect.touchpoint.core.LiveSyncCredentials
import com.amazon.connect.touchpoint.core.TouchpointBackend
import com.amazon.connect.touchpoint.core.VoiceContactCredentials
import com.amazon.connect.touchpoint.core.VoiceContactRequest

class MyBackend(private val api: MyApi) : TouchpointBackend {
    // Calls your backend, which calls StartChatContact.
    override suspend fun startChatContact(request: ChatContactRequest): ChatContactCredentials {
        val reply = api.startChat(request.displayName, request.attributes)
        return ChatContactCredentials(reply.contactId, reply.participantId, reply.participantToken, expiresAt = null)
    }

    // Calls your backend, which calls StartWebRTCContact.
    override suspend fun startVoiceContact(request: VoiceContactRequest): VoiceContactCredentials {
        val reply = api.startWebRTCContact(request.displayName, request.attributes)
        return VoiceContactCredentials(
            reply.contactId, reply.participantId, reply.participantToken,
            reply.meetingJson, reply.attendeeJson,   // The Chime Meeting and Attendee objects, as JSON.
            expiresAt = null,
        )
    }

    // Returns the ACXD deployment key and API key, only if you use Live Sync.
    override suspend fun liveSyncCredentials(): LiveSyncCredentials {
        val keys = api.liveSyncKeys()
        return LiveSyncCredentials(keys.deploymentKey, keys.apiKey, expiresAt = null)
    }
}
```

Don't put secrets in `ChatContactRequest.attributes`; the SDK forwards attributes to `StartChatContact` as contact attributes.

### Setting up Amazon Connect Customer
<a name="touchpoint-android-setup-connect"></a>

1. **Create a contact flow** in your Amazon Connect Customer instance that handles the contact; note the **instance ID** and **contact flow ID**.

1. **Stand up the backend endpoints** that your `TouchpointBackend` calls — the `StartChatContact` (chat) and `StartWebRTCContact` (voice) endpoints listed in [Prerequisites](#touchpoint-android-prerequisites). Authenticate calls to them the way your app authenticates its other API calls.

### Adding Live Sync (optional)
<a name="touchpoint-android-setup-livesync"></a>

Live Sync requires an ACXD application. Build and publish it, and route your contact flow into it, as described in [Adding Live Sync (optional)](touchpoint.md#touchpoint-setup-livesync) for the web SDK. Then return the application's **deployment key** and **API key** from your backend's `liveSyncCredentials()` implementation instead of packaging them in the app.

## Permissions and manifest
<a name="touchpoint-android-permissions"></a>

The SDK modules don't add permissions to your app's manifest, and the SDK never requests a runtime permission on its own — your app declares and requests permissions at a moment it chooses. The SDK reports a denied permission as a state in the UI rather than as a crash.


| Permission | When it's required | 
| --- | --- | 
| INTERNET | All modules. Declare it in your app's manifest. | 
| RECORD\_AUDIO and MODIFY\_AUDIO\_SETTINGS | Voice. Declare both and request RECORD\_AUDIO at runtime before the call starts. Without the microphone, the call view shows that it's off, with a link to Settings. | 
| POST\_NOTIFICATIONS | Optional. Chat push notifications on Android 13 (API level 33) and later. | 

The optional `touchpoint-voice-telecom` module is the one exception. It adds the `FOREGROUND_SERVICE`, `FOREGROUND_SERVICE_PHONE_CALL`, and `FOREGROUND_SERVICE_MICROPHONE` permissions and a phone-call foreground service to your merged manifest. If you include it, complete the foreground service declaration for your app in the Google Play Console.

Chat push notifications use Firebase Cloud Messaging (FCM). The SDK doesn't include Firebase or register a messaging service; your app forwards the FCM token and notification taps to the SDK through `ChatPushBridge`.

The SDK modules include consumer R8 rules, so you don't need to add keep rules for Touchpoint.

## Examples
<a name="touchpoint-android-examples"></a>

Every example starts from a `TouchpointSession`. A session coordinates one active contact. It uses a `CredentialBroker` that wraps your backend, a conversation store that keeps the transcript on the device, and one transport for each modality. Build the session in an object that outlives your screens, such as your `Application` class, so a configuration change doesn't cancel a contact that is starting.

### Chat
<a name="touchpoint-android-example-chat"></a>

The following example builds a session with the chat transport, starts a chat contact, and shows the chat in a sheet. Replace {{REPLACE\_WITH\_CUSTOMER\_NAME}} with the customer's display name, which the agent sees.

```
import com.amazon.connect.touchpoint.chat.ConnectChatTransport
import com.amazon.connect.touchpoint.chat.ui.TouchpointChatSheet
import com.amazon.connect.touchpoint.core.ChatContactRequest
import com.amazon.connect.touchpoint.core.CredentialBroker
import com.amazon.connect.touchpoint.core.Modality
import com.amazon.connect.touchpoint.core.TouchpointSession
import com.amazon.connect.touchpoint.core.android.AndroidStores

val keys = AndroidStores.secureStore(context)
val store = AndroidStores.conversationStore(context, keys)
val broker = CredentialBroker(MyBackend(api), keys)
val chat = ConnectChatTransport.live(context, region = "us-east-1")
val session = TouchpointSession(broker, store, mapOf(Modality.CHAT to chat))

// From a coroutine scope that outlives the screen:
session.startChat(ChatContactRequest("REPLACE_WITH_CUSTOMER_NAME", emptyMap()))

// In your composable:
TouchpointChatSheet(
    session = session,
    visible = showChat,
    onDismiss = { showChat = false },
)
```

To place the chat in your own container instead of a sheet, use `TouchpointChatView(session)`. The sheet supports full, half, and mini sizes through `TouchpointWindowSize`. You can customize bubbles, participant names, the assistant name and icon, and the welcome screen with `TouchpointChatOptions`.

### Voice
<a name="touchpoint-android-example-voice"></a>

Register the voice transport with the session, then show `TouchpointVoiceView` for the full-screen call experience or `TouchpointVoiceMini` for a compact floating widget. The view calls `onStartCall` when it opens, the same way the web SDK does. The following example registers the voice transport and shows the full-screen call view.

```
import com.amazon.connect.touchpoint.core.VoiceContactRequest
import com.amazon.connect.touchpoint.voice.ConnectVoiceTransport
import com.amazon.connect.touchpoint.voice.TouchpointVoiceView

val voice = ConnectVoiceTransport.live(context)
val session = TouchpointSession(
    broker, store,
    mapOf(Modality.CHAT to chat, Modality.VOICE to voice),
)

// In your composable, after the app has the RECORD_AUDIO permission:
TouchpointVoiceView(
    session = session,
    voice = voice,
    onStartCall = { session.startVoice(VoiceContactRequest("REPLACE_WITH_CUSTOMER_NAME", emptyMap())) },
)
```

A session has one active contact at a time, so end an open chat before you start a call on the same session. To keep the call running while your app is in the background, add `touchpoint-voice-telecom`. Then call `TouchpointBackgroundCalls.attach(context, session, displayName = "REPLACE_WITH_YOUR_APP_NAME", smallIcon = R.drawable.ic_call)`, replacing {{REPLACE\_WITH\_YOUR\_APP\_NAME}} with your app's name.

### Live Sync
<a name="touchpoint-android-example-livesync"></a>

Live Sync is native Amazon Connect Customer technology that synchronizes a voice or chat conversation with a digital, on-screen interface. As on the web, the AI agent drives your app through **custom actions**: you advertise a named action with a JSON Schema, the agent resolves what the customer said into typed arguments, and your handler applies them to the screen.

Create a `LiveSyncClient` for the contact you want to mirror. Its `conversationId` is the Amazon Connect contact ID — for example, `session.contactId` after a chat starts. The client gets the Live Sync keys from your backend through the credential broker. The following example creates a client, handles an action, and advertises it to the AI agent.

```
import com.amazon.connect.touchpoint.core.LiveSyncChannel
import com.amazon.connect.touchpoint.livesync.ConsentDecision
import com.amazon.connect.touchpoint.livesync.LiveSyncAction
import com.amazon.connect.touchpoint.livesync.LiveSyncClient
import com.amazon.connect.touchpoint.livesync.LiveSyncConfiguration
import java.util.Locale

val client = LiveSyncClient(
    LiveSyncConfiguration(
        region = "us-east-1",
        conversationId = contactId,                   // the contact to sync with
        channel = LiveSyncChannel.from(Locale.getDefault()),
    ),
    credentials = broker,             // fetches the deployment key and API key from MyBackend
    consent = ConsentDecision.HELD,   // nothing is sent until the customer grants consent
    autoConnect = false,
)

client.onAction = { invocation ->
    when (invocation.action) {
        "set_cabin_class" -> setCabinClass(invocation.decode<CabinChoice>().cabin)
        else -> Unit
    }
}
client.attach(session)   // suspends action delivery while a human agent is on the contact
client.connect()

// From a coroutine: advertise the actions the AI agent may take. Each call replaces the previous set.
client.sendContext(actions = listOf(
    LiveSyncAction(
        "set_cabin_class",
        description = "Choose the cabin class",
        schema = buildJsonObject {
            put("type", "object")
            putJsonObject("properties") {
                putJsonObject("cabin") {
                    put("type", "string")
                    putJsonArray("enum") { add("economy"); add("business"); add("first") }
                }
            }
            putJsonArray("required") { add("cabin") }
        },
    ),
))
```

Instead of maintaining the action list by hand, you can declare actions in the composables that handle them. The SDK advertises an action while it's composed and withdraws it when it leaves the composition. The context always matches what the customer sees. By default, the SDK derives the JSON Schema from the payload's serializer. The following example declares an action in a screen.

```
import com.amazon.connect.touchpoint.livesync.TouchpointAction
import com.amazon.connect.touchpoint.livesync.TouchpointActionAggregator
import com.amazon.connect.touchpoint.livesync.TouchpointLiveSync
import com.amazon.connect.touchpoint.livesync.TouchpointScope
import kotlinx.serialization.Serializable

@Serializable
data class DisputeDetails(val reason: String? = null, val amount: Double? = null)

val aggregator = TouchpointActionAggregator(report = { error -> log(error) }) { context ->
    client.sendContext(context)
}
client.onAction = aggregator::route

// Once, around the screens that declare actions:
TouchpointLiveSync(aggregator) {
    AppNavHost()
}

// In any screen inside it:
TouchpointScope("dispute") {
    TouchpointAction(
        "set_dispute_details",
        "Fill in the dispute form with what the customer said",
        DisputeDetails.serializer(),
    ) { details -> model.apply(details) }
    DisputeForm(model)
}
```

Make every payload field optional; the agent sends only what the customer said. Actions can also be configured in [Agentic CX designer (ACXD)](https://docs.aws.amazon.com/connect/latest/adminguide/acxd.html) on the Live Sync node; defining them in the app is useful for rapid prototyping.

Because the SDK doesn't observe your app's lifecycle, call `client.enterBackground()` and `client.enterForeground()` from your app's lifecycle observer, for example `ProcessLifecycleOwner`.

#### Live Sync consent
<a name="touchpoint-android-example-consent"></a>

Live Sync shares what is on the customer's screen with the AI agent. The client starts with consent `HELD` and sends no context until the customer grants it. Use `LiveSyncConsentController` to store the decision for each deployment, and show the SDK's `LiveSyncConsentSheet` – or your own composable — while the controller needs an answer. In the following example, replace {{REPLACE\_WITH\_DEPLOYMENT\_ID}} with an identifier for your ACXD deployment, and {{REPLACE\_WITH\_YOUR\_COMPANY}} with your company name as customers know it.

```
val consent = LiveSyncConsentController(
      client,
      ConsentStore(AndroidStores.secureStore(context), "REPLACE_WITH_DEPLOYMENT_ID"),
      ConsentPrompt(
          dataDescription = "which screen you are on and what you can do there",
          recipient = "REPLACE_WITH_YOUR_COMPANY's assistant",
      ),
  )

  // In your composable:
  val asking by consent.needsPrompt.collectAsState()
  LaunchedEffect(consent) { consent.load() }
  if (asking) {
      LiveSyncConsentSheet(
          consent.prompt,
          onAllow = { scope.launch { consent.grant() } },
          onDecline = { scope.launch { consent.deny() } },
      )
  }
```

To give customers a way to stop sharing at any time, call `consent.deny()` from a control in your settings screen or support UI. Denying consent closes the Live Sync connection and clears the advertised context immediately; chat and voice continue.

#### Live Sync without chat or voice
<a name="touchpoint-android-example-external"></a>

The equivalent of the web SDK's `input: "external"` mode is to include only `touchpoint-livesync` and create a `LiveSyncClient` for a contact that your app didn't start. A common case is a **phone call**: the caller talks to the agent while your app updates alongside them. No chat or voice backend is needed — only the Live Sync credentials and the contact ID.

Your app needs a way to learn the contact ID, for example from your authenticated backend or from a signed deep link. Don't accept a contact ID from an unauthenticated link: anyone who has the link can bind to the conversation.

## Theming and localization
<a name="touchpoint-android-customization"></a>

The SDK's theme tokens have the same names and default values as the web SDK's, so a brand configured once looks the same on both. Pass a `TouchpointTheme` to the `theme` parameter of the chat and voice composables. Start from `TouchpointTheme.Light`, `TouchpointTheme.Dark`, or `TouchpointTheme.system()`, and derive brand colors with `withPrimary`, `withSecondary`, and `withAccent`. The SDK applies its theme through its own composition local and never reads or changes your app's `MaterialTheme`.
+ **Dark theme** – by default, the SDK follows the system setting. (The web SDK defaults to dark.)
+ **Accessibility** – the composables support TalkBack, use 48 dp minimum touch targets, and scale with the customer's font size.
+ **Localization** – the SDK's strings are Android string resources that include the web SDK's translations. Every resource name starts with `touchpoint_`; override any of them in your app's resources to change the text. Make sure the Live Sync channel you pass to `LiveSyncChannel.from()` matches a language that your ACXD application supports.

## API reference
<a name="touchpoint-android-api-reference"></a>

Every public type is documented in source, and the [touchpoint-android repository](https://github.com/amazon-connect/touchpoint-android) on the GitHub website contains the full API documentation and a sample banking app. The following list describes common entry points.
+ `TouchpointBackend` – the interface your app implements to create contacts and vend Live Sync credentials.
+ `TouchpointSession` – coordinates one contact; `startChat`, `startVoice`, `end`, `resume`, and the `state` and `events` flows.
+ `TouchpointChatView`, `TouchpointChatSheet`, and `TouchpointChatOptions` – the chat UI and its options.
+ `ConnectVoiceTransport`, `TouchpointVoiceView`, and `TouchpointVoiceMini` – the call transport and its UI.
+ `LiveSyncClient`, `LiveSyncConfiguration`, `TouchpointAction`, and `LiveSyncConsentController` – the Live Sync connection, declarative actions, and consent.
+ `TouchpointException` and `LiveSyncException` – the errors the SDK throws or reports. For example, `LiveSyncException.ContactMayBeStale` indicates that the Live Sync connection is open but the contact ID likely no longer refers to a live contact.

## License
<a name="touchpoint-android-license"></a>

The Touchpoint SDK for Android is open source. For license terms, see the [LICENSE file](https://github.com/amazon-connect/touchpoint-android/blob/main/LICENSE) in the touchpoint-android repository on the GitHub website.