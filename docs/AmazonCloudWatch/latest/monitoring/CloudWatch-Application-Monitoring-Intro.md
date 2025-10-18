# Application performance monitoring (APM)

CloudWatch Application Signals provides application performance monitoring (APM) features such as pre-built, standardized dashboards for critical application metrics, 
 correlated trace spans, and a application map to enable you to visualize interactions between applications and their dependencies. You can also search and analyze 
 transaction spans and trace summaries to debug distributed application issues in a business context, for cases such as troubleshooting customer support tickets or
 finding top impacted customers. You can also create Service Level Objectives (SLOs) to closely track the performance KPIs of critical operations in your application, 
 enabling you to easily identify and triage operations that do not meet your business KPIs.

See the following sections for an overview of these troubleshooting capabilities:


* [Monitor the operational health of your applications with Application Signals](Services.md "Services.md")
* [Searching and analyzing spans](CloudWatch-Transaction-Search-search-analyze-spans.md "CloudWatch-Transaction-Search-search-analyze-spans.md")
**Start collecting application metrics and traces**

Get the most integrated application performance monitoring experience by auto-instrumenting applications to easily collect telemetry, whether they are running 
 in [Amazon EKS clusters](CloudWatch-Application-Signals-Enable-EKS.md "CloudWatch-Application-Signals-Enable-EKS.md"), [Amazon EC2](CloudWatch-Application-Signals-Enable-EC2Main.md "CloudWatch-Application-Signals-Enable-EC2Main.md"), 
 [Amazon ECS](CloudWatch-Application-Signals-Enable-ECSMain.md "CloudWatch-Application-Signals-Enable-ECSMain.md"),
 [Kubernetes](CloudWatch-Application-Signals-Enable-KubernetesMain.md "CloudWatch-Application-Signals-Enable-KubernetesMain.md"), [Lambda](CloudWatch-Application-Signals-Enable-LambdaMain.md "CloudWatch-Application-Signals-Enable-LambdaMain.md"), or 
 [on-premise](CloudWatch-Application-Signals-Enable.md "CloudWatch-Application-Signals-Enable.md"). Optionally,
 you can also use [OpenTelemetry](CloudWatch-OpenTelemetry-Sections.md "CloudWatch-OpenTelemetry-Sections.md") with Application Signals to collect telemetry.

###### Note

You must enable transaction search to get all APM features along with a new unified pricing for CloudWatch Application Signals, inclusive of X-Ray traces and application 
 transaction spans. For more information about pricing, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

###### Topics

* [Application Signals](CloudWatch-Application-Monitoring-Sections.md "CloudWatch-Application-Monitoring-Sections.md")
* [Service level objectives (SLOs)](CloudWatch-ServiceLevelObjectives.md "CloudWatch-ServiceLevelObjectives.md")
* [Transaction Search](CloudWatch-Transaction-Search.md "CloudWatch-Transaction-Search.md")
* [Synthetic monitoring (canaries)](CloudWatch_Synthetics_Canaries.md "CloudWatch_Synthetics_Canaries.md")
* [CloudWatch RUM](CloudWatch-RUM.md "CloudWatch-RUM.md")
* [Perform launches and A/B experiments with CloudWatch Evidently](CloudWatch-Evidently.md "CloudWatch-Evidently.md")
