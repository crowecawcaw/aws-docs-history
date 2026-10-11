

# Text chat returns HTTP 500 with `ParamValidationError` on every request
<a name="ts-session-id-length"></a>

 **Symptom.** The web UI’s text chat route (`/assistant/chat`) returns HTTP 500 on every request. CloudWatch Logs for the assistant-chat Lambda show `botocore.exceptions.ParamValidationError` referencing `runtimeSessionId`: the value fails the `Length Constraints: Minimum length of 33` check. The error is deterministic — every browser session from this client fails, while sessions from a different client or a direct API call with a longer session ID succeed.

 **Root cause.** The AgentCore `InvokeAgentRuntime` API enforces a minimum session ID length of 33 characters and a pattern of `[a-zA-Z0-9][a-zA-Z0-9-]*<timestamp>_<rand>` scheme that produces 31 characters — every call fails at the SDK validation layer before reaching the AgentCore service. The error is caught in Lambda and returned as a 500 to the client.

 **Resolution.** 

1. Add a padding step in the assistant-chat Lambda handler that extends any session ID shorter than 33 characters to exactly 33 characters before passing it to `invoke_agent_runtime`. Use a deterministic pad (for example, appending `x` characters) so that the same browser session always maps to the same upstream AgentCore session, preserving AgentCore Memory continuity:

   ```
   _MIN_RUNTIME_SESSION_LEN = 33
   runtime_session_id = session_id
   if len(runtime_session_id) < _MIN_RUNTIME_SESSION_LEN:
       pad_len = _MIN_RUNTIME_SESSION_LEN - len(runtime_session_id)
       runtime_session_id = f"{session_id}-{'x' * (pad_len - 1)}"
   ```

1. Return the original, unpadded session ID to the caller in the response body. The padding is an internal implementation detail; the client should not need to adapt.

1. In the web client, update the session ID generator to produce IDs of at least 33 characters by default, so the handler-side pad is a safety net rather than the primary fix.

1. Add a unit test that asserts the padded ID is at least 33 characters long, that the caller’s original session ID appears as a prefix, and that the padded form satisfies the allowed character pattern. Regression-test both the short-ID and already-long-ID paths.