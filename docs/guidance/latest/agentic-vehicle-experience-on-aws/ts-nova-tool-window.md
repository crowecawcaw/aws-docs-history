

# Nova 2 Sonic goes silent after a tool call that takes too long
<a name="ts-nova-tool-window"></a>

 **Symptom.** During a voice session the agent accepts the user’s utterance, begins processing, invokes a tool, receives the tool result, and then produces no speech output — the TTS narration is silently dropped. From the caller’s perspective the agent appears to have understood the question but refuses to answer. The bidi stream stays open; no error is returned to the client. Subsequent turns in the same session may also produce no speech, or the session may recover if a fast tool is invoked next.

 **Root cause.** Nova 2 Sonic’s speech-to-speech pipeline has an internal \~1-second tool-completion window. If a tool call takes longer than approximately one second to return, Nova’s post-tool narration injection is silently discarded. Sub-agent tools that invoke a language model synchronously (Claude Sonnet ≈ 3 s, Haiku ≈ 2 s) routinely exceed this budget. The tool technically succeeds and its result is available; only the voice narration is lost.

 **Resolution.** 

1. Audit every tool registered on the supervisor for its worst-case latency. Time the tool end-to-end under realistic load, including cold-start of any downstream API.

1. For tools that invoke a language model, restructure the tool to return the retrieved or processed content directly to Nova rather than synthesizing a response inside the tool. Nova synthesizes the final voice reply; the tool’s job is to surface facts, not to narrate them. This is the "sub-agent-as-content-returner" pattern: the tool calls the KB or runs the query, returns raw context, and lets Nova compose the answer.

1. For tools whose latency cannot be reduced below the \~1-second budget, add an in-process cache keyed on the tool’s logical input. Vehicle state lookups, diagnostic interpretations, and service-center queries are good candidates: the result changes slowly relative to a voice session’s duration, so a session-scoped cache with a 30–60 second TTL adds no visible staleness while keeping tool latency well under 100 ms on cache hits.

1. Do not rely on Nova recovering the narration in a subsequent turn. If the tool window is exceeded, the narration for that turn is permanently lost. Design for the constraint, not around it.