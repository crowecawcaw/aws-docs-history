

# ADVSUS05-BP02 Optimize fraud detection systems for resource efficiency
<a name="advsus05-bp02"></a>

 Fraud detection runs continuously against every impression, click, and conversion, so treating all traffic identically provisions compute for the worst case. When you match the intensity and placement of detection to each segment's risk, the workload consumes fewer resources without weakening its controls. 

 **Desired outcome:** 
+  Fraud detection in your video streaming advertising environment meets its accuracy and latency requirements while consuming the minimum compute, storage, and data-transfer resources needed for the workload. 
+  Detection accuracy and business risk thresholds are met with right-sized, energy-efficient compute rather than continuously over-provisioned capacity. 
+  Sampling, scheduling, and Regional placement decisions are driven by the actual risk profile of the traffic being analyzed. 
+  Fraud signal data is retained only as long as it is needed for compliance, security, or model accuracy. 

 **Common anti-patterns:** 
+  Running full-fidelity fraud analysis on every event when intelligent sampling would meet the same business requirement. 
+  Provisioning persistent, general-purpose compute for bursty or variable detection workloads. 
+  Centralizing detection in a single Region and moving large volumes of impression and click data across Regions to reach it. 
+  Retaining all raw fraud signals indefinitely with no archival or deletion lifecycle. 

 **Benefits of establishing this best practice:** 
+  Lower compute consumption across fraud detection, because analysis intensity is matched to the risk each traffic segment carries rather than applied uniformly. 
+  Reduced data movement, since retrospective analysis runs where the data already resides instead of copying impression and click sets between systems. 
+  Detection effectiveness is preserved, because the latency-sensitive path keeps full coverage while only deferrable analysis is sampled or scheduled. 
+  Improved scalability under variable advertising traffic, as detection capacity tracks demand instead of being provisioned for peak. 

 **Level of risk exposed if this best practice is not established:** Low 

## Implementation guidance
<a name="implementation-guidance"></a>

 Fraud detection in video streaming advertising is a continuous, high-volume workload where every impression, click, and conversion is a candidate for analysis. Treating all of this traffic identically leads to over-provisioned, always-on compute and large volumes of data movement, which raises the carbon impact of the workload without necessarily improving detection outcomes. Match the intensity and placement of detection to the actual risk it addresses. 

 Distinguish the near-real-time detection that blocks fraudulent activity from the retrospective pattern analysis that tolerates scheduling flexibility. Run latency-sensitive paths on energy-efficient, right-sized compute. Schedule batch analysis for lower-carbon time windows and Regions. 

 Detection logic rarely needs to inspect every event at full fidelity, and the data it does need isn't necessarily close to where the analysis runs. Data location matters most when analysis spans multiple advertising partners. Copying large impression and click data sets between parties is both costly and carbon-intensive. Favor patterns that analyze data where it already resides. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Use energy-efficient compute for ongoing monitoring:** For the persistent portion of fraud monitoring that runs on compute instances, select AWS Graviton-based instances to reduce energy consumption per unit of work. 

1.  **Apply intelligent sampling:** Where it meets your business and risk requirements, sample events for fraud detection instead of analyzing every event at full fidelity, reducing computational overhead. 

1.  **Schedule intensive analysis for low-carbon periods:** Run intensive, non-time-critical fraud pattern analysis as time-shiftable batch work rather than continuously, and prefer lower-carbon AWS Regions. To target genuinely lower-carbon periods, drive scheduling from a carbon-intensity data source (a third-party grid carbon-intensity API or published Region-level carbon data), since AWS doesn't expose a built-in real-time grid carbon-intensity signal. 

1.  **Use serverless for variable workloads:** Run variable or bursty detection workloads on serverless architectures such as AWS Lambda so capacity scales to demand instead of remaining provisioned at peak. 

1.  **Apply efficient storage patterns to fraud data:** Store fraud signals and patterns efficiently, archive data that isn't readily needed, and remove data that is no longer required for compliance or security purposes. 

1.  **Analyze partner data in place:** Use AWS Clean Rooms for measurement analysis across advertising partners so data sets can be analyzed where they reside, with no data movement. 

1.  **Cache frequently accessed detection rules:** Cache frequently accessed fraud detection rules to avoid repeated recomputation and data retrieval. 

1.  **Minimize cross-Region data transfer:** Configure Regional detection systems to process data close to its source and minimize cross-Region data transfer. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVSUS05-BP03 Optimize content moderation systems for sustainable operation](advsus05-bp03.md) 
+  [ADVSUS05-BP01 Optimize privacy workload processing patterns and resource allocation for sustainability](advsus05-bp01.md) 

 **Related documents:** 
+  [Hardware and services](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/hardware-and-services.html) 

 **Related services:** 
+  [Amazon EC2 with AWS Graviton processors](https://aws.amazon.com/ec2/graviton/) 
+  [AWS Lambda](https://aws.amazon.com/lambda/) 
+  [Amazon ElastiCache](https://aws.amazon.com/elasticache/) 
+  [AWS Clean Rooms](https://aws.amazon.com/clean-rooms/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 