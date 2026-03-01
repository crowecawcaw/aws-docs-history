# Agentic Retrieval Augmented Generation (RAG) in Amazon Q Business

Agentic RAG enhances the standard RAG workflow of Amazon Q Business with agentic
retrieval and response capabilities. Unlike standard RAG's document retrieval and simple
response generation process, Agentic RAG uses multiple intelligent agents and
specialized data retrieval tools to deliver more comprehensive and accurate responses
while maintaining conversation context.

With Agentic RAG system processes queries through a combination of the following
coordinated steps:

- Analyzes both the user's question and conversation history and determines
  which retrieval tools to use
- Intelligently deconstructs complex queries into simpler ones
- Intelligently triggers multiple data retrieval tools as needed
- Provides disambiguating questions based on enterprise data to clarify user
  intent
- Synthesizes information from various sources, and generates responses with its
  underlying large language model
- Provides follow-up questions to intelligently continue the conversation
  Throughout this process, it continuously checks response quality and activates
  additional data retrieval tools when necessary, showing users real-time progress to the
  user as it processes queries. All responses maintain existing permissions and include
  clear citations to source material.

Agentic RAG delivers several key improvements over standard RAG. It intelligently
selects from available retrieval tools based on query requirements and performs multiple
retrieval operations for complex queries. The system maintains conversation context
awareness and adapts response generation through retries or disambiguation techniques
based on the quality of retrieved information and the subsequent response generated.
These capabilities result in higher accuracy, more comprehensive information gathering,
and better handling of complex, multi-faceted queries.

To use Agentic RAG, enable the feature using the **Advanced search**
toggle in your web experience interface.

###### Note

While the Agentic RAG system provides more thorough responses, response times may
be longer than standard RAG due to its multiple retrieval operations.
