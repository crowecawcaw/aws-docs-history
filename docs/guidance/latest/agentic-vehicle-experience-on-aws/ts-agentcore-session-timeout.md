

# AgentCore session terminates with error code 532 during idle pauses
<a name="ts-agentcore-session-timeout"></a>

 **Symptom.** A voice or bidirectional streaming session that has been idle — no audio bytes arriving from the client, no tool calls in flight — terminates unexpectedly. The AgentCore runtime returns `InternalErrorCode=532`. Short sessions and continuously active sessions are unaffected; the failure is reproducible when the caller pauses for more than approximately 55 seconds without sending any interactive content.

 **Root cause.** AgentCore enforces a 55-second session-level idle timeout on gaps between audio bytes or interactive content events. This is a platform constraint, not a configurable parameter. The timeout fires regardless of whether the caller holds the connection open. Use cases that legitimately require longer thinking pauses — for example, a driver reviewing a diagnostic explanation before responding — will hit this window if no keep-alive mechanism is in place.

 **Resolution.** 

1. Implement a keep-alive heartbeat in the client that sends a minimal audio event (a short silent audio chunk) to the bidi runtime at an interval shorter than the 55-second timeout — a 30-second interval provides adequate headroom. The iOS reference client uses `DemoAudioInjector.trailingSilenceChunks` for a related purpose; the same mechanism can emit periodic keep-alive chunks during pauses.

1. For the text-channel (HTTP `InvokeAgentRuntime`), session continuity is stateless per call; there is no persistent connection to time out. The 55-second constraint applies only to the bidirectional streaming (bidi/voice) path.

1. Design voice interaction flows so that Nova provides ongoing verbal feedback — a "thinking" phrase or a partial narration — during long tool calls or multi-step orchestration. This activity counts as interactive content and resets the idle window.

1. Monitor CloudWatch Logs for the runtime log group for `InternalErrorCode=532` events. If the rate rises, tighten the keep-alive interval or add turn-level verbal pacing in the supervisor system prompt.