

# TELCOREL04-BP01 Implement bypass mode on peripheral network devices such as firewalls and network probes while connecting to the cloud
<a name="telcorel04-bp01"></a>

 Implementing bypass mode on network peripheral devices like firewalls and network probes is crucial for maintaining service continuity during device failures or power outages. This mechanism automatically creates a direct connection between incoming and outgoing network ports when a device fails, so critical network traffic continues to flow without interruption. By deploying bypass-capable devices while connecting to the cloud-based network infrastructure, telecom operators can reduce service disruptions that could occur during device failures, maintenance windows, or unexpected outages. This approach is particularly important for maintaining high availability in telecommunications networks where continuous service is essential for customer satisfaction and regulatory adherence. 

 **Desired outcome:** 
+  Verify continuous network traffic flow during device-level failures. 
+  Minimize service disruptions during maintenance or unexpected outages. 
+  Maintain high availability for critical network services. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Design your network architecture to include redundant paths and automated routing updates that can quickly respond to device failures. Implement comprehensive health monitoring and automated recovery procedures to minimize service disruptions. Establish clear operational procedures for managing bypass events, including notification workflows and post-event analysis to reduce recurring issues. 

 Regular testing of the bypass functionality is crucial to verify it will work as expected during actual failures. This includes conducting controlled failure scenarios during maintenance windows and validating that traffic continues to flow without interruption. Document bypass events and maintain historical data to identify patterns and potential improvements to the bypass implementation. 

### Implementation steps
<a name="implementation-steps"></a>
+  Default to fail-closed. Plan availability through AWS Network Firewall endpoint redundancy across multiple Availability Zones so an impaired engine in one AZ does not require bypassing inspection. 
+  Reserve fail-open for signaling planes (5G SBI, N2, SIP, Diameter) where packet loss during a firewall-engine outage causes call drops or session failures. Fail-open passes traffic uninspected while the engine is unavailable, so scope it explicitly to the signaling-firewall tier and document which interfaces are in scope. 
+  Where fail-open is justified, set the AWS Network Firewall StreamExceptionPolicy to CONTINUE on the stateful rule groups so flows resume inspection once the engine recovers, and keep a compensating inspection layer downstream of the fail-open tier (a stateless rule group, a Network Firewall endpoint in a downstream VPC, or an application-layer control) so the uninspected window is bounded by at least one other control. 
+  Configure Amazon CloudWatch alarms on the StreamExceptionPolicy state and on stateful-engine health metrics so every fail-open window is observed, timeboxed, and reviewed, with alerts integrated into operational incident response. 
+  Configure AWS Transit Gateway for centralized network management with automatic routing failover capabilities. 
+  Use Amazon CloudWatch to monitor the broader firewall and routing deployment for health and performance regressions on the AWS services involved. 

## Resources
<a name="resources"></a>

 **Key AWS services:** 

 [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/) 

 [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 