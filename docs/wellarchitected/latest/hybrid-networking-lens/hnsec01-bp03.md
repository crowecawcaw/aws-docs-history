

# HNSEC01-BP03 Implement continuous logging
<a name="hnsec01-bp03"></a>

 Continuous logging provides real-time visibility across on-premises and cloud infrastructures. Implementing comprehensive logging mechanisms enables teams to quickly detect anomalies, troubleshoot connectivity issues, and maintain a consistent audit trail for security compliance. 

 **Desired outcome:** Achieve continuous visibility, reduce mean time to resolution during incidents, and automated enforcement of compliance configurations. 

 **Benefits of establishing this best practice:** 
+  Enables prompt incident detection and response 
+  Provides clear audit trails for compliance 
+  Ensures ongoing alignment with regulatory standards 
+  Reduces manual compliance effort 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance-9"></a>
+  Capture cloud environment API activities using services such as AWS CloudTrail. 
+  Enable flow logs for network visibility using services such as VPC Flow Logs and Transit Gateway Flow Logs. 

## Resources
<a name="resources-8"></a>
+  [AWS services for logging and monitoring](https://docs.aws.amazon.com/prescriptive-guidance/latest/logging-monitoring-for-application-owners/aws-services-logging-monitoring.html) 
+  [AWS Transit Gateway Flow Logs](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-flow-logs.html) 
+  [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) 
+  [Logging IP traffic using VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) 