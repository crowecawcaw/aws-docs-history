# Cross-account and cross-region Git configurations

If your Amazon SageMaker Unified Studio domain uses Git connections from a different AWS account,
you must configure AWS Resource Access Manager (RAM) sharing and ensure that the
appropriate IAM permissions are in place.

## RAM permission version

Cross-account Git configurations require RAM resource shares with the correct
permission version. If you have existing RAM shares, they don't automatically update
to newer permission versions. You must manually update the RAM share permissions to
include the required CodeConnections actions.

To update your RAM share permissions, complete the following steps:

1. Open the AWS RAM console.
2. Navigate to your resource share for Amazon SageMaker Unified Studio.
3. Update the permission version to include the latest CodeConnections
   actions.

## IAM permissions

AWS managed policies for Amazon SageMaker Unified Studio already include the required permissions
for cross-account Git operations. If you use custom IAM policies, you must add the
following permissions:

- `codeconnections:ListTagsForResource`
- `codeconnections:GetConnection`
- `codeconnections:UseConnection`
- `datazone:StartCompute`
- `datazone:GetCompute`
- `datazone:StopCompute`
- `datazone:StartNotebookSync`

###### Important

If these permissions are missing from your custom policies, Git operations in
cross-account configurations fail silently or return authorization errors. Verify
that all required permissions are included before troubleshooting connection
issues.

## Cross-region support

Cross-region Git connections are supported in IAM Identity Center (IDC) domains.
You can connect to Git repositories hosted in a different AWS Region than your
Amazon SageMaker Unified Studio domain.

###### Note

Self-hosted GitLab and GitHub Enterprise Server instances must be accessible
from the tooling Region configured for your domain. Ensure that your self-hosted
instance network configuration allows connectivity from the Region where your
Amazon SageMaker Unified Studio compute resources run.
