

# Driver companion app
<a name="driver-companion-app"></a>

The companion app is a native iOS application built with SwiftUI, under `clients/ios/`. It is the driver’s surface: where the Fleet Manager console shows an operator every vehicle in a fleet, the companion app shows one driver the one vehicle assigned to them. It is not deployed by a CloudFormation stack — it is built and installed as a mobile application, and it consumes APIs that the CMS stacks already expose.

This section documents the CMS-side view: the app’s screens, and which CMS surfaces it calls. The application’s own architecture — the voice session transport and state machine, the Finding and Action contracts, the Acquire journey, and the agent reasoning the app narrates — is documented in the companion Agentic Vehicle Experience (AVX) accelerator’s implementation guide, in its **The Companion App** chapter. That guide owns the app’s internals because most of the app’s surface area is AVX-served; this guide owns the CMS integration described below.

The app uses only Apple frameworks (SwiftUI, AVFoundation, LocalAuthentication, CryptoKit) and has no third-party package dependencies.

## Screens
<a name="companion-tabs"></a>


| Tab | Contents | 
| --- | --- | 
| Home | Vehicle summary and quick actions, including claiming an assigned vehicle. | 
| Vehicle | Live telemetry, vehicle state, trip history, and the remote controls sheet. | 
| Alerts | Real-time driver signals — diagnostic trouble codes, safety events, triage outcomes, and agent findings. | 
| Service | Service history and appointment booking. Labelled **Dealer** for OEM-segment tenants, whose drivers are routed to authorized dealerships rather than a generic service center; fleet and rental tenants keep the service label. | 
| Account | Driver profile and settings. | 

The conversational assistant is not a tab. It opens as a full-screen presentation from anywhere in the app, and the Service tab’s **Book Service** action opens it with a primed prompt so the conversation begins as though the driver had asked for it. Additional journey surfaces beyond the tabs above are contributed by the companion AVX accelerator and are documented there, not in this guide.

## What it reads, and from where
<a name="companion-apis"></a>

The app talks to this guidance and to the companion AVX accelerator directly — it is a client of both, not a client of one that proxies the other.

From CMS:
+  **Main API** — claiming the driver’s assigned vehicle. The CMS Cognito authorizer accepts the app’s tokens, and the main API constrains driver tokens to a self-service allowlist, so a driver token cannot reach operator routes.
+  **Commands API** — a separate API Gateway from the main API. The app fetches the command catalog and issues remote commands against the driver’s own vehicle. The controls sheet is catalog-driven rather than hardcoded: it renders whatever the catalog exposes for that vehicle, with dedicated icons for `lock_all_doors`, `remote_start`, `start_preconditioning`, `flash_hazards`, `find_my_vehicle`, `open_charge_door` and `panic_mode`, and a neutral glyph for anything else. See [Remote commands](remote-commands-flow.md) for the end-to-end command path.
+  **Telemetry WebSocket** — the ws-fanout service, for real-time vehicle state and alerts. See [WebSocket telemetry fan-out](ws-fanout-stack.md).

From the companion AVX accelerator: the driver profile, triage, agent findings, service-center search, booking, and push-device registration, plus the bidirectional voice runtime. Voice runs over a SigV4-signed WebSocket to an Amazon Bedrock AgentCore runtime; see [In-vehicle assistant](fleet-manager-console.md#fm-assistant) for the assistant’s shared architecture.

## Authentication and driver scope
<a name="companion-auth"></a>

The app signs into the same Amazon Cognito user pool as the Fleet Manager console, so a driver has one identity across both surfaces. Tokens are held in the iOS keychain and the session is unlocked with Face ID or Touch ID.

Driver scope is narrow by design and enforced server-side. A signed-in driver reads the findings and the vehicle belonging to that driver — never another driver’s, and never another vehicle sold to the same customer. Remote commands act on the driver’s own vehicle only, and command history shows the commands that driver issued rather than every command on the vehicle.

## Configuration
<a name="companion-config"></a>

Backend endpoints are injected at build time through `.xcconfig` files, never by editing Swift source. Two layers: tracked files carrying fail-loud placeholder tokens, and an untracked per-developer sibling that overrides them. Absent the untracked layer the build still succeeds, but the app raises a diagnostic at startup in debug builds rather than passing placeholders to Cognito.

Endpoints are independently optional, and an unset endpoint hides its affordance rather than surfacing a broken one. With no CMS main API configured the vehicle-claim action is hidden; with no commands API the controls affordance is hidden rather than shown disabled. A deployment can therefore run the app against a subset of the platform.