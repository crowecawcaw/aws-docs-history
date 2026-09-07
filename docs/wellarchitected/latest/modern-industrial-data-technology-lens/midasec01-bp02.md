

# MIDASEC01-BP02 Standardize security baseline and implement role-based access controls
<a name="midasec01-bp02"></a>

 Establish a standardized security configuration across accounts and workloads using AWS Organizations, AWS IAM, and control policies. Implement role-based access controls (RBAC) to limit access based on job function and responsibility, especially across IT and OT environments. 

 **Desired outcome: **Establish consistent security controls across industrial cloud workloads that help protect both IT systems (MES, ERP) and OT systems (PLCs, SCADA), reducing exposure to unauthorized access and privilege escalation that could impact manufacturing operations. 

 **Benefits of establishing this best practice: **Enables centralized governance across IT and OT environments, improves auditability of manufacturing system access, and minimizes risk of misconfigurations through role-based controls aligned with production requirements. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation steps
<a name="implementation-steps-6"></a>
+  Define roles and responsibilities across IT and OT personas (for example, automation engineers, data scientists, or vendors). 
+  Create and assign IAM roles and policies aligned to job responsibilities. 
+  Use AWS IAM Identity Center for central identity management and federated access. 
+  Apply SCPs to enforce service-level restrictions at the organizational unit (OU) level. 

## Resources
<a name="resources-6"></a>

 **Related documents:** 
+  [ Service control policies (SCPs) ](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) 
+  [ Policies and permissions in IAM ](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) 
+  [AWS Identity and Access Management](https://aws.amazon.com/iam/) 