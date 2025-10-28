# Applying the plugin to Amazon OpenSearch Service queries

After you [create a pipeline](managed-opensearch-plugin-pipeline-example.md "managed-opensearch-plugin-pipeline-example.md"), you are ready to apply the Amazon Personalize Search Ranking plugin to queries.
You can apply the Amazon Personalize Search Ranking plugin to all queries and responses for an index. You can also apply the plugin to individual
queries and responses.

- You can use the following Python code to apply a search pipeline to an index. With this approach, all searches
  using this index use the plugin to apply personalization to search results.

```
import requests
from requests_auth_aws_sigv4 import AWSSigV4

domain_endpoint = '`domain endpoint`'
index = '`index name`'
url = f'{domain_endpoint}/{index}/_settings/'
auth = AWSSigV4('es')
headers = {'Content-Type': 'application/json'}
body = {
    "index.search.default_pipeline": "`pipeline name`"
}
try:
    response = requests.put(url, auth=auth, json=body, headers=headers)
    print(response.text)
except Exception as e:
    print(f"Error: {e}")
```

- You can use the following Python code to apply a search pipeline to an individual query for Toyota brand
  cars.

Update the code to specify your domain endpoint, your OpenSearch Service index, the name of your pipeline, and your query. For
`user_id`, specify the ID of the user that you're getting search results for. This user must be in the
data that you used to create your Amazon Personalize solution version. If the user wasn't present, Amazon Personalize ranks the items based on
their popularity.

For `context`, if you use contextual metadata, provide the user's contextual metadata, such as their
device type. The `context` field is optional. For more information, see [Increasing recommendation relevance with contextual metadata](contextual-metadata.md "contextual-metadata.md").

```
import requests
from requests_auth_aws_sigv4 import AWSSigV4

domain_endpoint = '`domain endpoint`'
index = '`index name`'
url = f'{domain_endpoint}/{index}/_search/'

auth = AWSSigV4('es')
headers = {'Content-Type': 'application/json'}
params = {"search_pipeline": "`pipeline-name`"}
body = {
    "query": {
        "multi_match": {
            "query": "`Toyota`",
            "fields": ["`BRAND`"]
        }
    },
    "ext": {
        "personalize_request_parameters": {
            "user_id": "`USER ID`",
            "context": { "`DEVICE`" : "`mobile phone`" }
        }
    }
}
try:
    response = requests.post(url, auth=auth, params=params, json=body, headers=headers, verify=False)
    print(response)
except Exception as e:
    print(f"Error: {e}")
```
