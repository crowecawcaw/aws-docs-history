# Extract information from documents with document

querying

###### Note

This section assumes that you’ve completed the section above [Prerequisites for document
querying](canvas-fm-chat-prereqs.md#canvas-fm-chat-prereqs-kendra "canvas-fm-chat-prereqs.md#canvas-fm-chat-prereqs-kendra").

Document querying is a feature that you can use while interacting with foundation
models in Canvas. With document querying, you can access a corpus of documents
stored in an Amazon Kendra _index_, which holds the contents of
your documents and is structured in a way to make documents searchable. You can ask
specific questions that are targeted to the data in your Amazon Kendra index, and the foundation
model returns answers to your questions. For example, you can query an internal
knowledge base of IT information and ask questions such as “How do I connect to my
company’s network?” For more information about setting up an index, see the [Amazon Kendra Developer
Guide](../../../kendra/latest/dg/what-is-kendra.md "../../../kendra/latest/dg/what-is-kendra.md").

When using the document query feature, the foundation models restrict their responses
to the content of the documents in your index with a technique called Retrieval
Augmented Generation (RAG). This technique bundles the most relevant information from
the index along with the user's prompt and sends it to the foundation model to get a
response. Responses are limited to what can be found in your index, preventing the model
from giving you incorrect responses based on external data. For more information about
this process, see the blog post [Quickly build high-accuracy Generative AI applications on enterprise
data](https://aws.amazon.com/blogs/machine-learning/quickly-build-high-accuracy-generative-ai-applications-on-enterprise-data-using-amazon-kendra-langchain-and-large-language-models/ "https://aws.amazon.com/blogs/machine-learning/quickly-build-high-accuracy-generative-ai-applications-on-enterprise-data-using-amazon-kendra-langchain-and-large-language-models/").

To get started, in a chat with a foundation model in Canvas, turn on the
**Document query** toggle at the top of the page. From the
dropdown, select the Amazon Kendra index that you want to query. Then, you can begin asking
questions related to the documents in your index.

###### Important

Document querying supports the [Compare model outputs](canvas-fm-chat-compare.md "canvas-fm-chat-compare.md") feature. Any existing chat history is
overwritten when you start a new chat to compare model outputs.
