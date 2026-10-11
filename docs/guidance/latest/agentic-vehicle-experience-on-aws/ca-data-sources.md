

# What the app reads, and from where
<a name="ca-data-sources"></a>

Most vehicle data reaches the app through the AVX API, which aggregates it from the CMS data layer and applies the caller’s scope. Three CMS surfaces are called **directly**, because each needs a path the aggregation layer does not provide.

## Through the AVX API
<a name="ca-avx-api"></a>


| Surface | Purpose | 
| --- | --- | 
| Driver and vehicle context | The signed-in driver, the assigned vehicle, live vehicle state, and recent trips. | 
| Safety events and service history | Recent safety events for the Alerts tab; past and upcoming service for the Service tab. | 
| Triage | Submits a candidate condition for classification and receives the classification and its recommended actions. | 
| Service centers and booking | Finds a service center and commits a booking, returning the confirmation the app renders as a card. | 
| Findings and Actions | The Findings the caller has standing over, and the approve and dismiss transitions on them. | 
| Tenant configuration | The row that drives segment, theming and tab labels. | 
| Device registration | Registers the device for push notifications, subject to consent. | 

## Directly against CMS
<a name="ca-cms-direct"></a>
+  **Main API — vehicle claim.** A driver claims their assigned vehicle so trips are attributed correctly. The CMS Cognito authorizer accepts the app’s tokens, and the CMS main API constrains driver tokens to a self-service allowlist, so a driver token presented to an operator route is rejected on the CMS side rather than filtered on the client.
+  **Commands API — remote commands.** A separate API Gateway from the main API, with its own base URL. Covered in [Remote commands](ca-remote-commands.md).
+  **Telemetry WebSocket — live vehicle state.** A direct subscription to the CMS fan-out service, so state and alerts arrive as they happen rather than on a poll.

The distinction matters when reasoning about failure. An AVX API outage degrades the app broadly; a CMS commands API misconfiguration removes exactly one affordance. See [Building on CMS and ADP](building-on-cms-and-adp.md) for the platform side of these integrations.