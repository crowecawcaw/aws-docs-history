

# Connected Services portal
<a name="connected-services-portal-walkthrough"></a>

The Connected Services portal is a second React application, deployed by `cms-{stage}-connected-services-ui` when `DEPLOY_CONNECTED_SERVICES_UI=true`. It is not a view within the Fleet Manager console: it has its own CloudFront distribution, its own subdomain, and its own authorization groups. Where the console answers **"how is my fleet operating?"**, the portal answers **"what does this vehicle platform consist of, and who is entitled to its data?"** 

![Connected Services portal signal catalog](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/cs-signals.png)


![Connected Services portal data collection campaigns](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/cs-campaigns.png)


![Connected Services portal vehicle simulation](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/cs-simulate-vehicle.png)


## Screen domains
<a name="cs-portal-domains"></a>

The portal organizes its screens into seven domains, reached from the side navigation:


| Domain | Screens | 
| --- | --- | 
| Command center | The landing view — a cross-domain summary with pending approvals. | 
| Data model | Signal catalog and signal detail, vehicle models and model detail, ECUs, decoder manifests and manifest detail, data-collection campaigns and campaign detail. | 
| Connectivity | Simulate Vehicle (with the trip simulator), available vehicles, fleet health, rate plans, policy control, subscriber lookup, and the FWE and simulator log viewers. | 
| Software | Signal detection, the diagnosis workbench, software campaigns, rollout monitor, and the security monitor. | 
| Diagnostics | Fault patterns and quality signals. | 
| Manufacturing | Build order, factory registration, homologation, ownership transfer, and stop-ship. | 
| Sales | Data products and product detail, the subscriber roster and subscriber detail, grants, connectivity plans, and the feature catalog. | 
| Compliance | Market posture, consent and privacy, and the audit log. | 

## Live data and illustrative data
<a name="cs-portal-data-sources"></a>

The portal deliberately mixes two kinds of data, and distinguishes them at the value level rather than the screen level.

 **Live surfaces** read CMS’s deployed APIs through three clients, and own no storage of their own — nothing in the data model is duplicated between the console and the portal:
+ The data-model domain and the sales signal catalog read the data-processing API.
+ Simulate Vehicle, available vehicles, the trip simulator and both log viewers read the simulation API.
+ Data products and the subscriber roster read the subscription plane API.

 **Illustrative surfaces** — the command center, manufacturing, compliance, diagnostics, most of software, and parts of connectivity and sales — render from fixtures committed alongside the screens. They exist to show the shape of a domain the guidance does not implement end to end, and they are what makes the portal readable as a whole product rather than a partial one.

Every value the portal renders carries a provenance marker of `live`, `simulated` or `absent`. The marker is enforced, not decorative: the shared display component throws at render time on a missing or unrecognised marker, `absent` renders an explicit em-dash so "no data" stays distinguishable from zero, and the marker is emitted into the DOM so it is machine-checkable in tests. The markers were originally shown as a badge beside every value; across 227 call sites that made the portal unreadable, so the per-value badge was removed while the runtime guarantee was kept. In its place, the sign-in screen states that the data is simulated and a compact indicator sits in the top bar, so a screenshot of any single screen cannot be mistaken for live production data.

## Authorization
<a name="cs-portal-authorization"></a>

The portal signs into the same Cognito pool as the Fleet Manager console, and separates two audiences by group. A `subscriber` user reaches the subscriber-facing routes; administrative routes — registering a subscriber, marking a vehicle available — require the `connected-services` group. Subscribers see only the vehicles their subscription entitles them to: the inventory filters on the vehicle `producer` attribute, and subscription eligibility is scoped by the caller’s `custom:customerIds` claim.

See [Connected Services portal and subscription plane](connected-services-portal.md) for the subscription plane’s data model and stacks, and [Third-party data delivery](third-party-data-delivery.md) for the delivery pattern the plane implements.