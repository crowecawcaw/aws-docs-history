# Speech models

When errors occur, we recommend trying the following steps:

1. Send the `promptEnd` event.
2. Send the `sessionEnd` event.
3. If the audio streaming has started, also send the `contentEnd` event.
   Completing these steps also frees GPU resources and memory.

When handling long conversations or recovering from errors, you can implement conversation resumption using the following approach:

1.  Set up chat history storage to preserve conversation context from previous interactions. You can find chat history example in our [Amazon Nova samples Github repo](https://github.com/aws-samples/amazon-nova-samples/tree/main/speech-to-speech/repeatable-patterns/chat-history-logger "https://github.com/aws-samples/amazon-nova-samples/tree/main/speech-to-speech/repeatable-patterns/chat-history-logger").
2.  Handle conversation timeouts proactively:
    - When approaching the maximum connection duration, end the current request and start a new one.
    - Include the saved chat history in the new request to maintain conversation continuity.

3.  Format resumed conversations properly:

        * Place the chat history after the system prompt but before any new user input.
        * Include previous messages with the proper user and assistant roles.
        * Ensure that the first message in the chat history is from the user.

    You can find chat resumption example in our [Amazon Nova samples Github repo](https://github.com/aws-samples/amazon-nova-samples/tree/main/speech-to-speech/repeatable-patterns/resume-conversation "https://github.com/aws-samples/amazon-nova-samples/tree/main/speech-to-speech/repeatable-patterns/resume-conversation").

###### When to use conversation resumption

The conversation resumption approach is particularly helpful for error recovery in the following scenarios:

- After you receive a `ModelTimeoutException` with the message "Model has timed out in processing the request".
- When you need to restore context after an unexpected disconnection.
