# Tutorial: Sending a message to an Amazon SQS

queue from Amazon Virtual Private Cloud

This tutorial shows you how to send messages to an Amazon SQS queue over a secure, private
network. The network includes:

- A VPC containing an Amazon EC2 instance.
- An interface VPC endpoint, which allows the Amazon EC2 instance to connect to Amazon SQS
  without using the public internet.
  Even in a fully private network, you can connect to the Amazon EC2 instance and send messages
  to the Amazon SQS queue. For more information, see [Amazon Virtual Private Cloud endpoints for Amazon SQS](sqs-internetwork-traffic-privacy.md#sqs-vpc-endpoints "sqs-internetwork-traffic-privacy.md#sqs-vpc-endpoints").

###### Important

- You can use Amazon Virtual Private Cloud only with HTTPS Amazon SQS endpoints.
- When you configure Amazon SQS to send messages from Amazon VPC, you must enable private DNS and
  specify endpoints in the format
  `sqs.`us-east-2`.amazonaws.com` or `sqs.`us-east-2`.api.aws` for the dual-stack endpoint.
- Amazon SQS also supports FIPS endpoints through PrivateLink using the `com.amazonaws.region.sqs-fips` endpoint service. You can connect to FIPS endpoints in the format `sqs-fips.region.amazonaws.com`.
- When using the dual-stack endpoint in Amazon Virtual Private Cloud, requests will be sent using IPv4 and IPv6.
- Private DNS doesn't support legacy endpoints such as
  `queue.amazonaws.com` or
  ``us-east-2`.queue.amazonaws.com`.

## Step 1: Create an Amazon EC2 key pair

A _key pair_ lets you connect to an Amazon EC2 instance.
It consists of a public key that encrypts your login information and a private key that
decrypts it.

1. Sign in to the [Amazon EC2
   console](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation menu, under **Network & Security**,
   choose **Key Pairs**.
3. Choose **Create Key Pair**.
4. In the **Create Key Pair** dialog box, for **Key pair
   name**, enter `SQS-VPCE-Tutorial-Key-Pair`, and then
   choose **Create**.
5. Your browser downloads the private key file
   `SQS-VPCE-Tutorial-Key-Pair.pem` automatically.

###### Important

Save this file in a safe place. EC2 does not generate a `.pem`
file for the same key pair a second time. 6. To allow an SSH client to connect to your EC2 instance, set the permissions
for your private key file so that only your user can have read permissions for
it, for example:

```
chmod 400 SQS-VPCE-Tutorial-Key-Pair.pem
```

## Step 2: Create AWS resources

To set up the necessary infrastructure, you must use an CloudFormation _template_, which is a blueprint for creating a _stack_
comprised of AWS resources, such as Amazon EC2 instances and Amazon SQS queues.

The stack for this tutorial includes the following resources:

- A VPC and the associated networking resources, including a subnet, a security
  group, an internet gateway, and a route table
- An Amazon EC2 instance launched into the VPC subnet
- An Amazon SQS queue

1. Download the CloudFormation template named [`SQS-VPCE-Tutorial-CloudFormation.yaml`](https://github.com/aws-samples/amazon-sqs-samples/blob/master/templates/SQS-VPCE-Tutorial-CloudFormation.yaml "https://github.com/aws-samples/amazon-sqs-samples/blob/master/templates/SQS-VPCE-Tutorial-CloudFormation.yaml") from
   GitHub.
2. Sign in to the [CloudFormation
   console](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
3. Choose **Create Stack**.
4. On the **Select Template** page, choose **Upload a
   template to Amazon S3**, select the
   `SQS-VPCE-SQS-Tutorial-CloudFormation.yaml` file, and then choose
   **Next**.
5. On the **Specify Details** page, do the following:
   1. For **Stack name**, enter
      `SQS-VPCE-Tutorial-Stack`.
   2. For **KeyName**, choose
      **SQS-VPCE-Tutorial-Key-Pair**.
   3. Choose **Next**.

6. On the **Options** page, choose
   **Next**.
7. On the **Review** page, in the
   **Capabilities** section, choose **I
   acknowledge that AWS CloudFormation might create IAM resources with custom
   names.**, and then choose **Create**.

CloudFormation begins to create the stack and displays the
**CREATE_IN_PROGRESS** status. When the process is complete, CloudFormation
displays the **CREATE_COMPLETE** status.

## Step 3: Confirm that

your EC2 instance isn't publicly accessible

Your CloudFormation template launches an EC2 instance named
`SQS-VPCE-Tutorial-EC2-Instance` into your VPC. This EC2 instance doesn't
allow outbound traffic and isn't able to send messages to Amazon SQS. To verify this, you
must connect to the instance, try to connect to a public endpoint, and then try to
message Amazon SQS.

1. Sign in to the [Amazon EC2
   console](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation menu, under **Instances**, choose
   **Instances**.
3. Select **SQS-VPCE-Tutorial-EC2Instance**.
4. Copy the hostname under **Public DNS**, for example,
   **ec2-203-0-113-0.us-west-2.compute.amazonaws.com**.
5. From the directory that contains [the key
   pair that you created earlier](#create-ec2-key-pair "#create-ec2-key-pair"), connect to the instance using the
   following command, for example:

```
ssh -i SQS-VPCE-Tutorial-Key-Pair.pem ec2-user@`ec2-203-0-113-0.us-east-2.compute.amazonaws.com`
```

6. Try to connect to any public endpoint, for example:

```
ping amazon.com
```

The connection attempt fails, as expected. 7. Sign in to the [Amazon SQS
console](https://console.aws.amazon.com/sqs/ "https://console.aws.amazon.com/sqs/"). 8. From the list of queues, select the queue created by your CloudFormation template, for
example,
**VPCE-SQS-Tutorial-Stack-CFQueue-1ABCDEFGH2IJK**. 9. On the **Details** table, copy the URL, for example,
**https://sqs.us-east-2.amazonaws.com/123456789012/**. 10. From your EC2 instance, try to publish a message to the queue using the
following command, for example:

```
aws sqs send-message --region `us-east-2` --endpoint-url `https://sqs.us-east-2.amazonaws.com/` --queue-url `https://sqs.us-east-2.amazonaws.com/123456789012/` --message-body "Hello from Amazon SQS."
```

The sending attempt fails, as expected.

###### Important

Later, when you create a VPC endpoint for Amazon SQS, your sending attempt will
succeed.

## Step 4: Create an Amazon VPC endpoint for

Amazon SQS

To connect your VPC to Amazon SQS, you must define an interface VPC endpoint. After you add
the endpoint, you can use the Amazon SQS API from the EC2 instance in your VPC. This allows
you to send messages to a queue within the AWS network without crossing the public
internet.

###### Note

The EC2 instance still doesn't have access to other AWS services and endpoints
on the internet.

1. Sign in to the [Amazon VPC
   console](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the navigation menu, choose **Endpoints**.
3. Choose **Create Endpoint**.
4. On the **Create Endpoint** page, for **Service
   Name**, choose the service name for Amazon SQS.

###### Note

The service names vary based on the current AWS Region. For example, if
you are in US East (Ohio), the service name is
**com.amazonaws.`us-east-2`.sqs**. 5. For **VPC**, choose
**SQS-VPCE-Tutorial-VPC**. 6. For **Subnets**, choose the subnet whose **Subnet
ID** contains **SQS-VPCE-Tutorial-Subnet**. 7. For **Security group**, choose **Select security
groups**, and then choose the security group whose **Group
Name** contains **SQS VPCE Tutorial Security
Group**. 8. Choose **Create endpoint**.

The interface VPC endpoint is created and its ID is displayed, for example,
**vpce-0ab1cdef2ghi3j456k**. 9. Choose **Close**.

The Amazon VPC console opens the **Endpoints** page.

Amazon VPC begins to create the endpoint and displays the **pending**
status. When the process is complete, Amazon VPC displays the **available**
status.

## Step 5: Send a message to your Amazon SQS

queue

Now that your VPC includes an endpoint for Amazon SQS, you can connect to your EC2 instance
and send messages to your queue.

1. Reconnect to your EC2 instance, for example:

```
ssh -i SQS-VPCE-Tutorial-Key-Pair.pem ec2-user@`ec2-203-0-113-0.us-east-2.compute.amazonaws.com`
```

2. Try to publish a message to the queue again using the following command, for
   example:

```
aws sqs send-message --region `us-east-2` --endpoint-url `https://sqs.us-east-2.amazonaws.com/` --queue-url `https://sqs.us-east-2.amazonaws.com/123456789012/` --message-body "Hello from Amazon SQS."
```

The sending attempt succeeds and the MD5 digest of the message body and the
message ID are displayed, for example:

```
{
	"MD5OfMessageBody": "a1bcd2ef3g45hi678j90klmn12p34qr5",
	"MessageId": "12345a67-8901-2345-bc67-d890123e45fg"
}
```

For information about receiving and deleting the message from the queue created by
your CloudFormation template (for example,
**VPCE-SQS-Tutorial-Stack-CFQueue-1ABCDEFGH2IJK**), see [Receiving and deleting a message in Amazon SQS](step-receive-delete-message.md "step-receive-delete-message.md") .

For information about deleting your resources, see the following:

- [Deleting a VPC
  Endpoint](../../../vpc/latest/userguide/delete-vpc-endpoint.md "../../../vpc/latest/userguide/delete-vpc-endpoint.md") in the _Amazon VPC User Guide_
- [Deleting an Amazon SQS queue](step-delete-queue.md "step-delete-queue.md")
- [Terminate Your
  Instance](../../../AWSEC2/latest/UserGuide/terminating-instances.md "../../../AWSEC2/latest/UserGuide/terminating-instances.md") in the _Amazon EC2 User Guide_
- [Deleting Your VPC](../../../vpc/latest/userguide/delete-vpc.md "../../../vpc/latest/userguide/delete-vpc.md") in the
  _Amazon VPC User Guide_
- [Deleting a Stack on
  the CloudFormation Console](../../../AWSCloudFormation/latest/UserGuide/cfn-console-delete-stack.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-delete-stack.md") in the
  _AWS CloudFormation User Guide_
- [Deleting Your
  Key Pair](../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md#delete-key-pair "../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md#delete-key-pair") in the _Amazon EC2 User Guide_
