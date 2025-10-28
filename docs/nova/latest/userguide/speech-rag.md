# Implementing RAG

Retrieval-Augmented Generation (RAG) enhances responses by retrieving and incorporating information from your knowledge bases. With Amazon Nova Sonic, RAG is implemented through tool use.

## Knowledge base implementation outline

Implementing a RAG requires the following elements:

- **Configure the tool** - Define a knowledge base search tool in your `promptStart` event.
- **Receive Tool Use Request** - When the user asks a question, the model will call the knowledge base tool.
- **Query Vector Database** - Execute the search query against your vector database.
- **Return Results** - Send the search results back to the model.
- **Generate Response** - The model incorporates the retrieved information in its spoken response.

## Knowledge base configuration

Here is an example configuration of a basic knowledge base tool:

```
{
     toolSpec: {
         name: "knowledgeBase",
         description: "Search the company knowledge base for information",
         inputSchema: {
             json: JSON.stringify({
                 type: "object",
                 properties: {
                     query: {
                         type: "string",
                         description: "The search query to find relevant information"
                     }
                 },
                 required: ["query"]
             })
         }
     }
 };
```
