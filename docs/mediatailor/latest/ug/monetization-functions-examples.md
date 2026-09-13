

# Function examples
<a name="monetization-functions-examples"></a>

Before working through these examples, you should be familiar with:
+ [Lifecycle hooks](monetization-functions-hooks.md) — Input fields and output namespaces available at each lifecycle hook.
+ [Function types and composition](monetization-functions-types.md) — How each function type works and its configuration fields.
+ [Creating and managing](monetization-functions-managing.md) — How to create functions and attach them to playback configurations.

This page provides complete, working function configurations for common use cases. Each example includes the scenario, the full configuration, the function mapping, and an explanation of what happens when the function runs.


| Example | Scenario description | 
| --- | --- | 
| [Example 1: Data enrichment](monetization-functions-examples-enrichment.md) | Fetch a LiveRamp identity envelope at session start and store it in player parameters. | 
| [Example 2: A/B traffic split](monetization-functions-examples-ab.md) | Split ad request traffic evenly between two ad decision server URLs for A/B testing. | 
| [Example 3: Contextual metadata](monetization-functions-examples-contextual-metadata.md) | Query Elemental Inference for IAB content classifications and GARM brand safety signals to enrich ad requests with contextual metadata. | 
| [Example 4: Secondary ad server fallback](monetization-functions-examples-backup-ads.md) | Fetch ads from a secondary ad server when the primary ADS response is short, and append them to the ad list. | 