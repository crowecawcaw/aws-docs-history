# Test your knowledge base with queries and responses

After you set up your knowledge base, you can test its behavior in the following ways:

- Send queries and retrieving relevant information from your data sources, by using the [Retrieve](../APIReference/API_agent-runtime_Retrieve.md "../APIReference/API_agent-runtime_Retrieve.md") operation.
- Send queries and generate responses to the queries based on the retrieved information from your data sources, by using the [RetrieveAndGenerate](../APIReference/API_agent-runtime_RetrieveAndGenerate.md "../APIReference/API_agent-runtime_RetrieveAndGenerate.md") operation.
- Use a reranking model over the default Amazon Bedrock Knowledge Bases reranking model to retrieve more relevant sources when using either [Retrieve](../APIReference/API_agent-runtime_Retrieve.md "../APIReference/API_agent-runtime_Retrieve.md") or [RetrieveAndGenerate](../APIReference/API_agent-runtime_RetrieveAndGenerate.md "../APIReference/API_agent-runtime_RetrieveAndGenerate.md").
- Use optional metadata filters with the `Retrieve` or `RetrieveAndGenerate`
  API to specify which documents in your data source can be used.
  When you are satisfied with your knowledge base's behavior, you can then set up your application to query the knowledge base or attach the knowledge base to an agent by proceeding to [Deploy your knowledge base for your AI application](knowledge-base-deploy.md "knowledge-base-deploy.md").

Select a topic to learn more about it.

###### Topics

- [Query a knowledge base and retrieve data](kb-test-retrieve.md "kb-test-retrieve.md")
- [Query a knowledge base and generate responses based off the retrieved data](kb-test-retrieve-generate.md "kb-test-retrieve-generate.md")
- [Generate a query for structured data](knowledge-base-generate-query.md "knowledge-base-generate-query.md")
- [Query a knowledge base connected to an Amazon Kendra GenAI index](kb-test-kendra.md "kb-test-kendra.md")
- [Query a knowledge base connected to an Amazon Neptune Analytics graph](kb-test-neptune.md "kb-test-neptune.md")
- [Configure and customize queries and response
  generation](kb-test-config.md "kb-test-config.md")
- [Configure response generation for reasoning models with Knowledge Bases](kb-test-configure-reasoning.md "kb-test-configure-reasoning.md")
