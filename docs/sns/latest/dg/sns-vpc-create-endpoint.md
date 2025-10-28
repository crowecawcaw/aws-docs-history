# Creating an Amazon VPC endpoint for Amazon SNS

To publish messages to your Amazon SNS topics from an Amazon VPC, create an interface VPC endpoint.
Then, you can publish messages to your topics while keeping the traffic within the network that
you manage with the VPC.

Use the following information to create the endpoint and test the connection between your
VPC and Amazon SNS. Or, for a walkthrough that helps you start from scratch, see [Publishing an Amazon SNS message from Amazon VPC](sns-vpc-tutorial.md "sns-vpc-tutorial.md").

## Creating the endpoint

You can create an Amazon SNS endpoint in your VPC using the AWS Management Console, the AWS CLI, an AWS SDK,
the Amazon SNS API, or AWS CloudFormation.

For information about creating and configuring an endpoint using the Amazon VPC console or the
AWS CLI, see [Creating
an Interface Endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint") in the _Amazon VPC User Guide_.

###### Important

You can use Amazon Virtual Private Cloud only with HTTPS Amazon SNS endpoints.

When you create an endpoint, specify Amazon SNS as the service that you want your VPC to
connect to. In the Amazon VPC console, service names vary based on the region. For example, if
you choose US East (N. Virginia), the service name is
**com.amazonaws.us-east-1.sns**.

When you configure Amazon SNS to send messages from Amazon VPC, you must enable private DNS and
specify endpoints in the format
`sns.`us-east-2`.amazonaws.com`.

Private DNS doesn't support legacy endpoints such as `queue.amazonaws.com` or
``us-east-2`.queue.amazonaws.com`.

For information about creating and configuring an endpoint using AWS CloudFormation, see the [`AWS::EC2::VPCEndpoint`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.md") resource in the
_AWS CloudFormation User Guide_.

## Testing the connection between your VPC and Amazon SNS

After you create an endpoint for Amazon SNS, you can publish messages from your VPC to your
Amazon SNS topics. To test this connection, do the following:

1. Connect to an Amazon EC2 instance that resides in your VPC. For information about
   connecting, see [Connect to Your Linux
   Instance](../../../AWSEC2/latest/DeveloperGuide/AccessingInstances.md "../../../AWSEC2/latest/DeveloperGuide/AccessingInstances.md") or [Connecting to Your Windows Instance](../../../AWSEC2/latest/WindowsGuide/connecting_to_windows_instance.md "../../../AWSEC2/latest/WindowsGuide/connecting_to_windows_instance.md") in the Amazon EC2 documentation.

For example, to connect to a Linux instance using an SSH client, run the following
command from a terminal:

```
`$` ssh -i `ec2-key-pair.pem` ec2-user@`instance-hostname`
```

Where:

    * *ec2-key-pair.pem* is the file that contains the
     key pair that Amazon EC2 provided when you created the instance.
    * *instance-hostname* is the public hostname of the
     instance. To get the hostname in the [Amazon EC2
     console](https://console.aws.amazon.com/ec2 "https://console.aws.amazon.com/ec2"): Choose **Instances**, choose your instance, and
     find the value for **Public DNS**.

2. From your instance, use the Amazon SNS [`publish`](../../../cli/latest/reference/sns/publish.md "../../../cli/latest/reference/sns/publish.md") command with the AWS CLI. You can send a simple message to
   a topic with the following command:

```
`$` aws sns publish --region `aws-region` --topic-arn `sns-topic-arn` --message "Hello"
```

Where:

    * *aws-region* is the AWS Region that the topic
     is located in.
    * *sns-topic-arn* is the Amazon Resource Name (ARN)
     of the topic. To get the ARN from the [Amazon SNS
     console](https://console.aws.amazon.com/sns/home "https://console.aws.amazon.com/sns/home"): Choose **Topics**, find your topic, and find the
     value in the **ARN** column.

If the message is successfully received by Amazon SNS, the terminal prints a message ID,
like the following:

```
{
   "MessageId": "6c96dfff-0fdf-5b37-88d7-8cba910a8b64"
}
```
