# Actions, resources, and condition keys for AWS Connector Service

AWS Connector Service (service prefix: `awsconnector`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../server-migration-service/latest/userguide/SMS_setup.md "../../../server-migration-service/latest/userguide/SMS_setup.md").
- View a list of the [API operations available for
  this service](../../../server-migration-service/latest/APIReference/API_Operations.md "../../../server-migration-service/latest/APIReference/API_Operations.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../server-migration-service/latest/userguide/SMS_setup.md "../../../server-migration-service/latest/userguide/SMS_setup.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/awsconnector/awsconnector.json "https://servicereference.us-east-1.amazonaws.com/v1/awsconnector/awsconnector.json") for this service.

###### Topics

- [Actions defined by AWS Connector Service](#list_awsconnector-actions-as-permissions "#list_awsconnector-actions-as-permissions")
- [Permission-only actions for AWS Connector Service](#list_awsconnector-permission-only-actions "#list_awsconnector-permission-only-actions")
- [Resource types defined by AWS Connector Service](#list_awsconnector-resources-for-iam-policies "#list_awsconnector-resources-for-iam-policies")
- [Condition keys for AWS Connector Service](#list_awsconnector-policy-keys "#list_awsconnector-policy-keys")

## Actions defined by AWS Connector Service

AWS Connector Service has no API operations that can be used in the
`Actions` element of an IAM policy statement.

## Permission-only actions for AWS Connector Service

The following actions are defined by AWS Connector Service but are not directly
invocable through any API operation. They can only be used in IAM policy statements
to grant or deny permissions.

| Actions                                                                                                                                                                                          | Description                                                                             | Resource types (\*required) | Condition keys | Access level |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------- | --------------------------- | -------------- | ------------ |
| [GetConnectorHealth](../../../server-migration-service/latest/userguide/prereqs.md#connector-permissions "../../../server-migration-service/latest/userguide/prereqs.md#connector-permissions")  | Retrieves all health metrics that were published from the Server Migration Connector.   |                             |                | Read         |
| [RegisterConnector](../../../server-migration-service/latest/userguide/prereqs.md#connector-permissions "../../../server-migration-service/latest/userguide/prereqs.md#connector-permissions")   | Registers AWS Connector with AWS Connector Service.                                     |                             |                | Write        |
| [ValidateConnectorId](../../../server-migration-service/latest/userguide/prereqs.md#connector-permissions "../../../server-migration-service/latest/userguide/prereqs.md#connector-permissions") | Validates Server Migration Connector Id that was registered with AWS Connector Service. |                             |                | Read         |

## Resource types defined by AWS Connector Service

AWS Connector Service does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for AWS Connector Service

AWS Connector Service has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
