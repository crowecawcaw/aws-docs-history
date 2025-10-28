# Applying the Amazon Personalize Search Ranking plugin to queries in open source OpenSearch

You can apply the Amazon Personalize Search Ranking plugin to all queries and responses for an OpenSearch index. You can also apply the plugin to
individual OpenSearch queries and responses.

- The following curl command applies a search pipeline to an OpenSearch index in an open source OpenSearch cluster
  running locally. With this approach, all searches at this index use the plugin to apply personalization to search
  results.

```
curl -XGET "https://localhost:9200/`index`/_settings" -ku 'admin:admin' --insecure -H 'Content-Type: application/json' -d'
{
  "index.search.default_pipeline": "`pipeline-name`"
}
'
```

- The following curl command applies a search pipeline to an individual query for Toyota brand cars on an index in
  an open source OpenSearch cluster running locally.

For `user_id`, specify the ID of the user that you're getting search results for. This user must be in
the data that you used to create your Amazon Personalize solution version. If the user wasn't present, Amazon Personalize ranks the items
based on their popularity. For `context`, if you use contextual metadata, provide the user's contextual
metadata, such as their device type. The `context` field is optional. For more information, see [Increasing recommendation relevance with contextual metadata](contextual-metadata.md "contextual-metadata.md").

```
curl -XGET "http://localhost:9200/`index`/_search?search_pipeline=`pipeline-name`" -ku 'admin:admin' --insecure -H 'Content-Type: application/json' -d'
{
  "query": {
    "multi_match": {
      "query": "Toyota",
      "fields": ["BRAND"]
    }
  },
  "ext": {
    "personalize_request_parameters": {
      "user_id": "`USER ID`",
      "context": { "`DEVICE`": "`mobile phone`" }
    }
  }
}
'
```

To understand how results are re-ranked, you can use OpenSearch Dashboards to compare OpenSearch results against
re-ranked results with the plugin. For more information, see [Comparing personalized OpenSearch results to results without personalization](opensource-comparing-results.md "opensource-comparing-results.md").

As you apply the plugin to OpenSearch queries, you can monitor the plugin by getting metrics for your OpenSearch
pipeline. For more information, see [Monitoring the plugin with open source OpenSearch](opensource-monitor.md "opensource-monitor.md").
