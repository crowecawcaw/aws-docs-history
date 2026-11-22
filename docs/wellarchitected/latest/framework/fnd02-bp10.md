

# FND02-BP10 Establish workload and machine identity federation

 Workloads and machines need to access AWS resources at least as often as people do, but they require a unique form of identity federation. Long-lived access keys stored in CI/CD systems, containers, or on-premises servers are a persistent source of credential exposure. Federating workload identities so they receive short-lived credentials from a trusted identity source removes the need to issue, store, and rotate those keys. 

 **Desired outcome:** 
+  Your workloads receive AWS credentials through federation from their native identity provider rather than from static IAM access keys. 
+  Your on-premises servers and systems outside AWS use IAM Roles Anywhere with certificates issued by a trusted certificate authority. 
+  Your CI/CD pipelines (GitHub Actions, GitLab CI, and similar) assume roles directly through OpenID Connect (OIDC) federation with no stored access keys. 
+  Your Kubernetes workloads use IAM roles for service accounts (IRSA) or EKS Pod Identity rather than node-level credentials shared by every pod. 
+  Your foundation team provides standard federation patterns as reusable infrastructure-as-code modules so workload teams can adopt them directly. 

 **Common anti-patterns:** 
+  Creating a long-lived IAM user with access keys for every CI/CD pipeline, then storing those keys in the CI system's secret store. 
+  Granting the same broad permissions to every pod on a Kubernetes node, so any pod can do anything any other pod can do. 
+  Allowing on-premises servers to use IAM users with long-lived access keys instead of IAM Roles Anywhere. 
+  Using the same federated role for an entire external workload when different components need different permissions. 
+  Treating federation as each workload team's responsibility, so every team reinvents the trust relationship and the IAM role design. 

 **Benefits of establishing this best practice:** 
+  Removing long-lived credentials for workloads removes the largest source of credential exposure risk in most environments. 
+  Automatic credential expiration through short-lived federated credentials limits the window of exposure if a credential is disclosed. 
+  Reduced operational overhead because there are no access keys to rotate, store, distribute, or track across CI/CD systems and external infrastructure. 
+  Stronger audit trails because CloudTrail shows the federated identity source (for example, the GitHub repository or the Kubernetes service account), not an anonymous IAM user. 
+  Consistent patterns across the organization because the foundation team provides reusable federation modules that workload teams consume. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 IAM users with long-lived access keys become the largest credential exposure surface as workloads multiply. Every CI/CD pipeline, container, hybrid server, and third-party integration that holds a long-lived key is a persistent risk: the key is stored in at least one system outside AWS, often in several, and never expires. 

 Federation removes the key. The workload authenticates with its own built-in identity source and exchanges that identity for short-lived AWS credentials. The authentication proof is whatever the workload already has, such as an OIDC token from GitHub Actions, a Kubernetes service account token, or an X.509 certificate from your internal PKI. AWS verifies the proof against a trust relationship the foundation team has established and returns temporary credentials that expire within hours. 

 The foundation team establishes the trust relationships once, publishes IAM role patterns workload teams can consume, and documents how each common federation source works. 

 **For CI/CD pipelines**, [OpenID Connect (OIDC) federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_oidc.html) is the mature pattern. [GitHub Actions](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/), GitLab, CircleCI, and similar systems publish OIDC tokens that can be exchanged for AWS credentials with no stored keys. Trust relationships are scoped to specific repositories, branches, or environments so an unauthorized workflow assumption cannot access unrelated resources. 

 **For Kubernetes workloads**, [IAM roles for service accounts (IRSA)](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html) and [EKS Pod Identity](https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html) give each pod its own IAM identity. This replaces the earlier pattern where every pod inherited the node's IAM role, which made least privilege at the pod level impossible. EKS Pod Identity is the newer option and simplifies setup because it does not require an OIDC provider per cluster. 

 **For workloads outside AWS**, [IAM Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html) uses X.509 certificates from a trusted certificate authority to obtain temporary credentials. This works for on-premises servers, other cloud providers, and any system that can present a certificate. It shifts credential management from "secure the access key" to "manage the certificate lifecycle," which existing PKI processes handle well. 

 **For SaaS and partner integrations**, cross-account IAM roles with external IDs and condition keys provide a federated pattern that avoids giving partners an IAM user. The partner assumes a role using their own AWS account as the trust source, and conditions on the trust policy lock the relationship to a specific external ID negotiated during onboarding. 

 The foundation team owns the trust relationship setup and publishes the IAM role patterns. Workload teams consume a standard module and pass parameters (repository name, cluster name, or certificate subject). This gives you a central place to enforce conditions (scoping trust to specific accounts, branches, or paths) so workload teams cannot accidentally create over-permissive trust policies. 

**Important**  
 Trust relationships scoped too broadly (for example, an OIDC trust that accepts any GitHub repository) remove most of the security benefit of federation. Scope trust policies to specific repositories, branches, environments, or subject claims. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Inventory workloads using long-lived credentials:** Use [IAM credential reports](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html) and [IAM Access Analyzer unused access findings](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) to list IAM users with active access keys across your organization. For each, identify the workload or system that owns the credential and where the key is stored. This inventory becomes the migration backlog. 

1.  **Establish OIDC federation for CI/CD systems:** Create [OIDC identity providers in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_oidc.html) for each CI/CD system your organization uses. For GitHub Actions, follow [Configuring OpenID Connect in Amazon Web Services](https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-aws). Publish reusable IAM role templates that workload teams parameterize with their repository and branch names. Scope trust policies using claim conditions (token.actions.githubusercontent.com:sub) so only specific repositories and branches can assume roles. 

1.  **Enable IAM roles for service accounts or Pod Identity on EKS clusters:** For [Amazon EKS](https://aws.amazon.com/eks/) clusters, enable [EKS Pod Identity](https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html) on new clusters and [IAM roles for service accounts (IRSA)](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html) on existing ones. Publish standard IAM role patterns for common workload types (read-only service, write-to-S3 service, cross-account service) so teams adopt per-pod identities rather than granting broad permissions to nodes. 

1.  **Deploy IAM Roles Anywhere for workloads outside AWS:** Set up [IAM Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/getting-started.html) with a [trust anchor](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/trust-model.html) tied to your certificate authority. For organizations without an internal PKI, use [AWS Private CA](https://aws.amazon.com/private-ca/) to issue certificates. Publish documentation for how on-premises teams request certificates and configure their systems to use the [credential helper](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/credential-helper.html). 

1.  **Publish federation patterns as reusable modules:** Package the common federation patterns (GitHub OIDC, GitLab OIDC, EKS IRSA, IAM Roles Anywhere, cross-account SaaS integration) as reusable infrastructure-as-code modules using [AWS CloudFormation](https://aws.amazon.com/cloudformation/), [AWS CDK](https://aws.amazon.com/cdk/), or Terraform. Store them in your shared repository and include documentation, examples, and scoped trust policies. Workload teams consume a module and pass parameters rather than writing trust policies themselves. 

1.  **Enforce federation through preventive controls:** Use [service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) to deny iam:CreateAccessKey except in accounts or for principals that have been explicitly approved. Use [AWS Config rules](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html) such as iam-user-no-policies-check and iam-user-unused-credentials-check to detect drift. For new workloads, require federation in your architecture review or workload readiness process. 

1.  **Migrate existing long-lived credentials:** Work through the inventory from step 1. For each workload, replace the IAM user with the appropriate federation pattern and delete the access key after the new path is verified. Track progress through a dashboard so the migration is visible and stakeholders see the exposure surface shrinking. 

1.  **Monitor and audit federated role usage:** Use [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) to verify federated roles are being assumed by the expected identities (GitHub repositories, Kubernetes service accounts, certificate subjects). Use [IAM Access Analyzer](https://aws.amazon.com/iam/access-analyzer/) to detect overly permissive trust policies. Configure alerts for unexpected role assumptions (for example, a GitHub role assumed from a different IP range or a certificate role assumed with an unexpected subject). 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [FND02-BP05 Grant least privilege access](fnd02-bp05.md) 
+  [FND02-BP06 Define permission guardrails for your organization](fnd02-bp06.md) 
+  [FND02-BP08 Audit and rotate credentials periodically](fnd02-bp08.md) 
+  [SEC02-BP01 Identify principals and identity use-cases](sec02-bp01.md) 

 **Related documents:** 
+  [IAM Roles Anywhere User Guide](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html) 
+  [OpenID Connect identity providers in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_oidc.html) 
+  [EKS Pod Identity](https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html) 
+  [IAM roles for service accounts on Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html) 
+  [Configuring OpenID Connect in Amazon Web Services (GitHub)](https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-aws) 
+  [Cross-account access using IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.html) 
+  [Alternatives to long-term access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds-programmatic-access.html#security-creds-alternatives-to-long-term-access-keys) 

 **Related examples:** 
+  [Secure access to AWS from GitHub Actions using OIDC](https://aws.amazon.com/blogs/security/use-iam-roles-to-connect-github-actions-to-actions-in-aws/) 
+  [Use IAM Roles Anywhere with AWS Private CA to sign X.509 certificates](https://aws.amazon.com/blogs/security/extend-aws-iam-roles-to-workloads-outside-of-aws-with-iam-roles-anywhere/) 

 **Related services:** 
+  [IAM Identity Center](https://aws.amazon.com/iam/identity-center/) 
+  [AWS IAM Roles Anywhere](https://aws.amazon.com/iam/roles-anywhere/) 
+  [AWS Private CA](https://aws.amazon.com/private-ca/) 