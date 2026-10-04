

AWS Well-Architected Agent is in preview release and is subject to change.

# Deleting an agent profile
<a name="agent-delete-profile"></a>

**Important**  
 Deleting an agent profile also deletes all goals, application contexts, and recommendations in the profile. Before deleting, verify that you have saved any information you may need from the profile. 

## Console
<a name="agent-delete-profile-console"></a>

**To delete a profile**

1. Choose **Agent profiles** in the left-hand navigation.

1. Choose **Actions** on the profile, then **Delete profile**.

1. Confirm the deletion.

If the **Delete profile** option is unavailable (grayed out), termination protection is enabled on the profile. Disable it first:

**To disable termination protection**

1. Choose **Agent profiles** in the left-hand navigation.

1. Choose **Actions** on the profile, then **Edit profile**.

1. In **Permissions and Integrations**, disable the **Termination protection** toggle.

1. Choose **Save**.

After disabling termination protection, return to **Agent profiles** and delete the profile using **Actions**, **Delete profile**.

## CLI
<a name="agent-delete-profile-cli"></a>

To delete a profile:

```
aws wellarchitected delete-agent-profile \
    --profile-arn "{{arn:aws:wellarchitected:us-east-1:111122223333:agent-profile/my-profile}}"
```

**Note**  
If deletion protection is enabled, you must first disable it using `UpdateAgentProfile` with `--deletion-protection false` before deleting the profile.