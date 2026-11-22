

# SEC03-BP04 Share resources securely within your organization

 You often need the same resource in several accounts, or you need one account to reach a resource owned by another. Recreating a resource in every account or sharing the resource broadly are both imperfect solutions. Instead, share resources through controlled mechanisms with trusted entities only, and monitor those shares to limit access to what each consumer needs. 

 **Desired outcome:** 
+  You share resources within your organization through mechanisms scoped to trusted identities, resources, and networks. 
+  You monitor shared resources continuously, and unexpected external sharing raises an alert. 
+  You maintain a baseline of resources approved for sharing, so deviations are easy to spot. 
+  You create foundational resources once and share them, rather than recreating overlapping copies per account. 

 **Common anti-patterns:** 
+  No process monitors shared resources or alerts on unexpected external sharing. 
+  Teams have no baseline for which resources to share and which to keep private. 
+  Accounts default to a broadly open policy instead of sharing explicitly when required. 
+  Teams recreate the same foundational resource in each account rather than sharing one. 

 **Benefits of establishing this best practice:** 
+  Sharing through scoped mechanisms reduces the chance of exposing a resource to an untrusted principal. 
+  Creating a resource once and sharing it lowers operational overhead and removes errors from duplicate builds. 
+  A defined trust boundary supports data loss prevention by limiting where resources can travel. 
+  Central management of shared resources shortens time to resolution when a shared component fails. 
+  A current view of shares increases confidence when deciding that a resource is no longer needed. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Give trusted accounts a controlled path to a specific resource, and restrict access outside of that. To do this, you need a mechanism that shares the resource and a boundary that constrains who the share can reach. Without the boundary, a sharing feature meant for internal use can grant access to any account that knows the resource identifier. 

 That boundary is a *data perimeter*: preventive guardrails that verify access only when a trusted identity reaches a trusted resource from an expected network. On AWS, the perimeter typically maps to your organization plus any on-premises networks that access your resources. Condition keys such as aws:PrincipalOrgID on a resource or endpoint policy enforce it, and deny requests from identities outside the organization. Building a perimeter has real cost, so evaluate the control objectives against your risk model before adopting them all. [Service control policies do not apply to service-linked roles or AWS service principals](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html#scp-effects-on-permissions), so the perimeter must account for those paths separately. 

 [Resource control policies (RCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html) complete the perimeter from the resource side. SCPs constrain the principals in your accounts, while an RCP sets the maximum access allowed on your resources regardless of which principal makes the request, including AWS service principals and principals outside your organization that SCPs cannot reach. Enforce aws:PrincipalOrgID in an RCP on supported resource types (such as Amazon S3, AWS STS, AWS KMS, Amazon SQS, and AWS Secrets Manager) to deny access from any identity outside your organization and close the service-principal gap that your SCPs have opened. 

 Prefer purpose-built sharing over general cross-account access. Many services integrate with [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services_list.html) to share to or manage from a central account, so [AWS Security Hub CSPM](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-securityhub.html) can consolidate findings and [AWS Backup](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-backup.html) can share backups across accounts. For common infrastructure such as subnets, Transit Gateway attachments, or firewalls, [AWS Resource Access Manager](https://aws.amazon.com/ram/) shares one resource across accounts and adds visibility and auditability through logging integrations that raw cross-account access does not provide. 

 For object storage, [turn off ACLs on your bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html) and define access through policies, which gives you a single control model instead of two overlapping ones. When a content delivery distribution reads from an origin bucket, [use origin access control](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html) instead of the older origin access identity, because it supports features such as server-side encryption with managed keys. Sharing an encrypted resource often means sharing access to the key as well, which is a separate grant. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Organize accounts with AWS Organizations:** Request accounts through your organization's account vending process so they join [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) and the organizational unit that matches their purpose. Grouping accounts into organizational units lets you attach policies that meet your security and compliance needs at the right scope. 

1.  **Establish a data perimeter:** Evaluate the perimeter controls already in place from account provisioning, and adopt the control objectives from [Building a data perimeter on AWS](https://docs.aws.amazon.com/whitepapers/latest/building-a-data-perimeter-on-aws/building-a-data-perimeter-on-aws.html) that fit your risk posture. Implement the guardrails that verify access comes from a trusted identity, to a trusted resource, over an expected network. Combine [SCPs](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) that constrain your principals with [RCPs](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html) that constrain your resources: attach an RCP that enforces aws:PrincipalOrgID on supported resource types so that no principal outside your organization, including AWS service principals, can reach them. Rather than authoring these policies from scratch, start from the [data perimeter policy examples](https://github.com/aws-samples/data-perimeter-policy-examples), which provide reference SCPs, RCPs, and VPC endpoint policies for each perimeter control objective. 

1.  **Use built-in resource sharing and restrict it:** Where a service supports sharing a resource with another account, such as [Amazon Machine Images](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html), constrain the share to trusted accounts. Restrict the ModifyImageAttribute API to specific accounts, and set the ram:RequestedAllowsExternalPrincipals condition to keep [AWS RAM](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html) sharing inside your organization. See [resource sharing and external targets](https://docs.aws.amazon.com/whitepapers/latest/building-a-data-perimeter-on-aws/perimeter-implementation.html) for prescriptive guidance. 

1.  **Share with AWS RAM instead of cross-account access:** Use [AWS RAM](https://aws.amazon.com/ram/) to create a resource once and share it with roles and accounts, gaining consistency and auditability through logging integrations. If you previously shared a resource through a resource-based policy, promote it with the [PromoteResourceShareCreatedFromPolicy API](https://docs.aws.amazon.com/ram/latest/APIReference/API_PromoteResourceShareCreatedFromPolicy.html) to manage it as a full RAM resource share. 

1.  **Share access to encryption keys when sharing encrypted resources:** For an encrypted resource such as an Amazon Elastic Block Store (EBS) snapshot, [share the AWS KMS key](https://docs.aws.amazon.com/ebs/latest/userguide/share-kms-key.html) as well, because a consumer cannot use the resource without access to the key that protects it. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC03-BP03 Analyze public and cross-account access](sec03-bp03.md) 
+  [SEC03-BP05 Share resources securely with a third party](sec03-bp05.md) 
+  [SEC03-BP01 Grant least privilege access in workload components](sec03-bp01.md) 
+  [SEC05-BP01 Create network layers](sec05-bp01.md) 

 **Related documents:** 
+  [Building a data perimeter on AWS](https://docs.aws.amazon.com/whitepapers/latest/building-a-data-perimeter-on-aws/building-a-data-perimeter-on-aws.html) 
+  [Bucket owner granting cross-account permission to objects it does not own](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-walkthroughs-managing-access-example4.html) 
+  [How to use trust policies with IAM roles](https://aws.amazon.com/blogs/security/how-to-use-trust-policies-with-iam-roles/) 
+  [How to use an external ID when granting a third party access to your AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_third-party.html) 
+  [AWS services you can use with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services_list.html) 
+  [Establishing a data perimeter on AWS: allow only trusted identities to access company data](https://aws.amazon.com/blogs/security/establishing-a-data-perimeter-on-aws-allow-only-trusted-identities-to-access-company-data/) 

 **Related examples:** 
+  [Data perimeter policy examples](https://github.com/aws-samples/data-perimeter-policy-examples) 