# Subscribe to AWS Windows AMI notifications

Whenever AWS Windows AMIs are released, we send notifications to the subscribers of the
`ec2-windows-ami-update` topic. Whenever released AWS Windows AMIs are made
private, we send notifications to the subscribers of the
`ec2-windows-ami-private` topic. If you no longer want to receive these
notifications, use the following procedure to unsubscribe.

To be notified when new AMIs are released or when previously released AMIs are
made private, subscribe to notifications using Amazon SNS.

###### To subscribe to AWS Windows AMI notifications

1.  Open the Amazon SNS console at
    [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home "https://console.aws.amazon.com/sns/v3/home").
2.  In the navigation bar, change the Region to **US East (N. Virginia)**, if
    necessary. You must use this Region because the Amazon SNS notifications that you are
    subscribing to were created in this Region.
3.  In the navigation pane, choose **Subscriptions**.
4.  Choose **Create subscription**.
5.  For the **Create subscription** dialog box, do the
    following:
    1.  For **Topic ARN**, copy and paste one of the following Amazon Resource
        Names (ARNs):

            * `arn:aws:sns:us-east-1:801119661308:ec2-windows-ami-update`
            * `arn:aws:sns:us-east-1:801119661308:ec2-windows-ami-private`

        For **AWS GovCloud (US) Regions**:

    `arn:aws-us-gov:sns:us-gov-west-1:077303321853:ec2-windows-ami-update` 2. For **Protocol**, choose
    **Email**. 3. For **Endpoint**, enter an email address that you can use to receive the
    notifications. 4. Choose **Create subscription**.

6.  You'll receive a confirmation email with the subject line `AWS
Notification - Subscription Confirmation`. Open the email and
    choose **Confirm subscription** to complete your
    subscription.

###### To unsubscribe from AWS Windows AMI notifications

1. Open the Amazon SNS console at
   [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home "https://console.aws.amazon.com/sns/v3/home").
2. In the navigation bar, change the Region to **US East (N. Virginia)**, if
   necessary. You must use this Region because the Amazon SNS notifications were created in
   this Region.
3. In the navigation pane, choose **Subscriptions**.
4. Select the subscriptions and then choose **Delete**. When
   prompted for confirmation, choose **Delete**.
