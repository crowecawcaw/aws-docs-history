

# Actions, resources, and condition keys for Amazon WorkMail Message Flow
<a name="list_workmailmessageflow"></a>

Amazon WorkMail Message Flow (service prefix: `workmailmessageflow`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/workmail/latest/adminguide/lambda-content.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/workmail/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/workmail/latest/adminguide/lambda-content.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/workmailmessageflow/workmailmessageflow.json) for this service.

**Topics**
+ [API operations defined by Amazon WorkMail Message Flow](#list_workmailmessageflow-operations)
+ [Actions defined by Amazon WorkMail Message Flow](#list_workmailmessageflow-actions-as-permissions)
+ [Resource types defined by Amazon WorkMail Message Flow](#list_workmailmessageflow-resources-for-iam-policies)
+ [Condition keys for Amazon WorkMail Message Flow](#list_workmailmessageflow-policy-keys)

## API operations defined by Amazon WorkMail Message Flow
<a name="list_workmailmessageflow-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_workmailmessageflow-actions-as-permissions).




- **   GetRawMessageContent  **
  - **IAM action:**  [workmailmessageflow:GetRawMessageContent](#list_workmailmessageflow-action-GetRawMessageContent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutRawMessageContent  **
  - **IAM action:**  [workmailmessageflow:PutRawMessageContent](#list_workmailmessageflow-action-PutRawMessageContent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon WorkMail Message Flow
<a name="list_workmailmessageflow-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [GetRawMessageContent](https://docs.aws.amazon.com/workmail/latest/APIReference/API_messageflow_GetRawMessageContent.html)  **
  - **Description:** Grants permission to read the content of email messages with the specified message ID
  - **Resource types (\*required):** [RawMessage\*](#list_workmailmessageflow-resource-RawMessage)
  - **Condition keys:**  
  - **Access level:** Read

- **   [PutRawMessageContent](https://docs.aws.amazon.com/workmail/latest/APIReference/API_messageflow_PutRawMessageContent.html)  **
  - **Description:** Grants permission to update the content of email messages with the specified message ID
  - **Resource types (\*required):** [RawMessage\*](#list_workmailmessageflow-resource-RawMessage)
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by Amazon WorkMail Message Flow
<a name="list_workmailmessageflow-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [RawMessage](https://docs.aws.amazon.com/workmail/latest/adminguide/lambda-content.html)  | arn:${Partition}:workmailmessageflow:${Region}:${Account}:message/${OrganizationId}/${Context}/${MessageId} |   | 

## Condition keys for Amazon WorkMail Message Flow
<a name="list_workmailmessageflow-policy-keys"></a>

Amazon WorkMail Message Flow has no service-specific condition keys that can be used in the `Condition` element of policy statements.