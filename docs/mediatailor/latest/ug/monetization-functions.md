

# Working with MediaTailor Monetization Functions
<a name="monetization-functions"></a>

With MediaTailor Monetization Functions (Functions), you can customize how AWS Elemental MediaTailor manages session data and builds ad requests during ad insertion. Functions let you call external APIs, transform data with expressions, and modify ad decision server (ADS) request parameters or player parameters. You don't need to deploy or manage custom infrastructure.

Functions use *JSONata*, a lightweight query and transformation language for JSON data, to evaluate expressions. You write JSONata expressions to read session data, transform values, and define output. For the complete list of supported JSONata functions, see [JSONata expression reference](monetization-functions-jsonata.md).

Use Functions when you need to:
+ **Enrich ad requests with viewer data.** Call an identity service at session start and include the resolved identity in every ADS request for personalized ad targeting.
+ **Customize ADS request parameters.** Dynamically set the ADS URL, headers, or body based on session data, SCTE-35 signals, or external API responses.
+ **Run A/B tests across ad servers.** Split traffic between different ADS endpoints based on session attributes or random assignment.
+ **Build multi-step enrichment pipelines.** Chain multiple functions together to fetch data from one API, transform it, and pass the results to the next step.

## How Functions fit into the MediaTailor workflow
<a name="monetization-functions-workflow"></a>

When a viewer starts a playback session, MediaTailor evaluates your functions at specific points in the ad insertion flow called *lifecycle hooks*.

1. You define a function and attach it to a playback configuration through a function mapping.

1. MediaTailor runs the function at the designated lifecycle hook.

1. The function reads session data, optionally calls an external API, and writes results that MediaTailor uses during playback processing.

**Tip**  
If you are new to Functions, start with the [Quick start guide](monetization-functions-quickstart.md), then read [Lifecycle hooks](monetization-functions-hooks.md). For expression syntax and complete examples, see [JSONata expression reference](monetization-functions-jsonata.md) and [Function examples](monetization-functions-examples.md).

**Topics**
+ [How Functions fit into the MediaTailor workflow](#monetization-functions-workflow)
+ [Functions quick start guide](monetization-functions-quickstart.md)
+ [Functions lifecycle hooks](monetization-functions-hooks.md)
+ [Function types and composition](monetization-functions-types.md)
+ [Creating and managing Functions](monetization-functions-managing.md)
+ [JSONata expression reference for Functions](monetization-functions-jsonata.md)
+ [Function examples](monetization-functions-examples.md)
+ [Troubleshooting and monitoring Functions](monetization-functions-troubleshooting.md)
+ [Functions limits](monetization-functions-limits.md)