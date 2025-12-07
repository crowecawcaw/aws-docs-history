# Cross region inference

AgentCore AgentCore Evaluations will automatically select the optimal region within your
geography to process your inference requests. This maximizes available compute
resources, model availability, and delivers the best customer experience. Your data will
remain stored only in the region where the request originated, however, input prompts
and output results may be processed outside that region. All data will be transmitted
encrypted across AWS's secure network.

If your use case requires avoiding [cross region inference](../../../cross-region-inference.md "../../../cross-region-inference.md"), you can create
[Custom evaluators](custom-evaluators.md "custom-evaluators.md") that operate
without CRIS. Custom evaluators provide the flexibility to:

- Replicate the functionality of built-in evaluators without using CRIS
- Define identical evaluation criteria and scoring schemas as built-in
  evaluators
- Maintain full control over the inference configuration

###### Note

While custom evaluators can be configured to match built-in evaluator
functionality, you are responsible for managing model availability and compute
resources.
