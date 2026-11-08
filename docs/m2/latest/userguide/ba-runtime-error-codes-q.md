

**AWS Mainframe Modernization self-managed experience** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization self-managed experience, explore capabilities from vendor-direct offerings and from AWS Transform. Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

**AWS Mainframe Modernization Service (Managed Runtime Environment experience)** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

# AWS Transform for mainframe Runtime Error Codes related to Queue
<a name="ba-runtime-error-codes-q"></a>

Queue error codes, prefixed with `BA-Q`.


| Key | Severity | Text | Additional details | 
| --- | --- | --- | --- | 
| BA-Q0001 | Warn | Invalid value for mq.connection.pool.share. Only true is supported to enable sharing of the JMS connection pool. The default behavior is that JMS connection pool share is disabled. Set mq.connection.pool.share: true in your configuration if you want to share the JMS connection pool. Remove the property to keep JMS connection pool share disabled. |  | 
| BA-Q1001 | Error | Failed to create connection pool. Check the pool connection configuration and resource availability, and ensure proper credentials are provided. |  | 
| BA-Q1002 | Error | Error closing factory. Verify that the factory is not in use and that all associated resources have been properly released. |  | 
| BA-Q2001 | Error | Failed to initialize AWS SQS client with credentials Verify AWS credentials configuration. Ensure the credentials file exists at the correct location. |  | 
| BA-Q2002 | Error | Failed to connect to SQS queue manager Check network connectivity to AWS SQS service and verify IAM permissions for sqs:ListQueues action. |  | 
| BA-Q2003 | Error | Failed to create SQS queue '%s' Verify IAM permissions for sqs:CreateQueue action and check queue name follows AWS naming conventions. |  | 
| BA-Q2004 | Error | Failed to send message to SQS queue '%s' Verify IAM permissions for sqs:SendMessage action and check message size is within SQS limits (256 KB). |  | 
| BA-Q2005 | Error | Failed to receive message from SQS queue '%s' Verify IAM permissions for sqs:ReceiveMessage action and check queue exists. |  | 
| BA-Q2006 | Error | Failed to delete message from SQS queue '%s' Verify IAM permissions for sqs:DeleteMessage action. Receipt handle may have expired if message visibility timeout has passed. |  | 
| BA-Q2007 | Error | Failed to delete SQS queue '%s' Verify IAM permissions for sqs:DeleteQueue action. Queue must be empty or you must wait 60 seconds after last message operation. |  | 
| BA-Q2008 | Error | Failed to get queue attributes for SQS queue '%s' Verify IAM permissions for sqs:GetQueueAttributes action and check queue exists. |  | 
| BA-Q2009 | Error | Failed to change message visibility for SQS queue '%s' Verify IAM permissions for sqs:ChangeMessageVisibility action. Receipt handle may have expired. |  | 
| BA-Q2010 | Error | SQS queue '%s' not found. Call openQueue() first Ensure openQueue() is called before attempting queue operations. |  | 
| BA-Q2011 | Error | Failed to cleanup SQS connection Check if SQS client is still in use. Ensure all queue operations are completed before cleanup. |  | 
| BA-Q2012 | Warn | MQ Operations: No message found with correlation ID [%s] in queue [%s]. |  | 
| BA-Q2013 | Warn | MQ Operations: tried to receive a message from queue [%s], but the queue seems empty. |  | 
| BA-Q2014 | Warn | MQ Operations: Error populating message descriptor from SQS message attributes: {} |  | 