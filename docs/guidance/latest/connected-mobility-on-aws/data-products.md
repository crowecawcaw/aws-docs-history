

# Data products
<a name="data-products"></a>

A data product is a named, versioned feed from one producer, with one connection, one authentication method, and one transform manifest. [Third-party data delivery](third-party-data-delivery.md) covers the model’s vocabulary, where each element is stored, and the authorization contract. This section covers the lifecycle an operator drives through it: **define**, **map**, **deliver**.

## The operator declares the catalog
<a name="dp-operator-declares"></a>

This platform is a third-party fleet platform. It has no knowledge of any particular producer’s portal, and does not assume one exists. So a fleet operator declares, inside the platform, every data product they intend to consume — producer identity, connection endpoint, authentication method, credentials pointer, tier, and transform manifest.

That is the load-bearing decision of the whole definition layer. The alternative — discovering products by calling a producer’s catalog API — would be less configuration to type and would make the platform a captive client of one producer’s portal. Operator-declared configuration keeps it generic across producers who have no portal at all.

The consequence is worth stating rather than papering over: **the catalog can drift from what the producer actually offers, and nothing reconciles the two.** Treat the catalog as the operator’s declaration of intent, not as a mirror of the producer’s inventory.

## Connection type and authentication are separate axes
<a name="dp-connection-auth"></a>

Connection type is an enum with genuinely different fields per value, and both the definition flow and the product detail view branch on it:


| Connection type | Type-specific fields | What the endpoint means | 
| --- | --- | --- | 
|  `rest_polling`  | Polling interval | The base URL to poll | 
|  `grpc_streaming`  | Service name, method name | The gRPC target | 
|  `kafka`  | Topic, consumer group | Comma-separated bootstrap servers | 
|  `websocket_inbound`  | Listen endpoint, allowed origin | Inverted — the platform owns the endpoint the producer connects **to**  | 

A single generic "connection string" field would have been faster to build and impossible to validate, and a detail view could not have explained to an operator what the string meant. The enum is what allows a Kafka product to require both a topic **and** a consumer group before it can be saved.

 **The consumer group is a captured field rather than a derived one.** It is the platform’s own identity for offset tracking, and two subscribers sharing a group share offsets and silently take records from each other — a failure that presents as data loss rather than as misconfiguration. Making it explicit and required puts the decision in front of the operator instead of defaulting it.

Authentication is a separate axis — OAuth 2.0, API key, mTLS, or SASL/SCRAM — because the real combinations cross: mTLS fronts inbound WebSocket, sometimes gRPC, sometimes Kafka; SASL/SCRAM is standard for cloud-deployed Kafka; OAuth and API keys dominate REST. Folding the two axes into one enum would produce a cross-product whose cells are mostly nonsense.

## Credentials by reference, never by value
<a name="dp-credentials"></a>

The catalog stores an AWS Secrets Manager ARN. The secret itself never enters the catalog record and never reaches the browser.

The detail view masks part of the ARN for display. To be precise about what that is: **the masking is a signal, not a control.** An ARN is catalog metadata, not a secret. It is masked so that an operator reading the page absorbs "credentials are referenced here, not stored here" without having to be told.

## Why a transform manifest exists
<a name="dp-why-manifest"></a>

Three producers describe the same physical quantity three different ways, with three different severity scales — a battery state of charge arrives as a nested camelCase path from one, a snake\_case protobuf field from another, and a flat REST key from a third. Seeing `speedMph`, `vehicle_speed_mph` and `speed` all landing on one canonical signal is the entire argument for normalizing at the boundary rather than downstream.

The demonstration data is deliberately inconsistent across producers for this reason. Producer catalogs also deliberately do not cover every canonical signal, and coverage is displayed as a count of mapped signals against the total so gaps are visible rather than implied.

 **Severity is mapped, never inferred.** Producer event names and producer severity labels are both producer-private vocabulary — one producer’s `HIGH` is another’s `warning`. Downstream flows for safety, maintenance and reporting key on the canonical name and the canonical severity, so the mapping is an explicit pair on both. Inferring severity from the producer’s own label would mean a producer relabelling `HIGH` to `MEDIUM` silently changes this platform’s safety behavior.

## Mapping is confirmed, not inferred
<a name="dp-mapping-confirmed"></a>

An auto-match action proposes pairings by exact normalized match first, then by shortest producer name containing the canonical name, then the inverse. It is deliberately naive, and is labelled as a starting point rather than an answer.

Sophisticated matching — synonym sets, ontologies, embeddings — was rejected for a specific reason: the operator confirms every pair either way, so a simple scorer that visibly guesses is safer than a sophisticated one that quietly guesses. A wrong pairing that looks like a guess gets checked; a wrong pairing that looks authoritative does not.

## Delivery
<a name="dp-delivery"></a>

Four properties govern the delivery layer:

 **One topic per product, not per subscriber.** The subscriber-facing topic is `cs-product-<product_id>` and carries the producer’s own format. Subscribers are separated by credentials and consumer group, not by topic.

 **One generic processor; sources are configuration.** The OEM telemetry processor subscribes to a topic **pattern** rather than a literal list, derives the source identity from the topic name, and applies that product’s transform manifest. A new product therefore appears by convention. The processor picks up a new topic within roughly five minutes, governed by its partition-discovery interval — so onboarding is not instantaneous, and verification should be planned around that window.

 **No side-loading.** Every record travels the same path. There is no bypass for a product that seems simple enough not to need a manifest.

 **An unmatched topic fails loudly.** Telemetry arriving on a topic with no mapping increments a metric and raises an alarm rather than being dropped quietly. See [Stream processing alarms](mon-alarms.md#mon-flink-alarms), including the note that this particular alarm does not self-clear in this release.

Adding a data product adds no Flink application. A source graduates to its own application only on a hard trigger — a compliance mandate for physical separation, or volume that distorts the shared job’s sizing — and never on source count alone. Per-source applications would turn onboarding back into a deployment, multiply the KPU floor, and turn a single Flink version upgrade into many migrations. The isolation usually being sought is available inside one job through keying, per-source dead-letter handling and tagged metrics; and where the real concern is a subscriber trust boundary, that is a question about what a subscriber’s credentials can reach, not about how many processes are running.

## Onboarding a product
<a name="dp-onboarding"></a>

Four steps, no application code:

1.  **Declare the topic** — add a name, partition count and replication factor to the topic inventory script and run it. The script is idempotent and skips existing topics. Broker-side auto-creation is a safety net rather than the mechanism: declaring the topic keeps partitioning deliberate and keeps the repository’s inventory answerable.

1.  **Grant the publisher write access** on that topic.

1.  **Place the transform manifest in Amazon S3** at `manifests/<product_id>-transform.json`, validated against the manifest schema.

1.  **If it is a delivery topic, grant each subscriber** scoped read on that topic, and describe and alter permissions on **its own** consumer group. Nothing wider.

## Current limitations
<a name="dp-limitations"></a>

The definition layer and the delivery layer are not yet connected, and the boundary matters when planning work on this area.
+  **The definition flow produces no manifest.** Mappings captured in the interface do not yet become the manifest file the processor reads; the one live product’s manifest was authored by hand. Until that loop closes, the catalog is a description of the pipeline rather than its configuration.
+  **Product definitions, fleet-to-product assignments and vehicle enrollments are not persisted.** They are session-scoped in the browser, and a page refresh loses them. Read paths, subscription operations, availability marking and end-to-end record pull are real; product **definition** is not yet.
+  **Producer signal and event advertisement is seeded per producer** rather than retrieved from the producer.
+  **The interface’s canonical signal list is a curated subset** of the platform’s full signal catalog, maintained separately. It will drift from the full catalog, and nothing currently detects that drift. Events are complete.
+  **The captured connection parameters are not consumed by the live path.** The one deployed Kafka route is wired by the topic inventory, an AWS IoT rule and an IAM statement — not by the catalog record.