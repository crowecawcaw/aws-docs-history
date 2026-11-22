

# SEC03-BP05 Share resources securely with a third party

 A workload often depends on third-party tools that need access to your account, such as a monitoring or analytics service. Grant third parties least privilege access through temporary credentials, and work with the provider to keep the scope of impact small. 

 **Desired outcome:** 
+  You give third parties access through IAM roles and temporary credentials, not long-term access keys. 
+  Each of your third-party trust policies requires a unique external ID that only you or the provider controls after creation. 
+  You keep the permissions policy attached to the cross-account role under your control, scoped to least privilege. 
+  You can revoke third-party access quickly, and you audit its use on a regular cadence. 

 **Common anti-patterns:** 
+  A third-party trust policy uses the default form with no conditions. 
+  Teams hand a third party long-term IAM credentials and access keys. 
+  The same external ID is reused across customers or providers. 
+  No plan exists to revoke third-party access when the relationship or service changes. 

 **Benefits of establishing this best practice:** 
+  Temporary credentials remove the standing secret that a long-term key represents if it is exposed. 
+  A unique external ID in the trust policy defends against the confused deputy problem. 
+  Controlling the permissions policy reduces gradual increases in scope by the third party. 
+  Defining the role through a template reduces manual policy errors and leaves an auditable trail. 
+  A revocation plan lets you cut access fast when access patterns or the relationship change. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Third parties operate outside your control and you cannot audit their systems, so the grant itself must carry the safeguards. Use a cross-account IAM role scoped to what the third party needs, assumed with temporary credentials. Do not issue long-term access keys because they persist, propagate through the provider's systems, and give you no visibility into where they end up. 

 An external ID closes a specific gap in cross-account roles known as the *[confused deputy problem](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html)*. A third party that serves many customers assumes a role in each customer's account. Without a distinguishing value, one customer could induce the provider to act against another customer's account using the provider's legitimate access. The [external ID condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_third-party.html) ties each trust relationship to a unique value that the caller must present, so the provider cannot be tricked into using the wrong customer's role. The external ID is not a secret, but it must not be guessable. Do not use an account ID or phone number. Make the field read-only so no one can change it to impersonate a different setup. 

 Decide explicitly who generates the external ID between you or the third party. The third party must enforce uniqueness and a consistent format across its customers and must map each external ID to its customer through a secure, auditable, and reproducible process. When the provider supplies the role through an [AWS CloudFormation](https://aws.amazon.com/blogs/apn/collecting-information-from-aws-cloudformation-resources-created-in-external-accounts-with-custom-resources/) template, you get a repeatable setup, a record of what was granted, and drift detection for unauthorized changes. 

 Your account structure, your need for the provider, or the provider's offering can all change or end completely. Audit the access you grant on a schedule, monitor use of the role and the store of external IDs, and be ready to revoke access temporarily or permanently when something unexpected appears. Measure what revocation costs in time, people, and downstream impact. [IAM Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html) extends the same role-based, temporary-credential model to third-party workloads that run outside AWS, which removes another reason to issue long-term keys. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Grant access through cross-account roles:** Use [cross-account roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_third-party.html) to give a third party access to resources in your account while retaining the ability to manage and audit that access. Do not issue long-term credentials or user access keys. For third-party workloads running outside AWS, use [IAM Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html) so they interact with your resources without long-term credentials. 

1.  **Perform due diligence on SaaS providers:** Before sharing resources with a third-party SaaS provider, evaluate their shared responsibility model to understand which security measures they provide and which remain yours. Confirm they access your resources through a secure, auditable process that uses [external IDs](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_third-party.html) and least-privilege access. Review their access on a schedule and audit it against your requirements. 

1.  **Deprecate long-term credentials:** Replace any long-term credentials with cross-account roles or IAM Roles Anywhere, and set a migration plan where you cannot switch immediately. Work with your AWS account team and the third party to establish a risk mitigation runbook, and coordinate it with your [Incident response](sec10.md) preparation. 

1.  **Automate and constrain the role setup:** Require the third party to provide a role policy document or an automated AWS CloudFormation setup, and keep the policy scoped to the [least-privilege principle](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) under your control. Make the external ID a non-guessable, read-only value, and decide with the provider who generates it. Monitor the deployed role for changes with drift detection. 

1.  **Plan for change and revocation:** Audit the access you grant on a regular cadence, and add detection that alerts you to unexpected changes in the role or the external ID store. Use the [Detection](sec04.md) practices to monitor use, and be prepared to revoke access when access patterns or the relationship change. Measure the time, people, and impact your revocation operation involves so it works under pressure. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC02-BP02 Use temporary credentials](sec02-bp02.md) 
+  [SEC03-BP03 Analyze public and cross-account access](sec03-bp03.md) 
+  [SEC03-BP04 Share resources securely within your organization](sec03-bp04.md) 
+  [SEC03-BP01 Grant least privilege access in workload components](sec03-bp01.md) 

 **Related documents:** 
+  [How to use an external ID when granting access to your AWS resources to a third party](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_third-party.html) 
+  [How to use trust policies with IAM roles](https://aws.amazon.com/blogs/security/how-to-use-trust-policies-with-iam-roles/) 
+  [Delegate access across AWS accounts using IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html) 
+  [How do I access resources in another AWS account using IAM?](https://repost.aws/knowledge-center/cross-account-access-iam) 
+  [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) 
+  [Cross-account policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic-cross-account.html) 
+  [Extend IAM roles to workloads outside of AWS with IAM Roles Anywhere](https://aws.amazon.com/blogs/security/extend-aws-iam-roles-to-workloads-outside-of-aws-with-iam-roles-anywhere/) 
+  [Securely using external ID for accessing AWS accounts owned by others](https://aws.amazon.com/blogs/apn/securely-using-external-id-for-accessing-aws-accounts-owned-by-others/) 

 **Related examples:** 
+  [Configure cross-account access to Amazon DynamoDB](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-cross-account-access-to-amazon-dynamodb.html) 
+  [AWS STS network query tool](https://github.com/aws-samples/aws-sts-network-query-tool) 