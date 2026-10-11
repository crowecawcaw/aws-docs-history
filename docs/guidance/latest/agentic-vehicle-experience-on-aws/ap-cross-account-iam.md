

# Broker Boundaries
<a name="ap-cross-account-iam"></a>

The outreach broker (`vsa-{stage}-avx-broker`) owns channel selection, consent enforcement, rate limiting, cardinality capping, and priority arbitration. No agent code participates in these decisions.

## Enforced boundaries
<a name="enforced-boundaries"></a>
+ No code path from a Tier 2 agent module reaches SNS, APNs, Amazon Connect, SMS, or any delivery API. The broker is the sole writer of `sns:Publish` for AVX Findings.
+ Executor classes are not importable from agent modules. An executor is called only from the `/findings/{id}/approve` path after the Action row is written.

These two rules are test-enforced.