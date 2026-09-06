

# Data retrieval APIs for Amazon SQS
<a name="amazonsqs"></a>

Amazon SQS provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="sqs-GetQueueAttributes"></a>[GetQueueAttributes](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_GetQueueAttributes.html) | Get attributes for the specified queue | Read | 
| <a name="sqs-GetQueueUrl"></a>[GetQueueUrl](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_GetQueueUrl.html) | Return the URL of an existing queue | Read | 
| <a name="sqs-ListDeadLetterSourceQueues"></a>[ListDeadLetterSourceQueues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ListDeadLetterSourceQueues.html) | Return a list of your queues that have the RedrivePolicy queue attribute configured with a dead letter queue | Read | 
| <a name="sqs-ListMessageMoveTasks"></a>[ListMessageMoveTasks](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ListMessageMoveTasks.html) | List message move tasks | Read | 
| <a name="sqs-ListQueueTags"></a>[ListQueueTags](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ListQueueTags.html) | List tags added to an SQS queue | Read | 
| <a name="sqs-ListQueues"></a>[ListQueues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ListQueues.html) | Return a list of your queues | Read | 
| <a name="sqs-ReceiveMessage"></a>[ReceiveMessage](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.html) | Retrieve one or more messages, with a maximum limit of 10 messages, from the specified queue | Read | 