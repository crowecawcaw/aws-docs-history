

# Handling output events with the bidirectional API
<a name="sonic-output-events"></a>

When the Amazon Nova Sonic model responds, it follows a structured event sequence. The flow begins with a `completionStart` event that contains unique identifiers like `sessionId`, `promptName`, and `completionId`. These identifiers are consistent throughout the response cycle and unite all subsequent response events.

## Overview
<a name="sonic-output-overview"></a>

Each response type follows a consistent three-part pattern: `contentStart` defines the content type and format, the actual content event, and `contentEnd` closes that segment. The response typically includes multiple content blocks in sequence: automatic speech recognition (ASR) transcription (what the user said), optional tool use (when external information is needed), text response (what the model plans to say), and audio response (the spoken output).

## Response Content Types
<a name="sonic-response-content-types"></a>

### ASR Transcription
<a name="sonic-asr-transcription"></a>

The ASR transcription appears first, delivering the model's understanding of the user's speech with `role: "USER"` and `"additionalModelFields": "{\"generationStage\":\"FINAL\"}"` in the `contentStart`.

### Tool Use
<a name="sonic-tool-use-response"></a>

When the model needs external data, it sends tool-related events with specific tool names and parameters.

### Text Response
<a name="sonic-text-response"></a>

The text response provides a preview of the planned speech with `role: "ASSISTANT"` and `"additionalModelFields": "{\"generationStage\":\"SPECULATIVE\"}"`.

### Audio Response
<a name="sonic-audio-response"></a>

The audio response then delivers base64-encoded speech chunks sharing the same `contentId` throughout the stream.

## Barge-In Support
<a name="sonic-barge-in-support"></a>

During audio generation, Amazon Nova Sonic supports natural conversation flow through its barge-in capability. When a user interrupts Amazon Nova Sonic while it's speaking, Nova Sonic immediately stops generating speech, switches to listening mode, and sends a content notification indicating the interruption has occurred. Because Nova Sonic operates faster than real-time, some audio may have already been delivered but not yet played. The interruption notification enables the client application to clear its audio queue and stop playback immediately, creating a responsive conversational experience.

## Final Transcription
<a name="sonic-final-transcription"></a>

After audio generation completes (or is interrupted via barge-in), Amazon Nova Sonic provides an additional text response that contains a sentence-level transcription of what was actually spoken. This text response includes a `contentStart` event with `role: "ASSISTANT"` and `"additionalModelFields": "{\"generationStage\":\"FINAL\"}"`.

## Usage Tracking
<a name="sonic-usage-tracking"></a>

Throughout the response handling, `usageEvent` events are sent to track token consumption. These events contain detailed metrics on input tokens and output tokens (both speech and text), and their cumulative totals. Each `usageEvent` maintains the same `sessionId`, `promptName`, and `completionId` as other events in the conversation flow. The details section provides both incremental changes (delta) and running totals of token usage, enabling precise monitoring of the usage during the conversation.

## Completion
<a name="sonic-completion"></a>

The model sends a `completionEnd` event with the original identifiers and a `stopReason` that indicates how the conversation ended. This event hierarchy ensures your application can track which parts of the response belong together and process them accordingly, maintaining conversation context throughout multiple turns.

The output event flow begins by entering the response generation phase. It starts with automatic speech recognition, selects a tool for use, transcribes speech, generates audio, finalizes the transcription, and finishes the session.

![Flow diagram showing conversation stages from Start through ASR, tool handling, text and audio responses, to End with associated events.](http://docs.aws.amazon.com/nova/latest/nova2-userguide/images/Output-Event -Flow_3.png)


## Output Event Flow
<a name="sonic-output-event-flow"></a>

The structure of the output event flow is described in this section.

### 1. UsageEvent
<a name="sonic-usage-event"></a>

```
"event": {
    "usageEvent": {
        "completionId": "string", // unique identifier for completion
        "details": {
            "delta": { // incremental changes since last event
                "input": {
                    "speechTokens": number, // input speech tokens
                    "textTokens": number // input text tokens
                },
                "output": {
                    "speechTokens": number, // speech tokens generated
                    "textTokens": number // text tokens generated
                }
            },
            "total": { // cumulative counts
                "input": {
                    "speechTokens": number, // total speech tokens processed
                    "textTokens": number // total text tokens processed
                },
                "output": {
                    "speechTokens": number, // total speech tokens generated
                    "textTokens": number // total text tokens generated
                }
            }
        },
        "promptName": "string", // same unique identifier from promptStart event
        "sessionId": "string", // unique identifier
        "totalInputTokens": number, // cumulative input tokens
        "totalOutputTokens": number, // cumulative output tokens
        "totalTokens": number // total tokens in the session
    }
}
```

### 2. CompleteStartEvent
<a name="sonic-completion-start-event"></a>

```
"event": {
    "completionStart": {
        "sessionId": "string", // unique identifier
        "promptName": "string", // same unique identifier from promptStart event
        "completionId": "string", // unique identifier
    }
}
```

### 3. TextOutputContent
<a name="sonic-text-output-content"></a>

#### ContentStart
<a name="sonic-text-output-content-start"></a>

```
"event": {
    "contentStart": {
        "additionalModelFields": "{\"generationStage\":\"FINAL\"}" | "{\"generationStage\":\"SPECULATIVE\"}",
        "sessionId": "string", // unique identifier
        "promptName": "string", // same unique identifier from promptStart event
        "completionId": "string", // unique identifier
        "contentId": "string", // unique identifier for the content block
        "type": "TEXT",
        "role": "USER" | "ASSISTANT",
        "textOutputConfiguration": {
            "mediaType": "text/plain"
        }
    }
}
```

#### TextOutput
<a name="sonic-text-output"></a>

```
"event": {
    "textOutput": {
        "sessionId": "string", // unique identifier
        "promptName": "string", // same unique identifier from promptStart event
        "completionId": "string", // unique identifier
        "contentId": "string", // same unique identifier from its contentStart
        "content": "string" // User transcribe or Text Response
    }
}
```

#### ContentEnd
<a name="sonic-text-output-content-end"></a>

```
"event": {
    "contentEnd": {
        "sessionId": "string", // unique identifier
        "promptName": "string", // same unique identifier from promptStart event
        "completionId": "string", // unique identifier
        "contentId": "string", // same unique identifier from its contentStart
        "stopReason": "PARTIAL_TURN" | "END_TURN" | "INTERRUPTED",
        "type": "TEXT"
    }
}
```

### 4. ToolUse
<a name="sonic-tool-use-output"></a>

#### ContentStart
<a name="sonic-tool-use-content-start"></a>

```
"event": {
    "contentStart": {
        "sessionId": "string", // unique identifier
        "promptName": "string", // same unique identifier from promptStart event
        "completionId": "string", // unique identifier
        "contentId": "string", // unique identifier for the content block
        "type": "TOOL",
        "role": "TOOL",
        "toolUseOutputConfiguration": {
            "mediaType": "application/json"
        }
    }
}
```

#### ToolUse
<a name="sonic-tool-use-event"></a>

```
"event": {
    "toolUse": {
        "sessionId": "string", // unique identifier
        "promptName": "string", // same unique identifier from promptStart event
        "completionId": "string", // unique identifier
        "contentId": "string", // same unique identifier from its contentStart
        "content": "json",
        "toolName": "string",
        "toolUseId": "string"
    }
}
```

#### ContentEnd
<a name="sonic-tool-use-content-end"></a>

```
"event": {
    "contentEnd": {
        "sessionId": "string", // unique identifier
        "promptName": "string", // same unique identifier from promptStart event
        "completionId": "string", // unique identifier
        "contentId": "string", // same unique identifier from its contentStart
        "stopReason": "TOOL_USE",
        "type": "TOOL"
    }
}
```

### 5. AudioOutputContent
<a name="sonic-audio-output-content"></a>

#### ContentStart
<a name="sonic-audio-output-content-start"></a>

```
"event": {
    "contentStart": {
        "sessionId": "string", // unique identifier
        "promptName": "string", // same unique identifier from promptStart event
        "completionId": "string", // unique identifier
        "contentId": "string", // unique identifier for the content block
        "type": "AUDIO",
        "role": "ASSISTANT",
        "audioOutputConfiguration": {
            "mediaType": "audio/lpcm",
            "sampleRateHertz": 8000 | 16000 | 24000,
            "sampleSizeBits": 16,
            "encoding": "base64",
            "channelCount": 1
        }
    }
}
```

#### AudioOutput
<a name="sonic-audio-output-event"></a>

```
"event": {
    "audioOutput": {
        "sessionId": "string", // unique identifier
        "promptName": "string", // same unique identifier from promptStart event
        "completionId": "string", // unique identifier
        "contentId": "string", // same unique identifier from its contentStart
        "content": "base64EncodedAudioData", // Audio
    }
}
```

#### ContentEnd
<a name="sonic-audio-output-content-end"></a>

```
"event": {
    "contentEnd": {
        "sessionId": "string", // unique identifier
        "promptName": "string", // same unique identifier from promptStart event
        "completionId": "string", // unique identifier
        "contentId": "string", // same unique identifier from its contentStart
        "stopReason": "PARTIAL_TURN" | "END_TURN",
        "type": "AUDIO"
    }
}
```

### 6. CompletionEndEvent
<a name="sonic-completion-end-event"></a>

```
"event": {
    "completionEnd": {
        "sessionId": "string", // unique identifier
        "promptName": "string", // same unique identifier from promptStart event
        "completionId": "string", // unique identifier
        "stopReason": "END_TURN" 
    }
}
```