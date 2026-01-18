# Service Quotas Automatic Management

Service Quotas Automatic Management monitors your service quotas usage and notifies you before you run out of your
allocated quotas. You gain better visibility and proactive awareness, enabling you to run
your applications without interruptions.

###### Key features of Automatic Management

**Opt-in options**

Enable Automatic Management using the Service Quotas console, AWS CLI, or API.

**Usage notifications**

Receive notifications when quota usage reaches the following utilization
thresholds:

- 80% utilization
- 95% utilization

**Auto-Adjust**

Automatic Management can make a service quota increase request on your behalf with
Notify and Auto-Adjust mode.

**Notification channels**

Configure notifications through multiple channels:

- AWS Console Mobile Application
- Email
- Slack

**Integration options**

- Subscribe to [Amazon EventBridge
  events](eventbridge-integration.md "eventbridge-integration.md") for automation workflows
- View notifications in the [AWS Health](../../../health/latest/ug/what-is-aws-health.md "../../../health/latest/ug/what-is-aws-health.md")
  dashboard

###### Topics

- [Service Quotas Automatic Management modes](#automatic-management-modes "#automatic-management-modes")
- [Service Quotas Automatic Management permissions](#permissions "#permissions")
- [Getting started with Service Quotas Automatic Management](getting-started-auto-mgmt.md "getting-started-auto-mgmt.md")
- [Viewing Service Quotas Automatic Management configuration](viewing-automatic-management.md "viewing-automatic-management.md")
- [Updating Service Quotas Automatic Management
  configuration](updating-automatic-management.md "updating-automatic-management.md")
- [Excluding service quotas from Service Quotas Automatic Management](excluding-quotas.md "excluding-quotas.md")
- [Stopping Service Quotas Automatic Management](stopping-automatic-management.md "stopping-automatic-management.md")
- [Service Quotas Automatic Management frequently asked questions](automatic-management-faq.md "automatic-management-faq.md")

## Service Quotas Automatic Management modes

There are two modes with Automatic Management: Notify and Auto-Adjust and Notify Only. Both
modes send you notifications about supported service quotas usage to the [AWS Health dashboard](../../../health/latest/ug/aws-health-dashboard-status.md "../../../health/latest/ug/aws-health-dashboard-status.md").

The following table highlights different features for each mode.

| Mode                   | Creates service quota increase request when service usage exceeds 80% of<br>utilization threshold | Creates service quota increase request when service usage exceeds 95% of<br>utilization threshold | Sends notifications when your service increase request fails | Monitors service quotas usage and sends notifications when approaching<br>80% service utilization threshold | Monitors service quotas usage and sends notifications when approaching<br>95% service utilization thresholds |
| ---------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Notify and Auto Adjust | Yes                                                                                               | Yes                                                                                               | Yes                                                          | No                                                                                                          | Yes                                                                                                          |
| Notify Only            | No                                                                                                | No                                                                                                | No                                                           | Yes                                                                                                         | Yes                                                                                                          |

### How service quota increase requests work with

Notify and Auto-Adjust mode

Automatic Management monitors your service usage and sends these metrics to CloudWatch. When your
usage for [adjustable services quotas](intro.md#intro_getting-started "intro.md#intro_getting-started") are
greater than the [utilization threshold](#notification-thresholds "#notification-thresholds"),
Automatic Management generates a service quota increase for that quota.

#### Auto-adjust vs manual quota increase requests

Auto-adjust requests are processed differently than manual quota increase requests:

Auto-adjust requests

- Use automated processing without creating a support case
- Only work for quotas that support automated approval
- May have more restrictive approval criteria
- Do not provide detailed rejection reasons when not approved

Manual requests

- Go through AWS Support with human review
- Can consider additional context and account-specific factors
- Provide detailed feedback through the support case process
- May be approved even when auto-adjust requests for the same quota are not

###### Important

Auto-adjustable status does not guarantee approval. If an auto-adjust request is not approved, you should submit a manual quota increase request through the Service Quotas console or API.

## Service Quotas Automatic Management permissions

To start Automatic Management, you'll need permissions to view AWS Health notifications and use
the Service Quotas console, AWS CLI, or API actions.

###### Permissions to use Automatic Management

- You should use the following AWS Managed Policies for Automatic Management.
  - [`ServiceQuotasFullAccess`](security-iam-awsmanpol.md#security-iam-awsmanpol-POLICYNAME "security-iam-awsmanpol.md#security-iam-awsmanpol-POLICYNAME")
  - [`AWSHealthFullAccess`](../../../health/latest/ug/security-iam-awsmanpol.md#security-iam-awsmanpol-AWSHealthFullAccess "../../../health/latest/ug/security-iam-awsmanpol.md#security-iam-awsmanpol-AWSHealthFullAccess")

###### Permissions to view Automatic Management

- [`AWSHealthFullAccess`](../../../health/latest/ug/security-iam-awsmanpol.md#security-iam-awsmanpol-AWSHealthFullAccess "../../../health/latest/ug/security-iam-awsmanpol.md#security-iam-awsmanpol-AWSHealthFullAccess")

For more information on creating IAM policies, see the following links.

- [IAM tutorial: Create
  and attach your first customer managed policy](../../../IAM/latest/UserGuide/tutorial_managed-policies.md "../../../IAM/latest/UserGuide/tutorial_managed-policies.md") in the _AWS Identity and Access Management
  User Guide_
- [Define custom IAM permissions with customer managed policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the
  _AWS Identity and Access Management User Guide_
- [Create IAM
  policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the _AWS Identity and Access Management
  User Guide_
