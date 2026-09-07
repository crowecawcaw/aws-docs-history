

# HNREL05-BP01 Failover testing of dedicated connections
<a name="hnrel05-bp01"></a>

 Regular failover testing of dedicated connections is essential for ensuring the resilience and reliability of hybrid network environments. Simulating various scenarios by temporarily disabling BGP peering sessions between on-premises networks and cloud. By regularly exercising these tests, organizations can validate their recovery procedures, uncover latent bugs, and ensure their hybrid network architecture performs as expected during failover scenarios. 

 **Desired outcome:** Verify that failover and recovery procedures for Direct Connect connections work as intended, minimizing downtime during real incidents. 

 **Level of risk exposed if this best practice is not established:** High 

 **Benefits of establishing this best practice:** 
+  Uncovers misconfigurations or gaps in failover processes 
+  Increases confidence in your recovery plans 
+  Enables you to proactively address weaknesses before actual failures 
+  Reduces business impact of network outages 

## Implementation guidance
<a name="implementation-guidance-37"></a>
+  Simulated BGP failures of dedicated connections and observe failover behavior, using services such as the AWS Direct Connect Resiliency Toolkit. 
+  Test all redundant dedicated connections and VPN links to ensure expected failover behavior. 
+  Document and refine your recovery steps based on test outcomes. 
+  Repeat testing regularly and after significant changes. 

## Resources
<a name="resources-29"></a>
+  [AWS Direct Connect Resiliency Toolkit](https://docs.aws.amazon.com/directconnect/latest/UserGuide/resiliency_toolkit.html) 