# Amazon Route 53 API permissions: Actions, resources,

and conditions reference

When you set up [Access control](auth-and-access-control.md#access-control "auth-and-access-control.md#access-control") and
write a permissions policy that you can attach to an IAM identity (identity-based
policies), you can use the lists of [Actions,
resources, and condition keys for Route 53](../../../service-authorization/latest/reference/list_amazonroute53.md "../../../service-authorization/latest/reference/list_amazonroute53.md"), [Actions,
resources, and condition keys for Route 53 Domains](../../../service-authorization/latest/reference/list_amazonroute53domains.md "../../../service-authorization/latest/reference/list_amazonroute53domains.md"), [Actions, resources, and condition keys for VPC Resolver](../../../service-authorization/latest/reference/list_amazonroute53resolver.md "../../../service-authorization/latest/reference/list_amazonroute53resolver.md"), and [Actions, resources, and condition keys for Amazon Route 53 Profiles enables sharing DNS settings with VPCs](../../../service-authorization/latest/reference/list_amazonroute53profilesenablessharingdnssettingswithvpcs.md "../../../service-authorization/latest/reference/list_amazonroute53profilesenablessharingdnssettingswithvpcs.md") in the _Service
Authorization Reference_. The pages include each Amazon Route 53 API action, the
actions that you must grant permissions access to, and the AWS resource that you must
grant access to. You specify the actions in the policy's `Action` field, and
you specify the resource value in the policy's `Resource` field.

You can use AWS-wide condition keys in your Route 53 policies to express conditions.
For a complete list of AWS-wide keys, see [Available
keys](../../../IAM/latest/UserGuide/reference_policies_elements.md#AvailableKeys "../../../IAM/latest/UserGuide/reference_policies_elements.md#AvailableKeys") in the _IAM User Guide_.

###### Note

When granting access, the hosted zone and the Amazon VPC must belong to the same
partition. A partition is a group of AWS Regions. Each AWS account is scoped to
one partition.

The following are the supported partitions:

- `aws` - AWS Regions
- `aws-cn` - China Regions
- `aws-us-gov` - AWS GovCloud (US) Region
  For more information, see [Access Management](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md")
  in the _AWS General Reference_.

###### Note

To specify an action, use the applicable prefix (`route53`,
`route53domains`, or `route53resolver`) followed by the
API operation name, for example:

- `route53:CreateHostedZone`
- `route53domains:RegisterDomain`
- `route53resolver:CreateResolverEndpoint`
