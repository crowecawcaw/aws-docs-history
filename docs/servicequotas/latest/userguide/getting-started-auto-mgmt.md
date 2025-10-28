# Getting started with Service Quotas Automatic Management

Service Quotas Automatic Management monitors service quotas usage patterns and sends you notifications when your usage
approach your allocated quotas. To allow AWS to monitor quotas in your AWS account, you
need to start the Automatic Management. The following procedures walks through how you can start
Automatic Management with either the AWS Management Console or AWS CLI.

AWS Management Console
Use the following steps to start Automatic Management using the AWS Management Console.

1. Open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/").
2. In the navigation pane, select
   **Automatic Management**.
   1. Alternatively, in the Service Quotas dashboard, under
      **Automatic Management**, select
      **Start**.

   ###### Important

   This starts Automatic Management for all available Service Quotas and only
   sends notifications to the AWS Health Dashboard.

3. Under **Automatic Management Mode**, Select **Notify Only**.
   There are two modes: Notify Only and Notify and Auto-Adjust. Currently, only
   Notify Only is available.

###### Note

Automatic Management monitors all the monitored service quotas and sends
notifications to AWS Health Dashboard. Optionally, you can send notifications to
your preferred channels in the next steps. Otherwise, choose
**Skip to Review and Confirm** to
continue.

    1. (Optional) You can enable **User Notification
     Service** to receive notifications on your
     preferred channel like email, app, or chat channels. Select your
     preferred notification method and then choose
     **Next**.
    2. (Optional) You can select exceptions for service quotas you do not want
     AWS to monitor and notify you about in your AWS account. Select your
     preferred exceptions and then choose
     **Next**.

4. Review your options on the **Review and Confirm**
   page. Make any edits and choose **Submit**.
5. Confirm your selection in the confirmation pop-up box.

AWS CLI
Using Automatic Management with the AWS CLI requires you to provide Service Quotas with the
necessary permission to create a AWS Support case on your behalf. You can provide
this permission by attaching the AWS managed policy [ServiceQuotasFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-POLICYNAME "security-iam-awsmanpol.md#security-iam-awsmanpol-POLICYNAME") to
your IAM principal.

###### Example Start Automatic Management for your account

The following example starts Automatic Management for an AWS account in
Canada (Central) AWS Region. Replace the `italicized
 placeholder text` in the example command with your
information.

```
aws service-quotas start-auto-management \
  --opt-in-level ACCOUNT \
  --opt-in-type NotifyOnly \
  --region `ca-central-1`
```

Automatic Management supports adding your [User Notification
(UNO)](../../../notifications/latest/userguide/what-is-service.md "../../../notifications/latest/userguide/what-is-service.md") to receive notifications in your preferred channels like app,
chat, or email. To add UNO configuration, provide your UNO ARN configuration
with the parameter `--notification-arn`.

###### Example Start Automatic Management with UNO configuration

The following example starts Automatic Management for a UNO ARN in an AWS account
in the Canada (Central) AWS Region. Replace the
`italicized placeholder text` in the example
command with your information.

```
aws service-quotas start-auto-management \
  --opt-in-level ACCOUNT \
  --opt-in-type NotifyOnly \
  --region `ca-central-1` \
  --notification-arn arn:aws:notifications::`111122223333`:configuration/`abc123def456gh789`
```
