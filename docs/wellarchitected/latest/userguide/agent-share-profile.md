

AWS Well-Architected Agent is in preview release and is subject to change.

# Sharing agent profiles in AWS Well-Architected Agent

Share an agent profile with other AWS accounts, an organization, or an organizational unit (OU) so that your team members can view and act on its recommendations. To share a profile, the profile owner attaches a resource-based policy to it in the AWS WA Agent console, with the API, or with the AWS CLI. The policy covers the profile, its goals and application context, and every recommendation in it.

**Important**  
Recipients can't open a shared profile without its URL. After you share, send the profile URL to the account owners.

For the actions you can grant and the rules a policy must follow, see [Profile sharing reference](#agent-share-profile-reference) and [Troubleshooting profile sharing](#agent-share-profile-troubleshooting).

## Console
<a name="agent-share-profile-console"></a>

You manage profile access from the **Profile Access** tab on the profile details page. The tab lists the AWS accounts that have access to the profile and their access level. The profile details page also offers an optional next step, **Provide profile access to team members**, that opens the same flow.

**To share with a preset access level**

1. Choose **Agent profiles**, then choose **See profile details** on the profile.

1. Choose **Actions**, then **Provide Profile access**.

1. Enter the 12-digit account IDs, separated by commas.

1. Choose **Read only** or **Read and Write**. For what each preset grants, see [Console access level presets](#agent-share-profile-presets).

1. Choose **Provide access**.

1. Choose **Copy link** and send the URL to the account owners.

To share with an organization or OU, edit the policy directly. See [Sharing with an organization or OU](#agent-share-profile-org-ou).

**To share by editing the policy**

1. On the profile details page, choose **Profile Access**, then **JSON view**, then **Edit policy**.

1. Enter the policy. For an example, see [API and CLI](#agent-share-profile-cli). For the rules a policy must follow, see [Troubleshooting profile sharing](#agent-share-profile-troubleshooting).

1. Choose **Save policy**.

1. Send the profile URL to the account owners.

To view who has access, open the **Profile Access** tab. **List view** shows each account and its access level. **JSON view** shows the policy. **Custom** means the account's statement doesn't match a preset.

To remove access for some accounts, open the **Profile Access** tab, select the accounts, choose **Un-share profile**, and confirm.

To remove access for all accounts, on the **Profile Access** tab choose **JSON view**, then **Edit policy**, clear the editor, and choose **Remove all access**.

## API and CLI
<a name="agent-share-profile-cli"></a>

Use the following operations to manage a profile's resource-based policy.


| Task | API operation | AWS CLI command | 
| --- | --- | --- | 
| Attach or replace the policy | `PutAgentProfilePolicy` | `put-agent-profile-policy --profile-arn {{arn}} --policy {{json}}` | 
| View the policy | `GetAgentProfilePolicy` | `get-agent-profile-policy --profile-arn {{arn}}` | 
| Remove the policy | `DeleteAgentProfilePolicy` | `delete-agent-profile-policy --profile-arn {{arn}}` | 

For the IAM permissions you need to call these operations, see [IAM permissions](#agent-share-profile-iam).

**To share a profile with the AWS CLI**

1. Create a file named `policy.json`. The following example grants the same actions as the console's **Read only** preset.

   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "AWSWellArchitectedAgentProfileReadOnly",
         "Effect": "Allow",
         "Principal": { "AWS": "arn:aws:iam::{{RECIPIENT_ACCOUNT_ID}}:root" },
         "Action": [
           "wellarchitected:GetAgentProfile",
           "wellarchitected:GetAgentGoal",
           "wellarchitected:ListAgentGoals",
           "wellarchitected:GetAgentContext",
           "wellarchitected:ListAgentContexts",
           "wellarchitected:ListAgentRecommendations",
           "wellarchitected:GetAgentRecommendation",
           "wellarchitected:ListAgentRecommendationItems",
           "wellarchitected:GetAgentRecommendationGeneration",
           "wellarchitected:ListAgentRecommendationGenerations"
         ],
         "Resource": [
           "arn:aws:wellarchitected:{{REGION}}:{{OWNER_ACCOUNT_ID}}:agent-profile/{{PROFILE_ID}}",
           "arn:aws:wellarchitected:{{REGION}}:{{OWNER_ACCOUNT_ID}}:agent-recommendation/*"
         ]
       }
     ]
   }
   ```

   To grant other actions, see [Actions you can grant](#agent-share-profile-actions).

1. Attach the policy to the profile:

   ```bash
   aws wellarchitected put-agent-profile-policy \
       --profile-arn "arn:aws:wellarchitected:{{REGION}}:{{OWNER_ACCOUNT_ID}}:agent-profile/{{PROFILE_ID}}" \
       --policy file://policy.json
   ```

1. Send the profile URL to the account owners.

**Note**  
`put-agent-profile-policy` replaces the whole policy. To add or remove one account, run `get-agent-profile-policy`, edit the policy, and then run `put-agent-profile-policy` with the updated policy. If the policy breaks a rule, the call fails with `ValidationException`. See [Troubleshooting profile sharing](#agent-share-profile-troubleshooting).

## Profile sharing reference
<a name="agent-share-profile-reference"></a>

A profile's resource-based policy has the following characteristics.
+ **What the policy covers:** The profile, its goals and application context, and every recommendation in it.
+ **Who can manage the policy:** The profile owner only.
+ **Re-sharing:** A recipient can't re-share the profile.
+ **`Resource` in the policy:** Exactly 2 entries, the profile ARN (`arn:aws:wellarchitected:{{REGION}}:{{OWNER_ACCOUNT_ID}}:agent-profile/{{PROFILE_ID}}`) and the recommendation wildcard ARN (`arn:aws:wellarchitected:{{REGION}}:{{OWNER_ACCOUNT_ID}}:agent-recommendation/*`).
+ **Limits:** Up to 100 accounts per share in the console, and a maximum policy size of 50 KB.
+ **Removing an account:** The account loses access to the profile and its recommendations, except recommendations shared with it directly.
+ **Deleting the profile:** Deletes the profile's policy.

### Console access level presets
<a name="agent-share-profile-presets"></a>

The console's access levels are presets. Each one writes a fixed set of actions into the policy. With **JSON view**, the API, or the AWS CLI, you can grant any combination of the actions in [Actions you can grant](#agent-share-profile-actions).


| Preset | On a profile, grants | 
| --- | --- | 
| **Read only** | View the profile, goals, application context, recommendations, and recommendation generations. | 
| **Read and Write** | Everything in **Read only**, plus update recommendation status, submit feedback, create, update, and delete goals and application context, and manage recommendation policies. | 

An account whose statement doesn't match a preset shows as **Custom** in the console.

### Actions you can grant
<a name="agent-share-profile-actions"></a>

You can grant any of the following actions in a profile policy. The columns show which preset includes each action.


| Action | **Read only** preset | **Read and Write** preset | 
| --- | --- | --- | 
| `GetAgentProfile` | Yes | Yes | 
| `GetAgentGoal`, `ListAgentGoals` | Yes | Yes | 
| `CreateAgentGoal`, `UpdateAgentGoal`, `DeleteAgentGoal` | — | Yes | 
| `GetAgentContext`, `ListAgentContexts` | Yes | Yes | 
| `CreateAgentContext`, `UpdateAgentContext`, `DeleteAgentContext` | — | Yes | 
| `ListAgentRecommendations` | Yes | Yes | 
| `GetAgentRecommendationGeneration`, `ListAgentRecommendationGenerations` | Yes | Yes | 
| `GetAgentRecommendation`, `ListAgentRecommendationItems` | Yes | Yes | 
| `UpdateAgentRecommendationStatus`, `PutAgentRecommendationFeedback` | — | Yes | 
| `PutAgentRecommendationPolicy`, `GetAgentRecommendationPolicy`, `DeleteAgentRecommendationPolicy` | — | Yes | 

You can't grant the following actions in a profile policy: `UpdateAgentProfile`, `UpdateAgentOrganizationalProfile`, `DeleteAgentProfile`, `StartAgentRecommendationGeneration`, and the profile policy operations (`PutAgentProfilePolicy`, `GetAgentProfilePolicy`, and `DeleteAgentProfilePolicy`).

### Sharing rules and behavior
<a name="agent-share-profile-rules"></a>
+ **Who you can share with:** AWS accounts, an organization in AWS Organizations, or an organizational unit (OU). Every principal in a shared account that has the required IAM permissions gets access. You can't share with an individual IAM user or role.
+ **Sharing with an organization or OU:** The console's share dialogs accept account IDs only. To share with an organization or OU, write the policy yourself in **JSON view**, with the API, or with the AWS CLI. See [Sharing with an organization or OU](#agent-share-profile-org-ou).
+ **Invitations:** None. Access takes effect immediately and doesn't expire.
+ **Finding shared resources:** Shared resources don't appear in the recipient's lists. Recipients open them from the URL that the owner sends.
+ **Owner account:** A policy affects only other accounts. Access within the owner account doesn't change.
+ **Regions:** A profile, its recommendations, and their policies exist only in the profile's AWS Region (the Region in the profile ARN). This can differ from the AWS Regions the profile analyzes. Recipients must use that Region: in the console, make sure that Region is selected; with the API or AWS CLI, specify it with `--region`.
+ **Lowering access in the console:** Sharing again with the **Read only** preset doesn't lower **Read and Write** access. Un-share the account, then share it again.
+ **No access:** Calls from another account without access return access denied, whether or not the resource exists.
+ **Failures:** If AWS WA Agent can't read a policy, it denies the request.

### Sharing with an organization or OU
<a name="agent-share-profile-org-ou"></a>

To share with every account in an organization or OU, set `Principal` to `"*"` and add conditions. Use this statement in place of the account statement in the example in [API and CLI](#agent-share-profile-cli). Keep the `Action` and `Resource` elements the same.

For an organization:

```json
"Principal": "*",
"Condition": {
  "StringEquals": { "aws:PrincipalOrgID": "{{ORG_ID}}" },
  "StringNotEquals": { "aws:PrincipalAccount": "{{OWNER_ACCOUNT_ID}}" }
}
```

For an OU:

```json
"Principal": "*",
"Condition": {
  "StringLike": { "aws:PrincipalOrgPaths": "{{ORG_ID}}/{{ROOT_ID}}/{{OU_ID}}/*" },
  "StringNotEquals": { "aws:PrincipalAccount": "{{OWNER_ACCOUNT_ID}}" }
}
```

The `aws:PrincipalAccount` condition is required. It excludes your own account from the share.

### IAM permissions
<a name="agent-share-profile-iam"></a>

To share or un-share a profile, your principal needs the following permissions:
+ `wellarchitected:GetAgentProfilePolicy`
+ `wellarchitected:PutAgentProfilePolicy`
+ `wellarchitected:DeleteAgentProfilePolicy`

The console reads the current policy before it writes one, so you need the `GetAgentProfilePolicy` permission to share from the console.

To prevent sharing, deny `wellarchitected:PutAgentProfilePolicy` and `wellarchitected:PutAgentRecommendationPolicy`.

## Troubleshooting profile sharing
<a name="agent-share-profile-troubleshooting"></a>

AWS WA Agent checks a policy before saving it. If the policy breaks a rule, the request fails with `ValidationException` and the existing policy doesn't change. In the console, a rejected save shows **Unable to update policy**. The following table lists the rules a profile policy must follow and the error message that each one returns.


| Element | Rule | Error message starts with | 
| --- | --- | --- | 
| Document | Valid policy JSON, 50 KB maximum, and can't allow public access. | "Invalid policy document"<br />"BlockPublicPolicy is enabled" | 
| `Effect` | `Allow` only. `NotPrincipal` and `NotAction` aren't supported. | "Only the Allow effect is supported"<br />"The supplied policy contains NotPrincipal" (or NotAction) | 
| `Principal` | Required. Each entry is a 12-digit account ID or `arn:aws:iam::{{RECIPIENT_ACCOUNT_ID}}:root`, listed once. Use `"*"` only to share with an organization or OU. | "Policy statement must contain a Principal block"<br />"Only account IDs or account root ARNs are allowed"<br />"Duplicate principal" | 
| `Condition` (with `"*"`) | `StringEquals` on `aws:PrincipalOrgID` with a valid organization ID, or `StringLike` on `aws:PrincipalOrgPaths`. Also `StringNotEquals` on `aws:PrincipalAccount` set to the owner account ID. | "Principal cannot equal \* without an organizations condition"<br />"aws:PrincipalAccount should exist"<br />"Principal account has to be resource owner"<br />"Only the StringEquals condition is supported" (or StringLike)<br />"Invalid organization ID format" | 
| `Action` | Required. List each action with the `wellarchitected:` prefix, no wildcards, and only actions in [Actions you can grant](#agent-share-profile-actions). | "Policy statement must contain an Action block"<br />"Wildcard actions are not allowed"<br />"Actions must use the wellarchitected: prefix"<br />"The supplied policy contains actions that are not shareable" | 
| `Resource` | Required. No `"*"`. Profile and recommendation ARNs only. | "Policy statement must contain a Resource block"<br />"Resource "\*" is not allowed"<br />"Resource ARNs must be agent-profile or agent-recommendation types" | 
| `Resource` in a profile policy | Exactly the profile ARN and its `agent-recommendation/*` ARN, in the profile's Region and account. | "Profile policy Resource must contain exactly 2 entries"<br />"Profile ARN in Resource must match"<br />"Recommendation resource in profile policy must use wildcard format"<br />"Recommendation resource ARN region must match"<br />"Recommendation resource ARN must belong to the same account" | 