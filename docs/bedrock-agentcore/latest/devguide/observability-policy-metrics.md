

# AgentCore generated Policy in AgentCore observability data
<a name="observability-policy-metrics"></a>

For policy and policy engine resource types, Amazon Bedrock AgentCore publishes invocation metrics to CloudWatch by default. Additional span data is available when traces are enabled for the attached AgentCore Gateway resource, which will emit spans for Policy in AgentCore related operations. See [Enabling observability for AgentCore runtime, memory, gateway, built-in tools, and identity resources](observability-configure.md#observability-configure-cloudwatch) to learn more about enablement.

**Topics**
+ [Provided metric data](#observability-policy-metrics-provided)
+ [Provided span data](#observability-policy-spans)

## Provided metric data
<a name="observability-policy-metrics-provided"></a>

Amazon Bedrock AgentCore publishes the following invocation metrics by default to the `AWS/Bedrock-AgentCore` CloudWatch namespace. These metrics can be used to observe and monitor policy evaluations and overall performance.


| Metric | Description | Unit | 
| --- | --- | --- | 
| Invocations | Number of requests made to the service | Count | 
| SystemErrors | Number of server-side errors (5xx) | Count | 
| UserErrors | Number of client-side errors (4xx) | Count | 
| Latency | Total time elapsed from sending a request to receiving a response | Milliseconds | 
| AllowDecisions | Number of decisions that resulted in ALLOW | Count | 
| DenyDecisions | Number of decisions that resulted in DENY | Count | 
| TotalMismatchedPolicies | Number of failed policies for a given request due to either missing attribute or type mismatch | Count | 
| PolicyMismatch | Number of failures for a specific policy caused by missing attribute or type mismatch | Count | 
| MismatchErrors | Number of requests that failed due to at least one mismatched policy | Count | 
| DeterminingPolicies | Number of determining policies for a request | Count | 
| NoDeterminingPolicies | Number of requests denied due to no determining policies | Count | 
| GuardrailLatency | Time spent evaluating guardrails for a request | Milliseconds | 
| ConfidenceScore | Score returned by Bedrock Guardrails for a policy evaluation. In the Bedrock Guardrails documentation this value is called a *severity score* for content filters and prompt attacks, and a *confidence score* for sensitive information filters. See [Bedrock Guardrails score definitions](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-use-invoke-guardrail-checks-scores.html). | None | 
| ConfidenceThreshold | Score threshold configured by a guardrail policy | None | 
| SuppressOutputs | Number of outputs suppressed by policies using the `suppressOutput` effect | Count | 
| LogOnlyMatches | Number of `LOG_ONLY` policy matches | Count | 
| LogOnlyDecisionFlips | Number of `LOG_ONLY` policy matches that change the authorization decision when the policy is promoted to `ACTIVE`  | Count | 
| LogOnlyEvalIncomplete | Number of requests for which `LOG_ONLY` policy evaluation was incomplete | Count | 
| TemporalLatency | Time spent evaluating temporal policies. One sample is emitted for each temporal evaluation. Use `SampleCount` to count evaluations. See [CloudWatch statistics definitions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html). | Milliseconds | 

### Metric Dimensions
<a name="observability-policy-metrics-dimensions"></a>

The following dimensions are available for the above metrics. These dimensions allow you to filter and analyze metric data at finer levels of detail.


| Dimension | Description | 
| --- | --- | 
| OperationName | The name of the API operation, valid values are `AuthorizeAction` and `PartiallyAuthorizeActions`  | 
| PolicyEngine | The Policy Engine identifier associated with the metric | 
| Policy | The Policy identifier associated with the metric | 
| TargetResource | The AgentCore Gateway resource identifier associated with the request | 
| ToolName | The name of the tool the metric applies to | 
| Mode | The enforcement mode configured on the AgentCore Gateway, valid values are `LOG_ONLY` and `ENFORCE`  | 
| Category | The guardrail safeguard type. Valid values are `contentFilter`, `promptAttack`, and `sensitiveInformation`. See [Guardrails in policies](policy-guardrails-in-policies.md). | 
| Filter | The guardrail filter or sensitive information entity, such as `VIOLENCE`, `PROMPT_INJECTION`, or `EMAIL`  | 
| PolicyEnforcementMode | The enforcement mode of an individual policy. Valid values are `ACTIVE` and `LOG_ONLY`. This dimension applies to `ConfidenceScore`, `ConfidenceThreshold`, and `MismatchErrors`. See [Test a policy in LOG\_ONLY mode](policy-test-a-policy.md). | 

## Provided span data
<a name="observability-policy-spans"></a>

Amazon Bedrock AgentCore provides additional structured span data through AgentCore Gateway observability, offering deeper insights into API invocations. Policy in AgentCore span data is available after enabling traces for your AgentCore Gateway resource and can be found in CloudWatch `aws/spans` log group.


| Operation | Span Attribute | Description | 
| --- | --- | --- | 
| AuthorizeAction | aws.agentcore.policy.authorization\_decision | The authorization decision after evaluating policies, valid values are `ALLOW` and `DENY`  | 
|  | aws.agentcore.policy.authorization\_reason | Reason for the authorization decision | 
|  | aws.agentcore.policy.determining\_policies | List of Policy identifiers that determined the decision outcome | 
|  | aws.agentcore.policy.mismatched\_policies | List of Policy identifiers that failed due to missing attributes or type mismatches | 
|  | aws.agentcore.policy.target\_resource.id | AgentCore Gateway resource identifier the request applies to | 
|  | aws.agentcore.gateway.policy.arn | Policy Engine Amazon Resource Name (ARN) configured on the AgentCore Gateway | 
|  | aws.agentcore.gateway.policy.mode | Policy Engine enforcement mode configured on the AgentCore Gateway, valid values are `LOG_ONLY` and `ENFORCE`  | 
|  | aws.agentcore.policy.guardrails.<category>.scores | Guardrail findings as Policy identifier, filter, and score tuples. Valid categories are `contentFilter`, `promptAttack`, and `sensitiveInformation`  | 
|  | aws.agentcore.policy.types | Policy identifier and policy type tuples for determining policies. Valid policy types are `Cedar` and `Guardrail`  | 
|  | aws.agentcore.policy.effects | Policy identifier and effect tuples. Valid effects are `PERMIT`, `FORBID`, and `SuppressOutput`  | 
|  | aws.agentcore.policy.guardrails.latency\_ms | Time spent evaluating guardrails, in milliseconds | 
|  | aws.agentcore.policy.log\_only\_matched\_policies | List of `LOG_ONLY` Policy identifiers that matched the request | 
|  | aws.agentcore.policy.log\_only\_decision\_flipping\_policies | List of `LOG_ONLY` Policy identifiers that change the authorization decision when promoted to `ACTIVE`  | 
|  | aws.agentcore.policy.log\_only\_mismatched\_policies | List of `LOG_ONLY` Policy identifiers that failed due to missing attributes or type mismatches | 
|  | aws.agentcore.policy.log\_only\_eval\_incomplete | The string `true` when `LOG_ONLY` policy evaluation was incomplete. The attribute is omitted otherwise | 
|  | aws.agentcore.policy.log\_only\_matched\_policies.guardrails.<category>.scores | Guardrail findings for matched `LOG_ONLY` policies as Policy identifier, filter, and score tuples | 
|  | aws.agentcore.policy.log\_only\_decision\_flipping\_policies.guardrails.<category>.scores | Guardrail findings for decision-flipping `LOG_ONLY` policies as Policy identifier, filter, and score tuples | 
|  | aws.agentcore.policy.temporal.latency\_ms | Time spent evaluating temporal policies, in milliseconds | 
|  | aws.agentcore.policy.temporal.evaluation\_invoked | Whether temporal policy evaluation ran for the request. This does not indicate that a temporal policy matched or determined the decision | 
|  | aws.agentcore.policy.temporal.event\_timestamp\_ns | Exact event timestamp used by the temporal evaluator to order the request event, in nanoseconds | 
| PartiallyAuthorizeActions | aws.agentcore.policy.allowed\_tools | List of tool names that evaluated to an `ALLOW` decision | 
|  | aws.agentcore.policy.denied\_tools | List of tool names that evaluated to a `DENY` decision | 
|  | aws.agentcore.policy.target\_resource.id | AgentCore Gateway resource identifier the request applies to | 
|  | aws.agentcore.gateway.policy.arn | Policy Engine Amazon Resource Name (ARN) configured on the AgentCore Gateway | 
|  | aws.agentcore.gateway.policy.mode | Policy Engine enforcement mode configured on the AgentCore Gateway, valid values are `LOG_ONLY` and `ENFORCE`  | 