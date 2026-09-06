

# Actions, resources, and condition keys for AWS Health APIs and Notifications
<a name="list_health"></a>

AWS Health APIs and Notifications (service prefix: `health`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/health/latest/ug/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/health/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/health/latest/ug/controlling-access.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/health/health.json) for this service.

**Topics**
+ [API operations defined by AWS Health APIs and Notifications](#list_health-operations)
+ [Actions defined by AWS Health APIs and Notifications](#list_health-actions-as-permissions)
+ [Resource types defined by AWS Health APIs and Notifications](#list_health-resources-for-iam-policies)
+ [Condition keys for AWS Health APIs and Notifications](#list_health-policy-keys)

## API operations defined by AWS Health APIs and Notifications
<a name="list_health-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_health-actions-as-permissions).




- **   DescribeAffectedAccountsForOrganization  **
  - **IAM action:**  [health:DescribeAffectedAccountsForOrganization](#list_health-action-DescribeAffectedAccountsForOrganization)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [organizations:ListAccounts](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListAccounts.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   DescribeAffectedEntities  **
  - **IAM action:**  [health:DescribeAffectedEntities](#list_health-action-DescribeAffectedEntities) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAffectedEntitiesForOrganization  **
  - **IAM action:**  [health:DescribeAffectedEntitiesForOrganization](#list_health-action-DescribeAffectedEntitiesForOrganization)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [organizations:ListAccounts](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListAccounts.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   DescribeEntityAggregates  **
  - **IAM action:**  [health:DescribeEntityAggregates](#list_health-action-DescribeEntityAggregates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEntityAggregatesForOrganization  **
  - **IAM action:**  [health:DescribeEntityAggregatesForOrganization](#list_health-action-DescribeEntityAggregatesForOrganization)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [organizations:ListAccounts](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListAccounts.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   DescribeEventAggregates  **
  - **IAM action:**  [health:DescribeEventAggregates](#list_health-action-DescribeEventAggregates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEventDetails  **
  - **IAM action:**  [health:DescribeEventDetails](#list_health-action-DescribeEventDetails) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEventDetailsForOrganization  **
  - **IAM action:**  [health:DescribeEventDetailsForOrganization](#list_health-action-DescribeEventDetailsForOrganization)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [organizations:ListAccounts](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListAccounts.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   DescribeEventTypes  **
  - **IAM action:**  [health:DescribeEventTypes](#list_health-action-DescribeEventTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEvents  **
  - **IAM action:**  [health:DescribeEvents](#list_health-action-DescribeEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEventsForOrganization  **
  - **IAM action:**  [health:DescribeEventsForOrganization](#list_health-action-DescribeEventsForOrganization)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [organizations:ListAccounts](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListAccounts.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   DescribeHealthServiceStatusForOrganization  **
  - **IAM action:**  [health:DescribeHealthServiceStatusForOrganization](#list_health-action-DescribeHealthServiceStatusForOrganization)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [organizations:ListAccounts](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListAccounts.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   DisableHealthServiceAccessForOrganization  **
  - **IAM action:**  [health:DisableHealthServiceAccessForOrganization](#list_health-action-DisableHealthServiceAccessForOrganization)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [organizations:DisableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DisableAWSServiceAccess.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [organizations:ListAccounts](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListAccounts.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   EnableHealthServiceAccessForOrganization  **
  - **IAM action:**  [health:EnableHealthServiceAccessForOrganization](#list_health-action-EnableHealthServiceAccessForOrganization)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [iam:CreateServiceLinkedRole](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateServiceLinkedRole.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [organizations:EnableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnableAWSServiceAccess.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [organizations:ListAccounts](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListAccounts.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List



## Actions defined by AWS Health APIs and Notifications
<a name="list_health-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [DescribeAffectedAccountsForOrganization](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeAffectedAccountsForOrganization.html)  **
  - **Description:** Grants permission to retrieve a list of accounts that have been affected by the specified events in organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeAffectedEntities](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeAffectedEntities.html)  **
  - **Description:** Grants permission to retrieve a list of entities that have been affected by the specified events
  - **Resource types (\*required):** [event\*](#list_health-resource-event)
  - **Condition keys:** [health:eventTypeCode](#list_health-health_eventTypeCode)<br />[health:service](#list_health-health_service)
  - **Access level:** Read

- **   [DescribeAffectedEntitiesForOrganization](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeAffectedEntitiesForOrganization.html)  **
  - **Description:** Grants permission to retrieve a list of entities that have been affected by the specified events and accounts in organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeEntityAggregates](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEntityAggregates.html)  **
  - **Description:** Grants permission to retrieve the number of entities that are affected by each of the specified events
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeEntityAggregatesForOrganization](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEntityAggregatesForOrganization.html)  **
  - **Description:** Grants permission to retrieve the number of entities that are affected by each of the specified events in an organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeEventAggregates](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventAggregates.html)  **
  - **Description:** Grants permission to retrieve the number of events of each event type (issue, scheduled change, and account notification)
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeEventDetails](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventDetails.html)  **
  - **Description:** Grants permission to retrieve detailed information about one or more specified events
  - **Resource types (\*required):** [event\*](#list_health-resource-event)
  - **Condition keys:** [health:eventTypeCode](#list_health-health_eventTypeCode)<br />[health:service](#list_health-health_service)
  - **Access level:** Read

- **   [DescribeEventDetailsForOrganization](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventDetailsForOrganization.html)  **
  - **Description:** Grants permission to retrieve detailed information about one or more specified events for provided accounts in organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeEventTypes](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventTypes.html)  **
  - **Description:** Grants permission to retrieve the event types that meet the specified filter criteria
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeEvents](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEvents.html)  **
  - **Description:** Grants permission to retrieve information about events that meet the specified filter criteria
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeEventsForOrganization](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventsForOrganization.html)  **
  - **Description:** Grants permission to retrieve information about events that meet the specified filter criteria in organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeHealthServiceStatusForOrganization](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeHealthServiceStatusForOrganization.html)  **
  - **Description:** Grants permission to retrieve the status of enabling or disabling the Organizational View feature
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DisableHealthServiceAccessForOrganization](https://docs.aws.amazon.com/health/latest/APIReference/API_DisableHealthServiceAccessForOrganization.html)  **
  - **Description:** Grants permission to disable the Organizational View feature
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [EnableHealthServiceAccessForOrganization](https://docs.aws.amazon.com/health/latest/APIReference/API_EnableHealthServiceAccessForOrganization.html)  **
  - **Description:** Grants permission to enable the Organizational View feature
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write



## Resource types defined by AWS Health APIs and Notifications
<a name="list_health-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [event](https://docs.aws.amazon.com/health/latest/ug/supported-operations.html)  | arn:${Partition}:health:\*::event/${Service}/${EventTypeCode}/\* |   | 

## Condition keys for AWS Health APIs and Notifications
<a name="list_health-policy-keys"></a>

AWS Health APIs and Notifications defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [health:eventTypeCode](https://docs.aws.amazon.com/health/latest/ug/controlling-access.html)  | Filters access by event type | String | 
|   [health:service](https://docs.aws.amazon.com/health/latest/ug/controlling-access.html)  | Filters access by impacted service | String | 