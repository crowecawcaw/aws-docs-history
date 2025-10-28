# Exclusions

When doing a blue/green or rolling deployment, your new endpoint configuration must have the
same variant name as the old endpoint configuration. There are also feature-based exclusions
that make your endpoint incompatible with deployment guardrails at this time. If your
endpoint uses any of the following features, you cannot use deployment guardrails on your
endpoint, and your endpoint will fall back to using a blue/green deployment with all at once
traffic shifting and no final baking period:

- Marketplace containers
- Endpoints that use Inf1 (Inferentia-based) instances
  If you're doing a rolling deployment, there are additional feature-based
  exclusions:

- Serverless inference endpoints
- Multi-variant inference endpoints
