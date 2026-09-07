

# MIDASEC01-BP05 Implement incident response playbooks
<a name="midasec01-bp05"></a>

 Develop and test incident response playbooks for common OT/IT scenarios such as device compromise, unauthorized access, and data exfiltration. Verify your cross-functional coordination and readiness to minimize downtime and safety risks. 

 **Desired outcome:** Manufacturing organizations respond to incidents swiftly with predefined procedures, minimizing production disruption. 

 **Benefits of establishing this best practice:** Improves MTTD and MTTR, reduces risk of safety events, and improves regulatory and audit outcomes. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance-8"></a>

 Use AWS Systems Manager, AWS Lambda, and Amazon EventBridge to automate containment and response. Simulate scenarios to validate readiness. 

### Implementation steps
<a name="implementation-steps-9"></a>
+  Identify critical incident types and build corresponding playbooks. 
+  Use AWS Systems Manager Automation to orchestrate predefined remediation. 
+  Run chaos experiments using AWS Fault Injection Service to test response efficacy. 
+  Train IT and OT teams on roles and escalation procedures. 

## Resources
<a name="resources-9"></a>

 **Related documents:** 
+  [AWS Systems Manager Automation ](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) 
+  [AWS Fault Injection Service](https://aws.amazon.com/fis/) 
+  [AWS Resilience Hub](https://aws.amazon.com/resilience-hub/) 