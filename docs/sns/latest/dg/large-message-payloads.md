# Publishing large messages with Amazon SNS and

Amazon S3

To publish large Amazon SNS messages, you can use the [Amazon SNS Extended
Client Library for Java](https://github.com/awslabs/amazon-sns-java-extended-client-lib/ "https://github.com/awslabs/amazon-sns-java-extended-client-lib/"), or the [Amazon SNS Extended
Client Library for Python](https://github.com/awslabs/amazon-sns-python-extended-client-lib "https://github.com/awslabs/amazon-sns-python-extended-client-lib"). These libraries are useful for messages that are
larger than the current maximum of 256 KB, with a maximum of 2 GB. Both libraries save the
actual payload to an Amazon S3 bucket, and publish the reference of the stored Amazon S3 object to the
Amazon SNS topic. Subscribed Amazon SQS queues can use the [Amazon SQS Extended
Client Library for Java](https://github.com/awslabs/amazon-sqs-java-extended-client-lib "https://github.com/awslabs/amazon-sqs-java-extended-client-lib") to de-reference and retrieve payloads from Amazon S3. Other
endpoints such as Lambda can use the [Payload
Offloading Java Common Library for AWS](https://github.com/awslabs/payload-offloading-java-common-lib-for-aws "https://github.com/awslabs/payload-offloading-java-common-lib-for-aws") to de-reference and retrieve the
payload.

###### Note

The Amazon SNS Extended Client Libraries are compatible with both standard and FIFO
topics.
