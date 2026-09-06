

# List recommendations
<a name="recommendations-list"></a>

List all recommendations in your account. Results are paginated and can be filtered by status.

## Code samples
<a name="list-rec-examples"></a>

**Example**  
List past recommendation jobs (running jobs are refreshed from the service):  

```
agentcore view recommendation
```
View a single recommendation by ID:  

```
agentcore view recommendation <recommendation-id>
```
Add `--json` for machine-readable output:  

```
agentcore view recommendation --json
```

```
import boto3

client = boto3.client("bedrock-agentcore", region_name="us-west-2")

# List all recommendations
response = client.list_recommendations()
for rec in response["recommendationSummaries"]:
    print(f"{rec['recommendationId']} | {rec['name']} | {rec['type']} | {rec['status']}")
```
Filter by status:  

```
response = client.list_recommendations(statusFilter="COMPLETED")

for rec in response["recommendationSummaries"]:
    print(f"{rec['recommendationId']}  {rec['name']}  {rec['status']}")
```
Paginate through all results:  

```
paginator = client.get_paginator("list_recommendations")
for page in paginator.paginate(statusFilter="COMPLETED"):
    for rec in page["recommendationSummaries"]:
        print(rec["recommendationId"])
```

## Request parameters
<a name="list-rec-params"></a>


| Parameter | Type | Required | Description | 
| --- | --- | --- | --- | 
|  `maxResults`  | Integer | No | Maximum number of results per page. Range: 1–100. | 
|  `nextToken`  | String | No | Pagination token from a previous response. | 
|  `statusFilter`  | String | No | Filter by status. One of: `PENDING`, `IN_PROGRESS`, `COMPLETED`, `FAILED`, `DELETING`. | 

## Response
<a name="list-rec-response"></a>


| Field | Type | Description | 
| --- | --- | --- | 
|  `recommendationSummaries`  | List | List of recommendation summaries. | 
|  `nextToken`  | String | Pagination token for the next page. Absent when there are no more results. | 

### Recommendation summary fields
<a name="list-rec-summary-fields"></a>


| Field | Type | Description | 
| --- | --- | --- | 
|  `recommendationId`  | String | Unique identifier. | 
|  `recommendationArn`  | String | ARN of the recommendation. | 
|  `name`  | String | The recommendation name. | 
|  `description`  | String | Optional description, if provided. | 
|  `type`  | String |  `SYSTEM_PROMPT_RECOMMENDATION` or `TOOL_DESCRIPTION_RECOMMENDATION`. | 
|  `status`  | String | Current status: `PENDING`, `IN_PROGRESS`, `COMPLETED`, `FAILED`, `DELETING`. | 
|  `createdAt`  | Timestamp | When the recommendation was created. | 
|  `updatedAt`  | Timestamp | When the recommendation was last updated. | 

To retrieve the full details and results of a recommendation, use [Get a recommendation](recommendations-get.md) with the `recommendationId`.

## Errors
<a name="list-rec-errors"></a>


| Error | HTTP status | Description | 
| --- | --- | --- | 
|  `ValidationException`  | 400 | Invalid pagination parameters or status filter value. | 
|  `AccessDeniedException`  | 403 | Insufficient permissions. | 
|  `ThrottlingException`  | 429 | Request rate exceeded. | 
|  `InternalServerException`  | 500 | Service-side error. | 