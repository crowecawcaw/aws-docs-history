

AWS Well-Architected Agent is in preview release and is subject to change.

# Troubleshooting AWS Well-Architected Agent
<a name="agent-troubleshooting"></a>

This section provides solutions to common issues you may encounter when setting up and using AWS Well-Architected Agent.

## Profile shows eligibleForScheduledGeneration: false
<a name="agent-ts-not-eligible"></a>

**Possible causes and solutions:**
+ **Missing application context:** At least one application context is required per profile. Navigate to **Profile Details**, choose the **Application context** tab, and add an application.
+ **No pillars selected:** Your profile must have at least one optimization pillar. Edit the profile and select one or more pillars.
+ **Access role trust policy not configured:** The access roles in your workload accounts must trust the execution role. Complete [Step 6: Create access roles in your workload accounts](agent-getting-started.md#agent-access-roles) and confirm the execution role ARN format is correct.
+ **Execution role does not exist or lacks permissions:** Verify the execution role ARN in your profile details page exists in IAM and has a permissions policy allowing `sts:AssumeRole` on your access roles.
+ **No accounts configured:** Your aggregation configuration must include at least one account. Edit the profile and add accounts to monitor.

To identify the specific issue, call `GetAgentProfile` and check the `fieldErrors` map in the response.

## Cross-account role configuration errors
<a name="agent-ts-trust-policy"></a>

**Possible causes and solutions:**
+ **Missing service-role/ path prefix:** If you created the execution role using the **Create new role** button in the AWS WA Agent console, the role is placed under the `service-role/` path. Use `arn:aws:iam::{{111122223333}}:role/service-role/ExecutionRoleForWellArchitectedAgent`, not `arn:aws:iam::{{111122223333}}:role/ExecutionRoleForWellArchitectedAgent`. Confirm the exact ARN from your profile details page.
+ **Wrong account ID in trust policy:** The Principal ARN must reference the account where your AWS WA Agent profile is created (the profile-owning account), not the workload account.
+ **Trust policy not applied to all accounts:** Each workload account in your aggregation configuration needs its own access role with the trust policy. Verify every account listed in your profile has a correctly configured access role.
+ **Execution role missing `sts:AssumeRole` permission:** The execution role in your profile account must have a permissions policy that allows `sts:AssumeRole` on your access roles. Verify the execution role's permissions policy includes an `sts:AssumeRole` action with the access role ARNs as resources. If you created the execution role through the AWS WA Agent console, the permissions policy must specify an access role name (for example, `AccessRoleForWellArchitectedAgent`) and cannot use wildcard (`*`) resources.

## No recommendations after 48 hours
<a name="agent-ts-no-recs"></a>

**Possible causes and solutions:**
+ **Profile not eligible:** Call `GetAgentProfile` and confirm `eligibleForScheduledGeneration` is `true`. If `false`, resolve the `fieldErrors` first.
+ **Missing application context:** At least one application context is required. Check the **Application context** tab in your profile details.
+ **Access role permissions insufficient:** Verify the [`WellArchitectedAgentResourceScanning`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/WellArchitectedAgentResourceScanning.html) managed policy is attached to each access role.
+ **Recently created profile:** Scheduled recommendations can take up to 48 hours after profile setup is complete. If less than 48 hours have elapsed, wait for the next generation cycle.

## ServiceQuotaExceededException during profile creation
<a name="agent-ts-quota-exceeded"></a>

**Possible causes and solutions:**
+ **Maximum profiles reached:** You have reached the maximum number of agent profiles for your support plan tier. See [AWS Well-Architected Agent Quotas and limits](agent-quotas.md) for tier-specific limits. Delete an unused profile or upgrade your support plan tier.