# Set up remote access

Before users can connect their local Visual Studio Code to Studio spaces, the
administrator must configure permissions. This section provides instructions for
administrators on how to set up their Amazon SageMaker AI domain with remote access.

Different connection methods require different IAM permissions. Configure the
appropriate permissions based on how your users will connect. Use the following workflow
along with the permissions aligned with the connection method.

###### Important

Currently remote IDE connections are authenticated using IAM credentials, not
IAM Identity Center. This applies for domains that use the IAM Identity Center [authentication method](onboard-custom.md#onboard-custom-authentication-details "onboard-custom.md#onboard-custom-authentication-details") for your users to access the domain. If you
prefer not to use IAM authentication for remote connections, you can opt-out by
disabling this feature using the `RemoteAccess` conditional key in your
IAM policies. For more information, see [Remote access enforcement](remote-access-remote-setup-abac.md#remote-access-remote-setup-abac-remote-access-enforcement "remote-access-remote-setup-abac.md#remote-access-remote-setup-abac-remote-access-enforcement").

1. Choose one of the following connection method permissions that align with your
   users’ [Connection methods](remote-access.md#remote-access-connection-methods "remote-access.md#remote-access-connection-methods").
2. [Create a custom IAM
   policy](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") based on the connection method permission.

###### Topics

- [Step 1: Configure security
  and permissions](#remote-access-remote-setup-permissions "#remote-access-remote-setup-permissions")
- [Step 2: Enable remote access for
  your space](#remote-access-remote-setup-enable "#remote-access-remote-setup-enable")
- [Advanced access control](remote-access-remote-setup-abac.md "remote-access-remote-setup-abac.md")
- [Set
  up Studio to run with subnets without internet access within a VPC](remote-access-remote-setup-vpc-subnets-without-internet-access.md "remote-access-remote-setup-vpc-subnets-without-internet-access.md")
- [Set up automated Studio
  space filtering when using the AWS Toolkit](remote-access-remote-setup-filter.md "remote-access-remote-setup-filter.md")

## Step 1: Configure security

and permissions

###### Topics

- [Method 1: Deep link permissions](#remote-access-remote-setup-method-1-deep-link-permissions "#remote-access-remote-setup-method-1-deep-link-permissions")
- [Method 2: AWS Toolkit permissions](#remote-access-remote-setup-method-2-aws-toolkit-permissions "#remote-access-remote-setup-method-2-aws-toolkit-permissions")
- [Method 3: SSH terminal permissions](#remote-access-remote-setup-method-3-ssh-terminal-permissions "#remote-access-remote-setup-method-3-ssh-terminal-permissions")

### Method 1: Deep link permissions

For users connecting via deep links from the SageMaker UI, use the following
permission and attach it to your SageMaker AI [space execution role](sagemaker-roles.md#sagemaker-roles-get-execution-role-space "sagemaker-roles.md#sagemaker-roles-get-execution-role-space") or [domain execution role](sagemaker-roles.md#sagemaker-roles-get-execution-role "sagemaker-roles.md#sagemaker-roles-get-execution-role"). If the space execution role is not
configured, the domain execution role is used by default.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "RestrictStartSessionOnSpacesToUserProfile",
            "Effect": "Allow",
            "Action": [
                "sagemaker:StartSession"
            ],
            "Resource": "arn:*:sagemaker:*:*:space/${sagemaker:DomainId}/*",
            "Condition": {
                "ArnLike": {
                    "sagemaker:ResourceTag/sagemaker:user-profile-arn": "arn:aws:sagemaker:*:*:user-profile/${sagemaker:DomainId}/${sagemaker:UserProfileName}"
                }
            }
        }
    ]
}
```

### Method 2: AWS Toolkit permissions

For users connecting through the AWS Toolkit for Visual Studio Code extension, attach the
following policy to one of the following:

- For IAM authentication, attach this policy to the IAM user or
  role
- For IdC authentication, attach this policy to the [Permission sets](../../../singlesignon/latest/userguide/permissionsetsconcept.md "../../../singlesignon/latest/userguide/permissionsetsconcept.md") managed by the IdC

To show only spaces relevant to the authenticated user, see [Filtering
overview](remote-access-remote-setup-filter.md#remote-access-remote-setup-filter-overview "remote-access-remote-setup-filter.md#remote-access-remote-setup-filter-overview").

###### Important

The following policy using `*` as the resource constraint is
only recommended for quick testing purposes. For production environments,
you should scope down these permissions to specific space ARNs to enforce
the principle of least privilege. See [Advanced access control](remote-access-remote-setup-abac.md "remote-access-remote-setup-abac.md") for examples of more
granular permission policies using resource ARNs, tags, and network-based
constraints.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sagemaker:ListSpaces",
                "sagemaker:DescribeSpace",
                "sagemaker:ListApps",
                "sagemaker:DescribeApp",
                "sagemaker:DescribeDomain",
                "sagemaker:UpdateSpace",
                "sagemaker:CreateApp",
                "sagemaker:DeleteApp",
                "sagemaker:AddTags"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AllowStartSessionOnSpaces",
            "Effect": "Allow",
            "Action": "sagemaker:StartSession",
            "Resource": [
                "arn:aws:sagemaker:`us-east-1`:`111122223333`:space/`domain-id`/`space-name-1`",
                "arn:aws:sagemaker:`us-east-1`:`111122223333`:space/`domain-id`/`space-name-2`"
            ]
        }
    ]
}
```

### Method 3: SSH terminal permissions

For SSH terminal connections, the `StartSession` API is called by
the SSH proxy command script below, using the local AWS credentials. See
[Configure the
AWS CLI](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md") for information and instructions on setting up the user's
local AWS credentials. To use these permissions:

1. Attach this policy to the IAM user or role associated with the local
   AWS credentials.
2. If using a named credential profile, modify the proxy command in your
   SSH config:

```
ProxyCommand '/home/user/sagemaker_connect.sh' '%h' `YOUR_CREDENTIAL_PROFILE_NAME`
```

###### Note

The policy needs to be attached to the IAM identity (user/role)
used in your local AWS credentials configuration, not to the
Amazon SageMaker AI domain execution role.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowStartSessionOnSpecificSpaces",
            "Effect": "Allow",
            "Action": "sagemaker:StartSession",
            "Resource": [
                "arn:aws:sagemaker:`us-east-1`:`111122223333`:space/`domain-id`/`space-name-1`",
                "arn:aws:sagemaker:`us-east-1`:`111122223333`:space/`domain-id`/`space-name-2`"
            ]
        }
    ]
}
```

After setup, users can run `ssh my_studio_space_abc` to start up
the space. For more information, see [Method 3: Connect from the terminal via SSH CLI](remote-access-local-ide-setup.md#remote-access-local-ide-setup-local-vs-code-method-3-connect-from-the-terminal-via-ssh-cli "remote-access-local-ide-setup.md#remote-access-local-ide-setup-local-vs-code-method-3-connect-from-the-terminal-via-ssh-cli").

## Step 2: Enable remote access for

your space

After you set up the permissions, you must toggle on **Remote
Access** and start your space in Studio before the user can
connect using their local VS Code. This setup only needs to be done once.

###### Note

If your users are connecting using [Method 2: AWS Toolkit permissions](#remote-access-remote-setup-method-2-aws-toolkit-permissions "#remote-access-remote-setup-method-2-aws-toolkit-permissions"), you do not necessarily need this step. AWS Toolkit for Visual Studio users can enable remote
access from the Toolkit.

###### Activate remote access for your Studio space

1. [Launch Amazon SageMaker Studio](studio-updated-launch.md#studio-updated-launch-console "studio-updated-launch.md#studio-updated-launch-console").
2. Open the Studio UI.
3. Navigate to your space.
4. In the space details, toggle on **Remote Access**.
5. Choose **Run space**.
