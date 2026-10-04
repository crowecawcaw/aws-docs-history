

# Client surfaces
<a name="client-surfaces"></a>

One platform, three front ends. They differ in audience, in what they are permitted to see, and in which APIs they call — not merely in styling. Deploying all three is optional; the Fleet Manager console is the only one deployed unconditionally.


|  | Fleet Manager console | Connected Services portal | Driver companion app | 
| --- | --- | --- | --- | 
| Audience | Fleet operators and administrators managing their own fleets | Subscribers and internal product teams working with the vehicle data model and data products | The individual driver of a single vehicle | 
| Platform | React SPA (Cloudscape), served by CloudFront | React SPA (Cloudscape), served by its own CloudFront distribution and subdomain | Native iOS application (SwiftUI) | 
| Deployed by |  `cms-{stage}-ui` — always |  `cms-{stage}-connected-services-ui` — opt-in, `DEPLOY_CONNECTED_SERVICES_UI=true`  | Not a CFN stack; built and installed as a mobile application | 
| Sign-in | Amazon Cognito; authority from the `platform-admin`, `fleet-operator` and `fleet-viewer` groups | Amazon Cognito on the same pool; the `subscriber` group for subscriber routes, `connected-services` for administrative routes | Amazon Cognito on the same pool as the console, plus Face ID / Touch ID for session unlock | 
| Scope of visibility | The fleets the signed-in user’s claims permit, across every vehicle in them | Only the vehicles a subscription entitles the caller to, filtered by the `custom:customerIds` claim | One vehicle — the one assigned to the signed-in driver | 
| Reads from | Fleet Management, Commands, Geofence and Fleet Intelligence APIs | The data-processing, simulation and subscription APIs | The companion AVX API, plus the CMS main API, commands API and telemetry WebSocket directly | 

The three surfaces are not tiers of the same application. A fleet operator sees an entire fleet and can act across it; a subscriber sees only entitled vehicles and cannot act on them at all; a driver sees one vehicle and can act only on that one. Those boundaries are enforced server-side by the APIs, not by the clients — each client hides affordances its user cannot exercise, but the authorization decision belongs to the API in every case. See [Security](security.md) for the claim-to-authority mapping.