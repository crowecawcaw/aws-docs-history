

# Get started with AgentCore Web Search

To search the web with AgentCore Web Search, grant a principal permission to call the `InvokeWebSearch` API, and then call it with the AWS SDKs or the AWS Command Line Interface (AWS CLI).

## Prerequisites
<a name="web-search-api-prerequisites"></a>

Before you call the API, make sure that you have the following:
+ An AWS account and credentials that the AWS SDKs or the AWS CLI can use.
+ An AWS Region where the API is available. For the list, see [Regions](web-search-api.md#web-search-api-regions).
+ A current version of the AWS SDK for Python (Boto3) or the AWS CLI. Earlier versions don’t include the `InvokeWebSearch` operation.
+ Permission to call the API, as described in the following section.

## Grant permission to call the API
<a name="web-search-api-permissions"></a>

To call the API, an AWS Identity and Access Management (IAM) principal needs the `bedrock-agentcore:InvokeWebSearch` permission on the AWS managed web search tool. The tool’s Amazon Resource Name (ARN) has the following form:

```text
arn:aws:bedrock-agentcore:<Region>:aws:tool/web-search.v1
```

The account field of the ARN is the literal value `aws`, because AWS owns the tool. It is not your account ID.

The following identity-based policy allows a principal to call the API in one Region. Replace `<Region>` with the code of a Region from [Regions](web-search-api.md#web-search-api-regions). To allow calls in every Region, use `*` in place of the Region code.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowInvokeWebSearch",
            "Effect": "Allow",
            "Action": "bedrock-agentcore:InvokeWebSearch",
            "Resource": "arn:aws:bedrock-agentcore:<Region>:aws:tool/web-search.v1"
        }
    ]
}
```

## Search the web
<a name="web-search-api-examples"></a>

Only `webSearchId` and `searchQuery` are required. The identifier of the AWS managed web search tool is `web-search.v1`. For an example of the response, see [Response](web-search-api-reference.md#web-search-api-response).

The following AWS SDK for Python (Boto3) and AWS CLI examples search for recent pages about a topic. They return up to five results, limit the results to two domains, and keep only pages published in January 2026:

**Example**  

```python
import boto3
from botocore.exceptions import ClientError

client = boto3.client("bedrock-agentcore", region_name="us-east-1")

try:
    response = client.invoke_web_search(
        webSearchId="web-search.v1",
        searchQuery="Amazon Bedrock AgentCore release announcements",
        maxResults=5,
        filters={
            "domainFilter": {
                "include": ["example.net", "example.org"]
            },
            "publishedDateFilter": {
                "publishedAfter": "2026-01-01T00:00:00Z",
                "publishedBefore": "2026-01-31T23:59:59Z"
            }
        }
    )
except ClientError as error:
    print(error.response["Error"]["Code"], error.response["Error"]["Message"])
    raise

for result in response["results"]:
    print(result.get("title"), result.get("url"))
    print(result["text"])
```

```bash
aws bedrock-agentcore invoke-web-search \
  --region us-east-1 \
  --web-search-id web-search.v1 \
  --search-query "Amazon Bedrock AgentCore release announcements" \
  --max-results 5 \
  --filters '{
    "domainFilter": {"include": ["example.net", "example.org"]},
    "publishedDateFilter": {
      "publishedAfter": "2026-01-01T00:00:00Z",
      "publishedBefore": "2026-01-31T23:59:59Z"
    }
  }'
```

For the request fields and their limits, see [Request and response](web-search-api-reference.md). For the full request and response syntax, see [InvokeWebSearch](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_InvokeWebSearch.html) in the *Amazon Bedrock AgentCore API Reference*.