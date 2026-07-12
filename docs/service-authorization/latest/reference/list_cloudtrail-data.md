# Actions, resources, and condition keys for AWS CloudTrail Data

AWS CloudTrail Data (service prefix: `cloudtrail-data`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md").
- View a list of the [API operations available for
  this service](../../../awscloudtraildata/latest/APIReference.md "../../../awscloudtraildata/latest/APIReference.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../awscloudtrail/latest/userguide/security_iam_service-with-iam.md "../../../awscloudtrail/latest/userguide/security_iam_service-with-iam.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/cloudtrail-data/cloudtrail-data.json "https://servicereference.us-east-1.amazonaws.com/v1/cloudtrail-data/cloudtrail-data.json") for this service.

###### Topics

- [API operations defined by AWS CloudTrail Data](#list_cloudtrail-data-operations "#list_cloudtrail-data-operations")
- [Actions defined by AWS CloudTrail Data](#list_cloudtrail-data-actions-as-permissions "#list_cloudtrail-data-actions-as-permissions")
- [Resource types defined by AWS CloudTrail Data](#list_cloudtrail-data-resources-for-iam-policies "#list_cloudtrail-data-resources-for-iam-policies")
- [Condition keys for AWS CloudTrail Data](#list_cloudtrail-data-policy-keys "#list_cloudtrail-data-policy-keys")

## API operations defined by AWS CloudTrail Data

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_cloudtrail-data-actions-as-permissions "#list_cloudtrail-data-actions-as-permissions").

| Operation      | IAM action                                                                                                                  | Condition key | Possible value(s) | Access level |
| -------------- | --------------------------------------------------------------------------------------------------------------------------- | ------------- | ----------------- | ------------ |
| PutAuditEvents | [cloudtrail-data:PutAuditEvents](#list_cloudtrail-data-action-PutAuditEvents "#list_cloudtrail-data-action-PutAuditEvents") |               |                   | Write        |

## Actions defined by AWS CloudTrail Data

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                       | Description                                                              | Resource types (\*required)                                                                  | Condition keys                                                                                                                 | Access level |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ------------ |
| [PutAuditEvents](../../../awscloudtraildata/latest/APIReference/API_PutAuditEvents.md "../../../awscloudtraildata/latest/APIReference/API_PutAuditEvents.md") | Grants permission to ingest your application events into CloudTrail Lake | [channel\*](#list_cloudtrail-data-resource-channel "#list_cloudtrail-data-resource-channel") | [aws:ResourceTag/${TagKey}](#list_cloudtrail-data-aws_ResourceTag___TagKey_ "#list_cloudtrail-data-aws_ResourceTag___TagKey_") | Write        |

## Resource types defined by AWS CloudTrail Data

The following resource types are defined by this service and can be used in the
`Resource` element of IAM permission policy statements.

| Resource types                                                                                                                                                                                           | ARN                                                                   | Condition keys                                                                                                                 |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| [channel](../../../awscloudtrail/latest/userguide/how-cloudtrail-works.md#how-cloudtrail-works-channels "../../../awscloudtrail/latest/userguide/how-cloudtrail-works.md#how-cloudtrail-works-channels") | arn:${Partition}:cloudtrail:${Region}:${Account}:channel/${ChannelId} | [aws:ResourceTag/${TagKey}](#list_cloudtrail-data-aws_ResourceTag___TagKey_ "#list_cloudtrail-data-aws_ResourceTag___TagKey_") |

## Condition keys for AWS CloudTrail Data

AWS CloudTrail Data defines the following condition keys that can be used in the
`Condition` element of an IAM policy.

| Condition keys                                                                                                                                                                                                             | Description                                                                 | Type          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | ------------- |
| [aws:RequestTag/${TagKey}](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-requesttag "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-requesttag")    | Filters access by a tag's key and value in a request                        | String        |
| [aws:ResourceTag/${TagKey}](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-resourcetag "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-resourcetag") | Filters actions based on the presence of tag key-value pairs in the request | String        |
| [aws:TagKeys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-tagkeys "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-tagkeys")                       | Filters access by the tag keys in a request                                 | ArrayOfString |
