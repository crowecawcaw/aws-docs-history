

# ADVCOST06-BP01 Design fraud detection pipelines to minimize redundant processing and optimize inference costs
<a name="advcost06-bp01"></a>

 Design fraud detection workflows that avoid repeated evaluations by caching known outcomes, filtering threats as early as possible, and running only the necessary inference steps on cost-efficient compute resources. 

## Implementation guidance
<a name="imp-guidance-advcost06-bp01"></a>
+  Enable AWS Cost Anomaly Detection with thresholds for each adtech microservice. 
+  Use Spot Instances and Managed Spot Training for SageMaker AI training jobs to identify malicious ads. 
+  Cache fraud evaluation results (for example, known creatives, IPs, or device IDs) using DynamoDB or ElastiCache to avoid reprocessing identical inputs. 
+  Implement AWS WAF rules for basic bot detection at edge (lowest cost). 