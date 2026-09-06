

# Actions, resources, and condition keys for AWS IoT Events
<a name="list_iotevents"></a>

AWS IoT Events (service prefix: `iotevents`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/iotevents/index.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/iotevents/latest/apireference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/iotevents/latest/developerguide/auth-and-access-control.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/iotevents/iotevents.json) for this service.

**Topics**
+ [Actions defined by AWS IoT Events](#list_iotevents-actions-as-permissions)
+ [Resource types defined by AWS IoT Events](#list_iotevents-resources-for-iam-policies)
+ [Condition keys for AWS IoT Events](#list_iotevents-policy-keys)

## Actions defined by AWS IoT Events
<a name="list_iotevents-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [BatchAcknowledgeAlarm](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_BatchAcknowledgeAlarm.html)  **
  - **Description:** Grants permission to send one or more acknowledge action requests to AWS IoT Events
  - **Resource types (\*required):** [alarmModel\*](#list_iotevents-resource-alarmModel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchDeleteDetector](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_BatchDeleteDetector.html)  **
  - **Description:** Grants permission to delete a detector instance within the AWS IoT Events system
  - **Resource types (\*required):** [detectorModel\*](#list_iotevents-resource-detectorModel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchDisableAlarm](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_BatchDisableAlarm.html)  **
  - **Description:** Grants permission to disable one or more alarm instances
  - **Resource types (\*required):** [alarmModel\*](#list_iotevents-resource-alarmModel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchEnableAlarm](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_BatchEnableAlarm.html)  **
  - **Description:** Grants permission to enable one or more alarm instances
  - **Resource types (\*required):** [alarmModel\*](#list_iotevents-resource-alarmModel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchPutMessage](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_BatchPutMessage.html)  **
  - **Description:** Grants permission to send a set of messages to the AWS IoT Events system
  - **Resource types (\*required):** [input\*](#list_iotevents-resource-input)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchResetAlarm](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_BatchResetAlarm.html)  **
  - **Description:** Grants permission to reset one or more alarm instances
  - **Resource types (\*required):** [alarmModel\*](#list_iotevents-resource-alarmModel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchSnoozeAlarm](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_BatchSnoozeAlarm.html)  **
  - **Description:** Grants permission to change one or more alarm instances to the snooze mode
  - **Resource types (\*required):** [alarmModel\*](#list_iotevents-resource-alarmModel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchUpdateDetector](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_BatchUpdateDetector.html)  **
  - **Description:** Grants permission to update a detector instance within the AWS IoT Events system
  - **Resource types (\*required):** [detectorModel\*](#list_iotevents-resource-detectorModel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateAlarmModel](https://docs.aws.amazon.com/iotevents/latest/apireference/API_CreateAlarmModel.html)  **
  - **Description:** Grants permission to create an alarm model to monitor an AWS IoT Events input attribute or an AWS IoT SiteWise asset property
  - **Resource types (\*required):** [alarmModel\*](#list_iotevents-resource-alarmModel)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotevents-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotevents-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDetectorModel](https://docs.aws.amazon.com/iotevents/latest/apireference/API_CreateDetectorModel.html)  **
  - **Description:** Grants permission to create a detector model to monitor an AWS IoT Events input attribute
  - **Resource types (\*required):** [detectorModel\*](#list_iotevents-resource-detectorModel)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotevents-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotevents-aws_TagKeys)
  - **Access level:** Write

- **   [CreateInput](https://docs.aws.amazon.com/iotevents/latest/apireference/API_CreateInput.html)  **
  - **Description:** Grants permission to create an Input in IotEvents
  - **Resource types (\*required):** [input\*](#list_iotevents-resource-input)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotevents-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotevents-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteAlarmModel](https://docs.aws.amazon.com/iotevents/latest/apireference/API_DeleteAlarmModel.html)  **
  - **Description:** Grants permission to delete an alarm model
  - **Resource types (\*required):** [alarmModel\*](#list_iotevents-resource-alarmModel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDetectorModel](https://docs.aws.amazon.com/iotevents/latest/apireference/API_DeleteDetectorModel.html)  **
  - **Description:** Grants permission to delete a detector model
  - **Resource types (\*required):** [detectorModel\*](#list_iotevents-resource-detectorModel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteInput](https://docs.aws.amazon.com/iotevents/latest/apireference/API_DeleteInput.html)  **
  - **Description:** Grants permission to delete an input
  - **Resource types (\*required):** [input\*](#list_iotevents-resource-input)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeAlarm](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_DescribeAlarm.html)  **
  - **Description:** Grants permission to retrieve information about an alarm instance
  - **Resource types (\*required):** [alarmModel\*](#list_iotevents-resource-alarmModel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeAlarmModel](https://docs.aws.amazon.com/iotevents/latest/apireference/API_DescribeAlarmModel.html)  **
  - **Description:** Grants permission to retrieve information about an alarm model
  - **Resource types (\*required):** [alarmModel\*](#list_iotevents-resource-alarmModel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDetector](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_DescribeDetector.html)  **
  - **Description:** Grants permission to retriev information about a detector instance
  - **Resource types (\*required):** [detectorModel\*](#list_iotevents-resource-detectorModel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDetectorModel](https://docs.aws.amazon.com/iotevents/latest/apireference/API_DescribeDetectorModel.html)  **
  - **Description:** Grants permission to retrieve information about a detector model
  - **Resource types (\*required):** [detectorModel\*](#list_iotevents-resource-detectorModel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDetectorModelAnalysis](https://docs.aws.amazon.com/iotevents/latest/apireference/API_DescribeDetectorModelAnalysis.html)  **
  - **Description:** Grants permission to retrieve the detector model analysis information
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeInput](https://docs.aws.amazon.com/iotevents/latest/apireference/API_DescribeInput.html)  **
  - **Description:** Grants permission to retrieve an information about Input
  - **Resource types (\*required):** [input\*](#list_iotevents-resource-input)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeLoggingOptions](https://docs.aws.amazon.com/iotevents/latest/apireference/API_DescribeLoggingOptions.html)  **
  - **Description:** Grants permission to retrieve the current settings of the AWS IoT Events logging options
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetDetectorModelAnalysisResults](https://docs.aws.amazon.com/iotevents/latest/apireference/API_GetDetectorModelAnalysisResults.html)  **
  - **Description:** Grants permission to retrieve the detector model analysis results
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListAlarmModelVersions](https://docs.aws.amazon.com/iotevents/latest/apireference/API_ListAlarmModelVersions.html)  **
  - **Description:** Grants permission to list all the versions of an alarm model
  - **Resource types (\*required):** [alarmModel\*](#list_iotevents-resource-alarmModel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAlarmModels](https://docs.aws.amazon.com/iotevents/latest/apireference/API_ListAlarmModels.html)  **
  - **Description:** Grants permission to list the alarm models that you created
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAlarms](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_ListAlarms.html)  **
  - **Description:** Grants permission to retrieve information about all alarm instances per alarmModel
  - **Resource types (\*required):** [alarmModel\*](#list_iotevents-resource-alarmModel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDetectorModelVersions](https://docs.aws.amazon.com/iotevents/latest/apireference/API_ListDetectorModelVersions.html)  **
  - **Description:** Grants permission to list all the versions of a detector model
  - **Resource types (\*required):** [detectorModel\*](#list_iotevents-resource-detectorModel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDetectorModels](https://docs.aws.amazon.com/iotevents/latest/apireference/API_ListDetectorModels.html)  **
  - **Description:** Grants permission to list the detector models that you created
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDetectors](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_ListDetectors.html)  **
  - **Description:** Grants permission to retrieve information about all detector instances per detectormodel
  - **Resource types (\*required):** [detectorModel\*](#list_iotevents-resource-detectorModel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListInputRoutings](https://docs.aws.amazon.com/iotevents/latest/apireference/API_ListInputRoutings.html)  **
  - **Description:** Grants permission to list one or more input routings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListInputs](https://docs.aws.amazon.com/iotevents/latest/apireference/API_ListInputs.html)  **
  - **Description:** Grants permission to lists the inputs you have created
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/iotevents/latest/apireference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags (metadata) which you have assigned to the resource
  - **Resource types (\*required):** [alarmModel](#list_iotevents-resource-alarmModel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [detectorModel](#list_iotevents-resource-detectorModel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [input](#list_iotevents-resource-input) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PutLoggingOptions](https://docs.aws.amazon.com/iotevents/latest/apireference/API_PutLoggingOptions.html)  **
  - **Description:** Grants permission to set or update the AWS IoT Events logging options
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartDetectorModelAnalysis](https://docs.aws.amazon.com/iotevents/latest/apireference/API_StartDetectorModelAnalysis.html)  **
  - **Description:** Grants permission to start the detector model analysis
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/iotevents/latest/apireference/API_TagResource.html)  **
  - **Description:** Grants permission to adds to or modifies the tags of the given resource.Tags are metadata which can be used to manage a resource
  - **Resource types (\*required):** [alarmModel](#list_iotevents-resource-alarmModel) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotevents-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotevents-aws_TagKeys)
  - **Resource types (\*required):** [detectorModel](#list_iotevents-resource-detectorModel) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotevents-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotevents-aws_TagKeys)
  - **Resource types (\*required):** [input](#list_iotevents-resource-input) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_iotevents-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotevents-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/iotevents/latest/apireference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove the given tags (metadata) from the resource
  - **Resource types (\*required):** [alarmModel](#list_iotevents-resource-alarmModel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotevents-aws_TagKeys)
  - **Resource types (\*required):** [detectorModel](#list_iotevents-resource-detectorModel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotevents-aws_TagKeys)
  - **Resource types (\*required):** [input](#list_iotevents-resource-input) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_iotevents-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAlarmModel](https://docs.aws.amazon.com/iotevents/latest/apireference/API_UpdateAlarmModel.html)  **
  - **Description:** Grants permission to update an alarm model
  - **Resource types (\*required):** [alarmModel\*](#list_iotevents-resource-alarmModel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDetectorModel](https://docs.aws.amazon.com/iotevents/latest/apireference/API_UpdateDetectorModel.html)  **
  - **Description:** Grants permission to update a detector model
  - **Resource types (\*required):** [detectorModel\*](#list_iotevents-resource-detectorModel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateInput](https://docs.aws.amazon.com/iotevents/latest/apireference/API_UpdateInput.html)  **
  - **Description:** Grants permission to update an input
  - **Resource types (\*required):** [input\*](#list_iotevents-resource-input)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateInputRouting](https://docs.aws.amazon.com/iotevents/latest/apireference/API_UpdateInputRouting.html)  **
  - **Description:** Grants permission to update input routing
  - **Resource types (\*required):** [input\*](#list_iotevents-resource-input)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS IoT Events
<a name="list_iotevents-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [alarmModel](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-getting-started.html)  | arn:${Partition}:iotevents:${Region}:${Account}:alarmModel/${AlarmModelName} | [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_) | 
|  [detectorModel](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-getting-started.html)  | arn:${Partition}:iotevents:${Region}:${Account}:detectorModel/${DetectorModelName} | [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_) | 
|  [input](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-getting-started.html)  | arn:${Partition}:iotevents:${Region}:${Account}:input/${InputName} | [aws:ResourceTag/${TagKey}](#list_iotevents-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS IoT Events
<a name="list_iotevents-policy-keys"></a>

AWS IoT Events defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters actions by the tag keys in the request | ArrayOfString | 
|   [iotevents:keyValue](https://docs.aws.amazon.com/iotevents/latest/developerguide/security_iam_id-based-policy-examples.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the instanceId (key-value) of the message | String | 