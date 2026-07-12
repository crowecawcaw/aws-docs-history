# Actions, resources, and condition keys for Amazon CloudFront KeyValueStore

Amazon CloudFront KeyValueStore (service prefix: `cloudfront-keyvaluestore`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../AmazonCloudFront/latest/DeveloperGuide.md "../../../AmazonCloudFront/latest/DeveloperGuide.md").
- View a list of the [API operations available for
  this service](../../../cloudfront/latest/APIReference.md "../../../cloudfront/latest/APIReference.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../AmazonCloudFront/latest/DeveloperGuide/security-iam.md "../../../AmazonCloudFront/latest/DeveloperGuide/security-iam.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/cloudfront-keyvaluestore/cloudfront-keyvaluestore.json "https://servicereference.us-east-1.amazonaws.com/v1/cloudfront-keyvaluestore/cloudfront-keyvaluestore.json") for this service.

###### Topics

- [API operations defined by Amazon CloudFront KeyValueStore](#list_cloudfront-keyvaluestore-operations "#list_cloudfront-keyvaluestore-operations")
- [Actions defined by Amazon CloudFront KeyValueStore](#list_cloudfront-keyvaluestore-actions-as-permissions "#list_cloudfront-keyvaluestore-actions-as-permissions")
- [Resource types defined by Amazon CloudFront KeyValueStore](#list_cloudfront-keyvaluestore-resources-for-iam-policies "#list_cloudfront-keyvaluestore-resources-for-iam-policies")
- [Condition keys for Amazon CloudFront KeyValueStore](#list_cloudfront-keyvaluestore-policy-keys "#list_cloudfront-keyvaluestore-policy-keys")

## API operations defined by Amazon CloudFront KeyValueStore

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_cloudfront-keyvaluestore-actions-as-permissions "#list_cloudfront-keyvaluestore-actions-as-permissions").

| Operation             | IAM action                                                                                                                                                                  | Condition key | Possible value(s) | Access level |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ----------------- | ------------ |
| DeleteKey             | [cloudfront-keyvaluestore:DeleteKey](#list_cloudfront-keyvaluestore-action-DeleteKey "#list_cloudfront-keyvaluestore-action-DeleteKey")                                     |               |                   | Write        |
| DescribeKeyValueStore | [cloudfront-keyvaluestore:DescribeKeyValueStore](#list_cloudfront-keyvaluestore-action-DescribeKeyValueStore "#list_cloudfront-keyvaluestore-action-DescribeKeyValueStore") |               |                   | Read         |
| GetKey                | [cloudfront-keyvaluestore:GetKey](#list_cloudfront-keyvaluestore-action-GetKey "#list_cloudfront-keyvaluestore-action-GetKey")                                              |               |                   | Read         |
| ListKeys              | [cloudfront-keyvaluestore:ListKeys](#list_cloudfront-keyvaluestore-action-ListKeys "#list_cloudfront-keyvaluestore-action-ListKeys")                                        |               |                   | List         |
| PutKey                | [cloudfront-keyvaluestore:PutKey](#list_cloudfront-keyvaluestore-action-PutKey "#list_cloudfront-keyvaluestore-action-PutKey")                                              |               |                   | Write        |
| UpdateKeys            | [cloudfront-keyvaluestore:UpdateKeys](#list_cloudfront-keyvaluestore-action-UpdateKeys "#list_cloudfront-keyvaluestore-action-UpdateKeys")                                  |               |                   | Write        |

## Actions defined by Amazon CloudFront KeyValueStore

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                                      | Description                                                                                       | Resource types (\*required)                                                                                                            | Condition keys | Access level |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ------------ |
| [DeleteKey](../../../cloudfront/latest/APIReference/API_kvs_DeleteKey.md "../../../cloudfront/latest/APIReference/API_kvs_DeleteKey.md")                                     | Grants permission to delete the key value pair specified by the key                               | [key-value-store\*](#list_cloudfront-keyvaluestore-resource-key-value-store "#list_cloudfront-keyvaluestore-resource-key-value-store") |                | Write        |
| [DescribeKeyValueStore](../../../cloudfront/latest/APIReference/API_kvs_DescribeKeyValueStore.md "../../../cloudfront/latest/APIReference/API_kvs_DescribeKeyValueStore.md") | Grants permission to return metadata information about Key Value Store                            | [key-value-store\*](#list_cloudfront-keyvaluestore-resource-key-value-store "#list_cloudfront-keyvaluestore-resource-key-value-store") |                | Read         |
| [GetKey](../../../cloudfront/latest/APIReference/API_kvs_GetKey.md "../../../cloudfront/latest/APIReference/API_kvs_GetKey.md")                                              | Grants permission to return a key value pair                                                      | [key-value-store\*](#list_cloudfront-keyvaluestore-resource-key-value-store "#list_cloudfront-keyvaluestore-resource-key-value-store") |                | Read         |
| [ListKeys](../../../cloudfront/latest/APIReference/API_kvs_ListKeys.md "../../../cloudfront/latest/APIReference/API_kvs_ListKeys.md")                                        | Grants permission to returns a list of key value pairs                                            | [key-value-store\*](#list_cloudfront-keyvaluestore-resource-key-value-store "#list_cloudfront-keyvaluestore-resource-key-value-store") |                | List         |
| [PutKey](../../../cloudfront/latest/APIReference/API_kvs_PutKey.md "../../../cloudfront/latest/APIReference/API_kvs_PutKey.md")                                              | Grants permission to create a new key value pair or replace the value of an existing key          | [key-value-store\*](#list_cloudfront-keyvaluestore-resource-key-value-store "#list_cloudfront-keyvaluestore-resource-key-value-store") |                | Write        |
| [UpdateKeys](../../../cloudfront/latest/APIReference/API_kvs_UpdateKeys.md "../../../cloudfront/latest/APIReference/API_kvs_UpdateKeys.md")                                  | Grants permission to put or delete multiple key value pairs in a single, all-or-nothing operation | [key-value-store\*](#list_cloudfront-keyvaluestore-resource-key-value-store "#list_cloudfront-keyvaluestore-resource-key-value-store") |                | Write        |

## Resource types defined by Amazon CloudFront KeyValueStore

The following resource types are defined by this service and can be used in the
`Resource` element of IAM permission policy statements.

| Resource types                                                                                                                                                   | ARN                                                                   | Condition keys |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- | -------------- |
| [key-value-store](../../../AmazonCloudFront/latest/DeveloperGuide/kvs-with-functions.md "../../../AmazonCloudFront/latest/DeveloperGuide/kvs-with-functions.md") | arn:${Partition}:cloudfront::${Account}:key-value-store/${ResourceId} |                |

## Condition keys for Amazon CloudFront KeyValueStore

Amazon CloudFront KeyValueStore has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
