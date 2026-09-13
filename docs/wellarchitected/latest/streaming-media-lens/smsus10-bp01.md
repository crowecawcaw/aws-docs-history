

# SMSUS10-BP01 Establish sustainability KPIs and ongoing optimization processes
<a name="smsus10-bp01"></a>

Measure the sustainability of your streaming workload with metrics you can actually obtain, assign ownership for acting on them, and review them on a regular cadence. Without measurement and accountability, sustainability improvements are one-time efforts that decay as the catalog, audience, and architecture change.

**Desired outcome:**
+ Sustainability is tracked through measurable resource-proxy metrics and the account-level carbon data AWS provides, not through figures that can't be obtained.
+ A named, cross-functional owner is accountable for reviewing the metrics and acting on findings.
+ Optimization is a recurring cadence with a baseline and trend, not a single project.

**Common anti-patterns:**
+ Defining key performance indicators (KPIs) such as energy or carbon per individual stream that AWS doesn't expose, so the metric can never be populated and the program stalls.
+ Collecting sustainability metrics on a dashboard that no one owns or reviews, so findings never turn into action.
+ Treating a sustainability optimization as a one-time project, so gains erode as the catalog and audience change.
+ Ignoring the right-sizing and efficiency recommendations that AWS tooling already surfaces.

**Benefits of establishing this best practice:**
+ A reliable view of efficiency over time, because metrics are based on data that can actually be obtained.
+ Findings that turn into action, because a named owner is accountable for review and follow-through.
+ Sustained rather than decaying gains, because optimization runs on a cadence with a baseline and trend.
+ Faster wins, because existing AWS recommendations are acted on rather than ignored.

**Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>

AWS doesn't expose energy or carbon at the granularity of an individual stream, so a KPI like "watts per stream" can't be populated and will stall a program that depends on it. The workable approach pairs resource proxies that the workload can emit, bytes delivered per viewing session, encoder compute hours per title, content delivery network (CDN) cache hit ratio, non-production running hours, and the share of work on efficient hardware, with the account-level carbon estimates from the AWS Customer Carbon Footprint Tool, which reports per Region on a monthly cadence. The proxies give frequent, useful signal at the workload level. The carbon tool gives the authoritative account-level trend. Together they form a measurable KPI set, but neither alone is sufficient.

Measurement without ownership produces dashboards nobody acts on. Sustainability spans encoding, delivery, storage, hardware, and process, so no single team owns all the levers, which is exactly why a cross-functional owner accountable for reviewing the metrics and driving action is necessary. Instrumenting and reviewing metrics costs effort, so favor a small set of proxies that map to decisions teams can actually make over an exhaustive set of metrics that are collected but never used.

A streaming workload changes constantly as titles are added, audiences shift, and services evolve, so efficiency gained once erodes unless it is revisited. Establish a baseline, review the proxy KPIs and the monthly carbon trend on a fixed cadence, act on the right-sizing and efficiency recommendations AWS tooling already surfaces, and run periodic architecture audits to catch drift that day-to-day metrics miss.

### Implementation steps
<a name="implementation-steps"></a>

1. **Define measurable proxy KPIs:** Select resource-proxy metrics the workload can emit, instead of per-stream energy figures that can't be obtained.
+ Bytes per viewing session
+ Encoder compute hours per title
+ Cache hit ratio
+ Non-production running hours
+ The share of work on efficient hardware

1. **Instrument with custom metrics and dashboards:** Publish the proxy KPIs as Amazon CloudWatch custom metrics and build dashboards and alarms so trends and regressions are visible to the teams that own the levers.

1. **Baseline against account-level carbon data:** Record a baseline from the AWS Customer Carbon Footprint Tool and review the monthly, per-Region trend alongside the proxy KPIs to confirm workload changes move the account-level figure.

1. **Act on AWS efficiency recommendations on a cadence:** Review and apply AWS Trusted Advisor and AWS Compute Optimizer recommendations regularly so surfaced right-sizing and waste-reduction opportunities are acted on rather than ignored.

1. **Assign cross-functional ownership and a review cadence:** Name an owner accountable for the sustainability KPIs and establish a recurring review across the following teams.
+ Encoding
+ Delivery
+ Storage
+ Infrastructure

1. **Run periodic sustainability audits:** Conduct scheduled architecture reviews of the streaming workload against the Sustainability Pillar to catch drift and identify optimizations that routine metrics don't surface.

## Resources
<a name="resources"></a>

**Related best practices**
+ [SMSUS02-BP01 Implement adaptive infrastructure scaling based on viewer patterns](smsus02-bp01.html)
+ [SMSUS09-BP01 Adopt sustainable development and deployment practices](smsus09-bp01.html)

**Related documents**
+ [AWS Customer Carbon Footprint Tool](https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/)
+ [Sustainability Pillar, Process and culture](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/process-and-culture.html)

**Related services**
+ [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
+ [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/)
+ [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/)