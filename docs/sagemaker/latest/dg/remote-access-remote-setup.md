

# Set up remote access
<a name="remote-access-remote-setup"></a>

Before users can connect their Remote IDE to Studio spaces, the administrator must configure permissions. This section provides instructions for administrators on how to set up their Amazon SageMaker AI domain with remote access.

Different connection methods require different IAM permissions. Configure the appropriate permissions based on how your users will connect. Use the following workflow along with the permissions aligned with the connection method.

**Important**  
Currently remote IDE connections are authenticated using IAM credentials, not IAM Identity Center. This applies for domains that use the IAM Identity Center [authentication method](https://docs.aws.amazon.com/sagemaker/latest/dg/onboard-custom.html#onboard-custom-authentication-details) for your users to access the domain. If you prefer not to use IAM authentication for remote connections, you can opt-out by disabling this feature using the `RemoteAccess` conditional key in your IAM policies. For more information, see [Remote access enforcement](remote-access-remote-setup-abac.md#remote-access-remote-setup-abac-remote-access-enforcement). When using IAM credentials, Remote IDE connections may maintain active sessions even after you log out of your IAM Identity Center session. Sometimes, these Remote IDE connections can persist for up to 12 hours. To ensure the security of your environment, administrators must review session duration settings where possible and be cautious when using shared workstations or public networks.

1. Choose one of the following connection method permissions that align with your users’ [Connection methods](remote-access.md#remote-access-connection-methods).

1. [Create a custom IAM policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) based on the connection method permission.

**Topics**
+ [Step 1: Configure security and permissions](#remote-access-remote-setup-permissions)
+ [Step 2: Enable remote access for your space](#remote-access-remote-setup-enable)
+ [Advanced access control](remote-access-remote-setup-abac.md)
+ [Set up Studio to run with subnets without internet access within a VPC](remote-access-remote-setup-vpc-subnets-without-internet-access.md)
+ [Set up automated Studio space filtering when using the AWS Toolkit](remote-access-remote-setup-filter.md)

## Step 1: Configure security and permissions
<a name="remote-access-remote-setup-permissions"></a>

**Topics**
+ [Method 1: Deep link permissions](#remote-access-remote-setup-method-1-deep-link-permissions)
+ [Method 2: AWS Toolkit permissions](#remote-access-remote-setup-method-2-aws-toolkit-permissions)
+ [Method 3: SSH terminal permissions](#remote-access-remote-setup-method-3-ssh-terminal-permissions)

**Important**  
Using broad permissions for `sagemaker:StartSession`, especially with a wildcard resource `*` creates the risk that any user with this permission can initiate a session against any SageMaker Space app in the account. This can lead to the impact of data scientists unintentionally accessing other users’ SageMaker Spaces. For production environments, you should scope down these permissions to specific space ARNs to enforce the principle of least privilege. See [Advanced access control](remote-access-remote-setup-abac.md) for examples of more granular permission policies using resource ARNs, tags, and network-based constraints.

### Method 1: Deep link permissions
<a name="remote-access-remote-setup-method-1-deep-link-permissions"></a>

For users connecting via deep links from the SageMaker UI, use the following permission and attach it to your SageMaker AI [space execution role](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html#sagemaker-roles-get-execution-role-space) or [domain execution role](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html#sagemaker-roles-get-execution-role). If the space execution role is not configured, the domain execution role is used by default.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
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

------

### Method 2: AWS Toolkit permissions
<a name="remote-access-remote-setup-method-2-aws-toolkit-permissions"></a>

For users connecting through the AWS Toolkit for Visual Studio Code extension, attach the following policy to one of the following:
+ For IAM authentication, attach this policy to the IAM user or role
+ For IdC authentication, attach this policy to the [Permission sets](https://docs.aws.amazon.com/singlesignon/latest/userguide/permissionsetsconcept.html) managed by the IdC

To show only spaces relevant to the authenticated user, see [Filtering overview](remote-access-remote-setup-filter.md#remote-access-remote-setup-filter-overview).

**Important**  
The following policy using `*` as the resource constraint is only recommended for quick testing purposes. For production environments, you should scope down these permissions to specific space ARNs to enforce the principle of least privilege. See [Advanced access control](remote-access-remote-setup-abac.md) for examples of more granular permission policies using resource ARNs, tags, and network-based constraints.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
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
                "arn:aws:sagemaker:{{us-east-1}}:{{111122223333}}:space/{{domain-id}}/{{space-name-1}}",
                "arn:aws:sagemaker:{{us-east-1}}:{{111122223333}}:space/{{domain-id}}/{{space-name-2}}"
            ]
        }
    ]
}
```

------

### Method 3: SSH terminal permissions
<a name="remote-access-remote-setup-method-3-ssh-terminal-permissions"></a>

For SSH terminal connections, the `StartSession` API is called by the SSH proxy command script below, using the local AWS credentials. See [Configure the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) for information and instructions on setting up the user's local AWS credentials. To use these permissions:

1. Attach this policy to the IAM user or role associated with the local AWS credentials.

1. If using a named credential profile, modify the proxy command in your SSH config:

   ```
   ProxyCommand '/home/user/sagemaker_connect.sh' '%h' {{YOUR_CREDENTIAL_PROFILE_NAME}}
   ```
**Note**  
The policy needs to be attached to the IAM identity (user/role) used in your local AWS credentials configuration, not to the Amazon SageMaker AI domain execution role.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Sid": "AllowStartSessionOnSpecificSpaces",
               "Effect": "Allow",
               "Action": "sagemaker:StartSession",
               "Resource": [
                   "arn:aws:sagemaker:{{us-east-1}}:{{111122223333}}:space/{{domain-id}}/{{space-name-1}}",
                   "arn:aws:sagemaker:{{us-east-1}}:{{111122223333}}:space/{{domain-id}}/{{space-name-2}}"
               ]
           }
       ]
   }
   ```

------

After setup, users can run `ssh my_studio_space_abc` to start up the space. For more information, see [Method 3: Connect from the terminal via SSH CLI](remote-access-local-ide-setup.md#remote-access-local-ide-setup-local-vs-code-method-3-connect-from-the-terminal-via-ssh-cli).

## Step 2: Enable remote access for your space
<a name="remote-access-remote-setup-enable"></a>

After you set up the permissions, you must toggle on **Remote Access** and start your space in Studio before the user can connect using their Remote IDE. This setup only needs to be done once.

**Note**  
If your users are connecting using [Method 2: AWS Toolkit permissions](#remote-access-remote-setup-method-2-aws-toolkit-permissions), you do not necessarily need this step. AWS Toolkit for Visual Studio users can enable remote access from the Toolkit.

**Activate remote access for your Studio space**

1. [Launch Amazon SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-launch.html#studio-updated-launch-console).

1. Open the Studio UI.

1. Navigate to your space.

1. In the space details, toggle on **Remote Access**.

1. Choose **Run space**.