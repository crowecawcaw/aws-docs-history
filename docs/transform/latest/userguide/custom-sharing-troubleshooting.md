

# Troubleshooting shared transformation definitions

The following table lists messages that you might see, what causes them, and what to do.


| Message | Cause | What to do | 
| --- | --- | --- | 
| You don't have access to {{ARN}}. | No active share gives your account access. For security, the message doesn't say whether the TD exists. | Check share list --incoming, and accept any pending invitation. Check that you're in the TD's Region, and that the ARN, including the owner's account ID, is exact. Ask the owner to confirm the share. | 
| This share lets you run '{{td}}' but not download it. Ask the owner to give the share the ExecuteWithLearningsAndPackageDownload managed policy. | atx custom def get on a share without download permission. | Ask the owner to change the permission. | 
| You already accepted this share and can't leave it. Ask the owner to remove you. | share decline on a share that you already accepted. | Ask the owner to revoke the share. | 
| No active share {{id}} in this account ({{Region}}). | The share was already revoked, or you're in another Region. | Check the Region and the share ID. | 
| Share ID must be a share ID (UUID) or a share ARN. | The share ID isn't valid. | Copy the ID from share list. | 
| The invitation disappeared from share list --incoming. | It expired after 12 hours. | Ask the owner to run share create again. | 
| A shared TD doesn't appear in atx custom def list. | The invitation isn't accepted, you're in another Region, or the share was revoked. | Run share list --incoming in the TD's Region. | 
| This transformation definition is in {{Region}}. Run with AWS\_REGION={{Region}}. | You used a shared TD's ARN from another Region. | Set AWS\_REGION to the Region in the ARN, and run the command again. | 
| This share doesn't accept learnings. Ask the owner to use the ExecuteWithLearningsAndContribution managed policy, or run without --share-learnings. | --share-learnings on a share that doesn't allow contribution. | Ask the owner to change the permission, or run without --share-learnings. | 
| Your IAM identity needs transform-custom:ContributeKnowledgeItems. | Your IAM policy, or an SCP, doesn't allow contribution. | Ask your administrator to allow transform-custom:ContributeKnowledgeItems on the TD's ARN. | 
| Sharing learnings isn't available in this region yet. | Lesson contribution isn't turned on in the Region. | Run without --share-learnings. | 
| Couldn't check whether this share accepts learnings. Try again, or run without --share-learnings. | The CLI couldn't reach the service to check. | Run the command again. | 
| Revoke did not finish: {{target}} can still use {{td}}. | Your IAM identity lacks transform-custom:DeleteResourcePolicy or transform-custom:PutResourcePolicy, so AWS RAM couldn't remove access. | Add the permissions that the CLI names, and then run share revoke again. | 
| Your IAM identity needs ram:{{Action}}. | Your IAM principal lacks AWS RAM permissions. | See [Identity-based policy examples for sharing](custom-sharing-policy-examples.md). | 