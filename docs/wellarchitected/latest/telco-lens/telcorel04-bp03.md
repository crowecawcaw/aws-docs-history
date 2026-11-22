

# TELCOREL04-BP03 Provide infrastructure mechanisms that enable network functions to implement graceful degradation during dependent-service failures

 When billing, charging, or policy services fail, the network functions that depend on them must decide how to handle in-flight sessions. That decision is the CSP's and vendor's to make. The cloud infrastructure's job is to provide the detection, buffering, and recovery that make any chosen degradation strategy possible. 

 **Desired outcome:** 
+  The infrastructure provides health-check mechanisms that network functions can use to detect when dependent services are unavailable. 
+  Temporary state storage is available for network functions that need to buffer usage data during dependent-service outages. 
+  Recovery mechanisms process buffered data once dependent services are restored. 

 **Common anti-patterns:** 
+  Not providing sufficient temporary storage capacity for usage-data buffering during extended outages. 
+  Lacking health-check visibility into dependent-service availability, so functions can't detect an outage cleanly. 
+  Having no recovery orchestration, so buffered data isn't reconciled when the dependent service returns. 
+  Treating the degradation policy as an infrastructure choice rather than a CSP and vendor decision with regulatory weight. 

 **Benefits of establishing this best practice:** 
+  A clear responsibility boundary keeps the cloud providing detection, storage, and recovery while the CSP and vendor own the degradation policy. 
+  Network functions can maintain service during dependent-system outages regardless of which degradation strategy they implement. 
+  Buffered usage data is preserved and processed after recovery, which prevents revenue loss from the outage period. 
+  Health-check visibility lets functions react promptly and predictably to a dependent-service failure. 

 **Level of risk exposed if this best practice is not established:** Medium \#\# Implementation guidance Whether to bypass billing during an outage, queue charges for later, or reject new sessions is a business decision with regulatory weight. Some jurisdictions require emergency calls to proceed regardless of billing status. Some operators continue all services during a billing outage to protect customer experience, while others reject non-emergency sessions to limit revenue exposure. The cloud provider is the wrong party to make these decisions. The CSP and CNF vendor own the degradation policy, and the infrastructure provides the mechanisms that make any policy implementable. 

 Failure detection gives a network function a reliable signal that a dependent service is unavailable, so it can trigger its configured behavior. Temporary state storage lets a function buffer charging records or session state during an outage. Capacity must cover the peak transaction rate multiplied by the maximum expected outage duration, or the buffer overflows when it is needed. When the dependent service returns, recovery orchestration drains the buffer, applies it, and verifies consistency. 

 Monitor each function's degraded-mode state and buffered-data volume to gauge recovery effort and alert on prolonged degradation. Test the degradation and recovery path end to end by stopping a dependent service or injecting its failure, to confirm the mechanisms work. 

## Implementation steps
<a name="implementation-steps"></a>
+  Provide dependent-service health checks: deploy Amazon CloudWatch or Route 53 health-check endpoints for billing, charging, and policy services that network functions can poll to detect unavailability. 
+  Provision buffering sized for outages: provide Amazon ElastiCache or Amazon SQS storage sized as peak transaction rate multiplied by maximum outage window (and average record size) for functions to buffer usage data. 
+  Implement recovery orchestration: build AWS Step Functions workflows that drain buffered data, apply it to the restored service, and verify consistency when a dependent service recovers. 
+  Monitor degradation state: set Amazon CloudWatch alarms that notify operations when a function enters degraded mode, and track degradation duration and buffered-data volume. 
+  Test degradation and recovery end to end by stopping a dependent service or using AWS Fault Injection Service, confirming detection, buffering, and reconciliation all work. 

## Resources
<a name="resources"></a>

 **Key AWS services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Amazon ElastiCache](https://aws.amazon.com/elasticache/) 
+  [Amazon SQS](https://aws.amazon.com/sqs/) 
+  [AWS Step Functions](https://aws.amazon.com/step-functions/) 
+  [AWS Lambda](https://aws.amazon.com/lambda/) 