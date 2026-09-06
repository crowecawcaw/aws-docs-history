

# Actions, resources, and condition keys for Amazon Security Lake
<a name="list_securitylake"></a>

Amazon Security Lake (service prefix: `securitylake`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/security-lake/latest/userguide/what-is-security-lake.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/security-lake/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/security-lake/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/securitylake/securitylake.json) for this service.

**Topics**
+ [API operations defined by Amazon Security Lake](#list_securitylake-operations)
+ [Actions defined by Amazon Security Lake](#list_securitylake-actions-as-permissions)
+ [Resource types defined by Amazon Security Lake](#list_securitylake-resources-for-iam-policies)
+ [Condition keys for Amazon Security Lake](#list_securitylake-policy-keys)

## API operations defined by Amazon Security Lake
<a name="list_securitylake-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_securitylake-actions-as-permissions).




- **   CreateAwsLogSource  **
  - **IAM action:**  [securitylake:CreateAwsLogSource](#list_securitylake-action-CreateAwsLogSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateCustomLogSource  **
  - **IAM action:**  [securitylake:CreateCustomLogSource](#list_securitylake-action-CreateCustomLogSource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** glue.amazonaws.com / **Access level:** Write

- **   CreateDataLake  **
  - **IAM action:**  [securitylake:CreateDataLake](#list_securitylake-action-CreateDataLake)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [securitylake:TagResource](#list_securitylake-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** lambda.amazonaws.com, s3.amazonaws.com / **Access level:** Write

- **   CreateDataLakeExceptionSubscription  **
  - **IAM action:**  [securitylake:CreateDataLakeExceptionSubscription](#list_securitylake-action-CreateDataLakeExceptionSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateDataLakeOrganizationConfiguration  **
  - **IAM action:**  [securitylake:CreateDataLakeOrganizationConfiguration](#list_securitylake-action-CreateDataLakeOrganizationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateSubscriber  **
  - **IAM action:**  [securitylake:CreateSubscriber](#list_securitylake-action-CreateSubscriber)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [securitylake:TagResource](#list_securitylake-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateSubscriberNotification  **
  - **IAM action:**  [securitylake:CreateSubscriberNotification](#list_securitylake-action-CreateSubscriberNotification)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** events.amazonaws.com / **Access level:** Write

- **   DeleteAwsLogSource  **
  - **IAM action:**  [securitylake:DeleteAwsLogSource](#list_securitylake-action-DeleteAwsLogSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCustomLogSource  **
  - **IAM action:**  [securitylake:DeleteCustomLogSource](#list_securitylake-action-DeleteCustomLogSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDataLake  **
  - **IAM action:**  [securitylake:DeleteDataLake](#list_securitylake-action-DeleteDataLake) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDataLakeExceptionSubscription  **
  - **IAM action:**  [securitylake:DeleteDataLakeExceptionSubscription](#list_securitylake-action-DeleteDataLakeExceptionSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDataLakeOrganizationConfiguration  **
  - **IAM action:**  [securitylake:DeleteDataLakeOrganizationConfiguration](#list_securitylake-action-DeleteDataLakeOrganizationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSubscriber  **
  - **IAM action:**  [securitylake:DeleteSubscriber](#list_securitylake-action-DeleteSubscriber) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSubscriberNotification  **
  - **IAM action:**  [securitylake:DeleteSubscriberNotification](#list_securitylake-action-DeleteSubscriberNotification) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeregisterDataLakeDelegatedAdministrator  **
  - **IAM action:**  [securitylake:DeregisterDataLakeDelegatedAdministrator](#list_securitylake-action-DeregisterDataLakeDelegatedAdministrator) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetDataLakeExceptionSubscription  **
  - **IAM action:**  [securitylake:GetDataLakeExceptionSubscription](#list_securitylake-action-GetDataLakeExceptionSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataLakeOrganizationConfiguration  **
  - **IAM action:**  [securitylake:GetDataLakeOrganizationConfiguration](#list_securitylake-action-GetDataLakeOrganizationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataLakeSources  **
  - **IAM action:**  [securitylake:GetDataLakeSources](#list_securitylake-action-GetDataLakeSources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSubscriber  **
  - **IAM action:**  [securitylake:GetSubscriber](#list_securitylake-action-GetSubscriber) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDataLakeExceptions  **
  - **IAM action:**  [securitylake:ListDataLakeExceptions](#list_securitylake-action-ListDataLakeExceptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDataLakes  **
  - **IAM action:**  [securitylake:ListDataLakes](#list_securitylake-action-ListDataLakes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLogSources  **
  - **IAM action:**  [securitylake:ListLogSources](#list_securitylake-action-ListLogSources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSubscribers  **
  - **IAM action:**  [securitylake:ListSubscribers](#list_securitylake-action-ListSubscribers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [securitylake:ListTagsForResource](#list_securitylake-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   RegisterDataLakeDelegatedAdministrator  **
  - **IAM action:**  [securitylake:RegisterDataLakeDelegatedAdministrator](#list_securitylake-action-RegisterDataLakeDelegatedAdministrator) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [securitylake:TagResource](#list_securitylake-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [securitylake:UntagResource](#list_securitylake-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateDataLake  **
  - **IAM action:**  [securitylake:UpdateDataLake](#list_securitylake-action-UpdateDataLake)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** s3.amazonaws.com / **Access level:** Write

- **   UpdateDataLakeExceptionSubscription  **
  - **IAM action:**  [securitylake:UpdateDataLakeExceptionSubscription](#list_securitylake-action-UpdateDataLakeExceptionSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSubscriber  **
  - **IAM action:**  [securitylake:UpdateSubscriber](#list_securitylake-action-UpdateSubscriber) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSubscriberNotification  **
  - **IAM action:**  [securitylake:UpdateSubscriberNotification](#list_securitylake-action-UpdateSubscriberNotification)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** events.amazonaws.com / **Access level:** Write



## Actions defined by Amazon Security Lake
<a name="list_securitylake-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateAwsLogSource](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_CreateAwsLogSource.html)  **
  - **Description:** Grants permission to enable any source type in any region for accounts that are either part of a trusted organization or standalone account
  - **Resource types (\*required):** [data-lake\*](#list_securitylake-resource-data-lake)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_securitylake-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_securitylake-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateCustomLogSource](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_CreateCustomLogSource.html)  **
  - **Description:** Grants permission to add a custom source
  - **Resource types (\*required):** [data-lake\*](#list_securitylake-resource-data-lake)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_securitylake-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_securitylake-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateDataLake](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_CreateDataLake.html)  **
  - **Description:** Grants permission to create a new security data lake
  - **Resource types (\*required):** [data-lake\*](#list_securitylake-resource-data-lake)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_securitylake-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_securitylake-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_securitylake-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDataLakeExceptionSubscription](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_CreateDataLakeExceptionSubscription.html)  **
  - **Description:** Grants permission to get instant notifications about exceptions. Subscribes to the SNS topics for exception notifications
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateDataLakeOrganizationConfiguration](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_CreateDataLakeOrganizationConfiguration.html)  **
  - **Description:** Grants permission to automatically enable Amazon Security Lake for new member accounts in your organization
  - **Resource types (\*required):** [data-lake\*](#list_securitylake-resource-data-lake)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_securitylake-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_securitylake-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateSubscriber](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_CreateSubscriber.html)  **
  - **Description:** Grants permission to create a subscriber
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_securitylake-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_securitylake-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_securitylake-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSubscriberNotification](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_CreateSubscriberNotification.html)  **
  - **Description:** Grants permission to create a webhook invocation to notify a client when there is new data in the data lake
  - **Resource types (\*required):** [subscriber\*](#list_securitylake-resource-subscriber)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_securitylake-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_securitylake-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAwsLogSource](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DeleteAwsLogSource.html)  **
  - **Description:** Grants permission to disable any source type in any region for accounts that are part of a trusted organization or standalone accounts
  - **Resource types (\*required):** [data-lake\*](#list_securitylake-resource-data-lake)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_securitylake-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_securitylake-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCustomLogSource](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DeleteCustomLogSource.html)  **
  - **Description:** Grants permission to remove a custom source
  - **Resource types (\*required):** [data-lake\*](#list_securitylake-resource-data-lake)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_securitylake-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_securitylake-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDataLake](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DeleteDataLake.html)  **
  - **Description:** Grants permission to delete security data lake
  - **Resource types (\*required):** [data-lake\*](#list_securitylake-resource-data-lake)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_securitylake-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_securitylake-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDataLakeExceptionSubscription](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DeleteDataLakeExceptionSubscription.html)  **
  - **Description:** Grants permission to unsubscribe from SNS topics for exception notifications. Removes exception notifications for the SNS topic
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteDataLakeOrganizationConfiguration](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DeleteDataLakeOrganizationConfiguration.html)  **
  - **Description:** Grants permission to remove the automatic enablement of Amazon Security Lake access for new organization accounts
  - **Resource types (\*required):** [data-lake\*](#list_securitylake-resource-data-lake)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_securitylake-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_securitylake-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSubscriber](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DeleteSubscriber.html)  **
  - **Description:** Grants permission to delete the specified subscriber
  - **Resource types (\*required):** [subscriber\*](#list_securitylake-resource-subscriber)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_securitylake-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_securitylake-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSubscriberNotification](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DeleteSubscriberNotification.html)  **
  - **Description:** Grants permission to remove a webhook invocation to notify a client when there is new data in the data lake
  - **Resource types (\*required):** [subscriber\*](#list_securitylake-resource-subscriber)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_securitylake-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_securitylake-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeregisterDataLakeDelegatedAdministrator](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DeregisterDataLakeDelegatedAdministrator.html)  **
  - **Description:** Grants permission to remove the Delegated Administrator account and disable Amazon Security Lake as a service for this organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetDataLakeExceptionSubscription](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_GetDataLakeExceptionSubscription.html)  **
  - **Description:** Grants permission to query the protocol and endpoint that were provided when subscribing to SNS topics for exception notifications
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetDataLakeOrganizationConfiguration](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_GetDataLakeOrganizationConfiguration.html)  **
  - **Description:** Grants permission to get an organization's configuration setting for automatically enabling Amazon Security Lake access for new organization accounts
  - **Resource types (\*required):** [data-lake\*](#list_securitylake-resource-data-lake)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_securitylake-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_securitylake-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDataLakeSources](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_GetDataLakeSources.html)  **
  - **Description:** Grants permission to get a static snapshot of the security data lake in the current region. The snapshot includes enabled accounts and log sources
  - **Resource types (\*required):** [data-lake\*](#list_securitylake-resource-data-lake)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_securitylake-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_securitylake-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSubscriber](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_GetSubscriber.html)  **
  - **Description:** Grants permission to get information about subscriber that is already created
  - **Resource types (\*required):** [subscriber\*](#list_securitylake-resource-subscriber)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_securitylake-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_securitylake-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListDataLakeExceptions](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_ListDataLakeExceptions.html)  **
  - **Description:** Grants permission to get the list of all non-retryable failures
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDataLakes](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_ListDataLakes.html)  **
  - **Description:** Grants permission to list information about the security data lakes
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListLogSources](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_ListLogSources.html)  **
  - **Description:** Grants permission to view the enabled accounts. You can view the enabled sources in the enabled regions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSubscribers](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_ListSubscribers.html)  **
  - **Description:** Grants permission to list all subscribers
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list all tags for the resource
  - **Resource types (\*required):** [data-lake](#list_securitylake-resource-data-lake) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_securitylake-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_securitylake-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [subscriber](#list_securitylake-resource-subscriber) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_securitylake-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_securitylake-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [RegisterDataLakeDelegatedAdministrator](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_RegisterDataLakeDelegatedAdministrator.html)  **
  - **Description:** Grants permission to designate an account as the Amazon Security Lake administrator account for the organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to the resource
  - **Resource types (\*required):** [data-lake](#list_securitylake-resource-data-lake) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_securitylake-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_securitylake-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_securitylake-aws_TagKeys)
  - **Resource types (\*required):** [subscriber](#list_securitylake-resource-subscriber) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_securitylake-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_securitylake-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_securitylake-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from the resource
  - **Resource types (\*required):** [data-lake](#list_securitylake-resource-data-lake) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_securitylake-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_securitylake-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_securitylake-aws_TagKeys)
  - **Resource types (\*required):** [subscriber](#list_securitylake-resource-subscriber) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_securitylake-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_securitylake-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_securitylake-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateDataLake](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_UpdateDataLake.html)  **
  - **Description:** Grants permission to update a security data lake
  - **Resource types (\*required):** [data-lake\*](#list_securitylake-resource-data-lake)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_securitylake-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_securitylake-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDataLakeExceptionSubscription](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_UpdateDataLakeExceptionSubscription.html)  **
  - **Description:** Grants permission to update subscriptions to the SNS topics for exception notifications
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateSubscriber](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_UpdateSubscriber.html)  **
  - **Description:** Grants permission to update subscriber
  - **Resource types (\*required):** [subscriber\*](#list_securitylake-resource-subscriber)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_securitylake-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_securitylake-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSubscriberNotification](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_UpdateSubscriberNotification.html)  **
  - **Description:** Grants permission to update a webhook invocation to notify a client when there is new data in the data lake
  - **Resource types (\*required):** [subscriber\*](#list_securitylake-resource-subscriber)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_securitylake-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_securitylake-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon Security Lake
<a name="list_securitylake-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [data-lake](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DataLakeResource.html)  | arn:${Partition}:securitylake:${Region}:${Account}:data-lake/default | [aws:RequestTag/${TagKey}](#list_securitylake-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_securitylake-aws_ResourceTag___TagKey_) | 
|  [subscriber](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_SubscriberResource.html)  | arn:${Partition}:securitylake:${Region}:${Account}:subscriber/${SubscriberId} | [aws:RequestTag/${TagKey}](#list_securitylake-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_securitylake-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Security Lake
<a name="list_securitylake-policy-keys"></a>

Amazon Security Lake defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by a tag key and value pair of a resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by tag keys that are passed in the request | ArrayOfString | 