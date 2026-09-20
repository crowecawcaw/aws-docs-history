

# DSSEC05-BP01 Control operator access to infrastructure from approved locations
<a name="dssec05-bp01"></a>

 For sovereign workloads, what matters isn't just who operates the infrastructure, but also where they connect from and how long their access lasts. Persistent privileges and manual operations each widen the window in which an operator can act beyond their authority. Controlling the location, duration, and necessity of operator access keeps infrastructure administration within sovereign boundaries and leaves an audit trail for each session. 

 **Desired outcome:** 
+  Operators access infrastructure resources only from verified locations within approved jurisdictions, using temporary elevated privileges that are automatically revoked. 
+  Routine operations are automated, reducing the need for interactive access. 

 **Common anti-patterns:** 
+  Granting persistent elevated privileges instead of just-in-time access for support roles. 
+  Allowing direct SSH/RDP access from the internet without session management or audit trails. 
+  Relying solely on IP-based restrictions without identity verification or location validation. 
+  Performing routine operations manually when they could be automated through runbooks. 

 **Benefits of establishing this best practice:** 
+  Reduce risk of unauthorized access by verifying operator location and enforcing temporary privileges. 
+  Improve auditability with session-level logging of operator activities. 
+  Reduce human error and security exposure by automating routine operations. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Focus on controlling *how and from where* operators interact with infrastructure. For data access controls (data perimeters, IAM condition keys, network controls, encryption), see [DSSEC02-BP01 Protect data through layered access controls within sovereign boundaries](dssec02-bp01.html). 

 **Digital sovereignty considerations:** 
+  Verify that access originates from within approved jurisdictions using secure connectivity such as [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) that terminates within sovereign boundaries. 
+  Combine location-based and identity-based controls using [Zero Trust Architecture](https://aws.amazon.com/security/zero-trust/) principles aligned to data residency requirements. 
+  Maintain audit trails that demonstrate adherence to local regulations. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Enforce just-in-time elevated access**: Grant temporary elevated privileges only when needed, and revoke them automatically after a defined period. Use [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) with [temporary elevated access](https://docs.aws.amazon.com/singlesignon/latest/userguide/temporary-elevated-access.html) to implement approval workflows. Require [multi-factor authentication (MFA)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html) for elevated privilege requests. 

1.  **Use session-managed access instead of direct connectivity**: Use [AWS Systems Manager Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html) for browser-based access to instances without opening inbound ports. Session Manager provides full audit trails with session logging. 

1.  **Automate routine operations to reduce interactive access**: Use [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) runbooks for routine tasks such as patching, backups, and credential rotation. Implement automated approval workflows using [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) for operations that require human approval. Use [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html) for automated fleet patching. 

1.  **Implement security gates in deployment pipelines**: Scan infrastructure as code (IaC) templates with [CloudFormation Guard](https://docs.aws.amazon.com/cfn-guard/latest/ug/what-is-guard.html) before deployment. Include [manual approval stages](https://docs.aws.amazon.com/codepipeline/latest/userguide/approvals.html) in [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) for production deployments. 

1.  **Remove technical means of accessing data:** Operators should not ordinarily have access to data. Refer to [Isolate data from your own operators](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/isolate-data-operators.html). 

1.  **Evaluate serverless offerings:** One of the most effective ways to minimize operator access to your workloads is to eliminate the infrastructure that operators need to access in the first place. Serverless compute services like AWS Lambda and AWS Fargate run code and containers without exposing any host operating system. There are no EC2 instances to SSH into, no operating systems to patch, and no interactive sessions to manage. Similarly, serverless databases like Amazon DynamoDB and Amazon Aurora Serverless remove the need to provision, manage, or access database servers. 

1.  **Control operator access points**: No single control can prove an operator's physical location. IAM condition keys such as aws:SourceIp restrict by IP address range, not by geography: an operator could use a VPN endpoint within an approved IP range while physically located in a foreign jurisdiction. Similarly, aws:SourceVpc proves the network path originates from a specific VPC, but not that the operator is physically within the approved jurisdiction. To strengthen location verification, consider layering multiple controls. Examples include: 
   +  **Network path:** Consider using [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) to provide connectivity from authorized physical locations, verifying that associated infrastructure is in the appropriate geographic region. AWS Direct Connect terminates at a known physical location, providing a known network termination point within a specific geography. However, corporate WANs can still allow traffic from other locations (backhauling), so Direct Connect alone doesn't prove operator location. 
   +  **Identity context:** Configure your identity provider (IdP) to enforce location-based authentication policies, such as device posture checks and network location validation, before issuing tokens to IAM Identity Center. Several leading IdP providers offer IP-based and GPS-based location awareness. However, accuracy varies by the geographic context (for example country compared to city awareness). 
   +  **Network origin:** Apply aws:SourceVpc or aws:SourceVpce condition keys in IAM policies as an additional layer to restrict the network origin of API requests. 
   +  **Time-bound sessions:** Require MFA and enforce short session durations to limit the window of exposure. 
   +  **Independent third-party certifications and attestations:** Require independent third-party certifications and attestations. For example, for demonstrating physical security guardrails and monitoring at colocation facilities. 
   +  **Contractual obligations:** Supplement technical controls with contractual obligations. These obligations may apply to your own employees and to operators provided by a third-party service provider (for example, Security Operations Center (SOC) as Service providers). 

    Layering these controls provides stronger location assurance but relies on physical and organizational controls (facility access, network topology, employment contracts) in addition to technical controls. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC02-BP02 Use temporary credentials](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_identities_unique.html) 
+  [SEC03-BP02 Grant least privilege access](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_least_privileges.html) 
+  [SEC03-BP03 Establish emergency access process](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_emergency_process.html) 
+  [SEC05-BP01 Create network layers](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_network_protection_create_layers.html) 
+  [SEC06-BP01 Perform vulnerability management](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_compute_vulnerability_management.html) 
+  [SEC06-BP03 Reduce manual management and interactive access](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_compute_reduce_manual_management.html) 
+  [DSSEC04-BP03 Establish comprehensive logging and monitoring of operator actions](dssec04-bp03.html) 

 **Related documents:** 
+  [AWS Systems Manager Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html) 
+  [Zero Trust on AWS](https://aws.amazon.com/security/zero-trust/) 

 **Related videos:** 
+  [AWS re:Inforce 2025 - Integrate Zero Trust into your cloud network (NIS304)](https://www.youtube.com/watch?v=AMSkou99Fus) 
+  [AWS re:Invent 2025 - Innovations in Infrastructure Protection to strengthen your network (SEC310)](https://www.youtube.com/watch?v=qt9kaqiOYbQ) 

 **Related examples:** 
+  [AWS Well-Architected Labs - Security](https://wellarchitectedlabs.com/security/) 
+  [AWS VPC Connectivity Options](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/introduction.html) 

 **Related services:** 
+  [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/) 
+  [AWS Systems Manager](https://aws.amazon.com/systems-manager/) 
+  [AWS Direct Connect](https://aws.amazon.com/directconnect/) 
+  [AWS CodePipeline](https://aws.amazon.com/codepipeline/) 
+  [AWS Step Functions](https://aws.amazon.com/step-functions/) 