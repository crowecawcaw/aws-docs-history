# Service Quotas Automatic Management

Service Quotas Automatic Management monitors your service quotas usage and notifies you before you run out of your
allocated quotas. You gain better visibility and proactive awareness, enabling you to run
your applications without interruptions.

###### Key features of Automatic Management

**Opt-in options**

Enable Automatic Management using the Service Quotas console, AWS CLI, or API.

**Usage notifications**

Receive notifications when quota usage reaches the following
thresholds:

- 80% utilization
- 95% utilization

**Notification channels**

Configure notifications through multiple channels:

- AWS Console Mobile Application
- Email
- Slack

**Integration options**

- Subscribe to [Amazon EventBridge events](eventbridge-integration.md "eventbridge-integration.md") for automation workflows
- View notifications in the [AWS Health](../../../health/latest/ug/what-is-aws-health.md "../../../health/latest/ug/what-is-aws-health.md")
  personal health dashboard

###### Topics

- [Service Quotas Automatic Management permissions](#permissions "#permissions")
- [Getting started with Service Quotas Automatic Management](getting-started-auto-mgmt.md "getting-started-auto-mgmt.md")
- [Viewing Service Quotas Automatic Management configuration](viewing-automatic-management.md "viewing-automatic-management.md")
- [Updating Service Quotas Automatic Management
  configuration](updating-automatic-management.md "updating-automatic-management.md")
- [Excluding service quotas from Service Quotas Automatic Management](excluding-quotas.md "excluding-quotas.md")
- [Stopping Service Quotas Automatic Management](stopping-automatic-management.md "stopping-automatic-management.md")

## Service Quotas Automatic Management permissions

To start Automatic Management, you'll need permissions to view AWS Health notifications and use
the Service Quotas console, AWS CLI, or API actions.

###### Permissions to use Automatic Management

- You should use the following AWS Managed Policies for Automatic Management.
  - [`ServiceQuotasFullAccess`](security-iam-awsmanpol.md#security-iam-awsmanpol-POLICYNAME "security-iam-awsmanpol.md#security-iam-awsmanpol-POLICYNAME")
  - [`AWSHealthFullAccess`](../../../health/latest/ug/security-iam-awsmanpol.md#security-iam-awsmanpol-AWSHealthFullAccess "../../../health/latest/ug/security-iam-awsmanpol.md#security-iam-awsmanpol-AWSHealthFullAccess")

###### Permissions to view Automatic Management

- [`AWSHealthFullAccess`](../../../health/latest/ug/security-iam-awsmanpol.md#security-iam-awsmanpol-AWSHealthFullAccess "../../../health/latest/ug/security-iam-awsmanpol.md#security-iam-awsmanpol-AWSHealthFullAccess").

For more information on creating IAM policies, see the following links.

- [IAM tutorial: Create
  and attach your first customer managed policy](../../../IAM/latest/UserGuide/tutorial_managed-policies.md "../../../IAM/latest/UserGuide/tutorial_managed-policies.md") in the _AWS Identity and Access Management
  User Guide_
- [Define custom IAM permissions with customer managed policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the
  _AWS Identity and Access Management User Guide_
- [Create IAM
  policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the _AWS Identity and Access Management
  User Guide_
