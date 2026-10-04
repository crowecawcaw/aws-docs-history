

# Best practices
<a name="tpd-best-practices"></a>

 **Design topics as contracts.** A third party consumes a stable, versioned topic with a schema held in a registry, not the platform’s internal topics, so producers can evolve without breaking consumers.

 **Keep source-specific logic in a declarative manifest, not in code.** The guidance’s OEM telemetry pipeline reduces its connector to an OEM-agnostic passthrough and moves all signal extraction, field splitting, and unit conversion into a versioned manifest in Amazon S3, so onboarding a new producer or consumer becomes a manifest change rather than a code change — the single most effective step for reusability. See [OEM telemetry processor](flink-stack.md#oem-telemetry-processor) in the architecture-details chapter for the reference implementation.

 **Give every consumer its own identity and least-privilege authorization**, scoped to the topics and signals it is entitled to, so consent and entitlement are enforced at the subscription rather than by trust.

 **Isolate by consumer group and quota** so tenancy is structural rather than a matter of good behavior.

 **Design to the producer’s published limits** rather than assuming infinite capacity — explicit enrollment quotas and pagination caps become first-class constraints, keeping a high-volume consumer from tripping a limit it did not know existed.

 **Make delivery observable end to end** — per-consumer lag, throughput, and error rates — so a problem on one consumer is visible before it becomes a support escalation, and the platform can prove which party a degradation belongs to.