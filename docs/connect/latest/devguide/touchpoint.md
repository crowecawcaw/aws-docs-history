

# Touchpoint
<a name="touchpoint"></a>

Touchpoint is a drop-in conversational UI and SDK for Amazon Connect Customer — a single widget for chat, voice, and voice-mini, plus **Live Sync**, the native technology that keeps a voice or chat conversation in sync with your on-screen interface.

Install the package from npm:

```
npm i @amazon-connect-touchpoint/web
```

**Important**  
Touchpoint is open source on GitHub at [https://github.com/amazon-connect/touchpoint](https://github.com/amazon-connect/touchpoint). The full SDK reference — every configuration option, type, and modality component — is generated from source and lives in the repository's [docs/](https://github.com/amazon-connect/touchpoint/tree/main/docs) directory.

**Topics**
+ [What Touchpoint provides](#touchpoint-what-provides)
+ [Prerequisites](#touchpoint-prerequisites)
+ [Examples](#touchpoint-examples)
+ [Interactive playground](#touchpoint-playground)
+ [API reference](#touchpoint-api-reference)
+ [License](#touchpoint-license)

## What Touchpoint provides
<a name="touchpoint-what-provides"></a>

Touchpoint renders a single widget that you configure through the `input` option. Choose the input mode that matches the experience you want:
+ `text` — a chat experience. Connects through your `StartChatContact` endpoint (`config.chatEndpoint`).
+ `voice` — the full-screen voice experience. Connects through your `StartWebRTCContact` endpoint (`config.voiceEndpoint`).
+ `voiceMini` — a compact, floating voice widget. Also connects through your `StartWebRTCContact` endpoint.
+ `external` — no rendered UI. Touchpoint opens no chat or voice contact of its own; it only connects Live Sync to an existing live contact so that contact can drive your digital asset in real time.

Live Sync is native Amazon Connect Customer technology that synchronizes a conversation with a digital, on-screen interface. Live Sync is the only feature that requires an Agentic CX Designer (ACXD) application; plain chat and voice work without it. For more information about ACXD, see the [Amazon CX Designer SDK](acxd-sdk.md) chapter in this guide and [Agentic CX designer (ACXD)](https://docs.aws.amazon.com/connect/latest/adminguide/acxd.html) in the *Amazon Connect Administrator Guide*.

## Prerequisites
<a name="touchpoint-prerequisites"></a>

To run Touchpoint you need an Amazon Connect Customer instance with a contact flow, plus a browser-facing endpoint that mints the contact credentials. Gather the following before you call `create()`:


| What you need | Where it comes from | 
| --- | --- | 
| StartChatContact endpoint (chat) | An API Gateway/Lambda route that calls Amazon Connect's StartChatContact and returns participant credentials. Deploy the [StartChatContact API](https://github.com/amazon-connect/amazon-connect-chat-ui-examples/tree/master/cloudformationTemplates/startChatContactAPI). Required for input: "text". Passed as config.chatEndpoint. | 
| StartWebRTCContact endpoint (voice) | An endpoint that calls StartWebRTCContact and returns the Chime connection data. Deploy the [StartWebRTCContact sample](https://github.com/amazon-connect/amazon-connect-in-app-calling-examples/tree/main/Backend/AmazonConnectNetraApiSample). Required for input: "voice" and input: "voiceMini". Passed as config.voiceEndpoint. | 
| Instance ID | The Amazon Connect Customer instance (UUID) the contact is created in. config.instanceId. | 
| Contact Flow ID | The contact flow (UUID) that handles the contact. config.contactFlowId. | 
| Region | AWS region of your instance, for example us-west-2. config.region. | 

That's everything you need for chat and voice. **Live Sync is optional** — it additionally requires an Agentic CX designer (ACXD) application; see the following procedures.

### Setting up Amazon Connect Customer
<a name="touchpoint-setup-connect"></a>

1. **Create a contact flow** in your Amazon Connect Customer instance that handles the contact; note the **instance ID** and **contact flow ID**.

1. **Stand up the browser endpoints** so the page can create a contact — the [StartChatContact](https://github.com/amazon-connect/amazon-connect-chat-ui-examples/tree/master/cloudformationTemplates/startChatContactAPI) (chat) and [StartWebRTCContact](https://github.com/amazon-connect/amazon-connect-in-app-calling-examples/tree/main/Backend/AmazonConnectNetraApiSample) (voice) endpoints listed in the preceding table.

### Adding Live Sync (optional)
<a name="touchpoint-setup-livesync"></a>

Live Sync keeps the conversation in sync with your on-screen interface. It's the only feature that requires ACXD; plain chat and voice work without it. To enable it:

1. **Build the ACXD application.** In the ACXD Canvas, wire `Start` → a **Live Sync** node → `Exit application`. On the Live Sync node, declare the actions and scopes the assistant may use (or define them on the fly with this SDK for rapid prototyping — see [Live Sync](#touchpoint-example-livesync)).

1. **Publish it and copy your keys.** Deploy the application, then copy the **deployment key** and **API key** from its settings.

1. **Route your contact flow into it** so contacts reach the ACXD application, and pass the keys as `liveSync.deploymentKey` / `liveSync.apiKey`.

The [Interactive playground](#touchpoint-playground) lets you plug these values into a form and launch a live instance without writing any code.

## Examples
<a name="touchpoint-examples"></a>

The following examples show how to configure Touchpoint for each input mode.

### Chat
<a name="touchpoint-example-chat"></a>

Configure a chat experience with `input: "text"`.

```
import { create } from "@amazon-connect-touchpoint/web";

const touchpoint = await create({
  config: {
    // Your StartChatContact endpoint (e.g. an API Gateway route) that mints a
    // participant token.
    chatEndpoint: "REPLACE_WITH_START_CHAT_ENDPOINT",
    instanceId: "REPLACE_WITH_INSTANCE_ID",
    contactFlowId: "REPLACE_WITH_CONTACT_FLOW_ID",
    region: "us-east-1",
  },
  input: "text",
});
```

### Voice mini
<a name="touchpoint-example-voice-mini"></a>

A compact, floating voice widget. Voice modes connect through your `StartWebRTCContact` endpoint.

```
import { create } from "@amazon-connect-touchpoint/web";

const touchpoint = await create({
  config: {
    voiceEndpoint: "REPLACE_WITH_START_WEBRTC_ENDPOINT",
    instanceId: "REPLACE_WITH_INSTANCE_ID",
    contactFlowId: "REPLACE_WITH_CONTACT_FLOW_ID",
    region: "us-east-1",
  },
  input: "voiceMini", // or "voice" for the full-screen experience
});
```

### Live Sync
<a name="touchpoint-example-livesync"></a>

Live Sync is native Amazon Connect Customer technology that synchronizes a voice (or chat) conversation with a digital, on-screen interface. Customers see options, next steps, and confirmations in real time while an AI agent guides them — no app, no channel switch — unlocking complex, multi-step tasks that voice or chat alone can't handle, where customers need to see, choose, and complete actions in a single continuous conversation.

In Touchpoint, the AI agent drives the page through **custom actions**: you register a named action with a JSON Schema, the agent resolves what the customer said into typed arguments, and your handler applies them to the page.

```
import { create } from "@amazon-connect-touchpoint/web";

const touchpoint = await create({
  config: {
    chatEndpoint: "REPLACE_WITH_START_CHAT_ENDPOINT",
    instanceId: "REPLACE_WITH_INSTANCE_ID",
    contactFlowId: "REPLACE_WITH_CONTACT_FLOW_ID",
    region: "us-east-1",
  },
  input: "text",
  liveSync: {
    deploymentKey: "REPLACE_WITH_DEPLOYMENT_KEY",
    apiKey: "REPLACE_WITH_API_KEY",
    // `contactId` is optional — defaults to the active session's contact. Set it
    // to bind a separate contact (e.g. an inbound phone call) to this page.
  },
});

// Advertise the actions the AI agent may take (sent once a contact exists):
await touchpoint.sendContext({
  actions: [
    {
      action: "set_cabin_class",
      description: "Choose the cabin class",
      schema: {
        type: "object",
        properties: {
          cabin: { type: "string", enum: ["economy", "business", "first"] },
        },
        required: ["cabin"],
      },
      handler: ({ cabin }) => setCabinClass(cabin),
    },
  ],
});
```

Actions can also be configured in [Agentic CX designer (ACXD)](https://docs.aws.amazon.com/connect/latest/adminguide/acxd.html) on the Live Sync node; defining them here is useful for rapid prototyping. To notify a Live Sync script that the user reached a step, call `touchpoint.sendStep({ stepId, scriptId, apiKey, context })`.

### External (no UI)
<a name="touchpoint-example-external"></a>

Use `input: "external"` to run Touchpoint with **no rendered UI**. It opens no chat or voice contact of its own — it only connects Live Sync to an existing live contact (identified by `liveSync.contactId`) so that contact can drive your digital asset in real time. A common case is a **phone call**: the caller talks to the agent while the page updates alongside them. No `chatEndpoint` or `voiceEndpoint` is needed; only the Live Sync credentials.

```
import { create } from "@amazon-connect-touchpoint/web";

const touchpoint = await create({
  config: { region: "us-east-1" },
  input: "external",
  liveSync: {
    deploymentKey: "REPLACE_WITH_DEPLOYMENT_KEY",
    apiKey: "REPLACE_WITH_API_KEY",
    contactId: "REPLACE_WITH_CONTACT_ID", // the contact to sync with
  },
});

// Advertise your actions, then drive the page as the agent invokes them.
await touchpoint.sendContext({ actions: [/* … */] });
```

## Interactive playground
<a name="touchpoint-playground"></a>

Running the project locally launches an interactive playground covering every capability (chat, voice, voice-mini, and Live Sync):

```
npm install
npm run dev
# then open http://localhost:5173
```

## API reference
<a name="touchpoint-api-reference"></a>

The full SDK specification — every configuration option, type, and modality component — is generated from source and lives in the repository's [docs/](https://github.com/amazon-connect/touchpoint/tree/main/docs) directory.

Common entry points include:
+ `create(config)` — create and mount a Touchpoint instance.
+ `TouchpointConfiguration` — top-level options (`config`, `input`, `colorMode`, `theme`, `liveSync`, and more).
+ `ConnectConfig` — Amazon Connect Customer connection details.
+ `LiveSyncConnection` / `LiveSyncContextInput` — Live Sync connection and the actions, scopes, and destinations you advertise to the AI agent.

## License
<a name="touchpoint-license"></a>

Touchpoint is released under the [MIT](https://github.com/amazon-connect/touchpoint/blob/main/LICENSE) license.