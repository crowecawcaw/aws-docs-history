# Collapsing/expanding query

results

###### Note

Feature support varies by index type and search API being used. To see if this
feature is supported for the index type and search API you’re using, see [Index
types](hiw-index-types.md "hiw-index-types.md").

When you connect Amazon Kendra to your data, it crawls [document
metadata attributes](hiw-document-attributes.md "hiw-document-attributes.md")—like `_document_title`,
`_created_at`, and `_document_id`—and uses these
attributes or fields to provide advanced search capabilities during query time.

Amazon Kendra's Collapse and expand query results feature allows you to group
search results using a common document attribute and display them—either
collapsed or partially expanded—under a designated primary document.

###### Note

The collapse and expand query results feature is currently available only via the
[Amazon Kendra API](../APIReference/welcome.md "../APIReference/welcome.md").

This is useful in the following kinds of search situations:

- Multiple versions of content exist in documents within your index. When your
  end user queries the index, you want them to see the most relevant version of
  the document with duplicates hidden/collapsed. For example, if your index
  contains multiple versions of a document named "NYC leave policy" you can choose
  to collapse the documents for the specific groups "HR" and "Legal" using the
  "Type" attribute/field.

![Example 1](images/expand-collapse-1.png)

- Your index contains multiple documents with unique information about one kind
  of item or object, like a product inventory, for example. To capture and sort
  item information conveniently, you want end users to access all documents linked
  by an item or object as one search result. In the example below, a customer
  search on "animal print shirts" returns results grouped by name, and sorted by
  ascending price order.

![Example 2](images/expand-collapse-2.png)

## Collapsing results

To group similar or related documents together, you must specify the attribute to
collapse on (for example, you can collapse/group documents by
`_category`). To do this, call the [Query API](../APIReference/API_Query.md "../APIReference/API_Query.md") and use the
[CollapseConfiguration](../APIReference/API_CollapseConfiguration.md "../APIReference/API_CollapseConfiguration.md") object to specify the
`DocumentAttributeKey` to collapse on. The
`DocumentAttributeKey` controls which field search results will be
collapsed upon. Supported attribute key fields include `String` and
`Number`. `String list` and `Date` type are not
supported.

## Choosing a primary document using sort

order

To configure the primary document to display for a collapsed group, you use the
`SortingConfigurations` parameter under [CollapseConfiguration](../APIReference/API_CollapseConfiguration.md "../APIReference/API_CollapseConfiguration.md"). For example, to get the most recent version of a
document, you would sort each collapsed group by `_version`. You can
specify up to 3 attributes/fields to sort by and a sort order for each
attribute/field using `SortingConfigurations`. You can request a quota
increase for the number of sort attributes.

By default, Amazon Kendra sorts query responses by the relevance score that
it determines for each result in the response. To change the default sort order,
make document attributes sortable and then configure Amazon Kendra to use these
attributes to sort responses. For more information, see [Sorting
responses](tuning-sorting-responses.md#sorting-responses "tuning-sorting-responses.md#sorting-responses").

## Missing document key strategy

If your document doesn't have a collapse attribute value, Amazon Kendra
offers three customization options:

- Choose to `COLLAPSE` all documents with null or missing values
  in one group. This is the default configuration.
- Choose to `IGNORE` documents with null or missing values.
  Ignored documents will not appear in query results.
- Choose to `EXPAND` each document with a null or missing value
  into a group of its own.

## Expanding results

You can choose whether collapsed search result groups expand using the
`Expand` parameter in the [CollapseConfiguration](../APIReference/API_CollapseConfiguration.md "../APIReference/API_CollapseConfiguration.md") object. Expanded results maintain the same sort
order that was used to select the primary document for the group.

To configure the number of collapsed search result groups to expand, you use the
`MaxResultItemstoExpand` parameter in the [ExpandConfiguration](../APIReference/API_ExpandConfiguration.md "../APIReference/API_ExpandConfiguration.md") object. If you set this value to 10, for example,
only the first 10 out of 100 result groups will have expand functionality.

To configure the number of expanded results to show per collapsed primary
document, use the `MaxExpandResultsPerItem` parameter. For instance, if
you set this value to 3, then at most 3 results per collapsed group will be
displayed.

## Interactions with other Amazon Kendra features

- Collapsing and expanding results doesn't change the number of facets or
  impact the total number of results displayed.
- Amazon Kendra
  [featured search results](featured-results.md "featured-results.md") won't be collapsed even if they have
  the same field value as the collapse field you configure.
- Collapsing and expanding results only applies to results of type
  `DOCUMENT`.
