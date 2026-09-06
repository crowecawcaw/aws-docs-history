

# Actions, resources, and condition keys for Amazon CloudFront KeyValueStore
<a name="list_cloudfront-keyvaluestore"></a>

Amazon CloudFront KeyValueStore (service prefix: `cloudfront-keyvaluestore`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/cloudfront/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/cloudfront-keyvaluestore/cloudfront-keyvaluestore.json) for this service.

**Topics**
+ [API operations defined by Amazon CloudFront KeyValueStore](#list_cloudfront-keyvaluestore-operations)
+ [Actions defined by Amazon CloudFront KeyValueStore](#list_cloudfront-keyvaluestore-actions-as-permissions)
+ [Resource types defined by Amazon CloudFront KeyValueStore](#list_cloudfront-keyvaluestore-resources-for-iam-policies)
+ [Condition keys for Amazon CloudFront KeyValueStore](#list_cloudfront-keyvaluestore-policy-keys)

## API operations defined by Amazon CloudFront KeyValueStore
<a name="list_cloudfront-keyvaluestore-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_cloudfront-keyvaluestore-actions-as-permissions).




- **   DeleteKey  **
  - **IAM action:**  [cloudfront-keyvaluestore:DeleteKey](#list_cloudfront-keyvaluestore-action-DeleteKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeKeyValueStore  **
  - **IAM action:**  [cloudfront-keyvaluestore:DescribeKeyValueStore](#list_cloudfront-keyvaluestore-action-DescribeKeyValueStore) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetKey  **
  - **IAM action:**  [cloudfront-keyvaluestore:GetKey](#list_cloudfront-keyvaluestore-action-GetKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListKeys  **
  - **IAM action:**  [cloudfront-keyvaluestore:ListKeys](#list_cloudfront-keyvaluestore-action-ListKeys) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutKey  **
  - **IAM action:**  [cloudfront-keyvaluestore:PutKey](#list_cloudfront-keyvaluestore-action-PutKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateKeys  **
  - **IAM action:**  [cloudfront-keyvaluestore:UpdateKeys](#list_cloudfront-keyvaluestore-action-UpdateKeys) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon CloudFront KeyValueStore
<a name="list_cloudfront-keyvaluestore-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [DeleteKey](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_kvs_DeleteKey.html)  **
  - **Description:** Grants permission to delete the key value pair specified by the key
  - **Resource types (\*required):** [key-value-store\*](#list_cloudfront-keyvaluestore-resource-key-value-store)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DescribeKeyValueStore](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_kvs_DescribeKeyValueStore.html)  **
  - **Description:** Grants permission to return metadata information about Key Value Store
  - **Resource types (\*required):** [key-value-store\*](#list_cloudfront-keyvaluestore-resource-key-value-store)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetKey](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_kvs_GetKey.html)  **
  - **Description:** Grants permission to return a key value pair
  - **Resource types (\*required):** [key-value-store\*](#list_cloudfront-keyvaluestore-resource-key-value-store)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListKeys](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_kvs_ListKeys.html)  **
  - **Description:** Grants permission to returns a list of key value pairs
  - **Resource types (\*required):** [key-value-store\*](#list_cloudfront-keyvaluestore-resource-key-value-store)
  - **Condition keys:**  
  - **Access level:** List

- **   [PutKey](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_kvs_PutKey.html)  **
  - **Description:** Grants permission to create a new key value pair or replace the value of an existing key
  - **Resource types (\*required):** [key-value-store\*](#list_cloudfront-keyvaluestore-resource-key-value-store)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateKeys](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_kvs_UpdateKeys.html)  **
  - **Description:** Grants permission to put or delete multiple key value pairs in a single, all-or-nothing operation
  - **Resource types (\*required):** [key-value-store\*](#list_cloudfront-keyvaluestore-resource-key-value-store)
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by Amazon CloudFront KeyValueStore
<a name="list_cloudfront-keyvaluestore-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [key-value-store](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/kvs-with-functions.html)  | arn:${Partition}:cloudfront::${Account}:key-value-store/${ResourceId} |   | 

## Condition keys for Amazon CloudFront KeyValueStore
<a name="list_cloudfront-keyvaluestore-policy-keys"></a>

Amazon CloudFront KeyValueStore has no service-specific condition keys that can be used in the `Condition` element of policy statements.