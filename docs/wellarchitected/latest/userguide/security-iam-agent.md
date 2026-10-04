

AWS Well-Architected Agent is in preview release and is subject to change.

# AWS Well-Architected Agent access model
<a name="security-iam-agent"></a>

AWS Well-Architected Agent uses customer-managed IAM roles rather than service-linked roles. This design gives you full control over the permissions that AWS WA Agent has in your environment and supports the cross-account access patterns required for multi-account infrastructure analysis.

Three principals interact with AWS WA Agent through IAM:
+ **Admin users** create and manage profiles, define scope and goals, configure cross-account access, and provide additional customer context. Admin users need permissions for profile management actions such as `wellarchitected:CreateAgentProfile` and `wellarchitected:DeleteAgentProfile`.
+ **Regular users** access generated recommendations, update recommendation lifecycle (mark as complete or suppress), and provide feedback. Regular users need permissions for actions such as `wellarchitected:ListAgentRecommendations` and `wellarchitected:GetAgentRecommendation`.
+ **AWS WA Agent as an AWS service** accesses your AWS infrastructure (like accounts, resources, and applications) and understands context (like business goals) to generate recommendations. This access is implemented through a pass role mechanism where you create and manage your own IAM roles.
<a name="security-iam-agent-pass-role"></a>
**Execution roles**  
When you create a profile, you pass an execution role to AWS WA Agent. The execution role is an IAM role in the same AWS account as the profile. AWS WA Agent assumes this role to orchestrate resource discovery across your configured accounts. The execution role requires a trust policy allowing the `wellarchitected.amazonaws.com` service principal to assume it, and a permissions policy granting `sts:AssumeRole` on the access roles in your target accounts. AWS WA Agent performs a pass role check during profile creation to validate that the caller has permission to pass the specified role to the service.
<a name="security-iam-agent-cross-account"></a>
**Cross-account access**  
AWS WA Agent uses IAM role chaining to access resources across multiple accounts:

1. **Admin account (profile account):** Contains the AWS WA Agent profile and the execution role. AWS WA Agent assumes the execution role in this account.

1. **Target accounts:** Each target account contains an access role that the execution role can assume. The access role grants AWS WA Agent read-only permissions to discover and analyze resources.

1. **Role chain:** AWS WA Agent assumes the execution role, which then assumes the access role in each target account.

Each access role requires:
+ A trust policy allowing the execution role to assume it.
+ The `WellArchitectedAgentResourceScanning` managed policy attached (recommended), or a custom policy scoped to only the actions you want AWS WA Agent to perform.

Use the following trust policy template for your access roles:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::{{ProfileOwningAccountID}}:role/service-role/{{ExecutionRoleName}}"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

Replace {{ProfileOwningAccountID}} with the AWS account ID where your AWS WA Agent profile is created, and {{ExecutionRoleName}} with the name of the execution role. When the AWS WA Agent console creates the execution role, it places it under the `service-role/` path. Confirm the exact ARN from your profile details page. Onboarding is opt-in per account. For details on setting up roles, see [Getting started with AWS Well-Architected Agent](agent-getting-started.md).
<a name="security-iam-agent-confused-deputy"></a>
**Confused deputy prevention**  
AWS WA Agent uses the profile ARN as an external ID in the role assumption chain, preventing the execution role from being used outside the context of its configured profile. AWS WA Agent also performs a pass role check during profile creation to validate that the calling principal has permission to pass the execution role to the service.
<a name="security-iam-agent-revoke"></a>
**Revoking access**  
You retain full control over AWS WA Agent's access at all times. Remove the trust policy from an access role, delete an access role entirely, or revoke active sessions to terminate in-progress data collection. If AWS WA Agent encounters a permission denial during recommendation generation, the details appear in the generation records.
<a name="security-iam-agent-best-practices"></a>
**Best practices**  
Run AWS WA Agent profiles from a dedicated AWS account without production workloads. Use the execution role ARN (not the root principal) in access role trust policies. Monitor AWS CloudTrail for AWS WA Agent API activity. Periodically review access role permissions and remove accounts that no longer require analysis.