# Event flow sequence

A typical conversation follows this event sequence:

1. **Session Start** - Initialize the
   conversation session
2. **System Prompt** - Send system
   instructions
3. **Chat History** (optional) - Provide
   conversation context
4. **Audio Chunks** - Stream user audio
   input
5. **Completion Start** - AI begins
   processing
6. **ASR Transcripts** (USER) - User speech
   transcription
7. **Tool Use** (optional) - AI requests tool
   execution
8. **Tool Handling** (optional) - Process and
   return tool results
9. **Transcript** (ASSISTANT) - SPECULATIVE -
   Preliminary AI response
10. **Audio Chunks** - Stream AI audio
    output
11. **Transcript** (ASSISTANT) - FINAL - Final AI
    response transcript
12. **Content End Audio** - Marks the end of
    audio content
13. **Prompt End** - Indicates the completion of
    the prompt processing
14. **Session End** - Close the
    conversation
