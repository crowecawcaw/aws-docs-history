

# Clean up example resources
<a name="bedrock-managed-agents-openai-cleanup"></a>

Clean up sessions before deleting the resources they use. Retain any generated files that you need before removing storage.

## Delete each BMA session
<a name="bedrock-managed-agents-openai-cleanup-delete-each-bma-session"></a>

From the example directory, select the client profile and state file for the session:

```
export AWS_PROFILE=my-bma-client-profile
./scripts/bma/4.delete-session.sh
```

If you used multiple state files, run the script once for each by setting `BMA_STATE_FILE`. For self-hosted sessions, stop each corresponding exec-server process after deletion.

If the local state file is unavailable, use the session ID and the signed Python client's `DELETE` operation. Inspect your session list and delete only sessions that belong to this exercise.

## Save outputs
<a name="bedrock-managed-agents-openai-cleanup-save-outputs"></a>

For AgentCore, copy the files you need from the outputs bucket before destroying the stack. For self-hosted compute, copy files from the workspace. Session deletion does not delete these copies.

## Remove the AgentCore stack
<a name="bedrock-managed-agents-openai-cleanup-remove-the-agentcore-stack"></a>

From `acr/`:

```
export AWS_PROFILE=my-deployment-profile
export AWS_REGION=us-east-1
export AWS_DEFAULT_REGION="$AWS_REGION"
npm run destroy
```

Review the stack selected for deletion. The example configures its buckets and S3 Files resources for removal, including automatic deletion of bucket objects. Destruction removes the Runtime, networking, and storage created by that stack.

Wait for CloudFormation deletion to finish. If a resource cannot be deleted, inspect the stack events, resolve the reported dependency, and retry. Confirm that no example NAT gateway or Runtime remains active.

Networking cleanup can continue after the Runtime and storage resources have been deleted. A subnet or security group cannot be removed while a service-created network interface still uses it. Check the interface's owner and associated service before taking action. See [Security group deletion dependencies](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-security-group.html). Do not treat deletion of the Runtime alone as completion of the stack cleanup.

## Remove the self-hosted IAM stack
<a name="bedrock-managed-agents-openai-cleanup-remove-the-self-hosted-iam-stack"></a>

After every session and Runtime that uses its session role has been cleaned up, run from `self-hosted/`:

```
export AWS_PROFILE=my-deployment-profile
npm run destroy
```

When the self-hosted stack owns the shared session role, destroy the AgentCore example first. If a stack was deployed with `ManageCustomerInferenceRole=false`, it does not own or delete that role.

## Review deployment assets and local files
<a name="bedrock-managed-agents-openai-cleanup-review-deployment-assets-and-local-files"></a>

CDK bootstrap resources are separate from the example stacks and can be shared by other applications. Keep them when other deployments depend on them. Review retained asset objects and container images according to your account's cleanup policy.

Remove local session-state files and test workspaces after retaining anything you need. Deleting a CloudFormation stack does not remove files from your development machine.