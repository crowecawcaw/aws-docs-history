

# Voice session ends prematurely; agent does not respond to full utterances
<a name="ts-trailing-silence"></a>

 **Symptom.** During a Nova 2 Sonic voice session the agent consistently fails to respond to complete utterances, or responds to only the first part of a sentence before cutting off. The behavior is intermittent — it worsens when the user speaks slowly, pauses mid-sentence, or speaks in an environment with low background noise. Inspecting the bidi stream shows that the `end_of_turn` event fires before the user has finished speaking, causing Nova to process a partial utterance and either produce an incorrect response or produce no response.

 **Root cause.** Nova 2 Sonic’s end-of-turn detection requires a minimum of approximately 1600 milliseconds of trailing silence after the last speech content to reliably detect that the speaker has finished. Audio streams that inject trailing silence shorter than this threshold cause Nova to accept the audio, process the tool result, and begin narration injection, but produce zero TTS output for the rest of the session. The threshold is a property of the Nova 2 Sonic model’s voice-activity detection, not of the transport layer or the AgentCore runtime.

This constraint also affects programmatic audio injection in test or demo harnesses: if a test client injects a pre-recorded utterance followed by fewer than 1600 ms of silence, end-of-turn detection is unreliable and the test produces inconsistent results.

 **Resolution.** 

1. Configure the audio client to append at least 1600 ms of silence — preferably 2000 ms to provide headroom — after the last detected speech segment before signaling end-of-turn. The reference iOS client uses a `trailingSilenceChunks` value of 10 (20 ms per chunk, totaling 200 ms), which is calibrated to a specific voice-activity detector; adjust this value to produce at least 1600 ms of silence when multiplied by the audio chunk duration.

1. For automated test or demo harnesses that inject pre-recorded audio, append a silent audio segment of at least 2000 ms after each utterance clip. Do not rely on the natural end of the WAV file as a silence marker; explicitly construct and append a silent chunk of the appropriate duration.

1. Verify the fix by inspecting the bidi stream’s `end_of_turn` event timing relative to the last non-silent audio chunk. The event should fire at least 1600 ms after the last speech-containing chunk. If end-of-turn fires earlier, increase the trailing silence padding.

1. Below the 1600 ms threshold the failure mode is session-wide, not turn-level: once Nova fails to produce TTS for a turn due to insufficient trailing silence, subsequent turns in the same session may also produce no TTS output. If a voice session produces no audio after the first non-trivial tool call, check the trailing silence configuration before investigating other causes.