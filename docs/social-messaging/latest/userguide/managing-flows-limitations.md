

# Limitations and considerations
<a name="managing-flows-limitations"></a>

Consider the following limitations when working with WhatsApp Flows:
+ **Flow name uniqueness** — Flow names must be unique within a WABA.
+ **Flow JSON size** — The maximum size of a Flow JSON definition is 10 MB.
+ **Flow JSON version** — Supported versions for publishing are 5.1, 6.0–6.3, and 7.0–7.3. We recommend version 7.3.
+ **Only DRAFT Flows can be deleted** — Published or deprecated Flows cannot be deleted.
+ **Data exchange endpoints** — Flows with endpoints that exchange data between screens and a business server (the `endpoint_uri` and `data_exchange` capabilities) are planned for an upcoming release. Only Flows without an endpoint are currently supported.
+ **Flow migration** — Copying or migrating Flows between WABAs is not supported. You can clone a Flow within the same WABA using the `cloneFlowId` parameter.
+ **Rate limits** — Standard Meta API rate limits apply to all Flow operations.