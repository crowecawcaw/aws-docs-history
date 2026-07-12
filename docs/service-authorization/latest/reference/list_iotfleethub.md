# Actions, resources, and condition keys for AWS IoT Fleet Hub for Device Management

AWS IoT Fleet Hub for Device Management (service prefix: `iotfleethub`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../iot/latest/fleethubuserguide.md "../../../iot/latest/fleethubuserguide.md").
- View a list of the [API operations available for
  this service](../../../iot/latest/apireference/API_Operations_AWS_IoT_Fleet_Hub.md "../../../iot/latest/apireference/API_Operations_AWS_IoT_Fleet_Hub.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../iot/latest/fleethubuserguide/aws-iot-monitor-security.md "../../../iot/latest/fleethubuserguide/aws-iot-monitor-security.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/iotfleethub/iotfleethub.json "https://servicereference.us-east-1.amazonaws.com/v1/iotfleethub/iotfleethub.json") for this service.

###### Topics

- [Actions defined by AWS IoT Fleet Hub for Device Management](#list_iotfleethub-actions-as-permissions "#list_iotfleethub-actions-as-permissions")
- [Resource types defined by AWS IoT Fleet Hub for Device Management](#list_iotfleethub-resources-for-iam-policies "#list_iotfleethub-resources-for-iam-policies")
- [Condition keys for AWS IoT Fleet Hub for Device Management](#list_iotfleethub-policy-keys "#list_iotfleethub-policy-keys")

## Actions defined by AWS IoT Fleet Hub for Device Management

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                                  | Description                                       | Resource types (\*required)                                                                      | Condition keys                                                                                                                                                                                                                                                                                                                | Access level   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| [CreateApplication](../../../iot/latest/apireference/API_iotfleethub_CreateApplication.md "../../../iot/latest/apireference/API_iotfleethub_CreateApplication.md")       | Grants permission to create an application        |                                                                                                  | [aws:RequestTag/${TagKey}](#list_iotfleethub-aws_RequestTag___TagKey_ "#list_iotfleethub-aws_RequestTag___TagKey_")<br>[aws:TagKeys](#list_iotfleethub-aws_TagKeys "#list_iotfleethub-aws_TagKeys")                                                                                                                           | Write          |
| [DeleteApplication](../../../iot/latest/apireference/API_iotfleethub_DeleteApplication.md "../../../iot/latest/apireference/API_iotfleethub_DeleteApplication.md")       | Grants permission to delete an application        | [application\*](#list_iotfleethub-resource-application "#list_iotfleethub-resource-application") | [aws:ResourceTag/${TagKey}](#list_iotfleethub-aws_ResourceTag___TagKey_ "#list_iotfleethub-aws_ResourceTag___TagKey_")                                                                                                                                                                                                        | Write          |
| [DescribeApplication](../../../iot/latest/apireference/API_iotfleethub_DescribeApplication.md "../../../iot/latest/apireference/API_iotfleethub_DescribeApplication.md") | Grants permission to describe an application      | [application\*](#list_iotfleethub-resource-application "#list_iotfleethub-resource-application") | [aws:ResourceTag/${TagKey}](#list_iotfleethub-aws_ResourceTag___TagKey_ "#list_iotfleethub-aws_ResourceTag___TagKey_")                                                                                                                                                                                                        | Read           |
| [ListApplications](../../../iot/latest/apireference/API_iotfleethub_ListApplications.md "../../../iot/latest/apireference/API_iotfleethub_ListApplications.md")          | Grants permission to list all applications        |                                                                                                  |                                                                                                                                                                                                                                                                                                                               | List           |
| [ListTagsForResource](../../../iot/latest/apireference/API_iotfleethub_ListTagsForResource.md "../../../iot/latest/apireference/API_iotfleethub_ListTagsForResource.md") | Grants permission to list all tags for a resource | [application](#list_iotfleethub-resource-application "#list_iotfleethub-resource-application")   | [aws:ResourceTag/${TagKey}](#list_iotfleethub-aws_ResourceTag___TagKey_ "#list_iotfleethub-aws_ResourceTag___TagKey_")                                                                                                                                                                                                        | Read           |
| [TagResource](../../../iot/latest/apireference/API_iotfleethub_TagResource.md "../../../iot/latest/apireference/API_iotfleethub_TagResource.md")                         | Grants permission to tag a resource               | [application](#list_iotfleethub-resource-application "#list_iotfleethub-resource-application")   | [aws:RequestTag/${TagKey}](#list_iotfleethub-aws_RequestTag___TagKey_ "#list_iotfleethub-aws_RequestTag___TagKey_")<br>[aws:ResourceTag/${TagKey}](#list_iotfleethub-aws_ResourceTag___TagKey_ "#list_iotfleethub-aws_ResourceTag___TagKey_")<br>[aws:TagKeys](#list_iotfleethub-aws_TagKeys "#list_iotfleethub-aws_TagKeys") | Tagging, Write |
| [UntagResource](../../../iot/latest/apireference/API_iotfleethub_UntagResource.md "../../../iot/latest/apireference/API_iotfleethub_UntagResource.md")                   | Grants permission to untag a resource             | [application](#list_iotfleethub-resource-application "#list_iotfleethub-resource-application")   | [aws:ResourceTag/${TagKey}](#list_iotfleethub-aws_ResourceTag___TagKey_ "#list_iotfleethub-aws_ResourceTag___TagKey_")<br>[aws:TagKeys](#list_iotfleethub-aws_TagKeys "#list_iotfleethub-aws_TagKeys")                                                                                                                        | Tagging, Write |
| [UpdateApplication](../../../iot/latest/apireference/API_iotfleethub_UpdateApplication.md "../../../iot/latest/apireference/API_iotfleethub_UpdateApplication.md")       | Grants permission to update an application        | [application\*](#list_iotfleethub-resource-application "#list_iotfleethub-resource-application") | [aws:ResourceTag/${TagKey}](#list_iotfleethub-aws_ResourceTag___TagKey_ "#list_iotfleethub-aws_ResourceTag___TagKey_")                                                                                                                                                                                                        | Write          |

## Resource types defined by AWS IoT Fleet Hub for Device Management

The following resource types are defined by this service and can be used in the
`Resource` element of IAM permission policy statements.

| Resource types                                                                                                                                                 | ARN                                                                            | Condition keys                                                                                                         |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| [application](../../../iot/latest/apireference/API_iotfleethub_ApplicationSummary.md "../../../iot/latest/apireference/API_iotfleethub_ApplicationSummary.md") | arn:${Partition}:iotfleethub:${Region}:${Account}:application/${ApplicationId} | [aws:ResourceTag/${TagKey}](#list_iotfleethub-aws_ResourceTag___TagKey_ "#list_iotfleethub-aws_ResourceTag___TagKey_") |

## Condition keys for AWS IoT Fleet Hub for Device Management

AWS IoT Fleet Hub for Device Management defines the following condition keys that can be used in the
`Condition` element of an IAM policy.

| Condition keys                                                                                                                                                                                                             | Description                                              | Type          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- | ------------- |
| [aws:RequestTag/${TagKey}](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-requesttag "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-requesttag")    | Filters access by the tag key-value pairs in the request | String        |
| [aws:ResourceTag/${TagKey}](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-resourcetag "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-resourcetag") | Filters access by the tags attached to the resource      | String        |
| [aws:TagKeys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-tagkeys "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-tagkeys")                       | Filters actions by the tag keys in the request           | ArrayOfString |
