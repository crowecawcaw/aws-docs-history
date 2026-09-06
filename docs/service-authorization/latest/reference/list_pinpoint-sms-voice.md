

# Actions, resources, and condition keys for Amazon Pinpoint SMS and Voice Service
<a name="list_pinpoint-sms-voice"></a>

Amazon Pinpoint SMS and Voice Service (service prefix: `sms-voice`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/pinpoint/latest/developerguide).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/pinpoint-sms-voice/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/pinpoint/latest/developerguide/permissions-actions.html#permissions-actions-apiactions) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/sms-voice/sms-voice.json) for this service.

**Topics**
+ [API operations defined by Amazon Pinpoint SMS and Voice Service](#list_pinpoint-sms-voice-operations)
+ [Actions defined by Amazon Pinpoint SMS and Voice Service](#list_pinpoint-sms-voice-actions-as-permissions)
+ [Resource types defined by Amazon Pinpoint SMS and Voice Service](#list_pinpoint-sms-voice-resources-for-iam-policies)
+ [Condition keys for Amazon Pinpoint SMS and Voice Service](#list_pinpoint-sms-voice-policy-keys)

## API operations defined by Amazon Pinpoint SMS and Voice Service
<a name="list_pinpoint-sms-voice-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_pinpoint-sms-voice-actions-as-permissions).




- **   CreateConfigurationSet  **
  - **SDK client:** pinpoint-sms-voice
  - **IAM action:**  [sms-voice:CreateConfigurationSet](#list_pinpoint-sms-voice-action-CreateConfigurationSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sms-voice:TagResource](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_TagResource.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateConfigurationSetEventDestination  **
  - **SDK client:** pinpoint-sms-voice
  - **IAM action:**  [sms-voice:CreateConfigurationSetEventDestination](#list_pinpoint-sms-voice-action-CreateConfigurationSetEventDestination)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sms-voice.amazonaws.com / **Access level:** Write

- **   DeleteConfigurationSet  **
  - **SDK client:** pinpoint-sms-voice
  - **IAM action:**  [sms-voice:DeleteConfigurationSet](#list_pinpoint-sms-voice-action-DeleteConfigurationSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConfigurationSetEventDestination  **
  - **SDK client:** pinpoint-sms-voice
  - **IAM action:**  [sms-voice:DeleteConfigurationSetEventDestination](#list_pinpoint-sms-voice-action-DeleteConfigurationSetEventDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetConfigurationSetEventDestinations  **
  - **SDK client:** pinpoint-sms-voice
  - **IAM action:**  [sms-voice:GetConfigurationSetEventDestinations](#list_pinpoint-sms-voice-action-GetConfigurationSetEventDestinations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListConfigurationSets  **
  - **SDK client:** pinpoint-sms-voice
  - **IAM action:**  [sms-voice:ListConfigurationSets](#list_pinpoint-sms-voice-action-ListConfigurationSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   SendVoiceMessage  **
  - **SDK client:** pinpoint-sms-voice
  - **IAM action:**  [sms-voice:SendVoiceMessage](#list_pinpoint-sms-voice-action-SendVoiceMessage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateConfigurationSetEventDestination  **
  - **SDK client:** pinpoint-sms-voice
  - **IAM action:**  [sms-voice:UpdateConfigurationSetEventDestination](#list_pinpoint-sms-voice-action-UpdateConfigurationSetEventDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateConfigurationSet  **
  - **SDK client:** sms-voice
  - **IAM action:**  [sms-voice:CreateConfigurationSet](#list_pinpoint-sms-voice-action-CreateConfigurationSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sms-voice:TagResource](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_TagResource.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateConfigurationSetEventDestination  **
  - **SDK client:** sms-voice
  - **IAM action:**  [sms-voice:CreateConfigurationSetEventDestination](#list_pinpoint-sms-voice-action-CreateConfigurationSetEventDestination)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sms-voice.amazonaws.com / **Access level:** Write

- **   DeleteConfigurationSet  **
  - **SDK client:** sms-voice
  - **IAM action:**  [sms-voice:DeleteConfigurationSet](#list_pinpoint-sms-voice-action-DeleteConfigurationSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConfigurationSetEventDestination  **
  - **SDK client:** sms-voice
  - **IAM action:**  [sms-voice:DeleteConfigurationSetEventDestination](#list_pinpoint-sms-voice-action-DeleteConfigurationSetEventDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetConfigurationSetEventDestinations  **
  - **SDK client:** sms-voice
  - **IAM action:**  [sms-voice:GetConfigurationSetEventDestinations](#list_pinpoint-sms-voice-action-GetConfigurationSetEventDestinations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListConfigurationSets  **
  - **SDK client:** sms-voice
  - **IAM action:**  [sms-voice:ListConfigurationSets](#list_pinpoint-sms-voice-action-ListConfigurationSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   SendVoiceMessage  **
  - **SDK client:** sms-voice
  - **IAM action:**  [sms-voice:SendVoiceMessage](#list_pinpoint-sms-voice-action-SendVoiceMessage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateConfigurationSetEventDestination  **
  - **SDK client:** sms-voice
  - **IAM action:**  [sms-voice:UpdateConfigurationSetEventDestination](#list_pinpoint-sms-voice-action-UpdateConfigurationSetEventDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Pinpoint SMS and Voice Service
<a name="list_pinpoint-sms-voice-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [CreateConfigurationSet](https://docs.aws.amazon.com/pinpoint-sms-voice/latest/APIReference/v1-sms-voice-configuration-sets.html)  | Create a new configuration set. After you create the configuration set, you can add one or more event destinations to it. |  |   | Write | 
|   [CreateConfigurationSetEventDestination](https://docs.aws.amazon.com/pinpoint-sms-voice/latest/APIReference/v1-sms-voice-configuration-sets-configurationsetname-event-destinations.html)  | Create a new event destination in a configuration set. |  |   | Write | 
|   [DeleteConfigurationSet](https://docs.aws.amazon.com/pinpoint-sms-voice/latest/APIReference/v1-sms-voice-configuration-sets-configurationsetname.html)  | Deletes an existing configuration set. |  |   | Write | 
|   [DeleteConfigurationSetEventDestination](https://docs.aws.amazon.com/pinpoint-sms-voice/latest/APIReference/v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationname.html)  | Deletes an event destination in a configuration set. |  |   | Write | 
|   [GetConfigurationSetEventDestinations](https://docs.aws.amazon.com/pinpoint-sms-voice/latest/APIReference/v1-sms-voice-configuration-sets-configurationsetname-event-destinations.html)  | Obtain information about an event destination, including the types of events it reports, the Amazon Resource Name (ARN) of the destination, and the name of the event destination. |  |   | Read | 
|   [ListConfigurationSets](https://docs.aws.amazon.com/pinpoint-sms-voice/latest/APIReference/v1-sms-voice-configuration-sets.html)  | Return a list of configuration sets. This operation only returns the configuration sets that are associated with your account in the current AWS Region. |  |   | Read | 
|   [SendVoiceMessage](https://docs.aws.amazon.com/pinpoint-sms-voice/latest/APIReference/v1-sms-voice-voice-message.html)  | Create a new voice message and send it to a recipient's phone number. |  |   | Write | 
|   [UpdateConfigurationSetEventDestination](https://docs.aws.amazon.com/pinpoint-sms-voice/latest/APIReference/v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationname.html)  | Update an event destination in a configuration set. An event destination is a location that you publish information about your voice calls to. For example, you can log an event to an Amazon CloudWatch destination when a call fails. |  |   | Write | 

## Resource types defined by Amazon Pinpoint SMS and Voice Service
<a name="list_pinpoint-sms-voice-resources-for-iam-policies"></a>

Amazon Pinpoint SMS and Voice Service does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for Amazon Pinpoint SMS and Voice Service
<a name="list_pinpoint-sms-voice-policy-keys"></a>

Amazon Pinpoint SMS and Voice Service has no service-specific condition keys that can be used in the `Condition` element of policy statements.