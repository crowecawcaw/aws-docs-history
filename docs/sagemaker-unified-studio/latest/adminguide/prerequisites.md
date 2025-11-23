# Prerequisites

To get started with a new Amazon SageMaker Unified Studio domain, choose an IAM role which will be used to
administer the Amazon SageMaker Unified Studio domain. This is the role you will use to login and setup Amazon SageMaker Unified Studio as
an administrator.

Use the following steps to update the chosen IAM role with the necessary permissions to
setup Amazon SageMaker Unified Studio following these steps to

1. Verify your current role has AWS IAM administrator privileges or ask your AWS IAM
   administrator to perform the next step.
2. Navigate to the IAM console. Choose "Add permission" followed by "Attach policy" and
   search for the managed policy [AWS
   policy: SageMakerStudioAdminIAMConsolePolicy](security-iam-awsmanpol-SageMakerStudioAdminIAMConsolePolicy.md "security-iam-awsmanpol-SageMakerStudioAdminIAMConsolePolicy.md"). Select it
   to add it to your existing role.
   This policy provides initial administrative and individual setup privileges for Amazon SageMaker Unified Studio
   via the AWS Management Console and SDK. It grants permissions for launching Amazon SageMaker Unified Studio. To
   view the permissions for this policy, see [SageMakerStudioAdminIAMConsolePolicy](../../../aws-managed-policy/latest/reference/SageMakerStudioAdminIAMConsolePolicy.md "../../../aws-managed-policy/latest/reference/SageMakerStudioAdminIAMConsolePolicy.md") in the AWS Managed Policy Reference.
