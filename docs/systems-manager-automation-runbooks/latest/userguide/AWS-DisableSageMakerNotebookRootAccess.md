# `AWS-DisableSageMakerNotebookRootAccess`

**Description**

The `AWS-DisableSageMakerNotebookRootAccess` runbook disables root
access on a Amazon SageMaker AI notebook instance. During the automation, the notebook instance
is stopped to make the required changes. SageMaker AI Studio notebook instances aren't
supported.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-DisableSageMakerNotebookRootAccess "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-DisableSageMakerNotebookRootAccess")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**

- AutomationAssumeRole

Type: String

Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
(IAM) role that allows Systems Manager Automation to perform the actions on your
behalf. If no role is specified, Systems Manager Automation uses the permissions of
the user that starts this runbook.

- NotebookInstanceName

Type: String

Description: (Required) The name of the SageMaker AI notebook instance to disable
root access on.

- StartInstanceAfterUpdate

Type: Boolean

Default: true

Description: (Optional) Determines whether the notebook instance is
started after disabling root access. The default setting for this parameter
is `true`. If set to `true`, the instance is started
after root access is disabled. If set to `false`, the instance is
left in the `stopped` state after root access is disabled.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:StartAutomationExecution`
- `ssm:GetAutomationExecution`
- `sagemaker:DescribeNotebookInstance`
- `sagemaker:StartNotebookInstance`
- `sagemaker:StopNotebookInstance`
- `sagemaker:UpdateNotebookInstance`

**Document Steps**

- CheckNotebookInstanceStatus (aws:executeAwsApi): Checks the current status
  of the notebook instance.
- StopOrUpdateNotebookInstance (aws:branch): Branches based on the status of
  the notebook instance.
- StopNotebookInstance (aws:executeAwsApi): Starts the instance if the
  status is `stopped`.
- WaitForInstanceToStop (aws:waitForAwsResourceProperty): Verifies the
  instance is `stopped`.
- UpdateNotebookInstance (aws:executeAwsApi): Disables root access on the
  notebook instance.
- WaitForNotebookUpdate (aws:waitForAwsResourceProperty): Verifies root
  access has been disabled and the instance has a `stopped`
  status.
- ChooseInstanceStart (aws:branch): Branch based on whether the instance
  should be started.
- StartNotebookInstance (aws:executeAwsApi): Starts the notebook
  instance.
- VerifyNotebookInstanceStatus (aws:waitForAwsResourceProperty): Verifies if
  the instance is `available` before disabling root access.
- VerifyNotebookInstanceRootAccess (aws:assertAwsResourceProperty): Verifies
  the notebook instance root access setting is successfully disabled.
