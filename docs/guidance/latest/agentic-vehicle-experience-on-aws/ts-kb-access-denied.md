

# Knowledge Base Retrieve calls return AccessDenied despite a grant being present
<a name="ts-kb-access-denied"></a>

 **Symptom.** Agent tool calls that invoke Bedrock Knowledge Base `Retrieve` fail with `AccessDeniedException` at runtime. CloudWatch Logs show that the retrieval tool returns `{"available": false}` or falls back to local corpora rather than querying the Knowledge Base. IAM policy simulation (`iam:SimulatePrincipalPolicy`) on the AgentCore execution role returns `allowed` for the action that was granted — yet the live Retrieve still fails, or the simulation returns `implicitDeny` even though the CDK stack shows a statement.

 **Root cause.** Two distinct misconfigurations produce this symptom and are frequently confused:
+  **Wrong IAM action namespace.** The boto3 client ID for the Bedrock agent-runtime service is `bedrock-agent-runtime`, but the IAM action namespace is `bedrock:`. A statement that grants `bedrock-agent-runtime:Retrieve` or `bedrock-agent-runtime:RetrieveAndGenerate` is syntactically valid IAM but grants nothing — these action strings do not exist in the IAM service authorization tables. The correct actions are `bedrock:Retrieve` and `bedrock:RetrieveAndGenerate`. A policy containing only the wrong-namespace actions will produce an `implicitDeny` on simulation and an `AccessDeniedException` at runtime.
+  **Missing cross-account Knowledge Base ID in the agent configuration.** If the agent’s `Config` object is populated from environment variables but the field for the Knowledge Base identifier is not declared in the dataclass and not wired through the deployment pipeline, `getattr(config, "adp_kb_id", "")` resolves to the empty string. Retrieve calls issued against an empty KB ID silently fall back to local corpora rather than raising an exception, making the misconfiguration invisible until grounding quality is inspected.

 **Resolution.** 

1. Audit every IAM policy statement on the AgentCore execution role that references Bedrock Knowledge Base actions. Replace any `bedrock-agent-runtime:Retrieve` or `bedrock-agent-runtime:RetrieveAndGenerate` action strings with `bedrock:Retrieve` and `bedrock:RetrieveAndGenerate`. Redeploy the role policy and confirm with `iam:SimulatePrincipalPolicy` that the result changes from `implicitDeny` to `allowed`.

1. Verify that the Knowledge Base ID field is declared in the agent configuration dataclass, populated in `from_env()` from the correct environment variable, and that the deployment pipeline threads the environment variable through to the AgentCore runtime container. Add a pre-flight assertion in the deployment Makefile that fails the deploy if the Knowledge Base ID variable is empty — silent fallback to local corpora is not acceptable in a production-grounded deployment.

1. For cross-account Knowledge Base deployments, confirm that the Knowledge Base resource policy in the ADP account grants `bedrock:Retrieve` to the AVX AgentCore execution role principal, and that the AVX role’s identity policy grants `bedrock:Retrieve` on the cross-account Knowledge Base ARN. Both sides of the cross-account trust must be present; either side alone is insufficient.

1. Add a smoke test that runs `iam:SimulatePrincipalPolicy` against the deployed role for `bedrock:Retrieve` on the Knowledge Base ARN, and separately issues a live `Retrieve` call with a known query, asserting that the result set contains at least one chunk with a source URI matching the expected S3 prefix.