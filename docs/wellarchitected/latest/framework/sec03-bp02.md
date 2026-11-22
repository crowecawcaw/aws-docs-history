

# SEC03-BP02 Use scalable and centralized permissions management in your workload

 When you have a workload with rich authorization needs, you must decide who can access and modify resources, often under changing conditions. When that logic lives inside application code or a custom database table, it drifts out of sync across components and becomes hard to audit or change. Manage permissions through a centralized, policy-based authorization service instead, so decisions stay consistent and reviewable as the workload grows. 

 **Desired outcome:** 
+  Your workload evaluates authorization through a centralized service rather than logic scattered across components. 
+  Your permission decisions are consistent for the same principal and action regardless of which component handles the request. 
+  Your authorization policies are versioned and auditable, so you can see what changed, when, and by whom. 
+  Your authorization model expresses access as roles, attributes, or policies that scale without per-user maintenance. 

 **Common anti-patterns:** 
+  Teams build custom authorization logic instead of using a managed service. 
+  Permission rules are hard-coded in application code or stored in a database table. 
+  Each component manages its own permissions, so the same principal is evaluated differently in different places. 
+  Different parts of the workload use different authentication and authorization mechanisms. 
+  Authentication and authorization logic are entangled, with no clear separation between them. 
+  Access relies only on coarse-grained rules and ignores role-based, attribute-based, or policy-based control. 

 **Benefits of establishing this best practice:** 
+  Consistent access decisions across components reduce the risk of a gap that grants unintended access. 
+  A single policy store gives you one place to audit and change permissions. 
+  Externalizing authorization from code lets you adjust access without redeploying the workload. 
+  Policy-based models scale to new features and tenants without rewriting permission logic. 
+  Separating authentication from authorization makes each easier to reason about and test. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Authorization becomes expensive when it exists in application code. Each service ends up with its own copy of the rules, the copies diverge over time, and no single place fully explains your access patterns. Auditing a permission means reading source across every component, and changing a rule means a code change and a deployment. Centralize authorization by treating permissions as data that a dedicated service evaluates, so every component queries the same authority. 

 Not every workload needs this. Coarse-grained access, where a role either can or cannot reach a whole service, is simpler and often enough for internal tools with stable requirements. The investment pays off when access is dynamic, such as for delegated permissions, temporary sharing, per-tenant isolation, or conditions that depend on request context. Those cases are where scattered logic fails, because rules change faster than code review can keep up. Match the mechanism to the requirement rather than defaulting to the most powerful model. 

 Before choosing a service, define an *authorization model*: the set of principals, the actions they perform, the resources they act on, and the conditions that qualify access. Identify the roles and attributes that recur across those rules, because they determine which access-control style fits. *Role-based access control* groups permissions by job function and works well when access maps cleanly to a manageable set of roles. *Attribute-based access control* derives access from attributes on the principal and resource, which scales as those populations grow without adding new roles. *Policy-based access control* expresses rules as explicit policies evaluated at request time, which suits fine-grained decisions over your application's own resources. Many workloads combine them. 

 Authentication establishes who the caller is, while authorization decides what actions they can take. Keep them separate, where a centralized identity source performs authentication and a policy service performs authorization. Each concern stays testable on its own. 

 On AWS, [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html) manages user identities and supports [role-based](https://docs.aws.amazon.com/cognito/latest/developerguide/role-based-access-control.html) and [attribute-based](https://docs.aws.amazon.com/cognito/latest/developerguide/attributes-for-access-control.html) access control when a workload acts on AWS resources for a user. For fine-grained decisions over your application's own resources, [Amazon Verified Permissions](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/what-is-avp.html) is a policy-based service that returns an allow-or-deny decision from a runtime query and keeps policies in one auditable store. Reevaluate the model periodically, because access requirements change as the workload adds features and tenants. 

 When your workload provides workforce access to data through AWS analytics services rather than serving external end users, centralize those permissions against the corporate identity, not a shared service role. [Trusted identity propagation](https://docs.aws.amazon.com/singlesignon/latest/userguide/trustedidentitypropagation-overview.html) in IAM Identity Center carries the signed-in user's identity through services such as Amazon Redshift, AWS Quick, Amazon Athena, and Amazon EMR. Define fine-grained permissions once in [AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html) or [Amazon S3 Access Grants](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants.html), and each service authorizes and audits access against the user or their group. See [SEC02-BP04 Rely on a centralized identity provider for users and machines](sec02-bp04.md) for the identity-provider side of this pattern. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define your authorization model:** Enumerate the principals, actions, resources, conditions, roles, and attributes that govern access in your workload. Write the access rules in plain terms first, then translate them into policies or technical guidelines. This model drives every later decision, so keep it explicit rather than implied by code. 

1.  **Choose an authorization strategy:** Match the model to a mechanism. Use [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html) user pools for user management and authentication, and use [Amazon Verified Permissions](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/what-is-avp.html) for fine-grained, policy-based authorization over application resources. 

1.  **Centralize user and identity management:** Manage principals through one unified service across all components, so user attributes and entitlements have a single source of truth. This prevents the same principal from resolving to different permissions in different parts of the workload. 

1.  **Define authorization policies centrally:** Express access as roles, attributes, or policies, and store them in [Amazon Verified Permissions](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/policies.html). Use attribute-based rules to scale permissions from principal and resource attributes rather than enumerating access per user. 

1.  **Add enforcement points to your components:** Place authorization checks where components handle requests. For access to AWS resources, use [Amazon Cognito identity pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity.html) to obtain temporary AWS credentials for authenticated users. For application resources, call the [Verified Permissions authorization API](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/authorization-sdk.html) to evaluate each decision and enforce the result in your code. 

1.  **Monitor authorization decisions:** Track allow and deny outcomes with [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) and log decisions to maintain an audit trail. Use these signals to spot misconfigured policies and to troubleshoot access issues without loosening rules blindly. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC03-BP01 Grant least privilege access in workload components](sec03-bp01.md) 
+  [SEC02-BP01 Identify principals and identity use-cases](sec02-bp01.md) 
+  [SEC02-BP04 Rely on a centralized identity provider for users and machines](sec02-bp04.md) 

 **Related documents:** 
+  [Amazon Cognito - using attributes for access control](https://docs.aws.amazon.com/cognito/latest/developerguide/attributes-for-access-control.html) 
+  [Amazon Cognito - using role-based access control](https://docs.aws.amazon.com/cognito/latest/developerguide/role-based-access-control.html) 

 **Related examples:** 
+  [Policy-based access control in application development with Amazon Verified Permissions](https://aws.amazon.com/blogs/devops/policy-based-access-control-in-application-development-with-amazon-verified-permissions/) 
+  [Manage roles and entitlements with PBAC using Amazon Verified Permissions](https://aws.amazon.com/blogs/devops/manage-roles-and-entitlements-with-pbac-using-amazon-verified-permissions/) 
+  [Simplify fine-grained authorization with Amazon Verified Permissions and Amazon Cognito](https://aws.amazon.com/blogs/security/simplify-fine-grained-authorization-with-amazon-verified-permissions-and-amazon-cognito/) 

 **Related tools:** 
+  [IAM policy simulator](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_testing-policies.html) 
+  [IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) 