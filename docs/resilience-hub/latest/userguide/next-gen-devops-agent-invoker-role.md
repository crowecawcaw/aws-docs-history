

# Add DevOps Agent permissions to the invoker role
<a name="next-gen-devops-agent-invoker-role"></a>

Resilience Hub connects to your Agent Space by assuming your existing invoker role – the same cross-account role that resource discovery uses. You do *not* create a new role or change its trust policy. You only add the following DevOps Agent (`aidevops`) permissions to it.

If the invoker role is missing these permissions, the connection fails with an access denied error, and the service's DevOps Agent status becomes `FAILED` with a reason that tells you to update the role. This is the most common cause of a failed connection.

Attach the following least-privilege policy to the invoker role. These eight actions are the complete set that Resilience Hub calls on your behalf – validating connectivity and starting, polling, and canceling investigations. None of them can mutate your Agent Space, or your resources.

```
{
  "Version": "2012-10-17"		 	 	 ,
  "Statement": [
    {
      "Sid": "ResilienceHubV2DevOpsAgentInvestigation",
      "Effect": "Allow",
      "Action": [
        "aidevops:CreateBacklogTask",
        "aidevops:GetBacklogTask",
        "aidevops:ListExecutions",
        "aidevops:ListJournalRecords",
        "aidevops:UpdateBacklogTask"
      ],
      "Resource": "arn:aws:aidevops:*:*:agentspace/*"
    },
    {
      "Sid": "ResilienceHubV2DevOpsAgentValidation",
      "Effect": "Allow",
      "Action": [
        "aidevops:GetAgentSpace",
        "aidevops:GetOperatorApp",
        "aidevops:ListAssociations"
      ],
      "Resource": "arn:aws:aidevops:*:*:agentspace/*"
    }
  ]
}
```

The policy contains two statements:
+ `ResilienceHubV2DevOpsAgentInvestigation` – Lets Resilience Hub start, poll, update, and cancel the backlog tasks and read the journal records that make up an investigation.
+ `ResilienceHubV2DevOpsAgentValidation` – Grants the read-only access that Resilience Hub uses to validate the Agent Space connection.

**Important**  
Do not attach the broad AWS managed policies `AIDevOpsAgentFullAccess` or `AIDevOpsOperatorAppAccessPolicy`. They grant mutating Agent Space actions that Resilience Hub must never call. The inline policy above is the only grant that the integration needs.

Save the permissions policy as `resiliencehub-devops-agent-policy.json`, then add it to the invoker role as an inline policy.

```
aws iam put-role-policy \
  --role-name {{my-invoker-role}} \
  --policy-name ResilienceHubDevOpsAgentAccess \
  --policy-document file://resiliencehub-devops-agent-policy.json
```

To confirm that the policy was added, run the following command.

```
aws iam get-role-policy \
  --role-name {{my-invoker-role}} \
  --policy-name ResilienceHubDevOpsAgentAccess
```