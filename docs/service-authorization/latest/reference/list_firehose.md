

# Actions, resources, and condition keys for Amazon Kinesis Firehose
<a name="list_firehose"></a>

Amazon Kinesis Firehose (service prefix: `firehose`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/firehose/latest/dev/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/firehose/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/firehose/latest/dev/controlling-access.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/firehose/firehose.json) for this service.

**Topics**
+ [API operations defined by Amazon Kinesis Firehose](#list_firehose-operations)
+ [Actions defined by Amazon Kinesis Firehose](#list_firehose-actions-as-permissions)
+ [Resource types defined by Amazon Kinesis Firehose](#list_firehose-resources-for-iam-policies)
+ [Condition keys for Amazon Kinesis Firehose](#list_firehose-policy-keys)

## API operations defined by Amazon Kinesis Firehose
<a name="list_firehose-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_firehose-actions-as-permissions).




- **   CreateDeliveryStream  **
  - **IAM action:**  [firehose:CreateDeliveryStream](#list_firehose-action-CreateDeliveryStream)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [firehose:TagDeliveryStream](#list_firehose-action-TagDeliveryStream)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** firehose.amazonaws.com / **Access level:** Write

- **   DeleteDeliveryStream  **
  - **IAM action:**  [firehose:DeleteDeliveryStream](#list_firehose-action-DeleteDeliveryStream) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeDeliveryStream  **
  - **IAM action:**  [firehose:DescribeDeliveryStream](#list_firehose-action-DescribeDeliveryStream) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDeliveryStreams  **
  - **IAM action:**  [firehose:ListDeliveryStreams](#list_firehose-action-ListDeliveryStreams) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForDeliveryStream  **
  - **IAM action:**  [firehose:ListTagsForDeliveryStream](#list_firehose-action-ListTagsForDeliveryStream) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutRecord  **
  - **IAM action:**  [firehose:PutRecord](#list_firehose-action-PutRecord) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutRecordBatch  **
  - **IAM action:**  [firehose:PutRecordBatch](#list_firehose-action-PutRecordBatch) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartDeliveryStreamEncryption  **
  - **IAM action:**  [firehose:StartDeliveryStreamEncryption](#list_firehose-action-StartDeliveryStreamEncryption) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopDeliveryStreamEncryption  **
  - **IAM action:**  [firehose:StopDeliveryStreamEncryption](#list_firehose-action-StopDeliveryStreamEncryption) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagDeliveryStream  **
  - **IAM action:**  [firehose:TagDeliveryStream](#list_firehose-action-TagDeliveryStream) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagDeliveryStream  **
  - **IAM action:**  [firehose:UntagDeliveryStream](#list_firehose-action-UntagDeliveryStream) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateDestination  **
  - **IAM action:**  [firehose:UpdateDestination](#list_firehose-action-UpdateDestination)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** firehose.amazonaws.com / **Access level:** Write



## Actions defined by Amazon Kinesis Firehose
<a name="list_firehose-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateDeliveryStream](https://docs.aws.amazon.com/firehose/latest/APIReference/API_CreateDeliveryStream.html)  **
  - **Description:** Grants permission to create a delivery stream
  - **Resource types (\*required):** [deliverystream\*](#list_firehose-resource-deliverystream)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_firehose-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_firehose-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_firehose-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteDeliveryStream](https://docs.aws.amazon.com/firehose/latest/APIReference/API_DeleteDeliveryStream.html)  **
  - **Description:** Grants permission to delete a delivery stream and its data
  - **Resource types (\*required):** [deliverystream\*](#list_firehose-resource-deliverystream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_firehose-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeDeliveryStream](https://docs.aws.amazon.com/firehose/latest/APIReference/API_DescribeDeliveryStream.html)  **
  - **Description:** Grants permission to describe the specified delivery stream and gets the status
  - **Resource types (\*required):** [deliverystream\*](#list_firehose-resource-deliverystream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_firehose-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListDeliveryStreams](https://docs.aws.amazon.com/firehose/latest/APIReference/API_ListDeliveryStreams.html)  **
  - **Description:** Grants permission to list your delivery streams
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForDeliveryStream](https://docs.aws.amazon.com/firehose/latest/APIReference/API_ListTagsForDeliveryStream.html)  **
  - **Description:** Grants permission to list the tags for the specified delivery stream
  - **Resource types (\*required):** [deliverystream\*](#list_firehose-resource-deliverystream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_firehose-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [PutRecord](https://docs.aws.amazon.com/firehose/latest/APIReference/API_PutRecord.html)  **
  - **Description:** Grants permission to write a single data record into an Amazon Kinesis Firehose delivery stream
  - **Resource types (\*required):** [deliverystream\*](#list_firehose-resource-deliverystream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_firehose-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutRecordBatch](https://docs.aws.amazon.com/firehose/latest/APIReference/API_PutRecordBatch.html)  **
  - **Description:** Grants permission to write multiple data records into a delivery stream in a single call, which can achieve higher throughput per producer than when writing single records
  - **Resource types (\*required):** [deliverystream\*](#list_firehose-resource-deliverystream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_firehose-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartDeliveryStreamEncryption](https://docs.aws.amazon.com/firehose/latest/APIReference/API_StartDeliveryStreamEncryption.html)  **
  - **Description:** Grants permission to enable server-side encryption (SSE) for the delivery stream
  - **Resource types (\*required):** [deliverystream\*](#list_firehose-resource-deliverystream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_firehose-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopDeliveryStreamEncryption](https://docs.aws.amazon.com/firehose/latest/APIReference/API_StopDeliveryStreamEncryption.html)  **
  - **Description:** Grants permission to disable the specified destination of the specified delivery stream
  - **Resource types (\*required):** [deliverystream\*](#list_firehose-resource-deliverystream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_firehose-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagDeliveryStream](https://docs.aws.amazon.com/firehose/latest/APIReference/API_TagDeliveryStream.html)  **
  - **Description:** Grants permission to add or update tags for the specified delivery stream
  - **Resource types (\*required):** [deliverystream\*](#list_firehose-resource-deliverystream)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_firehose-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_firehose-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_firehose-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagDeliveryStream](https://docs.aws.amazon.com/firehose/latest/APIReference/API_UntagDeliveryStream.html)  **
  - **Description:** Grants permission to remove tags from the specified delivery stream
  - **Resource types (\*required):** [deliverystream\*](#list_firehose-resource-deliverystream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_firehose-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_firehose-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateDestination](https://docs.aws.amazon.com/firehose/latest/APIReference/API_UpdateDestination.html)  **
  - **Description:** Grants permission to update the specified destination of the specified delivery stream
  - **Resource types (\*required):** [deliverystream\*](#list_firehose-resource-deliverystream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_firehose-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon Kinesis Firehose
<a name="list_firehose-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [deliverystream](https://docs.aws.amazon.com/firehose/latest/dev/basic-create.html)  | arn:${Partition}:firehose:${Region}:${Account}:deliverystream/${DeliveryStreamName} | [aws:ResourceTag/${TagKey}](#list_firehose-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Kinesis Firehose
<a name="list_firehose-policy-keys"></a>

Amazon Kinesis Firehose defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 