

# SEC03-BP01 Grant least privilege access in workload components

 Every component in a workload runs with some set of permissions. When those permissions exceed what a component needs, each component becomes a wider path for an unauthorized user to move through. Grant each component only the permissions its function requires, and remove access as functions change. This limits the impact of any single component under unauthorized control to what that component could already do. 

 **Desired outcome:** 
+  Each of your workload components or services runs under a distinct identity scoped to the permissions its function requires. 
+  Your components use temporary credentials instead of long-lived keys wherever the service supports them. 
+  You detect unused permissions and permission drift automatically, and you refine access on a defined cadence. 
+  You keep permission ownership clear, with your application and infrastructure teams agreeing on who requests, approves, and revokes access. 

 **Common anti-patterns:** 
+  Teams share a single service account or role across multiple components, which breaks separation of concerns. 
+  Components carry administrative access that lets them modify their own permission sets. 
+  Services deploy with broad permissions rather than function-specific access. 
+  Teams leave permissions in place after the features or integrations that needed them are removed. 
+  Manual permission assignment cannot keep pace as the number of components grows. 
+  Development environments run with the same permissions granted to production. 

 **Benefits of establishing this best practice:** 
+  A component under unauthorized control exposes only the narrow set of actions it was granted, which limits blast radius. 
+  Automated analysis of granted compared to used permissions makes over-provisioning visible. 
+  Function-scoped identities produce clearer audit trails, because each action traces to a specific component. 
+  Defining permissions as code lets you review and version access changes alongside application changes. 
+  Removing unused access on a cadence keeps permissions aligned with current function. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Least privilege at the component level treats permissions as an attack surface. A web service that only reads one database table and writes logs does not need broad database or logging access. If an unauthorized user gains control of that service, they inherit exactly what you granted it. Scoping permissions to the component's function turns a potential full-account incident into a contained one. 

 The process of determining the minimum set of permissions is the hard part. A more reliable approach is to derive permissions from observed activity: run the component, capture which actions it calls, and generate a policy from that record. Even then, permissions can decay as features are removed and integrations are deprecated, and the grants that supported those features and integrations stay behind as *permission drift*. Without continuous analysis, the gap between granted and used permissions widens. 

 Treat least privilege as continuous work across your environments, because cleaning up access already granted does not stop the next code change from reintroducing broad permissions. Tighten access as code promotes toward production. In sandbox and development environments, reduce the friction of manually writing policies with [IAM Policy Autopilot](https://aws.amazon.com/blogs/security/iam-policy-autopilot-an-open-source-tool-that-brings-iam-policy-expertise-to-builders-and-ai-coding-assistants/). This open-source tool runs as a command-line tool or a Model Context Protocol (MCP) server for AI coding assistants, and it analyzes your application code to generate a baseline identity-based policy from the AWS SDK calls it finds. These baseline policies favor working functionality over minimal permissions, so refine them before use. As the change promotes to higher environments such as test, QA, and production, gate each promotion with automated policy analysis. Use [IAM Access Analyzer unused access findings](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-findings.html) to strip permissions the component never exercised, and use the [IAM Access Analyzer custom policy check](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-custom-policy-checks.html) CheckNoNewAccess as a pipeline gate so a merge cannot silently widen access without review. Add preventive checks to the environments that need them: CheckNoPublicAccess confirms a resource-based policy does not expose a resource publicly, and CheckAccessNotGranted fails the pipeline if a policy grants specific sensitive actions, such as write access to a regulated database or a bucket of sensitive records. 

 Give each component its own identity. Shared roles blur audit trails and force the permission set to be the union of every consumer's needs. Where the runtime supports it, attach a role to the compute itself and use temporary credentials that rotate automatically, so no long-lived key exists that could be exposed. For service-to-service access, resource-based policies let the target resource state which principals it trusts, complementing the identity-based policies attached to the caller. 

 Ownership determines whether least privilege holds over time. Infrastructure teams typically set the outer boundary with organization-wide controls and permission boundaries, and application teams define the specific grants within that boundary. When neither side clearly owns refinement, permissions accumulate. Agree early on who requests, approves, and revokes access, and treat that process as part of the workload's operating model. Guardrails such as service control policies and permission boundaries limit what can be granted, but they do not replace scoping each component. 

 [IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) [generates policies from access activity](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation.html) recorded in [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html), so policies reflect real usage. Its [unused access analysis](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-findings.html) flags roles, keys, and permissions that have gone idle. Defining roles and policies through [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) or the [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/home.html) puts every permission change under review and version control. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Map the permissions each component needs:** Document the function of each component and the specific actions and resources it requires. Analyze [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) to see which actions each component actually calls, and use [IAM Access Analyzer policy generation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation.html) to derive a policy from that activity. Confirm the result stays within the [service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) your infrastructure team defines. 

1.  **Generate baseline policies in development without slowing developers:** In sandbox and development environments, use [IAM Policy Autopilot](https://github.com/awslabs/iam-policy-autopilot) to generate a baseline identity-based policy from the AWS SDK calls in your application code, either through its CLI or its MCP server integration with an AI coding assistant. This removes the friction that pushes teams toward over-granting when they write policies manually. Because these policies favor working functionality over minimal permissions, and do not cover resource-based policies, treat the output as a reviewed starting point rather than a final grant, and refine it in the steps below. 

1.  **Assign a distinct identity with temporary credentials to each component:** Attach a scoped [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) to each component rather than sharing one. For containers, use [task roles in Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html) or [IAM roles for service accounts in Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html). For instances, use [Amazon EC2 instance profiles](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html). Store any unavoidable secrets in [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) with [automatic rotation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html) enabled. 

1.  **Set boundaries between components:** Control service-to-service access with [resource-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html) that name the principals each resource trusts. Apply [permissions boundaries](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) so a team can create roles without granting more than the boundary allows. Confirm cross-account paths with your security team before enabling them. 

1.  **Monitor permission use and errors:** Track access-denied errors and service interactions with [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html), and use [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html) to trace permission failures across components in distributed workloads. Set alerting thresholds with your infrastructure team so denied calls surface as signals for refinement rather than noise. 

1.  **Gate least privilege through your promotion pipeline:** Define roles and policies as code with [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) or the [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/home.html) so every permission change is reviewed and versioned. As a change promotes toward production, tighten access at each stage rather than only after deployment. Enable [IAM Access Analyzer unused access analysis](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-findings.html) to identify permissions the component has not exercised, and remove them before promoting to the next environment. Add [IAM Access Analyzer custom policy checks](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-custom-policy-checks.html) to the pipeline as gates: CheckNoNewAccess blocks a change that would widen access beyond the current policy without explicit review, CheckNoPublicAccess confirms a resource-based policy does not expose a resource publicly, and CheckAccessNotGranted fails the build when a policy grants sensitive actions you have designated off-limits, such as write access to a regulated data store. Validate changes with the [IAM policy simulator](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_testing-policies.html) before deployment, and continue to review unused access on a recurring cadence in production. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC03-BP02 Use scalable and centralized permissions management in your workload](sec03-bp02.md) 
+  [SEC03-BP03 Analyze public and cross-account access](sec03-bp03.md) 
+  [SEC02-BP01 Identify principals and identity use-cases](sec02-bp01.md) 
+  [SEC02-BP02 Use temporary credentials](sec02-bp02.md) 
+  [SEC02-BP05 Audit and rotate credentials periodically](sec02-bp05.md) 

 **Related documents:** 
+  [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) 
+  [Apply least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) 
+  [Amazon ECS container instance IAM role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/instance_IAM_role.html) 
+  [AWS Lambda execution role](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html) 
+  [Identity-based policies and resource-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html) 
+  [Validate policies with IAM Access Analyzer custom policy checks](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-custom-policy-checks.html) 

 **Related examples:** 
+  [IAM Policy Autopilot: an open-source tool that brings IAM policy expertise to builders and AI coding assistants](https://aws.amazon.com/blogs/security/iam-policy-autopilot-an-open-source-tool-that-brings-iam-policy-expertise-to-builders-and-ai-coding-assistants/) 

 **Related tools:** 
+  [IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) 
+  [IAM policy simulator](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_testing-policies.html) 
+  [IAM Policy Autopilot (GitHub)](https://github.com/awslabs/iam-policy-autopilot) 