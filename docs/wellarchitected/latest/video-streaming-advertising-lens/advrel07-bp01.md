

# ADVREL07-BP01 Design resilient architectures with privacy-preserving fault tolerance

 Deploy privacy-enhancing data collaboration environments across multiple regions with replicated privacy policies, differential privacy budgets, and encrypted collaboration configurations so that privacy-protected analytics continue during regional outages. 

 **Desired outcome:** 
+  Privacy-enhanced collaboration environments remain available during regional failures with privacy controls intact. 
+  Failover procedures preserve privacy policies, differential privacy budgets, and cryptographic configurations. 
+  Circuit breakers fail-closed when privacy controls can't be verified, so that collaboration halts rather than proceeding without privacy protection. 

 **Common anti-patterns:** 
+  Circuit breakers that fail open, which lets collaboration proceed without verified privacy controls. 
+  Single-region AWS Clean Rooms setup with no cross-region KMS key access, so a regional outage halts privacy-protected analytics. 
+  No monitoring of differential privacy budget, so budget exhaustion halts queries without warning. 
+  Failover procedures that restore compute but not the privacy policies, budgets, and cryptographic configuration. 

 **Benefits of establishing this best practice:** 
+  Privacy-enhanced collaboration stays available during regional failures with privacy controls intact. 
+  Fail-closed circuit breakers guarantee collaboration halts rather than proceeding without privacy protection. 
+  Budget monitoring alerts measurement teams before exhaustion disrupts queries. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Treat privacy state as unique, with its own failover considerations. For example, a Clean Rooms session keeps encryption contexts in memory, and Nitro Enclave attestation binds to the hardware that produced it. Neither of these survives a move to another Region, so recovery must rebuild these protections from durable configuration. 

 The differential privacy budget measures information extraction across queries, and consumption moves in one direction only. A failover can replay a query, and replaying spends the budget twice. Enclave memory hides the duplicate spend, so track the budget durably in DynamoDB. Then you can recognize and refuse the second execution. 

 Configure circuit breakers to fail closed when privacy controls can't be verified. A fail-closed circuit breaker halts collaboration until controls verify, at the cost of availability. A fail-open circuit breaker keeps queries flowing but risks exposing partner records or overspending the budget. One unverified exposure harms the partner relationship more than a measured outage. 

 The team that negotiated the collaboration agreement defines acceptable exposure. Measurement teams consume the budget and need visibility into how much remains. Assign both responsibilities in a runbook before an incident. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Deploy Clean Rooms collaborations with Multi-Region KMS key access:** Configure Clean Rooms with KMS Multi-Region keys so that collaboration encryption keys are available in both the primary and failover regions. Test key access from the failover region before any DR exercise. 

1.  **Implement circuit breakers with privacy-first fail-closed logic:** For all privacy-enhanced computation workflows, implement circuit breakers that halt operations when: differential privacy budget is exhausted, cryptographic attestation verification fails, or privacy policy enforcement can't be confirmed. These circuit breakers should fail closed (halt computation) rather than failing open (continue without privacy protections). 

1.  **Monitor differential privacy budget consumption:** Publish differential privacy budget consumption as a custom CloudWatch metric. Configure alarms at 75% and 95% budget consumption to alert measurement teams before budget exhaustion halts queries. Implement budget distribution policies that limit how much of the period's budget any single measurement workflow can consume. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVREL07-BP02 Maintain data consistency and availability across collaboration workflows](advrel07-bp02.md) 
+  [ADVREL04-BP02 Architect defensively against failures](advrel04-bp02.md) 

 **Related documents:** 
+  [AWS Clean Rooms documentation](https://docs.aws.amazon.com/clean-rooms/latest/userguide/what-is.html) 
+  [AWS Nitro Enclaves](https://docs.aws.amazon.com/enclaves/latest/user/nitro-enclave.html) 

 **Related services:** 
+  [AWS Clean Rooms](https://aws.amazon.com/clean-rooms/) 
+  [Amazon Route 53](https://aws.amazon.com/route53/) 