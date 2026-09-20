

# Software dependency validation
<a name="dsperf02"></a>

 Third-party software components introduce sovereignty risks that standard security scanning doesn't detect. Export controls can block the delivery of updates. Copyleft licensing can create unintended source-code disclosure obligations. A critical dependency maintained by contributors in a single jurisdiction becomes a continuity risk if that jurisdiction faces trade restrictions. These concerns require evaluation criteria that go beyond vulnerability scanning to assess sovereignty-specific risks before components are deployed. 

 This capability covers the validation of third-party software components (open source libraries, commercial SDKs, and proprietary middleware) against sovereignty-specific criteria including export control, licensing, maintainer jurisdiction, and supply chain continuity. 


|  DSPERF02: How do you validate software dependencies for sovereignty compliance?  | 
| --- | 
| [DSPERF02-BP01 Validate third-party software components for sovereignty compliance](dsperf02-bp01.md) | 

## Capability intent
<a name="capability-intent-1"></a>
+  Third-party components are evaluated against sovereignty-specific criteria (export controls, licensing obligations, maintainer jurisdiction, update availability) before they enter the approved dependency list. 
+  The software bill of materials stays current and shows which third-party components are deployed and what risks they carry. 
+  Components subject to export controls or restrictive licensing are identified and managed with explicit acceptance of the constraints they impose. 
+  Supply chain continuity risk is assessed for critical dependencies, with mitigation plans for components where update availability depends on a single jurisdiction. 
+  Validation is integrated into the development lifecycle so that new dependencies are assessed before they reach production, not discovered during compliance reviews. 

## Maturity levels
<a name="maturity-levels-1"></a>

 These levels summarize what each stage of maturity looks like for this capability as a whole. 


|  Level  |  Name  |  What it looks like  | 
| --- | --- | --- | 
|  1  |  Initial  |  Dependencies are added based on functionality without sovereignty-specific evaluation. The software bill of materials is incomplete or absent. Export control and licensing risks are discovered reactively.  | 
|  2  |  Emerging  |  High-risk components are evaluated for licensing and export control concerns. A partial software bill of materials exists. Some components have known sovereignty concerns but no formal mitigation plan.  | 
|  3  |  Defined  |  All third-party components are evaluated against documented sovereignty criteria before approval. The software bill of materials is maintained and current. Components with export control or licensing constraints are explicitly accepted with documented risk decisions. Supply chain continuity is assessed for critical dependencies.  | 
|  4  |  Proactive  |  Dependency validation runs automatically in CI/CD pipelines and blocks unapproved components before they reach production. Maintainer jurisdiction and update availability are monitored for changes. Alternative components are pre-identified for critical dependencies with supply chain risk.  | 
|  5  |  Optimized  |  Dependency governance adapts to changing geopolitical conditions proactively. Supply chain risk is quantified and informs architectural decisions about component selection. The organization contributes to or forks critical open source dependencies to reduce single-jurisdiction risk.  | 

## Common issues to watch for
<a name="common-issues-to-watch-for-1"></a>
+  Vulnerability scanning treated as sufficient dependency governance, which overlooks sovereignty-specific risks that scanners do not evaluate, such as export controls, licensing obligations, and maintainer jurisdiction. 
+  Software bill of materials that captures direct dependencies but not transitive ones, so sovereignty risks stay hidden in the dependency tree. 
+  Export control assessments conducted at initial adoption but not revisited when geopolitical conditions or component classification changes. 
+  Critical dependencies with single-jurisdiction maintainers identified as a risk but without mitigation plans (forking, alternative sourcing, or contribution) that would maintain update availability if that jurisdiction becomes restricted. 
+  Dependency validation that exists as a policy but isn't enforced in pipelines, so unapproved components reach production through developer workstations or alternative deployment paths. 