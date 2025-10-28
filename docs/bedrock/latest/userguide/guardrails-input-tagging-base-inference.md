# Use your guardrail with

inference operations to evaluate user input

You can use guardrails with the base inference operations, [InvokeModel](../APIReference/API_runtime_InvokeModel.md "../APIReference/API_runtime_InvokeModel.md") and
[InvokeModelWithResponseStream](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md") (streaming). This section covers how you selectively evaluate user
input and how you can configure streaming response behavior. Note that for
conversational applications, you can achieve the same results with the [Converse API](guardrails-use-converse-api.md "guardrails-use-converse-api.md").

For example code that calls
the base inference operations, see [Submit a single prompt with InvokeModel](inference-invoke.md "inference-invoke.md"). For information about using a guardrail with the
base inference operations, follow the steps in the API tab of [Test your guardrail](guardrails-test.md "guardrails-test.md").

###### Topics

- [Apply tags to user input to filter content](guardrails-tagging.md "guardrails-tagging.md")
- [Configure streaming response behavior to filter content](guardrails-streaming.md "guardrails-streaming.md")
- [Include a guardrail with the
  Converse API](guardrails-use-converse-api.md "guardrails-use-converse-api.md")
