# Monitor

your current account

If you choose to monitor applications in your current AWS account, choose which
AWS resources in your account and Region are covered or analyzed and specify one
or two Amazon Simple Notification Service topics that are used to notify you when an insight is created. You
can update these settings later as needed.

###### Enable DevOps Guru to monitor applications in your current AWS account

1.  Open the Amazon DevOps Guru console at [https://console.aws.amazon.com/devops-guru/](https://console.aws.amazon.com/devops-guru/ "https://console.aws.amazon.com/devops-guru/").
2.  Choose **Monitor applications in the current AWS
    account** as the setup type.
3.  In **DevOps Guru analysis coverage**, choose one of the
    following.

        * **Analyze all AWS resources in the current AWS
         account**: DevOps Guru analyzes all AWS resources in your
         account.
        * **Choose AWS resources to analyze later**:
         You
         choose your analysis boundary later.
         For
         more information, see [Determine coverage for
         DevOps Guru](setting-up.md#setting-up-determine-coverage "setting-up.md#setting-up-determine-coverage") and [Updating your AWS analysis coverage in DevOps Guru](update-settings.md#update-coverage "update-settings.md#update-coverage").

    DevOps Guru can analyze any resource that is associated with the AWS account
    it supports. For more
    information about the supported services and resources, see
    [Amazon DevOps Guru pricing](https://aws.amazon.com/devops-guru/pricing/ "https://aws.amazon.com/devops-guru/pricing/").

4.  You can add up to two topics. DevOps Guru uses the topic or topics to notify you
    about important DevOps Guru events, such as the creation of a new insight. If you
    don't specify a topic now, you can add one later by choosing
    **Settings** in the navigation pane.
    1. In **Specify an Amazon SNS topic**, choose a topic to
       use.
    2. To add an Amazon SNS topic, do one of the following.
       - Choose **Generate a new SNS topic using email**. Then, from **Specify the email address**,
         enter the email address you want to receive notifications. To enter in additional email addresses, choose **Add new email**.
       - Choose **Use an existing SNS topic**. Then, from **Choose a topic in
         your AWS account**, choose the topic you want to use.
       - Choose **Use an existing SNS topic ARN to specify an existing topic from another account**. Then, in **Enter an ARN for a topic**,
         enter the topic ARN. The ARN is the topic's Amazon Resource Name. You can specify a topic in a different account. If you use
         a topic in another account, you must add a resource policy to the topic. For more information,
         see [Permissions for Amazon SNS topics](sns-required-permissions.md "sns-required-permissions.md").

5.  Choose **Enable**.
