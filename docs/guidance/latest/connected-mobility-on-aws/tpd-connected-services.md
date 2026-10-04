

# The Connected Services subscription plane: a concrete implementation
<a name="tpd-connected-services"></a>

The Connected Services subscription plane in this guidance is a concrete implementation of the pattern above, shipped as three opt-in stacks: `SubscriptionsStack`, `ConnectedServicesUiStack`, and `ConnectedServicesConsumerStack`. It is a mediated delivery — subscribers pull records over REST — that composes with the underlying Kafka topic model for delivery to more capable consumers.

## Seven nouns worth keeping distinct
<a name="cs-model"></a>

Seven concepts show up in this plane, and confusing any two makes the rest fuzzy. The distinction between **product** and **subscription** and between **subscription** and **enrollment** is where most of the design leverage lives.


| Concept | Owner | What it is | 
| --- | --- | --- | 
|  **Producer**  | External organization | Whoever publishes vehicle data — an OEM, a Tier 1 telematics provider, or CMS itself | 
|  **Data product**  | Declared in CMS | A named, versioned feed from one producer with one connection, one authentication method, and one transform manifest | 
|  **Product topic**  | CMS/MSK |  `cs-product-<product_id>` — the subscriber-facing Kafka topic carrying the producer’s own format, not CMS canonical | 
|  **Transform manifest**  | CMS, in Amazon S3 | The rules that turn producer format into CMS canonical | 
|  **Subscriber**  | A consuming principal | Holds credentials and its own consumer group. CMS is one subscriber among many; it is deliberately not a special case | 
|  **Subscription**  | CMS | A subscriber’s declared relationship to one catalog entry — a tier, a vehicle capacity, a scope | 
|  **Enrollment**  | CMS | The specific VINs inside a subscription that data actually flows for | 

Two distinctions that are easy to lose and expensive to lose:
+  **Product ≠ subscription.** The catalog entry says **what exists and how to connect**. The subscription says **we consume it, at this tier, for up to N vehicles**. One catalog entry can carry many subscriptions.
+  **Subscription ≠ enrollment.** A subscription with a 500-vehicle capacity and zero enrolled VINs moves no data. Capacity is the ceiling; enrollment is the actual set.

## Where things live
<a name="cs-model-storage"></a>


| Element | Location | Notes | 
| --- | --- | --- | 
| Products |  `services/connectors/subscriptions/products.json` (Lambda-bundled) | Four seeded products: `telemetry-hifi-v1`, `meridian-telemetry-v1`, `diagnostics-v1`, `charging-sessions-v1`  | 
| Subscriptions |  `cms-{stage}-storage-subscriptions-{region}-{account}`  | Partition key `subscription_id` (ULID). GSI on `consumer_id` provides "my subscriptions" ordering by creation time | 
| Vehicle availability |  `cms-{stage}-storage-vehicle-availability-{region}-{account}`  | Populated by the admin `mark_available` route; read by the subscriber `vehicles_available` route | 
| Feed cache |  `cms-{stage}-storage-cs-feed-cache-{region}-{account}`  | Deployed by `ConnectedServicesConsumerStack`; the read path is not yet wired (partial in v0.4.0) | 

## Authorization
<a name="cs-authorization"></a>

Every subscriber-facing route requires the `subscriber` Amazon Cognito group; every admin route requires the `connected-services` group.

 **Subscription ownership is derived from the row’s `consumer_id` field, not from a JWT claim.** At create time, `consumer_id` is written from the caller’s Cognito `sub` claim and is immutable thereafter. Every subsequent operation on the subscription — detail, add scope, remove scope, pull records — reads the row and enforces `row.consumer_id == claims["sub"]`. This prevents privilege escalation via a client-supplied `consumer_id` and makes the row’s contents alone determine access.

A JWT `custom:subscriptionIds` claim was considered as an ownership signal but had no writer path. It is retired and does not participate in authorization.

 **Subscriber-scope isolation.** Each subscriber runs its own Kafka consumer group and holds least-privilege AWS credentials scoped to the topics its subscription entitles it to. Two subscribers sharing a consumer group would share offsets and silently take records from each other — the failure would look like data loss, not misconfiguration — so the consumer-group identity is a captured field per subscriber, not a default.

## Delivery target
<a name="cs-delivery-target"></a>

The subscription plane ships REST pull as the primary delivery target today. A second delivery target, `msk_topic`, is implemented for producers that write into the platform through a product topic (`cs-product-<product_id>`) rather than through a REST push — the sibling **CS-mediated Meridian ingestion** pattern uses this path to bring an external producer’s telemetry INTO CMS on canonical MSK topics, where the generic `OEMTelemetryProcessor` picks it up via a topic-pattern subscription and applies the product’s transform manifest by topic-derived source key.

Additional shapes that appeared in an earlier draft of the plane (`kafka_replicator`, `privatelink_kafka`) were cut and superseded by the `msk_topic` shape.

## CMS as its own subscriber
<a name="cs-cms-as-subscriber"></a>

 `ConnectedServicesConsumerStack` deploys CMS’s own consumer surface. CMS holds a single machine subscriber account in the **producer’s** Cognito pool — not a new CMS pool, not a new CMS Cognito group — and one subscription to `telemetry-hifi-v1`. The subscriber credential lives server-side in AWS Secrets Manager (`cms-{stage}-connected-services-subscriber-{region}-{account}`); the browser never sees it. Two guards enforce this: a frontend bundle-hygiene test that runs against the real production bundle, and a deploy-time asset scan that greps for the actual credential value.

The enrollment step an operator triggers from Vehicle Detail is the same `POST /subscriptions/{id}/scope` call an external subscriber makes, so the demo path exercises the real contract rather than a CMS-privileged shortcut. Three CMS-side proxy routes at `/api/v1/connected-services/subscription-feed*` proxy the producer routes; `Cache-Control: no-store` is set on all three. The GET route is a **filter** — a fleet-scoped operator sees only their fleet’s rows within the subscription’s scope — and the POST and DELETE scope routes are **gates** — each names exactly one VIN, so a scope violation returns HTTP 403. Two authorization checks compose: the producer enforces that CMS’s subscriber account sees only its own subscription’s VINs, and CMS enforces that a given operator sees only their fleet’s VINs within those.

## Partial in this release
<a name="cs-partial"></a>
+ The `DataProductsView` "Create data product" flow in the Connected Services portal is a UI-shape stub; there is no submission target and no persistence, so product **definitions** are browser-only in this release. Read paths, subscription CRUD, availability marking, and end-to-end record pull are real.
+ The feed-cache table `cms-{stage}-storage-cs-feed-cache-{region}-{account}` is deployed but nothing reads or writes it — the CMS-side proxy calls the producer live on every request. The authorization contract holds either way; the freshness and TTL properties a cache would provide do not exist yet.
+ The `charging-sessions-v1` product table exists on staging only; the production table has not been created.