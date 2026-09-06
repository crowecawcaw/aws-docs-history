

# Actions, resources, and condition keys for Amazon API Gateway
<a name="list_apigatewaymanagementapi"></a>

Amazon API Gateway (service prefix: `execute-api`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/apigateway/latest/api/API_Operations.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-to-api.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/execute-api/execute-api.json) for this service.

**Topics**
+ [Actions defined by Amazon API Gateway](#list_apigatewaymanagementapi-actions-as-permissions)
+ [Resource types defined by Amazon API Gateway](#list_apigatewaymanagementapi-resources-for-iam-policies)
+ [Condition keys for Amazon API Gateway](#list_apigatewaymanagementapi-policy-keys)

## Actions defined by Amazon API Gateway
<a name="list_apigatewaymanagementapi-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [InvalidateCache](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-caching.html)  **
  - **Description:** Grants permission to invalidate API cache upon a client request
  - **Resource types (\*required):** [execute-api-general\*](#list_apigatewaymanagementapi-resource-execute-api-general)
  - **Condition keys:** [execute-api:viaDomainArn](#list_apigatewaymanagementapi-execute-api_viaDomainArn)
  - **Access level:** Write

- **   [Invoke](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-call-api.html)  **
  - **Description:** Grants permission to invoke an API upon a client request
  - **Resource types (\*required):** [execute-api-domain](#list_apigatewaymanagementapi-resource-execute-api-domain) / **Condition keys:**  
  - **Resource types (\*required):** [execute-api-general](#list_apigatewaymanagementapi-resource-execute-api-general) / **Condition keys:** [execute-api:viaDomainArn](#list_apigatewaymanagementapi-execute-api_viaDomainArn)
  - **Access level:** Write

- **   [ManageConnections](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-control-access-iam.html)  **
  - **Description:** Grants permission to access the Websocket @connections Route
  - **Resource types (\*required):** [execute-api-general\*](#list_apigatewaymanagementapi-resource-execute-api-general)
  - **Condition keys:** [execute-api:viaDomainArn](#list_apigatewaymanagementapi-execute-api_viaDomainArn)
  - **Access level:** Write



## Resource types defined by Amazon API Gateway
<a name="list_apigatewaymanagementapi-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [execute-api-domain](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | arn:${Partition}:execute-api:${Region}:${Account}:/domainnames/${DomainName}\+${DomainIdentifier} |   | 
|  [execute-api-general](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | arn:${Partition}:execute-api:${Region}:${Account}:${ApiId}/${Stage}/${Method}/${ApiSpecificResourcePath} | [execute-api:viaDomainArn](#list_apigatewaymanagementapi-execute-api_viaDomainArn) | 

## Condition keys for Amazon API Gateway
<a name="list_apigatewaymanagementapi-policy-keys"></a>

Amazon API Gateway defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [execute-api:viaDomainArn](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_service-with-iam.html)  | Filters access by the DomainName ARN the API is called from | ARN | 