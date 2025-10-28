# Setting-up a Amazon Data Firehose delivery stream for

Amazon SNS message archiving

This topic explains how to create the Amazon Data Firehose delivery stream for the [message archiving and analytics example use
case](firehose-example-use-case.md "firehose-example-use-case.md").

###### To create the Amazon Data Firehose delivery stream

1.  Open the [Amazon Data Firehose services
    console](https://console.aws.amazon.com/kinesis/home "https://console.aws.amazon.com/kinesis/home").
2.  Choose **Firehose** and then choose **Create delivery
    stream**.
3.  On the **New delivery stream** page, for **Delivery stream
    name**, enter `ticketUploadStream`, and then choose
    **Next**.
4.  On the **Process records** page, choose
    **Next**.
5.  On the **Choose a destination** page, do the following:
    1. For **Destination**, choose **Amazon S3**.
    2. Under **S3 destination**, for **S3 bucket**,
       choose the S3 bucket that you [created
       initially](firehose-example-initial-resources.md "firehose-example-initial-resources.md").
    3. Choose **Next**.

6.  On the **Configure settings** page, for **S3 buffer
    conditions**, do the following:

        * For **Buffer size**, enter `1`.
        * For **Buffer interval**, enter `60`.

    Using these values for the Amazon S3 buffer lets you quickly test the configuration. The
    first condition that is satisfied triggers data delivery to the S3 bucket.

7.  On the **Configure settings** page, for
    **Permissions**, choose to create an AWS Identity and Access Management (IAM) role with the
    required permissions assigned automatically. Then choose **Next**.
8.  On the **Review** page, choose **Create delivery
    stream**.
9.  From the **Amazon Data Firehose delivery streams page,** choose the
    delivery stream you just created (**ticketUploadStream**). On the
    **Details** tab, note the stream's Amazon Resource Name (ARN) for
    later.
    For more information on creating delivery streams, see [Creating an Amazon Data Firehose Delivery Stream](../../../firehose/latest/dev/basic-create.md "../../../firehose/latest/dev/basic-create.md") in the
    _Amazon Data Firehose Developer Guide_. For more information on creating IAM roles, see [Creating a role to delegate permissions
    to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the _IAM User Guide_.

You've created the Firehose delivery stream with the required permissions. To continue, see
[Subscribing the Firehose
delivery stream to the Amazon SNS topic](firehose-example-subscribe-delivery-stream-to-topic.md "firehose-example-subscribe-delivery-stream-to-topic.md").
