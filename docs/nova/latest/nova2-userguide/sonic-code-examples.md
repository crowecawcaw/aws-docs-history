# Code examples

These code examples help you quickly get started with Amazon Nova 2 Sonic. You can access the
complete list of examples in the [Amazon Nova Sonic GitHub samples](https://github.com/aws-samples/amazon-nova-samples/tree/main/speech-to-speech/amazon-nova-2-sonic "https://github.com/aws-samples/amazon-nova-samples/tree/main/speech-to-speech/amazon-nova-2-sonic") page.

## Getting started examples

For simple examples designed to get you started using Amazon Nova 2 Sonic, refer to the
following implementations:

- [Basic Nova Sonic implementation (Python)](https://github.com/aws-samples/amazon-nova-samples/blob/main/speech-to-speech/amazon-nova-2-sonic/sample-codes/console-python/nova_sonic_simple.py "https://github.com/aws-samples/amazon-nova-samples/blob/main/speech-to-speech/amazon-nova-2-sonic/sample-codes/console-python/nova_sonic_simple.py"): A basic
  implementation that demonstrates how events are structured in the
  bidirectional streaming API. This version does not support barge-in
  functionality (interrupting the assistant while it is speaking) and does not
  implement true bidirectional communication.
- [Full featured Nova Sonic implementation (Python)](https://github.com/aws-samples/amazon-nova-samples/blob/main/speech-to-speech/amazon-nova-2-sonic/sample-codes/console-python/nova_sonic_tool_use.py "https://github.com/aws-samples/amazon-nova-samples/blob/main/speech-to-speech/amazon-nova-2-sonic/sample-codes/console-python/nova_sonic_tool_use.py"): The
  full-featured implementation with real bidirectional communication and
  barge-in support. This allows for more natural conversations where users can
  interrupt the assistant while it is speaking, similar to human
  conversations.
- [Nova Sonic with tool use (Python)](https://github.com/aws-samples/amazon-nova-samples/blob/main/speech-to-speech/amazon-nova-2-sonic/sample-codes/console-python/nova_sonic_tool_use.py "https://github.com/aws-samples/amazon-nova-samples/blob/main/speech-to-speech/amazon-nova-2-sonic/sample-codes/console-python/nova_sonic_tool_use.py"): An advanced implementation
  that extends the bidirectional communication capabilities with tool use
  examples. This version demonstrates how Amazon Nova 2 Sonic can interact with
  external tools and APIs to provide enhanced functionality.
- [Nova Sonic with text and mixed Input (Python)](https://github.com/aws-samples/amazon-nova-samples/blob/main/speech-to-speech/amazon-nova-2-sonic/sample-codes/console-python/nova_sonic_with_text.py "https://github.com/aws-samples/amazon-nova-samples/blob/main/speech-to-speech/amazon-nova-2-sonic/sample-codes/console-python/nova_sonic_with_text.py"): Example implementation to showcase how Amazon Nova 2 Sonic can have text as an input.
- [Java WebSocket implementation (Java)](https://github.com/aws-samples/amazon-nova-samples/tree/main/speech-to-speech/amazon-nova-2-sonic/sample-codes/websocket-java "https://github.com/aws-samples/amazon-nova-samples/tree/main/speech-to-speech/amazon-nova-2-sonic/sample-codes/websocket-java"): This example implements a
  bidirectional WebSocket-based audio streaming application that integrates
  with Amazon Nova 2 Sonic for real-time speech-to-speech conversation using
  Java.
- [NodeJS Websocket implementation (NodeJS)](https://github.com/aws-samples/amazon-nova-samples/tree/main/speech-to-speech/amazon-nova-2-sonic/sample-codes/websocket-nodejs "https://github.com/aws-samples/amazon-nova-samples/tree/main/speech-to-speech/amazon-nova-2-sonic/sample-codes/websocket-nodejs"): This example
  implements a bidirectional WebSocket-based audio streaming application that
  integrates with Amazon Nova 2 Sonic for real-time speech-to-speech conversation
  using NodeJS.
- [NodeJS Websocket implementation (C#)](https://github.com/aws-samples/amazon-nova-samples/tree/main/speech-to-speech/amazon-nova-2-sonic/sample-codes/websocket-dotnet "https://github.com/aws-samples/amazon-nova-samples/tree/main/speech-to-speech/amazon-nova-2-sonic/sample-codes/websocket-dotnet"): This example
  implements a bidirectional WebSocket-based audio streaming application that
  integrates with Amazon Nova 2 Sonic for real-time speech-to-speech conversation
  using .NET.

## Advanced use cases

For advanced examples demonstrating more complex use cases, refer to the following
implementations:

- [Amazon Bedrock Knowledge Base implementation (NodeJS)](https://github.com/aws-samples/amazon-nova-samples/tree/main/speech-to-speech/amazon-nova-2-sonic/repeatable-patterns/bedrock-knowledge-base "https://github.com/aws-samples/amazon-nova-samples/tree/main/speech-to-speech/amazon-nova-2-sonic/repeatable-patterns/bedrock-knowledge-base"): This example
  demonstrates how to build an intelligent conversational application by
  integrating Amazon Nova 2 Sonic with Amazon Bedrock Knowledge Base using NodeJS.
- [Chat History Management (Python)](https://github.com/aws-samples/amazon-nova-samples/tree/main/speech-to-speech/amazon-nova-2-sonic/repeatable-patterns/chat-history-logger "https://github.com/aws-samples/amazon-nova-samples/tree/main/speech-to-speech/amazon-nova-2-sonic/repeatable-patterns/chat-history-logger"): This example includes a chat
  history logging system that captures and preserves all interactions between
  the user and Amazon Nova 2 Sonic using Python.
- [Hotel Reservation Cancellation (NodeJS)](https://github.com/aws-samples/amazon-nova-samples/tree/main/speech-to-speech/amazon-nova-2-sonic/repeatable-patterns/customer-service/hotel-cancellation-websocket "https://github.com/aws-samples/amazon-nova-samples/tree/main/speech-to-speech/amazon-nova-2-sonic/repeatable-patterns/customer-service/hotel-cancellation-websocket"): This example
  demonstrates a practical customer service use case for Amazon Nova 2 Sonic,
  implementing a hotel reservation cancellation system using NodeJS.
- [LangChain Knowledge Base integration (Python)](https://github.com/aws-samples/amazon-nova-samples/tree/main/speech-to-speech/amazon-nova-2-sonic/repeatable-patterns/langchain-knowledge-base "https://github.com/aws-samples/amazon-nova-samples/tree/main/speech-to-speech/amazon-nova-2-sonic/repeatable-patterns/langchain-knowledge-base"): This
  implementation demonstrates how to integrate Amazon Nova 2 Sonic speech-to-speech
  capabilities with a LangChain-powered knowledge base for enhanced
  conversational experiences using Python.
- [Conversation Resumption (NodeJS)](https://github.com/aws-samples/amazon-nova-samples/tree/main/speech-to-speech/amazon-nova-2-sonic/repeatable-patterns/resume-conversation "https://github.com/aws-samples/amazon-nova-samples/tree/main/speech-to-speech/amazon-nova-2-sonic/repeatable-patterns/resume-conversation"): This example demonstrates how
  to implement conversation resumption capabilities with Amazon Nova 2 Sonic. Using a
  hotel reservation cancellation scenario as the context, the application
  shows how to maintain conversation state across sessions, allowing users to
  seamlessly continue interactions that were previously interrupted using
  NodeJS.
- [Nova 2 Sonic Speaks First (NodeJS)](https://github.com/aws-samples/amazon-nova-samples/tree/main/speech-to-speech/amazon-nova-2-sonic/repeatable-patterns/nova-sonic-speaks-first "https://github.com/aws-samples/amazon-nova-samples/tree/main/speech-to-speech/amazon-nova-2-sonic/repeatable-patterns/nova-sonic-speaks-first"): This example demonstrates how
  Amazon Nova 2 Sonic can initiate conversations proactively.
- [Session Continuation (NPython)](https://github.com/aws-samples/amazon-nova-samples/tree/main/speech-to-speech/amazon-nova-2-sonic/repeatable-patterns/session-continuation/console-python "https://github.com/aws-samples/amazon-nova-samples/tree/main/speech-to-speech/amazon-nova-2-sonic/repeatable-patterns/session-continuation/console-python"): This example demonstrates how to enable unlimited conversation length with Amazon Nova 2 Sonic by implementing seamless session transitions. The application automatically creates and switches to new sessions in the background, allowing conversations to continue indefinitely without interruption or context loss.

## Hands-on workshop

A hands-on workshop is available that guides you through building a voice chat
application using Amazon Nova 2 Sonic with a bidirectional streaming interface. You can
[access the workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/5238419f-1337-4e0f-8cd7-02239486c40d/en-US "https://catalog.us-east-1.prod.workshops.aws/workshops/5238419f-1337-4e0f-8cd7-02239486c40d/en-US") and find the [complete code examples](https://github.com/aws-samples/amazon-nova-samples/tree/main/speech-to-speech/workshops "https://github.com/aws-samples/amazon-nova-samples/tree/main/speech-to-speech/workshops").
