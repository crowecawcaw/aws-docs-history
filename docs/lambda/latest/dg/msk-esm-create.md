# Creating a Lambda event source mapping for an Amazon MSK event source

To create an event source mapping, you can use the Lambda console, the [AWS Command Line Interface (CLI)](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md"), or an
[AWS SDK](https://aws.amazon.com/getting-started/tools-sdks/ "https://aws.amazon.com/getting-started/tools-sdks/").

###### Note

When you create the event source mapping, Lambda creates a [hyperplane ENI](configuration-vpc.md#configuration-vpc-enis "configuration-vpc.md#configuration-vpc-enis") in the private subnet that contains your MSK cluster, allowing Lambda to
establish a secure connection. This hyperplane ENI allows uses the subnet and security group
configuration of your MSK cluster, not your Lambda function.

The following console steps add an Amazon MSK cluster as a trigger for your Lambda function. Under the hood,
this creates an event source mapping resource.

###### To add an Amazon MSK trigger to your Lambda function (console)

1. Open the [Function page](https://console.aws.amazon.com/lambda/home#/functions "https://console.aws.amazon.com/lambda/home#/functions")
   of the Lambda console.
2. Choose the name of the Lambda function you want to add an Amazon MSK trigger to.
3. Under **Function overview**, choose **Add trigger**.
4. Under **Trigger configuration**, choose **MSK**.
5. To specify your Kafka cluster details, do the following:
   1. For **MSK cluster**, select your cluster.
   2. For **Topic name**, enter the name of the Kafka topic to consume
      messages from.
   3. For **Consumer group ID**, enter the ID of a Kafka consumer group
      to join, if applicable. For more information, see [Customizable consumer group ID in Lambda](msk-cgid.md "msk-cgid.md").

6. For **Cluster authentication**, make the necessary configurations. For more
   information about cluster authentication, see [Configuring cluster authentication methods in Lambda](msk-cluster-auth.md "msk-cluster-auth.md").
   - Toggle on **Use authentication** if you want Lambda to perform
     authentication with your MSK cluster when establishing a connection. Authentication
     is recommended.
   - If you use authentication, for **Authentication method**, choose
     the authentication method to use.
   - If you use authentication, for **Secrets Manager key**, choose the Secrets Manager key
     that contains the authentication credentials needed to access your cluster.

7. Under **Event poller configuration**, make the necessary configurations.
   - Choose **Activate trigger** to enable the trigger immediately after creation.
   - Choose whether you want to **Configure provisioned mode** for your event source
     mapping. For more information, see [Event poller scaling modes in Lambda](msk-scaling-modes.md "msk-scaling-modes.md").
     - If you configure provisioned mode, enter a value for **Minimum event pollers**,
       a value for **Maximum event pollers**, or both values.

   - For **Starting position**, choose how you want Lambda to start reading from your stream.
     For more information, see [Polling and stream starting positions in Lambda](msk-starting-positions.md "msk-starting-positions.md").

8. Under **Batching**, make the necessary configurations. For more information about
   batching, see [Batching behavior](invocation-eventsourcemapping.md#invocation-eventsourcemapping-batching "invocation-eventsourcemapping.md#invocation-eventsourcemapping-batching").
   1. For **Batch size**, enter the maximum number of messages to receive in
      a single batch.
   2. For **Batch window**, enter the maximum number of seconds that Lambda spends
      gathering records before invoking the function.

9. Under **Filtering**, make the necessary configurations. For more information about
   filtering, see [Using event filtering with an Amazon MSK event source](with-msk-filtering.md "with-msk-filtering.md").
   - For **Filter criteria**, add filter criteria definitions to determine whether
     or not to process an event.

10. Under **Failure handling**, make the necessary configurations. For more information
    about failure handling, see [Capturing discarded batches for an Amazon MSK event source](with-msk-on-failure.md "with-msk-on-failure.md").
    - For **On-failure destination**, specify the ARN of your on-failure destination.

11. For **Tags**, enter the tags to associate with this event source mapping.
12. To create the trigger, choose **Add**.
    You can also create the event source mapping using the AWS CLI with the [create-event-source-mapping](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-event-source-mapping.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-event-source-mapping.html") command. The following example creates an event source mapping to map the Lambda
    function `my-msk-function` to the `AWSKafkaTopic` topic, starting from the `LATEST`
    message. This command also uses the [SourceAccessConfiguration](../api/API_SourceAccessConfiguration.md "../api/API_SourceAccessConfiguration.md") object to instruct
    Lambda to use [SASL/SCRAM](msk-cluster-auth.md#msk-sasl-scram "msk-cluster-auth.md#msk-sasl-scram") authentication when connecting to the cluster.

```
aws lambda create-event-source-mapping \
  --event-source-arn arn:aws:kafka:us-east-1:111122223333:cluster/my-cluster/fc2f5bdf-fd1b-45ad-85dd-15b4a5a6247e-2 \
  --topics AWSKafkaTopic \
  --starting-position LATEST \
  --function-name my-kafka-function
  --source-access-configurations '[{"Type": "SASL_SCRAM_512_AUTH","URI": "arn:aws:secretsmanager:us-east-1:111122223333:secret:my-secret"}]'
```

If the cluster uses [mTLS authentication](msk-cluster-auth.md#msk-mtls "msk-cluster-auth.md#msk-mtls"), include a [SourceAccessConfiguration](../api/API_SourceAccessConfiguration.md "../api/API_SourceAccessConfiguration.md") object that specifies
`CLIENT_CERTIFICATE_TLS_AUTH` and a Secrets Manager key ARN. This is shown in the following command:

```
aws lambda create-event-source-mapping \
  --event-source-arn arn:aws:kafka:us-east-1:111122223333:cluster/my-cluster/fc2f5bdf-fd1b-45ad-85dd-15b4a5a6247e-2 \
  --topics AWSKafkaTopic \
  --starting-position LATEST \
  --function-name my-kafka-function
  --source-access-configurations '[{"Type": "CLIENT_CERTIFICATE_TLS_AUTH","URI": "arn:aws:secretsmanager:us-east-1:111122223333:secret:my-secret"}]'
```

When the cluster uses [IAM authentication](msk-cluster-auth.md#msk-iam-auth "msk-cluster-auth.md#msk-iam-auth"), you don’t need a
[SourceAccessConfiguration](../api/API_SourceAccessConfiguration.md "../api/API_SourceAccessConfiguration.md") object. This is shown in the following command:

```
aws lambda create-event-source-mapping \
  --event-source-arn arn:aws:kafka:us-east-1:111122223333:cluster/my-cluster/fc2f5bdf-fd1b-45ad-85dd-15b4a5a6247e-2 \
  --topics AWSKafkaTopic \
  --starting-position LATEST \
  --function-name my-kafka-function
```
