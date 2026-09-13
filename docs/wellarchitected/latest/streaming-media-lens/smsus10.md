

# Measurement and optimization
<a name="smsus10"></a>

Without measurement and ownership, sustainability improvements are one-time efforts that decay.


| SMSUS10: How do you drive ongoing improvement in sustainability for your streaming workloads? | 
| --- | 
| [SMSUS10-BP01 Establish sustainability KPIs and ongoing optimization processes](smsus10-bp01.md) | 

## Capability intent
<a name="smsus10-intent"></a>
+ Sustainability is tracked through metrics that can actually be obtained, not aspirational figures.
+ A named owner is accountable for reviewing and acting on findings.
+ Optimization runs on a recurring cadence with a baseline and visible trend.
+ Existing AWS efficiency recommendations are acted on rather than ignored.

## Maturity levels
<a name="smsus10-maturity"></a>


| Level | Name | What it looks like | 
| --- | --- | --- | 
| 1 | Initial | No sustainability metrics defined. Optimization is one-time with no baseline or ownership. | 
| 2 | Emerging | Some resource proxies collected (bytes per session, compute hours). No named owner. Review happens only when prompted. | 
| 3 | Defined | A measurable KPI set is defined and baselined. A named owner reviews metrics on a fixed cadence. AWS efficiency recommendations are acted on. | 
| 4 | Proactive | Proxy KPIs and account-level carbon data are reviewed together. Regressions trigger action. Periodic architecture audits supplement metric review. | 
| 5 | Optimized | Efficiency improves continuously as catalog and audience change. The KPI set itself evolves as better proxies become available. | 

## Common issues to watch for
<a name="smsus10-issues"></a>
+ Defining KPIs that depend on data AWS doesn't expose (energy per stream, carbon per title).
+ Dashboards that no one owns or reviews, so findings never become action.
+ Treating sustainability as a one-time project with no follow-up cadence.
+ Ignoring right-sizing recommendations that tooling already surfaces.