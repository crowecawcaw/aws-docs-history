# Managing chat history

Amazon Nova 2 Sonic responses include ASR (Automatic Speech Recognition) transcripts for
both user and assistant voices. Storing chat history is a best practice—not only for
logging purposes but also for resuming sessions when the connection is unexpectedly
closed. This allows the client to send context back to Nova Sonic to continue the
conversation seamlessly.

## Sending chat history

A conversation history can be included only once, after the system/speech
prompt and before audio streaming begins. Overall chat history cannot be larger
than 40KB.

![](images/Sending-Chat-History_4.png)

Each historical message requires three events: `contentStart`,
`textInput` and `contentEnd`.

**Event schema per message:**

- `contentStart` - Defines the message role and
  configuration
- `textInput` - Contains the actual message content. One
  textInput cannot be larger than 1KB. If so, split into multiple
  textInputs in the same content block. If the conversation is larger than
  40KB, trim the overall chat history.
- `contentEnd` - Marks the end of the message

Repeat these three events for each message in your chat history, alternating
between USER and ASSISTANT roles.

**Important considerations:**

- Chat history can only be included once per session
- Chat history must be sent after the system prompt and before audio
  streaming begins
- All historical messages must be sent before starting the audio
  streaming
- Each message must specify either USER or ASSISTANT role
- Use the stored transcript content from textOutput events as the
  content value in textInput

## Receiving ASR transcripts

Amazon Nova 2 Sonic provides transcripts for both user speech and assistant
responses. These transcripts should be stored for chat history
management.

**User transcripts:** Appear in
`textOutput` events with `role: "USER"` and
`generationStage: "FINAL"`.

**Assistant transcripts:** Appear in
`textOutput` events with `role: "ASSISTANT"` and
`generationStage: "FINAL"` after audio generation
completes.

## Best practices

- Store transcripts from both USER and ASSISTANT roles
- Monitor total chat history size and trim if approaching 40KB
  limit
- Implement session recovery logic to resume conversations after
  disconnections
- Use FINAL transcripts for accurate chat history, not SPECULATIVE
  ones
