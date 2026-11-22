

AWS Well-Architected Agent is in preview release and is subject to change.

# Sharing recommendations in AWS Well-Architected Agent

Share a single recommendation with other AWS accounts, an organization, or an organizational unit (OU) so that the teams that own the affected resources can review and act on it. To share a recommendation, you attach a resource-based policy to it in the AWS WA Agent console, with the API, or with the AWS CLI. The profile owner can share a recommendation, and so can any account that the profile policy allows to do so. To share every recommendation in a profile, share the profile instead. For more information, see [Sharing agent profiles in AWS Well-Architected Agent](agent-share-profile.md).

**Important**  
Recipients can't open a shared recommendation without its URL. After you share, send the recommendation URL to the account owners.

For the actions you can grant and the rules a policy must follow, see [Recommendation sharing reference](#agent-share-rec-reference) and [Troubleshooting recommendation sharing](#agent-share-rec-troubleshooting).

## Console
<a name="agent-share-rec-console"></a>

You manage recommendation access from the recommendation detail page, under **Actions**, **Recommendation shared with**.

**To share with a preset access level**

1. Open the recommendation's detail page from the dashboard.

1. Choose **Actions**, then **Share Recommendation**.

1. Choose **All affected accounts** and select accounts, or choose **Custom accounts** and enter the 12-digit account IDs, separated by commas.

1. Choose **Read only** or **Read and Write**. For what each preset grants, see [Console access level presets](#agent-share-rec-presets).

1. Choose **Share recommendation**.

1. Choose **Copy link** and send the URL to the account owners.

To share with an organization or OU, edit the policy directly. See [Sharing with an organization or OU](#agent-share-rec-org-ou).

**To share by editing the policy**

1. On the recommendation detail page, choose **Actions**, then **Recommendation shared with**, then **JSON view**, then **Edit policy**.

1. Enter the policy. For an example, see [API and CLI](#agent-share-rec-cli). For the rules a policy must follow, see [Troubleshooting recommendation sharing](#agent-share-rec-troubleshooting).

1. Choose **Save policy**.

1. Send the recommendation URL to the account owners.

To view who has access, open the **Recommendation shared with** page. **List view** shows each account and its access level. **JSON view** shows the policy.

To remove access for some accounts, on the **Recommendation shared with** page, select the accounts, choose **Un-share recommendation**, and confirm. The accounts keep any access they have through a profile share. See [How the two policies combine](#agent-share-rec-combine).

To remove access for all accounts, on the **Recommendation shared with** page choose **JSON view**, then **Edit policy**, clear the editor, and choose **Remove all access**.

## API and CLI
<a name="agent-share-rec-cli"></a>

Use the following operations to manage a recommendation's resource-based policy.


| Task | API operation | AWS CLI command | 
| --- | --- | --- | 
| Attach or replace the policy | `PutAgentRecommendationPolicy` | `put-agent-recommendation-policy --recommendation-arn {{arn}} --policy {{json}}` | 
| View the policy | `GetAgentRecommendationPolicy` | `get-agent-recommendation-policy --recommendation-arn {{arn}}` | 
| Remove the policy | `DeleteAgentRecommendationPolicy` | `delete-agent-recommendation-policy --recommendation-arn {{arn}}` | 

For the IAM permissions you need to call these operations, see [IAM permissions](#agent-share-rec-iam).

**To share a recommendation with the AWS CLI**

1. Create a file named `policy.json`. The following example grants the same actions as the console's **Read and Write** preset.

   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "AWSWellArchitectedAgentRecommendationReadWrite",
         "Effect": "Allow",
         "Principal": { "AWS": "arn:aws:iam::{{RECIPIENT_ACCOUNT_ID}}:root" },
         "Action": [
           "wellarchitected:GetAgentRecommendation",
           "wellarchitected:ListAgentRecommendationItems",
           "wellarchitected:UpdateAgentRecommendationStatus",
           "wellarchitected:PutAgentRecommendationFeedback"
         ],
         "Resource": "arn:aws:wellarchitected:{{REGION}}:{{OWNER_ACCOUNT_ID}}:agent-recommendation/{{RECOMMENDATION_ID}}"
       }
     ]
   }
   ```

   To grant other actions, see [Actions you can grant](#agent-share-rec-actions).

1. Attach the policy to the recommendation:

   ```bash
   aws wellarchitected put-agent-recommendation-policy \
       --recommendation-arn "arn:aws:wellarchitected:{{REGION}}:{{OWNER_ACCOUNT_ID}}:agent-recommendation/{{RECOMMENDATION_ID}}" \
       --policy file://policy.json
   ```

1. Send the recommendation URL to the account owners.

**Note**  
`put-agent-recommendation-policy` replaces the whole policy. To add or remove one account, run `get-agent-recommendation-policy`, edit the policy, and then run `put-agent-recommendation-policy` with the updated policy. If the policy breaks a rule, the call fails with `ValidationException`. See [Troubleshooting recommendation sharing](#agent-share-rec-troubleshooting).

## Recommendation sharing reference
<a name="agent-share-rec-reference"></a>

A recommendation's resource-based policy has the following characteristics.
+ **What the policy covers:** One recommendation and its affected resources.
+ **Who can manage the policy:** The profile owner, or an account that the profile policy grants `PutAgentRecommendationPolicy`, `GetAgentRecommendationPolicy`, and `DeleteAgentRecommendationPolicy`.
+ **Re-sharing:** A recommendation policy can't grant re-sharing. Only the profile policy can grant it.
+ **`Resource` in the policy:** Exactly 1 entry, the recommendation ARN (`arn:aws:wellarchitected:{{REGION}}:{{OWNER_ACCOUNT_ID}}:agent-recommendation/{{RECOMMENDATION_ID}}`).
+ **Limits:** Up to 100 accounts per share in the console, and a maximum policy size of 50 KB.
+ **Removing an account:** The account loses access from the recommendation policy, but keeps any access from a profile share. See [How the two policies combine](#agent-share-rec-combine).

### Console access level presets
<a name="agent-share-rec-presets"></a>

The console's access levels are presets. Each one writes a fixed set of actions into the policy. With **JSON view**, the API, or the AWS CLI, you can grant any combination of the actions in [Actions you can grant](#agent-share-rec-actions).


| Preset | On a recommendation, grants | 
| --- | --- | 
| **Read only** | View the recommendation and its affected resources. | 
| **Read and Write** | Everything in **Read only**, plus update the recommendation status and submit feedback. | 

An account whose statement doesn't match a preset shows as **Custom** in the console.

### Actions you can grant
<a name="agent-share-rec-actions"></a>

A recommendation policy can grant only the following four actions. The columns show which preset includes each action.


| Action | **Read only** preset | **Read and Write** preset | 
| --- | --- | --- | 
| `GetAgentRecommendation` | Yes | Yes | 
| `ListAgentRecommendationItems` | Yes | Yes | 
| `UpdateAgentRecommendationStatus` | — | Yes | 
| `PutAgentRecommendationFeedback` | — | Yes | 

A recommendation policy can't grant any other action, including the recommendation policy operations (`PutAgentRecommendationPolicy`, `GetAgentRecommendationPolicy`, and `DeleteAgentRecommendationPolicy`). Only the profile policy can grant those.

### How the two policies combine
<a name="agent-share-rec-combine"></a>

For a recommendation, AWS WA Agent checks both the recommendation policy and the profile policy. Either one can grant access.


| Recommendation policy grants the account | Profile policy grants the account | Access | 
| --- | --- | --- | 
| Yes | Yes or No | Allowed | 
| No | Yes | Allowed | 
| No | No | Denied | 

The exception is `PutAgentRecommendationPolicy`, `GetAgentRecommendationPolicy`, and `DeleteAgentRecommendationPolicy`. Only the profile policy can grant these.

### Sharing rules and behavior
<a name="agent-share-rec-rules"></a>
+ **Who you can share with:** AWS accounts, an organization in AWS Organizations, or an organizational unit (OU). Every principal in a shared account that has the required IAM permissions gets access. You can't share with an individual IAM user or role.
+ **Sharing with an organization or OU:** The console's share dialogs accept account IDs only. To share with an organization or OU, write the policy yourself in **JSON view**, with the API, or with the AWS CLI. See [Sharing with an organization or OU](#agent-share-rec-org-ou).
+ **Invitations:** None. Access takes effect immediately and doesn't expire.
+ **Finding shared resources:** Shared resources don't appear in the recipient's lists. Recipients open them from the URL that the owner sends.
+ **Owner account:** A policy affects only other accounts. Access within the owner account doesn't change.
+ **Regions:** A recommendation and its policy exist only in the profile's AWS Region (the Region in the recommendation ARN). This can differ from the AWS Regions the profile analyzes. Recipients must use that Region: in the console, make sure that Region is selected; with the API or AWS CLI, specify it with `--region`.
+ **Lowering access in the console:** Sharing again with the **Read only** preset doesn't lower **Read and Write** access. Un-share the account, then share it again.
+ **No access:** Calls from another account without access return access denied, whether or not the resource exists.
+ **Failures:** If AWS WA Agent can't read a policy, it denies the request.

### Sharing with an organization or OU
<a name="agent-share-rec-org-ou"></a>

To share with every account in an organization or OU, set `Principal` to `"*"` and add conditions. Use this statement in place of the account statement in the example in [API and CLI](#agent-share-rec-cli). Keep the `Action` and `Resource` elements the same.

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
<a name="agent-share-rec-iam"></a>

To share or un-share a recommendation, your principal needs the following permissions:
+ `wellarchitected:GetAgentRecommendationPolicy`
+ `wellarchitected:PutAgentRecommendationPolicy`
+ `wellarchitected:DeleteAgentRecommendationPolicy`

The console reads the current policy before it writes one, so you need the `GetAgentRecommendationPolicy` permission to share from the console.

To prevent sharing, deny `wellarchitected:PutAgentProfilePolicy` and `wellarchitected:PutAgentRecommendationPolicy`.

## Troubleshooting recommendation sharing
<a name="agent-share-rec-troubleshooting"></a>

AWS WA Agent checks a policy before saving it. If the policy breaks a rule, the request fails with `ValidationException` and the existing policy doesn't change. In the console, a rejected save shows **Unable to update policy**. The following table lists the rules a recommendation policy must follow and the error message that each one returns.


| Element | Rule | Error message starts with | 
| --- | --- | --- | 
| Document | Valid policy JSON, 50 KB maximum, and can't allow public access. | "Invalid policy document"<br />"BlockPublicPolicy is enabled" | 
| `Effect` | `Allow` only. `NotPrincipal` and `NotAction` aren't supported. | "Only the Allow effect is supported"<br />"The supplied policy contains NotPrincipal" (or NotAction) | 
| `Principal` | Required. Each entry is a 12-digit account ID or `arn:aws:iam::{{RECIPIENT_ACCOUNT_ID}}:root`, listed once. Use `"*"` only to share with an organization or OU. | "Policy statement must contain a Principal block"<br />"Only account IDs or account root ARNs are allowed"<br />"Duplicate principal" | 
| `Condition` (with `"*"`) | `StringEquals` on `aws:PrincipalOrgID` with a valid organization ID, or `StringLike` on `aws:PrincipalOrgPaths`. Also `StringNotEquals` on `aws:PrincipalAccount` set to the owner account ID. | "Principal cannot equal \* without an organizations condition"<br />"aws:PrincipalAccount should exist"<br />"Principal account has to be resource owner"<br />"Only the StringEquals condition is supported" (or StringLike)<br />"Invalid organization ID format" | 
| `Action` | Required. List each action with the `wellarchitected:` prefix, no wildcards, and only actions in [Actions you can grant](#agent-share-rec-actions). | "Policy statement must contain an Action block"<br />"Wildcard actions are not allowed"<br />"Actions must use the wellarchitected: prefix"<br />"The supplied policy contains actions that are not shareable" | 
| `Resource` | Required. No `"*"`. Profile and recommendation ARNs only. | "Policy statement must contain a Resource block"<br />"Resource "\*" is not allowed"<br />"Resource ARNs must be agent-profile or agent-recommendation types" | 
| `Resource` in a recommendation policy | Exactly the recommendation ARN. | "Recommendation policy Resource must contain exactly 1 entry"<br />"Recommendation policy Resource must be exactly the recommendation ARN" | 