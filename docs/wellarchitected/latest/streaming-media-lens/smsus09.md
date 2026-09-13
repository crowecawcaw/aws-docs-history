

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

## Maturity levels
<a name="smsus09-maturity"></a>


| Level | Name | What it looks like | 
| --- | --- | --- | 
| 1 | Initial | Non-production environments run continuously. Builds rebuild from scratch every run. No visibility into engineering process resource use. | 
| 2 | Emerging | Some environments stopped outside working hours. Build caching partially adopted. Deployment overlap isn't tracked. | 
| 3 | Defined | Environments defined as code and created on demand. Builds right-sized with dependency caching. Deployment overlap windows are minimized. | 
| 4 | Proactive | Non-production running hours and build compute hours tracked in the pipeline. On-demand device testing replaces standing labs. | 
| 5 | Optimized | Sustainability metrics visible within CI/CD. Engineering process efficiency is reviewed on a cadence alongside production workload metrics. | 

## Common issues to watch for
<a name="smsus09-issues"></a>
+ Development and staging environments running continuously including nights and weekends.
+ Oversized build environments rebuilding dependencies from scratch every run.
+ Blue/green deployments with long overlap windows doubling resources far beyond what cutover requires.
+ No visibility into non-production running hours or build compute hours.