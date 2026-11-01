

# Using the timestamp field in time series collections
<a name="serverless-timestamp-field"></a>

Each index in an Amazon OpenSearch Serverless NextGen time series collection has a designated *timestamp field* – a single `date` field that represents the event time of every document in the index. OpenSearch Serverless uses this field to organize and manage time series data. Every document that you ingest into a NextGen time series collection must include the designated timestamp field. If a document is missing the timestamp field or provides an invalid value, OpenSearch Serverless rejects that document. For more information about this validation, see [Ingesting documents](#serverless-timestamp-field-ingest).

**Note**  
The timestamp field applies only to *NextGen time series* collections. It doesn't apply to Classic time series collections, and it has no effect on search or vector search collections.

**Topics**
+ [Specifying the timestamp field](#serverless-timestamp-field-setting)
+ [Ingesting documents](#serverless-timestamp-field-ingest)
+ [Updating documents](#serverless-timestamp-field-update)

## Specifying the timestamp field
<a name="serverless-timestamp-field-setting"></a>

You specify the timestamp field for an index with the `index.timestamp_field` index setting. This setting is **optional**. OpenSearch Serverless resolves the timestamp field for an index in the following order of precedence:

1. The `index.timestamp_field` setting on the index, if you specify one when you create the index.

1. The `index.timestamp_field` setting defined by a matching index template, if the index doesn't specify one directly.

1. The default field `@timestamp`, if neither the index nor a matching template specifies a timestamp field.

The following OpenSearch REST API request creates an index that designates a field named `event-time` as the timestamp field. Replace {{my-logs}} with your index name and {{event-time}} with the name of the field that you want to use as the timestamp field.

```
PUT /{{my-logs}}
{
  "settings": {
    "index": {
      "timestamp_field": "{{event-time}}"
    }
  }
}
```

If neither the index nor a matching index template specifies the setting, the index uses `@timestamp`, and every document must include an `@timestamp` field.

If you ingest a document into an index that doesn't exist yet, OpenSearch Serverless automatically creates the index. An automatically created index can't specify the `index.timestamp_field` setting directly, so OpenSearch Serverless resolves its timestamp field from a matching index template, or from the default `@timestamp` field if no template matches. To designate a specific timestamp field for automatically created indexes, define an index template that sets `index.timestamp_field`.

**Note**  
The designated timestamp field must be mapped as a top-level `date` field. It can't be an object or nested field. OpenSearch Serverless sets the timestamp field as the index sort field in descending order.

## Ingesting documents
<a name="serverless-timestamp-field-ingest"></a>

When you ingest a document into a time series collection, OpenSearch Serverless validates the designated timestamp field:
+ If the document contains the timestamp field and its value is a valid `date`, OpenSearch Serverless indexes the document.
+ If the document doesn't contain the designated timestamp field, OpenSearch Serverless rejects the document.
+ If the document contains the field but its value isn't a valid `date`, OpenSearch Serverless rejects the document.

OpenSearch Serverless rejects only the individual document that fails validation, not the entire bulk request. The response identifies each rejected document and the reason.

## Updating documents
<a name="serverless-timestamp-field-update"></a>

The timestamp of an existing document is **immutable**. You can update other fields of a document, but you can't change its timestamp.
+ An update that doesn't include the timestamp field succeeds. OpenSearch Serverless preserves the document's original timestamp.
+ An update that includes the timestamp field with the same value as the document's original timestamp succeeds.
+ An update that changes the timestamp to a different value, or that provides an invalid `date`, is rejected and the document is unchanged.

To correct the timestamp of a document, delete the document and index it again with the corrected value.