# Managing large Amazon SQS messages with Extended

Client Library and Amazon Simple Storage Service

Use the [Amazon SQS
Extended Client Library for Java](https://github.com/awslabs/amazon-sqs-java-extended-client-lib "https://github.com/awslabs/amazon-sqs-java-extended-client-lib") and [Amazon SQS Extended
Client Library for Python](https://github.com/awslabs/amazon-sqs-python-extended-client-lib/ "https://github.com/awslabs/amazon-sqs-python-extended-client-lib/") to send large messages, especially for payloads
between 256 KB and 2 GB. These libraries store the message payload in an Amazon S3 bucket and
send a reference to the stored object in the Amazon SQS queue.

###### Note

The Amazon SQS Extended Client Libraries are compatible with both standard and FIFO
queues.
