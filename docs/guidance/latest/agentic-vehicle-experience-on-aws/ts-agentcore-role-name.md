

# Nova 2 Sonic InvokeModelWithBidirectionalStream returns empty-message AccessDeniedException
<a name="ts-agentcore-role-name"></a>

 **Symptom.** The AgentCore execution role has a policy statement granting `bedrock:InvokeModel` and `bedrock:InvokeModelWithResponseStream`, IAM policy simulation returns `allowed`, and the Bedrock model availability check shows `AUTHORIZED` and `AVAILABLE` — yet live voice sessions fail with `AccessDeniedException` where the exception `message` field is empty (rather than containing the standard ARN-and-principal detail). Standard IAM diagnostics do not identify a denial reason.

 **Root cause.** Bedrock’s `InvokeModelWithBidirectionalStream` API has a service-side restriction that requires the AgentCore execution role name to match the prefix `AmazonBedrockAgentCoreSDKRuntime-`. Roles with any other name — including CDK-generated names — receive an `AccessDeniedException` with an empty `message` string regardless of the IAM policy’s content. The empty message is the diagnostic differentiator: a standard IAM denial includes the principal ARN and resource; this service-side name check produces no such detail. Standard IAM simulation tools cannot surface this restriction because it is enforced by the Bedrock service, not by the IAM policy evaluation engine.

 **Resolution.** 

1. Rename or recreate the AgentCore execution role so that its name matches the required prefix. A name of the form `AmazonBedrockAgentCoreSDKRuntime-<region>-<qualifier>` satisfies the restriction and also encodes the deployment region, which prevents cross-region name collisions when the same stack is deployed to multiple regions.

1. Encode this naming pattern in the CDK construct that creates the execution role so that any future deployment stage or region clone automatically uses a compliant name. Hardcode the prefix as a constant in the construct; do not derive it from a stack name or CDK logical ID, which may not preserve the required prefix.

1. After renaming the role, update the `execution_role` reference in `.bedrock_agentcore.yaml` and redeploy the AgentCore runtime. The runtime container must be redeployed with the new role; updating only the CDK stack is not sufficient because the AgentCore runtime stores the execution role ARN at registration time.

1. Confirm the fix by running a live bidi session and verifying that `AccessDenied count: 0` appears in the runtime log group and that the session produces audio output. Policy simulation alone is not sufficient to confirm this fix because the service-side check is invisible to simulation.