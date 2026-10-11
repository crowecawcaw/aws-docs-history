

# Delivery
<a name="dp-delivery"></a>

Four properties govern the delivery layer:

 **One topic per product, not per subscriber.** Each product’s inbound feed is the topic `cs-product-<product_id>`, which carries the producer’s own format. The producer writes it and CMS reads it. Readers of the topic are separated by credentials and consumer group, not by topic. That keeps offsets apart, but it does not limit which vehicles a reader sees: Kafka permissions apply to a whole topic, so every reader of a product topic can read every VIN in it. A shared product topic is therefore safe only while every reader may see every record. Delivering a product to subscribers entitled to different vehicles uses a topic per subscription; see [Real-time B2B delivery over Amazon MSK](tpd-realtime-b2b.md) in the Third-party data delivery chapter.

 **One generic processor; sources are configuration.** The OEM telemetry processor subscribes to a topic **pattern** rather than a literal list, derives the source identity from the topic name, and applies that product’s transform manifest. A new product therefore appears by convention. The processor picks up a new topic within roughly five minutes, governed by its partition-discovery interval — so onboarding is not instantaneous, and verification should be planned around that window.

 **No side-loading.** Every record travels the same path. There is no bypass for a product that seems simple enough not to need a manifest.

 **An unmatched topic fails loudly.** Telemetry arriving on a topic with no mapping increments a metric and raises an alarm rather than being dropped quietly. See [Stream processing alarms](mon-alarms.md#mon-flink-alarms), including the note that this alarm does not self-clear.

Adding a data product adds no Flink application. A source graduates to its own application only on a hard trigger — a compliance mandate for physical separation, or volume that distorts the shared job’s sizing — and never on source count alone. Per-source applications would turn onboarding back into a deployment, multiply the KPU floor, and turn a single Flink version upgrade into many migrations. The isolation usually being sought is available inside one job through keying, per-source dead-letter handling and tagged metrics; and where the real concern is a subscriber trust boundary, that is a question about what a subscriber’s credentials can reach, not about how many processes are running.