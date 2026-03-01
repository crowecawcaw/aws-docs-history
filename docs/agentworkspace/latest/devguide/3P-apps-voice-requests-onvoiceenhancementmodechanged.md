# Subscribe to voice enhancement mode change events in Amazon Connect Agent Workspace

Subscribes a callback function whenever voice enhancements mode is changed in user's
profile.

**Signature**

```
onVoiceEnhancementModeChanged(handler: VoiceEnhancementModeChangedHandler)
```

**Usage**

```
const handler: VoiceEnhancementModeChangedHandler = async (data: VoiceEnhancementModeChanged) => {
  console.log("User VoiceEnhancementMode changed! " + data);
}

voiceClient.onVoiceEnhancementModeChanged(handler);

// VoiceEnhancementModeChanged structure
{
  voiceEnhancementMode: string
  previous: {
     voiceEnhancementMode: string
  }
}
```

**Permissions required:**

```
*
```
