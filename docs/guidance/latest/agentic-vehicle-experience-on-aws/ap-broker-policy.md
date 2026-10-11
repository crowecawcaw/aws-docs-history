

# Broker policy surfaces
<a name="ap-broker-policy"></a>

The broker is invoked from a DynamoDB stream on `vsa-{stage}-avx-findings`. For each new or updated Finding, it evaluates the following in order:

1.  **Consent** — Per-category consent from `vsa-{stage}-notification-devices`. Consent gates push, not the card: a Finding in a category the owner has opted out of still appears as an in-app card but sends no push.

1.  **Cardinality cap** — Per-owner, per-day ceiling on open cards. SSM key `/vsa/{stage}/avx/broker/cardinality-cap` (default 15). Excess is dropped in order of lowest priority then oldest.

1.  **Rate limit** — Per-owner per-hour and per-day caps on new cards. SSM key `/vsa/{stage}/avx/broker/rate-limit` (default day 10, hour 3).

1.  **Feedback demotion** — Dismissals in the trailing 30 days demote Findings with the same `finding_kind` and owner. A demoted Finding still creates an in-app card but does not push unless `p0`.

1.  **APNs threshold** — The minimum severity that triggers a push. SSM key `/vsa/{stage}/avx/broker/apns-severity-threshold` (default `p0`).

1.  **Priority arbitration** — When multiple Findings compete for a push slot in a short window, the broker selects by severity then `computed_at`.