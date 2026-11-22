

# Actions, resources, and condition keys for AWS Agent Registry Public Search and Discovery

AWS Agent Registry Public Search and Discovery (service prefix: `agent-discovery`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/agent-discovery/latest/APIReference/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/agent-discovery/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/agent-discovery/latest/APIReference/) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/agent-discovery/agent-discovery.json) for this service.

**Topics**
+ [API operations defined by AWS Agent Registry Public Search and Discovery](#list_agent-discovery-operations)
+ [Actions defined by AWS Agent Registry Public Search and Discovery](#list_agent-discovery-actions-as-permissions)
+ [Resource types defined by AWS Agent Registry Public Search and Discovery](#list_agent-discovery-resources-for-iam-policies)
+ [Condition keys for AWS Agent Registry Public Search and Discovery](#list_agent-discovery-policy-keys)

## API operations defined by AWS Agent Registry Public Search and Discovery
<a name="list_agent-discovery-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_agent-discovery-actions-as-permissions).




- **   SearchPublicRecords  **
  - **IAM action:**  [agent-discovery:SearchPublicRecords](#list_agent-discovery-action-SearchPublicRecords) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read



## Actions defined by AWS Agent Registry Public Search and Discovery
<a name="list_agent-discovery-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. For each action, the table lists the resource types and condition keys supported by that action. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [SearchPublicRecords](https://docs.aws.amazon.com/agent-discovery/latest/APIReference/API_SearchPublicRecords.html)  | Grants permission to search public agent registry records |  |   | Read | 

## Resource types defined by AWS Agent Registry Public Search and Discovery
<a name="list_agent-discovery-resources-for-iam-policies"></a>

AWS Agent Registry Public Search and Discovery does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for AWS Agent Registry Public Search and Discovery
<a name="list_agent-discovery-policy-keys"></a>

AWS Agent Registry Public Search and Discovery has no service-specific condition keys that can be used in the `Condition` element of policy statements.