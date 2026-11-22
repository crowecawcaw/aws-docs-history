

# Resolve Insights issues

Use this topic to diagnose missing Agent Insights, request errors, Store state problems, and encryption failures.

The following table lists common symptoms and errors with recommended actions.


| Symptom or error | Action | 
| --- | --- | 
| No Agent Insights appear | Confirm that the Store is `ENABLED` and `ACTIVE`. Confirm that the evaluation uses `Builtin.FailureAnalysis`. For an online evaluation, confirm that the configuration targets the expected `service.name` and has processed sessions with failure findings. For a batch evaluation, confirm that the job completed, then filter by its `batchEvaluationId`. `ListAgentInsights` returns only active findings by default. Set `archiveStatus` to `ARCHIVED` to check the archived view. | 
|  `ValidationException`  | Check the request fields and identifiers. For `UpdateAgentInsightStore`, provide `enablementStatus`, `encryptionConfiguration`, or both. If you provide both, set `enablementStatus` to `ENABLED`. For customer managed key encryption, provide a key ARN from the Store’s Region, not a key ID or alias ARN. | 
|  `ConflictException` from `UpdateAgentInsightStore`  | Another process might still be updating the Store. You can also receive this error when you request an encryption change for a disabled Store. Poll `GetAgentInsightStore` until the current update settles. To change the encryption configuration of an `INACTIVE` Store, set `enablementStatus` to `ENABLED` and include the new `encryptionConfiguration` in the same request. | 
|  `ConflictException` from `UpdateAgentInsight`  | Another caller might be updating the Agent Insight. Read its current state, then retry the archive or restore request. | 
|  `ResourceNotFoundException`  | For Store requests, use the ID `default-insight-store`. For Agent Insight requests, provide the `agentInsightId` together with the `applicationName` returned by `ListAgentInsights`. | 
|  `AccessDeniedException`  | Verify your `bedrock-agentcore` permissions. For a customer managed key update, also verify your KMS permissions, the key policy, the Region, and the encryption-context conditions described in [Encryption at rest for Agent Insights](insights-security.md). | 
|  `customerMetadataStatus` is `CUSTOMER_KEY_UNAVAILABLE`  | Restore the customer managed key and the required permissions. Keep prior and current keys usable until any re-encryption operation finishes. | 
| Store `status` is `ERROR`  | Read `failureReason`, correct the reported cleanup or encryption problem, and retry the relevant update with a new client token. | 
|  `ThrottlingException` or `InternalServerException`  | Retry with exponential backoff and jitter. If the error continues, contact AWS Support. | 
|  `ServiceQuotaExceededException` from `UpdateAgentInsightStore`  | Agent Insights doesn’t expose a customer-adjustable Service Quotas value for the Store. If the error continues, contact AWS Support. | 