

# Text chat returns 500 RuntimeClientError; voice works normally
<a name="ts-no-text-runtime"></a>

 **Symptom.** The web UI text chat route returns HTTP 500. CloudWatch Logs for the assistant-chat Lambda show a `RuntimeClientError` from the AgentCore service, not a boto3 validation error. The error occurs after authentication and IAM succeed. Simultaneously, the iOS voice channel continues to work without error. Inspecting the runtime log group for the deployed AgentCore runtime shows `ERROR: No entrypoint defined`.

 **Root cause.** The deployed AgentCore runtime is configured for the bidirectional streaming (bidi/voice) path — its container command runs the Nova 2 Sonic bidi handler, which speaks WebSocket and has no `@app.entrypoint` decorated function. HTTP `InvokeAgentRuntime` calls arrive at a container that has no HTTP handler; the runtime reports that no entrypoint is defined and rejects the call. The voice channel is unaffected because it uses `InvokeAgentRuntimeWithWebSocketStream`, which the bidi container does handle.

This situation arises when the text chat route is wired to an existing bidi runtime ARN under the assumption that a single runtime serves both protocols. AgentCore runtimes are protocol-specific: a container serving the bidi/voice path cannot simultaneously serve HTTP text calls unless it explicitly registers both handlers.

 **Resolution.** 

1. Deploy a separate AgentCore runtime whose container entry point uses the HTTP handler (the `@app.entrypoint`-decorated function in the text-path application module). Use a naming convention that encodes the protocol — for example `vsa_supervisor_text_<stage>` versus `vsa_supervisor_bidi_<stage>` — so the protocol is unambiguous from the resource name.

1. After configuring the text runtime, verify that the `.bedrock_agentcore.yaml` configuration file uses relative paths for `entrypoint` and `source_path` (for example, `entrypoint: agents/supervisor/<handler>.py` and `source_path: .` relative to the repository root). When the AgentCore CLI resolves these to absolute paths scoped to a subdirectory, the container zip omits the parent package, causing an import error at runtime startup. Always redeploy from the repository root and confirm the YAML uses relative paths.

1. Update the Lambda that fronts the text chat route to target the new text runtime ARN, and expand the IAM grant on that Lambda to cover both the runtime ARN and its sub-resource path (`<arn>/*`). AgentCore evaluates `bedrock-agentcore:InvokeAgentRuntime` against `<runtime-arn>/runtime-endpoint/DEFAULT`, not the bare ARN; a grant covering only the bare ARN produces an `AccessDeniedException` on the actual invocation.

1. Thread any runtime-specific environment variables (persona configuration, Knowledge Base identifiers, memory IDs) into the text runtime container at deploy time. The text runtime does not inherit environment variables from the bidi runtime; each runtime must be configured independently.

1. Confirm that the Cognito user identity is delivered to the text runtime. The AgentCore HTTP unary path does not forward arbitrary custom request headers; pass the identity token as a field in the request payload rather than relying on a custom header to be forwarded by the platform.