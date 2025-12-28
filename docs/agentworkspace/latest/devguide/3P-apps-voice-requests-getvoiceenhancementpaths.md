# Get voice enhancement

model paths in Amazon Connect Agent Workspace

Returns the voice enhancements models static assets URL paths.

**Signature**

```
async getVoiceEnhancementPaths(): Promise<VoiceEnhancementPaths>
```

**Usage**

```
voiceClient.getVoiceEnhancementPaths();

// VoiceEnhancementPaths structure
interface VoiceEnhancementPaths {
  processors: string;
  workers: string;
  wasm: string;
  models: string;
}
```

**Permissions required:**

```
*
```
