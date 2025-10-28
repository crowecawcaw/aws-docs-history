# Subscribing the Firehose

delivery stream to the Amazon SNS topic

This topic explains how to create the following resources for the [message archiving and analytics example use
case](firehose-example-use-case.md "firehose-example-use-case.md"):

- The AWS Identity and Access Management (IAM) role that allows the Amazon SNS subscription to put records on the
  delivery stream.
- The Firehose delivery stream subscription to the Amazon SNS topic.

###### To create the IAM role for the Amazon SNS subscription

1. Open the [Roles page](https://console.aws.amazon.com/iam/home?#/roles "https://console.aws.amazon.com/iam/home?#/roles") of the
   IAM console.
2. Choose **Create role**.
3. For **Select type of trusted entity**, choose **AWS
   service**.
4. For **Choose a use case**, choose **SNS**. Then choose
   **Next: Permissions**.
5. Choose **Next: Tags**.
6. Choose **Next: Review**.
7. On the **Review** page, for **Role name**, enter
   `ticketUploadStreamSubscriptionRole`. Then choose **Create
   role**.
8. When the role is created, choose its name
   (**ticketUploadStreamSubscriptionRole**).
9. On the role's **Summary** page, choose **Add inline
   policy**.
10. On the **Create policy** page, choose the **JSON**
    tab, and then paste the following policy into the box:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "firehose:DescribeDeliveryStream",
 "firehose:ListDeliveryStreams",
 "firehose:ListTagsForDeliveryStream",
 "firehose:PutRecord",
 "firehose:PutRecordBatch"
 ],
 "Resource": [
 "arn:aws:firehose:us-east-1:123456789012:deliverystream/ticketUploadStream"
 ],
 "Effect": "Allow"
 }
 ]
}`

```

In this policy, replace the AWS account number
(`123456789012`) with your own, and change the AWS Region
(`us-east-1`) accordingly. 11. Choose **Review policy**. 12. On the **Review policy** page, for **Name**, enter
`FirehoseSnsPolicy`. Then choose **Create
policy**. 13. On the role's **Summary** page, note the **Role ARN**
for later.
For more information on creating IAM roles, see [Creating a role to delegate permissions
to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the _IAM User Guide_.

###### To subscribe the Firehose delivery stream to the SNS topic

1. Open the [Topics page](https://console.aws.amazon.com/sns/home#/topics "https://console.aws.amazon.com/sns/home#/topics") of the
   Amazon SNS console.
2. On the **Subscriptions**, tab, choose **Create
   subscription**.
3. Under **Details**, for **Protocol**, choose
   .
4. For **Endpoint**, enter the Amazon Resource Name (ARN) of the
   **ticketUploadStream** delivery stream that you created earlier. For
   example, enter
   `arn:aws:firehose:us-east-1:123456789012:deliverystream/ticketUploadStream`.
5. For **Subscription role ARN**, enter the ARN of the
   **ticketUploadStreamSubscriptionRole** IAM role that you created
   earlier. For example, enter
   `arn:aws:iam::123456789012:role/ticketUploadStreamSubscriptionRole`.
6. Select the **Enable raw message delivery** check box.
7. Choose **Create subscription**.
   You've created the IAM role and SNS topic subscription. To continue, see [Testing and querying an Amazon SNS configuration
   for effective data management](firehose-example-test-and-query.md "firehose-example-test-and-query.md").
