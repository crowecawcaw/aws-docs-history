# Amazon Q Business boosting types

###### Note

Relevance tuning has replaced metadata boosting. For more information,
see [Tuning the query
results based on document attribute relevancy](relevancy-tuning.md "relevancy-tuning.md").

Amazon Q Business offers two types of boosting: document attribute boosting
and document attribute value boosting. This section outlines how these types of
boosting work.

###### Note

To use the `STRING` and `STRING_LIST` type document
attributes for boosting on the console and the API, they must be enabled for
search using the [DocumentAttributeConfiguration](../api-reference/API_DocumentAttributeConfiguration.md "../api-reference/API_DocumentAttributeConfiguration.md")
object of the [UpdateIndex](../api-reference/API_UpdateIndex.md "../api-reference/API_UpdateIndex.md") API operation. If
you don't enable search on these attributes, you can't boost attributes of these
data types on either the Amazon Q Business console or the API.

###### Types of boosting

- [Boosting document attribute importance](#boosting-document-attribute "#boosting-document-attribute")
- [Boosting document attribute value](#boosting-document-attribute-value "#boosting-document-attribute-value")

## Boosting document attribute importance

###### Note

Relevance tuning has replaced metadata boosting. For more information,
see [Tuning the query
results based on document attribute relevancy](relevancy-tuning.md "relevancy-tuning.md").

You can boost document attributes to control the relative importance, or
boosting level, of the field for end user queries. You can boost importance for
all document attribute data types that are supported by Amazon Q—`DATE`, `NUMBER`, `STRING`, and
`STRING_LIST`.

###### Note

Amazon Q Business automatically boosts the document title attribute
to **Low**. You can change this value when you customize
boosting.

If you choose to boost document attributes, you can also customize boosting in
the following ways:

- **Boost duration** – Specifies the
  time period over which a boost applies to a `DATE` type
  document attribute. For example, if you set boosting duration to 604,800
  seconds (1 week) for the `_created_at` reserved attribute,
  documents created within the last week will be boosted.

Generally, all documents inside the boosting duration will be given
more importance over documents outside the boosting duration. Within the
boosting duration, documents with more recent dates will be given more
importance over documents with less recent dates.

Outside the boosting duration, the documents with more recent dates
will continue to be given more importance over documents with less
recent dates. However, the overall effect of the date boosting will
taper to zero as the dates move further away from the boosting
duration.

###### Note

Boosting duration is based on the most recent date in all
documents in the index.

- **Boost order** – Determines
  whether a `NUMBER` type document attribute is boosted in
  prioritizing higher values or prioritizing lower values.

For example, if your documents contain attributes for view count, you
can choose to prioritize chat responses with higher view count values by
boosting larger values over smaller values. Or, suppose your documents
contain attributes that denote priority—for example, a task
tracker that assigns priority 1 to the most important task. In that
case, you can choose to boost documents using smaller values.

## Boosting document attribute value

###### Note

Relevance tuning has replaced metadata boosting. For more information,
see [Tuning the query
results based on document attribute relevancy](relevancy-tuning.md "relevancy-tuning.md").

To customize boosting levels, you can boost document attribute values for only
`STRING` type document attributes.

For example, suppose that you're applying an importance boost to a
`STRING` attribute called `department`. The
`department` attribute has values like `HR` and
`Legal`. You can assign the values `HR, VERY_HIGH` and
`Legal, HIGH` to customize the importance that Amazon Q gives to these attribute values when they match a chat request.
