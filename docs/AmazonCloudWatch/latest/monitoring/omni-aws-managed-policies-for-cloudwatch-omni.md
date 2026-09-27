

# AWS managed policies for CloudWatch Omni
<a name="omni-aws-managed-policies-for-cloudwatch-omni"></a>

CloudWatch Omni provides AWS managed policies for the space operator role, for the domain access role of an organization domain, and for the roles that support organization-level Context Graph enablement. Each policy's details — the description, what it attaches to, the version history, and the complete JSON policy document — are published in the [AWS Managed Policy Reference](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/policy-list.html), which is generated from the policy itself and updated automatically when a policy changes. The following table links to each policy's page there.

For guidance on which policy you need for which task, which permissions read across your whole account, and the permissions you provide yourself, see [IAM policies to use CloudWatch Omni](omni-iam-policies-to-use-cloudwatch-omni.md).

**The policies**


| Policy | What it grants | 
| --- | --- | 
| [CloudWatchOmniSpaceAccessPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchOmniSpaceAccessPolicy.html) | The base policy, always attached to the space operator role. The space experience (space and access-grant management, telemetry queries, the context graph, alerts, dashboards, access profiles, views, threads, and integrations), together with the management side of evaluation. | 
| [CloudWatchOmniModelInferencePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchOmniModelInferencePolicy.html) | Model inference only. Attached only to spaces that use the prompt playground or run evaluations that invoke a model. | 
| [CloudWatchOmniDomainAccessPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchOmniDomainAccessPolicy.html) | Domain management for an organization domain. Attached to the domain access role, which CloudWatch Omni assumes to operate the domain. The role is created in the management account during organization domain setup. Single-account domains do not use it. | 
| [CloudWatchOmniAWSIntegrationPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchOmniAWSIntegrationPolicy.html) | Resource discovery for Context Graph: lets CloudWatch Omni discover resources and their relationships in an account. Optional on the space operator role — you choose it during space setup. In an organization Centralization rule, CloudWatch Omni also attaches it to the integration roles it provisions in each source account. | 
| [AWSCloudWatchOmniServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSCloudWatchOmniServiceRolePolicy.html) | Attached to the AWSServiceRoleForCloudWatch\_Omni service-linked role, which provisions the integration roles and the AWS Config recorder in member accounts. You cannot attach it to your own identities. | 

**CloudWatch Omni updates to AWS managed policies**

The following table describes updates to CloudWatch Omni's AWS managed policies.


| Change | Description | Date | 
| --- | --- | --- | 
| [AWSCloudWatchOmniServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSCloudWatchOmniServiceRolePolicy.html) — Updated policy | CloudWatch Omni added the iam:GetRole permission. This lets the service-linked role read and reuse the integration role it provisions in an account, instead of recreating it. | September 24, 2026 | 
| [CloudWatchOmniSpaceAccessPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchOmniSpaceAccessPolicy.html) — New policy | CloudWatch Omni added a policy that grants the space experience — space and access-grant management, telemetry queries, alerts, dashboards, access profiles, views, threads, and integrations — together with the management side of evaluation. | September 22, 2026 | 
| [CloudWatchOmniModelInferencePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchOmniModelInferencePolicy.html) — New policy | CloudWatch Omni added a policy that grants model inference for the prompt playground and for evaluations that invoke a model. | September 22, 2026 | 
| [CloudWatchOmniDomainAccessPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchOmniDomainAccessPolicy.html) — New policy | CloudWatch Omni added a policy that grants domain management for an organization domain, attached to the domain access role created during organization domain setup. | September 22, 2026 | 
| [CloudWatchOmniAWSIntegrationPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchOmniAWSIntegrationPolicy.html) — New policy | CloudWatch Omni added a policy that grants resource discovery for Context Graph. It is optional on the space operator role, and CloudWatch Omni attaches it to the integration roles it provisions in the source accounts of an organization Centralization rule. | September 22, 2026 | 
| [AWSCloudWatchOmniServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSCloudWatchOmniServiceRolePolicy.html) — New policy | CloudWatch Omni added a policy for the AWSServiceRoleForCloudWatch\_Omni service-linked role, which provisions the integration roles and the AWS Config recorder in member accounts. | September 22, 2026 | 
| CloudWatch Omni started tracking changes | CloudWatch Omni started tracking changes for its AWS managed policies. | September 22, 2026 | 