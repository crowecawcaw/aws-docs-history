

# How it works
<a name="companion-how-it-works"></a>

## Sign-in and driver scope
<a name="companion-auth"></a>

The app signs into the same Amazon Cognito user pool as the Fleet Intelligence portal, so a driver has one identity across both. Tokens are held in the iOS keychain, and the stored session is unlocked with Face ID or Touch ID instead of a password prompt.

Scope comes from the driver’s Cognito claims, which carry the driver ID, the vehicle ID, and the tenant ID. The app does not ask the driver to choose a vehicle. Scope is enforced server-side: a driver reads the vehicle and findings that belong to them, never another driver’s, and never another vehicle sold to the same customer.

After sign-in the app looks up the tenant configuration and derives a layout segment from it. The segment sets tab labels, icons, theming, and whether the Buy tab appears. If the lookup fails, the app falls back to a default segment and logs the tenant ID it tried, because a missing tenant row shows up as a mislabelled app rather than an error.

## Vehicle claim
<a name="companion-claim"></a>

Claiming calls the CMS main API. The CMS Cognito authorizer accepts the app’s tokens, and the main API limits driver tokens to a self-service allowlist of routes, so a driver token sent to an operator route is rejected by CMS. Once claimed, new trips are attributed to the driver, as described in [Driver Assignment](fleet-manager-console.md#fm-driver-assignment).

## Live vehicle state
<a name="companion-live-state"></a>

The app subscribes to the CMS telemetry WebSocket, so state and alerts arrive as they happen rather than on a poll. See [WebSocket telemetry fan-out](fip-architecture-details.md#ws-fanout-stack).

## Remote commands
<a name="companion-commands"></a>

Remote commands go to the CMS Commands API, a separate API Gateway from the main API, whose Cognito authorizer trusts the same user pool.
+  **The controls sheet is catalog-driven.** The app fetches the command catalog and renders what the platform offers for that vehicle. `lock_all_doors`, `remote_start`, `start_preconditioning`, `flash_hazards`, `find_my_vehicle`, `open_charge_door`, and `panic_mode` get dedicated icons; anything else gets a neutral icon. A command added to the platform appears without an app release.
+  **Sending is not confirming.** A successful send means the command was accepted for publication, not that the vehicle performed it. The app shows the command as in progress, and confirms it from command history when the command reaches a succeeded state, or from live state on the telemetry WebSocket when the command changes vehicle state.
+  **Scope is the driver’s own vehicle.** Commands act on the driver’s vehicle only, and command history shows the commands that driver issued rather than every command recorded against the vehicle.

The vehicle-side path is described in [Remote commands](fip-how-it-works.md#remote-commands-flow).

## Alerts and findings
<a name="companion-findings"></a>

Findings are produced server-side by autonomous agents in the AVX accelerator; the app reads them and performs no reasoning over them. The app asks for the findings the driver has standing over and receives exactly those, instead of fetching a broader set and filtering on the device. Approving a finding sends a fixed, minimal body. Dismissing one uses a dedicated sub-resource that distinguishes declining to act from cancelling something already approved. A summary endpoint supplies open counts for tab badges.

Push notifications are consent-gated, and consent is asked for in context rather than at first launch. Tapping a notification opens the relevant finding.

## Voice assistant
<a name="companion-voice"></a>

The assistant is served by an Amazon Bedrock AgentCore bidirectional runtime in the AVX accelerator, using Amazon Nova 2 Sonic for speech to speech.
+  **Transport.** The app opens a SigV4-signed WebSocket to the runtime. It exchanges its Cognito identity for short-lived AWS credentials through an Amazon Cognito identity pool federated with the user pool, and signs the request with them. This is the app’s only AWS-signed request; every other call is a bearer-token REST request.
+  **Protocol.** A small JSON protocol runs over the socket. The app sends `session.start`, `audio.chunk`, `text.input`, `escalation.request`, and `session.end`. The runtime sends `transcript`, `audio.chunk`, `tool.call` and `tool.result`, `classification`, `escalation`, `interruption`, `info.message`, `session.ended`, `error`, and `debug`. `info.message` carries content that is better read than heard, such as a tire-pressure table, which the app renders on screen while the assistant speaks a summary.
+  **Audio.** Capture is 16 kHz mono 16-bit PCM. Playback is 24 kHz, converted to Float32 before it reaches the mixer, because a 16-bit connection works in the simulator but crashes on a device. If the audio hardware reports no usable format, the session continues as text.
+  **State.** The session moves through seven states: disconnected, connecting, ready, talking, thinking, speaking, and error. The UI is derived from this state. Messages typed while connecting are queued and sent when the session is ready.
+  **Timing.** A tool call must return within about one second. Nova Sonic closes an idle session after 55 seconds, so the app sends silence audio every 40 seconds to keep a session open. Booking commits are allowed 90 seconds.
+  **Transparency.** Tool calls, their inputs and outputs, and classifications appear in a reasoning drawer, and booking confirmations render as structured cards rather than prose.

Escalation to a contact-center agent runs alongside the voice session rather than replacing it, so the assistant keeps talking to the driver while the handoff opens.

## Client-side triage
<a name="companion-triage"></a>

The app watches incoming telemetry and asks the platform’s triage classifier to classify a condition when a threshold is crossed. The classifier decides the outcome; the app only decides when to ask. Its thresholds are slightly looser than the classifier’s, so a borderline condition is submitted rather than filtered out, and requests are debounced so a fast telemetry stream produces one request rather than many. A stop-driving outcome is shown with the classifier’s wording, unchanged.

## Buy journey
<a name="companion-buy"></a>

For tenants that enable it, the Buy tab runs discovery, a step-by-step configurator (category, model, variant, interior, color, accessories, finance, review, and confirmation), upgrade offers for existing owners, lead capture to a dealer, reservations, and order tracking. Finance terms and disclosure text come from the platform and are shown as issued. The app can also run as a showroom kiosk on a shared device, clearing everything a visitor entered before the next visitor.