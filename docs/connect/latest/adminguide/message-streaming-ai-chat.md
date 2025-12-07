# Enable message streaming for AI-powered

chat

Amazon Connect supports message streaming for AI-powered chat interactions. Responses from AI
agents appear progressively as they're generated, improving the customer experience
during conversations.

The following are integration options, along with features of each option:

- Amazon Connect agents
  - Eliminates Amazon Lex timeout limitations
  - Provides fulfillment messages during processing (such as "One moment
    while I review your account")
  - Displays partial responses with progressive text (growing text
    bubble)

- Third-party bots via Amazon Lex, Lambda, or the [CreateParticipant](../APIReference/API_CreateParticipant.md "../APIReference/API_CreateParticipant.md") API
  - Eliminates Amazon Lex timeout limitations
  - Standard bot response behavior
