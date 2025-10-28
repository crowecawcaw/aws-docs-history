# Analyzing Amazon SNS messages for OpenSearch Service

destinations

This topic explains how to analyze Amazon SNS messages sent through delivery streams to
Amazon OpenSearch Service (OpenSearch Service) destinations.

###### To analyze SNS messages sent through Firehose delivery streams to OpenSearch Service destinations

1. Configure your OpenSearch Service resources. For instructions, see [Getting Started with Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/es-gsg.md "../../../opensearch-service/latest/developerguide/es-gsg.md") in the
   _Amazon OpenSearch Service Developer Guide_.
2. Configure your delivery stream. For instructions, see [Choose OpenSearch Service
   for Your Destination](../../../firehose/latest/dev/create-destination.md#create-destination-elasticsearch "../../../firehose/latest/dev/create-destination.md#create-destination-elasticsearch") in the _Amazon Data Firehose Developer Guide_.
3. Run a query using OpenSearch Service queries and Kibana. For more information, see [Step 3: Search Documents in an OpenSearch Service Domain](../../../opensearch-service/latest/developerguide/es-gsg-search.md "../../../opensearch-service/latest/developerguide/es-gsg-search.md")
   and [Kibana](../../../opensearch-service/latest/developerguide/es-kibana.md "../../../opensearch-service/latest/developerguide/es-kibana.md") in the
   _Amazon OpenSearch Service Developer Guide_.

## Example query

The following example queries the `my-index` index for all SNS messages
received in the specified date range:

```
POST https://search-my-domain.us-east-1.es.amazonaws.com/my-index/_search
{
  "query": {
    "bool": {
      "filter": [
        {
          "range": {
            "Timestamp": {
              "gte": "2020-12-08T00:00:00.000Z",
              "lte": "2020-12-09T00:00:00.000Z",
              "format": "strict_date_optional_time"
            }
          }
        }
      ]
    }
  }
}
```
