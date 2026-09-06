

# Troubleshoot Amazon SQS API errors
<a name="troubleshooting-api-errors"></a>

The following topics cover the most common errors returned when making Amazon SQS API calls, and how to troubleshoot them.

## QueueDoesNotExist error
<a name="queuedoesnotexist-error"></a>

This error will be returned when the Amazon SQS service can't find the mentioned queue for the Amazon SQS action.

**Possible causes and mitigations:**
+ **Incorrect region:** Review the Amazon SQS client configuration to confirm that you configured the correct Region on the client. When you don't configure a Region on the client, then the SDK or AWS CLI chooses the Region from the [configuration file](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html) or the environment variable. If the SDK doesn't find a Region in the configuration file, then the SDK sets the Region to us-east-1 by default. 
+ **Queue might be recently deleted:** If the queue was deleted before the API call was made, then the API call will return this error. Check CloudTrail for any [DeleteQueue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_DeleteQueue.html) operations before the time of the error.
+ **Permission issues:** If the requesting AWS Identity and Access Management (IAM) user or role doesn't have the required permissions, then you might receive the following error:

  ```
  The specified queue does not exist or you do not have access to it.
  ```

  Check the permissions, and make the API call with correct permissions. 

For more details on troubleshooting the `QueueDoesNotExist` error, see [How do I troubleshoot the QueueDoesNotExist error when I make API calls to my Amazon SQS queue?](https://repost.aws/knowledge-center/sqs-queuedoesnotexist-errors) in the *AWS Knowledge Center Guide*.

## InvalidAttributeValue error
<a name="invalidattributevalue-error"></a>

This error will be returned upon updating the Amazon SQS queue resource policy, or properties with an incorrect policy or a principal.

**Possible causes and mitigations:**
+ **Invalid resource policy:** Check that the resource policy has all the required fields. For more information, see [IAM JSON policy elements reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html) and [Validating IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_policy-validator.html). You can also use the [IAM policy generator](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation.html) to create and test an Amazon SQS resource policy. Make sure that the policy is in JSON format.
+ **Invalid principal:** Ensure that the `Principal` element exists in the resource policy and that the value is valid. If your Amazon SQS resource policy `Principal` element includes an IAM entity, make sure that the entity exists before you use the policy. Amazon SQS validates the resource policy and checks for the IAM entity. If the IAM entity doesn't exist, you will receive an error. To confirm IAM entities, use the [`GetRole`](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetRole.html) and [`GetUser`](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetUser.html) APIs.

For additional information on how to troubleshoot an `InvalidAttributeValue` error, see [How do I troubleshoot the QueueDoesNotExist error when I make API calls to my Amazon SQS queue?](https://repost.aws/knowledge-center/sqs-invalid-parameter-policy) in the *AWS Knowledge Center Guide*.

## ReceiptHandle error
<a name="receipthandle-error"></a>

Upon making a [`DeleteMessage`](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_DeleteMessage.html) API call, the error `ReceiptHandleIsInvalid` or `InvalidParameterValue` might be returned if the receipt handle is incorrect or expired.
+ **ReceiptHandleIsInvalid error:** If the receipt handle is incorrect, you'll receive an error similar to this example:

  ```
  An error occurred (ReceiptHandleIsInvalid) when calling the DeleteMessage operation: The input receipt handle <YOUR RECEIPT HANDLE> is not a valid receipt handle.
  ```
+ **InvalidParameterValue error:** If the receipt handle is expired, you'll receive an error similar to this example:

  ```
  An error occurred (InvalidParameterValue) when calling the DeleteMessage operation: Value <YOUR RECEIPT HANDLE> for parameter ReceiptHandle is invalid. Reason: The receipt handle has expired.
  ```

**Possible causes and mitigations:**

The receipt handle is created for every received message, and is only valid for the visibility timeout period. When the visibility timeout period expires, the message becomes visible on the queue for consumers. When you receive the message again from the consumer, you receive a new receipt handle. To prevent incorrect or expired receipt handle errors, use the correct receipt handle to delete the message within the Amazon SQS queue visibility timeout period.

For additional information on how to troubleshoot a `ReceiptHandle` error, see [How do I troubleshoot "ReceiptHandleIsInvalid" and "InvalidParameterValue" errors when I use the Amazon SQS DeleteMessage API call?](https://repost.aws/knowledge-center/sqs-receipt-handle-error) in the *AWS Knowledge Center Guide*.