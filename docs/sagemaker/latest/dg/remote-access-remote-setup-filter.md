# Set up automated Studio

space filtering when using the AWS Toolkit

Users can filter spaces in the AWS Toolkit for Visual Studio Code explorer to display only relevant
spaces. This section provides information on filtering and how to set up automated
filtering.

This setup only applies when using the [Method 2: AWS Toolkit for Visual Studio Code](remote-access-local-ide-setup.md#remote-access-local-ide-setup-local-vs-code-method-2-aws-toolkit-in-vs-code "remote-access-local-ide-setup.md#remote-access-local-ide-setup-local-vs-code-method-2-aws-toolkit-in-vs-code") method to connect from local Visual Studio Codes to Amazon SageMaker Studio spaces. See [Set up remote access](remote-access-remote-setup.md "remote-access-remote-setup.md") for more information.

###### Topics

- [Filtering
  overview](#remote-access-remote-setup-filter-overview "#remote-access-remote-setup-filter-overview")
- [Set
  up when connecting with IAM credentials](#remote-access-remote-setup-filter-set-up-iam-credentials "#remote-access-remote-setup-filter-set-up-iam-credentials")

## Filtering

overview

**Manual filtering** allows users to manually
select which user profiles to display spaces for through the AWS Toolkit
interface. This method works for all authentication types and takes precedence
over automated filtering. To manually filter, see [Manual
filtering](remote-access-local-ide-setup-filter.md#remote-access-local-ide-setup-filter-manual "remote-access-local-ide-setup-filter.md#remote-access-local-ide-setup-filter-manual").

**Automated filtering** automatically shows only
spaces relevant to the authenticated user. This filtering behavior depends on
the authentication method during sign-in. See [connecting to AWS from the Toolkit](../../../toolkit-for-vscode/latest/userguide/connect.md#connect-to-aws "../../../toolkit-for-vscode/latest/userguide/connect.md#connect-to-aws") in the Toolkit for VS Code
User Guide for more information. The following lists the sign-in options.

- **Authenticate and connect with SSO**:
  Automated filtering works by default.
- **Authenticate and connect with IAM
  credentials**: Automated filtering **requires administrator setup** for the following IAM
  credentials. Without this setup, AWS Toolkit cannot identify which
  spaces belong to the user, so all spaces are shown by default.
  - **Using IAM user
    credentials**
  - **Using assumed IAM role session
    credentials**

## Set

up when connecting with IAM credentials

**When using IAM user credentials**

Toolkit for VS Code can match spaces belonging to user profiles that start
with the authenticated IAM user name or assumed role session name. To set this
up:

###### Note

Administrators must configure Studio user profile names to follow
this naming convention for automated filtering to work correctly.

- Administrators must ensure Studio user profile names follow the
  naming convention:
  - For IAM users: prefix with
    ``IAM-user-name`-`
  - For assumed roles: prefix with
    ``assumed-role-session-name`-`

- `aws sts get-caller-identity` returns the identity
  information used for matching
- Spaces belonging to the matched user profiles will be automatically
  filtered in the Toolkit for VS Code

**When using assumed IAM role session
credentials** In addition to the setup when using IAM user
credentials above, you will need to ensure session ARNs include user identifiers
as prefixes that match. You can configure trust policies that ensure session
ARNs include user identifiers as prefixes. [Create a trust
policy](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") and attach it to the assumed role used for
authentication.

This setup is not required for direct IAM user credentials or IdC
authentication.

**Set up trust policy for IAM role session credentials
example** Create a trust policy that enforces role sessions to
include the IAM user name. The following is an example policy:

```
{
    "Statement": [
        {
            "Sid": "RoleTrustPolicyRequireUsernameForSessionName",
            "Effect": "Allow",
            "Action": "sts:AssumeRole",
            "Principal": {"AWS": "arn:aws:iam::`ACCOUNT`:root"},
            "Condition": {
                "StringLike": {"sts:RoleSessionName": "${aws:username}"}
            }
        }
    ]
}
```
