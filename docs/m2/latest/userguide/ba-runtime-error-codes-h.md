

**AWS Mainframe Modernization self-managed experience** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization self-managed experience, explore capabilities from vendor-direct offerings and from AWS Transform. Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

**AWS Mainframe Modernization Service (Managed Runtime Environment experience)** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

# AWS Transform for mainframe Runtime Error Codes related to CL Command Programs
<a name="ba-runtime-error-codes-h"></a>

CL Command pgm error codes, prefixed with `BA-H`.


| Key | Severity | Text | Additional details | 
| --- | --- | --- | --- | 
| BA-H0001 | Warning | Invalid value for 'blu4iv.logging.terminalIdMdc': '%s'. Only 'true' or 'false' are supported values. The terminal id is not added to the MDC. Set the property to 'true' or 'false', or remove it to use the default ('false'). | Reported at startup. See blu4iv.logging.terminalIdMdc in [Available properties for the main application](ba-runtime-key-value.md#ba-runtime-key-value-main). | 
| BA-H2010 | Fatal | FILE parameter is required in command RMVM. Provide a valid FILE parameter to the RMVM command. The FILE parameter specifies the file from which the member should be removed. |  | 
| BA-H2011 | Fatal | Unexpected FILE parameter type in command RMVM. Ensure the FILE parameter is provided as a String or RecordAdaptable type. Check the command syntax and parameter types being passed to RMVM. |  | 
| BA-H2020 | Warn | File is not a database file. Lock operation ignored in command. Only database files can be locked. The file is a flatfile or does not exist. Verify the file name and library. |  | 
| BA-H2030 | Error | Unable to parse INCREL relationship value '%s' in command CPYF. This condition is skipped. Valid INCREL relationship values are '\*IF', '\*AND' and '\*OR'. Correct the INCREL clause so each condition begins with one of these. |  | 
| BA-H2040 | Error | Unable to parse INCREL operator value '%s' in command CPYF. This condition is skipped. Valid INCREL relational operators are '\*EQ', '\*NE', '\*GT', '\*LT', '\*GE' and '\*LE'. Correct the INCREL clause to use one of these operators. |  | 
| BA-H3001 | Error | DQ Operations: Data queue '%s' maps onto the SQS queue name '%s', which contains characters other than alphanumerics, hyphen and underscore Review dataqueue.queues.sqs.queue-name-prefix and dataqueue.queues.sqs.name-separator so the mapped name only uses characters SQS accepts. |  | 
| BA-H3002 | Error | DQ Operations: Data queue '%s' maps onto the SQS queue name '%s', which is %s characters long where SQS allows at most %s Shorten dataqueue.queues.sqs.queue-name-prefix or dataqueue.queues.sqs.name-separator. |  | 
| BA-H3003 | Error | DQ Operations: Missing queue name when mapping a data queue name onto an SQS queue name Check the data queue name passed by the program; it must not be blank. |  | 
| BA-H3004 | Error | DQ Operations: Refusing to send an empty entry to data queue '%s' SQS requires a non empty message body, and a zero length entry would be read back as an empty queue. Send at least one byte. |  | 
| BA-H3005 | Error | DQ Operations: Failed to create the SQS queue '%s' backing data queue '%s' Verify IAM permissions for the sqs:CreateQueue action, and check the queue name follows AWS naming conventions. When queues are provisioned externally, set dataqueue.queues.sqs.create-queues-if-missing to false. |  | 
| BA-H3006 | Error | DQ Operations: Failed to send an entry to data queue '%s' Verify IAM permissions for the sqs:SendMessage action and check the entry size is within the SQS limit (256 KB). |  | 
| BA-H3007 | Error | DQ Operations: Failed to receive an entry from data queue '%s' Verify IAM permissions for the sqs:ReceiveMessage action and check the queue exists. |  | 
| BA-H3008 | Error | DQ Operations: Failed to delete an entry received from data queue '%s'; it will be redelivered once its visibility timeout lapses Verify IAM permissions for the sqs:DeleteMessage action. The receipt handle may have expired if the visibility timeout elapsed while the entry was being processed. |  | 
| BA-H3009 | Error | DQ Operations: Failed to clear data queue '%s' Verify IAM permissions for the sqs:ReceiveMessage and sqs:DeleteMessageBatch actions, or for sqs:PurgeQueue when dataqueue.queues.sqs.clear-strategy is purge. |  | 
| BA-H3010 | Error | DQ Operations: Failed to delete data queue '%s' Verify IAM permissions for the sqs:DeleteQueue action. |  | 
| BA-H3011 | Warning | DQ Operations: The SQS client of the data queue backend could not be closed: %s |  | 
| BA-H3012 | Warning | DQ Operations: Clear of data queue '%s' stopped at the %s entry bound; the queue may still hold entries Raise dataqueue.queues.sqs.clear-max-messages if the queue legitimately holds more entries than the bound allows. |  | 
| BA-H3013 | Error | DQ Operations: The SQS queue '%s' backing data queue '%s' was deleted less than a minute ago, and SQS refuses to recreate a queue name for sixty seconds after a delete Leave sixty seconds between deleting a data queue and sending to it again. Reads and clears report the queue as empty in the meantime; only a send fails, because the entry would otherwise be lost. |  | 
| BA-H3014 | Error | DQ Operations: An entry of data queue '%s' is not valid Base64 and cannot be decoded; it has been delivered %s times and will be redelivered until it reaches the %s delivery limit The entry was not written by the SQS data queue backend. Remove it, or raise dataqueue.queues.sqs.poison-message-max-receives to allow more attempts. Until it is removed or discarded it blocks every later entry of this data queue, because all entries of one queue share a message group. |  | 
| BA-H3015 | Warning | DQ Operations: An entry of data queue '%s' was discarded after %s deliveries because its body could never be decoded; later entries of the queue can now be delivered Find out what wrote a non Base64 entry to this queue. Set dataqueue.queues.sqs.poison-message-max-receives to zero if such an entry must never be discarded, accepting that the data queue stays blocked until it is removed by hand. |  | 