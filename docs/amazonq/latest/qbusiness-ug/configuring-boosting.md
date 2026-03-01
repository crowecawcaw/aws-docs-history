# Configuring document attributes for boosting in Amazon Q Business

###### Note

Relevance tuning has replaced metadata boosting. For more information,
see [Tuning the query
results based on document attribute relevancy](relevancy-tuning.md "relevancy-tuning.md").

To boost specific documents for end user queries using document attributes, you
can use the AWS Management Console or the [DocumentAttributeBoostingConfiguration](../api-reference/API_DocumentAttributeBoostingConfiguration.md "../api-reference/API_DocumentAttributeBoostingConfiguration.md") parameter of the
[UpdateRetriever](../api-reference/API_UpdateRetriever.md "../api-reference/API_UpdateRetriever.md") API
operation.

###### Note

For `STRING` and `STRING_LIST` type document attributes
to be used for boosting on the console and the API, they must be enabled for
search using the [DocumentAttributeConfiguration](../api-reference/API_DocumentAttributeConfiguration.md "../api-reference/API_DocumentAttributeConfiguration.md")
object of the [UpdateIndex](../api-reference/API_UpdateIndex.md "../api-reference/API_UpdateIndex.md") API operation. If
you don't enable search on these attributes, you can't boost attributes of these
data types on either the console or the API.

The following tabs provide a procedure to boost document attributes using the
console and code examples for the AWS CLI.

Console
**To boost document attributes**

1. Sign in to the AWS Management Console and open the Amazon Q Business
   console.
2. In **Applications**, select the name of your
   application environment from the list of applications.
3. From the left navigation menu, choose **Metadata
   boosting**.
4. In **Metadata boosting**, choose the document
   attribute type that you want to boost.

###### Note

You can boost attributes using the following values:
**None**, **Low**,
**Medium**, **High**,
and **Very high**.

Choose from the following options:

    1. **Popular** – Amazon Q displays the following popularly boosted
     document attributes for you to choose from:


    	1. **Document title** –
    	 Use to boost the title of a document. You can also
    	 use **Advanced settings** to
    	 boost specific document titles. By default, the
    	 document title attribute is enabled for search
    	 with a value of `Low`. You can change
    	 this value when you customize boosting.
    	2. **Last updated** – Use
    	 to boost content by its last updated date. You can
    	 also use **Advanced settings** to
    	 configure **Boosting duration**,
    	 or how long your boost should apply.
    	3. **File type** – Use to
    	 boost content by file type.
    	4. **Data sources** – Use
    	 to boost the content data source type.
    	5. To save your configuration, choose
    	 **Save**.
    2. **Text** – Use to boost
     `STRING` and `STRING_LIST`
     type reserved or custom document attributes that you
     have enabled for search. Then, choose
     **Save**.
    3. **Date** – Use to boost
     content using `DATE` type reserved or custom
     document attributes. For example, use the
     **Created at** document attribute
     to boost content based on recency. You can also use
     **Advanced settings** to configure
     **Boosting duration**, or how long
     your boost should apply. Then, choose
     **Save**.
    4. **Numeric** – Use to boost
     content using `NUMERIC` type reserved or
     custom attributes. For example, use the **View
     count** document attribute to boost content
     based on view count. Based on your boosting needs,
     choose either **Prioritize higher
     values** or **Prioritize lower
     values**. Then, choose
     **Save**.
    5. Once done, you can select **View web
     experience** to check boosting. Your
     configured web experience will open in a new
     window.

AWS CLI
**Update your Amazon Q Business index to
apply boosting**

This example shows how to apply `VERY_HIGH` boosting for
the `STRING` type document attribute
`_document_title`.

```

aws qbusiness update-retriever \
--application-id `APPLICATION-ID` --retriever-id `RETRIEVER-ID` \
--configuration '{
        "nativeIndexConfiguration": {
            "indexId": "`INDEX-ID`",
            "boostingOverride": {
                "_document_title": {
                    "stringConfiguration": {
                        "boostingLevel": "VERY_HIGH"
                    }
                }
            }
        }
}'
```

This example shows how to apply boosting for the `STRING`
type attribute `_category`, the `DATE` type
attribute `_created_at`, the `NUMBER` type
attribute `_view_count`, and the `STRING_LIST`
type attribute `_authors`.

```

aws qbusiness update-retriever \
--application-id `APPLICATION-ID` --retriever-id `RETRIEVER-ID` \
--configuration '{
        "nativeIndexConfiguration": {
            "indexId": "`INDEX-ID`",
            "boostingOverride": {
                "_category": {
                    "stringConfiguration": {
                        "boostingLevel": "LOW",
                        "attributeValueBoosting": {
                            "HR": "MEDIUM"
                        }
                    }
                },
                "_created_at": {
                    "dateConfiguration": {
                        "boostingLevel": "LOW",
                        "boostingDurationInSeconds": 2592000
                    }
                },
                "_view_count": {
                    "numberConfiguration": {
                        "boostingLevel": "LOW",
                        "boostingType": "PRIORITIZE_SMALLER_VALUES"
                    }
                },
                "_authors": {
                    "stringListConfiguration": {
                        "boostingLevel": "HIGH"
                    }
                }
            }
        }
}'
```

**Update your Amazon Q Business retriever to
remove any existing boosts**

This example shows how to remove any existing boosts from document
attributes in your retriever.

```

aws qbusiness update-retriever \
--application-id `APPLICATION-ID` --retriever-id `RETRIEVER-ID` \
--configuration '{
        "nativeIndexConfiguration": {
            "indexId": "`INDEX-ID`"
        }
}'
```

**Get details about your Amazon Q Business
retriever boosts**

This example shows how to get details for your existing boosting
configuration

```

aws qbusiness get-retriever \
--application-id `APPLICATION-ID` --retriever-id `RETRIEVER-ID`
```
