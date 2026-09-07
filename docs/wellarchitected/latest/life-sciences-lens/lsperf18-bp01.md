

# LSPERF18-BP01 Perform cross-functional performance reviews between IT and scientists
<a name="lsperf18-bp01"></a>

 IT professionals and scientists conduct joint performance reviews to evaluate system effectiveness. These teams set specific goals that align technical capabilities with scientific needs. For example, they might target a 99.9% system uptime while verifying that data accuracy meets research requirements. 

 **Desired outcome:** Achieving specific uptime and performance goals through joint performance reviews and aligned technical-scientific goal setting. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 To effectively implement collaborative performance reviews, bring together IT professionals and scientists in structured evaluation sessions that assess system effectiveness from both technical and scientific perspectives. These cross-functional teams should establish specific, measurable goals that harmonize technical capabilities with scientific requirements, such as maintaining 99.9% system uptime while simultaneously verifying that data accuracy meets rigorous research standards. 

 Create detailed documentation of these performance standards, clearly articulating how technical metrics connect to validation requirements and scientific outcomes. 

 Develop comprehensive monitoring dashboards that visualize both technical performance indicators (latency, throughput, resource utilization) and scientific metrics (data quality, validation status, experimental reproducibility). This integrated view enables teams to identify optimization opportunities that don't compromise scientific integrity. 

 Implement regular review cycles where technical and scientific stakeholders jointly analyze performance data, discuss potential improvements, and make data-driven decisions about system adjustments. 

### Implementation steps
<a name="implementation-steps"></a>

1.  Schedule reviews using AWS Systems Manager OpsCenter items. 

1.  Track service-level agreements (SLAs) with Amazon CloudWatch dashboards and custom metrics. 

1.  Document goals in AWS Well-Architected Tool workloads. 

1.  Implement Amazon SageMaker AI Model Monitor for accuracy checks. 

1.  Use Service Catalog to enforce approved configurations. 