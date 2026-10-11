

# Application architecture
<a name="ca-architecture"></a>

## Module layout
<a name="ca-module-layout"></a>


| Group | Responsibility | 
| --- | --- | 
|  `Api/`  | REST clients and wire models. `VSAClient` covers the AVX API plus the two CMS APIs the app calls directly; `AcquireCatalogClient` covers the Acquire journey; `AvxModels` and `RemoteCommandModels` carry the Finding, Action and command contracts; `TriageCoordinator` decides when to ask for a triage classification. | 
|  `Auth/`  |  `AuthService` (Amazon Cognito sign-in), `BiometricAuth` (Face ID / Touch ID), and `KeychainStore` (token storage). | 
|  `Voice/`  | The voice subsystem: the session view model and its state machine, the bidirectional WebSocket client, microphone capture, and speaker playback. | 
|  `Views/`  | Screens, grouped by tab, with `Views/Acquire/` holding the journey flows and `Views/Acquire/Steps/` the configurator step sequence. | 
|  `Telemetry/`  | The vehicle telemetry WebSocket client, plus a mock client used for development without a deployment. | 
|  `Services/`  | Cross-cutting services: push-notification consent, tab badging, and deep-link routing from a tapped notification into the right screen. | 
|  `Theming/`  | Tenant-driven colors and logos. | 
|  `UI/`  | Layout context and kiosk-mode session handling. | 
|  `Config/`  | Build-time configuration, read from `Info.plist` substitution rather than hardcoded in Swift. | 

 `Presenter/` and `DemoClips/` support scripted demonstration rather than production behavior, and are called out here so they are not mistaken for platform features.

## Session and identity state
<a name="ca-session-identity"></a>

The app signs into Amazon Cognito and holds the resulting tokens in the iOS keychain, unlocking the stored session with Face ID or Touch ID rather than re-prompting for a password. One session object, injected through the SwiftUI environment, is the single source of truth for who is signed in, which vehicle is theirs, which tenant they belong to, and which voice session — if any — is live.

Identity is claim-driven. The signed-in user’s Cognito claims carry the driver id, the vehicle id and the tenant id, and the app reads its scope from those claims rather than asking the user to choose. Several of these attributes are immutable in Cognito once a user is created, which constrains how demo and test identities are provisioned; see [Persona inference](pt-persona-inference.md) for how claims map to personas.

## Tenant configuration drives presentation
<a name="ca-tenant-presentation"></a>

After sign-in the app resolves the tenant id against the tenant-configuration table and derives a layout segment from the row. The segment is not cosmetic: it decides tab labels, iconography, theming, and whether the Buy tab appears at all. An OEM-segment tenant sees the service tab labelled **Dealer** with a building icon, because its drivers are routed to authorized dealerships; fleet and rental segments keep the wrench and the generic service label.

Because presentation hangs off a table lookup, a missed lookup is a silent failure mode rather than a loud one — the segment falls back to a default, tab labels and theming are quietly wrong, and nothing errors. The app therefore emits an explicit diagnostic on lookup failure naming the tenant id it tried and stating that a fallback is in effect. This is worth knowing when onboarding a new tenant: a missing configuration row presents as a subtly mislabelled app, not as an error. See [Tenancy](pt-tenancy.md).

## Launch sequence
<a name="ca-launch-sequence"></a>

Three stages, deliberately continuous so the handoffs are invisible: a static launch image composited by iOS before any app code runs, an animated wordmark reveal shown once per cold start, and a short crossfade into the application root, after which the player is torn down.

Two details are load-bearing. The reveal clip is cut short rather than played to completion, at the first frame where the animation matches the static launch image — so the handoff has no visible jump and the launch delay stays bounded. And dismissal is driven by a timer rather than by the player’s end-of-playback notification: the splash sits above the entire app, so a clip that never reported an end would otherwise trap the user behind a blank screen. The notification is still observed; it is just not relied upon. With Reduce Motion enabled, or if the clip is missing or undecodable, the app shows the static wordmark briefly instead.

## Configuration and graceful degradation
<a name="ca-config-degradation"></a>

Backend endpoints are injected at build time through `.xcconfig` files and read via `Info.plist` substitution. Swift source is never edited to point the app at a deployment. Two layers: tracked files carrying fail-loud placeholder tokens, and an untracked per-developer sibling that overrides them. Absent the untracked layer the build still succeeds, but the app raises a diagnostic at startup in debug builds rather than silently passing placeholder values to Cognito.

Endpoints are independently optional, and **an unset endpoint hides its affordance rather than surfacing a broken one**. With no CMS main API configured, the vehicle-claim action is absent; with no commands API, the controls affordance is absent rather than shown disabled with no explanation. The app therefore runs against a partial deployment — useful when evaluating AVX without CMS, or the reverse — and the missing capability is legible as absence rather than as breakage.