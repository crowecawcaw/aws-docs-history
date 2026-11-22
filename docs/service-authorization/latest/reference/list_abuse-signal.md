

# Actions, resources, and condition keys for AWS Abuse Signal API

AWS Abuse Signal API (service prefix: `abuse`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/abuse-signal/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/abuse-signal/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/abuse-signal/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/abuse/abuse.json) for this service.

**Topics**
+ [API operations defined by AWS Abuse Signal API](#list_abuse-signal-operations)
+ [Actions defined by AWS Abuse Signal API](#list_abuse-signal-actions-as-permissions)
+ [Resource types defined by AWS Abuse Signal API](#list_abuse-signal-resources-for-iam-policies)
+ [Condition keys for AWS Abuse Signal API](#list_abuse-signal-policy-keys)

## API operations defined by AWS Abuse Signal API
<a name="list_abuse-signal-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_abuse-signal-actions-as-permissions).




- **   CreateAbuseReport  **
  - **IAM action:**  [abuse:CreateAbuseReport](#list_abuse-signal-action-CreateAbuseReport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAbuseReportStatus  **
  - **IAM action:**  [abuse:GetAbuseReportStatus](#list_abuse-signal-action-GetAbuseReportStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAbuseReportStatuses  **
  - **IAM action:**  [abuse:ListAbuseReportStatuses](#list_abuse-signal-action-ListAbuseReportStatuses) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read



## Actions defined by AWS Abuse Signal API
<a name="list_abuse-signal-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. For each action, the table lists the resource types and condition keys supported by that action. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [CreateAbuseReport](https://docs.aws.amazon.com/abuse-signal/latest/APIReference/API_CreateAbuseReport.html)  | Grants permission to submit a new abuse report |  |   | Write | 
|   [GetAbuseReportStatus](https://docs.aws.amazon.com/abuse-signal/latest/APIReference/API_GetAbuseReportStatus.html)  | Grants permission to retrieve the status of an abuse report |  |   | Read | 
|   [ListAbuseReportStatuses](https://docs.aws.amazon.com/abuse-signal/latest/APIReference/API_ListAbuseReportStatuses.html)  | Grants permission to list abuse report statuses |  |   | Read | 

## Resource types defined by AWS Abuse Signal API
<a name="list_abuse-signal-resources-for-iam-policies"></a>

AWS Abuse Signal API does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for AWS Abuse Signal API
<a name="list_abuse-signal-policy-keys"></a>

AWS Abuse Signal API has no service-specific condition keys that can be used in the `Condition` element of policy statements.