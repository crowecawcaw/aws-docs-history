# AWS

policy: SageMakerStudioAdminIAMConsolePolicy

This policy provides initial administrative and individual setup privileges for
Amazon SageMaker Unified Studio via the AWS Management Console and SDK. It grants permissions for launching
Amazon SageMaker Unified Studio.

- Amazon DataZone permissions are required to allow principals full access to all
  Amazon DataZone actions.
- AWS Identity and Access Management permissions are required to allow principals to list and get IAM
  roles, get IAM users and pass roles when creating Amazon DataZone resources.
- AWS Systems Manager permissions are required to manage parameters to enable
  Amazon Q.
  To view the permissions for this policy, see [SageMakerStudioAdminIAMConsolePolicy](../../../aws-managed-policy/latest/reference/SageMakerStudioAdminIAMConsolePolicy.md "../../../aws-managed-policy/latest/reference/SageMakerStudioAdminIAMConsolePolicy.md") in the _AWS
  Managed Policy Reference_.
