# Tuning and sorting responses

###### Note

Feature support varies by index type and search API being used. To see if this
feature is supported for the index type and search API you’re using, see [Index
types](hiw-index-types.md "hiw-index-types.md").

You can modify the effect of a field or attribute on the search relevance through
relevance tuning. You can also sort the search results by a certain attribute or
field.

###### Topics

- [Tuning responses](#tuning-responses "#tuning-responses")
- [Sorting responses](#sorting-responses "#sorting-responses")

## Tuning responses

You can modify the effect of a field or attribute on the search relevance through
relevance tuning. To quickly test relevance tuning, use the [Query](../APIReference/API_Query.md "../APIReference/API_Query.md") API to pass in tuning configurations in the query. Then you can
see the different search results that you get from different configurations.
Relevance tuning at the query level is not supported in the console. You can also
tune fields or attributes that are of the type `StringList` at the index
level only. For more information, see [Tuning search relevance](tuning.md "tuning.md").

By default, query responses are sorted by the relevance score that Amazon Kendra determines for each result in the response.

You can tune results for any built-in or custom attribute/field of the following
types:

- Date value
- Long value
- String value

You can't sort attributes of the following type:

- String list values

###### Rank and tune document results (AWS SDK)

Set the `Searchable` parameter to true to boost the document
metadata configuration.

To tune an attribute in a query, set the
`DocumentRelevanceOverrideConfigurations` parameter of the
`Query` API and specify the name of the attribute to tune.

The following JSON example shows a
`DocumentRelevanceOverrideConfigurations` object that overrides the
tuning for the attribute called "department" in the index.

```
"DocumentRelevanceOverrideConfigurations" : [
    "Name": "department",
    "Relevance": {
        "Importance": 1,
        "ValueImportanceMap": {
            "IT": 3,
            "HR": 7
        }
    }
]
```

## Sorting responses

Amazon Kendra uses the sorting attribute or field as part of the criteria for
the documents returned by the query. For example, the results returned by a query
sorted by "\_created_at" might not contain the same results as a query sorted by
"\_version".

By default, query responses are sorted by the relevance score that Amazon Kendra determines for each result in the response. To change the sort order,
make a document attribute sortable and then configure Amazon Kendra to use that
attribute to sort responses.

You can sort results on any built-in or custom attribute/field of the following
types:

- Date value
- Long value
- String value

You can't sort attributes of the following type:

- String list values

You can sort on one or more document attributes in each query. Queries return 100
results. If there are fewer than 100 documents with the sorting attribute set,
documents without a value for the sorting attribute are returned at the end of the
results, sorted by relevance to the query.

###### To sort document results (AWS SDK)

1. To use the [UpdateIndex](../APIReference/API_UpdateIndex.md "../APIReference/API_UpdateIndex.md") API to make an attribute sortable, set the
   `Sortable` parameter to `true`. The following JSON
   example uses `DocumentMetadataConfigurationUpdates` to add an
   attribute called "Department" to the index and make it sortable.

```
"DocumentMetadataConfigurationUpdates": [
   {
       "Name": "Department",
       "Type": "STRING_VALUE",
       "Search": {
           "Sortable": "true"
       }
   }
]
```

2. To use one sortable attribute in a query, set the
   `SortingConfiguration` parameter of the [Query](../APIReference/API_Query.md "../APIReference/API_Query.md") API. Specify the name of the attribute to sort and
   whether to sort the response in ascending or descending order.

The following JSON example shows the `SortingConfiguration`
parameter that you use to sort the results of a query by the "Department"
attribute in ascending order.

```
   "SortingConfiguration": {
      "DocumentAttributeKey": "Department",
      "SortOrder": "ASC"
   }

```

3. To use more than one sortable attribute in a query, set the
   `SortingConfigurations` parameter of the [Query](../APIReference/API_Query.md "../APIReference/API_Query.md") API. You can set upto 3 fields that Amazon Kendra
   should sort the results on. You can also specify whether the results should
   be sorted in ascending or descending order. The sort field quota can be
   increased.

If you don't provide a sorting configuration, the results are sorted by
the relevance that Amazon Kendra determines for the result. In the case
of ties in sorting the results, the results are sorted by relevance.

The following JSON example shows the `SortingConfigurations`
parameter that you use to sort the results of a query by the attributes
"Name" and "Price" in ascending order.

```
"CollapseConfiguration" : {
    "DocumentAttributeKey": "Name",
    "SortingConfigurations": [
        {
            "DocumentAttributeKey": "Price",
            "SortOrder": "ASC"
        }
    ],
    "MissingAttributeKeyStrategy": "IGNORE"
}
```

###### To sort document results (console)

###### Note

Multi-attribute sort isn't currently supported by the AWS Management Console.

1. To make an attribute sortable in the console, choose
   **Sortable** in the attribute definition. You can make
   an attribute sortable when you create the attribute, or you can modify it
   later.
2. To sort a query response in the console, choose the attribute to sort the
   response from the **Sort** menu. Only attributes that were
   marked sortable during datasource configuration appear in the list.
