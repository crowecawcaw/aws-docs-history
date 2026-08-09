# Identity and access management for Web Search

Web Search on Amazon Bedrock uses AWS Identity and Access Management (IAM) to control who can run searches and fetches
and in which Regions. This page describes the service's IAM prefix, actions, AWS managed
policies, condition keys, example policies, and the controls administrators use to disable Web
Search.

The IAM service prefix for Web Search is `bedrock-websearch`. Use this prefix
when you write policy statements, for example
`bedrock-websearch:InvokeSearch`.

## Actions

Web Search supports three actions.

| **Action**                            | **Description**                                                                                                                                    | **Access level** |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| `bedrock-websearch:InvokeSearch`      | Issue a search query. Returns URLs, titles, and snippets from the Amazon Bedrock web<br>index. Does not make outbound calls.                       | Read / Write     |
| `bedrock-websearch:InvokeFetch`       | Retrieve cached page content for a specific URL from the Amazon Bedrock cache. Does not<br>make live outbound calls.                               | Read / Write     |
| `bedrock-websearch:ExternalWebAccess` | Governs whether search and fetch may access the external web in addition to the<br>Amazon Bedrock web index and cache. Applies to both operations. | Read / Write     |

All three actions support the `*` resource type.

The model decides when to call search and when to call fetch based on its reasoning over
each request and the responses to previous tool calls. Both tools are exposed to the model
whenever `web_search` is added to a request; IAM permissions don't change what the
model sees, and each permission is evaluated only when the model actually attempts that call.
When a call is denied, the model continues with the information it already has and tells you if
it couldn't retrieve enough current information to answer.

The two actions grant different capabilities. With
`InvokeSearch` but not `InvokeFetch`, the model can run searches and
ground its answer in the titles, URLs, and snippets that search returns, but cannot read the
cached content of a page. With `InvokeFetch` but not `InvokeSearch`, the
model cannot run searches to discover sources, but fetch still applies to any URL the model
produces — one you provide in your request or one the model generates from its own
knowledge — subject to that content being in the Amazon Bedrock cache. Fetch is not limited to
URLs you supply, so if you intend to constrain the model to specific sources, restricting
`InvokeSearch` alone does not achieve that.

## Managed policies

Web Search provides the following AWS managed policies.

| **Managed policy**                         | **Grants**                                                                                                                                                                                                   |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `AmazonBedrockWebSearchFullAccess`         | Search and cached fetch actions only. No external web access with this<br>policy.                                                                                                                            |
| `AmazonBedrockWebSearchReadOnly`           | Search and cached fetch actions in a read-only variant, with no external web access.<br>Provided for parity with other AWS services and for policy automation that expects a<br>ReadOnly policy per service. |
| `AmazonBedrockExternalWebSearchFullAccess` | All Web Search actions, including `ExternalWebAccess`, with no<br>condition-key restrictions. Intended for unrestricted use.                                                                                 |
| `AmazonBedrockExternalWebSearchReadOnly`   | All Web Search actions, including `ExternalWebAccess`, in a read-only<br>variant. Provided for parity with other AWS services and for policy automation that<br>expects a ReadOnly policy per service.       |

In addition to the web-search-specific policies above, the basic Web Search actions
(`bedrock-websearch:InvokeSearch` and `bedrock-websearch:InvokeFetch`)
have been added to the following AWS managed policies:

- `AmazonBedrockFullAccess`
- `AmazonMantleFullAccess`
- `AmazonBedrockLimitedAccess`
- `AmazonBedrockMantleInferenceAccess`

None of these general policies grant `bedrock-websearch:ExternalWebAccess`, so
identities that hold them can use Search and cached Fetch without an additional policy change,
while retrieval from the live web must be granted explicitly.
`AmazonBedrockFullAccess` is distinct from
`AmazonBedrockExternalWebSearchFullAccess`, which grants all Web Search actions
including `ExternalWebAccess`; `AmazonBedrockWebSearchFullAccess`, by
contrast, grants search and cached fetch only.

## Condition key

Web Search provides the following IAM condition key:

| **Condition key**     | **Applies to** | **Description**                                                                            |
| --------------------- | -------------- | ------------------------------------------------------------------------------------------ |
| `aws:RequestedRegion` | Both actions   | Restrict Web Search to specific Regions. This is the standard AWS global condition<br>key. |

## Disable Web Search

Administrators can turn off Web Search at several scopes.

| **Scope**    | **Mechanism**                                                                                             |
| ------------ | --------------------------------------------------------------------------------------------------------- |
| Organization | A Service Control Policy (SCP) that denies all `bedrock-websearch` actions<br>across an AWS Organization. |
| Account      | A standard IAM deny on the `bedrock-websearch` actions.                                                   |
| Region       | A deny that uses the `aws:RequestedRegion` condition key.                                                 |

The model decides when to call search and when to call fetch based on the content of each
request. Before you restrict or disable either action, test your specific request patterns to
understand which operations they trigger. That way you can confirm a policy change has the
effect you intend and does not unexpectedly degrade responses.

## Example policies

**Allow search and cached fetch in a specific Region**

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowWebSearchInRegion",
      "Effect": "Allow",
      "Action": [
        "bedrock-websearch:InvokeSearch",
        "bedrock-websearch:InvokeFetch"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:RequestedRegion": "us-west-2"
        }
      }
    }
  ]
}
```

**Allow search, cached fetch, and external web
access**

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowWebSearchWithExternalAccess",
      "Effect": "Allow",
      "Action": [
        "bedrock-websearch:InvokeSearch",
        "bedrock-websearch:InvokeFetch",
        "bedrock-websearch:ExternalWebAccess"
      ],
      "Resource": "*"
    }
  ]
}
```

**Allow cached fetch only**

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowCachedFetch",
      "Effect": "Allow",
      "Action": [
        "bedrock-websearch:InvokeFetch"
      ],
      "Resource": "*"
    }
  ]
}
```

**Deny Web Search across an organization (SCP)**

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyAllWebSearch",
      "Effect": "Deny",
      "Action": "bedrock-websearch:*",
      "Resource": "*"
    }
  ]
}
```
