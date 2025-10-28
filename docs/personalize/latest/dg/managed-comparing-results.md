# Comparing personalized Amazon OpenSearch Service results to results without personalization

The Amazon Personalize Search Ranking plugin rearranges search results based on both the ranking from Amazon Personalize and the ranking from OpenSearch. The
way that the plugin re-ranks the results depends on how you configured the `personalized_search_ranking` response processor in your
pipelines.

To understand how results are ranked, you can run queries with and without personalization, and compare the results.
You can use the following Python code to run two different queries and output the results to two JSON files. The first
method runs a query that uses the plugin to re-rank results. The second runs a method that generates results without
personalization.

```
import json
import requests
from requests_auth_aws_sigv4 import AWSSigV4


# Returns re-ranked OpenSearch results using the Amazon Personalize Search Ranking plugin.
def get_personalized_results(pipeline_name):
    url = f'{domain}/{index}/_search/'
    auth = AWSSigV4('es')
    headers = {'Content-Type': 'application/json'}
    params = {"search_pipeline": pipeline_name}
    body = {
        "query": {
            "multi_match": {
                "query": "Toyota",
                "fields": ["BRAND"]
            }
        },
        "ext": {
            "personalize_request_parameters": {
                "user_id": "1"
            }
        }
    }
    try:
        response = requests.post(url, auth=auth, params=params, json=body, headers=headers, verify=False)
    except Exception as e:
        return f"Error: {e}"
    return response.text


# Returns OpenSearch results without personalization.
def get_opensearch_results():
    url = f'{domain}/{index}/_search/'
    auth = AWSSigV4('es')
    headers = {'Content-Type': 'application/json'}
    body = {
        "query": {
            "multi_match": {
                "query": "Toyota",
                "fields": ["BRAND"]
            }
        }
    }
    try:
        response = requests.post(url, auth=auth, json=body, headers=headers, verify=False)
    except Exception as e:
        return f"Error: {e}"
    return response.text


def print_results(file_name, results):
    results_file = open(file_name, 'w')
    results_file.write(json.dumps(results, indent=4))
    results_file.close()


# specify domain endpoint
domain = "`DOMAIN_ENDPOINT`"

# specify the region where you created your Amazon Personalize resources and Amazon OpenSearch domain
aws_region = "`REGION`"

# specify the name of the pipeline that uses the Amazon Personalize plugin
pipeline_name = "`PIPELINE_NAME`"

# specify your Amazon OpenSearch index
index = "`INDEX`"

# specify names for json files for comparison
personalized_results_file = "personalized_results.json"
opensearch_results_file = "opensearch_results.json"

# get personalized results
personalized_results = json.loads(get_personalized_results(pipeline_name))

# get OpenSearch results without personalization
opensearch_results = json.loads(get_opensearch_results())

# print results to files
print_results(personalized_results_file, personalized_results)
print_results(opensearch_results_file, opensearch_results)
```
