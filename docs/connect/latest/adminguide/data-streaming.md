

# Enable data streaming for your Connect Customer instance
<a name="data-streaming"></a>

You can export contact records and agent events from Connect Customer and perform real-time analysis on contacts. Data streaming sends data to Amazon Kinesis.

**To enable data streaming for your instance**

1. Open the Connect Customer console at [https://console.aws.amazon.com/connect/](https://console.aws.amazon.com/connect/).

1. On the instances page, choose the instance alias. The instance alias is also your **instance name**, which appears in your Connect Customer URL. The following image shows the **Connect Customer virtual contact center instances** page, with a box around the instance alias.  
![The Connect Customer virtual contact center instances page, the instance alias.](http://docs.aws.amazon.com/connect/latest/adminguide/images/instance.png)

1. In the navigation pane, choose **Data streaming**.

1. Choose **Enable data streaming**.

1. For **Contact records**, do one of the following:
   + Choose **Kinesis Firehose** and select an existing delivery stream, or choose **Create a new Kinesis firehose** to open the Kinesis Firehose console and create the delivery stream. For more information, see [Creating an Amazon Data Firehose Delivery Stream](https://docs.aws.amazon.com/firehose/latest/dev/basic-create.html).
   + Choose **Kinesis Stream** and select an existing stream, or choose **Create a Kinesis stream** to open the Kinesis console and create the stream. For more information, see [Creating and Managing Streams](https://docs.aws.amazon.com/streams/latest/dev/working-with-streams.html).

1. For **Agent Events**, select an existing Kinesis stream or choose **Create a new Kinesis stream** to open the Kinesis console and create the stream.

1. Choose **Save**.

## Use server-side encryption for the Kinesis stream
<a name="server-side-encryption-data-stream"></a>

Connect Customer supports streaming to Amazon Kinesis Data Streams and Firehose streams that have server-side encryption with a [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-mgmt) enabled. For a general overview of this feature, see [What Is Server-Side Encryption for Kinesis Data Streams?](https://docs.aws.amazon.com/streams/latest/dev/what-is-sse.html)

To stream to Kinesis Data Streams, you need to grant your Connect Customer instance permission to use a customer managed key. For details on the permissions needed for KMS keys, see [Permissions to Use User-Generated KMS Master Keys](https://docs.aws.amazon.com/streams/latest/dev/permissions-user-key-KMS.html). (Connect Customer acts as the Kinesis stream producer that is described in that topic.)

When Connect Customer puts records into your Kinesis Data Streams, it uses the service-linked role of the instance for authorization. This role needs permission to use the KMS key that encrypts the data stream. To assign permissions to the role, perform the following steps to update the [key policy ](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) of that KMS key. 

**Note**  
To avoid missing data, update the permission of the KMS key before using a KMS key with Connect Customer streaming.

### Step 1: Obtain the ARN for the service-linked role of your Connect Customer instance
<a name="step1-sse"></a>

You can use the Connect Customer console or the AWS CLI to obtain the ARN.

**Use the Connect Customer console to obtain the ARN**

1. Open the Connect Customer console at [https://console.aws.amazon.com/connect/](https://console.aws.amazon.com/connect/).

1. On the instances page, choose the instance name, as shown in the following image.   
![The Connect Customer virtual contact center instances page, the instance alias.](http://docs.aws.amazon.com/connect/latest/adminguide/images/instance.png)

1. On the **Account overview** page, in the **Distribution settings** section, the service-linked role is displayed.  
![The account overview page, the service-linked role ARN.](http://docs.aws.amazon.com/connect/latest/adminguide/images/service-linked-role.png)

1. Choose the copy icon to copy the role ARN to your clipboard, and save that ARN. You're going to use it in [Step 2: Construct a policy statement](#step2-sse).

**Use the AWS CLI to obtain the ARN**

1. Run the following command:

    `aws connect describe-instance --instance-id {{your_instance_id}}` 

1. Save the ServiceRole value from the CLI output.

### Step 2: Construct a policy statement
<a name="step2-sse"></a>

Construct a policy statement that gives permission to the ARN of the Connect Customer service-link role to generate data keys. The following code shows a sample policy.

```
{
    "Sid": "Allow use of the key for Connect Customer streaming",
    "Effect": "Allow",
    "Principal": {
        "AWS": "{{the ARN of the Connect Customer service-linked role}}"
    },
    "Action": "kms:GenerateDataKey",
    "Resource": "*"
 }
```

Add this statement to the KMS key policy by using your preferred mechanism, such as the AWS Key Management Service console, the AWS CLI, or the AWS CDK.