

# `AWSSupportRemediator-DisableSageMakerNotebookInstanceRootAccess`

**Description**

Disables root access for an Amazon SageMaker AI notebook instance.

This runbook stops the notebook instance if it is in `InService` state, disables root access, and restarts the notebook instance to its initial state after the change.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Security Hub CSPM control [Users should not have root access to SageMaker notebook instances](https://docs.aws.amazon.com/securityhub/latest/userguide/sagemaker-controls.html#sagemaker-3).

If root access is already disabled for the SageMaker AI notebook instance, the notebook instance does not exist, or the notebook instance is being deleted, the automation completes successfully without making changes.

**Important considerations**  
You are responsible for reviewing automation actions before they run.
This automation might cause stack drift if the resource is part of an AWS CloudFormation stack. The runbook temporarily stops the notebook instance during the update, which might interrupt active sessions.
Access to `AWSSupportRemediator-*` runbooks requires an active Business Support\+, Enterprise Support, or Unified Operations Support plan. For more information, see [Compare AWS Support Plans](https://aws.amazon.com/premiumsupport/plans/) on the AWS website.

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**
+ AutomationAssumeRole

  Type: String

  Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
+ NotebookInstanceArn

  Type: String

  Description: (Required) The Amazon Resource Name (ARN) of the SageMaker AI notebook instance.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `sagemaker:DescribeNotebookInstance`
+ `sagemaker:StartNotebookInstance`
+ `sagemaker:StopNotebookInstance`
+ `sagemaker:UpdateNotebookInstance`

**Document Steps**

1. **validateNotebookInstance** - Validates that the SageMaker AI notebook instance exists and checks if root access is enabled.

1. **branchOnChangeRequired** - Branches on whether disabling root access is required and the initial notebook instance status.

1. **waitForNoteBookToStart** - Waits for the notebook instance to reach `InService` state when the initial state is `Pending`.

1. **stopNoteBookInstance** - Stops the notebook instance to allow updating root access settings.

1. **waitForNoteBookToStop** - Waits for the notebook instance to reach stopped state before updating.

1. **disableRootAccess** - Disables root access on the notebook instance.

1. **waitForNoteBookToFinishUpdate** - Waits for the notebook instance update to complete.

1. **branchOnNoteBookInitialStatus** - Branches on the initial notebook instance status to determine if the instance should be restarted.

1. **startNoteBookInstance** - Starts the notebook instance to restore it to its initial state.

1. **waitForNoteBookBackToInitialStatus** - Waits for the notebook instance to return to its initial state.

**Outputs**
+ validateNotebookInstance.NotebookInstanceName: The name of the SageMaker AI notebook instance.
+ validateNotebookInstance.InitialRootAccess: The initial setting for root access for the notebook instance.
+ validateNotebookInstance.InitialNotebookInstanceStatus: The initial state of the notebook instance.
+ validateNotebookInstance.ValidationMessage: The reason in case no change is required.
+ validateNotebookInstance.ChangeRequired: Whether a change is required for the request.