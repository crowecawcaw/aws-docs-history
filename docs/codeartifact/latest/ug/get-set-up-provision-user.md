# Provision an IAM user

Follow these instructions to prepare an IAM user to use CodeArtifact.

###### To provision anIAM user

1. Create an IAM user, or use one that is associated with your AWS account. For
   more information, see [Creating an
   IAM user](../../../IAM/latest/UserGuide/Using_SettingUpUser.md#Using_CreateUser_console "../../../IAM/latest/UserGuide/Using_SettingUpUser.md#Using_CreateUser_console") and [Overview
   of AWS IAM policies](../../../IAM/latest/UserGuide/PoliciesOverview.md "../../../IAM/latest/UserGuide/PoliciesOverview.md") in the
   _IAM User Guide_.
2. Grant the IAM user access to CodeArtifact.
   - **Option 1:** Create a custom IAM policy. With a custom IAM
     policy, you can provide the minimum required permissions and change how long
     authentication tokens last. For more information and example policies, see
     [Identity-based policy
     examples for AWS CodeArtifact](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").
   - **Option 2:** Use the `AWSCodeArtifactAdminAccess` AWS managed policy.
     The following snippet shows the contents of this policy.

   ###### Important

   This policy grants access to all CodeArtifact APIs. We recommend that you always use the minimum
   permissions required to accomplish your task. For more information, see
   [IAM best
   practices](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Action": [
    "codeartifact:*"
    ],
    "Effect": "Allow",
    "Resource": "*"
    },
    {
    "Effect": "Allow",
    "Action": "sts:GetServiceBearerToken",
    "Resource": "*",
    "Condition": {
    "StringEquals": {
    "sts:AWSServiceName": "codeartifact.amazonaws.com"
    }
    }
    }
    ]
   }`

   ```

###### Note

The `sts:GetServiceBearerToken` permission must be added to the
IAM user or role policy. While it can be added to a CodeArtifact domain or repository resource policy,
the permission will have no effect in resource policies.

The `sts:GetServiceBearerToken` permission is required to call the CodeArtifact
`GetAuthorizationToken` API. This API returns a token that must be used when
using a package manager such as `npm` or `pip` with CodeArtifact. To use a
package manager with a CodeArtifact repository, your IAM user or role must allow
`sts:GetServiceBearerToken` as shown in the preceding policy example.

If you haven't installed the package manager or build tool that you plan to use with
CodeArtifact, see [Install your package manager or
build tool](getting-started-install-package-manager.md "getting-started-install-package-manager.md").
