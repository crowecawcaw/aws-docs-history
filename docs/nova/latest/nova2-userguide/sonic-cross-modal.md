# Cross-modal input

Amazon Nova 2 Sonic now supports cross-modal input, allowing you to send text messages
in addition to voice input during a conversation session. While speech remains the
primary mode of interaction, text input provides flexibility for scenarios where
typing is more convenient or appropriate.

**Continuous streaming required**: Cross-modal input
requires an active streaming session to function properly. The session must maintain
continuous streaming like a regular voice session, otherwise standard session
timeouts will be applied and the connection will be terminated.

Sensitivity levels in cross-modal text input is useful for scenarios such
as:

- Client-side app integration (web and mobile): Allows users to interact
  with the application using both text and voice, supporting seamless
  multimodal experiences.
- "Model-start-first" use case: A text message can be sent immediately after
  the session starts to prompt the model to begin speaking.
- Guiding the model during async tool calling: When a toolUse event is
  triggered and the system begins processing tool calls, the client can send a
  text message to Sonic to provide a natural response while waiting — such as,
  “Hold on a second while I process your information. In the meantime, is
  there anything else I can assist with?”
- Telephony DTMF integration: Customer uses phone keypad to enter sensitive
  information (such as credit card numbers). Note: Amazon Nova Sonic does not
  process DTMF tones natively. To support DTMF input, your system must detect
  the tones, convert them to text (such as "1234"), and send to Nova 2
  Sonic.

## How it works

Cross-modal input uses a three-event sequence similar to audio input:

1. **Content Start Event:** Signals the
   beginning of text input
2. **Text Input Event:**Contains the actual
   text message
3. **Content End Event:** Signals the
   completion of text input

All three events must use the same promptName and contentName to maintain the
sequence. A new UUID should be generated for contentName each time you send text
input to ensure proper multi-turn conversation tracking.

## Event structure

Initiates the text input sequence with configuration details:

```
{
  "event": {
    "contentStart": {
      "promptName": "<prompt_name>",
      "contentName": "<new_content_name>",
      "role": "USER",
      "type": "TEXT",
      "interactive": true,
      "textInputConfiguration": {
        "mediaType": "text/plain"
      }
    }
  }
}
```

Key Parameters:

- `promptName`:The name of your conversation prompt
  (consistent across the session)
- `contentName`: A unique identifier for this text
  input (generate a new UUID for each message)
- `role`: Set to `"USER"` to indicate user
  input
- `type`: Set to `"TEXT"` for text
  input
- `interactive`: Set to `true` to enable
  interactive mode
- `mediaType`: Set to `"text/plain"` for
  plain text content
  Contains the actual text message content:

```
{
  "event": {
    "textInput": {
      "promptName": "<prompt_name>",
      "contentName": "<new_content_name>",
      "content": "<your_text_message>"
    }
  }
}
```

Key Parameters:

- `promptName`: Must match the value from Content
  Start Event
- `contentName`: Must match the value from Content
  Start Event
- `role`: Your text message string
  Signals the completion of the text input:

```
{
  "event": {
    "contentEnd": {
      "promptName": "<prompt_name>",
      "contentName": "<new_content_name>"
    }
  }
}
```

Key Parameters:

- `promptName`: Must match the value from previous
  events
- `contentName`: Must match the value from previous
  events
