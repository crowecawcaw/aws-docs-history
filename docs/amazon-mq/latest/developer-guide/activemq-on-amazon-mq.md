# ActiveMQ tutorials

The following tutorials show how you can create and connect to your ActiveMQ brokers. To use the ActiveMQ Java example code, you must install the
[Java Standard Edition Development Kit](https://www.oracle.com/technetwork/java/javase/downloads/index.html "https://www.oracle.com/technetwork/java/javase/downloads/index.html") and make some
changes to the code

###### Topics

- [Creating and configuring an Amazon MQ network of brokers](amazon-mq-creating-configuring-network-of-brokers.md "amazon-mq-creating-configuring-network-of-brokers.md")
- [Connecting a Java application to your Amazon MQ broker](amazon-mq-connecting-application.md "amazon-mq-connecting-application.md")
- [Integrating ActiveMQ brokers with LDAP](security-authentication-authorization.md "security-authentication-authorization.md")
- [Step 3: (Optional) Connect to an AWS Lambda function](#activemq-connect-to-lambda "#activemq-connect-to-lambda")
- [Creating an ActiveMQ broker user](amazon-mq-listing-managing-users.md "amazon-mq-listing-managing-users.md")
- [Edit an ActiveMQ broker user](edit-existing-user-console.md "edit-existing-user-console.md")
- [Delete an ActiveMQ broker user](delete-existing-user-console.md "delete-existing-user-console.md")
- [Working examples of using Java Message Service (JMS) with ActiveMQ](amazon-mq-working-java-example.md "amazon-mq-working-java-example.md")

## Step 3: (Optional) Connect to an AWS Lambda function

AWS Lambda can connect to and consume messages from your Amazon MQ broker.
When you connect a broker to Lambda, you create an [event source mapping](../../../lambda/latest/dg/invocation-eventsourcemapping.md "../../../lambda/latest/dg/invocation-eventsourcemapping.md")
that reads messages from a queue and invokes the function [synchronously](../../../lambda/latest/dg/invocation-sync.md "../../../lambda/latest/dg/invocation-sync.md"). The event
source mapping you create reads messages from your broker in batches and converts them into a Lambda payload in the form of a JSON object.

###### To connect your broker to a Lambda function

1. Add the following IAM role permissions to your Lambda function [execution role](../../../lambda/latest/dg/lambda-intro-execution-role.md "../../../lambda/latest/dg/lambda-intro-execution-role.md").
   - [mq:DescribeBroker](../api-reference/brokers-broker-id.md#brokers-broker-id-http-methods "../api-reference/brokers-broker-id.md#brokers-broker-id-http-methods")
   - [ec2:CreateNetworkInterface](../../../AWSEC2/latest/APIReference/API_CreateNetworkInterface.md "../../../AWSEC2/latest/APIReference/API_CreateNetworkInterface.md")
   - [ec2:DeleteNetworkInterface](../../../AWSEC2/latest/APIReference/API_DeleteNetworkInterface.md "../../../AWSEC2/latest/APIReference/API_DeleteNetworkInterface.md")
   - [ec2:DescribeNetworkInterfaces](../../../AWSEC2/latest/APIReference/API_DescribeNetworkInterfaces.md "../../../AWSEC2/latest/APIReference/API_DescribeNetworkInterfaces.md")
   - [ec2:DescribeSecurityGroups](../../../AWSEC2/latest/APIReference/API_DescribeSecurityGroups.md "../../../AWSEC2/latest/APIReference/API_DescribeSecurityGroups.md")
   - [ec2:DescribeSubnets](../../../AWSEC2/latest/APIReference/API_DescribeSubnets.md "../../../AWSEC2/latest/APIReference/API_DescribeSubnets.md")
   - [ec2:DescribeVpcs](../../../AWSEC2/latest/APIReference/API_DescribeVpcs.md "../../../AWSEC2/latest/APIReference/API_DescribeVpcs.md")
   - [logs:CreateLogGroup](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.md")
   - [logs:CreateLogStream](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogStream.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogStream.md")
   - [logs:PutLogEvents](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.md")
   - [secretsmanager:GetSecretValue](../../../secretsmanager/latest/apireference/API_GetSecretValue.md "../../../secretsmanager/latest/apireference/API_GetSecretValue.md")

###### Note

Without the necessary IAM permissions, your function will not be able to successfully read records from Amazon MQ resources. 2. (Optional) If you have created a broker without public accessibility, you must do one of the following to allow Lambda to connect to your broker:

    * Configure one NAT gateway per public subnet. For more information, see
     [Internet and service access for VPC-connected functions](../../../lambda/latest/dg/configuration-vpc.md#vpc-internet "../../../lambda/latest/dg/configuration-vpc.md#vpc-internet") in the *AWS Lambda Developer Guide*.
    * Create a connection between your Amazon Virtual Private Cloud (Amazon VPC) and Lambda using a VPC endpoint. Your Amazon VPC must also connect to AWS Security Token Service (AWS STS) and Secrets Manager endpoints.
     For more information, see [Configuring interface VPC endpoints for Lambda](../../../lambda/latest/dg/configuration-vpc-endpoints.md "../../../lambda/latest/dg/configuration-vpc-endpoints.md")
     in the *AWS Lambda Developer Guide*.

3. [Configure your broker as an event source](../../../lambda/latest/dg/with-mq.md#services-mq-eventsourcemapping "../../../lambda/latest/dg/with-mq.md#services-mq-eventsourcemapping") for a Lambda function using the AWS Management Console. You can also use the
   [`create-event-source-mapping`](../../../cli/latest/reference/lambda/create-event-source-mapping.md "../../../cli/latest/reference/lambda/create-event-source-mapping.md") AWS Command Line Interface command.
4. Write some code for your Lambda function to process the messages consumed from your broker. The Lambda payload that
   retrieved by your event source mapping depends on the engine type of the broker. The following is an example of a Lambda payload for an Amazon MQ for ActiveMQ queue.

###### Note

In the example, `testQueue` is the name of the queue.

```
{
  "eventSource": "aws:amq",
  "eventSourceArn": "arn:aws:mq:us-west-2:112556298976:broker:test:b-9bcfa592-423a-4942-879d-eb284b418fc8",
  "messages": {
    [
      {
        "messageID": "ID:b-9bcfa592-423a-4942-879d-eb284b418fc8-1.mq.us-west-2.amazonaws.com-37557-1234520418293-4:1:1:1:1",
        "messageType": "jms/text-message",
        "data": "QUJDOkFBQUE=",
        "connectionId": "myJMSCoID",
        "redelivered": false,
        "destination": {
          "physicalname": "testQueue"
        },
        "timestamp": 1598827811958,
        "brokerInTime": 1598827811958,
        "brokerOutTime": 1598827811959
      },
      {
        "messageID": "ID:b-9bcfa592-423a-4942-879d-eb284b418fc8-1.mq.us-west-2.amazonaws.com-37557-1234520418293-4:1:1:1:1",
        "messageType":"jms/bytes-message",
        "data": "3DTOOW7crj51prgVLQaGQ82S48k=",
        "connectionId": "myJMSCoID1",
        "persistent": false,
        "destination": {
          "physicalname": "testQueue"
        },
        "timestamp": 1598827811958,
        "brokerInTime": 1598827811958,
        "brokerOutTime": 1598827811959
      }
    ]
  }
}
```

For more information about connecting Amazon MQ to Lambda, the options Lambda supports for an Amazon MQ event source, and event source mapping errors, see
[Using Lambda with Amazon MQ](../../../lambda/latest/dg/with-mq.md "../../../lambda/latest/dg/with-mq.md") in the _AWS Lambda Developer Guide_.
