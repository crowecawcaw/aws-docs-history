# Pipeline metrics example

As you apply the Amazon Personalize Search Ranking plugin to OpenSearch queries, you can monitor the plugin by getting metrics for your search
pipelines. Pipeline metrics include statistics like the number of failed requests for the `personalized_search_ranking` response
processor.

The following code shows an excerpt of the pipeline metrics that are returned from OpenSearch. It shows only the
`pipelines` object that contains statistics for two different pipelines. For each pipeline, you can find
Amazon Personalize Search Ranking plugin metrics in the `personalized_search_ranking` response processor list. For a complete example of all metrics, see [Search pipeline
metrics](https://opensearch.org/docs/latest/search-plugins/search-pipelines/search-pipeline-metrics/ "https://opensearch.org/docs/latest/search-plugins/search-pipelines/search-pipeline-metrics/").

```
{
....
....
  "pipelines": {
    "pipelineA": {
      "request": {
        "count": 0,
        "time_in_millis": 0,
        "current": 0,
        "failed": 0
      },
      "response": {
        "count": 6,
        "time_in_millis": 2246,
        "current": 0,
        "failed": 0
      },
      "request_processors": [],
      "response_processors": [
        {
          **personalized\_search\_ranking": {
 "type": "personalized\_search\_ranking",
 "stats": {
 "count": <number of requests>,
 "time\_in\_millis": <time>,
 "current": 0,
 "failed": <number of failed requests>
 }
 }**
        }
      ]
    },
    "pipelineB": {
      "request": {
        "count": 0,
        "time_in_millis": 0,
        "current": 0,
        "failed": 0
      },
      "response": {
        "count": 8,
        "time_in_millis": 2248,
        "current": 0,
        "failed": 0
      },
      "request_processors": [],
      "response_processors": [
        {
          **"personalized\_search\_ranking": {
 "type": "personalized\_search\_ranking",
 "stats": {
 "count": <number of requests>,
 "time\_in\_millis": <time>,
 "current": 0,
 "failed": <number of failed requests>
 }
 }**
        }
      ]
    }
  }
....
....
}
```
