

Amazon Kendra is no longer open to new customers. For capabilities similar to Amazon Kendra, explore Amazon Bedrock Knowledge Bases. [Learn more](https://docs.aws.amazon.com/kendra/latest/dg/kendra-availability-change.html).

# How Amazon Kendra works
<a name="how-it-works"></a>

Amazon Kendra provides search and Retrieval Augmented Generation (RAG) functionality for your application. It indexes your documents directly—or from your third-party document repository—and intelligently serves relevant information to your users. You can use Amazon Kendra to create an updatable index of documents of a variety of types. For a list of document types supported by Amazon Kendra, see [Types of documents](https://docs.aws.amazon.com/kendra/latest/dg/index-document-types.html).

Amazon Kendra integrates with other services. You can connect an Amazon Kendra GenAI Enterprise Edition index to [Amazon Q Business](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/what-is.html) and [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) for creating your RAG chat solution. Or, you can power [Amazon Lex chat bots](https://docs.aws.amazon.com/lexv2/latest/dg/faq-bot-kendra-search.html) with Amazon Kendra search to provide useful answers to users' questions. You can also use an [Amazon Simple Storage Service bucket](https://docs.aws.amazon.com/kendra/latest/dg/data-source-s3.html) as a data source for Amazon Kendra to connect to and index your documents.

Amazon Kendra has the following components:
+ An [*index*](https://docs.aws.amazon.com/kendra/latest/dg/create-index.html) that holds your documents and makes them searchable.
+ A [*data source*](https://docs.aws.amazon.com/kendra/latest/dg/data-source.html) that stores your documents and Amazon Kendra connects to. You can automatically synchronize a data source with an Amazon Kendra index so that your index stays updated with your source repository.
+ A [*document addition API*](https://docs.aws.amazon.com/kendra/latest/dg/in-adding-documents.html) that adds documents directly to an index.
+ A [*retrieve API*](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Retrieve.html) that retrieves relevant passages or text excerpts given an input query.
+ A [*query API*](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Query.html) that searches an index given an input query.

You can use Amazon Kendra through the console or the API. You can create, update, and delete indexes. Deleting an index deletes all of its data source connectors and permanently deletes all of your document information from Amazon Kendra.

**Topics**
+ [Indexes in Amazon Kendra](hiw-index.md)
+ [Documents](hiw-documents.md)
+ [Data sources](hiw-data-source.md)
+ [Queries](hiw-query.md)
+ [Tags](tagging.md)