

# Development and deployment
<a name="smsus09"></a>

The engineering process behind a streaming service carries its own resource footprint, dominated by idle non-production environments.


| SMSUS09: How do you incorporate sustainability into your development and deployment processes? | 
| --- | 
| [SMSUS09-BP01 Adopt sustainable development and deployment practices](smsus09-bp01.md) | 

## Capability intent
<a name="smsus09-intent"></a>
+ Non-production environments exist only when in use.
+ Build environments are right-sized and dependencies are cached.
+ Deployment overlap windows are as short as safety allows.
+ Sustainability metrics are visible within the delivery pipeline.

## Common issues to watch for
<a name="smsus09-issues"></a>
+ Development and staging environments running continuously including nights and weekends.
+ Oversized build environments rebuilding dependencies from scratch every run.
+ Blue/green deployments with long overlap windows doubling resources far beyond what cutover requires.
+ No visibility into non-production running hours or build compute hours.