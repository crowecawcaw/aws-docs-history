# Set up an investigation group

To set up CloudWatch investigations in your account for use with an enhanced investigation, you create
an _investigation group_. Creating an investigation group is a
one-time setup task, after it's created it is used to conduct other investigations.
Settings in the investigation group help you centrally manage the common properties of
your investigations, such as the following:

- Who can access the investigations
- Cross-account investigation support to access resources in other accounts
  during the investigation
- Whether investigation data is encrypted with a customer managed AWS Key Management Service
  key.
- How long investigations and their data are retained by default.
  You can have one investigation group per account. Each investigation in your account
  will be part of this investigation group.

To create an investigation group you must be signed in to an IAM principal that has
the either the **AIOpsConsoleAdminPolicy** or the
**AdministratorAccess** IAM policy attached, or to an account
that has similar permissions.

###### Note

To be able to choose the recommended option of creating a new IAM role for CloudWatch investigations
operational investigations, you must be signed in to an IAM principal that has the
`iam:CreateRole`, `iam:AttachRolePolicy`, and
`iam:PutRolePolicy` permissions.

###### Important

CloudWatch investigations uses _cross-Region inference_ to distribute traffic across
different AWS Regions. For more information, see [Cross-Region inference](Investigations-Security.md#cross-region-inference "Investigations-Security.md#cross-region-inference").

###### To create an investigation group in your account

1.  Open the CloudWatch console at
    [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2.  In the left navigation pane, choose **AI Operations**,
    **Configuration**.
3.  Choose **Configure for this account**.
4.  Optionally change the retention period for investigations. For more
    information about what the retention period governs, see [CloudWatch investigations data retention](Investigations-Retention.md "Investigations-Retention.md").
5.  (Optional) To encrypt your investigation data with a customer managed AWS KMS
    key, choose **Customize encryption settings** and follow the
    steps to create or specify a key to use. If you don't specify a customer managed
    key, CloudWatch investigations uses an AWS owned key for encryption. For more information, see
    [Encryption of investigation data](Investigations-Security.md#Investigations-KMS "Investigations-Security.md#Investigations-KMS").
6.  Choose how to give CloudWatch investigations permissions to access resources. To be able to choose
    either of the first two options, you must be signed in to an IAM principal
    that has the `iam:CreateRole`, `iam:AttachRolePolicy`, and
    `iam:PutRolePolicy` permissions.
    1. (Recommended) Select **Auto-create a new role with default
       investigation permissions**. This role will be granted
       permissions using the AWS managed policies for AI Operations.For more
       information, see [User permissions for your CloudWatch investigations group](Investigations-Security.md#Investigations-Security-IAM "Investigations-Security.md#Investigations-Security-IAM") .
    2. Create a new role yourself and then assign the policy templates.
    3. Choose **Assign an existing role** if you already
       have a role with the permissions that you want to use.

    If you choose this option, you must make sure the role includes a
    trust policy that names `aiops.amazonaws.com` as the service
    principal. For more information about using service principals in trust
    policies, see [AWS service principals](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md#principal-services "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md#principal-services").

    We also recommend that you include a `Condition` section
    with the account number, to prevent a confused deputy situation. The
    following example trust policy illustrates both the service principal
    and the `Condition` section.

    JSON

    ```
    `{
     "Version":"2012-10-17",
     "Statement": [
     {
     "Effect": "Allow",
     "Principal": {
     "Service": "aiops.amazonaws.com"
     },
     "Action": "sts:AssumeRole",
     "Condition": {
     "StringEquals": {
     "aws:SourceAccount": "123456789012"
     },
     "ArnLike": {
     "aws:SourceArn": "arn:aws:aiops:us-east-1:123456789012:*"
     }
     }
     }
     ]
    }`

    ```

7.  Choose **Create investigation group**, you can now create an
    investigation from an alarm, metric, or log insight.
    Optionally, you can setup additional recommended configurations to enhance your
    experience.

8.  In the left navigation pane, choose **AI Operations,
    Configuration**.
9.  On the **Optional configuration** tab, choose the
    enhancements you want to add to CloudWatch investigations.
10. In **Configure cross account access** you can set this
    account as a monitoring account that collects data from other source accounts in
    your organization. For more information, see [Cross-account investigations](Investigations-cross-account.md "Investigations-cross-account.md").
11. For **Enhanced integrations**, choose to allow CloudWatch investigations access to
    additional services in your system, to enable it to gather more data and be more
    useful.
    1. In the **Tags for application boundary detection**
       section, enter the existing custom tag keys for custom applications in
       your system. Resource tags help CloudWatch investigations narrow the search space when it is
       unable to discover definite relationships between resources. For
       example, to discover that an Amazon ECS service depends on an Amazon RDS database,
       CloudWatch investigations can discover this relationship using data sources such as X-Ray
       and CloudWatch Application Signals. However, if you haven't deployed these
       features, CloudWatch investigations will attempt to identify possible relationships. Tag
       boundaries can be used to narrow the resources that will be discovered
       by CloudWatch investigations in these cases.

    You don't need to enter tags created by myApplications or CloudFormation,
    because CloudWatch investigations can automatically detect those tags. 2. CloudTrail records events about changes in your system including deployment
    events. These events can often be useful to CloudWatch investigations to create hypotheses
    about root causes of issues in your system. In the **CloudTrail
    for change event detection** section, you can give CloudWatch investigations
    some access to the events logged by AWS CloudTrail by enabling **Allow
    the assistant access to CloudTrail change events through the
    CloudTrail Event history**. For more information, see
    [Working with CloudTrail Event history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md"). 3. The **X-Ray for topology mapping** and
    **Application Signals for health assessment**
    sections point out other AWS services that can help CloudWatch investigations find
    information. If you have deployed them and you have granted the
    **AIOpsAssistantPolicy** IAM policy to CloudWatch investigations, it
    will be able to access X-Ray and Application Signals telemetry.

    For more information about how these services help CloudWatch investigations, see [X-Ray](Investigations-RecommendedServices.md#Investigations-Xray "Investigations-RecommendedServices.md#Investigations-Xray")
    and [CloudWatch Application Signals](Investigations-RecommendedServices.md#Investigations-ApplicationSignals "Investigations-RecommendedServices.md#Investigations-ApplicationSignals"). 4. If you use Amazon EKS, your CloudWatch investigations investigation group can utilize
    information directly from your Amazon EKS cluster once you set up access
    entries. For more information, see [Integration with Amazon EKS](EKS-Integration.md "EKS-Integration.md"). 5. If you use Amazon RDS, enable the Advanced mode of Database Insights on your database
    instances. Database Insights monitors database load and provides detailed
    performance analysis that helps CloudWatch investigations identify database-related issues
    during investigations. When Advanced Database Insights is enabled, CloudWatch investigations can
    automatically generate performance analysis reports that include
    detailed observations, metric anomalies, root cause analysis, and
    recommendations specific to your database workload. For more information
    about Database Insights and how to enable Advanced mode, see [Monitoring Amazon RDS databases with CloudWatch Database
    Insights](../../../AmazonRDS/latest/UserGuide/USER_DatabaseInsights.md "../../../AmazonRDS/latest/UserGuide/USER_DatabaseInsights.md").

12. You can integrate CloudWatch investigations with a _chat
    channel_. This makes it possible to receive notifications about an
    investigation through the chat channel. CloudWatch investigations support chat channels in the
    following applications:

        * Slack
        * Microsoft Teams

    If you want to integrate with a chat channel, we recommend that you complete
    some additional steps before enabling this enhancement in your investigation
    group. For more information, see [Integration with third-party chat
    systems](Investigations-Integrations.md#Investigations-Integrations-Chat "Investigations-Integrations.md#Investigations-Integrations-Chat").

Then, perform the following steps to integrate with a chat channel in chat
applications:

    * In the **Chat client integration** section, choose
     **Select SNS topic**.
    * Select the SNS topic to use for sending notifications about your
     investigations.
