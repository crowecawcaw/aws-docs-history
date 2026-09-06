

# Audit guide
<a name="audit-tutorial"></a>

This tutorial provides instructions on how to configure a recurring audit, setting up alarms, reviewing audit results and mitigating audit issues.

**Topics**
+ [Prerequisites](#audit-tutorial-prerequisites)
+ [Enable audit checks](#audit-tutorial-enable-checks)
+ [View audit results](#audit-tutorial-view-audit)
+ [Creating audit mitigation actions](#audit-tutorial-mitigation)
+ [Apply mitigation actions to your audit findings](#apply-mitigation-actions)
+ [Creating an AWS IoT Device Defender Audit IAM role (optional)](#audit-iam)
+ [Enable SNS notifications (optional)](#audit-tutorial-enable-sns)
+ [Configure permissions for customer managed keys (optional)](#audit-tutorial-cmk-permissions)
+ [Enable logging (optional)](#enable-logging)

## Prerequisites
<a name="audit-tutorial-prerequisites"></a>

To complete this tutorial, you need the following:
+ An AWS account. If you don't have this, see [Setting up](https://docs.aws.amazon.com/iot/latest/developerguide/dd-setting-up.html).

## Enable audit checks
<a name="audit-tutorial-enable-checks"></a>

In the following procedure, you enable audit checks that look at account and device settings and policies to ensure security measures are in place. In this tutorial we instruct you to enable all audit checks, but you're able to select whichever checks you wish.

Audit pricing is per device count per month (fleet devices connected to AWS IoT). Therefore, adding or removing audit checks would not affect your monthly bill when using this feature.

1. Open the [AWS IoT console](https://console.aws.amazon.com/iot). In the navigation pane, expand **Security** and choose **Intro**.

1. Choose **Automate AWS IoT security audit**. Audit checks are automatically turned on.

1. Expand **Audit** and choose **Settings** to view your audit checks. Select an audit check name to learn about what the audit check does. For more information about audit checks, see [Audit Checks](https://docs.aws.amazon.com/iot/latest/developerguide/device-defender-audit-checks.html).

1. (Optional) If you already have a role that you want to use, choose **Manage service permissions**, choose the role from the list, and then choose **Update**.

## View audit results
<a name="audit-tutorial-view-audit"></a>

The following procedure shows you how to view your audit results. In this tutorial, you see the audit results from the audit checks set up in [Enable audit checks](#audit-tutorial-enable-checks) tutorial.

**To view audit results**

1. Open the [AWS IoT console](https://console.aws.amazon.com/iot). In the navigation pane, expand **Security**, **Audit**, and then choose **Results**.

1. Select the **Name** of the audit schedule you'd like to investigate.

1. In **Non-compliant checks**, under **Mitigation**, select the info buttons for information about why it's non-compliant. For guidance on how to make your non-compliant checks compliant, see [Audit checks](device-defender-audit-checks.md).

## Creating audit mitigation actions
<a name="audit-tutorial-mitigation"></a>

In the following procedure, you will create an AWS IoT Device Defender Audit Mitigation Action to enable AWS IoT logging. Each audit check has mapped mitigation actions that will affect which **Action type** you choose for the audit check you want to fix. For more information, see [Mitigation actions](https://docs.aws.amazon.com/iot/latest/developerguide/device-defender-mitigation-actions.html#defender-audit-apply-mitigation-actions.html).

**To use the AWS IoT console to create mitigation actions**

1. Open the [AWS IoT console](https://console.aws.amazon.com/iot). In the navigation pane, expand **Security**, **Detect**, and then choose **Mitigation actions**.

1. On the **Mitigation actions** page, choose **Create**.

1. On the **Create a new mitigation action** page, for **Action name**, enter a unique name for your mitigation action such as {{EnableErrorLoggingAction}}.

1. For **Action type**, choose **Enable AWS IoT logging**.

1. In **Permissions**, choose **Create role**. For **Role name**, use {{IoTMitigationActionErrorLoggingRole}}. Then, choose **Create**.

1. In **Parameters**, under **Role for logging**, choose `IoTMitigationActionErrorLoggingRole`. For **Log level**, choose `Error`.

1. Choose **Create**.

## Apply mitigation actions to your audit findings
<a name="apply-mitigation-actions"></a>

The following procedure shows you how to apply mitigation actions to your audit results.

**To mitigate non-compliant audit findings**

1. Open the [AWS IoT console](https://console.aws.amazon.com/iot). In the navigation pane, expand **Security**, **Audit**, and then choose **Results**.

1. Choose an audit result that you want to respond to.

1. Check your results.

1. Choose **Start mitigation actions**.

1. For **Logging disabled**, choose the mitigation action that you previously created, `EnableErrorLoggingAction`. You can select the appropriate actions for each non-compliant finding to address the issues.

1. For **Select reason codes**, choose the reason code that was returned by the audit check.

1. Choose **Start task**. The mitigation action may take a few minutes to run.

**To check that the mitigation action worked**

1. In the AWS IoT console, in the navigation pane, choose **Settings**.

1. In **Service log**, confirm that the **Log level** is `Error (least verbosity)`.

## Creating an AWS IoT Device Defender Audit IAM role (optional)
<a name="audit-iam"></a>

In the following procedure, you create an AWS IoT Device Defender Audit IAM role that provides AWS IoT Device Defender read access to AWS IoT.

**To create the service role for AWS IoT Device Defender (IAM console)**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane of the IAM console, choose **Roles**, and then choose **Create role**.

1. Choose the **AWS service** role type.

1. In **Use cases for other AWS services**, choose **AWS IoT**, and then choose **IoT - Device Defender Audit**.

1. Choose **Next**.

1. (Optional) Set a [permissions boundary](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html). This is an advanced feature that is available for service roles, but not service-linked roles. 

   Expand the **Permissions boundary** section and choose **Use a permissions boundary to control the maximum role permissions**. IAM includes a list of the AWS managed and customer managed policies in your account. Select the policy to use for the permissions boundary or choose **Create policy** to open a new browser tab and create a new policy from scratch. For more information, see [Creating IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html#access_policies_create-start) in the *IAM User Guide*. After you create the policy, close that tab and return to your original tab to select the policy to use for the permissions boundary.

1. Choose **Next**.

1. Enter a role name to help you identify the purpose of this role. Role names must be unique within your AWS account. They are not distinguished by case. For example, you cannot create roles named both **PRODROLE** and **prodrole**. Because various entities might reference the role, you can't edit the name of the role after it has been created.

1. (Optional) For **Description**, enter a description for the new role.

1. Choose **Edit** in the **Step 1: Select trusted entities** or **Step 2: Select permissions** sections to edit the use cases and permissions for the role. 

1. (Optional) Add metadata to the user by attaching tags as key-value pairs. For more information about using tags in IAM, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html) in the *IAM User Guide*.

1. Review the role and then choose **Create role**.

## Enable SNS notifications (optional)
<a name="audit-tutorial-enable-sns"></a>

In the following procedure, you enable Amazon SNS (SNS) notifications to alert you when your audits identify any non-compliant resources. In this tutorial you will set up notifications for the audit checks enabled in the [Enable audit checks](#audit-tutorial-enable-checks) tutorial.

1. If you haven't already, attach a policy that provides access to SNS via the AWS Management Console. You can do this by following the instructions in [Attaching a policy to an IAM user group](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_manage_attach-policy.html) in the *IAM User Guide* and selecting the **AWSIoTDeviceDefenderPublishFindingsToSNSMitigationAction** policy.

1. Open the [AWS IoT console](https://console.aws.amazon.com/iot). In the navigation pane, expand **Security**, **Audit**, and then choose **Settings**.

1. At the bottom of the **Device Defender audit settings** page, choose **Enable SNS alerts**.

1. Choose **Enabled**.

1. For **Topic**, choose **Create new topic**. Name the topic {{IoTDDNotifications}} and choose **Create**. For **Role**, choose the role that you created in [Creating an AWS IoT Device Defender Audit IAM role (optional)](#audit-iam).

1. Choose **Update**.

1. If you'd like to receive email or text in your Ops platforms through Amazon SNS, see [Using Amazon Simple Notification Service for user notifications](https://docs.aws.amazon.com/sns/latest/dg/sns-user-notifications.html).

## Configure permissions for customer managed keys (optional)
<a name="audit-tutorial-cmk-permissions"></a>

**Note**  
This configuration is only required if you have opted in to customer managed keys for AWS IoT Core. For more information about AWS IoT Core encryption at rest, see [Data encryption at rest in AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/encryption-at-rest.html).

If you have enabled customer managed keys (CMK) for AWS IoT Core encryption at rest, the IAM role used by AWS IoT Device Defender Audit requires additional permissions to decrypt data. Without these permissions, audit operations will fail.

The [`AWSIoTDeviceDefenderAudit`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSIoTDeviceDefenderAudit.html) managed policy does not include `kms:Decrypt` permissions by design, following the principle of least privilege. You must manually add these permissions to your audit role when using customer managed keys.

**To add KMS permissions to your AWS IoT Device Defender Audit IAM role**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Roles**, and then search for the role you created in [Creating an AWS IoT Device Defender Audit IAM role (optional)](#audit-iam) or the role you specified when configuring audit settings.

1. Choose the role name to open its details page.

1. In the **Permissions** tab, choose **Add permissions**, and then choose **Create inline policy**.

1. Choose the **JSON** tab and enter the following policy. Replace the example {{us-east-1}} Region, {{111122223333}} account ID, and {{KEY\_ID}} with your AWS KMS key details:

   ```
   {
     "Version": "2012-10-17",		 	 	 
     "Statement": [
       {
         "Effect": "Allow",
         "Action": [
           "kms:Decrypt"
         ],
         "Resource": "arn:aws:kms:{{us-east-1}}:{{111122223333}}:key/{{KEY_ID}}"
       }
     ]
   }
   ```

1. Choose **Next**.

1. For **Policy name**, enter a descriptive name such as **DeviceDefenderAuditKMSDecrypt**.

1. Choose **Create policy**.

## Enable logging (optional)
<a name="enable-logging"></a>

This procedure describes how to enable AWS IoT to log information to CloudWatch Logs. This will allow you to view your audit results. Enabling logging may result in incurred charges.

**To enable logging**

1. Open the [AWS IoT console](https://console.aws.amazon.com/iot). On the navigation pane, choose **Settings**.

1. In **Logs**, choose **Manage logs**.

1. For **Select role**, choose **Create role**. Name the role {{AWSIoTLoggingRole}} and choose **Create**. A policy is automatically attached.

1. For **Log level**, choose **Debug (most verbosity)**.

1. Choose **Update**.