# Required permissions to configure

controls in Security Hub CSPM

To view information about security controls and enable and disable security controls in
standards, the AWS Identity and Access Management (IAM) role that you use to access AWS Security Hub CSPM needs permissions to
call the following operations of the Security Hub CSPM API.

To get the necessary permissions, you can use [Security Hub CSPM managed policies](security-iam-awsmanpol.md "security-iam-awsmanpol.md"). Alternatively, you can update custom IAM policies to
include permissions for these actions.

- **[BatchGetSecurityControls](../../1.0/APIReference/API_BatchGetSecurityControls.md "../../1.0/APIReference/API_BatchGetSecurityControls.md")**
  – Returns information about a batch of security controls for the current
  account and AWS Region.
- **[ListSecurityControlDefinitions](../../1.0/APIReference/API_ListSecurityControlDefinitions.md "../../1.0/APIReference/API_ListSecurityControlDefinitions.md")**
  – Returns information about security controls that apply to a specified
  standard.
- **[ListStandardsControlAssociations](../../1.0/APIReference/API_ListStandardsControlAssociations.md "../../1.0/APIReference/API_ListStandardsControlAssociations.md")**
  – Identifies whether a security control is currently enabled in or disabled
  from each enabled standard in the account.
- **[BatchGetStandardsControlAssociations](../../1.0/APIReference/API_BatchGetStandardsControlAssociations.md "../../1.0/APIReference/API_BatchGetStandardsControlAssociations.md")**
  – For a batch of security controls, identifies whether each control is
  currently enabled in or disabled from a specified standard.
- **[BatchUpdateStandardsControlAssociations](../../1.0/APIReference/API_BatchUpdateStandardsControlAssociations.md "../../1.0/APIReference/API_BatchUpdateStandardsControlAssociations.md")**
  – Used to enable a security control in standards that include the control, or
  to disable a control in standards. This is a batch substitute for the existing
  [`UpdateStandardsControl`](../../1.0/APIReference/API_UpdateStandardsControl.md "../../1.0/APIReference/API_UpdateStandardsControl.md") operation.
- **[BatchUpdateStandardsControlAssociations](../../1.0/APIReference/API_BatchUpdateStandardsControlAssociations.md "../../1.0/APIReference/API_BatchUpdateStandardsControlAssociations.md")**
  – Used to enable or disable a batch of security controls in standards that include the controls. This is a batch substitute for the existing
  [`UpdateStandardsControl`](../../1.0/APIReference/API_UpdateStandardsControl.md "../../1.0/APIReference/API_UpdateStandardsControl.md") operation.
- **[UpdateStandardsControl](../../1.0/APIReference/API_UpdateStandardsControl.md "../../1.0/APIReference/API_UpdateStandardsControl.md")**
  – Used to enable or disable a single security control in standards that include the control
- **[DescribeStandardsControl](../../1.0/APIReference/API_DescribeStandardsControls.md "../../1.0/APIReference/API_DescribeStandardsControls.md")**
  – Returns details about specified security controls.
  In addition to the preceding APIs, you should add permission to call `BatchGetControlEvaluations` to your IAM role. This
  permission is necessary to view the enablement and compliance status of a control, the
  findings count for a control, and the overall security score for controls on the Security Hub CSPM
  console. Because only the console calls `BatchGetControlEvaluations`, this permission doesn't
  directly correspond to publicly documented Security Hub CSPM APIs or AWS CLI commands.
