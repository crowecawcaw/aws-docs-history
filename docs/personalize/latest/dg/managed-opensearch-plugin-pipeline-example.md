# Creating a pipeline in Amazon OpenSearch Service

After you [install the Amazon Personalize Search Ranking plugin](open-search-install-managed.md "open-search-install-managed.md"), you're ready to configure it by creating an OpenSearch search pipeline.

A _search pipeline_ is a set of request and response processors that run sequentially
in the order that you create them. When you create a search pipeline for the plugin, you specify a `personalized_search_ranking` response
processor. For information about search pipelines, see [Search pipelines](https://opensearch.org/docs/latest/search-plugins/search-pipelines/index/ "https://opensearch.org/docs/latest/search-plugins/search-pipelines/index/").

After you create a search pipeline with a `personalized_search_ranking` response processor, you're ready to start applying the
plugin to OpenSearch queries. You can apply it to an OpenSearch index or an individual OpenSearch query. For more
information, see [Applying the plugin](managed-apply-plugin.md "managed-apply-plugin.md").

You can use the following Python code to create a search pipeline with a `personalized_search_ranking` response processor on an
OpenSearch Service domain. Replace `domain endpoint` with your domain endpoint URL. For example: `https://<domain
 name>.<AWS region>.es-staging.amazonaws.com`. For a complete explanation of each `personalized_search_ranking` parameter,
see [Fields for the personalized_search_ranking response processor](opensearch-plugin-pipeline-fields.md "opensearch-plugin-pipeline-fields.md").

```
import requests
from requests_auth_aws_sigv4 import AWSSigV4

domain_endpoint = '`domain endpoint`'
pipeline_name = '`pipeline name`'
url = f'{domain_endpoint}/_search/pipeline/{pipeline_name}'
auth = AWSSigV4('es')

headers = {'Content-Type': 'application/json'}

body = {
  "description": "A pipeline to apply custom re-ranking from Amazon Personalize",
  "response_processors": [
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
  ]
}
try:
    response = requests.put(url, auth=auth, json=body, headers=headers, verify=False)
    print(response.text)
except Exception as e:
    print(f"Error: {e}")
```
