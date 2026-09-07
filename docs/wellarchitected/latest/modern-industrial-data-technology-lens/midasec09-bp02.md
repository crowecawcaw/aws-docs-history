

# MIDASEC09-BP02 Perform regular vulnerability scans and penetration tests
<a name="midasec09-bp02"></a>

 Identify and mitigate vulnerabilities in applications and environments by conducting recurring scans and authorized penetration testing. 

 **Desired outcome:** Exposed vulnerabilities are proactively identified and mitigated before exploitation. 

 **Benefits of establishing this best practice:** Enhances visibility into system weaknesses and builds resilience against external and internal threats. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance-31"></a>

 Use Amazon Inspector and integrate third-party scanning tools for deep and layered assessments. 

### Implementation steps
<a name="implementation-steps-32"></a>
+  Schedule recurring scans using Amazon Inspector across EC2 and container workloads. 
+  Perform black-box and white-box pen tests with third-party experts. 
+  Integrate findings with AWS Security Hub CSPM for centralized visibility. 
+  Remediate critical vulnerabilities through prioritized CI/CD updates. 

## Resources
<a name="resources-32"></a>
+  [ Getting started with Amazon Inspector ](https://docs.aws.amazon.com/inspector/latest/user/getting-started.html) 
+  [ Penetration Testing ](https://aws.amazon.com/security/penetration-testing/) 