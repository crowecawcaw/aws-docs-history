# Unsubscribe from voice enhancement mode change events in Amazon Connect Customer agent workspace

Unsubscribes a callback function registered for voice enhancements mode changed
event.

**Signature**

```
offVoiceEnhancementModeChanged(handler: VoiceEnhancementModeChangedHandler)
```

**Usage**

```
const handler: VoiceEnhancementModeChangedHandler = async (data: VoiceEnhancementModeChanged) => {
  console.log("User VoiceEnhancementMode changed! " + data);
}

// subscribe a callback for mode change
voiceClient.onVoiceEnhancementModeChanged(handler);

// unsubsribes a callback for mode change
voiceClient.offVoiceEnhancementModeChanged(handler);
```

**Permissions required:**

```
*
```
