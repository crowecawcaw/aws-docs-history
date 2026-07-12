# Actions, resources, and condition keys for AWS Control Catalog

AWS Control Catalog (service prefix: `controlcatalog`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../controlcatalog/latest/userguide.md "../../../controlcatalog/latest/userguide.md").
- View a list of the [API operations available for
  this service](../../../controlcatalog/latest/APIReference.md "../../../controlcatalog/latest/APIReference.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../controlcatalog/latest/userguide/security-iam.md "../../../controlcatalog/latest/userguide/security-iam.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/controlcatalog/controlcatalog.json "https://servicereference.us-east-1.amazonaws.com/v1/controlcatalog/controlcatalog.json") for this service.

###### Topics

- [API operations defined by AWS Control Catalog](#list_controlcatalog-operations "#list_controlcatalog-operations")
- [Actions defined by AWS Control Catalog](#list_controlcatalog-actions-as-permissions "#list_controlcatalog-actions-as-permissions")
- [Resource types defined by AWS Control Catalog](#list_controlcatalog-resources-for-iam-policies "#list_controlcatalog-resources-for-iam-policies")
- [Condition keys for AWS Control Catalog](#list_controlcatalog-policy-keys "#list_controlcatalog-policy-keys")

## API operations defined by AWS Control Catalog

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_controlcatalog-actions-as-permissions "#list_controlcatalog-actions-as-permissions").

| Operation                                                                                                                                 | IAM action                                                                                                                              | Condition key | Possible value(s) | Access level |
| ----------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ----------------- | ------------ |
| GetControl                                                                                                                                | [controlcatalog:GetControl](#list_controlcatalog-action-GetControl "#list_controlcatalog-action-GetControl")                            |               |                   | Read         |
| [controltower:DescribeGuardrail](../../../controltower/latest/userguide/controls.md "../../../controltower/latest/userguide/controls.md") |                                                                                                                                         |               | Read              |
| ListCommonControls                                                                                                                        | [controlcatalog:ListCommonControls](#list_controlcatalog-action-ListCommonControls "#list_controlcatalog-action-ListCommonControls")    |               |                   | List         |
| ListControlMappings                                                                                                                       | [controlcatalog:ListControlMappings](#list_controlcatalog-action-ListControlMappings "#list_controlcatalog-action-ListControlMappings") |               |                   | List         |
| ListControls                                                                                                                              | [controlcatalog:ListControls](#list_controlcatalog-action-ListControls "#list_controlcatalog-action-ListControls")                      |               |                   | List         |
| [controltower:ListGuardrails](../../../controltower/latest/userguide/controls.md "../../../controltower/latest/userguide/controls.md")    |                                                                                                                                         |               | List              |
| ListDomains                                                                                                                               | [controlcatalog:ListDomains](#list_controlcatalog-action-ListDomains "#list_controlcatalog-action-ListDomains")                         |               |                   | List         |
| ListObjectives                                                                                                                            | [controlcatalog:ListObjectives](#list_controlcatalog-action-ListObjectives "#list_controlcatalog-action-ListObjectives")                |               |                   | List         |

## Actions defined by AWS Control Catalog

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                                | Description                                                                                               | Resource types (\*required)                                                                | Condition keys | Access level |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | -------------- | ------------ |
| [GetControl](../../../controlcatalog/latest/APIReference/API_GetControl.md "../../../controlcatalog/latest/APIReference/API_GetControl.md")                            | Grants permission to return details about a specific control                                              | [control\*](#list_controlcatalog-resource-control "#list_controlcatalog-resource-control") |                | Read         |
| [ListCommonControls](../../../controlcatalog/latest/APIReference/API_ListCommonControls.md "../../../controlcatalog/latest/APIReference/API_ListCommonControls.md")    | Grants permission to return a paginated list of common controls from the AWS Control Catalog              |                                                                                            |                | List         |
| [ListControlMappings](../../../controlcatalog/latest/APIReference/API_ListControlMappings.md "../../../controlcatalog/latest/APIReference/API_ListControlMappings.md") | Grants permission to return a paginated list of control mappings from the AWS Control Catalog             |                                                                                            |                | List         |
| [ListControls](../../../controlcatalog/latest/APIReference/API_ListControls.md "../../../controlcatalog/latest/APIReference/API_ListControls.md")                      | Grants permission to return a paginated list of all available controls in the AWS Control Catalog library | [control\*](#list_controlcatalog-resource-control "#list_controlcatalog-resource-control") |                | List         |
| [ListDomains](../../../controlcatalog/latest/APIReference/API_ListDomains.md "../../../controlcatalog/latest/APIReference/API_ListDomains.md")                         | Grants permission to return a paginated list of domains from the AWS Control Catalog                      |                                                                                            |                | List         |
| [ListObjectives](../../../controlcatalog/latest/APIReference/API_ListObjectives.md "../../../controlcatalog/latest/APIReference/API_ListObjectives.md")                | Grants permission to return a paginated list of objectives from the AWS Control Catalog                   |                                                                                            |                | List         |

## Resource types defined by AWS Control Catalog

The following resource types are defined by this service and can be used in the
`Resource` element of IAM permission policy statements.

| Resource types                                                                                                                                                      | ARN                                                                 | Condition keys |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | -------------- |
| [common-control](../../../controlcatalog/latest/APIReference/API_CommonControlSummary.md "../../../controlcatalog/latest/APIReference/API_CommonControlSummary.md") | arn:${Partition}:controlcatalog:::common-control/${CommonControlId} |                |
| [control](../../../controlcatalog/latest/APIReference/API_ControlSummary.md "../../../controlcatalog/latest/APIReference/API_ControlSummary.md")                    | arn:${Partition}:controlcatalog:::control/${ControlId}              |                |
| [domain](../../../controlcatalog/latest/APIReference/API_DomainSummary.md "../../../controlcatalog/latest/APIReference/API_DomainSummary.md")                       | arn:${Partition}:controlcatalog:::domain/${DomainId}                |                |
| [objective](../../../controlcatalog/latest/APIReference/API_ObjectiveSummary.md "../../../controlcatalog/latest/APIReference/API_ObjectiveSummary.md")              | arn:${Partition}:controlcatalog:::objective/${ObjectiveId}          |                |

## Condition keys for AWS Control Catalog

AWS Control Catalog has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
