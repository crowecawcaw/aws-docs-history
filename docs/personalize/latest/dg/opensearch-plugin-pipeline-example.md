# Creating a pipeline in open source OpenSearch

After you install the plugin on your cluster, you're ready to configure it by creating an OpenSearch search pipeline.

A _search pipeline_ is a set of request and response processors that run sequentially
in the order that you create them. When you create a search pipeline for the plugin, you specify a `personalized_search_ranking` response
processor. For information about search pipelines, see [Search pipelines](https://opensearch.org/docs/latest/search-plugins/search-pipelines/index/ "https://opensearch.org/docs/latest/search-plugins/search-pipelines/index/").

After you create a pipeline with a `personalized_search_ranking` response processor, you are ready to start applying the plugin to queries.
For more information, see [Applying the plugin](opensource-apply-plugin.md "opensource-apply-plugin.md").

You can use the following curl command to create a search pipeline with a `personalized_search_ranking` response processor on an
open source OpenSearch cluster. For a complete explanation of each `personalized_search_ranking` parameter,
see [Fields for the personalized_search_ranking response processor](opensearch-plugin-pipeline-fields.md "opensearch-plugin-pipeline-fields.md").

```
curl -X PUT "http://localhost:9200/_search/pipeline/`pipeline-name`" -ku 'admin:admin' --insecure -H 'Content-Type: application/json' -d'
{
  "description": "A pipeline to apply custom re-ranking from Amazon Personalize",
  "response_processors" : [
    {
      "`personalized_search_ranking`" : {
        "campaign_arn" : "`Amazon Personalize Campaign ARN`",
        "item_id_field" : "`productId`",
        "recipe" : "aws-personalized-ranking-v2",
        "weight" : "`0.3`",
        "tag" : "`personalize-processor`",
        "iam_role_arn": "`Role ARN`",
        "aws_region": "`AWS region`",
        "ignore_failure": `true`
      }
    }
  ]
}'
```

After you create a search pipeline with a `personalized_search_ranking` response processor, you're ready to start applying the
plugin to OpenSearch queries. You can apply it to an OpenSearch index or an individual OpenSearch query. For more
information, see [Applying the Amazon Personalize Search Ranking plugin to queries in open source OpenSearch](opensource-apply-plugin.md "opensource-apply-plugin.md").
