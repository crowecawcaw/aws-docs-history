# Web Search

Web Search is a built-in tool that provides web search capability in Amazon Bedrock. When you
enable it, supported models can retrieve current information from the web during a request and
use it to ground their answers, instead of relying only on the data they were trained on.
Responses include citations to the sources the model used. Web Search is hosted and built by
AWS, and your data stays within the AWS boundary by default.

## Data governance

By default, when using the [AmazonBedrockFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonBedrockFullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonBedrockFullAccess") policy, Web Search is served from the Amazon Bedrock web index and
cache, and your request data does not leave the AWS boundary for retrieval. You can also use
IAM to enforce this at the policy level. Depending on the model you are using, your data is
subject to the automated [Amazon Bedrock abuse detection](abuse-detection.md "abuse-detection.md")
mechanisms.

## When to use Web Search

Web Search is useful whenever an answer depends on information that is more recent, more
specialized, or more authoritative than a model's parametric knowledge. Recency is one common
case: current events, recent product releases, prices, or documentation for a new library
version. It is equally useful for long-tail or specialized questions where the model's knowledge
is thin or imprecise, such as niche APIs, specific configuration values, or domain-specific
facts, and for cases where you want a grounded, citable source rather than a
recollection.

## How Web Search works

Because the tool runs inside Amazon Bedrock, you do not need to host a search index, manage
crawlers, or write the tool-call loop yourself. You add the tool to your Amazon Bedrock inference request,
and the model invokes it as needed. Web Search provides current information to the model,
enabling the model to return grounded answers with citations.

When Web Search is enabled, the model decides whether a request needs current information.
If it does, the model issues one or more search queries to the Web Search tool and receives a
set of observations drawn from a web index built and maintained by Amazon. Each observation
includes a title, a source URL, and a content snippet. The model then composes an answer
grounded in those results and adds citations that point back to the sources.

If the first set of results is not enough to answer the question, the model can
reformulate its query using what it found and search again within the same turn. When the
results do not support an answer, the model tells you so rather than filling the gap from its
training data.

### Search and Fetch operations

Web Search is built from two operations:

- **Search** – Returns titles, URLs, and snippets from
  the Amazon Bedrock web index and knowledge graph for high-confidence facts.
- **Fetch** – Retrieves cached page content for a
  specific URL from the Amazon Bedrock cache. If the result is unavailable in the cache, the model
  may choose to either notify you or build a response based on the best information it
  has.

By default, both operations are served entirely from within the AWS service boundary
using the Amazon Bedrock web index and cache, a snapshot of web content hosted inside AWS, rather
than fetching from the live web at request time. The `external_web_access`
parameter in the Responses API and the `bedrock-websearch:ExternalWebAccess` IAM
permission govern whether search and fetch may reach the external web directly. For details,
see [Controlling external web access](#web-search-controlling-external "#web-search-controlling-external").

### Supported models

Web Search is available for OpenAI GPT models served through the Amazon Bedrock
`bedrock-mantle` endpoint, using the Responses API. It is currently supported on
`openai.gpt-5.4`, `openai.gpt-5.5`, and `openai.gpt-5.6`
(luna, terra, and sol). For Web Search pricing, refer to the [Amazon Bedrock pricing page](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/").

### Regional availability

Web Search processes queries in-Region in three US Regions:

| **Region**            | **Region code** |
| --------------------- | --------------- |
| US East (N. Virginia) | `us-east-1`     |
| US East (Ohio)        | `us-east-2`     |
| US West (Oregon)      | `us-west-2`     |

Web Search is strictly regional. Each Region operates its own search and fetch tier, and
queries, fetches, index data, and results are not routed across Regions. A query issued in a
given Region stays within that Region's boundary.

## Enable Web Search

To use Web Search, the IAM identity behind your request must be allowed to call the Web
Search actions. For the required permissions and example policies, see [Identity and access management for Web Search](security-web-search.md "security-web-search.md").

### Set your environment

Set the following before running the examples:

```
export OPENAI_API_KEY="your-amazon-bedrock-api-key"
export OPENAI_BASE_URL="https://bedrock-mantle.us-west-2.api.aws/openai/v1"
```

### Add the Web Search tool to a request

To enable Web Search, add a tool of type `web_search` to the
`tools` array in your request. The model uses the tool only when it determines the
request needs current information. For runnable examples, see [Code examples](#web-search-code-examples "#web-search-code-examples").

## Controlling external web access

By default, Web Search is served entirely from the Amazon Bedrock web index and cache, and no
request data leaves the AWS boundary for retrieval. Whether search and fetch may reach the
external web is governed by two controls that work together: the
`external_web_access` parameter in the Responses API and the
`bedrock-websearch:ExternalWebAccess` IAM permission.

The `external_web_access` parameter defaults to `true`, matching the
OpenAI Responses API so that your call does not have to change. The [AmazonBedrockFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonBedrockFullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonBedrockFullAccess") policy
grants the basic Web Search actions — `bedrock-websearch:InvokeSearch` and
`bedrock-websearch:InvokeFetch` — but does not grant
`bedrock-websearch:ExternalWebAccess`. As a result, a request that leaves
`external_web_access` at `true` from an identity that does not hold
`ExternalWebAccess` returns a `403 AccessDenied` on the authorization
check. The model does not fail the request: it grounds its answer in Search and cached Fetch
and reports that it could not obtain external web access.

To make a request that does not hit this error, use one of the two approaches
below.

### Keep requests within the AWS boundary

Set `"external_web_access": false` on the tool. This does not require the
`ExternalWebAccess` permission, retrieval is served entirely from the Amazon Bedrock web
index and cache, and your request data does not leave the AWS boundary. Because
[AmazonBedrockFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonBedrockFullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonBedrockFullAccess")
does not grant `ExternalWebAccess`, this configuration is safe by default.

```
response = client.responses.create(
    model="openai.gpt-5.5",
    input="Summarize recent guidance on AWS Lambda cold starts.",
    tools=[{"type": "web_search", "external_web_access": False}],
)
```

```
curl "https://bedrock-mantle.us-west-2.api.aws/openai/v1/responses" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "openai.gpt-5.5",
    "input": "Summarize recent guidance on AWS Lambda cold starts.",
    "tools": [{"type": "web_search", "external_web_access": false}]
  }'
```

### Enable external web access

Grant `bedrock-websearch:ExternalWebAccess` to the request identity and leave
`external_web_access` at its default of `true`. This configuration
governs whether search and fetch may reach the external web. Today, retrieval is served
entirely from the Amazon Bedrock web index and cache, so no request data leaves the AWS boundary
even when this permission is granted. In a future release, this configuration may allow
search and fetch to retrieve content from the live external web, at which point request data
may leave the AWS boundary. External web access is disabled by default (that is,
`bedrock-websearch:ExternalWebAccess` is disallowed), and any future change will
require allowing `bedrock-websearch:ExternalWebAccess` as an explicit opt-in
before it takes effect. External web access remains under your control: it applies only
because you granted the permission and left the parameter enabled.

## Code examples

### Responses API

```
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="openai.gpt-5.5",
    input="What are the most significant AWS launches announced this month?",
    tools=[{"type": "web_search", "external_web_access": False}],
)

print(response.output_text)
```

The response includes the grounded answer text together with
`url_citation` annotations that point back to the sources:

```
{
  "content": [
    {
      "annotations": [
        {
          "end_index": 573,
          "start_index": 441,
          "title": "Upgrade Amazon EKS clusters with confidence using Kubernetes version rollbacks | AWS News Blog",
          "type": "url_citation",
          "url": "https://aws.amazon.com/blogs/aws/upgrade-amazon-eks-clusters-with-confidence-using-kubernetes-version-rollbacks/"
        },
        {
          "end_index": 1094,
          "start_index": 888,
          "title": "AWS Weekly Roundup: AWS Builder Center at 1 year, Network Scanning in Security Hub, Loom for AWS, and more (July 13, 2026) | AWS News Blog",
          "type": "url_citation",
          "url": "https://aws.amazon.com/blogs/aws/aws-weekly-roundup-aws-builder-center-at-one-year-network-scanning-in-security-hub-loom-for-aws-and-more-july-13-2026/"
        },
        {
          "end_index": 1837,
          "start_index": 1414,
          "title": "AWS Weekly Roundup: One-click Lambda setup prompt, OpenAI GPT-5.6 models on Bedrock, and more (July 20, 2026) | AWS News Blog",
          "type": "url_citation",
          "url": "https://aws.amazon.com/blogs/aws/aws-weekly-roundup-one-click-lambda-setup-prompt-openai-gpt-5-6-models-on-bedrock-and-more-july-20-2026/"
        }
      ],
      "logprobs": [],
      "text": "As of **July 30, 2026**, the most significant AWS launches this month:\n\n1. **Amazon EKS Kubernetes version rollbacks** — EKS now lets admins roll back a Kubernetes version upgrade within **seven days**, effectively adding an “undo” path for cluster upgrades and reducing upgrade risk for large or regulated Kubernetes fleets. It’s available at no additional cost in commercial Regions where EKS is available. ([aws.amazon.com](https://aws.amazon.com/blogs/aws/upgrade-amazon-eks-clusters-with-confidence-using-kubernetes-version-rollbacks/))\n\n2. **AWS Security Hub Network Scanning + Azure support** — Security Hub added active Network Scanning to find resources actually reachable from the public internet, and also expanded unified security management to **Microsoft Azure** resources, making this a notable multi-cloud security/posture-management move. ([aws.amazon.com](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-aws-builder-center-at-one-year-network-scanning-in-security-hub-loom-for-aws-and-more-july-13-2026/))\n\n3. **New frontier models on Amazon Bedrock: Claude Sonnet 5, Claude Opus 5, and OpenAI GPT-5.6 models** — AWS added major new model choices to Bedrock this month: Anthropic’s Claude Sonnet 5 and Claude Opus 5, plus OpenAI GPT-5.6 Sol, Terra, and Luna, expanding Bedrock’s role as a multi-model enterprise AI platform. ([aws.amazon.com](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-one-click-lambda-setup-prompt-openai-gpt-5-6-models-on-bedrock-and-more-july-20-2026/))",
      "type": "output_text"
    }
  ],
  "id": "msg_dcda8e4b477f5a1d96bfbcadefef7a77",
  "phase": "final_answer",
  "role": "assistant",
  "status": "completed",
  "type": "message"
}
```

### Direct HTTPS request

If you are not using the OpenAI SDK, send the request directly to the Responses endpoint.
The `tools` field carries the Web Search tool.

```
curl "https://bedrock-mantle.us-west-2.api.aws/openai/v1/responses" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "openai.gpt-5.5",
    "input": "What are the most significant AWS launches announced this month?",
    "tools": [{"type": "web_search", "external_web_access": false}]
  }'
```

### Reading citations from the response

Web Search returns citations as `url_citation` annotations attached to the
text. Each annotation carries the source title and URL and the character span in the answer
it supports. Retain and display these to end users.

```
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="openai.gpt-5.5",
    input="What are the most significant AWS launches announced this month?",
    tools=[{"type": "web_search", "external_web_access": False}],
)

# The grounded answer
print(response.output_text)

# The sources behind it
for item in response.output:
    if item.type == "message":
        for block in item.content:
            if block.type == "output_text":
                for ann in block.annotations:
                    if ann.type == "url_citation":
                        print(f"- {ann.title}: {ann.url}")
```

If you are working with the raw JSON (for example, from a direct HTTPS call), the same
data lives at `output[].content[].annotations[]`:

```
jq '.output[] | select(.type=="message") | .content[]
      | select(.type=="output_text") | .annotations[]
      | select(.type=="url_citation") | {title, url, start_index, end_index}' response.json
```

### Streaming responses

The Responses API streams the answer as it is generated. Text arrives as
`response.output_text.delta` events, and each citation arrives as a
`response.output_text.annotation.added` event as the model grounds a
statement.

```
from openai import OpenAI

client = OpenAI()

stream = client.responses.create(
    model="openai.gpt-5.5",
    input="What are the most significant AWS launches announced this month?",
    tools=[{"type": "web_search", "external_web_access": False}],
    stream=True,
)

for event in stream:
    if event.type == "response.output_text.delta":
        print(event.delta, end="", flush=True)
    elif event.type == "response.output_text.annotation.added":
        ann = event.annotation
        print(f"\n[source] {ann['title']}: {ann['url']}")
```

Over the wire, the annotation event looks like this:

```
event: response.output_text.annotation.added
data: {"type":"response.output_text.annotation.added","annotation":{"type":"url_citation","title":"News and Updates from the July 2025 Pokémon Presents","url":"https://www.pokemon.com/us/pokemon-news/...","start_index":589,"end_index":698},"annotation_index":2,"content_index":0,"item_id":"msg_...","output_index":1}
```

## Security

Web Search on Amazon Bedrock uses AWS Identity and Access Management (IAM) to control who can run searches and fetches
and in which Regions. The IAM service prefix for Web Search is
`bedrock-websearch`. For the full list of actions, managed policies, condition keys,
example policies, and administrator controls for disabling Web Search, see [Identity and access management for Web Search](security-web-search.md "security-web-search.md").

## Monitoring with CloudTrail

Web Search on Amazon Bedrock is integrated with AWS CloudTrail. CloudTrail captures API activity for Web
Search as data events, so you can audit who invoked the tool, when, and from where. For the
fields captured, how to enable data event logging, and what is intentionally excluded, see
[Monitor Web Search](monitoring-web-search.md "monitoring-web-search.md").

## Acceptable use

If you use Web Search on Amazon Bedrock, Amazon Bedrock provides Web Search results (“Search
Results”) to supported models, which the model may use to generate its response. You are
responsible for your use, and any use by your end users, of model outputs that incorporate
Search Results. You must retain and display the source citations and links provided in model
outputs in any output you surface to your end users. You may not use Web Search to (a) extract,
store, or reproduce content from Search Results in bulk, or (b) build or populate a competing
index or database.
