# Audit guide

This tutorial provides instructions on how to configure a recurring audit, setting up
alarms, reviewing audit results and mitigating audit issues.

###### Topics

- [Prerequisites](#audit-tutorial-prerequisites "#audit-tutorial-prerequisites")
- [Enable audit checks](#audit-tutorial-enable-checks "#audit-tutorial-enable-checks")
- [View audit results](#audit-tutorial-view-audit "#audit-tutorial-view-audit")
- [Creating audit mitigation actions](#audit-tutorial-mitigation "#audit-tutorial-mitigation")
- [Apply mitigation actions to your audit findings](#apply-mitigation-actions "#apply-mitigation-actions")
- [Creating an AWS IoT Device Defender Audit IAM role (optional)](#audit-iam "#audit-iam")
- [Enable SNS notifications (optional)](#audit-tutorial-enable-sns "#audit-tutorial-enable-sns")
- [Enable logging (optional)](#enable-logging "#enable-logging")

## Prerequisites

To complete this tutorial, you need the following:

- An AWS account. If you don't have this, see [Setting
  up](../../../iot/latest/developerguide/dd-setting-up.md "../../../iot/latest/developerguide/dd-setting-up.md").

## Enable audit checks

In the following procedure, you enable audit checks that look at account and device
settings and policies to ensure security measures are in place. In this tutorial we
instruct you to enable all audit checks, but you're able to select whichever checks you
wish.

Audit pricing is per device count per month (fleet devices connected to AWS IoT).
Therefore, adding or removing audit checks would not affect your monthly bill when using
this feature.

1. Open the [AWS IoT console](https://console.aws.amazon.com/iot "https://console.aws.amazon.com/iot"). In the navigation pane, expand **Security** and choose **Intro**.
2. Choose **Automate AWS IoT security audit**. Audit checks are automatically turned on.
3. Expand **Audit** and choose **Settings** to view your audit checks. Select an audit check name to learn about what the audit check does. For more information about audit
   checks, see [Audit
   Checks](../../../iot/latest/developerguide/device-defender-audit-checks.md "../../../iot/latest/developerguide/device-defender-audit-checks.md").
4. (Optional) If you already have a role that you want to use, choose
   **Manage service permissions**, choose the role from the list, and then choose **Update**.

## View audit results

The following procedure shows you how to view your audit results. In this tutorial,
you see the audit results from the audit checks set up in [Enable audit checks](#audit-tutorial-enable-checks "#audit-tutorial-enable-checks") tutorial.

###### To view audit results

1. Open the [AWS IoT console](https://console.aws.amazon.com/iot "https://console.aws.amazon.com/iot"). In the navigation pane, expand **Security**, **Audit**, and then choose **Results**.
2. Select the **Name** of the audit schedule you'd like to
   investigate.
3. In **Non-compliant checks**, under **Mitigation**, select the info buttons for information about why it's non-compliant. For guidance on how to make your non-compliant checks
   compliant, see [Audit checks](device-defender-audit-checks.md "device-defender-audit-checks.md").

## Creating audit mitigation actions

In the following procedure, you will create an AWS IoT Device Defender Audit Mitigation Action to enable
AWS IoT logging. Each audit check has mapped mitigation actions that will affect which
**Action type** you choose for the audit check you want to fix. For
more information, see [Mitigation actions](../../../iot/latest/developerguide/device-defender-mitigation-actions.md#defender-audit-apply-mitigation-actions.html "../../../iot/latest/developerguide/device-defender-mitigation-actions.md#defender-audit-apply-mitigation-actions.html").

###### To use the AWS IoT console to create mitigation actions

1. Open the [AWS IoT console](https://console.aws.amazon.com/iot "https://console.aws.amazon.com/iot"). In the navigation pane, expand **Security**, **Detect**, and then choose **Mitigation actions**.
2. On the **Mitigation actions** page, choose
   **Create**.
3. On the **Create a new mitigation action** page, for
   **Action name**, enter a unique name for your mitigation
   action such as `EnableErrorLoggingAction`.
4. For **Action type**, choose **Enable AWS IoT
   logging**.
5. In **Permissions**, choose **Create
   role**. For **Role name**, use
   `IoTMitigationActionErrorLoggingRole`. Then, choose
   **Create**.
6. In **Parameters**, under **Role for
   logging**, choose `IoTMitigationActionErrorLoggingRole`. For
   **Log level**, choose `Error`.
7. Choose **Create**.

## Apply mitigation actions to your audit findings

The following procedure shows you how to apply mitigation actions to your audit
results.

###### To mitigate non-compliant audit findings

1. Open the [AWS IoT console](https://console.aws.amazon.com/iot "https://console.aws.amazon.com/iot"). In the navigation pane, expand **Security**, **Audit**, and then choose **Results**.
2. Choose an audit result that you want to respond to.
3. Check your results.
4. Choose **Start mitigation actions**.
5. For **Logging disabled**, choose the mitigation action that you previously created, `EnableErrorLoggingAction`. You can select the appropriate actions for each non-compliant finding to address the issues.
6. For **Select reason codes**, choose the reason code that was returned by the audit check.
7. Choose **Start task**. The mitigation action may take a few minutes to
   run.

###### To check that the mitigation action worked

1. In the AWS IoT console, in the navigation pane, choose
   **Settings**.
2. In **Service log**, confirm that the
   **Log level** is `Error (least verbosity)`.

## Creating an AWS IoT Device Defender Audit IAM role (optional)

In the following procedure, you create an AWS IoT Device Defender Audit IAM role that provides AWS IoT Device Defender
read access to AWS IoT.

###### To create the service role for AWS IoT Device Defender (IAM console)

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane of the IAM console, choose **Roles**, and
   then choose **Create role**.
3. Choose the **AWS service** role type.
4. In **Use cases for other AWS services**, choose **AWS IoT**, and then choose **IoT - Device Defender Audit**.
5. Choose **Next**.
6. (Optional) Set a [permissions
   boundary](../../../IAM/latest/UserGuide/access_policies_boundaries.md "../../../IAM/latest/UserGuide/access_policies_boundaries.md"). This is an advanced feature that is available for service roles, but
   not service-linked roles.

Expand the **Permissions boundary** section and choose
**Use a permissions boundary to control the maximum role permissions**.
IAM includes a list of the AWS managed and customer managed policies in your account.
Select the policy to use for the permissions boundary or choose **Create
policy** to open a new browser tab and create a new policy from scratch. For
more information, see [Creating IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-start "../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-start")
in the _IAM User Guide_. After you create the policy, close that tab and return to your original tab to select the policy to use for the permissions
boundary. 7. Choose **Next**. 8. Enter a role name to help you identify the purpose of
this role. Role names must be unique within your AWS account. They are not distinguished
by case. For example, you cannot create roles named both `PRODROLE`
and `prodrole`. Because various entities might reference the role,
you can't edit the name of the role after it has been created. 9. (Optional) For **Description**, enter a description for the new
role. 10. Choose **Edit** in the **Step 1: Select trusted
entities** or **Step 2: Select permissions** sections to edit
the use cases and permissions for the role. 11. (Optional) Add metadata to the user by attaching tags as key-value pairs. For more
information about using tags in IAM, see [Tagging IAM resources](../../../IAM/latest/UserGuide/id_tags.md "../../../IAM/latest/UserGuide/id_tags.md") in the _IAM User Guide_. 12. Review the role and then choose **Create role**.

## Enable SNS notifications (optional)

In the following procedure, you enable Amazon SNS (SNS)
notifications to alert you when your audits identify any non-compliant resources. In
this tutorial you will set up notifications for the audit checks enabled in the [Enable audit checks](#audit-tutorial-enable-checks "#audit-tutorial-enable-checks") tutorial.

1. If you haven't already, attach a policy that provides access to SNS
   via the AWS Management Console. You can do this by following the instructions in [Attaching a policy to an IAM user group](../../../IAM/latest/UserGuide/id_groups_manage_attach-policy.md "../../../IAM/latest/UserGuide/id_groups_manage_attach-policy.md") in the _IAM User Guide_ and selecting the
   **AWSIoTDeviceDefenderPublishFindingsToSNSMitigationAction** policy.
2. Open the [AWS IoT console](https://console.aws.amazon.com/iot "https://console.aws.amazon.com/iot"). In the navigation pane, expand **Security**, **Audit**, and then choose **Settings**.
3. At the bottom of the **Device Defender audit settings** page, choose **Enable SNS alerts**.
4. Choose **Enabled**.
5. For **Topic**, choose
   **Create new topic**. Name the topic
   `IoTDDNotifications` and choose
   **Create**. For **Role**, choose the
   role that you created in [Creating an AWS IoT Device Defender Audit IAM role (optional)](#audit-iam "#audit-iam").
6. Choose **Update**.
7. If you'd like to receive email or text in your Ops platforms through Amazon SNS, see
   [Using Amazon Simple Notification Service for user notifications](../../../sns/latest/dg/sns-user-notifications.md "../../../sns/latest/dg/sns-user-notifications.md").

## Enable logging (optional)

This procedure describes how to enable AWS IoT to log information to CloudWatch Logs.
This will allow you to view your audit results. Enabling logging may result in incurred
charges.

###### To enable logging

1. Open the [AWS IoT console](https://console.aws.amazon.com/iot "https://console.aws.amazon.com/iot"). On the navigation pane, choose **Settings**.
2. In **Logs**, choose **Manage logs**.
3. For **Select role**, choose **Create role**.
   Name the role `AWSIoTLoggingRole` and choose **Create**. A policy is
   automatically attached.
4. For **Log level**, choose **Debug (most
   verbosity)**.
5. Choose **Update**.
