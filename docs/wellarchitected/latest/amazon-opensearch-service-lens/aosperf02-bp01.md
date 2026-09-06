

# AOSPERF02-BP01 Implement processor utilization monitoring
<a name="aosperf02-bp01"></a>

 Keep CPU usage under 75% to maintain efficient resource utilization and prevent potential performance issues. 

 **Level of risk exposed if this best practice is not established**: High 

 **Desired outcome**: CPU utilization is below 75% for efficient resource utilization and minimizing potential performance issues. 

 **Benefits of establishing this best practice:** 
+  **Prevent performance issues:** Keeping CPU utilization below 75% helps identify and address potential issues related to high CPU usage, minimizing the risk of indexing or query processing bottlenecks. 
+  **Maintain scalability:** By keeping CPU utilization within a safe threshold, you can prevent scalability issues and ensure that your OpenSearch Service domains can handle increased traffic or workloads without degradation. 

## Implementation guidance
<a name="implementation-guidance-32"></a>

 The performance and efficiency in your OpenSearch Service domain can be maintained by closely monitoring CPU utilization. This involves tracking CPU usage over the past 14 days and verifying that the average rate remains below 75 percent. By doing so, you can proactively identify and address potential issues related to high CPU utilization, such as indexing or query processing bottlenecks, before they affect your domain's performance or scalability. 

### Implementation steps
<a name="implementation-steps-17"></a>
+  Log in to the AWS Management Console. 
+  Navigate to the Amazon OpenSearch Service console. 
+  Select your OpenSearch Service domain name. 
+  Choose the **Cluster health** tab. 
+  Navigate to the Data nodes box. 
+  Choose the **CPU utilization** graph. 
+  Adjust time range to `2w` and Statistic to `Average`. 

 If you notice that your average CPU utilization exceeds 75% over a 14-day period, it's recommended to investigate further by checking for dedicated leader nodes and reviewing the best practices outlined in [AOSPERF01](https://docs.aws.amazon.com/wellarchitected/latest/amazon-opensearch-service-lens/architecture-selection.html). 

## Resources
<a name="resources-31"></a>
+  [Monitoring OpenSearch cluster metrics with Amazon CloudWatch](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-cloudwatchmetrics.html#managedomains-cloudwatchmetrics-cluster-metrics) 
+  [Choosing the number of shards](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/bp-sharding.html) 
+  [Sizing OpenSearch Service domains](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/sizing-domains.html) 