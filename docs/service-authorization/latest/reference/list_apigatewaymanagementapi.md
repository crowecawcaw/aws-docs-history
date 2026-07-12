# Actions, resources, and condition keys for Amazon API Gateway

Amazon API Gateway (service prefix: `execute-api`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../apigateway/latest/developerguide/welcome.md "../../../apigateway/latest/developerguide/welcome.md").
- View a list of the [API operations available for
  this service](../../../apigateway/latest/api/API_Operations.md "../../../apigateway/latest/api/API_Operations.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../apigateway/latest/developerguide/apigateway-control-access-to-api.md "../../../apigateway/latest/developerguide/apigateway-control-access-to-api.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/execute-api/execute-api.json "https://servicereference.us-east-1.amazonaws.com/v1/execute-api/execute-api.json") for this service.

###### Topics

- [Actions defined by Amazon API Gateway](#list_apigatewaymanagementapi-actions-as-permissions "#list_apigatewaymanagementapi-actions-as-permissions")
- [Resource types defined by Amazon API Gateway](#list_apigatewaymanagementapi-resources-for-iam-policies "#list_apigatewaymanagementapi-resources-for-iam-policies")
- [Condition keys for Amazon API Gateway](#list_apigatewaymanagementapi-policy-keys "#list_apigatewaymanagementapi-policy-keys")

## Actions defined by Amazon API Gateway

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                                                          | Description                                                                                                                                 | Resource types (\*required)                                                                                                                      | Condition keys                                                                                                                              | Access level |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| [InvalidateCache](../../../apigateway/latest/developerguide/api-gateway-caching.md "../../../apigateway/latest/developerguide/api-gateway-caching.md")                                           | Grants permission to invalidate API cache upon a client request                                                                             | [execute-api-general\*](#list_apigatewaymanagementapi-resource-execute-api-general "#list_apigatewaymanagementapi-resource-execute-api-general") | [execute-api:viaDomainArn](#list_apigatewaymanagementapi-execute-api_viaDomainArn "#list_apigatewaymanagementapi-execute-api_viaDomainArn") | Write        |
| [Invoke](../../../apigateway/latest/developerguide/how-to-call-api.md "../../../apigateway/latest/developerguide/how-to-call-api.md")                                                            | Grants permission to invoke an API upon a client request                                                                                    | [execute-api-domain](#list_apigatewaymanagementapi-resource-execute-api-domain "#list_apigatewaymanagementapi-resource-execute-api-domain")      |                                                                                                                                             | Write        |
| [execute-api-general](#list_apigatewaymanagementapi-resource-execute-api-general "#list_apigatewaymanagementapi-resource-execute-api-general")                                                   | [execute-api:viaDomainArn](#list_apigatewaymanagementapi-execute-api_viaDomainArn "#list_apigatewaymanagementapi-execute-api_viaDomainArn") |
| [ManageConnections](../../../apigateway/latest/developerguide/apigateway-websocket-control-access-iam.md "../../../apigateway/latest/developerguide/apigateway-websocket-control-access-iam.md") | Grants permission to access the Websocket @connections Route                                                                                | [execute-api-general\*](#list_apigatewaymanagementapi-resource-execute-api-general "#list_apigatewaymanagementapi-resource-execute-api-general") | [execute-api:viaDomainArn](#list_apigatewaymanagementapi-execute-api_viaDomainArn "#list_apigatewaymanagementapi-execute-api_viaDomainArn") | Write        |

## Resource types defined by Amazon API Gateway

The following resource types are defined by this service and can be used in the
`Resource` element of IAM permission policy statements.

| Resource types                                                                                                                                                                 | ARN                                                                                                      | Condition keys                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| [execute-api-domain](../../../apigateway/latest/developerguide/security_iam_service-with-iam.md "../../../apigateway/latest/developerguide/security_iam_service-with-iam.md")  | arn:${Partition}:execute-api:${Region}:${Account}:/domainnames/${DomainName}+${DomainIdentifier}         |                                                                                                                                             |
| [execute-api-general](../../../apigateway/latest/developerguide/security_iam_service-with-iam.md "../../../apigateway/latest/developerguide/security_iam_service-with-iam.md") | arn:${Partition}:execute-api:${Region}:${Account}:${ApiId}/${Stage}/${Method}/${ApiSpecificResourcePath} | [execute-api:viaDomainArn](#list_apigatewaymanagementapi-execute-api_viaDomainArn "#list_apigatewaymanagementapi-execute-api_viaDomainArn") |

## Condition keys for Amazon API Gateway

Amazon API Gateway defines the following condition keys that can be used in the
`Condition` element of an IAM policy.

| Condition keys                                                                                                                                                                      | Description                                                 | Type |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | ---- |
| [execute-api:viaDomainArn](../../../apigateway/latest/developerguide/security_iam_service-with-iam.md "../../../apigateway/latest/developerguide/security_iam_service-with-iam.md") | Filters access by the DomainName ARN the API is called from | ARN  |
