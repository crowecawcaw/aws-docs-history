

# Required permissions to configure controls in Security Hub CSPM
<a name="iam-permissions-controls-standards"></a>

To view information about security controls and enable and disable security controls in standards, the AWS Identity and Access Management (IAM) role that you use to access AWS Security Hub CSPM needs permissions to call the following operations of the Security Hub CSPM API.

To get the necessary permissions, you can use [Security Hub CSPM managed policies](https://docs.aws.amazon.com/securityhub/latest/userguide/security-iam-awsmanpol.html). Alternatively, you can update custom IAM policies to include permissions for these actions.
+  **[BatchGetSecurityControls](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchGetSecurityControls.html)** – Returns information about a batch of security controls for the current account and AWS Region. 
+  **[ListSecurityControlDefinitions](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ListSecurityControlDefinitions.html)** – Returns information about security controls that apply to a specified standard. 
+  **[ListStandardsControlAssociations](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ListStandardsControlAssociations.html)** – Identifies whether a security control is currently enabled in or disabled from each enabled standard in the account. 
+  **[BatchGetStandardsControlAssociations](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchGetStandardsControlAssociations.html)** – For a batch of security controls, identifies whether each control is currently enabled in or disabled from a specified standard. 
+  **[BatchUpdateStandardsControlAssociations](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateStandardsControlAssociations.html)** – Used to enable a security control in standards that include the control, or to disable a control in standards. This is a batch substitute for the existing [`UpdateStandardsControl`](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UpdateStandardsControl.html) operation. 
+  **[BatchUpdateStandardsControlAssociations](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateStandardsControlAssociations.html)** – Used to enable or disable a batch of security controls in standards that include the controls. This is a batch substitute for the existing [`UpdateStandardsControl`](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UpdateStandardsControl.html) operation. 
+  **[UpdateStandardsControl](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UpdateStandardsControl.html)** – Used to enable or disable a single security control in standards that include the control 
+  **[DescribeStandardsControl](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DescribeStandardsControls.html)** – Returns details about specified security controls.

In addition to the preceding APIs, you should add permission to call `BatchGetControlEvaluations` to your IAM role. This permission is necessary to view the enablement and compliance status of a control, the findings count for a control, and the overall security score for controls on the Security Hub CSPM console. Because only the console calls `BatchGetControlEvaluations`, this permission doesn't directly correspond to publicly documented Security Hub CSPM APIs or AWS CLI commands.