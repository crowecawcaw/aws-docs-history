

# Actions, resources, and condition keys for AWS PrivateLink
<a name="list_vpce"></a>

AWS PrivateLink (service prefix: `vpce`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/vpce/vpce.json) for this service.

**Topics**
+ [Actions defined by AWS PrivateLink](#list_vpce-actions-as-permissions)
+ [Permission-only actions for AWS PrivateLink](#list_vpce-permission-only-actions)
+ [Resource types defined by AWS PrivateLink](#list_vpce-resources-for-iam-policies)
+ [Condition keys for AWS PrivateLink](#list_vpce-policy-keys)

## Actions defined by AWS PrivateLink
<a name="list_vpce-actions-as-permissions"></a>

AWS PrivateLink has no API operations that can be used in the `Actions` element of an IAM policy statement.

## Permission-only actions for AWS PrivateLink
<a name="list_vpce-permission-only-actions"></a>

The following actions are defined by AWS PrivateLink but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [AllowMultiRegion](https://docs.aws.amazon.com/vpc/latest/privatelink/security_iam_service-with-iam.html)  **
  - **Description:** Grants permission to manage multi-region VPC endpoints and VPC endpoint service configurations
  - **Resource types (\*required):** [vpc-endpoint](#list_vpce-resource-vpc-endpoint) / **Condition keys:**  
  - **Resource types (\*required):** [vpc-endpoint-service](#list_vpce-resource-vpc-endpoint-service) / **Condition keys:**  
  - **Access level:** Write



## Resource types defined by AWS PrivateLink
<a name="list_vpce-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [vpc-endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/endpoint-services-overview.html)  | arn:${Partition}:ec2:${Region}:${Account}:vpc-endpoint/${VpcEndpointId} |   | 
|  [vpc-endpoint-service](https://docs.aws.amazon.com/vpc/latest/userguide/endpoint-services-overview.html)  | arn:${Partition}:ec2:${Region}:${Account}:vpc-endpoint-service/${VpcEndpointServiceId} |   | 

## Condition keys for AWS PrivateLink
<a name="list_vpce-policy-keys"></a>

AWS PrivateLink has no service-specific condition keys that can be used in the `Condition` element of policy statements.