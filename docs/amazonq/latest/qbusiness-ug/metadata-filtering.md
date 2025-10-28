# Filtering chat responses using document attributes

and metadata

###### Note

This section assumes that you have an understanding of [document attributes and how they work](doc-attributes.md "doc-attributes.md") in Amazon Q.

The Amazon Q Business API includes a feature that lets you filter by document
attribute. By using this feature, you can customize and control chat responses for your
end user using attributes—or metadata—attached to documents that are
mapped to index fields. For example, if `data source type` is an attribute
that's attached to your documents, you can specify that chat responses should be
generated only from a specific data source.

Or, you can allow end users to restrict the scope of chat responses using the
attribute filters that you have selected. For example, an end user can choose to have
their chat responses generated using only documents from data sources that they
specify.

Filtering chat responses using metadata has the following key benefits:

- **Q&A on LLM knowledge** – Users can
  ask questions and get answers from the general knowledge that the LLM
  has.
- **Ensure response relevance and accuracy**
  – You can indicate that responses should only be generated from specific
  authoritative sources within your data.
- **Control response context** – You can
  specify the file type (for example, PDF) and library or collection of documents
  (for example, business requirements documents) that responses are generated
  from.
- **Maintain response freshness** – You can
  restrict chat responses to come from only documents that were generated after a
  specific date.
- **Scope chat responses** – You can help
  your end users to narrow the scope of their responses and get to the right
  answer more quickly.
  Amazon Q Business offers a set of reserved document attributes that you can use.
  You can also create custom document attributes that better represent your organization’s
  data and use cases for more finely-tuned chat response control.

###### Important

Filtering using document attributes in chat is only supported using the API.
Boosting
search results using document attributes is supported using the console or the
API.
