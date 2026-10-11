

# Architecture details
<a name="companion-architecture"></a>

## What it reads, and from where
<a name="companion-apis"></a>

The app is a client of CMS and of the AVX accelerator directly; neither proxies the other.


| Platform | Surface | Used for | 
| --- | --- | --- | 
| CMS | Main API (Amazon API Gateway, AWS Lambda) | Vehicle claim. | 
| CMS | Commands API (Amazon API Gateway, AWS Lambda, AWS IoT Core) | Command catalog, remote commands, and command history. | 
| CMS | Telemetry WebSocket (API Gateway WebSocket API) | Live vehicle state and alerts. | 
| CMS | Amazon Cognito user pool | Sign-in, shared with the Fleet Intelligence portal. | 
| AVX | AVX API | Driver and vehicle context, safety events, service history, triage, service centers and booking, findings and their transitions, tenant configuration, and push-device registration. | 
| AVX | Amazon Bedrock AgentCore runtime, with an Amazon Cognito identity pool | The voice assistant. | 

An outage of the AVX API degrades most of the app; a misconfigured CMS Commands API removes only the remote controls.

## Module layout
<a name="companion-modules"></a>


| Group | Responsibility | 
| --- | --- | 
|  `Api/`  | REST clients and wire models, including the Finding, Action, and remote-command contracts, and the triage coordinator that decides when to ask for a classification. | 
|  `Auth/`  | Cognito sign-in, Face ID and Touch ID, and keychain token storage. | 
|  `Voice/`  | The voice session view model and state machine, the WebSocket client, microphone capture, and speaker playback. | 
|  `Telemetry/`  | The telemetry WebSocket client, and a mock client for development without a deployment. | 
|  `Views/`  | Screens by tab; `Views/Acquire/` holds the Buy journey and its configurator steps. | 
|  `Services/`  | Push-notification consent, tab badges, and routing from a notification to a screen. | 
|  `Theming/`, `UI/`, `Config/`  | Tenant colors and logos, layout context and kiosk mode, and build-time configuration. | 

## Configuration
<a name="companion-config"></a>

Backend endpoints are set at build time through `.xcconfig` files and read through `Info.plist` substitution; Swift source is never edited to point the app at a deployment. Tracked files carry fail-loud placeholder values, and an untracked per-developer file overrides them. Without the untracked file the build still succeeds, but debug builds report the placeholders at startup instead of passing them to Cognito.

Each endpoint is optional, and an unset endpoint hides its feature instead of showing a broken one. With no CMS main API configured, the vehicle-claim action is hidden; with no Commands API, the remote controls are hidden. The app can therefore run against part of the platform, for example AVX without CMS.

## Logging
<a name="companion-logging"></a>

The voice path logs state transitions with their reasons, connection and teardown, tool results, watchdog timeouts, and credential exchange, with a distinct prefix per subsystem so that one log capture gives a full timeline. The app uses `NSLog` so the lines reach the unified system log when the app is launched outside a debugger. Filter a log stream on the prefix: predicate-based filters do not capture these lines from an app launched that way.

Token bodies, secret keys, and session tokens are never logged; only their lengths are, which is enough to tell an empty token from a present one. Access key IDs are logged as a short prefix only, and error response bodies are logged only on failure. A customer-supplied log can therefore be used to debug the voice path without disclosing credentials.