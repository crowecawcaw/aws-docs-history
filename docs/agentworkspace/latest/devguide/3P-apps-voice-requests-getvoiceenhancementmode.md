# Get the voice enhancement mode in Amazon Connect Agent Workspace

Gets the voice enhancement mode of the user that's currently logged in to Amazon
Connect agent workspace. The voice enhancement mode can have the following values:

- `VOICE_ISOLATION`: it suppresses background noise and isolates the
  agent's voice. This mode should only be enabled if the agent uses a wired
  headsets.
- `NOISE_SUPPRESSION`: it suppresses the background noise. We
  recommend using this mode with any type of headset.
- `NONE`: no voice enhancement applies.

**Signature**

```
async getVoiceEnhancementMode(): Promise<VoiceEnhancementMode>
```

**Usage**

```
const voiceEnhancementMode: VoiceEnhancementMode = await voiceClient.getVoiceEnhancementMode();
```

**Permissions required:**

```
*
```
