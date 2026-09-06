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

| **Action**                            | **Description**                                                                                                                                                                  | **Access level** |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| `bedrock-websearch:InvokeSearch`      | Issue a search query. Returns URLs, titles, and snippets from the Amazon Bedrock web<br>index. Does not make outbound calls.                                                     | Read / Write     |
| `bedrock-websearch:InvokeFetch`       | Retrieve page content for a specific URL. Fetch uses the Amazon Bedrock cache only unless<br>the request also enables external web access and the identity is allowed to use it. | Read / Write     |
| `bedrock-websearch:ExternalWebAccess` | Allow Fetch to retrieve from the external web after a cache miss. Search continues to<br>use the Amazon Bedrock web index.                                                       | Read / Write     |

All three actions support the `*` resource type.

The model decides when to call search and when to call fetch based on its reasoning over
each request and the responses to previous tool calls. Both tools are exposed to the model
whenever `web_search` is added to a request; IAM permissions don't change what the
model sees, and each permission is evaluated only when the model actually attempts that call.
When a call is denied, the model can continue with the information it already has or obtained
from another tool call. The model response is not guaranteed to disclose the denial. To audit
denied calls, enable CloudTrail data event logging for Web Search.

The two actions grant different capabilities. With
`InvokeSearch` but not `InvokeFetch`, the model can run searches and
ground its answer in the titles, URLs, and snippets that search returns, but cannot read the
cached content of a page. With `InvokeFetch` but not `InvokeSearch`, the
model cannot run searches to discover sources, but fetch still applies to any URL the model
produces — one you provide in your request or one the model generates from its own
knowledge — subject to the configured Fetch mode and permissions. Fetch is not limited to
URLs you supply, so if you intend to constrain the model to specific sources, restricting
`InvokeSearch` alone does not achieve that.

## Managed policies

Web Search provides the following AWS managed policies.

| **Managed policy**                         | **Grants**                                                                                                                                                                                                   |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `AmazonBedrockWebSearchFullAccess`         | Search and cached fetch actions only. No external web access with this<br>policy.                                                                                                                            |
| `AmazonBedrockWebSearchReadOnly`           | Search and cached fetch actions in a read-only variant, with no external web access.<br>Provided for parity with other AWS services and for policy automation that expects a<br>ReadOnly policy per service. |
| `AmazonBedrockExternalWebSearchFullAccess` | All three Web Search actions, including `ExternalWebAccess`, on all Web<br>Search resources.                                                                                                                 |
| `AmazonBedrockExternalWebSearchReadOnly`   | The same actions and resources as<br>`AmazonBedrockExternalWebSearchFullAccess`, under a ReadOnly policy name provided<br>for policy naming and automation conventions.                                      |

###### Important

The current versions of `AmazonBedrockExternalWebSearchReadOnly` and
`AmazonBedrockExternalWebSearchFullAccess` have identical effective permissions.
The ReadOnly policy does not restrict external web retrieval. Use a custom policy if you need a
narrower permission set.

In addition to the web-search-specific policies above, the basic Web Search actions
(`bedrock-websearch:InvokeSearch` and `bedrock-websearch:InvokeFetch`)
have been added to the following AWS managed policies:

- `AmazonBedrockFullAccess`
- `AmazonMantleFullAccess`
- `AmazonBedrockLimitedAccess`
- `AmazonBedrockMantleInferenceAccess`

None of these general policies grant `bedrock-websearch:ExternalWebAccess`.
Identities that hold them can use Search. To use cached Fetch without an additional policy
change, explicitly set `external_web_access` to `false`. If you leave the
parameter at its default of `true`, each Fetch attempt fails authorization before the
cache is read. Retrieval from the external web must be granted explicitly.
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
