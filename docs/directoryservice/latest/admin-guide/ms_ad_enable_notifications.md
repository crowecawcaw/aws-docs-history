# Enabling AWS Managed Microsoft AD directory status

notifications with Amazon Simple Notification Service

Using Amazon Simple Notification Service (Amazon SNS), you can receive email or text (SMS) messages when the status of
your directory changes. You get notified if your directory goes from an Active status to an
[Impaired status](ms_ad_directory_status.md "ms_ad_directory_status.md"). You also receive a notification
when the directory returns to an Active status.

## How It Works

Amazon SNS uses "topics" to collect and distribute messages. Each topic has one or more
subscribers who receive the messages that have been published to that topic. Using the steps
below you can add Directory Service as publisher to an Amazon SNS topic. When Directory Service detects a change in your
directory's status, it publishes a message to that topic, which is then sent to the
topic's subscribers.

You can associate multiple directories as publishers to a single topic. You can also add
directory status messages to topics that you've previously created in Amazon SNS. You have detailed
control over who can publish to and subscribe to a topic. For complete information about
Amazon SNS, see [What is Amazon SNS?](../../../sns/latest/dg/welcome.md "../../../sns/latest/dg/welcome.md").

###### Note

Directory status notifications is a Regional feature of AWS Managed Microsoft AD.
If you are using [Multi-Region replication](ms_ad_configure_multi_region_replication.md "ms_ad_configure_multi_region_replication.md"), the
following procedures must be applied separately in each Region. For more information, see
[Global vs Regional features](multi-region-global-region-features.md "multi-region-global-region-features.md").

## Enabling Amazon SNS

The following walks you through how you can enable Amazon SNS for your AWS Managed Microsoft AD:

1. Sign in to the AWS Management Console and open the [Directory Service
   console](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/").
2. On the **Directories** page, choose your directory ID.
3. On the **Directory details** page, do one of the
   following:
   - If you have multiple Regions showing under **Multi-Region
     replication**, select the Region where you want to enable SNS messaging,
     and then choose the **Maintenance** tab. For more
     information, see [Primary vs additional Regions](multi-region-global-primary-additional.md "multi-region-global-primary-additional.md").
   - If you do not have any Regions showing under **Multi-Region
     replication**, choose the **Maintenance**
     tab.

4. In the **Directory monitoring** section, choose
   **Actions**, and then select **Create
   notification**.
5. On the **Create notification** page, select **Choose a
   notification type**, and then choose **Create a new
   notification**. Alternatively, if you already have an existing SNS topic, you
   can choose **Associate existing SNS topic** to send status messages
   from this directory to that topic.

###### Note

If you choose **Create a new notification** but then use the same
topic name for an SNS topic that already exists, Amazon SNS does not create a new topic,
but just adds the new subscription information to the existing topic.

If you choose **Associate existing SNS topic**, you will only be
able to choose an SNS topic that is in the same Region as the directory. 6. Choose the **Recipient type** and enter the
**Recipient** contact information. If you enter a phone number for
SMS, use numbers only. Do not include dashes, spaces, or parentheses. 7. (Optional) Provide a name for your topic and an SNS display name. The display name
is a short name up to 10 characters that is included in all SMS messages from this
topic. When using the SMS option, the display name is required.

###### Note

If you are logged in using an IAM user or role that has only the [DirectoryServiceFullAccess](role_ds_full_access.md "role_ds_full_access.md") managed policy, your topic name must start with
"DirectoryMonitoring". If you would like to further customize your topic name you will need
additional privileges for SNS. 8. Choose **Create**.

If you want to designate additional SNS subscribers, such as an additional email
address, Amazon SQS queues or AWS Lambda, you can do this from the [Amazon SNS console](https://console.aws.amazon.com//sns/v3/home. "https://console.aws.amazon.com//sns/v3/home.").

## Removing directory status messages from an Amazon SNS

topic

The following walks you through how you can remove your AWS Managed Microsoft AD directory status
messages from an Amazon SNS topic:

1. Sign in to the AWS Management Console and open the [Directory Service
   console](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/").
2. On the **Directories** page, choose your directory ID.
3. On the **Directory details** page, do one of the
   following:
   - If you have multiple Regions showing under **Multi-Region
     replication**, select the Region where you want to remove status
     messages, and then choose the **Maintenance** tab. For
     more information, see [Primary vs additional Regions](multi-region-global-primary-additional.md "multi-region-global-primary-additional.md").
   - If you do not have any Regions showing under **Multi-Region
     replication**, choose the **Maintenance**
     tab.

4. In the **Directory monitoring** section, select an SNS topic name
   in the list, choose **Actions**, and then select
   **Remove**.
5. Choose **Remove**.

This removes your directory as a publisher to the selected SNS topic.

## Deleting an Amazon SNS topic

If you want to delete the entire topic, you can do this from the [Amazon SNS console](https://console.aws.amazon.com//sns/v3/home. "https://console.aws.amazon.com//sns/v3/home.").

Before deleting an Amazon SNS topic using the SNS console, you should ensure that a
directory is not sending status messages to that topic.

If you delete an Amazon SNS topic using the SNS console, this change will not immediately
be reflected within the Directory Services console. You would only be notified the next
time a directory publishes a notification to the deleted topic, in which case you would
see an updated status on the directory's **Monitoring** tab indicating
the topic could not be found.

Therefore, to avoid missing important directory status messages, before deleting any
topic that receives messages from Directory Service, associate your directory with a different Amazon SNS
topic.

For more information on how to delete an Amazon SNS topic, see [Deleting an
Amazon SNS topic and subscription](../../../sns/latest/dg/sns-delete-subscription-topic.md "../../../sns/latest/dg/sns-delete-subscription-topic.md").
