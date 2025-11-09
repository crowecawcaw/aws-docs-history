AWS Application Discovery Service is no longer open to new customers. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](application-discovery-service-availability-change.md "application-discovery-service-availability-change.md").

# AWS Application Discovery Service ARN formats

An Amazon Resource Name (ARN) is a string that uniquely identifies an AWS resource.
AWS requires an ARN when you want to specify a resource unambiguously across all of AWS.
AWS Application Discovery Service defines the following ARNs.

- **Discovery Agent**:
  `arn:aws:discovery:`region`:`account`:agent/discovery-agent/`agentId``
- **Agentless Collector**:
  `arn:aws:discovery:`region`:`account`:agent/agentless-collector/`agentId``
- **Migration Evaluator Collector**:
  `arn:aws:discovery:`region`:`account`:agent/migration-evaluator-collector/`agentId``
- **Discovery Connector**:
  `arn:aws:discovery:`region`:`account`:agent/discovery-connector/`agentId``
