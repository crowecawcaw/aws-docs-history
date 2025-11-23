# Built-in strategies

AgentCore Memory lets you add the following built-in memory strategies:

- Semantic memory strategy
- User preference memory strategy
- Summary strategy

###### Note

For semantic and user preference memory strategy, only [USER and
ASSISTANT role messages](../APIReference/API_Conversational.md "../APIReference/API_Conversational.md") are processed for long term memory extraction
and messages with rest of the role types are skipped. For summary strategy all roles
are processed.

Each memory strategy provides a structured output format tailored to its purpose. The
output is not uniform across strategies, because the type of information being stored
and retrieved differs:

- **Semantic memory strategy** returns facts as
  JSON objects, each representing a standalone personal fact about the
  user.
- **User preference memory strategy** returns JSON
  objects with context, preference, and categories, making it easier to capture
  user choices and decision patterns.
- **Summary strategy** returns XML-formatted
  output, where each `<topic>` tag represents a distinct area of
  the user's memory. XML lets multiple topics to be captured and organized in a
  single summary while preserving clarity.
  This maintains that each memory type exposes only the fields most relevant to its
  strategy. You can find the output format for semantic and user preference strategy in
  the extraction output schema and for summary strategy in the consolidation output
  schema.

###### Topics

- [Semantic memory strategy](semantic-memory-strategy.md "semantic-memory-strategy.md")
- [User preference memory strategy](user-preference-memory-strategy.md "user-preference-memory-strategy.md")
- [Summary strategy](summary-strategy.md "summary-strategy.md")
