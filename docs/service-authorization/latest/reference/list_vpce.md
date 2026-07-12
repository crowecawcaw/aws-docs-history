# Actions, resources, and condition keys for AWS PrivateLink

AWS PrivateLink (service prefix: `vpce`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../AWSEC2/latest/UserGuide.md "../../../AWSEC2/latest/UserGuide.md").
- View a list of the [API operations available for
  this service](../../../AWSEC2/latest/APIReference.md "../../../AWSEC2/latest/APIReference.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../vpc/latest/privatelink/vpc-endpoints-iam.md "../../../vpc/latest/privatelink/vpc-endpoints-iam.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/vpce/vpce.json "https://servicereference.us-east-1.amazonaws.com/v1/vpce/vpce.json") for this service.

###### Topics

- [Actions defined by AWS PrivateLink](#list_vpce-actions-as-permissions "#list_vpce-actions-as-permissions")
- [Permission-only actions for AWS PrivateLink](#list_vpce-permission-only-actions "#list_vpce-permission-only-actions")
- [Resource types defined by AWS PrivateLink](#list_vpce-resources-for-iam-policies "#list_vpce-resources-for-iam-policies")
- [Condition keys for AWS PrivateLink](#list_vpce-policy-keys "#list_vpce-policy-keys")

## Actions defined by AWS PrivateLink

AWS PrivateLink has no API operations that can be used in the
`Actions` element of an IAM policy statement.

## Permission-only actions for AWS PrivateLink

The following actions are defined by AWS PrivateLink but are not directly
invocable through any API operation. They can only be used in IAM policy statements
to grant or deny permissions.

| Actions                                                                                                                                                 | Description                                                                                    | Resource types (\*required)                                                         | Condition keys | Access level |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | -------------- | ------------ |
| [AllowMultiRegion](../../../vpc/latest/privatelink/security_iam_service-with-iam.md "../../../vpc/latest/privatelink/security_iam_service-with-iam.md") | Grants permission to manage multi-region VPC endpoints and VPC endpoint service configurations | [vpc-endpoint](#list_vpce-resource-vpc-endpoint "#list_vpce-resource-vpc-endpoint") |                | Write        |
| [vpc-endpoint-service](#list_vpce-resource-vpc-endpoint-service "#list_vpce-resource-vpc-endpoint-service")                                             |                                                                                                |

## Resource types defined by AWS PrivateLink

The following resource types are defined by this service and can be used in the
`Resource` element of IAM permission policy statements.

| Resource types                                                                                                                                    | ARN                                                                                    | Condition keys |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------- |
| [vpc-endpoint](../../../vpc/latest/userguide/endpoint-services-overview.md "../../../vpc/latest/userguide/endpoint-services-overview.md")         | arn:${Partition}:ec2:${Region}:${Account}:vpc-endpoint/${VpcEndpointId}                |                |
| [vpc-endpoint-service](../../../vpc/latest/userguide/endpoint-services-overview.md "../../../vpc/latest/userguide/endpoint-services-overview.md") | arn:${Partition}:ec2:${Region}:${Account}:vpc-endpoint-service/${VpcEndpointServiceId} |                |

## Condition keys for AWS PrivateLink

AWS PrivateLink has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
