# Actions, resources, and condition keys for Amazon WorkMail Message Flow

Amazon WorkMail Message Flow (service prefix: `workmailmessageflow`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../workmail/latest/adminguide/lambda-content.md "../../../workmail/latest/adminguide/lambda-content.md").
- View a list of the [API operations available for
  this service](../../../workmail/latest/APIReference.md "../../../workmail/latest/APIReference.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../workmail/latest/adminguide/lambda-content.md "../../../workmail/latest/adminguide/lambda-content.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/workmailmessageflow/workmailmessageflow.json "https://servicereference.us-east-1.amazonaws.com/v1/workmailmessageflow/workmailmessageflow.json") for this service.

###### Topics

- [API operations defined by Amazon WorkMail Message Flow](#list_workmailmessageflow-operations "#list_workmailmessageflow-operations")
- [Actions defined by Amazon WorkMail Message Flow](#list_workmailmessageflow-actions-as-permissions "#list_workmailmessageflow-actions-as-permissions")
- [Resource types defined by Amazon WorkMail Message Flow](#list_workmailmessageflow-resources-for-iam-policies "#list_workmailmessageflow-resources-for-iam-policies")
- [Condition keys for Amazon WorkMail Message Flow](#list_workmailmessageflow-policy-keys "#list_workmailmessageflow-policy-keys")

## API operations defined by Amazon WorkMail Message Flow

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_workmailmessageflow-actions-as-permissions "#list_workmailmessageflow-actions-as-permissions").

| Operation            | IAM action                                                                                                                                                | Condition key | Possible value(s) | Access level |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ----------------- | ------------ |
| GetRawMessageContent | [workmailmessageflow:GetRawMessageContent](#list_workmailmessageflow-action-GetRawMessageContent "#list_workmailmessageflow-action-GetRawMessageContent") |               |                   | Read         |
| PutRawMessageContent | [workmailmessageflow:PutRawMessageContent](#list_workmailmessageflow-action-PutRawMessageContent "#list_workmailmessageflow-action-PutRawMessageContent") |               |                   | Write        |

## Actions defined by Amazon WorkMail Message Flow

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                                               | Description                                                                             | Resource types (\*required)                                                                                   | Condition keys | Access level |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | -------------- | ------------ |
| [GetRawMessageContent](../../../workmail/latest/APIReference/API_messageflow_GetRawMessageContent.md "../../../workmail/latest/APIReference/API_messageflow_GetRawMessageContent.md") | Grants permission to read the content of email messages with the specified message ID   | [RawMessage\*](#list_workmailmessageflow-resource-RawMessage "#list_workmailmessageflow-resource-RawMessage") |                | Read         |
| [PutRawMessageContent](../../../workmail/latest/APIReference/API_messageflow_PutRawMessageContent.md "../../../workmail/latest/APIReference/API_messageflow_PutRawMessageContent.md") | Grants permission to update the content of email messages with the specified message ID | [RawMessage\*](#list_workmailmessageflow-resource-RawMessage "#list_workmailmessageflow-resource-RawMessage") |                | Write        |

## Resource types defined by Amazon WorkMail Message Flow

The following resource types are defined by this service and can be used in the
`Resource` element of IAM permission policy statements.

| Resource types                                                                                                              | ARN                                                                                                         | Condition keys |
| --------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | -------------- |
| [RawMessage](../../../workmail/latest/adminguide/lambda-content.md "../../../workmail/latest/adminguide/lambda-content.md") | arn:${Partition}:workmailmessageflow:${Region}:${Account}:message/${OrganizationId}/${Context}/${MessageId} |                |

## Condition keys for Amazon WorkMail Message Flow

Amazon WorkMail Message Flow has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
