# Tuning the query results based on document attribute relevancy

###### Important

This section assumes that you understand [document
attributes](doc-attributes.md "doc-attributes.md") and [metadata
controls](mapping-doc-attributes.md "mapping-doc-attributes.md") in Amazon Q Business.

###### Note

If you are already using [metadata
boosting](metadata-boosting.md "metadata-boosting.md"), please contact AWS Support to migrate to the new version.

Relevancy tuning in Amazon Q Business is only available if you use an Amazon Q native
retriever. If you use an Amazon Kendra retriever, you must configure boosting for [document
attributes](../../../kendra/latest/dg/tuning.md "../../../kendra/latest/dg/tuning.md") in Amazon Kendra.

Relevance tuning or boosting is the ability for the admins to provide their preference
based on document attributes that can guide the retrieval and response generation in
Amazon Q Business. Choosing to boost document attributes doesn't by itself cause Amazon Q Business to
include or exclude a document in the chat response. A boosted document attribute is only
one of the factors that Amazon Q Business uses to determine the relevance of a document. You
can provide preferences on recency of the documents or the data sources where the
documents are stored using the metadata fields.

For more information, see [Understanding boosting in Amazon Q Business](understanding-boosting.md "understanding-boosting.md")

###### Topics

- [Recency](#recency "#recency")
- [Sources](#sources "#sources")
- [Rank order](#sources "#sources")
- [Setting relevancy preferences](#setting-relevancy-preferences "#setting-relevancy-preferences")

## Recency

Recency is the preference when the documented was created or last updated. To tune
for the results for recency, enable this preference. In **Recency
type**, choose either the `_created_at` or
`_last_updated_at` document attribute to indicate which metadata
field to use to guide Amazon Q Business. After choosing a document attribute, set the time
period in **Boosting duration** over which the boost applies to the
`DATE` type document attribute. You can pick either the last three,
six, nine, or 12 months to apply the boost.

For example, if you set boosting duration to the last three months for the
`_created_at` reserved attribute, documents created within the last
three months will be get a higher preference than documents created more than three
months ago.

Generally, all documents inside the boosting duration will be given more
importance over documents outside the boosting duration. Within the boosting
duration, documents with more recent dates will be given more importance over
documents with less recent dates. Outside the boosting duration, the documents will
not get be any additional preference or boost.

## Sources

Sources is the preference where the document is stored. This preference allows you
to boost chat responses based on `_data_source_id` document attribute
that helps you rank sources that are more authoritative than other sources in your
application environment. You can select up to five data sources.

For example, you have a two data sources—Sharepoint and an S3 bucket. If
you want Amazon Q Business to respond based on documents in S3 (if available) first and
then look at documents stored in Sharepoint, rank S3 higher than Sharepoint.

If you enable both preferences, you can also set the rank order of the
**Recency** and **Sources** preferences. For
example, if where the document is stored is more important than when the document
was created or updated, drag **Source** to have a higher priority
than **Recency**.

## Rank order

If you enable both preferences, you can also set the rank order of the
**Recency** and **Sources** preferences. For
example, if where the document is stored is more important than when the document
was created or updated, drag **Source** to have a higher priority
than **Recency**.

## Setting relevancy preferences

The following tabs provide a procedure to tune the query responses based on
document attributes using the console and code examples for the AWS CLI.

Console

**To tune the relevancy based on recency or data
source**

1. Sign in to the AWS Management Console and open the Amazon Q Business
   console.
2. In **Applications**, select the name of your
   application environment from the list of applications.
3. From the left navigation menu under
   **Enhancements**, choose
   **Relevance tuning**.
4. Enable the attributes to tune the query responses.
5. Drag the attribute to the order you want to prioritize the
   attributes.
6. To prioritize responses from more recent documents, in
   **Recency**, set the **Recency
   Type** and **Boosting duration**.
   In **Recency Type**, choose the metadata field
   you want to use. For **Boosting duration**,
   choose the time periods to prioritize when searching through
   data sources. Documents that were created or updated outside of
   the specified time periods will not have additional boosting or
   priority.
7. To prioritize based on data sources, in
   **Sources**, choose a data source, and
   choose **Add a source**. You can choose up to
   five data sources to search for documents. Rank the data source
   based to define the priority to be used for responses.

AWS CLI

**Update your Amazon Q Business index to apply relevancy
tuning**

This example shows how to increase the relevancy based on the
`_last_update_at` metadata field. In this example,
replace each `user input placeholder` with your
own information:

```

aws qbusiness --region `region` update-retriever \
  --application-id ``application_id`` \
  --retriever-id ``retriever_id`` \
  --configuration '{
    "nativeIndexConfiguration": {
        "indexId": "``index_id``",
        "boostingOverride": {
          "_last_updated_at"|"_created_at": {
            "dateConfiguration": {
              "boostingLevel": "ONE"|"TWO",
              "boostingDurationInSeconds": ``long``;
            }
          },
          "_data_source_id": {
            "stringConfiguration": {
              "boostingLevel": "ONE"|"TWO",
              "attributeValueBoosting": {
                "``data_source_id_1``": "ONE"|"TWO"|"THREE"|"FOUR"|"FIVE",
                "``data_source_id_1``": "ONE"|"TWO"|"THREE"|"FOUR"|"FIVE",
                ...
              }
            }
          }
        }
    }
  }'

```

This example shows an example input. Replace each `user
 input placeholder` with your own information:

```

aws qbusiness --region us-west-2 update-retriever \
  --endpoint-url https://``endpoint-url`` \
  --application-id ``application_id``
  --retriever-id ``retriever_id`` \
  --configuration '{
    "nativeIndexConfiguration": {
        "indexId": "``index_id``",
        "boostingOverride": {
          "_last_updated_at": {
            "dateConfiguration": {
              "boostingLevel": "ONE",
              "boostingDurationInSeconds": 100
            }
          },
          "_data_source_id": {
            "stringConfiguration": {
              "boostingLevel": "TWO",
              "attributeValueBoosting": {
                "``data_source_id_1``": "ONE",
                "``data_source_id_1``": "TWO",
                "``data_source_id_1``": "THREE",
                "``data_source_id_1``": "FOUR",
                "``data_source_id_1``": "FIVE"
              }
            }
          }
        }
    }
  }'


```
