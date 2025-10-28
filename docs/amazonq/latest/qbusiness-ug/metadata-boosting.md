# Boosting chat responses using metadata

boosting

###### Note

Relevance tuning has replaced metadata boosting. For more information,
see [Tuning the query
results based on document attribute relevancy](relevancy-tuning.md "relevancy-tuning.md").

###### Important

This section assumes that you understand [document attributes](doc-attributes.md "doc-attributes.md") and [metadata controls](mapping-doc-attributes.md "mapping-doc-attributes.md") in Amazon Q Business.

###### Note

Before you configure relevance tuning, you must [create a Amazon Q Business retriever and index](select-retriever.md "select-retriever.md") for your
application.

If you choose to use an Amazon Q Business native retriever, you can assign
weights to document attributes after mapping them to Amazon Q Business index
fields using the Amazon Q Business
_metadata boosting_ feature. Then, you can use these assigned weights
to fine-tune the underlying ranking of RAG retrieved passages within your Amazon Q application environment to optimize the relevance of chat responses. In Amazon Q, boosting means to raise a document in chat results using these
weights.

###### Important

Boosting document attributes using _metadata boosting_ is an
admin-only feature.

Boosting chat responses based on document attributes helps you rank sources that are
more authoritative higher than other sources in your application environment. You can assign a
higher value to more recent content, specific file types, or specific data
sources.

Amazon Q Business automatically boosts specific document attributes, like
document title, when retrieving information from your index to generate end user chat
responses. You can use the boosting feature to customize and control boosting, and also
override any pre-existing boosts applied by Amazon Q Business.

When you use this feature, a Retrieval Augmented Generation (RAG)-generated result is
given a boost during retrieval when the query includes terms that match that field or
attribute. You specify how much of a boost the document receives when there is a match.
When Amazon Q Business generates responses, it prioritizes the sources that are
assigned higher rankings.

Choosing to boost document attributes doesn't by itself cause Amazon Q Business
to include or exclude a document in the chat response. A boosted document attribute is
only one of the factors that Amazon Q Business uses to determine the relevance of
a document.

###### Note

Boosting in Amazon Q Business is only available if you use an Amazon Q native retriever. If you use an Amazon Kendra retriever, you
must [configure
boosting for document attributes](../../../kendra/latest/dg/tuning.md "../../../kendra/latest/dg/tuning.md") in Amazon Kendra. Amazon Q Business supports any boosting that's already configured in your Amazon Kendra index.

###### Topics

- [Understanding boosting in Amazon Q Business](#understanding-boosting "#understanding-boosting")
- [Amazon Q Business boosting types](boosting-parameters.md "boosting-parameters.md")
- [Configuring document attributes for boosting
  in Amazon Q Business](configuring-boosting.md "configuring-boosting.md")
- [Enabling document attributes for
  search in Amazon Q Business](boosting-searchable-attributes.md "boosting-searchable-attributes.md")

## Understanding boosting in Amazon Q Business

###### Note

Relevance tuning has replaced metadata boosting. For more information,
see [Tuning the query
results based on document attribute relevancy](relevancy-tuning.md "relevancy-tuning.md").

To improve retrieved results and customize the end user chat experience, Amazon Q enables you to map attributes to fields in your Amazon Q Business index.

Amazon Q Business offers [two kinds of attributes](doc-attributes.md#doc-attribute-types "doc-attributes.md#doc-attribute-types"):

- **Reserved or default** – Reserved
  attributes are based on document attributes that commonly occur in most
  data. You can use reserved attributes to map commonly occurring document
  attributes in your data to Amazon Q Business index fields.
- **Custom** – You can create custom
  attributes to map document attributes that are unique to your data to
  Amazon Q Business index fields.

Document attributes can be [mapped to index fields](mapping-doc-attributes.md "mapping-doc-attributes.md") using either the Amazon Q console or the API:

- **Use the API** – Before you use the
  API, you must first create an index. Next, create index fields. Then, to
  ingest documents into your Amazon Q Business index, use the [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") or [BatchPutDocument](../api-reference/API_BatchPutDocument.md "../api-reference/API_BatchPutDocument.md") API
  operations.
- **Use the console** – You can choose
  to map document attributes directly to your index or from your data sources
  when you connect your data source to Amazon Q Business.

You can create and map document attributes to index fields using the
_Metadata_ function on the console.

When you use data sources the your document attributes are added using
data sources, Amazon Q Business automatically maps specific data
source document fields to Amazon Q Business index fields. You can
choose to add custom fields during the data source configuration process as
well.

Document attributes—both reserved and custom—can only be of the
following data types: `DATE`, `NUMBER`, `STRING`,
and `STRING_LIST`. To use `STRING` and
`STRING_LIST` type document attributes for boosting on the console
and the API, they must be enabled for search. To enable these attributes using API,
use the [DocumentAttributeConfiguration](../api-reference/API_DocumentAttributeConfiguration.md "../api-reference/API_DocumentAttributeConfiguration.md")
object of the [UpdateIndex](../api-reference/API_UpdateIndex.md "../api-reference/API_UpdateIndex.md") API operation.

To customize and control boosting for document attributes, use the
`boostingOverride` parameter of the [NativeIndexConfiguration](../api-reference/API_NativeIndexConfiguration.md "../api-reference/API_NativeIndexConfiguration.md") object of
the [UpdateRetriever](../api-reference/API_UpdateRetriever.md "../api-reference/API_UpdateRetriever.md") API
operation.

To enable these attributes using the console, follow the steps in [Mapping document attributes directly to index
fields](mapping-doc-attributes.md#mapping-doc-attributes-directly "mapping-doc-attributes.md#mapping-doc-attributes-directly").

###### Note

If you don't enable search on these attributes, you can't boost attributes of
these data types on either the Amazon Q Business console or the
API.

For more information about Amazon Q Business document attributes and how to
map them, see [Document attributes and types](doc-attributes.md "doc-attributes.md").
