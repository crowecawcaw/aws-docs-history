# Creating data protection

policies in Amazon SNS using the console

The number and size of Amazon SNS resources in an AWS account are limited. For more
information, see [Amazon Simple Notification Service
endpoints and quotas](../../../general/latest/gr/sns.md "../../../general/latest/gr/sns.md").

###### To create a data protection policy together with an Amazon SNS topic (Console)

Use this option to create a new data protection policy together with a standard Amazon SNS
topic.

1.  Sign in to the [Amazon SNS console](https://console.aws.amazon.com/sns/home "https://console.aws.amazon.com/sns/home").
2.  Choose a topic or create a new one. For more details on creating topics, see [Creating an Amazon SNS topic](sns-create-topic.md "sns-create-topic.md").
3.  On the **Create topic** page, in the **Details**
    section, choose **Standard**.
    1. Enter a **Name** for the topic.
    2. (Optional) Enter a **Display name** for the topic.

4.  Expand **Data protection policy**.
5.  Choose a **Configuration mode**:
    - **Basic** – Define a data protection policy using
      a simple menu.

    - **Advanced** – Define a custom data protection
      policy using JSON.

6.  (Optional) To create your own **custom data
    identifier**, expand the **Custom data identifier configuration
    section** do the following:
    1. Enter a unique **name** for the custom data
       identifier. Custom data identifier names support alphanumeric, underscore
       (\_), and hyphen (-) characters. Up to 128 character are supported. This name
       cannot share the same name as a [managed
       data identifier](sns-message-data-protection-managed-data-identifiers.md "sns-message-data-protection-managed-data-identifiers.md"). For a full list of custom data identifier
       limitations, see [Custom data identifier
       constraints](sns-message-data-protection-custom-data-identifiers.md#custom-data-identifiers-limitations "sns-message-data-protection-custom-data-identifiers.md#custom-data-identifiers-limitations").
    2. Enter a regular expression (RegEx) for the custom data identifier. RegEx
       supports alphanumeric characters, RegEx reserved characters, and symbols.
       RegEx has a maximum length of 200 characters. If the RegEx is too
       complicated, Amazon SNS will fail the API call. For a full list of RegEx
       limitations, see [Custom data identifier
       constraints](sns-message-data-protection-custom-data-identifiers.md#custom-data-identifiers-limitations "sns-message-data-protection-custom-data-identifiers.md#custom-data-identifiers-limitations").
    3. (Optional) Choose **Add custom data identifier** to add
       additional data identifiers as needed. A maximum of 10 custom data
       identifiers are supported for each data protection policy.

7.  Choose the statement(s) that you'd like to add to your data protection policy. You
    can add **audit**, **de-identify** (mask or
    redact), and **deny** (block) statement types to the same data
    protection policy.
    1. **Add audit statement** – Configure which
       sensitive data to audit, what percentage of messages you want to audit for
       that data, and where to send audit logs.

    ###### Note

    Only one audit statement is allowed per data protection policy or
    topic.

        1. Select **data identifiers**  to define the
         sensitive data that you want to audit.
        2. For **Audit sample rate**, enter the percentage
         of messages to audit for sensitive information, up to a maximum of
         99%.
        3. For **Audit destination**, select which
         AWS services to send the audit finding results, and enter a
         destination name for each AWS service that you use. You can select
         from the following Amazon Web Services:




        	* **Amazon CloudWatch** – CloudWatch Logs is the
        	 AWS standard logging solution. Using CloudWatch Logs, you can
        	 perform log analytics using Logs Insights ([see samples here](../../../AmazonCloudWatch/latest/logs/CWL_QuerySyntax-examples.md "../../../AmazonCloudWatch/latest/logs/CWL_QuerySyntax-examples.md")) and create metrics and
        	 alarms. CloudWatch Logs is where many services publish logs, which
        	 makes it easier to aggregate all logs using one solution.
        	 For information about Amazon CloudWatch, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md").
        	* – Firehose satisfies
        	 the demands for real-time streaming to Splunk, OpenSearch,
        	 and Amazon Redshift for further log analytics. For information about
        	 , see the  [User Guide](../../../firehose/latest/dev/what-is-this-service.md "../../../firehose/latest/dev/what-is-this-service.md").
        	* **Amazon Simple Storage Service** – Amazon S3 is an
        	 economical log destination for archival purposes. You may be
        	 required to retain logs for a period of years. In this case,
        	 you can put logs into Amazon S3 to save costs. For information
        	 about Amazon Simple Storage Service, see the [Amazon Simple Storage Service
        	 User Guide](../../../AmazonS3/latest/userguide/Welcome.md "../../../AmazonS3/latest/userguide/Welcome.md").

    2.  **Add a de-identify statement** – Configure the
        sensitive data you want to de-identify in the message, whether you want to
        mask or redact that data, and the accounts to stop delivery of that
        data.
        1. For **Data identifiers**, select the sensitive
           data that you want to de-identify.
        2. For **Define this de-identify statement for**,
           select the AWS accounts or IAM principals to which this
           de-identify statement applies. You can apply it to **all
           AWS accounts**, or to **specific AWS
           accounts** or **IAM entities**
           (account roots, roles, or users) that use account IDs or IAM
           entity ARNs. Separate multiple IDs or ARNs using a comma ( ,
           ).

        The following [IAM
        principals](../../../IAM/latest/UserGuide/reference_identifiers.md "../../../IAM/latest/UserGuide/reference_identifiers.md") are supported:

            * **IAM account principals** – For
             example,`arn:aws:iam::AWS-account-ID:root`.
            * **IAM role principals** – For
             example,
             `arn:aws:iam::AWS-account-ID:role/role-name`.
            * **IAM user principals** – For
             example,
             `arn:aws:iam::AWS-account-ID:user/user-name`.

        3. For **De-identify Option**, select how you want
           to de-identify the sensitive data. The following options are
           supported:
           - **Redact** – Completely removes
             data. For example, email: `classified@amazon.com`
             becomes email: .
           - **Mask** – Replaces the data with
             single characters. For example, email:
             `classified@amazon.com` becomes email:
             `*********************`.

        4. (Optional) Continue to add de-identify statements as
           needed.

    3.  **Add deny statement** – Configure which sensitive
        data to prevent from moving through your topic, and which principals to
        prevent from delivering that data.
        1. For **data direction** , choose the direction of
           the messages for the deny statement:
           - **Inbound messages** – Apply this
             deny statement to messages that are sent to the
             topic.
           - **Outbound messages** – Apply this
             deny statement to messages that the topic delivers to
             subscription endpoints.

        2. Choose the **data identifiers** to define the
           sensitive data that you want to deny.
        3. Choose the **IAM principals** that
           apply to this deny statement. You can apply it to **all AWS accounts**, to **specific AWS accounts**, or **IAM entities** (for example, account roots,
           roles, or users) that use account IDs or IAM entity ARNs. Separate
           multiple IDs or ARNs using a comma ( , ). The following [IAM](../../../IAM/latest/UserGuide/reference_identifiers.md "../../../IAM/latest/UserGuide/reference_identifiers.md") principals are supported:
           - **IAM account principals**
             – For example,
             `arn:aws:iam::AWS-account-ID:root`.
           - **IAM role principals**
             – For example,
             `arn:aws:iam::AWS-account-ID:role/role-name`.
           - **IAM user principals**
             – For example,
             `arn:aws:iam::AWS-account-ID:user/user-name`.

        4. (Optional) Continue to add deny statements as needed.
