# Monitoring the plugin with open source OpenSearch

As you apply the Amazon Personalize Search Ranking plugin to OpenSearch queries, you can monitor the plugin by getting metrics for your search
pipelines. Pipeline metrics include statistics like the number of failed requests for the `personalized_search_ranking` response
processor.

You can use the following code to get metrics for all of your pipelines. The response contains statistics for all
search pipelines. For an example of pipeline metrics, see [Pipeline metrics example](monitor-response.md "monitor-response.md").

```
curl -XGET "https://localhost:9200/_nodes/stats/search_pipeline?pretty" -ku 'admin:admin'
```
