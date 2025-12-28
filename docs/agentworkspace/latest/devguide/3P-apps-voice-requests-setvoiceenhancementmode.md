# Set the voice

enhancement mode in Amazon Connect Agent Workspace

Sets the voice enhancement mode of the user that's currently logged in to Amazon
Connect agent workspace. The voice enhancement mode can have the following values:

- `VOICE_ISOLATION`: it suppresses background noise and isolates the
  agent's voice. This mode should only be enabled if the agent uses a wired
  headsets.
- `NOISE_SUPPRESSION`: it suppresses the background noise. We
  recommend using this mode with any type of headset.
- `NONE`: no voice enhancement applies.

**Signature**

```
async setVoiceEnhancementMode(voiceEnhancementMode: VoiceEnhancementMode): Promise<void>
```

**Usage**

```
await voiceClient.setVoiceEnhancementMode(VoiceEnhancementMode.NOISE_SUPPRESSION);
```

**Input**

| **Parameter**                   | **Type**             | **Description**                                                                                    |
| ------------------------------- | -------------------- | -------------------------------------------------------------------------------------------------- |
| voiceEnhancementMode _Required_ | VoiceEnhancementMode | The mode to set on the user. Values accepted:<br>`VOICE_ISOLATION`, `NOISE_SUPPRESSION`,<br>`NONE` |

**Permissions required:**

```
*
```
