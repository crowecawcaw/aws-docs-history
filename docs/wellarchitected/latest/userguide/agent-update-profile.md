

AWS Well-Architected Agent is in preview release and is subject to change.

# Updating an agent profile
<a name="agent-update-profile"></a>

You can update a profile's display name, description, pillars, execution role, aggregation configuration, deletion protection, and business overview at any time.

## Console
<a name="agent-update-profile-console"></a>

**To update a profile**

1. Choose **Agent profiles** in the left-hand navigation.

1. Choose **Actions** on the profile, then **Edit profile**.

1. Update the fields you want to change.

1. Choose **Save**.

## CLI
<a name="agent-update-profile-cli"></a>

**Important**  
When you update a profile using the API or CLI (`UpdateAgentProfile`), you must specify all fields in the request, not only the fields you want to change. Any field omitted from the update request is reset to its default value or cleared. The update operation uses full replacement semantics (PUT), not partial update semantics (PATCH). The console handles this automatically by pre-populating all current values.

To avoid unintentionally clearing fields, retrieve the current profile configuration first, modify the values you want to change, then pass the full object back:

```
# 1. Get the current profile configuration
aws wellarchitected get-agent-profile \
    --profile-arn "{{arn:aws:wellarchitected:us-east-1:111122223333:agent-profile/my-profile}}"

# 2. Update the profile with all fields specified
aws wellarchitected update-agent-profile \
    --profile-arn "{{arn:aws:wellarchitected:us-east-1:111122223333:agent-profile/my-profile}}" \
    --display-name "{{My Profile}}" \
    --description "{{Profile description}}" \
    --pillars COST_OPTIMIZATION SECURITY \
    --execution-role-arn "{{arn:aws:iam::111122223333:role/MyExecutionRole}}" \
    --aggregation-configuration '{{[{"accountId":"111122223333","regions":["us-east-1"],"accessRoleArn":"arn:aws:iam::111122223333:role/MyRole"}]}}' \
    --deletion-protection \
    --business-overview "{{Overview of the business context}}"
```