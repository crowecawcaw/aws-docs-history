

# Graceful degradation
<a name="bca-graceful-degradation"></a>

AVX is designed to degrade gracefully when a foundation is partially unavailable.
+  **ADP Memory miss** — if the `persona_loader` cannot load a data product at session init (Athena timeout, cross-account grant not yet propagated, upstream Glue table absent), the affected tools return a structured unavailable message rather than an error. The session continues with the data that is available; the supervisor informs the caller that some context could not be loaded.
+  **ADP KB unavailable** — if a Bedrock Retrieve call fails, the knowledge tools fall back to local corpus content where available (DTC code rules, triage logic). The supervisor notes that the full knowledge base could not be consulted and recommends the caller follow up with a service advisor.
+  **CMS Redis unavailable** — if the LKS read fails at session init, the supervisor proceeds without a live telemetry snapshot. Triage classifications are based on the caller’s verbal description only and will be conservative (P1 when in doubt). The supervisor explicitly notifies the caller that live vehicle state is unavailable.
+  **CMS DynamoDB write failure** — if the `book()` tool cannot write the service-history row, it returns the STAR envelope with `status: sink-error` rather than silently swallowing the failure. The driver can ask for a person, who can complete the booking.

These degradation behaviors are hard-coded in each tool’s error handling path.