# Actions, resources, and condition keys for Amazon Bedrock Web Search

Amazon Bedrock Web Search (service prefix: `bedrock-websearch`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../bedrock/latest/userguide/web-search.md "../../../bedrock/latest/userguide/web-search.md").
- View a list of the [API operations available for
  this service](${UserGuideDocPage}.md "${UserGuideDocPage}.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../bedrock/latest/userguide/security-web-search.md "../../../bedrock/latest/userguide/security-web-search.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/bedrock-websearch/bedrock-websearch.json "https://servicereference.us-east-1.amazonaws.com/v1/bedrock-websearch/bedrock-websearch.json") for this service.

###### Topics

- [Actions defined by Amazon Bedrock Web Search](#list_bedrock-websearch-actions-as-permissions "#list_bedrock-websearch-actions-as-permissions")
- [Permission-only actions for Amazon Bedrock Web Search](#list_bedrock-websearch-permission-only-actions "#list_bedrock-websearch-permission-only-actions")
- [Resource types defined by Amazon Bedrock Web Search](#list_bedrock-websearch-resources-for-iam-policies "#list_bedrock-websearch-resources-for-iam-policies")
- [Condition keys for Amazon Bedrock Web Search](#list_bedrock-websearch-policy-keys "#list_bedrock-websearch-policy-keys")

## Actions defined by Amazon Bedrock Web Search

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                                                     | Description                                  | Resource types (\*required)                                                             | Condition keys | Access level |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- | --------------------------------------------------------------------------------------- | -------------- | ------------ |
| [InvokeFetch](../../../bedrock/latest/userguide/security-web-search.md#security-web-search-actions "../../../bedrock/latest/userguide/security-web-search.md#security-web-search-actions")  | Grants permission to invoke web fetch tools  | [tool\*](#list_bedrock-websearch-resource-tool "#list_bedrock-websearch-resource-tool") |                | Read         |
| [InvokeSearch](../../../bedrock/latest/userguide/security-web-search.md#security-web-search-actions "../../../bedrock/latest/userguide/security-web-search.md#security-web-search-actions") | Grants permission to invoke web search tools | [tool\*](#list_bedrock-websearch-resource-tool "#list_bedrock-websearch-resource-tool") |                | Read         |

## Permission-only actions for Amazon Bedrock Web Search

The following actions are defined by Amazon Bedrock Web Search but are not directly
invocable through any API operation. They can only be used in IAM policy statements
to grant or deny permissions.

| Actions                                                                                                                                                                                          | Description                                                                            | Resource types (\*required) | Condition keys | Access level |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------- | --------------------------- | -------------- | ------------ |
| [ExternalWebAccess](../../../bedrock/latest/userguide/security-web-search.md#security-web-search-actions "../../../bedrock/latest/userguide/security-web-search.md#security-web-search-actions") | Grants permission to retrieve content from external web sites outside the AWS boundary |                             |                | Read         |

## Resource types defined by Amazon Bedrock Web Search

The following resource types are defined by this service and can be used in the
`Resource` element of IAM permission policy statements.

| Resource types                                                                                                                                                                      | ARN                                                               | Condition keys |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | -------------- |
| [tool](../../../bedrock/latest/userguide/security-web-search.md#security-web-search-actions "../../../bedrock/latest/userguide/security-web-search.md#security-web-search-actions") | arn:${Partition}:bedrock-websearch:${Region}:aws:tool/${ToolName} |                |

## Condition keys for Amazon Bedrock Web Search

Amazon Bedrock Web Search has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
