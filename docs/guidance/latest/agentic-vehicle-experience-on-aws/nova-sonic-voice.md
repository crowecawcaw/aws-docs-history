

# Amazon Nova 2 Sonic speech-to-speech voice
<a name="nova-sonic-voice"></a>

Amazon Nova 2 Sonic v2 (`amazon.nova-2-sonic-v1:0`) provides the speech-to-speech voice capability for AVX. It accepts PCM audio input and produces PCM audio output in a single bidirectional stream, with sub-700ms latency from end of user speech to first audio output token.

## Integration architecture
<a name="integration-architecture"></a>

Nova 2 Sonic is integrated through the Strands `BidiNovaSonicModel` class:

```
from strands.experimental.bidi.models.nova_sonic import (
    BidiNovaSonicModel,
    NOVA_SONIC_V2_MODEL_ID,
)

sonic_model = BidiNovaSonicModel(
    model_id=NOVA_SONIC_V2_MODEL_ID,      # 'amazon.nova-2-sonic-v1:0'
    provider_config={
        "audio": {
            "voice": "matthew",            # Nova 2 Sonic voice profile
            "input_rate": 16000,           # 16 kHz mono PCM input
            "output_rate": 24000,          # 24 kHz mono PCM output
        }
    },
    client_config={"region": "us-east-1"},  # Nova 2 Sonic v2 region
)

agent = BidiAgent(
    model=sonic_model,
    tools=tools,
    system_prompt=rendered_system_prompt,
    name="vsa-supervisor",
)
await agent.run(inputs=[input_callable], outputs=[output_callable])
```

Nova 2 Sonic is available in select Regions, including `us-west-2`. Deploy the voice runtime in a Region where it is available. The execution role’s Region, the Bedrock IAM grant’s foundation-model ARN and the `BidiNovaSonicModel` client Region must all match; the bidirectional stream rejects cross-Region invocation.

## Operational constraints — design around these
<a name="operational-constraints-design-around-these"></a>

The following constraints are platform-level properties of Nova 2 Sonic v2 and the AgentCore runtime. They are not bugs; they are characteristics you must design around in every tool, prompt, and session flow.


| Constraint | Value | Design implication | 
| --- | --- | --- | 
|  **Tool-completion window**  | \~1 second | Every tool called during a voice session must return within \~1s or Nova’s post-tool TTS goes silent. Do not make LLM calls inside tools. Return retrieved content and let Nova synthesize. Cache hot lookups at session-init. | 
|  **Trailing silence for end-of-turn detection**  | ≥ 1,600 ms | Audio inputs must include at least 1,600 ms of trailing silence for Nova’s voice activity detection (VAD) to reliably detect end of turn. Below this threshold, Nova accepts the audio but produces zero TTS output for the rest of the session. Audio fixtures and demo clips must encode this silence explicitly. | 
|  **AgentCore session-level timeout**  | 55 seconds | If no audio bytes or interactive content flows for 55 seconds, AgentCore closes the session with `InternalErrorCode=532`. Long-running tool chains must complete inside this window. Sessions that expect user think time need keep-alive activity. | 
|  ** `agent.send` re-entrancy from `output_callable` **  | Does not deliver | Calling `await agent.send(…​)` from inside the `output_callable` callback is silently dropped — a Strands re-entrancy constraint. Use `asyncio.create_task(agent.send(…​))` to schedule the send outside the callback’s call stack. | 
|  **Mid-response narration injection**  | Dropped as `{"interrupted": true}`  | Injecting text asynchronously while Nova is mid-response causes the injection to be dropped. Wait for the `bidi_response_complete` event before sending a narration injection. | 
|  **Nova 2 Sonic VAD sentence splitting**  | Splits on periods | Nova’s VAD treats internal periods as sentence boundaries and splits the turn. Audio fixture text must be a single sentence with no internal periods. Spell out DTC codes character by character (for example, "D T C P zero four two zero") to avoid Polly mis-pronunciation that Nova’s STT will mangle. | 

## Audio wire format
<a name="audio-wire-format"></a>


| Parameter | Value | 
| --- | --- | 
| Container | RIFF / WAV (header stripped before send; raw LPCM on the wire) | 
| Sample rate | 16,000 Hz (input); 24,000 Hz (output) | 
| Channels | Mono (1 channel) | 
| Bit depth | 16-bit signed little-endian PCM | 
| Chunk size | 100 ms per chunk (1,600 samples = 3,200 bytes) | 
| Trailing silence | ≥ 1,600 ms (2,000 ms recommended for reliability) | 

## Session lifecycle
<a name="session-lifecycle"></a>

A voice session follows this sequence:

1. Client sends `{"type": "session.start", "tenantId": "…​", "vin": "…​", "jwt": "…​"}` as the first WebSocket message.

1. The runtime resolves tenant and VIN, loads live vehicle state, runs the persona loader (cross-region Athena queries against the ADP data lake), and constructs the `BidiAgent`.

1.  `BidiAgent.run(inputs, outputs)` starts; queued audio chunks begin flowing.

1. Nova 2 Sonic VAD detects end of utterance after the trailing silence threshold.

1. The supervisor calls tools (Triage first, then routing-dependent specialists).

1. Nova synthesizes and streams the audio response.

1. Client sends `{"type": "session.end"}` when the caller hangs up or the session completes.

**Important**  
Do not send `session.end` immediately after the last audio chunk. The runtime’s `agent.run` loop must have time to process the trailing-silence frames and complete the VAD turn. A common symptom of premature `session.end` is a trace showing `bidi_connection_start` with no `bidi_usage` — the turn never processed.