AWS Application Discovery Service will discontinue onboarding new customers starting November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](application-discovery-service-availability-change.md "application-discovery-service-availability-change.md").

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
