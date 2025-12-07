# AgentCore generated AgentCore Policy observability

data

For AgentCore Policy and policy Engine resource types, Amazon Bedrock AgentCore publishes invocation
metrics to CloudWatch by default. Additional span data is available when traces are enabled for
the attached AgentCore Gateway resource, which will emit spans for AgentCore Policy related operations. See
[Enabling observability for
AgentCore runtime, memory, gateway, built-in tools, and identity
resources](observability-configure.md#observability-configure-cloudwatch "observability-configure.md#observability-configure-cloudwatch") to learn more about
enablement.

###### Topics

- [Provided metric data](#observability-policy-metrics-provided "#observability-policy-metrics-provided")
- [Provided span data](#observability-policy-spans "#observability-policy-spans")

## Provided metric data

Amazon Bedrock AgentCore publishes the following invocation metrics by default to the
`Bedrock-Agentcore` CloudWatch namespace. These metrics can be used to observe
and monitor policy evaluations and overall performance.

| Metric                  | Description                                                                                       | Unit         |
| ----------------------- | ------------------------------------------------------------------------------------------------- | ------------ |
| Invocations             | Number of requests made to the service                                                            | Count        |
| SystemErrors            | Number of server-side errors (5xx)                                                                | Count        |
| UserErrors              | Number of client-side errors (4xx)                                                                | Count        |
| Latency                 | Total time elapsed from sending a request to receiving a<br>response                              | Milliseconds |
| AllowDecisions          | Number of decisions that resulted in ALLOW                                                        | Count        |
| DenyDecisions           | Number of decisions that resulted in DENY                                                         | Count        |
| TotalMismatchedPolicies | Number of failed policies for a given request due to either missing<br>attribute or type mismatch | Count        |
| PolicyMismatch          | Number of failures for a specific policy caused by missing attribute<br>or type mismatch          | Count        |
| MismatchErrors          | Number of requests that failed due to at least one mismatched<br>policy                           | Count        |
| DeterminingPolicies     | Number of determining policies for a request                                                      | Count        |
| NoDeterminingPolicies   | Number of requests denied due to no determining policies                                          | Count        |

### Metric Dimensions

The following dimensions are available for the above metrics. These dimensions
allow you to filter and analyze metric data at finer levels of detail.

| Dimension      | Description                                                                                             |
| -------------- | ------------------------------------------------------------------------------------------------------- |
| OperationName  | The name of the API operation, valid values are<br>`AuthorizeAction` and<br>`PartiallyAuthorizeActions` |
| PolicyEngine   | The Policy Engine identifier associated with the metric                                                 |
| Policy         | The Policy identifier associated with the metric                                                        |
| TargetResource | The AgentCore Gateway resource identifier associated with the<br>request                                |
| ToolName       | The name of the tool the metric applies to                                                              |
| Mode           | The enforcement mode configured on the AgentCore Gateway, valid values<br>are `LOG_ONLY` and `ENFORCE`  |

## Provided span data

Amazon Bedrock AgentCore provides additional structured span data through AgentCore Gateway
observability, offering deeper insights into API invocations. AgentCore Policy span data is
available after enabling traces for your AgentCore Gateway resource and can be found in CloudWatch
`aws/spans` log group.

| Operation                 | Span Attribute                              | Description                                                                                                      |
| ------------------------- | ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| AuthorizeAction           | aws.agentcore.policy.authorization_decision | The authorization decision after evaluating policies, valid values<br>are `ALLOW` and `DENY`                     |
|                           | aws.agentcore.policy.authorization_reason   | Reason for the authorization decision                                                                            |
|                           | aws.agentcore.policy.determining_policies   | List of Policy identifiers that determined the decision<br>outcome                                               |
|                           | aws.agentcore.policy.mismatched_policies    | List of Policy identifiers that failed due to missing attributes or<br>type mismatches                           |
|                           | aws.agentcore.policy.target_resource.id     | AgentCore Gateway resource identifier the request applies to                                                     |
|                           | aws.agentcore.gateway.policy.arn            | Policy Engine Amazon Resource Name (ARN) configured on the AgentCore Gateway                                     |
|                           | aws.agentcore.gateway.policy.mode           | Policy Engine enforcement mode configured on the AgentCore Gateway, valid<br>values are `LOG_ONLY` and `ENFORCE` |
| PartiallyAuthorizeActions | aws.agentcore.policy.allowed_tools          | List of tool names that evaluated to an `ALLOW`<br>decision                                                      |
|                           | aws.agentcore.policy.denied_tools           | List of tool names that evaluated to a `DENY`<br>decision                                                        |
|                           | aws.agentcore.policy.target_resource.id     | AgentCore Gateway resource identifier the request applies to                                                     |
|                           | aws.agentcore.gateway.policy.arn            | Policy Engine Amazon Resource Name (ARN) configured on the AgentCore Gateway                                     |
|                           | aws.agentcore.gateway.policy.mode           | Policy Engine enforcement mode configured on the AgentCore Gateway, valid<br>values are `LOG_ONLY` and `ENFORCE` |
