

# Onboarding a product
<a name="dp-onboarding"></a>

Four steps, no application code:

1.  **Declare the topic** — add a name, partition count and replication factor to the topic inventory script and run it. The script is idempotent and skips existing topics. Broker-side auto-creation is a safety net rather than the mechanism: declaring the topic keeps partitioning deliberate and keeps the repository’s inventory answerable.

1.  **Grant the publisher write access** on that topic.

1.  **Place the transform manifest in Amazon S3** at `manifests/<product_id>-transform.json`, validated against the manifest schema.

1.  **If it is a delivery topic, grant each subscriber** scoped read on that topic, and describe and alter permissions on **its own** consumer group. Nothing wider.